# Midterm speaking brief: Coco.ai

Earlier six-minute version retained as background. The current eight-minute,
twelve-slide structure with actual Plause feedback and physical-outcome follow-up
is `midterm_slide_structure.md`. Use that file for the upcoming presentation.

No slides created. Target: approximately six minutes of speaking, then questions.
Use this narrative as the basis for a later deck. The full understanding notes
are in `midterm_walkthrough.md`; do not try to read that entire report aloud.

## 1. Opening and continuity: 40 seconds

“Planning documents exist to manage development. Coco.ai would use them for a
different decision: which proposed data-center project should a cooling supplier
investigate? My original idea was to recognize potential customer needs before
normal sales signals make them obvious. For the midterm, I narrowed that to one
location and one measurable question: can dated public records give notice before
planning approval, and do they add anything beyond ordinary public information?”

## 2. What changed after collecting real data: 45 seconds

“I collected official Loudoun County planning and permit records. The first
problem was that an old application date does not mean its current description
was visible on that old date. Some descriptions were updated later. So I could
not honestly use today's text to claim an early historical prediction. I kept
that collection as background and moved the timing analysis to dated newsletters
and county news releases. I also chose planning approval as an observable
milestone, while keeping clear that approval is not a cooling purchase.”

## 3. Data and preparation: 50 seconds

“The main pilot uses one Ashburn District newsletter dated January 26, 2024.
It contains sixteen development-application entries. I recorded each entry's
main purpose and the stage reported in that issue, along with its application
identifier and source. That preparation was AI-assisted manual interpretation,
not an automatically scraped historical database. I then collected dated later
evidence separately. Where I could not recover an approval date, I left it
unknown. I did not turn missing information into a failed project.”

## 4. Method and baseline: 50 seconds

“The baseline flags any entry mentioning data-center use. The alternative uses
simple scope and stage rules: investigate explicit proposed data-center buildings
awaiting a planning decision, separate already-approved projects, and review mixed
or ambiguous uses. The baseline flags six entries. Our rules produce three
investigation items, one review item and one already-approved data-center item.
Both use manually prepared source facts. There is no trained machine-learning
model here. We are testing whether the information and decision logic are useful
before adding complexity.”

## 5. Results and evaluation: 100 seconds

“The most important result comes from Belmont Innovation Campus. The main
January newsletter describes it seventy-five days before its April 2024 approval.
Looking further back, I recovered a February 2023 county newsletter: that is
four hundred and twenty-seven days before approval.

“But that alone would make the story look better than the evidence warrants.
Industry news covered the proposed campus in October 2022, one hundred and
twenty-five days before our earlier recovered county notice. So we found advance
notice before approval, but did not beat ordinary news on discovery timing.

“The case also includes an initial denial and subsequent reconsideration before
a smaller proposal was approved. An early alert is therefore not a guarantee.
Another entry, Vantage VA3, had already been approved before the newsletter. Two
other proposed projects still lack recovered later approval dates in our analysis.
Our evaluation reports notice days and missing-outcome coverage, rather than
pretending one traced approval proves a success rate. Publisher issue dates are
our availability proxies; original delivery timestamps remain unverified.”

## 6. Competition and commercial meaning: 45 seconds

“DC Byte already advertises early project alerts, supplier segmentation and
prioritization. Coco's intended use overlaps with that. We have not measured
performance against DC Byte, and our basic keyword baseline finds all three
investigation items on the same newsletter date. The current benefit is an
inspectable watchlist with scope and stage context. Saved time, earlier useful
outreach and additional sales are not demonstrated. Source transparency is a
prototype attribute, not a proven competitive moat.”

## 7. Next steps, risk and discussion: 30 seconds

“The next steps are independent source review, recovering missing outcomes,
testing unseen dated records, and asking suppliers which milestone actually
changes their outreach decision. Customer interviews have not yet been conducted.
If discovery is already well served, I may change the decision to monitoring
meaningful changes in known projects, or pivot after customer discovery. I want
the evidence to determine that choice, rather than add a complex model to force
the original idea to work.”

## Coverage of professor requirements

