## MP03 Methodology - Team 16

### Financial Services Pipeline - Chinmoy Chowdhury

#### 6.1 Ticker-list rationale

The Financial Services ticker list was extended from 14 to 28 companies. The original seed focused on large national banks, payments, insurance, and asset management firms, but the first live runs showed that many physical branch announcements come from regional and community banks. The team kept the original seed, added Goldman Sachs (GS), Morgan Stanley (MS), and Charles Schwab (SCHW) for capital-markets and brokerage coverage, and added NKSH, UNTY, FMCB, HNVR, MCB, FUNC, WSBK, WSBC, PGC, JUVF, and BRO because those companies produced finance-sector branch, office, or financial-center filings during tuning.

#### 6.2 Search-phrase rationale

Two Financial Services phrases were added: "financial center" and "wealth management office". These phrases catch banking and brokerage location announcements that do not always use the word branch. The original data-center phrase produced many false positives before ticker filtering, so the final pipeline strictly filters every candidate by ticker before sending it to Claude.

#### 6.3 Financial Services window results

| industry | window_days | candidate_count | event_count | estimated_cost_usd |
|---|---:|---:|---:|---:|
| Financial Services | 30 | 12 | 11 | 0.0320 |

The 30-day Financial Services trial passed the 8-event target and stayed well under the cost ceiling. For the final common 180-day window, Financial Services produced 25 ticker-filtered candidates, 18 classified events, and 15 geocoded map events.

#### 6.4 Financial Services classification quality

In the 30-day window trial, 12 ticker-filtered candidates produced 11 classified location events, and 10 geocoded successfully. In the final 180-day common-window run, 25 candidates produced 18 classified events and 15 geocoded events. The stricter ticker filter removed thousands of unrelated EDGAR search hits before classification, which improved sector accuracy and prevented unrelated companies from appearing as Financial Services markers.

### Travel and Hospitality Pipeline - Rahim

#### 6.1 Ticker-list rationale

The Travel and Hospitality ticker list was extended from 14 to 21 companies. The original seed covered hotels, cruise lines, airlines, and online travel companies, but live tuning showed that many recent location events came from gaming, entertainment venues, hospitality real estate, and lodging-adjacent operators. The team added PENN, BALY, GLPI, VENU, CWD, HHH, and TH to capture casino openings, venue openings, hotel developments, and hospitality property activity.

#### 6.2 Search-phrase rationale

The seeded phrases were kept because they cover the main location events for this industry: new hotels, resort openings, property openings, brand conversions, new routes, gateways, terminals, and grand openings. The final code pairs those broad phrases with strict ticker filtering so unrelated companies found by generic phrases such as "grand opening" are removed before classification.

#### 6.3 Travel and Hospitality window results

| industry | window_days | candidate_count | event_count | estimated_cost_usd |
|---|---:|---:|---:|---:|
| Travel and Hospitality | 30 | 2 | 2 | 0.0052 |
| Travel and Hospitality | 60 | 3 | 3 | 0.0077 |
| Travel and Hospitality | 90 | 7 | 7 | 0.0187 |
| Travel and Hospitality | 180 | 10 | 9 | 0.0264 |

The 30-day, 60-day, and 90-day windows did not reach the 8-event target. The 180-day window reached the target with 9 classified location events, all of which geocoded successfully. The Travel and Hospitality cumulative window-tuning cost was about $0.0580. Including the Financial Services 30-day trial, the cumulative window-tuning cost across both industries was about $0.0899, below the $3.00 limit.

#### 6.4 Travel and Hospitality classification quality

The final 180-day Travel and Hospitality run produced 10 ticker-filtered candidates, 9 classified events, and 9 geocoded events. The stricter ticker filter removed thousands of nonmatching search hits before Claude classification, which fixed the earlier problem where unrelated companies appeared in the Travel and Hospitality layer.

#### 6.5 Limitations

The pipeline is limited to US geocoding, so international hotel, airline, cruise, and banking activity can be dropped even when the filing is relevant. The two sectors also use different location language: Financial Services uses branch, office, and financial-center wording, while Travel and Hospitality uses hotel, venue, property, route, and grand-opening language. Another limitation is that the exhibit text is truncated to 8,000 characters, so long filings may lose location details that appear later in the document. The final map contains 24 geocoded events: 15 Financial Services events and 9 Travel and Hospitality events.
