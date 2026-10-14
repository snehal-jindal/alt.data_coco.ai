"""Check evidence joins, date arithmetic, missing outcomes and future-input isolation."""
import csv
import json
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from analyze_early_notice import days,decision,read


class EarlyNotice(unittest.TestCase):
    def test_source_dates_and_ids_are_consistent(self):
        sources={r['source_id']:r for r in read('dated_sources.csv')}
        projects=read('dated_projects.csv')
        self.assertEqual(len(projects),len({r['application_id'] for r in projects}))
        for r in projects:
            self.assertEqual(r['issue_date'],sources[r['source_id']]['document_date'])
        for r in read('dated_events.csv'):
            s=sources[r['source_id']]
            self.assertTrue(s['url'].startswith('https://'))
            if s['document_date']:
                self.assertGreaterEqual(days(r['event_date'],s['document_date']),0)

    def test_signed_lead_times_are_not_clipped(self):
        self.assertEqual(days('2024-01-26','2024-04-10'),75)
        self.assertEqual(days('2024-01-26','2023-05-15'),-256)
        self.assertEqual(days('2023-02-08','2022-10-06'),-125)

    def test_future_outcome_does_not_change_alert(self):
        r=next(r for r in read('dated_projects.csv') if r['application_id']=='LEGI-2023-0048')
        answer=decision(r)
        self.assertEqual(answer,decision({**r,'approval_date':'2099-01-01','current_status':'Cancelled','purchase_probability':'0.99'}))
        approved={**r,'stage_at_issue':'already_approved'}
        self.assertEqual(decision(approved)[0],'later_stage')

    def test_missing_outcomes_remain_unknown(self):
        with (ROOT/'data/processed/early_notice_screening.csv').open(newline='') as f:
            rows=list(csv.DictReader(f))
        for r in rows:
            if not r['approval_date_recovered']:
                self.assertEqual(r['days_from_issue_to_approval'],'')
                self.assertEqual(r['outcome_status'],'not_recovered_not_a_negative')
        summary=json.loads((ROOT/'data/processed/early_notice_summary.json').read_text())
        self.assertEqual(sum(r['coco_action']=='investigate' and not r['approval_date_recovered'] for r in rows),summary['investigation_alerts_with_unknown_outcome_date'])
        self.assertFalse(summary['training_used'])
        self.assertFalse(summary['historical_delivery_timestamps_verified'])


if __name__=='__main__':
    unittest.main()
