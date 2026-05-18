# MP03 Methodology — Team 17

## 6.1 Ticker-list rationale

**Financial Services:** We started with big banks like JPM and BAC but found they don't file location-related 8-Ks. We switched to smaller regional banks like NKSH, LKFN, and ACNB because they regularly announce branch openings and closures in their filings.

**Travel and Hospitality:** We started with hotel chains and airlines like MAR, HLT, and DAL. We added casino companies like CZR, BALY, and PENN because they file 8-Ks for new property openings. Even with these additions, we only found 4 events at the 360-day ceiling.

## 6.2 Search-phrase rationale

**Financial Services:** We kept the seeded phrases like "new branch", "branch closure", and "branch consolidation". These worked well for regional banks. "New location" returned some false positives but was kept for recall.

**Travel and Hospitality:** We kept the seeded hotel phrases and added "new casino", "casino opening", "new resort", "new destination", and "new flight" to capture gaming and airline activity.

## 6.3 Window-experiment results

| industry | window_days | candidate_count | event_count | estimated_cost_usd |
|---|---|---|---|---|
| Financial Services | 30 | 8 | 2 | 0.02 |
| Financial Services | 180 | 23 | 7 | 0.06 |
| Travel and Hospitality | 180 | 10 | 5 | 0.03 |
| Travel and Hospitality | 360 | 12 | 4 | 0.03 |

We chose 360 days as the final window. Total cost was approximately $0.14, well below the $3.00 ceiling.

## 6.4 Stage 3 classification quality per industry

**Financial Services:** Out of 23 candidates at 180 days, 7 were classified as genuine location events. False positives were filings that mentioned locations only in passing.

**Travel and Hospitality:** Out of 12 candidates at 360 days, 4 were classified as genuine location events. Some false positives were filings that mentioned locations in a financial context.

## 6.5 Limitations

- Travel and Hospitality fell short of the 8-event target even at 360 days.
- Large banks like JPM were excluded because they don't file location-specific 8-Ks.
- The professor confirmed that low T&H activity is acceptable.
