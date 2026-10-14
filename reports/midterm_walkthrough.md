# Coco.ai: the current project, explained from beginning to end

Updated October 14, 2026. This is the main midterm reference. The earlier
407-permit description-classification exercise is retained separately in
`qualification_walkthrough.md`; it does not establish early-warning performance.

## The goal and the result

We want to help a data-center cooling supplier decide which proposed project
deserves investigation before a later development milestone. The first measurable
milestone is **planning approval**, because public sources provide identifiable
approval events. We have not established that this is an open equipment-buying
window. Permission to develop, construction start, and supplier selection are
different events.

We completed a small dated-document pilot in the Ashburn District of Loudoun
County, Virginia. It produces an investigation queue, a review queue and a source-
backed timeline. **It does not demonstrate earlier discovery than ordinary news.**
For the fully traced example, recovered news coverage predates our recovered
county notices. That negative comparison is a main result, not something to hide.
One case cannot establish that public-record intelligence always fails, just as
advance notice in one case cannot prove the product works. The present evidence
supports a functioning small research prototype and leaves broader usefulness open.

## What we did, in everyday terms

A county newsletter lists proposed developments. We read each listed application
and recorded what the issue said about its purpose and stage. We wrote a short
program that keeps explicit proposed DC buildings awaiting planning decisions,
marks already-approved developments as later-stage, and asks for review when
building scope is unclear. We then looked for dated later approval evidence and
compared the recovered county notices with a dated industry-news article.

There are no learned parameters. The rules are written instructions. There is
no statistical training set and no untouched test set. The analysis is a
retrospective, AI-assisted, manually prepared case pilot. Another person should
review the extraction before it is treated as reliable ground truth.

## Which data is being used for which purpose

| Data | Dates and location | Purpose |
|---|---|---|
| Main screening source: Ashburn District newsletter | January 26, 2024; Ashburn District, Loudoun | Fixed set of 16 application entries; issue-era scope and stage |
| Earlier archived county newsletters | February 8, 2023 and January 8, 2024 | Additional recovered Belmont notices; not earliest-ever claims |
| Dated county news releases | March 22 and April 11, 2024 | Evidence of Belmont denial, reconsideration and approval events |
| Dated industry-news article | October 6, 2022 | Ordinary-news comparison for the same campus |
| Archived issued-permit report | July 1–15, 2025 reporting period | Checks one permit's issue date against the prior snapshot; not a campus timing endpoint |
| Current DC Byte product page | Checked October 14, 2026 | Competitor capability research, not a measured competitor-performance test |

All URLs, publisher identities, date interpretations and access limitations are
in `data/curated/dated_sources.csv`. Project facts are in `dated_projects.csv`;
later events are in `dated_events.csv`. These are AI-assisted manual extractions
of facts from sources, not an automatically scraped historical database.

The newsletter is issued by the county supervisor's office, even though its
online version is hosted by Constant Contact. County PDFs are on loudoun.gov.
The comparison article is from Data Center Dynamics. No DC Byte dataset was
purchased or used to produce alerts.

## Why one January 2024 issue, rather than the 2000–2026 collection

The earlier broad download contains historical application dates with current
descriptions. It does not preserve what people could read on each old date.
Restricting those records to 2023–2025 did not solve that problem.

For this timing pilot, we selected a dated newsletter containing multiple
development entries, including active proposals and an already-approved example.
It gives a fixed, inspectable screening frame. We did not assemble the main
screening list solely from projects known to receive later permits.

However, this issue was selected retrospectively after some outcomes were known,
and source recovery began with Belmont. The district, issue and tiny sample are
not random or representative of all Loudoun developments. This is a feasibility
pilot, not a full historical validation or a countywide discovery test.

## What the program receives and returns

The program receives three manually recorded facts from the January issue:

1. Does the entry mention DC use anywhere?
2. Is the main proposal explicitly for new DC buildings, another use, or mixed
   land-use permission requiring more investigation?
3. Does that issue describe planning as pending or already approved?

It does not read later approval dates or today's statuses when deciding to alert.
Those later dates are joined afterward only to evaluate timing. Code tests check
that changing a future outcome field cannot change the initial alert decision.

Outputs mean:

- **Investigate:** explicit proposed DC buildings awaiting a planning decision.
- **Review:** mixed DC-use permission or uncertain historical scope/stage.
- **Later stage:** DC proposal whose approval was already reported in this issue.
- **Outside scope:** primary application concerns another type of development.

