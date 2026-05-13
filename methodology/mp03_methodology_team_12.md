# MP03 Methodology — Team 12
CIS 3120 — Programming for Analytics · Baruch College

## 1. Ticker List Rationale

**Financial Services.** The instructor seed covered retail-banking well (JPM, BAC, WFC, C,
PNC, USB, TFC) but was acknowledged to undercount capital-markets activity. We added Goldman
Sachs (`GS`) and Morgan Stanley (`MS`) to capture trading floor and advisory office
relocations, which are structurally different from retail branch closures. We also added `RF`
(Regions Financial) for broader regional-bank geographic coverage, and `SQ`/`PYPL` for
fintech-sector operations centers, which have been a notable category of 8-K location
disclosures.

**Travel & Hospitality.** The seed was strong on hotels and airlines. We added `JBLU`
(JetBlue) to capture a budget carrier whose route-launch cadence differs from the legacy
majors. We added `MGM`, `WYNN`, and `LVS` (casino-resort operators) because they file
location-specific 8-Ks for casino openings and resort expansions that are qualitatively
similar to hotel openings but represent a distinct sub-segment.

## 2. Search-Phrase Rationale

**Financial Services.** Extended with `"technology center"`, `"trading floor"`,
`"advisory office"`, and `"wealth management office"` to capture capital-markets and
private-bank events underrepresented in the retail-banking seed.

**Travel & Hospitality.** Extended with `"new destination"`, `"casino opening"`,
`"homeport"`, and `"new port"` to cover cruise-port and casino sub-segments and improve
event-type precision in Stage 3.

## 3. Window-Tuning Results

See the window-experiment results table in notebook Section 4. The chosen window is the
smallest at which both industries reached ≥ 8 geocoded location events, subject to the
$3.00 cumulative API cost ceiling.

## 4. Stage 3 Classification Quality

**Financial Services.** False positives were most common for `"data center"` hits in
IT-contract contexts. `"Operations center"` had moderate precision; some investor-day
filings were misclassified.

**Travel & Hospitality.** Classification was generally clean. `"Brand conversion"` generated
noise when filings described franchise terms without a specific city; Claude correctly
rejected these when no city was extractable.

## 5. Limitations

1. Short windows may yield fewer than 8 events per industry; any shortfall is documented in
   the results table.
2. Geocoding is U.S.-only; international locations are excluded from the map.
3. Claude Haiku may misclassify a small fraction of event types; spot-checking is
   recommended before final submission.
