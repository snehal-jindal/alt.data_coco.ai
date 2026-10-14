# Background: the earlier filing-qualification exercise

This report preserves the earlier 407-permit exercise. It is supporting work,
not the current early-notice analysis. Read `midterm_walkthrough.md` for the
dated-document study and the current conclusion.

Prepared October 14, 2026. This report accompanies executable data/code, not a
finished slide deck. Start here; the other reports preserve the technical detail.

## 1. What we are trying to do

The original Coco.ai idea was to help suppliers recognize a potential customer
need from operational records before a normal sales announcement or RFP makes
it obvious. Our first customer is a data-center cooling supplier. Workforce
signals, other industries and investment predictions are outside this midterm.

The research scope narrows the first step to new data-center buildings and
substantial physical expansions in Loudoun County, Virginia. The working question
is: **which building filings deserve investigation as evidence of a new physical
data-center project?** This is qualification, not a purchase forecast.

Our output is a filing plus its source text and explanation, assigned to one of
three queues: qualifies under our scope, clearly outside this scope, or needs
review. There is no numerical purchasing probability or buying-window estimate.

The distinction matters. A new data-center building may be relevant to a cooling
supplier, but its cooling supplier could already have been chosen. A building
permit alone does not establish an open contract or imminent quote request.

## 2. What existed before, and what has been done now

At the initial presentation we had a customer, a proposed alternative-data use
case and a research plan. This was not yet a collected dataset or tested product.

On October 13 we downloaded real county planning and permit records and wrote
code to clean them. That broad source audit exposed a problem: the feeds contain
old event dates but current descriptions, and no cooling RFQ labels. We could not
honestly test the original idea of predicting a quote request within 180 days.
That horizon was an unvalidated suggestion, not a commitment from a seller.

On October 14, following the scope definition, we created one narrower dataset,
explicit labeling criteria, AI-assisted initial desk labels, a county-category
baseline, one transparent rule classifier, an evaluation script, error records
and reproducibility checks. We did not turn missing RFQs into negative outcomes.

## 3. Where the data comes from

All model-input records come directly from official Loudoun County public GIS
services. An API is simply a structured download route for the county's records.
We did not buy DC Byte data, scrape LinkedIn or invent examples.