Later-stage does not mean no sales opportunity. It means the entry cannot count
as a pre-approval warning under this endpoint. A watchlist item is not an open
contract, a verified cooling requirement, or a probability of closing a sale.

## Baseline and screening results

Baseline: flag any application entry whose text mentions data-center use,
including references to another application. We recorded that presence from the
source; we did not run an automated text parser on an independently archived file.
Both baseline and Coco rules therefore use manually curated source facts.

| January 26 screening result | Count |
|---|---:|
| Application entries inspected | 16 |
| Broad DC-mention baseline alerts | 6 |
| Coco investigation items | 3 |
| Mixed-scope item needing review | 1 |
| Already-approved DC item | 1 |
| Other entries outside scope | 11 |

The three investigation items are Belmont Innovation Campus, CyrusOne Broadlands
and Belmont Landbay KK. Vantage VA3 is already approved. Luck Stone Leesburg Plant
is mixed quarry/DC-use permission, so it goes to review. Northstar Square is a
residential application with a cross-reference to a different DC application.

These counts describe the implemented queue logic. They are not independent
precision/recall estimates or evidence that review time is reduced. The broader
baseline detects every one of the three Coco investigation items on the same
issue date: **the filtering adds no detection-time advantage over this baseline.**

## The timing result: Belmont Innovation Campus

We linked the old ZMAP-2022-0021 application and later LEGI-2023-0048 umbrella
application using the campus name and explicit county application references.
This is a campus-level comparison; it does not establish identical building
scope across every version. The final approved proposal was reduced.

| Evidence or event | Date | Meaning |
|---|---|---|
| Recovered industry article describing the proposal | October 6, 2022 | An ordinary-news reader already had campus visibility |
| Earlier recovered county newsletter describing the proposal | February 8, 2023 | Pending proposal is visible in a dated county issue |
| Main cohort newsletter | January 26, 2024 | Proposal remains awaiting Board action |
| Initial denial | March 13, 2024 | Progress is uncertain; proposal is not guaranteed to advance |
| Vote to reconsider | March 19, 2024 | Revised proposal is revived |
| Approval of reduced proposal | April 10, 2024 | Our chosen later milestone occurs |

The January 26 notice precedes approval by **75 calendar days**. The recovered
February 8, 2023 notice precedes approval by **427 days**. But the recovered
industry article precedes approval by **552 days**. Even our earlier county
notice is **125 days later than the industry article**. We therefore found
advance notice before approval but no incremental discovery advantage over news.

This is one fully traced later approval, not average performance across three
successful projects. For CyrusOne Broadlands and Belmont Landbay KK, later
approval dates were not recovered in this analysis. We leave their outcomes
unknown. We do not count either as failed, successful, or definitely pending today.

Vantage VA3 provides a useful negative timing control: its May 15, 2023 site-plan
approval predates the January 26, 2024 issue by 256 days. We preserve that negative
lead time rather than portraying the newsletter as an early approval warning.

## The date assumptions, stated honestly

We use printed newsletter issue dates as proxies for when subscribers could
have received the information. We did not independently verify original delivery
logs, historical web posting timestamps or first-version snapshots. The result
should be described as a **publisher-dated reconstruction**, conditional on
those issue dates representing availability of the observed content.

A later news release can document an earlier event. For example, the March 22
release describes votes on March 13 and March 19. The event dates do not prove
our recovered release was readable before March 22. Both event date and evidence
document date are saved in the output timeline.

The old DCD article has a displayed publication date, but its original first
version was not independently archived. We do not assert that we recovered the
earliest public mention ever, or that later edits never occurred. The dated
comparison is still an important challenge to the discovery-alpha hypothesis.

The July 2025 report corroborates permit BLDC-2025-009449's July 8 issue event
against the original snapshot. It does not provide its own publication timestamp.
Campus/building linkage was not independently settled, so this permit is explicitly
excluded from the campus timing calculation. We do not substitute permit issuance
for a construction start or purchase.

## What is genuinely implemented, and what is not

Implemented: transparent alert logic, issue-era source facts, an investigation
queue, review/later-stage routing, signed notice-time calculations, a news
comparison, explicit missing outcomes, source provenance and reproducibility.
Eleven automated integrity/metric checks pass across the repository.

Not established: predictive accuracy, countywide coverage, independent label
validity, actual historical delivery timestamps, supplier-selection timing,
earlier discovery than news/DC Byte, saved salesperson time or additional sales.
The source interpretation step is manual. Production document extraction and
continuous monitoring have not been built; this is research code, not an app.

