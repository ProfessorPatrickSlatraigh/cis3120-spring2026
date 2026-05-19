


## 6.3 Window-experiment results
        industry	      window_days	    candidate_count	         event_count	    estimated_cost_usd
0	Financial Services	    360	                  84	                 3	                0.006886
1	Travel and Hospitality	360	                  59	                 8	                0.310000

The chosen window length was 360 days. This was selected because the shorter windows did not produce enough usable financial services events. At the max window of 360 days financial services only produced 3 location events, while travel and hospitality produced more than the target threshold. The estimated cost remained below $3.00. The API cost was controlled by filtering EDGAR candidates by ticker before stage 3 classification, which prevented the model from classifying every raw EDGAR result.

6.5 Limitations
One limitation that we as a team encountered was the financial services pipeline only producing 3 geocoded events, even at the 360 day window ceiling. This made the sample size of the financial services pipeline smaller when compared to the travel and hospitality pipeline.

Another limitation that we faced was the EDGAR search depending heavily on the selected ticker and phrase lists. Even though the list was expanded, the financial services ticker list still missed a lot of companies.

