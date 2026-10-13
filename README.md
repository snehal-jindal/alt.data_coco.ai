# Coco.ai

Alternative-data research for prioritizing data-center cooling opportunities.

**Owner:** Snehal Jindal

## Research question

Can dated planning and design signals identify an upcoming cooling quote
request better than announcement alerts or a simple project-stage ranking?
The original proposed forecast horizon is 180 days, subject to seller validation.

The customer is a cooling-equipment sales team. The intended decision is which
project to investigate next. Workforce intelligence remains future scope.

## Status: source audit completed, prediction feasibility unresolved

On October 13, 2026 we collected official Loudoun County planning and permit
records, audited their schema, removed duplicate permit IDs and produced clean
tables. These are current snapshots with historical event dates. They do not
establish what a seller could have known at each historical date.

No RFQ labels, purchasing forecast, model performance, sales lift or customer
interview results are claimed. See `reports/source_audit.md` for verified counts
and `reports/research_protocol.md` for the evaluation gate.

## Structure

- `scripts/collect.py`: read-only, paginated official-source collection.
- `scripts/audit.py`: deterministic cleaning, deduplication and source audit.
- `tests/test_data_quality.py`: checks against actual cleaned records.
- `data/processed/`: cleaned snapshot tables and audit samples.
- `data/raw/`: original query responses and source metadata, kept locally.
- `reports/`: source findings, definitions and research decisions.

## Reproduce

Python 3.12 or newer. The audit uses the Python standard library only.

```sh
python scripts/collect.py --parcel-followup
python scripts/audit.py
python -m unittest discover -s tests -v
```

The live source changes over time. A fresh collection can produce different
counts. Raw responses retain query parameters, retrieval timestamps and SHA-256
hashes to distinguish snapshots. Reruns must not be presented as the same cohort.

## Data boundaries

A permit is not a project or a purchase. A parcel is not necessarily a single
building. Current status and edited descriptions cannot be used as historical
features without publication/version evidence. Blank outcomes are not negatives.

Source government records retain their original rights and disclaimers.
No blanket license is asserted for collected data or documents. Contact names
and emails are intentionally excluded from collected record fields.
