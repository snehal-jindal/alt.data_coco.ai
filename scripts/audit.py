"""Produce a deterministic source audit. Does not train a predictive model."""
import csv
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / 'data' / 'raw'
OUT = ROOT / 'data' / 'processed'
OUT.mkdir(parents=True, exist_ok=True)


def iso(value):
    if value is None:
        return ''
    return datetime.fromtimestamp(value / 1000, timezone.utc).isoformat()


def application_date(value):
    date = iso(value)
    # 1753 is observed in this feed and cannot represent a data-center permit.
    # Preserve the source value separately rather than silently dropping it.
    return date if date and date[:4] >= '1900' else ''


def local_day(date):
    return datetime.fromisoformat(date).astimezone(ZoneInfo('America/New_York')).date() if date else None


def load(name):
    return json.loads((RAW / name).read_text())


def write_csv(name, records):
    if not records:
        return
    with (OUT / name).open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)


def main():
    plans = load('plans_dc.json')
    # Multiple GIS polygons may refer to one application. GUID is the entity
    # key, not the GIS polygon's object ID or the possibly repeated site name.
    unique_plans = {}
    conflicts = []
    for row in plans['records']:
        key = row['PlanGuid'] or row['PlanNumber']
        if key in unique_plans:
            before = {k: v for k, v in unique_plans[key].items() if k != 'OBJECTID'}
            after = {k: v for k, v in row.items() if k != 'OBJECTID'}
            if before != after:
                conflicts.append(key)
        else:
            unique_plans[key] = row
    plan_rows = [{
        'plan_guid': r['PlanGuid'], 'plan_number': r['PlanNumber'],
        'plan_name': r['PlanName'], 'application_date_utc': iso(r['PlanApplicationDate']),
        'plan_type': r['PlanType'], 'current_status': r['PlanStatus'],
        'description_current': r['PlanDescription'], 'retrieved_at_utc': plans['retrieved_at_utc'],
        'historical_publication_date': '', 'source_url': plans['source'],
    } for _, r in sorted(unique_plans.items())]
    write_csv('plans.csv', plan_rows)

    permits = {}
    conflicts_permits = []
    for file in ('issued_dc.json', 'submitted_dc.json', 'issued_parcel_followup.json', 'submitted_parcel_followup.json'):
        if not (RAW / file).exists():
            continue
        payload = load(file)
        for r in payload['records']:
            key = r['PermitGUID']
            clean = {
                'permit_guid': key, 'permit_number': r['PermitNumber'],
                'parcel_pin': r['ParcelPIN'], 'house_number': r['ADDRESSLINE1'], 'city': r['CITY'],
                'permit_type': r['PermitType'], 'work_class': r['PermitWorkClass'],
                'current_status': r['PermitStatus'], 'application_date_utc': application_date(r['APPLYDATE']),
                'application_date_source_utc': iso(r['APPLYDATE']),
                'application_date_invalid': bool(r['APPLYDATE'] is not None and not application_date(r['APPLYDATE'])),
                'issue_date_utc': iso(r['ISSUEDATE']), 'finalize_date_utc': iso(r['FINALIZEDATE']),
                'snapshot_date_utc': iso(r['DataSnapshot']),
                'description_current': r['DESCRIPTION'], 'square_feet': r['SQUAREFEET'],
                'declared_value': r['VALUE'],
                'dc_keyword': bool(re.search(r'data\s*cent(?:er|re)', r['DESCRIPTION'] or '', re.I)),
                'retrieved_at_utc': payload['retrieved_at_utc'], 'historical_publication_date': '',
                'source_url': payload['source'],
            }
            clean['issue_before_application_day'] = bool(clean['application_date_utc'] and clean['issue_date_utc'] and local_day(clean['issue_date_utc']) < local_day(clean['application_date_utc']))
            if key in permits:
                # Cross-feed snapshot conflicts are reported, not averaged.
                check = ('application_date_utc','issue_date_utc','description_current','permit_type','current_status')
                if any(permits[key][k] != clean[k] for k in check):
                    conflicts_permits.append({'permit_guid': key, 'feed': file})
                if file.startswith('issued'):
                    permits[key] = clean
            else:
                permits[key] = clean
    rows = [permits[k] for k in sorted(permits)]
    write_csv('permits.csv', rows)
    keywords = [r for r in rows if r['dc_keyword']]
    mechanical = [r for r in rows if 'mechanical' in (r['permit_type'] or '').lower()]
    ranges = {}
    for field in ('application_date_utc','issue_date_utc','snapshot_date_utc'):
        dates = sorted(r[field] for r in rows if r[field])
        ranges[field] = {'min': dates[0] if dates else None, 'max': dates[-1] if dates else None,
                         'missing': sum(not r[field] for r in rows)}
    summary = {
        'plan_gis_rows': len(plans['records']), 'unique_plan_applications': len(plan_rows),
        'plan_duplicate_rows': len(plans['records']) - len(plan_rows),
        'plan_conflicting_guids': sorted(set(conflicts)),
        'unique_parcel_associated_permits': len(rows), 'explicit_dc_keyword_permits': len(keywords),
        'parcels_with_dc_keyword': len({r['parcel_pin'] for r in keywords if r['parcel_pin']}),
        'mechanical_permits_at_seed_parcels': len(mechanical),
        'mechanical_with_dc_keyword': sum(r['dc_keyword'] for r in mechanical),
        'invalid_application_dates': sum(r['application_date_invalid'] for r in rows),
        'issue_before_application_timestamp': sum(bool(r['application_date_utc'] and r['issue_date_utc'] and r['issue_date_utc'] < r['application_date_utc']) for r in rows),
        'issue_before_application_day': sum(r['issue_before_application_day'] for r in rows),
        'permit_cross_feed_conflicts': conflicts_permits,
        'permit_types': dict(Counter(r['permit_type'] for r in rows)),
        'plan_types': dict(Counter(r['plan_type'] for r in plan_rows)),
        'date_ranges': ranges,
        'rfq_labels': 0, 'verified_historical_publication_dates': 0,
        'predictive_backtest_ready': False,
        'warning': 'Current snapshots. Parcel association is not building-level matching. Permit events are not purchases.',
    }
    # Stable chronological examples for manual audit, not an outcome-selected
    # evaluation cohort. Do not treat these ten records as ten unique projects.
    sample = sorted(keywords, key=lambda r: (r['application_date_utc'],r['permit_number']))[:10]
    write_csv('manual_audit_sample.csv', sample)
    write_csv('mechanical_audit_sample.csv', sorted([r for r in mechanical if r['dc_keyword']], key=lambda r:r['permit_number'])[:10])
    (OUT / 'audit_summary.json').write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
