6.1 Ticker-list rationale

We started with the instructor-provided ticker lists for both industries.

For Financial Services, the list includes large banks and financial companies, but it does not include some smaller regional banks and financial firms that also appear in EDGAR filings. We added a few additional companies to better represent the full industry.

For Travel and Hospitality, the list includes major airlines, hotels, and cruise companies, but it does not fully include smaller travel and hospitality firms. We added more companies to better cover the range of businesses in this industry.

6.2 Search-phrase rationale

The original search phrases were useful, but some were too broad and returned unrelated results.

For Financial Services, we improved the phrases by focusing more on real physical location events such as branch openings, closures, office relocations, and operations changes. This reduced irrelevant results.

For Travel and Hospitality, we adjusted the phrases to better focus on real operational events like hotel openings, new routes, and expansions. This improved the accuracy of the results.

6.3 Window-experiment results

| Industry             | Window Days | Candidate Count | Event Count | Estimated Cost |
| -------------------- | ----------- | --------------- | ----------- | -------------- |
| Financial Services   | 30          | 0             | 2         | 0.5            |
| Financial Services   | 30          | 0             | 2         | 0.5            |
| Financial Services   | 60          | 0             | 3         | 0.5            |
| Financial Services   | 90         | 0             | 3         | 0.5            |
| Financial Services   | 180         | 0             | 6         | 0.5            |
| Financial Services | 360          | 0             | 5         | 0.5            |
| Travel & Hospitality | 360          | 1             | 1         | 0.5            |


We tested different time windows such as 30, 60, 90, 180, and 360 days.

Smaller windows did not produce enough location events for analysis. Larger windows produced more events but increased cost without significantly improving the results.

We selected the smallest window that produced at least 8 location events for both industries while staying within the cost limit.

6.4 Stage 3 classification quality per industry

Stage 3 worked fairly well for Financial Services.

In some cases, the model treated general mentions of cities or office locations in filings as real location events, which created a few false positives. However, it was generally able to identify clear events such as branch openings, closures, and relocations.

Overall, performance was decent, but not perfect, because financial filings often use indirect or formal language that can be harder to interpret correctly.

6.5 Limitations

The first limitation was that some tickers couldn't find from EDGAR search results. There is a trade-off between using strict filtering and relaxed filerting. We don't want to remove relevant filings nor put unrelated filings into the pipeline. The second limitation was the API cost constraint. Since we need to repeatly run and process a large number of filings. We have to be carefully on the runtime within the budget. The third limitation was stage 3 classification in which it didn't correctly identify office relocations. The final limitation was the map didn't fully show all marker activies in both industries. The public SEC filings sometimes have certain companies available.
