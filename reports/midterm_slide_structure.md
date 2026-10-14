# Coco.ai: twelve-slide written midterm structure

Slide-by-slide research narrative and speaker notes for the midterm presentation.
[Google Slides deck](https://docs.google.com/presentation/d/16yxMeZ2Dwdd8IzQ9tnGfU3xiDa9a28AADcd5fszQ4rA).
Planned narration: 7 minutes 40 seconds, leaving 20 seconds within an eight-minute slot.
The code/source checks are complete; independent and commercial validation remain gaps.

## Slide 1 — Coco.ai: Which projects deserve your next call? — 25 seconds

On slide: Public development records → supplier investigation.
Cooling suppliers. Loudoun County, Virginia.

Visual: one restrained illustration of project information reaching a salesperson.

Speaker notes: “Imagine you sell commercial cooling equipment. Someone proposes
a data center, and you want to know whether that project deserves your attention.
Coco.ai's original idea was to repurpose public information for that sales
decision. I narrowed the midterm to new data-center buildings and substantial
physical expansions in Loudoun County. Two things matter: how early the signal
appears, and whether it points to projects that actually progress.”

Footer: Original project concept and Coco.ai research scope.

## Slide 2 — Step 1: Collect the county's construction paperwork — 40 seconds

On slide: Official planning and permit records / Collected October 13, 2026 /
407 building filings in the initial audit.

Visual: planning records + building permits → cleaned table. Small progress line:
Idea → collected data → working research code.

Speaker notes: “Companies submit government paperwork to seek development or
construction permission. I downloaded official county records containing dates,
identifiers and descriptions. The broad permit collection spans application dates
from 2000 to 2026. I removed repeated permit IDs and flagged unusable dates. I then
selected 407 commercial-building filings from 2023–2025 for a manageable first
description audit. Those years were a practical choice, not a proven forecasting
period. That audit is supporting work, not a training dataset.”

Footer: Loudoun County planning/permit APIs; Coco.ai source audit.

## Slide 3 — Step 2: An old application can contain newer information — 35 seconds

On slide: Application date ≠ date of the description we downloaded.
Current descriptions cannot prove an earlier warning.

Visual: clearly illustrative 2024 application → 2026 edit/download.

Speaker notes: “The first major challenge was historical timing. A filing submitted
in 2024 can contain a description revised in 2026. Recognizing a data center in
that later text does not prove a salesperson could recognize it in 2024. I kept
the 407-record exercise for description sorting, but did not use it to claim
historical early detection. I moved the timing pilot to dated documents. Original
versions and posting or delivery dates still need verification.”

Footer: Coco.ai source audit. Example labeled illustrative.

## Slide 4 — Step 3: Examine a dated local update — 40 seconds

On slide: Ashburn District newsletter / January 26, 2024 / 16 development entries.
Community news containing development proposals.

Visual: genuine issue heading and the three facts.

Speaker notes: “This newsletter comes from the Ashburn supervisor's office. Its
audience is residents, and it covers roads, community news and development.
It is not mainly about data centers. I used one accessible dated issue containing
sixteen application entries. January 2024 was a convenient pilot, not a special
commercial date. I used AI assistance to read the entries and record their purpose, application identifier,
reported stage and source. This preparation was manual and AI-assisted. The stated
issue date is our availability proxy; original delivery is not independently verified.”

Footer: Ashburn District newsletter, January 26, 2024.

## Slide 5 — Step 4: Compare a basic filter with scope and stage rules — 50 seconds

On slide: 16 inspected → 6 DC mentions → 3 investigate.
Other baseline entries: 1 review / 1 already approved / 1 different application.

Visual: six baseline entries split into four groups; numbers sum to six.

Speaker notes: “The baseline flags any entry mentioning data-center use: six
entries. Our rules examine the actual proposal and stage. Three explicitly concern
proposed DC buildings awaiting a decision: Belmont Innovation Campus, CyrusOne
Broadlands and Belmont Landbay KK. The others are mixed-use permission needing
review, an already-approved DC project, and a residential application referring
to another DC proposal. The code sorts facts I prepared; it does not read new
websites automatically. These are written instructions, with no statistical
training. Both filters find the same three projects on the same issue date.”

Footer: January 26 newsletter; dated_projects.csv; early_notice_screening.csv.

## Slide 6 — Step 5: Change the watchlist when the evidence changes — 45 seconds

On slide: Belmont / Investigate → Review revised proposal → Approval reported.
Document dates: Feb 8, 2023 → Mar 22, 2024 → Apr 11, 2024.

Visual: three states; distinguish the April 10 vote from the April 11 reporting document.

Speaker notes: “I also implemented a dated update replay. Belmont starts as a
pending proposal to investigate. A March 22 release reports an initial denial
and subsequent reconsideration, so the code asks for review of the revised
proposal. The April 11 release reports approval, so it moves to a later stage.
The code does not backdate that update to the April 10 vote. Repeated notices
are not new discoveries. This demonstrates update handling, not sales performance.
Already approved does not necessarily mean too late to sell.”

Footer: County February 8 newsletter, March 22 and April 11 releases;
watchlist_update_replay.csv. Publisher dates used as proxies.

## Slide 7 — Test 1: Was the signal early—and earlier than news? — 55 seconds

On slide: Days before Belmont planning approval:
Recovered county notice: 427 / Recovered industry article: 552.
Industry news was 125 days earlier.

Visual: two bars or a timeline ending at April 10, 2024 approval.

Speaker notes: “Notice time is approval date minus notice date. The main January
issue is seventy-five days before Belmont's approval. Looking further back,
a recovered February 2023 county notice is four hundred and twenty-seven days
before approval. But an industry article is dated October 2022: five hundred and
fifty-two days before approval. It is earlier by one hundred and twenty-five days.
This case therefore shows advance notice but no discovery advantage over news.
These are recovered publisher dates, not proof of the earliest mention anywhere.
We measured planning approval, not construction completion or a purchase.”

Footer: County February 8, 2023 newsletter; April 11, 2024 release; DCD October 6,
2022 article; early_notice_summary.json. Small selected case; date assumptions apply.

## Slide 8 — Test 2: Did the shortlisted projects actually progress? — 50 seconds

On slide:
Belmont Innovation — approval + contractor scope reported.
Landbay KK — conditional site-plan approval.
CyrusOne Broadlands — proposal described; physical outcome unresolved.
Construction/completion quality: not yet validated.

Visual: three-row evidence table; no green “built” checkmarks or success percentage.

Speaker notes: “You also need to check signal quality: do the projects actually
progress? I followed up all three investigation items. Belmont has approval
evidence and a contractor reporting a finishing-and-sealants scope. Landbay KK
has conditional site-plan approval reported in 2025. CyrusOne remains a described
proposal in recovered sources. None of these establishes a verified construction
start or completion under our evidence standard. That means unresolved outcomes,
not three failures. We cannot calculate construction precision or recall yet.
Approval, contractor engagement and a completed building are different evidence.”

Footer: County approval release; Sparkle Painting public company update; November
3, 2025 Ashburn newsletter; October 11, 2026 Broad Run bulletin; quality_followup.csv.
Checked October 14, 2026. Exact contractor post date not recovered.

## Slide 9 — The customer value and competitive edge still need testing — 40 seconds

On slide: DC Byte: global supplier/project intelligence.
Coco pilot: local source-linked rules and updates.
Customer interviews: not yet conducted.

Visual: small two-column comparison; no invented ROI or superiority claim.

Speaker notes: “DC Byte already advertises early project alerts, segmentation,
supplier relationships and prioritization. It also describes analyst research
and industry engagement. Our intended use substantially overlaps. We have a
small inspectable prototype, not a demonstrated advantage over its product.
Customer interviews have not been conducted. A clearer investigation list or
useful project update could help a supplier, but saved time and additional sales
are untested. We have neither proven commercial alpha nor ruled out value.”

Footer: DC Byte Supplier Analytics and FAQ, checked October 14, 2026; Coco.ai results.

## Slide 10 — Plause feedback made the explanation more specific — 25 seconds

On slide:
Unclear signal/narrative → one use case, explicit steps.
Validate the metric → separate timing and outcome quality.
Compare existing products → explicit DC Byte overlap.

Visual: three feedback-to-response pairs.

Speaker notes: “Plause feedback asked for clearer signal explanation and narrative,
how the final metric would be validated, and comparison with existing products.
This presentation responds with one supplier decision, explicit steps, two distinct
evaluation questions and a competitor comparison. The signal means a proposed
development worth investigating. It does not mean an imminent equipment purchase.
These are responses in this presentation; I am not claiming newly supplied
feedback caused all the earlier research.”

Footer: Plause peer feedback.

## Slide 11 — What will it take to validate the idea? — 45 seconds

On slide:
Verify dates and interpretations.
Match construction outcomes; test unseen cases.
Interview suppliers; compare their workflow.
Continue, revise or pivot based on evidence.

Visual: four concise risk-to-action rows; deployment is gated by validation.

Speaker notes: “First, independently check the source dates and interpretations.
Second, match candidates to dated construction or completion evidence and follow
both shortlisted and comparison projects to the same cutoff. Keep unknowns separate,
then estimate how many alerts genuinely progress and which relevant projects we
miss. Third, ask suppliers when outreach is useful and what they already know.
Compare decision quality and review time with their current workflow. If updates
to known projects help, test that decision. If existing tools already solve it,
change direction. Equipment fit and purchasing forecasts remain later scope.”

Footer: Coco.ai proposed validation plan; not completed customer interviews or deployment.

## Slide 12 — Thank you — 10 seconds

On slide: Thank you / What information would change a supplier's next call?
Repository link for discussion and reproducibility.

Speaker notes: “We have working research code and inspectable evidence. Useful
sales intelligence is still the hypothesis to validate. I welcome feedback on
which supplier decision we should test next.”

Footer: github.com/snehal-jindal/alt.data_coco.ai.

## Full source URLs

- Planning API: https://logis.loudoun.gov/gis/rest/services/Projects/LOLA_DATA/MapServer/0
- Issued permits: https://logis.loudoun.gov/gis/rest/services/LMARC/LandMARC_Permits/MapServer/1
- Submitted permits: https://logis.loudoun.gov/gis/rest/services/LMARC/LandMARC_Permits/MapServer/2
- January 26 issue: https://myemail.constantcontact.com/Ashburn-District-Newsletter---January-26th--2024.html?aid=_M6Nr9sPRk8&soid=1133733712698
- February 8, 2023 issue: https://www.loudoun.gov/Archive.aspx?ADID=12779
- March 22 release: https://www.loudoun.gov/Archive.aspx?ADID=13777
- April 11 release: https://www.loudoun.gov/ArchiveCenter/ViewFile/Item/13812
- DCD: https://www.datacenterdynamics.com/en/news/sdc-capital-partners-planning-data-center-campus-in-belmont-virginia/
- Contractor self-report: https://www.linkedin.com/company/sparkle-painting-co.-inc.
- Conditional approval report: https://myemail.constantcontact.com/Ashburn-District--October-Wrap-Up-Flyer---.html?aid=DFYPIm4LYSI&soid=1133733712698
- CyrusOne follow-up: https://myemail.constantcontact.com/Broad-Run-Bulletin---October-2026.html?aid=VjdCYNcS0uo&soid=1133737022011
- DC Byte: https://www.dcbyte.com/us/supplier-analytics/
- DC Byte methodology: https://www.dcbyte.com/faq/

Availability dates are publisher-stated proxies. First versions and delivery logs
are not authenticated. Contractor scope is self-reported and not proof of finished
work. Conditional approval is separate from full approval. No cooling purchase,
construction-completion accuracy or competitor-performance claim is made.
