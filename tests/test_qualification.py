"""Cohort, metric and provenance checks; not external validation."""
import csv
import hashlib
import json
import sys
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from evaluate_qualification import metrics
from qualify import cohort


class QualificationAudit(unittest.TestCase):
    def test_annotation_coverage_and_source_evidence(self):
        source = {r['permit_guid']: r for r in cohort()}
        with (ROOT / 'data/processed/qualification_annotations.csv').open(newline='') as f:
            labels = list(csv.DictReader(f))
        self.assertEqual(len(labels), len(source))
        self.assertEqual({r['permit_guid'] for r in labels}, set(source))
        for r in labels:
            self.assertIn(r['desk_label'], {'positive','negative','unknown'})
            self.assertEqual(r['annotation_evidence'], source[r['permit_guid']]['description_current'])
            self.assertEqual(r['human_reviewed'], 'False')

    def test_unknown_is_not_negative_and_review_is_not_recall_credit(self):
        fixture = [
            {'desk_label':'positive','rules':'qualified'},
            {'desk_label':'positive','rules':'review'},
            {'desk_label':'negative','rules':'qualified'},
            {'desk_label':'unknown','rules':'qualified'},
        ]
        result = metrics(fixture,'rules')
        self.assertEqual(result['false_positives'],1)
        self.assertEqual(result['qualified_but_unknown_label'],1)
        self.assertEqual(result['precision_on_resolved_labels'],.5)
        self.assertEqual(result['recall_on_desk_positives'],.5)
        self.assertEqual(result['desk_positive_share_of_entire_qualified_queue'],1/3)

    def test_saved_metrics_reconcile_and_match_inputs(self):
        summary=json.loads((ROOT / 'data/processed/qualification_metrics.json').read_text())
        with (ROOT / 'data/processed/qualification_comparison.csv').open(newline='') as f:
            rows=list(csv.DictReader(f))
        for method in ('baseline','rules'):
            self.assertEqual(summary['all_years'][method],metrics(rows,method))
        for y in ('2023','2024','2025'):
            for method in ('baseline','rules'):
                self.assertEqual(summary['by_application_year'][y][method],metrics([r for r in rows if r['application_year']==y],method))
        for key,path in [('source_input_sha256','data/processed/permits.csv'),
                         ('annotation_sha256','data/processed/qualification_annotations.csv'),
                         ('rules_sha256','scripts/qualify.py')]:
            self.assertEqual(summary[key],hashlib.sha256((ROOT / path).read_bytes()).hexdigest())
        self.assertFalse(summary['independent_test_set'])


if __name__ == '__main__':
    unittest.main()