## Competitors and the business implication

DC Byte currently describes supplier-facing project discovery, early alerts for
new/expanding DCs, segmentation, supplier relationships and prioritization. Our
intended use overlaps substantially. We cannot infer from its public page that
it lacks permit tracking or detailed project-stage information.

| Aspect | Coco pilot | DC Byte public offering |
|---|---|---|
| Intended user | Cooling supplier investigation workflow | Broader data-center supplier/sales teams |
| Geography and coverage | One district issue; tiny research sample | Advertised global project coverage |
| Early-project visibility | Reconstructed from public sources | Advertised early-stage/project alerts |
| Prioritization | Explicit scope/stage rules and review route | Advertised supplier segmentation/prioritization |
| Validation | One recovered later approval; unknowns retained | Not audited by us |
| Measured timing advantage | None over the recovered news comparator | No empirical head-to-head comparison available |

Coco's source explanations and small local workflow are implemented attributes,
not demonstrated competitive advantages. The commercial question is still open:
would a seller find this decision support useful enough to adopt or pay for,
given existing tools?

The strongest current lesson is that discovery alone may be the wrong place to
seek an advantage. Stage changes, reversals and scope reductions might matter
for deciding where to spend investigation effort, but competitors also track
stages. That direction needs customer evidence and a genuine comparison.

## Challenges, resolutions and remaining roadblocks

| Challenge | What we did | What remains |
|---|---|---|
| Current permit descriptions cannot be backdated | Switched primary timing evidence to dated documents | Historical first-version and delivery verification |
| Broad original collection confused the task | Separated 407-permit background audit from 16-entry timing pilot | Larger representative dated sample if warranted |
| Keyword mentions can concern another application | Used primary scope and historical stage; kept review route | Independent checking and automated extraction |
| Later approval dates missing for two proposals | Preserved unknown outcomes | Recover dated records; no failure rate until coverage is known |
| Similar names/campus phases can be mismatched | Used application IDs; excluded unsettled permit linkage | Building-level reconciliation where needed |
| Ordinary news can be earlier | Measured and disclosed negative timing advantage | No support yet for a discovery-led commercial edge |
| Direct PDF/HTML downloads returned HTTP 403 | Read accessible source text through web retrieval and recorded links | Original source bytes were not archived or hashed; no access bypass attempted |
| Approval may be a poor sales milestone | Explicitly labeled it a development endpoint | Ask a seller when outreach is commercially useful |

## Continue, change direction, or pivot?

Continue the same early-discovery thesis only if a larger independently reviewed
dated sample shows useful incremental notice over news and existing workflows,
and a seller confirms the selected milestone precedes a useful outreach window.

Change the supported decision if discovery is already commoditized: for example,
test whether documented changes to known projects improve investigation choices.
This is a candidate question, not a feature gap proven in DC Byte.

Pivot later if suppliers cannot act on the available timing, existing products
already serve the decision adequately, or we cannot obtain reliable dated
evidence/outcomes. A narrower underserved supplier decision or another industry
would need new customer discovery before new modeling. Do not add ML merely to
make a weak information advantage sound more sophisticated.

## What remains before stronger claims

Independent review, unseen-source evaluation and seller validation are still
necessary. These are unresolved foundations, not optional details to hide as
future expansion. Equipment recommendations, purchasing probabilities and
seller-specific buying-window forecasts remain the explicitly deferred scope.
Slides have not been rebuilt, and no customer interviews or Plause feedback have
been invented.

For the midterm, the honest claim is: **we built a small source-backed proposal
watchlist and tested notice timing; public documents preceded approval in one
traced case, but ordinary news was earlier and commercial alpha is unproven.**

## Reproduce and inspect

Run `python scripts/analyze_early_notice.py` and then
`python -m unittest discover -s tests -v`.

Inspect `data/processed/early_notice_screening.csv`,
`early_notice_investigation_queue.csv`, `early_notice_timeline.csv` and
`early_notice_summary.json`. The source inputs are committed under `data/curated/`.
This reruns calculations on the frozen manual extraction; it does not recollect
or authenticate the original historical webpages.

The professor's required overview, progress, data preparation/issues, baseline,
analytical method, preliminary results, evaluation, next steps and risks all have
documented material above. Primary evaluation uses notice days and outcome-date
coverage. Success rate, recall and sales conversion are not reported because the
sample/labels cannot support them. Presentation preparation and real customer
discovery remain outstanding.
