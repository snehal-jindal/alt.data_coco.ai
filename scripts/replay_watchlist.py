"""Replay recovered disclosures by DOCUMENT date, not retrospectively known event date.

Publisher-stated document dates remain availability proxies. This is a workflow
check on curated evidence, not an independently validated historical backtest.
"""
import json
from collections import defaultdict
from analyze_early_notice import ROOT, read, decision, write


def replay(as_of='2024-04-11'):
    sources={r['source_id']:r for r in read('dated_sources.csv')}
    projects=read('dated_projects.csv')
    groups=defaultdict(lambda:{'project':None,'events':[]})
    for row in projects:
        if row['dc_mention_anywhere']=='True':
            groups[(row['issue_date'],row['application_id'],row['source_id'])]['project']=row
    excluded=[]
    for event in read('dated_events.csv'):
        s=sources[event['source_id']]
        if event['event_type']=='industry_news':
            continue  # Independent comparator, not a county workflow update.
        if not s['document_date']:
            excluded.append({'source_id':event['source_id'],'reason':'No recovered document date; event date alone cannot time an alert'})
            continue
        groups[(s['document_date'],event['application_id'],event['source_id'])]['events'].append(event)
    history=[]
    state={}
    for (document_date,app,source_id),group in sorted(groups.items()):
        if document_date>as_of:
            continue
        events=sorted(group['events'],key=lambda x:x['event_date'])
        row=group['project']
        action,reason=decision(row) if row else ('review','Read recovered dated evidence')
        if events:
            last=events[-1]['event_type']
            if last=='planning_approval':
                action,reason='later_stage','Approval is reported in this document; no longer a pre-approval item'
            elif last=='reconsideration_vote':
                action,reason='review_revised_proposal','This release reports denial AND subsequent reconsideration; review the revised proposal'
            elif last=='planning_denial':
                action,reason='pause_review','Recovered document reports denial; investigate implications before pursuing'
            elif last=='county_proposal_notice':
                action,reason='investigate','Recovered document describes a pending DC proposal'
        before=state.get(app,'not_seen_in_recovered_county_sources')
        history.append({'application_id':app,'evidence_document_date':document_date,
            'reported_event_dates':';'.join(e['event_date'] for e in events),
            'source_id':source_id,'source_url':sources[source_id]['url'],
            'previous_action':before,'action_after_document':action,'changed':str(before!=action),
            'reason':reason,'availability_basis':sources[source_id]['date_basis']})
        state[app]=action
    return history,excluded


def main():
    history,excluded=replay()
    write('watchlist_update_replay.csv',history)
    summary={'as_of':'2024-04-11','type':'Workflow replay using recovered document dates; availability assumptions persist',
        'observations':len(history),'undated_sources_excluded':excluded,
        'belmont_updates':[{k:r[k] for k in ('evidence_document_date','reported_event_dates','action_after_document','changed')}
                           for r in history if r['application_id']=='LEGI-2023-0048'],
        'limitations':['Manually curated evidence, not automated document ingestion',
            'Last recovered state is not a verified live project status',
            'No claim of sales lift, first discovery, independent prediction performance or DC Byte superiority']}
    (ROOT/'data/processed/watchlist_update_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))


if __name__=='__main__':
    main()
