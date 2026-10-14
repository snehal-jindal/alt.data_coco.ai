import csv
import json
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]


class SignalQuality(unittest.TestCase):
    def test_followup_matches_all_shortlisted_projects(self):
        with (ROOT/'data/processed/early_notice_investigation_queue.csv').open(newline='') as f:
            expected={r['application_id'] for r in csv.DictReader(f)}
        with (ROOT/'data/curated/quality_followup.csv').open(newline='') as f:
            rows=list(csv.DictReader(f))
        self.assertEqual({r['application_id'] for r in rows},expected)
        self.assertEqual(len(rows),len(expected))

    def test_unresolved_physical_outcomes_do_not_become_zero_accuracy(self):
        s=json.loads((ROOT/'data/processed/signal_quality_audit.json').read_text())
        self.assertEqual(s['physical_construction_outcomes_resolved'],0)
        self.assertEqual(s['completion_outcomes_resolved'],0)
        self.assertIsNone(s['signal_precision'])
        self.assertIsNone(s['signal_recall'])
        self.assertIsNone(s['completion_success_rate'])


if __name__=='__main__':
    unittest.main()
