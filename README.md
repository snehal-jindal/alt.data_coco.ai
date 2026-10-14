# Coco.ai

Alternative-data research for a cooling supplier's project-investigation queue.

**Owner:** Snehal Jindal

## Midterm: one task, one county

Identify filings documenting new data-center buildings or substantial physical
data-hall additions in **Loudoun County, Virginia**. Compare a simple county
work-class filter with transparent description rules.

This implements the first qualification step of the original sales-intelligence
idea. It does not estimate buying dates, win probability, equipment requirements
or earnings. Workforce intelligence remains future scope.

## Completed and preliminary results

Official records were collected October 13, 2026, cleaned and deduplicated.
The focused cohort has 407 commercial-building filings applied for in 2023–2025.
Each has an AI-assisted desk label, source evidence and reason. Executable code
compares a county-category baseline with one rules classifier and a review route.

Across resolved desk labels, baseline precision is 63.0%; rule precision is 87.5%.
Rules qualify 28 of 29 desk-positive filings automatically, make 4 clear false
alerts and send 80 filings to review. **In the 2025 subset, baseline precision is
better: 83.3% versus 76.9%.** Aggregate improvement is not consistent by year.

These are internal agreement figures, **not independent test performance**.
The same AI assistant interpreted descriptions and developed rules. Labels need
independent human/expert validation. Current edited text cannot establish what
was knowable in earlier years. Filings are not necessarily distinct buildings,
live leads or purchases. Review-work savings and commercial alpha are unproven.

Read [the plain-English walkthrough](reports/midterm_walkthrough.md) first.
[The scope](reports/midterm_scope.md) defines the task. The older
[research protocol](reports/research_protocol.md) concerns deferred buying-window
prediction; its suggested 180-day horizon was unvalidated.

## Structure

- `scripts/collect.py`: read-only, paginated official-source collection.
- `scripts/audit.py`: deterministic cleaning, deduplication and source audit.
- `scripts/qualify.py`: focused cohort, baseline and readable description rules.
- `scripts/evaluate_qualification.py`: agreement metrics, year breakdown and errors.
- `tests/test_data_quality.py`: checks against actual cleaned records.
- `data/processed/`: cleaned snapshot tables and audit samples.
- `data/raw/`: original query responses and source metadata, kept locally.
- `reports/`: source findings, definitions and research decisions.

## Reproduce the frozen midterm audit

Python 3.12+, standard library only. Committed processed data is sufficient.

```sh
python scripts/qualify.py
python scripts/evaluate_qualification.py
python -m unittest discover -s tests -v
```

Outputs in `data/processed/` include full predictions, qualified filings, a review
queue, comparison, exposed errors and metrics. `qualification_annotations.csv`
contains initial desk labels and original text for independent review.

Source recollection is separate:

```sh
python scripts/collect.py --parcel-followup
python scripts/audit.py
```

The live source changes. Collection replaces local raw files and can change the
cohort. Save a dated copy first; do not reuse frozen annotations on changed data.
Raw responses retain query parameters, timestamps and hashes locally. They are
not committed to this repository.

## Data boundaries

A permit is not a project or a purchase. A parcel is not necessarily a single
building. Current status and edited descriptions cannot be used as historical
features without publication/version evidence. Blank outcomes are not negatives.

Source government records retain their original rights and disclaimers.
No blanket license is asserted for collected data or documents. Contact names
and emails are intentionally excluded from collected record fields.
