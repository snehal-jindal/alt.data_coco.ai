# Coco.ai

A small, transparent study of public-record notice for data-center suppliers.
**Owner:** Snehal Jindal

## Current midterm question

Can dated public documents identify proposed new data-center buildings before
planning approval, and do they add timing value over ordinary public information?

The customer hypothesis is a cooling supplier deciding which project to investigate.
Planning approval is an observable development milestone, not a verified buying
window. Purchasing probabilities, equipment fit and RFQ timing remain deferred.

## Result: advance notice, no demonstrated discovery advantage

A fixed January 26, 2024 Ashburn District newsletter contains 16 application
entries. A broad DC-mention baseline flags 6; our manually prepared scope/stage
rules produce 3 investigation items, 1 review item and 1 later-stage DC item.

For Belmont Innovation Campus, the fixed issue is 75 days before April 10, 2024
approval. An earlier recovered county notice is 427 days before approval.
**Recovered industry news is 552 days before approval: 125 days earlier than that
county notice.** No news-timing advantage is demonstrated.

Vantage VA3 was already approved 256 days before the fixed issue. Two proposed
projects lack recovered later approval dates and remain unknown, not failures.
The keyword baseline finds all 3 investigation items on the same issue date.
Filtering is implemented; incremental discovery timing and sales value are unproven.

## Read first

- [Plain-English explanation](reports/midterm_walkthrough.md): complete current story.
- [Current presentation structure](reports/midterm_slide_structure.md): twelve
  slides for eight minutes, speaker notes, sources and professor-requirement mapping;
  no slide deck created. The earlier six-minute brief is retained as background.
- [Source register](data/curated/dated_sources.csv): links, dates and their limits.
- [Results](data/processed/early_notice_summary.json): reproducible numbers.

## Reproduce the current pilot

Python 3.12+, standard library only:

    python scripts/analyze_early_notice.py
    python scripts/replay_watchlist.py
    python scripts/audit_signal_quality.py
    python -m unittest discover -s tests -v

Inputs are AI-assisted manual fact extractions in data/curated/. They are NOT an
automatically scraped historical dataset or independently human-validated labels.
The script outputs a screening table, investigation queue, timeline and summary
in data/processed/early_notice_*.

There is no statistical training or untouched test set. Publisher-stated issue
dates are historical-availability proxies; original delivery/posting timestamps
and first versions have not been independently verified. Original document bytes
could not be downloaded from this environment and are not archived here.
Seventeen code/data checks pass; that does not validate commercial performance.

## Additional midterm checks

The disclosure-date replay changes Belmont from investigate to review of the
revised proposal to approval reported. It uses the date of the reporting document,
not an earlier vote date the document describes. Repeated notices are not new discoveries.

Physical-outcome follow-up now covers all three investigation items. Belmont has
a contractor-reported scope, Landbay KK has reported conditional site-plan approval,
and CyrusOne remains a described proposal in recovered sources. No construction
start or completion is independently verified. That is unresolved evidence, not
zero successful projects. Conditional approval is not pooled with full approval.

## What remains

Independently review source facts, recover unresolved outcomes, evaluate unseen
dated sources and confirm a useful seller decision. DC Byte already advertises
early alerts, segmentation and supplier prioritization; no feature gap or
superiority over it is established. Continue, change the supported decision or
pivot according to evidence rather than force a success claim.

## Earlier supporting work

The October 13 county collection and October 14 407-permit qualification exercise
are preserved as background. They classify current descriptions and do not prove
historical early detection. Read [the background explanation](reports/qualification_walkthrough.md)
and [source audit](reports/source_audit.md) if needed. They are not a second current
model or a statistical training set for the dated pilot.

Live collection scripts remain available, but recollecting replaces local raw
responses and can change the cohort. Save dated copies and re-annotate changed
text rather than reuse frozen labels.

A permit is not a purchase; a parcel is not necessarily one building. Government
records retain their original rights/disclaimers. No blanket data license is
asserted. Contact fields were excluded from the original API collection.
