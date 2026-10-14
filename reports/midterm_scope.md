# Midterm scope, fixed before evaluation

## User decisions, October 14, 2026

Start with discovering or qualifying opportunities. Prioritize new data-center
buildings and substantial physical expansions. Defer equipment fit, purchasing
likelihood and buying-window prediction until after the midterm. Location:
Loudoun County, Virginia, consistent with the original pitch.

## One task

Given a commercial-building permit description, identify whether the filing
documents a new data-center building or a physical addition creating new
data-hall space. Separate clear routine/support work from records requiring
more investigation. This is classification of current public evidence, not a
forecast of buying dates or an estimate of whether a contract can be won.

## Sample

Take the October 13, 2026 snapshot already collected. Restrict to commercial
building permits with application years 2023–2025 from the 160 queried seed parcels.
There are 407 distinct permit IDs before annotation. This is a selected audit
cohort, not every development in Loudoun or a historically available universe.
Do not add unrelated geographies or sources to improve the result.
The cohort has 93 representative parcel IDs; four permits have additional parcel
associations, making 95 parcels across all source associations. A permit is not
automatically a distinct project/building.

Historical application years describe the filings. Their text is the version
retrieved in October 2026, not a verified original application version. This
distinction is harmless for present-day document qualification but prevents
claims of earlier historical sales detection.

## Definitions for desk annotation

Positive: explicit construction of a whole new data-center/data-hall building,
core/shell of such a building, or a structural addition creating new data halls.
An occupied existing campus can contain a qualifying new building.

Negative: fit-out within an existing structure, office-only work, guardhouse,
switching station, mechanical yard, routine alterations, occupancy-only records,
or phased permits whose description explicitly points to an already separate
core/shell parent permit. Large internal fit-outs can need cooling but are
outside this first physical-building scope.

Unknown: insufficient detail, unnamed shell buildings without explicit DC use,
generic phase identifiers, or mixed scope that cannot be resolved from text.
Unknown is not a negative. No RFQ or open supplier-selection window is inferred.

Labels are AI-assisted desk interpretations of county descriptions. They have
not been independently human-reviewed or validated by a construction expert.
The same assistant developed rules and read the descriptions, so this is an
internal agreement check, not a blind model test. Record the reason for every label
and expose the benchmark for user review. Use a model abstention/review route.

## Comparison

Baseline: qualify any commercial-building permit whose county work class is
New Construction or Addition.

Alternative: transparent description rules identifying explicit new DC buildings
and additions, rejecting routine/support records, and returning review when
the evidence is ambiguous. Use only description text and document identifiers
for explanations. No current status, issue date, money, or future outcome enters
the classification rule. Do not tune rules on evaluation errors.

Evaluate precision, recall and F1 for qualified positive records, false positives,
missed positives and review volume. The baseline is a basic listing, not DC Byte.
Exact PermitGUID duplicates are removed, but similar copy/parent filings are not
automatically merged across IDs; building-level deduplication remains future work.

This internal comparison is a preliminary audit, not independent external
validation, calibrated purchasing probabilities, or evidence of sales uplift.

## Commercial claim

The testable benefit is fewer irrelevant or duplicated records in the seller's
investigation queue. Existing competitors already offer project discovery and
prioritization. No unique market feature or superiority over them is claimed.
A future defensible product must demonstrate an additional buying-timing or
seller-specific decision advantage and actual willingness to pay.
