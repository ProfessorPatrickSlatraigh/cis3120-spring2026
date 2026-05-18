## Methodology

### 1. Ticker List Rationale
Financial Services seed list covers money-center banks (JPM, BAC, WFC, C),
regional banks (PNC, USB, TFC), asset managers (BLK, BX), insurers (MET, PRU),
and payments companies (V, MA, AXP). Extended to include capital markets firms
(MS, GS), custody/servicing (STT, BK), brokerage (SCHW, COF), and fintech (PYPL).
Travel and Hospitality seed covers hotels (MAR, HLT, H, CHH, WH), cruise lines
(CCL, RCL, NCLH), airlines (DAL, UAL, AAL, LUV), and online travel (BKNG, EXPE).
Extended to include ABNB, TRIP, and ALGT for broader coverage.

### 2. Search Phrase Rationale
Standard seed phrases like "new branch" and "new property" returned zero matches
for our target tickers because large public companies file 8-Ks using company-name
anchored language. Phrases were rewritten as company-name plus action pairs
(e.g. "Hilton" "opening", "Wells Fargo" "branch") which successfully returned
filings from target companies. Several EDGAR queries returned 500 errors due to
server-side limitations on multi-word phrase searches; these were caught and skipped.

### 3. Window-Tuning Results

| industry | window_days | candidate_count | event_count | estimated_cost_usd |
|---|---|---|---|---|
| Financial Services | 30 | 0 | 0 | 0.00 |
| Travel and Hospitality | 30 | 0 | 0 | 0.00 |
| Financial Services | 60 | 0 | 0 | 0.00 |
| Travel and Hospitality | 60 | 0 | 0 | 0.00 |
| Financial Services | 90 | 0 | 0 | 0.00 |
| Travel and Hospitality | 90 | 0 | 0 | 0.00 |
| Financial Services | 180 | 4 | 0 | 0.00 |
| Travel and Hospitality | 180 | 1 | 0 | 0.00 |
| Financial Services | 360 | 19 | 1 | 0.20 |
| Travel and Hospitality | 360 | 49 | 5 | 0.20 |

Chosen window: 360 days (maximum allowed).
Justification: Smaller windows produced zero candidates for both industries.
The 8-event threshold was not reached for either industry at 360 days.
This shortfall is acknowledged below.

### 4. Stage 3 Classification Quality
Claude correctly identified location events from hotel and airline filings.
Financial Services filings were predominantly financial supplements and earnings
reports rather than location announcements, resulting in low recall for that
industry. Travel and Hospitality filings more frequently contained explicit
location language (city names, property openings, route launches).

### 5. Limitations
The 8-event threshold was not reached: Financial Services produced 1 geocoded
event and Travel and Hospitality produced 5, both below the 8-event target.
This occurred because large public companies in our ticker lists rarely file
8-K exhibits that explicitly announce individual branch or property locations
in searchable plain text. The EDGAR full-text search also returned 500 errors
for several high-traffic phrase combinations, reducing recall further.
The comparative map reflects a sparse but real sample of location-related
disclosures from each industry.