| Source | What it contains | What we use it for |
|---|---|---|
| [County planning layer](https://logis.loudoun.gov/gis/rest/services/Projects/LOLA_DATA/MapServer/0) | Planning application number, date, type, current status and description | Earlier source exploration; **not an input to the current classifier** |
| [Issued permit layer](https://logis.loudoun.gov/gis/rest/services/LMARC/LandMARC_Permits/MapServer/1) | Permit identifier, application/issue dates, work category, parcel and description | Main permit collection; supplies current classification examples |
| [Submitted permit layer](https://logis.loudoun.gov/gis/rest/services/LMARC/LandMARC_Permits/MapServer/2) | Similar fields for submitted records | Complements the issued feed; combined and deduplicated |
| Our initial desk-annotation file | Our interpretation of each description, with evidence and reason | Initial answer key for an internal agreement audit; **not county or independent expert labels** |
| Our generated predictions and metrics | Program decisions and comparisons with desk labels | Model outputs; these are not additional source data |

Both permit feeds may have repeated rows for addresses or parcel associations.
The county PermitGUID is the key for one permit. One permit can span parcels;
one campus can contain several buildings; several permits can concern one
building. We have not solved complete building/phase matching.

## 4. Which dates and geography apply

The download happened October 13, 2026. The county permit feed's snapshot is also
October 13. The larger collected permit table includes application dates from
August 2000 through October 2026; the planning applications extend from May 2005
through October 2026. We are **not modeling that whole history**.

The midterm cohort is only commercial-building permits applied for in 2023–2025:

| Application year | Unique permit IDs |
|---|---:|
| 2023 | 65 |
| 2024 | 180 |
| 2025 | 162 |
| Total | 407 |

The exact selected application dates run January 10, 2023 to December 26, 2025,
using Eastern local calendar dates. This bounded selection gives complete
calendar years and avoids mixing incomplete 2026 with them. It does not prove
these are the ideal commercial years or create a forecasting experiment.

Every selected record comes from the Loudoun County collection. Ashburn and
Sterling are locations within this county, not separate model markets. The table
has 93 representative parcel IDs; four permits have multiple parcel associations,
making 95 parcels across all those source associations.

Earlier I described 140 as the seed-parcel count. That conflated two numbers.
The raw keyword rows actually generated **160 queried parcels**; after one-row-
per-permit cleaning, 140 representative parcels remained on keyword records.
The focused cohort is 407 filings regardless of that correction.

An application date tells us when the filing was made. A retrieval date tells us
when we downloaded the version we possess. These are different. Some 2024/2025
filings explicitly mention revisions in 2026. We cannot place that later text
back in 2024 and pretend a seller knew it then. The present audit classifies the
text now available. Older filings are testing examples, not automatically live
sales leads in October 2026.

## 5. How we narrowed and cleaned the records

The initial keyword queries found descriptions mentioning data centers. We then
downloaded all permit types at the 160 associated parcel IDs to retain records
whose short description omitted the words data center. Cleaning produced 6,858
unique permit IDs. This includes electrical, mechanical and unrelated work.

We selected the commercial-building type and application years 2023–2025,
leaving 407. Planning and mechanical records stay in the source audit; they are
not mixed into this classifier. Status, monetary value and issue dates are not
classification inputs. The baseline uses work category; the alternative uses
description text. Application date only selects the cohort and year summaries.

Duplicates with the same PermitGUID are removed. Invalid dates are blanked and
flagged rather than fabricated. Twenty-two local-day issue-before-application
anomalies in the larger table are flagged; neither date becomes a buying label.
Multiple parcel mappings are reported separately. Missing information leads to
review. Cross-ID copy filings remain a future deduplication problem.

The selection is biased toward parcels already identifiable as DC-associated
from current text. Therefore this experiment **cannot measure how well we find
unknown new DC sites across the county**, or how early we would have found them.
It tests qualification within the collected candidate pool.

## 6. What counts as the right answer

Positive means explicit whole-building data-center construction, its core/shell,
or a physical addition creating new data-hall space. A new building on an
existing campus qualifies. Internal fit-out, office-only work, guardhouses,
mechanical yards and separately referenced occupancy phases do not qualify under
this particular physical-building definition. They may still be commercially
valuable under a broader equipment-sales task; we deliberately exclude them here.

Unknown means the description is too vague to decide. A shell building without
explicit DC use, unexplained acronym or generic phase is not quietly labeled
negative. Our initial desk reading produced 29 positives, 310 negatives and
68 unknowns. Every label and full source description is available in
`qualification_annotations.csv`.

**AI assistance supported description labeling and rule development. The labels
have not been independently reviewed by a construction expert or supplier.**
The present results establish agreement with that initial interpretation. They
do not establish real-world accuracy or independent generalization.

## 7. What the two methods do

Baseline: select filings the county categorizes as New Construction or Addition.
This is what a very basic project list might do. It selects 57 filings. Those
categories include guardhouses, office work and repeated construction phases.

Alternative: inspect the description with readable rules. Evidence of a new
physical data-hall addition or whole DC building qualifies. Explicit routine/
support work and parent-linked phases are excluded. Ambiguous records go to
review. Each output names the rule that caused the decision.

For example, `BLDC-2024-035070` includes both interior work and a new two-story
structure with two data halls. The physical addition qualifies even though its
description also mentions an existing building. `BLDC-2025-051479` is a
prefabricated guardhouse for a data center: the baseline qualifies it, while the
text rule excludes it. `BLDC-2025-036008` says only Shell Building Permit, so the
text rule asks for review rather than assuming a DC building.

## 8. Training versus testing, without jargon

A trained model learns patterns from labeled examples: we show it examples and
answers, and it adjusts numerical parameters to improve its predictions.

This first version works differently. We write instructions explicitly. It does
not estimate parameters from examples and has no statistical training dataset.
The analytical method is a deterministic rule system.

Testing still means checking its answers. We ran both methods over all 407
filings and compared them with the initial desk labels. We also report each year
separately. **2023–2024 are not secretly a training set, and 2025 is not a blind
test set.** All years were inspected during development. A year breakdown is a
diagnostic, not an independent train/test split.

For the next stronger test: freeze the current rules, obtain independently
reviewed labels on new, previously unseen filings, and run once before changing
rules. For a future learned model, use older independently labeled examples for
training and later unseen examples for testing, keeping related buildings/phases
together so copies do not appear on both sides. Buying-window forecasting would
add the requirement of verifying what was public before each prediction date.

## 9. What the initial results actually show

| Measure, all 407 filings | County-category baseline | Description rules |
|---|---:|---:|
| Automatically qualified filings | 57 | 32 |
| Desk-positive filings among those | 29 | 28 |
| Clear desk-negative false alerts | 17 | 4 |
| Qualified filings with unknown desk label | 11 | 0 |
| Desk positives not automatically qualified | 0 | 1 |
| Filings sent to review | 0 | 80 |
| Precision on resolved labels | 63.0% | 87.5% |
| Recall on desk positives | 100% | 96.6% |
| F1 on resolved labels | 0.773 | 0.918 |

Precision asks: of the auto-qualified filings whose desk answer is known, how
many fit our scope? Baseline: 29 / (29 + 17). Rules: 28 / (28 + 4). The 11 unknown
baseline selections are excluded from that denominator, not assumed wrong.
Across its entire 57-record queue, 29 are desk-positive, 17 negative and 11
unresolved. This makes the precision figure's limit visible.

Recall asks: of the 29 desk-positive filings, how many were auto-qualified? The
rules place the remaining one in review, which still counts as a miss for
automatic qualification. F1 combines precision and recall in one measure.

There is a second important result: **2025 precision is worse for our rules**,
76.9% versus baseline 83.3% on resolved labels. All 10 desk positives are found
by both, but rules produce three clear false alerts versus two for the baseline.
The pooled gain is partly driven by noisier 2024 categories. No consistent
year-to-year advantage has been established.

The 80-record rule review queue contains 68 unknowns, 11 desk negatives and one
desk positive. Consequently a cleaner automatic shortlist does not prove lower
total review effort: inspecting 32 alerts plus all 80 review records could take
more work than inspecting the baseline's 57 alerts. Time savings need measurement.

## 10. What went wrong, and why it matters

The four rule false alerts are an office phase, a temporary break tent whose
description quotes a DC parent, and two existing-shell tenant fit-outs. These
show a specific text problem: mentioning the parent new building does not mean
this particular filing constructs it. The rule misses automatic qualification
for VA16 because its wording says a building is to be constructed to operate as
a data center rather than using the simpler phrases the rule recognizes.

All five cases are in `qualification_errors.csv`. We did not tune the rules on
these evaluation errors and rerun to present perfect scores. The next revision
must distinguish this filing's actual scope from quoted parent context, then be
evaluated on independently reviewed unseen records.

Seven automated integrity/metric tests pass. They check record uniqueness,
date handling, annotation coverage, source-text consistency and correct handling
of unknowns. Passing code tests does not validate the commercial idea.

## 11. Where the alternative-data value and startup question stand

County records exist for permitting and development administration. We use them
for a supplier's different decision: which project should I investigate? That
repurposing is the alternative-data use case. Public availability does not make
the interpretation trivial, but public-source use alone is not a competitive moat.

For this midterm, the measurable contribution is a transparent qualification
experiment with a baseline, a review route and exposed errors. It is not yet
early-warning alpha. Potential commercial value is a better investigation queue;
less irrelevant work, earlier useful conversations and more sales remain
unverified hypotheses.

[DC Byte Supplier Analytics](https://www.dcbyte.com/us/supplier-analytics/)
already advertises early alerts, project discovery, supplier segmentation and
prioritization. We cannot claim these functions are unique. We have not tested
against DC Byte. A plausible future distinction is seller-specific, source-backed
buying-window evidence with demonstrated additional decision value; even that
is a research direction, not a verified gap in competitors' capabilities.

## 12. What remains, in order

1. Independently review labels, especially every qualified filing and ambiguous
   parent/phase case. Confirm with a seller which physical-building scopes are
   actually useful. Correct disagreements before treating labels as ground truth.
2. Test frozen rules on unseen filings; improve parent-context handling using a
   separate development set. Compare both precision and human review effort.
3. Resolve cross-ID copies and building/phase identities before claiming counts
   of distinct projects. Verify current project status before using old examples
   as live sales leads.
4. For the post-midterm timing stage, recover dated public documents and obtain
   seller evidence about supplier selection/RFQs. Define one actual buying-window
   outcome and test whether earlier evidence anticipates it. Do not equate a
   mechanical permit or construction start with an open buying opportunity.

The primary risk is not too little modeling complexity: it is confidently
answering a commercial question our evidence does not yet support. This narrower
prototype makes the foundation inspectable while preserving the original goal.
