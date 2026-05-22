---

## 6. Methodology

The content below also appears as a standalone Markdown file at `methodology/mp03_methodology_team_18.md`. Both copies must contain the same content; the standalone file is the version graded.

### 6.1 Ticker-list rationale

We used the seeded ticker lists for both industries. The Financial Services list covers banks, asset managers, insurers, and payment companies, which fits the project focus on branches, offices, and operations centers. The Travel and Hospitality list covers hotels, cruise lines, airlines, and online travel firms, which fits the focus on hotels, resorts, routes, terminals, and travel capacity.

We did not expand the ticker lists because the team hit an Anthropic API credit limitation during Stage 3. Expanding the lists would have increased the number of filings requiring classification.


### 6.2 Search-phrase rationale

Financial Services phrases focused on branch openings, branch closures, branch consolidations, regional offices, office closures, operations centers, data centers, and new locations.

Travel and Hospitality phrases focused on new properties, hotel openings, resort openings, property openings, brand conversions, new routes, gateways, terminals, and grand openings.

These phrase lists were kept industry-specific because location events are described differently across the two sectors.


### 6.3 Window-experiment results

| industry | window_days | candidate_count | event_count | estimated_cost_usd |
|---|---:|---:|---:|---:|
| Financial Services | 360 | 1 | 0 | 0.00 |
| Travel and Hospitality | 360 | 3 | 0 | 0.00 |

At the 360-day window, EDGAR search, ticker filtering, and SEC exhibit fetching worked. Financial Services produced 250 raw candidates and 1 filtered candidate. Travel and Hospitality produced 250 raw candidates and 3 filtered candidates.

Stage 3 Claude extraction failed because the available Anthropic account had insufficient credits. Therefore, the zero event counts are not interpreted as true zero-event findings.


### 6.4 Stage 3 classification quality per industry

Stage 3 classification quality could not be fully evaluated because Claude extraction did not complete. The failure occurred after SEC exhibit fetching succeeded, so the issue was isolated to the Anthropic API credit limitation rather than EDGAR search or filtering.


### 6.5 Limitations

The main limitation is that Anthropic credits prevented Stage 3 classification, so real event records could not be populated. As a result, the map code was completed using the expected `all_events` structure, but the final analytical map depends on rerunning the notebook once credits are available.

A second limitation is the small filtered candidate count at the 360-day window. Future work should expand phrases or tickers and rerun the full tuning sequence once API credits are available.
