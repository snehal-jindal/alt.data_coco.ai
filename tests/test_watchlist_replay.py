import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from replay_watchlist import replay


class WatchlistReplay(unittest.TestCase):
    def test_approval_is_not_used_before_reporting_document(self):
        history,_=replay('2024-04-10')
        belmont=[r for r in history if r['application_id']=='LEGI-2023-0048']
        self.assertEqual(belmont[-1]['action_after_document'],'review_revised_proposal')
        history,_=replay('2024-04-11')
        self.assertEqual([r for r in history if r['application_id']=='LEGI-2023-0048'][-1]['action_after_document'],'later_stage')

    def test_same_document_denial_and_revival_do_not_create_fake_earlier_alerts(self):
        history,_=replay()
        update=[r for r in history if r['application_id']=='LEGI-2023-0048' and r['source_id']=='belmont_2024_03_22']
        self.assertEqual(len(update),1)
        self.assertEqual(update[0]['evidence_document_date'],'2024-03-22')
        self.assertEqual(update[0]['action_after_document'],'review_revised_proposal')
        self.assertEqual(update[0]['reported_event_dates'],'2024-03-13;2024-03-19')

    def test_retrospectively_reported_approval_is_not_backdated(self):
        earlier,_=replay('2024-01-25')
        self.assertFalse(any(r['application_id']=='STMP-2022-0016' for r in earlier))
        later,_=replay('2024-01-26')
        self.assertEqual([r for r in later if r['application_id']=='STMP-2022-0016'][0]['action_after_document'],'later_stage')

    def test_undated_report_is_excluded_and_unchanged_evidence_not_new(self):
        history,excluded=replay()
        self.assertTrue(any(r['source_id']=='permits_2025_07_01_15' for r in excluded))
        self.assertFalse(any(r['source_id']=='permits_2025_07_01_15' for r in history))
        jan=[r for r in history if r['application_id']=='LEGI-2023-0048' and r['evidence_document_date']=='2024-01-08']
        self.assertEqual(jan[0]['changed'],'False')


if __name__=='__main__':
    unittest.main()