| Requirement from the screenshots | Where the narrative covers it |
|---|---|
| Project overview, original objectives and intended impact | Opening: alternative-data sales intelligence for cooling suppliers |
| Progress, milestones and major challenges | Official collection, dated evidence, executable rules and timing analysis; edited-text problem |
| Data collection/preparation, missingness, bias and availability | Fixed newsletter, manual fields, separate later evidence, unknown outcomes; retrospective/publisher-date limits |
| Analytical methods, BASELINE and preliminary results | Broad mention baseline versus scope/stage rules; counts and timeline |
| Evaluation metrics | Notice days, comparative timing, unknown-outcome coverage and past-milestone control; no unsupported accuracy metric |
| Next steps | Independent review, unseen evaluation, missing outcomes and seller discovery |
| Challenges/risks and mitigation | Leakage, uncertain buying relevance, weak comparator advantage and possible pivot |
| Customer discovery | Explicitly not completed; do not invent interviews |
| Plause feedback, encouraged but optional | No feedback supplied; do not claim it was used |

This covers the requested topics honestly. It does not turn unresolved validation
or customer-discovery work into completed accomplishments.

## Questions you should be ready to answer

**Is this predictive modeling?**
It is a rules-based proposal watchlist and retrospective timing pilot. It does
not forecast a purchase or assign calibrated probabilities. A trained model is
not needed to ask whether a dated alert precedes a milestone, but independent
evaluation is still needed.

**Why not train a model now?**
Reliable historical information and commercially meaningful outcomes are the
current constraint. A more complicated model cannot supply missing evidence.

**Why do later outcomes matter without training?**
They let us check whether an alert preceded an actual milestone. Otherwise we
only know the program found a proposal. They are evaluation evidence, not inputs
used to make the early decision.

**What happened to the data from 2000 onward and the 407 records?**
Those are the broader snapshot and earlier description-qualification exercise.
They are supporting work, not the timing experiment or a training set. The current
primary pilot is sixteen entries in one dated 2024 issue, with older documents
used to investigate one case's history.

**Does a newsletter date prove exactly when the information became public?**
No. We use its publisher-stated issue date as a proxy. Historical delivery logs
and first-version archiving remain verification gaps.

**Why planning approval?**
It is a recoverable, identifiable development event and relevant to tracking
project progression. Its usefulness as a cooling outreach deadline is not yet
validated. It is not construction start or supplier selection.

**Does the project work?**
The code works on the curated facts and produces inspectable queues/calculations.
The evidence does not yet establish commercial usefulness or an information edge.
Ordinary news is earlier in the traced case.

**How is this different from DC Byte?**
The scope is much smaller and the reasoning is exposed in a public research repo.
That is an implementation difference, not demonstrated customer value or a
feature gap in DC Byte. Its advertised functions overlap substantially.

**Where is the alpha?**
The proposed alpha was earlier useful awareness and better investigation choices.
The current study has not demonstrated discovery timing alpha. We should state
that plainly and test a revised decision only if customers identify a genuine gap.

**What about the missing outcomes?**
Two investigation items lack recovered later approval dates. They are unknown,
not failures; 1 of 3 recovered dates is evidence coverage, not 33% precision.

**What did you actually build?**
Official-source collection/cleaning scripts, a dated-source fact table, rule-based
screening, source-linked queues, signed timing calculations, comparison outputs
and eleven integrity tests. Dated fact extraction is still manual; no app exists.

**What would make you pivot?**
If sellers cannot act on the available evidence, existing tools already serve the
decision well, or historical validation remains infeasible, change the customer
decision or niche based on discovery rather than insist on the current product.

## Sources to cite later on slides

Use the complete URLs in `data/curated/dated_sources.csv`. At minimum cite:
the January 26, 2024 supervisor newsletter for screening; February 8, 2023 county
archive and April 11, 2024 release for Belmont timing; October 6, 2022 DCD article
for the news comparison; March 22, 2024 release for reversal risk; and the current
DC Byte Supplier Analytics page for competitor claims. Date the competitor check
October 14, 2026. Do not cite the county sources as proof of an open RFQ.
