"""Read-only collector for Loudoun County's public ArcGIS services.

Stores query parameters, retrieval times, response hashes and server counts.
No login, tokens, personal contact fields or write operations are used.
"""
import argparse
import hashlib
import json
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://logis.loudoun.gov/gis/rest/services/'
SOURCES = {
    'plans': BASE + 'Projects/LOLA_DATA/MapServer/0',
    'issued': BASE + 'LMARC/LandMARC_Permits/MapServer/1',
    'submitted': BASE + 'LMARC/LandMARC_Permits/MapServer/2',
}
PLAN_FIELDS = 'OBJECTID,PlanGuid,PlanNumber,PlanApplicationDate,PlanType,PlanStatus,PlanDescription,PlanName'
PERMIT_FIELDS = 'ID,APPLYDATE,PermitGUID,PermitNumber,PermitType,PermitStatus,ParcelGUID,ParcelPIN,DataSnapshot,ADDRESSLINE1,CITY,DESCRIPTION,PermitWorkClass,ISSUEDATE,FINALIZEDATE,SQUAREFEET,VALUE'
DC_PERMITS = "UPPER(DESCRIPTION) LIKE '%DATA CENTER%' OR UPPER(DESCRIPTION) LIKE '%DATA CENTRE%' OR UPPER(DESCRIPTION) LIKE '%DATACENTER%'"
DC_PLANS = "UPPER(PlanDescription) LIKE '%DATA CENTER%' OR UPPER(PlanDescription) LIKE '%DATA CENTRE%' OR UPPER(PlanDescription) LIKE '%DATACENTER%' OR UPPER(PlanName) LIKE '%DATA CENTER%'"


def request_json(url, params):
    query = urllib.parse.urlencode(params)
    headers = {'User-Agent': 'CocoAcademicResearch/0.1'}
    if len(url + '?' + query) > 1800:
        # ArcGIS supports POST for read-only queries. Avoid IIS URL-length
        # limits on the bounded parcel IN clause; this does not write data.
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        request = urllib.request.Request(url, data=query.encode(), headers=headers)
    else:
        request = urllib.request.Request(url + '?' + query, headers=headers)
    # Only transient server/network errors are retried. Authentication/access
    # errors are stop conditions, never bypassed.
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=45) as response:
                raw = response.read()
            result = json.loads(raw)
            if 'error' in result:
                raise RuntimeError(json.dumps(result['error']))
            return result, hashlib.sha256(raw).hexdigest()
        except urllib.error.HTTPError as exc:
            if exc.code < 500 or attempt == 2:
                raise
            time.sleep(attempt + 1)
    raise RuntimeError('unreachable')


def collect(name, where, suffix):
    url = SOURCES[name]
    folder = ROOT / 'data' / 'raw'
    folder.mkdir(parents=True, exist_ok=True)
    metadata, metadata_hash = request_json(url, {'f': 'json'})
    (folder / (name + '_metadata.json')).write_text(json.dumps(metadata, indent=2))
    count, _ = request_json(url + '/query', {'f': 'json', 'where': where, 'returnCountOnly': 'true'})
    oid = metadata.get('objectIdField') or metadata.get('objectIdFieldName')
    if not oid:
        oid = next(f['name'] for f in metadata['fields'] if f['type'] == 'esriFieldTypeOID')
    fields = PLAN_FIELDS if name == 'plans' else PERMIT_FIELDS
    records, hashes, offset = [], [], 0
    while True:
        params = {'f': 'json', 'where': where, 'outFields': fields, 'returnGeometry': 'false',
                  'orderByFields': oid, 'resultOffset': offset, 'resultRecordCount': 1000}
        page, digest = request_json(url + '/query', params)
        batch = page.get('features', [])
        records.extend(f['attributes'] for f in batch)
        hashes.append({'offset': offset, 'sha256': digest, 'query': params})
        if not page.get('exceededTransferLimit'):
            break
        if not batch:
            raise RuntimeError('Pagination stalled')
        offset += len(batch)
        time.sleep(.2)
    if len(records) != count['count']:
        raise RuntimeError(f"Count mismatch: {len(records)} vs {count['count']}")
    if len({r[oid] for r in records}) != len(records):
        raise RuntimeError('Duplicated server object IDs')
    payload = {'source': url, 'retrieved_at_utc': datetime.now(timezone.utc).isoformat(),
               'where': where, 'fields': fields.split(','), 'server_count': count['count'],
               'metadata_sha256': metadata_hash, 'pages': hashes, 'records': records}
    path = folder / (name + '_' + suffix + '.json')
    path.write_text(json.dumps(payload, indent=2))
    print(json.dumps({'file': str(path), 'records': len(records)}), flush=True)
    return records


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--parcel-followup', action='store_true')
    parser.add_argument('--only-followup', action='store_true')
    args = parser.parse_args()
    if args.only_followup:
        issued = json.loads((ROOT / 'data/raw/issued_dc.json').read_text())['records']
        submitted = json.loads((ROOT / 'data/raw/submitted_dc.json').read_text())['records']
    else:
        collect('plans', DC_PLANS, 'dc')
        issued = collect('issued', DC_PERMITS, 'dc')
        submitted = collect('submitted', DC_PERMITS, 'dc')
    if args.parcel_followup or args.only_followup:
        pins = sorted({r['ParcelPIN'] for r in issued + submitted if r.get('ParcelPIN')})
        # One bounded query covers all records at identified data-center parcels.
        # The resulting rows are parcel-associated, not automatically DC rows.
        where = 'ParcelPIN IN (' + ','.join("'" + p.replace("'", "''") + "'" for p in pins) + ')'
        if pins:
            collect('issued', where, 'parcel_followup')
            collect('submitted', where, 'parcel_followup')


if __name__ == '__main__':
    main()
