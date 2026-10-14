# Research protocol

## Current scope, October 14 update

The dated-document pilot is the primary midterm analysis. It compares a fixed
January 26, 2024 newsletter's proposal flags with planning-approval events and
recovered news coverage. It uses manually curated issue-era facts and simple
rules. It is not statistical training or an independent predictive test.

The result does not establish incremental discovery timing over news. Missing
approval dates remain unknown. Approval is a development milestone, not a verified
cooling purchasing window. See `midterm_walkthrough.md` for current conclusions.

The rest of this document preserves the earlier purchasing-forecast proposal.
Its 180-day horizon and historical-cohort plan are deferred, not current claims.
The earlier reference to 140 seed parcels means representative cleaned parcel
IDs; 160 parcels were actually queried. Neither set is a historical at-risk universe.

## Continuity with the original pitch

Keep the cooling seller, Loudoun geography, prioritization decision and
comparison with simple baselines. The earlier 180-day horizon was unvalidated. Do not expand
into workforce prediction, earnings forecasting or a generic lead-generation app.

## Decisions supported by the first audit

1. Official project/permit sources are accessible through public read-only APIs.
2. Description-only discovery misses potentially relevant mechanical records.
3. Historical dates exist, but publication dates and historical description
   versions have not been recovered.
4. Quote requests and open supplier-selection windows are not in the audited
   schemas. No purchase labels are available yet.

## Gate before modeling

For a sample of identifiable buildings/phases, establish a timeline using dated
archived records. Confirm an outcome definition, coverage of eligible projects,
at-risk dates and independent follow-up. A sales outcome requires supplier
records or other direct evidence. A permit cannot substitute for a purchase.

If purchasing labels remain unavailable, propose an explicit narrower study:
forecast an observable construction milestone. Name that milestone and its
commercial limitations before estimating any model. Do not choose a convenient
outcome because it produces attractive performance.

The initial source sample is not a supervised training cohort. The 140 parcel
seed set uses information retrieved in 2026 and cannot be used unchanged as a
historically available data-center universe. Doing so would introduce selection
bias and future-information leakage.

## Baseline specification (not fitted)

Once the gate passes, define the eligible project universe at each forecast
date. Baseline: rank using stage and recency available on that date. Compare
one interpretable alternative that adds verified planning/design signals.
An announcement-only benchmark requires actual dated announcement data; it
has not been collected and must not be simulated from current descriptions.

Evaluate equal outreach budgets using precision at k, recall at k, false alerts
and lead time to the same outcome. Select k with the intended seller.
Precision at 10 = verified events among ten shortlisted eligible projects,
with unknown labels handled separately. Lead time = outcome date minus first
eligible alert date, reported jointly with precision.

Use a chronological held-out period and keep records of the same project/campus
together where dependence exists. Include a gap where 180-day outcome windows
would otherwise overlap the split. Test feature contributions individually.
Report uncertainty, sample size and failure cases. Business conversion needs
a later prospective pilot.

## Next narrow work package

Recover archived evidence and manually reconcile ten identifiable buildings or
phases. Public building-permit reports exist back to 2015, but document retrieval,
release dates and their coverage still need verification. Compare original
descriptions with current ones. Seek a supplier design partner separately.
Do not claim interviews have occurred.
