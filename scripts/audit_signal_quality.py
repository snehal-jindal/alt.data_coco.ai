"""Report evidence completeness for physical progression, not invented accuracy."""
import csv
import json
from analyze_early_notice import ROOT


def main():
    with (ROOT/'data/curated/quality_followup.csv').open(newline='') as f:
        rows=list(csv.DictReader(f))
    for r in rows:
        if r['physical_construction_verified'] not in {'yes','no','unknown'}:
            raise ValueError('Invalid physical-construction evidence status')
        if r['completion_verified'] not in {'yes','no','unknown'}:
            raise ValueError('Invalid completion evidence status')
    summary={
        'checked_as_of':'2026-10-14','shortlisted_projects_checked':len(rows),
        'physical_construction_outcomes_resolved':sum(r['physical_construction_verified']!='unknown' for r in rows),
        'completion_outcomes_resolved':sum(r['completion_verified']!='unknown' for r in rows),
        'planning_or_contractor_evidence':[{'project':r['project_name'],'evidence':r['reported_progress'],'limit':r['limitation']} for r in rows],
        'signal_precision':None,'signal_recall':None,'completion_success_rate':None,
        'conclusion':'Physical-outcome quality remains unvalidated. Zero resolved outcomes is evidence coverage, NOT zero successful projects.',
        'next_test':'Obtain matched dated contractor/developer construction evidence or official completion/occupancy records, follow shortlisted and comparison candidates to the same cutoff, retain unresolved cases, then estimate quality with sample size and uncertainty.',
    }
    (ROOT/'data/processed/signal_quality_audit.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))


if __name__=='__main__':
    main()
