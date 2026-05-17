---

## 6. Methodology

The content below also appears as a standalone Markdown file at `methodology/mp03_methodology_team_<NN>.md`. Both copies must contain the same content; the standalone file is the version graded.

### 6.1 Ticker-list rationale

*TODO: For each industry, justify any modifications to the seeded ticker list. Identify what the seeded list undercounts or overcounts and explain how your changes address those limitations.*

&nbsp;
>We immediately realized that within the financial services tickers weree lacking crucial capital market and consumer banks like Morgan Stanley, Goldman Sachs, Citi Bank, Wells Fargo, Discover, etc.

>For the travel and hospitality tickers, we added additional tickers in order to diversify the filing search to return more events. The tickers undercounted resorts and casinos. These are prevalent hospitality and travel locations, especially resorts. By adding these tickers in, we ensure to get an accurate filings search that includes all hospitality and travel spots.

&nbsp;

### 6.2 Search-phrase rationale

*TODO: For each industry, justify any modifications to the seeded phrase list. Note any phrases that returned high-volume false positives or missed event categories the team considered important.*

&nbsp;

>We added similar action items such as "new branch, branch closure, operations center, new headquarters, etc" in order to broaden the search to include any filings related to massive operational changes within the industry that would signal a positive growth for the firm.

>We also discovered that the Travel and Hospitality phrases were all related to new expansions, diversification, etc, but, undercounted phrases that were related to selling properties, relocations, or signals to a decline in profits. As a result, we added phrases like "new aquisition,completed the aquisition,sold its,and sale of the hotel. These are missed events that are more likely to appear in filings that were related to operational changes within the industry.

&nbsp;
### 6.3 Window-experiment results

*TODO: Insert the populated `window_results` table here (as Markdown) and explain why the chosen window is appropriate. Address the cost ceiling explicitly.*

&nbsp;

industry | window_days | candidate_count | event_count | estimated_cost_ud
---------|-------------|-----------------|-------------|------------------
Financial Services|30|50 | 9| 0.135726
Travel and Hospitality|30|50 | 8| 0.124854

> This project required testing different filing windows to determine which window (in the smallest amount of time) produced the required threshold of events for a valid comparison between the industries. We tested all the available windows from 30-360 days.

> Initially, our results were less than optimal. At first, all of the filing windows produced very little events. No solutions were found until we altered the filter_candidate_by ticker function to include additional logic to handle the filings that didn't have consistent ticker metadata. We also capped the max filings to 50 to improve runtime and ensure we were not over using the API’s capabilities and staying under the $3.00 ceiling. If candidate count was increased, the run The final window time that was selected after these changes was 30 days because both industries reached the minimum target of 8 location events while staying way below the API cost requirement.

&nbsp;

### 6.4 Stage 3 classification quality per industry

*TODO: For each industry, document observed precision and any patterns in the Stage 3 classifications (false positives, false negatives, ambiguous cases). Use small numerical examples where possible.*

&nbsp;

11 geocoded events were classified as "opening" event types, 1 "closing" event, 1 "expansion" event, and 1 "acquisition" event. These were all events taht were accurately classified.


&nbsp;

### 6.5 Limitations

*TODO: Identify limitations the team encountered and discuss how each affects the comparative reflection.*

&nbsp;

We faced multiple limitations including capping the candidate count to 50 and maintaining a low cost under the $3.00 cost ceiling. These can affect the folium map and the comparative reflection by provoding limited data that will not provide us a full outlook on the geographic patterns of each industry. If we increased the candidate count and window_days, the map would display more than 17 events. This would have provided a fuller, overall picture of the financial and hospitality sectors.

---

## 7. Comparative Reflection

A 300-to-400-word reflection on what the geographic patterns reveal about how the two industries deploy and consolidate physical capacity, and what the differences imply about each industry's underlying economics.

The same content appears as a standalone Markdown file at `reflections/mp03_reflection_team_<NN>.md`.

*TODO: Write the comparative reflection here. Mere description of the maps does not earn full credit; the reflection must offer substantive interpretation grounded in the underlying business economics and address limitations honestly.*


>In the Financial Services sector, we observed mainly openings and expansions primarily concentrated along the east coast of the U.S. These locations include New York, Pennsylvania, New Jersey, Washington DC, and California. This pattern suggests that financial institutions prioritize proximity to established clientele, primarily proximity to Wall Street. Historical Ties to New York play a major role in the geographic locations of financial institutions across America. Moreover, openings and expansions in these areas indicate a mixed strategy of diversifying revenue streams, digital adoption to AI, and strategic positioning while protecting their institutions from major economic forces like inflation. We didn’t observe any closings or relocations for the Financial Services, as we did for the travel and hospitality sector. Overall, these financial institutions could be keeping their focus on key economic centers like the east coast, rather than expanding westward because of inflation, foreign conflicts, and supply chain issues.

>For Travel and Hospitality, the event locations show a clear correlation with popular tourist destinations and cities that are known for leisure and professional conferences. For instance, the map showcases firms in New York, Chicago, Dallas, Houston, and Denver. New hotel openings and expansions signal some confidence in growing tourism and hospitality markets, seeking to maximize revenue. On the other hand, there is a closing as a result of severe debt and looking for ways to strategically optimize their portfolios.This may be from the high rise of inflation in the country. As consumer and income preferences change, luxury goods and experiences aren't as prioritized for the average consumer. Taking this into consideration, a wide range of hotel openings in this 30-day time frame was quite surprising for us.

>Overall, the Travel and Hospitality and Financial Services sector both have similar strategies of strategically positioning themselves in cities and states that offer large consumer markets, with established infrastructure in order to balance expansion opportunities with financial risks like inflation and changes in consumer preferences. These geographic patterns ultimately reflect how industries adapt differently to changing economic conditions while still seeking long-term growth and profitability.





