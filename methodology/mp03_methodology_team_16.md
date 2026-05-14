## MP03 Methodology - Team 16

### Financial Services Pipeline - Chinmoy Chowdhury

#### 6.1 Ticker-List Rationale

The Financial Services ticker list was extended from 14 to 17 companies by adding Goldman Sachs (`GS`), Morgan Stanley (`MS`), and Charles Schwab (`SCHW`). The seeded list was biased toward retail banking and undercounted capital-markets and brokerage activity. `GS` and `MS` represent large investment banks whose filings can describe office openings, relocations, and trading-floor expansion. `SCHW` adds retail brokerage coverage, including branch consolidation activity after the TD Ameritrade acquisition. No seeded tickers were removed.

#### 6.2 Search-Phrase Rationale

Two Financial Services phrases were added: `"financial center"` and `"wealth management office"`. The seed phrases emphasized branch and operations-center language, which fits banks but misses language used by brokerage, wealth-management, and capital-markets firms. The added phrases broaden retrieval while ticker filtering keeps the candidate set industry-specific.

#### 6.3 Window-Experiment Results

| industry | window_days | candidate_count | event_count | estimated_cost_usd |
|---|---:|---:|---:|---:|
| Financial Services | 30 | 259 | 52 | 0.6666 |

The 30-day Financial Services trial exceeded the target of 8 classified location events and stayed below the $3.00 team cost ceiling.

#### 6.4 Stage 3 Classification Quality

In the recorded Financial Services run, 259 ticker-filtered candidates produced 52 classified location events, and 39 of those events geocoded successfully. That is a 20.1% classified-event rate and a 75.0% geocoding rate. The lost geocodes were primarily filings that named international locations, neighborhood-level locations, or locations too ambiguous for the US-only Nominatim query. A spot-check of 10 classified events found branch openings, closings, office relocations, or other named-location events rather than generic corporate updates.

#### 6.5 Limitations

The pipeline is limited to US geocoding, so international branch and office activity is dropped. Ticker filtering can miss filings submitted under subsidiary CIKs that are not associated with the parent ticker in EDGAR search results. The 8,000-character truncation can also omit location details from unusually long press releases.
