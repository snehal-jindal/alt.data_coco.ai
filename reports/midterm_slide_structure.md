# Coco.ai: midterm presentation and speaker notes

[Google Slides deck](https://docs.google.com/presentation/d/16yxMeZ2Dwdd8IzQ9tnGfU3xiDa9a28AADcd5fszQ4rA)

Eleven main slides, followed by one skipped backup. The speaking script is about seven minutes at a moderate pace. Expanded explanations are reference material, not additional narration.

## 1. Coco.ai: which projects deserve a cooling supplier’s next call?

SAY
Imagine you sell commercial cooling equipment. Someone proposes building a data center, and you want to know whether that project deserves your attention. Coco.ai would use public development information to help you choose which projects to investigate. For this midterm, I focused on new data-center buildings and substantial physical expansions in Loudoun County, Virginia. I asked how early the information appears and whether the projects progress. Eventually, I want to understand when a supplier should approach them and what equipment fits, but those are later questions.

SOURCES
Coco.ai research concept and scope.

## 2. I started with the county’s building records

SAY
I started with official county planning and permit records containing dates, identifiers and descriptions. I downloaded them in October 2026. The broad permit collection includes application dates from 2000 to 2026. I removed repeated permit IDs and flagged unusable dates, then selected 407 commercial-building filings from 2023 to 2025 for a manageable description audit. Those years were a practical starting point. This was data preparation and exploration, rather than a statistical training dataset.

SOURCES
https://logis.loudoun.gov/gis/rest/services/Projects/LOLA_DATA/MapServer/0
https://github.com/snehal-jindal/alt.data_coco.ai

## 3. The filing date did not solve the timing problem

SAY
Then I encountered a timing problem. The records contain historical application dates, but I downloaded their current descriptions in 2026. Imagine a 2024 filing originally saying construct a building, then changing in 2026 to say construct a data center. Recognizing the data center now would not prove we could recognize it in 2024. This is an illustrative example, not a recovered pair of document versions. I kept the 407-record exercise as background and looked for a source with a clear issue date.

SOURCES
https://github.com/snehal-jindal/alt.data_coco.ai

## 4. A dated newsletter gave us a smaller test

SAY
I used an Ashburn District newsletter dated January 26, 2024. The county supervisor publishes it for residents, with community news and development proposals. It contains 16 development-application entries, including housing and data-center proposals. I manually prepared the project facts with AI assistance. That gives us a small, dated starting point: if a cooling salesperson read this issue, which entries would deserve investigation? The issue date is our availability proxy; original delivery and first versions still need verification.

SOURCES
https://myemail.constantcontact.com/Ashburn-District-Newsletter---January-26th--2024.html?aid=_M6Nr9sPRk8&soid=1133733712698

## 5. A data-center mention needed a second look

SAY
First, I used a basic filter: does the entry mention a data center? Six did. Then I checked what each application actually proposed and its reported stage. Three described proposed DC buildings to investigate. One needed review, one already had approval, and one was a residential application referring to a different DC proposal. A careful reader could do this manually. The code makes that sorting repeatable using the facts I prepared. It does not automatically read websites. The possible value is maintaining useful context across many documents, which still needs testing.

SOURCES
https://myemail.constantcontact.com/Ashburn-District-Newsletter---January-26th--2024.html?aid=_M6Nr9sPRk8&soid=1133733712698
https://github.com/snehal-jindal/alt.data_coco.ai

## 6. The notice was early. The news was earlier.

SAY
For Belmont, I reconstructed the dates rather than just counting mentions. Our January newsletter appears 75 days before planning approval. An older county notice gives 427 days. But industry news already described the campus 552 days before approval, 125 days ahead of the county notice. Public documents therefore provided advance notice, but finding the name first is not the advantage demonstrated here. The useful lesson is to compare against information a supplier already has. The next question is whether official scope or stage information adds something that changes the supplier’s investigation.

FOR YOUR UNDERSTANDING
WHY THIS RESULT MATTERS
The timing test protects against building a product around information that customers already possess. It gives a baseline more demanding than merely showing that a document preceded approval. The October 6, 2022 DCD article is an ordinary public-information comparator, not a measured DC Byte alert. The recovered county notice is February 8, 2023, while the fixed screening issue is January 26, 2024. All three refer to the same campus proposal, allowing the comparison with April 10, 2024 planning approval. Notice days equal approval date minus source date. We have not authenticated first versions or original delivery logs, and cannot claim earliest-ever discovery.

POSSIBLE VALUE TO TEST
A project name may already be known. A supplier might still need a dated change in scope, approval status, project identity or a reason to investigate. Public records could contribute to that context. This case does not prove that they do, and we have not measured which additional facts the news article or an incumbent already supplied. Planning approval also does not establish an open cooling purchase window. The next test should ask whether a specific update changes a real supplier action rather than seeking more impressive lead-day numbers.

SOURCES
https://www.datacenterdynamics.com/en/news/sdc-capital-partners-planning-data-center-campus-in-belmont-virginia/
https://www.loudoun.gov/Archive.aspx?ADID=12779
https://myemail.constantcontact.com/Ashburn-District-Newsletter---January-26th--2024.html?aid=_M6Nr9sPRk8&soid=1133733712698
https://www.loudoun.gov/ArchiveCenter/ViewFile/Item/13812

## 7. The shortlist revealed different project situations

SAY
I then followed up all three shortlisted projects. Belmont has planning approval and a contractor reporting a finishing-and-sealants scope. Landbay KK has reported conditional site-plan approval. CyrusOne remains a described proposal in the sources I recovered. These are three different situations, so a useful list should show the evidence and the next question for each project. For Belmont, check the current scope and procurement stage. For Landbay, check the remaining conditions. For CyrusOne, monitor the proposal’s status. Those are suggested investigation actions. We still need dated construction evidence to test which signals reliably lead to physical progress.

FOR YOUR UNDERSTANDING
WHAT WE ACTUALLY RECOVERED
Belmont Innovation Campus: county planning approval plus Sparkle Painting’s public self-report of a finishing/sealants scope. The contractor update is an additional supplier-side clue, but its exact post/event date was not recovered and it does not confirm completed construction. Belmont Landbay KK: a November 3, 2025 Ashburn newsletter reports conditional site-plan approval on October 6, 2025. Conditional approval is a different milestone from full approval or construction. CyrusOne Broadlands: an October 11, 2026 Broad Run bulletin still describes the proposal and discussions, without confirming physical construction.

VALUE AND LIMIT
The pilot connects a shortlist to source-linked project context and exposes where further investigation is needed. The next-question column on the slide is a proposed use of that context, not an observed customer response. We have not verified physical starts/completions for these three under the current standard. Unknown does not mean failed. There is no defensible construction success rate, precision or recall yet. To evaluate quality, recover dated evidence, independently match it to the right project/building, and track both shortlisted and comparison candidates to a common cutoff. Precision needs resolved alert outcomes with unknowns reported separately. Recall additionally needs a sufficiently complete set of relevant projects that could have been missed.

SOURCES
https://www.loudoun.gov/ArchiveCenter/ViewFile/Item/13812
https://www.linkedin.com/company/sparkle-painting-co.-inc.
https://myemail.constantcontact.com/Ashburn-District--October-Wrap-Up-Flyer---.html?aid=DFYPIm4LYSI&soid=1133733712698
https://myemail.constantcontact.com/Broad-Run-Bulletin---October-2026.html?aid=VjdCYNcS0uo&soid=1133737022011

## 8. DC Byte shows why industry evidence matters

SAY
DC Byte helps explain why useful sales intelligence takes more than collecting documents. It says its analysts conduct facility reviews, market inspections, primary research and direct industry engagement. Its supplier product already offers project alerts, stage filters and supplier relationships. Our use case overlaps. The implication for Coco is that public documents can supply a traceable starting point, while supplier or developer conversations may be needed to understand the actual opportunity. That is a direction to test, not a proven gap in DC Byte. Our alpha would be information that changes a supplier’s action, and we have not measured it yet.

FOR YOUR UNDERSTANDING
WHAT DC BYTE SAYS
Its FAQ describes a global research team, facility reviews, market inspections, primary research and direct industry engagement, with ongoing review and validation. Supplier Analytics advertises alerts on new or expanding facilities, project-stage and supplier-segment filters, supplier relationships and project prioritization. These are provider descriptions, not independently measured product performance. We did not purchase its data or compare its actual alerts against ours.

WHAT THAT MEANS FOR COCO
The overlap is substantial. A simple public-document shortlist is not a demonstrated competitive advantage. My inference is that primary research can help fill the gap between a recorded development proposal and a supplier’s actual commercial decision. We need conversations to establish which facts are useful, available and underserved. Public evidence plus industry evidence is a possible research design, not a claim of novelty.

DEFINE ALPHA IN THIS PROJECT
Alpha means an incremental decision advantage: discovering an actionable opportunity earlier than the customer’s baseline, reducing investigation time without losing important projects, or supplying an update that changes whom the seller contacts, when or why. None has been validated commercially. Potential positioning such as a narrower cooling workflow, simpler evidence review or a different customer segment must emerge from research. We have not established lower cost, better coverage or a feature gap. Customer interviews have not been conducted.

SOURCES
https://www.dcbyte.com/faq/
https://www.dcbyte.com/us/supplier-analytics/

## 9. The feedback pushed me toward a clearer test

SAY
The peer feedback asked for a clearer signal, an explanation of metric validation, and a comparison with existing products. I have narrowed the signal to a proposed DC project worth investigating, separated notice timing from physical progress, and made the DC Byte overlap explicit. The next version should be judged by whether a supplier finds the evidence useful in a real decision.

FOR YOUR UNDERSTANDING
FEEDBACK CONNECTION
The actual comments asked for greater clarity about the signal/narrative, how to validate the final metric and comparison with existing products. On-slide phrases are shortened paraphrases. This presentation addresses them through a single supplier decision, a chronological account of the work, separate timing and progress tests, and explicit competitor overlap. It does not invent customer feedback or claim that newly supplied Plause comments caused all prior research.

SOURCES
Attached Plause peer-feedback screenshot.

## 10. Next: test whether the evidence changes a sales decision

SAY
The next step is a small test of one cooling supplier’s actual workflow. First, independently check the project matches, dates and extracted facts. Then follow shortlisted and comparison projects to the same cutoff, using dated construction evidence and keeping unknown outcomes separate. Freeze the rules before testing more documents. In parallel, ask suppliers what they already know, when outreach matters, and which missing facts prevent action. Compare review time and decisions with their current process. Continue if the evidence improves a decision, add industry research if that is the missing piece, or change the use case if existing tools already solve it.

FOR YOUR UNDERSTANDING
A SMALL, COMPLETE NEXT EXPERIMENT
Select one supplier decision with a cooling salesperson, such as which existing project warrants investigation this week. Record their current sources, known projects, criteria and usual review time before showing Coco’s results. Independently review a manageable new set of dated documents, preserve source versions and availability dates where possible, and match repeated application/building references. Freeze the sorting rules, then apply them before inspecting later outcomes. Include shortlisted and comparison candidates, not just projects that are easy to confirm.

FOLLOW THE EVIDENCE
Track each candidate to the same date. Collect construction-start, occupancy or completion evidence depending on the defined outcome; do not merge unlike milestones. Report unresolved cases and sample size. Evaluate whether the shortlist misses relevant projects and whether the customer gains useful context. For commercial usefulness, compare time spent and actual investigation/contact decisions against the customer’s existing workflow. Do not promise an ROI or sale from this small study.

DECISION AFTER THE TEST
If public evidence improves a decision, continue that narrow workflow. If missing status or procurement context limits usefulness, explore permissioned developer, contractor or supplier interviews and legitimate data partnerships. If incumbents already meet the need or users cannot act, revise or pivot. Equipment recommendations and purchase-window forecasting remain later scope. Deployment follows validation; more model complexity alone does not resolve unreliable dates or absent customer value.

SOURCES
https://github.com/snehal-jindal/alt.data_coco.ai

## 11. Thank you

SAY
The midterm produced a reproducible research pilot and clarified what a useful product must answer. I welcome feedback on which piece of information would actually change a cooling supplier’s next call.

SOURCES
https://github.com/snehal-jindal/alt.data_coco.ai

## 12. Backup: Belmont’s status changed over time

SAY
This optional backup shows how manually recovered documents change the status of Belmont over time. The code uses reporting-document dates, rather than assuming information was available on an earlier event date. It is an update-handling demonstration using prepared facts, not an automated monitoring platform.

SOURCES
https://www.loudoun.gov/Archive.aspx?ADID=12779
https://www.loudoun.gov/Archive.aspx?ADID=13777
https://www.loudoun.gov/ArchiveCenter/ViewFile/Item/13812
