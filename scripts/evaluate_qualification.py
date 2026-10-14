"""Internal agreement audit against AI-assisted desk labels, not blind validation."""
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path
from qualify import ROOT, INPUT, baseline, classify, cohort, write_csv


def metrics(rows, method):
    known = [r for r in rows if r['desk_label'] != 'unknown']
    tp = sum(r['desk_label'] == 'positive' and r[method] == 'qualified' for r in known)
    fp = sum(r['desk_label'] == 'negative' and r[method] == 'qualified' for r in known)
    fn = sum(r['desk_label'] == 'positive' and r[method] != 'qualified' for r in known)
    precision = tp / (tp + fp) if tp + fp else None
    recall = tp / (tp + fn) if tp + fn else None
    f1 = 2 * precision * recall / (precision + recall) if precision is not None and recall is not None and precision + recall else None
    accepted = [r for r in rows if r[method] == 'qualified']
    return {
        'filings': len(rows), 'desk_labels': dict(Counter(r['desk_label'] for r in rows)),
        'qualified_filings': len(accepted), 'true_positives': tp, 'false_positives': fp,
        'missed_desk_positives': fn, 'precision_on_resolved_labels': precision,
        'recall_on_desk_positives': recall, 'f1_on_resolved_labels': f1,
        'qualified_but_unknown_label': sum(r['desk_label'] == 'unknown' for r in accepted),
        'desk_positive_share_of_entire_qualified_queue': tp / len(accepted) if accepted else None,
        'review_filings': sum(r[method] == 'review' for r in rows),
        'desk_positives_in_review': sum(r['desk_label'] == 'positive' and r[method] == 'review' for r in rows),
        'desk_negatives_in_review': sum(r['desk_label'] == 'negative' and r[method] == 'review' for r in rows),
        'unknown_labels_rejected': sum(r['desk_label'] == 'unknown' and r[method] == 'out_of_scope' for r in rows),
        'decisions': dict(Counter(r[method] for r in rows)),
    }


def main():
    with (ROOT / 'data/processed/qualification_annotations.csv').open(newline='') as f:
        labels = {r['permit_guid']: r for r in csv.DictReader(f)}
    rows = []
    for r in cohort():
        label = labels[r['permit_guid']]
        if label['annotation_evidence'] != r['description_current']:
            raise ValueError('Source description changed since annotation; independent relabeling is required.')
        decision, reason = classify(r['description_current'])
        rows.append({
            'permit_guid': r['permit_guid'], 'permit_number': r['permit_number'],
            'application_year': r['application_day_local'][:4], 'parcel_pin': r['parcel_pin'],
            'desk_label': label['desk_label'], 'baseline': baseline(r), 'rules': decision,
            'rule_reason': reason, 'annotation_reason': label['annotation_reason'],
            'description_current': r['description_current'],
        })
    if len(labels) != len(rows):
        raise ValueError('Annotations and selected cohort must match exactly; do not reuse labels on a new snapshot.')
    summary = {
        'task': 'New physical DC-building filing qualification',
        'evaluation_type': 'Internal agreement audit; AI-assisted labels; rules and labels share a researcher; NOT blind or independent test performance',
        'statistical_training': False, 'independent_test_set': False,
        'geography': 'Loudoun County, Virginia', 'application_years': [2023,2024,2025],
        'text_retrieval_date_utc': '2026-10-13',
        'source_input_sha256': hashlib.sha256(INPUT.read_bytes()).hexdigest(),
        'annotation_sha256': hashlib.sha256((ROOT / 'data/processed/qualification_annotations.csv').read_bytes()).hexdigest(),
        'rules_sha256': hashlib.sha256((ROOT / 'scripts/qualify.py').read_bytes()).hexdigest(),
        'cohort_parcels': len({r['parcel_pin'] for r in rows}),
        'all_years': {m: metrics(rows,m) for m in ('baseline','rules')},
        'by_application_year': {y: {m: metrics([r for r in rows if r['application_year']==y],m) for m in ('baseline','rules')} for y in ('2023','2024','2025')},
        'limitations': ['Selected DC-associated parcels, not countywide discovery evaluation',
                        'Current edited descriptions, not historical initial-publication versions',
                        'AI-assisted labels need independent construction/seller review',
                        'Repeated campus/phase records are correlated',
                        'No RFQ, buying probability, lead-time, sales conversion or competitor benchmark'],
    }
    write_csv(ROOT / 'data/processed/qualification_comparison.csv', rows)
    errors = [r for r in rows if (r['desk_label'] == 'negative' and r['rules'] == 'qualified')
              or (r['desk_label'] == 'positive' and r['rules'] != 'qualified')
              or (r['desk_label'] == 'unknown' and r['rules'] != 'review')]
    write_csv(ROOT / 'data/processed/qualification_errors.csv', errors)
    (ROOT / 'data/processed/qualification_metrics.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary['all_years'],indent=2))
    print('Errors / unresolved decisions:', len(errors))


if __name__ == '__main__':
    main()
