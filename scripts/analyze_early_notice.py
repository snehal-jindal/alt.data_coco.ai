"""Dated-document replay with manually curated source facts, not trained ML.

Main endpoint: planning approval. No RFQ, construction-start or cooling purchase
is inferred. Missing later dates remain unknown. Publisher dates are explicit
availability proxies, not independently verified web posting timestamps.
"""
import csv
import hashlib
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURATED = ROOT / 'data/curated'
OUT = ROOT / 'data/processed'


def read(name):
    with (CURATED / name).open(newline='') as f:
        return list(csv.DictReader(f))


def days(start, end):
    return (date.fromisoformat(end)-date.fromisoformat(start)).days


def decision(row):
    # These three fields were desk-extracted ONLY from the dated newsletter.
    # Outcomes, present statuses, monetary values and later permits are not read.
    if row['scope_at_issue'] == 'new_dc_buildings':
        if row['stage_at_issue'] == 'pending':
            return 'investigate', 'Explicit proposed DC building; planning decision pending in this issue'
        if row['stage_at_issue'] == 'already_approved':
            return 'later_stage', 'Approval already reported; not a pre-approval alert'
        return 'review', 'DC scope recognized; historical stage unresolved'
    if row['scope_at_issue'] == 'mixed_land_use' and row['dc_mention_anywhere'] == 'True':
        return 'review', 'Mixed land-use/DC permission; distinct building proposal unclear'
    return 'out_of_scope', 'Primary application scope is not a new DC building'


def write(name, rows):
    with (OUT / name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)


def main():
    projects, events, sources = read('dated_projects.csv'), read('dated_events.csv'), read('dated_sources.csv')
    source_map={r['source_id']:r for r in sources}
    approvals={r['application_id']:r for r in events if r['event_type']=='planning_approval'}
    results=[]
    for row in projects:
        action,reason=decision(row)
        outcome=approvals.get(row['application_id'])
        results.append({**row,'keyword_baseline_alert':row['dc_mention_anywhere'],
            'coco_action':action,'decision_reason':reason,
            'approval_date_recovered':outcome['event_date'] if outcome else '',
            'approval_source_id':outcome['source_id'] if outcome else '',
            'days_from_issue_to_approval':days(row['issue_date'],outcome['event_date']) if outcome else '',
            'outcome_status':'date_recovered' if outcome else 'not_recovered_not_a_negative',
            'source_url':source_map[row['source_id']]['url'],
        })
    write('early_notice_screening.csv',results)
    write('early_notice_investigation_queue.csv',[r for r in results if r['coco_action']=='investigate'])
    belmont=[r for r in events if r['application_id']=='LEGI-2023-0048']
    approval=approvals['LEGI-2023-0048']['event_date']
    notices=[r['event_date'] for r in belmont if r['event_type']=='county_proposal_notice']
    news=min(r['event_date'] for r in belmont if r['event_type']=='industry_news')
    timeline=[]
    for r in sorted(events,key=lambda r:(r['application_id'],r['event_date'])):
        timeline.append({**r,'evidence_document_date':source_map[r['source_id']]['document_date'],
                         'date_basis':source_map[r['source_id']]['date_basis'],
                         'source_url':source_map[r['source_id']]['url']})
    write('early_notice_timeline.csv',timeline)
    summary={
        'study':'Small retrospectively curated dated-document pilot; NOT independent predictive validation',
        'geography':'Ashburn District in Loudoun County Virginia',
        'cohort_document_date':'2024-01-26','endpoint':'planning approval; board rezoning and administrative site-plan approvals distinguished in notes',
        'training_used':False,'historical_delivery_timestamps_verified':False,
        'curated_inputs':'AI-assisted human-readable extraction of issue-era scope and stage; independent review pending',
        'screened_entries':len(results),
        'keyword_baseline_alerts':sum(r['keyword_baseline_alert']=='True' for r in results),
        'investigate':sum(r['coco_action']=='investigate' for r in results),
        'review':sum(r['coco_action']=='review' for r in results),
        'later_stage':sum(r['coco_action']=='later_stage' for r in results),
        'out_of_scope':sum(r['coco_action']=='out_of_scope' for r in results),
        'investigation_alerts_with_recovered_later_approval':sum(r['coco_action']=='investigate' and r['approval_date_recovered']!='' and int(r['days_from_issue_to_approval'])>0 for r in results),
        'investigation_alerts_with_unknown_outcome_date':sum(r['coco_action']=='investigate' and r['approval_date_recovered']=='' for r in results),
        'belmont':{
            'fixed_issue_notice':'2024-01-26','approval_date':approval,
            'fixed_issue_lead_days':days('2024-01-26',approval),
            'earliest_recovered_county_notice':min(notices),
            'earlier_county_notice_lead_days':days(min(notices),approval),
            'recovered_industry_news_date':news,'industry_news_lead_days':days(news,approval),
            'county_notice_advantage_days_vs_news':days(min(notices),news),
            'fixed_issue_advantage_days_vs_news':days('2024-01-26',news),
            'initial_denial_then_reconsideration':True,
            'interpretation':'Notice precedes planning approval but recovered industry news precedes all recovered county notices. No news-timing advantage demonstrated.',
        },
        'vantage_control':{'issue_to_prior_approval_days':days('2024-01-26',approvals['STMP-2022-0016']['event_date']),
            'interpretation':'Already-approved control; negative lead is preserved and not mislabeled early'},
        'limitations':['Selected newsletter issue and tiny cohort; no countywide recall estimate',
            'Manual feature extraction and source selection after outcomes were knowable; not blind testing',
            'Publisher-stated dates used as historical-availability proxies',
            'Two proposed-project approval dates not recovered; not failures and not proven pending through today',
            'Prior news may have been edited; first-version existence/content not independently archived',
            'Planning approval is not construction start or an open cooling procurement window',
            'No empirical DC Byte timing/coverage comparison; no measured sales or time-saving advantage'],
        'input_sha256':{n:hashlib.sha256((CURATED/n).read_bytes()).hexdigest() for n in ('dated_projects.csv','dated_events.csv','dated_sources.csv')},
    }
    (OUT/'early_notice_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))


if __name__=='__main__':
    main()
