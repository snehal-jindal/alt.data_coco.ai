"""Transparent filing qualification; no training, purchasing probability or timing."""
import csv
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / 'data/processed/permits.csv'


def cohort(path=INPUT):
    with path.open(newline='') as stream:
        rows = list(csv.DictReader(stream))
    selected = []
    for row in rows:
        if row['permit_type'] != 'Building (Commercial)' or not row['application_date_utc']:
            continue
        day = datetime.fromisoformat(row['application_date_utc']).astimezone(ZoneInfo('America/New_York')).date()
        if 2023 <= day.year <= 2025:
            selected.append({**row, 'application_day_local': day.isoformat()})
    return sorted(selected, key=lambda r: r['permit_number'])


def baseline(row):
    return 'qualified' if row['work_class'] in {'New Construction', 'Addition'} else 'out_of_scope'


def classify(description):
    text = re.sub(r'\s+', ' ', (description or '').lower()).strip()
    text = text.replace('–', '-').replace('—', '-').replace('‑', '-')
    if not text or 'see narrative' in text:
        return 'review', 'R0: missing description or external narrative required'

    # A physical addition may coexist with interior work; do not let the
    # interior-work rule discard a clearly described new data-hall structure.
    if (re.search(r'data\s*halls?', text) and re.search(r'\baddition\b', text)
            and re.search(r'new.{0,60}(?:structure|building)', text)):
        return 'qualified', 'R1: explicit new physical structure and data-hall addition'

    if re.search(r'(?:plans|fees|building|phases).{0,100}(?:reviewed|approved|paid).{0,50}under\s+bldc-', text):
        return 'out_of_scope', 'R2: phase/occupancy record references already-reviewed parent scope'
    if re.search(r'(?:this is for|build\.)\s*(?:the\s*)?phase\s*\d', text):
        return 'review', 'R3: phase-specific description; distinct new building not established'

    dc = bool(re.search(r'data\s*(?:cent(?:er|re)|hall)', text))
    shell = bool(re.search(r'core\s*(?:/|&|and|-&-)\s*shell|core\s*shell', text))
    whole_shell = dc and shell and not re.search(r'fit\s*-?\s*out.{0,35}(?:within|scope)', text)
    whole_new = dc and bool(re.search(r'new\s+(?:\d[- ]story\s+)?(?:data\s*cent(?:er|re)|build)|construction\s+of\s+(?:a\s+)?(?:\w+\s+story\s+)?data\s*cent(?:er|re)', text))
    # Story-count alone is not a new-building signal when the same clause
    # explicitly concerns existing equipment/rooms or interior-only work.
    full_building = dc and bool(re.search(r'(?:\d|two|three|four)[ -]story.{0,35}data\s*cent(?:er|re)', text)) and not re.search(r'existing|interior|upgrades|replacement|fit\s*-?\s*out', text)
    if whole_shell or whole_new or full_building:
        # Child fit-out descriptions can quote the new core/shell parent's
        # scope. The subject of this filing must be distinguished from it.
        if re.search(r'fit\s*-?\s*out\s+scope|\bwithin\s+the\s+new\s+construction', text):
            return 'out_of_scope', 'R4: this filing is internal fit-out, quoting parent construction'
        return 'qualified', 'R5: explicit new DC building, core/shell or whole-building construction'

    if re.search(r'fit\s*-?\s*(?:out|up)|tenant\s+improvement|interior\s+(?:alterations?|renovation|buildout)|\bcolo\s+\d\s+build-out', text):
        return 'out_of_scope', 'R6: internal fit-out or alterations; no physical building addition established'

    if re.search(r'guard\s*(?:house|booth|shack)|switching\s+station|sewer\s+pump\s+station|equipment\s+yard|gen\s+yard|generator\s+yard\s+screen|retaining\s+wall|monument\s+sign|directional\s+sign|temporary.{0,50}(?:tent|shelter)|lunch\s+tent|crash\s+rated|security\s+(?:hardening|upgrades|wedge|turnstiles)|vehicular\s+security|traffic\s+(?:control\s+)?arm|pedestrian\s+gates|gate\s+assembly', text):
        return 'out_of_scope', 'R7: standalone site support/security structure'
    if re.search(r'replace|replacement|remediation|demoli|\bdemo\b|rack\s+install|cable\s*tray|containment|water\s+treatment|chlorination|photovoltaic|nitrogen\s+vent|customer\s+cage|electrical\s+equipment.{0,60}upgrades|busway\s+upgrades|new\s+ductwork|air\s+handler\s+undeferral|electrical\s+room\s+undeferral|\bacc\s+\d\s+chiller|systems\s+furniture|restroom\s+renovation|permanent\s+stairs|sound\s+wall|communications\s+cabling|single\s+story\s+pre-engineered\s+office', text):
        return 'out_of_scope', 'R8: equipment/interior/routine work rather than a new DC building'
    return 'review', 'R9: text insufficient to establish building use or physical scope'


def write_csv(path, rows):
    if not rows:
        return
    with path.open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main():
    rows = []
    for r in cohort():
        decision, reason = classify(r['description_current'])
        rows.append({
            'permit_guid': r['permit_guid'], 'permit_number': r['permit_number'],
            'application_day_local': r['application_day_local'], 'parcel_pin': r['parcel_pin'],
            'baseline_decision': baseline(r), 'rule_decision': decision, 'rule_reason': reason,
            'description_current': r['description_current'], 'source_url': r['source_url'],
            'retrieved_at_utc': r['retrieved_at_utc'],
        })
    write_csv(ROOT / 'data/processed/qualification_predictions.csv', rows)
    write_csv(ROOT / 'data/processed/qualified_filings.csv', [r for r in rows if r['rule_decision'] == 'qualified'])
    write_csv(ROOT / 'data/processed/review_queue.csv', [r for r in rows if r['rule_decision'] == 'review'])
    print(f'Qualified {sum(r["rule_decision"] == "qualified" for r in rows)} / {len(rows)} filings; see review_queue.csv.')


if __name__ == '__main__':
    main()
