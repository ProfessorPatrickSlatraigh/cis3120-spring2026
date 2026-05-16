**6. Methodology**

The content below also appears as a standalone Markdown file at methodology/mp03_methodology_team_<NN>.md. Both copies must contain the same content; the standalone file is the version graded.

**6.1 Ticker-list rationale**

For the Financial Services pipeline, tickers such as FMCB, UNTY, and other small regional banks were added to the seeded list to cover more geographic areas and increase the likelihood of finding location events.

For Travel and Hospitality, JBLU and IHG were added to better represent budget airlines and international hotels, which were undercounted in the original seed.

**6.2 Search-phrase rationale**

For Financial Services, phrases such as "new office" and "branch relocation" were added to capture location events that the original seed phrases missed.

For Travel and Hospitality, "new service" and "new destination" were added to target airline route launches and new property announcements. Despite these additions, the T&H phrase set did not produce candidates that survived ticker filtering, suggesting T&H companies announce expansions through channels other than SEC 8-K filings.

**6.3 Window-experiment results**

| Industry | Window (days) | Candidates | Location Events | Est. Cost (USD) |
|---|---|---|---|---|
| Financial Services | 30 | 10 | 3 | $0.0086 |
| Financial Services | 60 | 11 | 3 | $0.0086 |
| Financial Services | 90 | 13 | 3 | $0.0086 |
| Financial Services | 180 | 28 | 6 | $0.0147 |
| Financial Services | 360 | 40 | 10 | $0.0256 |
| Travel and Hospitality | 30 | 0 | 0 | $0.0000 |
| Travel and Hospitality | 60 | 0 | 0 | $0.0000 |
| Travel and Hospitality | 360 | 0 | 0 | $0.0000 |

We started with 5.00 USD in API credits and have 3.16 USD remaining, meaning we spent about 1.84 USD total including all development and trial runs. The actual window tuning trials cost well under 0.10 USD combined, which is way below the 3.00 USD ceiling. Haiku 4.5 pricing is 1.00 USD per million input tokens and 5.00 USD per million output tokens, so the low cost makes sense given how few candidates survived the ticker filter at each window.

We chose 360 days as our final window because Financial Services did not hit 8 events until that point. We ran every window from 30 to 360 days for FS and kept getting under 8 events until the last one. For T&H we got 0 events at every window we tried so we stopped at 360 since that is the ceiling. The T&H shortfall is explained further in sections 6.4 and 6.5.

**6.4 Stage 3 classification quality per industry**

In the search 10 financial service location events were extracted and reviewed with the results from 360 days. For each of these 10 services the city and state as well as event type were filled with data. There were no false positives found in the data as each one was identified correctly as a new branch of the bank opening soon. Madison NJ and Medford MA seemed to appear multiple times showing various banks opening in the same areas. The summary showed data for each of the new banks opening and it seems that the quality for this data was good as there were 10 confirmed events after going through the 40 candidates from the filter showing a precision of 25%.

At the 360 day window, stage 1 returned 250 candidates before ticker filtering. After applying the ticker, 3 candidates remained. Claude classified aall 3 as non-location events. the likely explanation is that the 3 filitered fillings mentioned T&H tickers in passing rather than announcing a specific physical facility opening, closing, relocation, or expansion. This is conistent with the strick classification criteria in the system prompt. The shortfall at 360 days means the T&H pipeline produced no geocoded events. This limits the comparative analysis and is addressed honestly in the reflection section.

**6.5 Limitations**

T&H had zero events. Even after running 360 days, only 3 candidates made it through the ticker filter and Claude classified all 3 as not location events. Because of this we could only map Financial Services data.

The ticker filter may have been too strict. It only matches companies whose ticker appears in EDGAR's display names field. A lot of T&H companies probably filed under different names so they got dropped before even reaching Claude.

Geocoding only works for US locations. We added USA to every search so anything international would not show up on the map.

Long filings get cut off at 8000 characters. If the location info was near the end of a filing it would have been missed entirely.

Cost estimates are not exact. We only counted tokens for candidates that passed the ticker filter. The ones that got rejected also used tokens so the real cost is a little higher than what we reported.
