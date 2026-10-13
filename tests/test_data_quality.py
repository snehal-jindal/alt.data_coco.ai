"""Meaningful integrity checks on the collected source snapshot."""
import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class DataQuality(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with (ROOT / 'data/processed/permits.csv').open(newline='') as stream:
            cls.rows = list(csv.DictReader(stream))
        cls.summary = json.loads((ROOT / 'data/processed/audit_summary.json').read_text())

    def test_one_row_per_permit(self):
        ids = [r['permit_guid'] for r in self.rows]
        self.assertTrue(all(ids))
        self.assertEqual(len(ids), len(set(ids)))

    def test_invalid_dates_are_visible_and_excluded(self):
        for r in self.rows:
            if r['application_date_invalid'] == 'True':
                self.assertEqual(r['application_date_utc'], '')
                self.assertTrue(r['application_date_source_utc'])
            elif r['application_date_utc']:
                self.assertGreaterEqual(r['application_date_utc'][:4], '1900')

    def test_historical_publication_is_not_invented(self):
        self.assertTrue(all(not r['historical_publication_date'] for r in self.rows))
        self.assertFalse(self.summary['predictive_backtest_ready'])
        self.assertEqual(self.summary['rfq_labels'], 0)

    def test_aggregate_counts_reconcile(self):
        self.assertEqual(len(self.rows), self.summary['unique_parcel_associated_permits'])
        self.assertEqual(sum(r['dc_keyword'] == 'True' for r in self.rows), self.summary['explicit_dc_keyword_permits'])
        self.assertEqual(sum(r['permit_type'] == 'Mechanical (Commercial)' for r in self.rows), self.summary['mechanical_permits_at_seed_parcels'])
        self.assertEqual(sum(r['issue_before_application_day'] == 'True' for r in self.rows), self.summary['issue_before_application_day'])


if __name__ == '__main__':
    unittest.main()
