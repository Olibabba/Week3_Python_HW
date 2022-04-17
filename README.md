# Election_Analysis

## Overview

The tri-county area containing Jefferson, Denver, and Arapahoe counties requested a vote tabulation program to quickly calculate the vote spread, declare a winner, and audit the results. This report contains the results of the recent election with a break down by candidate and county. I will highlight relevent code to provide insight into the methods used to calculate the results. If anyone so wishes to audit my full code it is included in my public repository for review here: https://github.com/Olibabba/Week3_Python_HW/tree/main

## Election and Audit Results

The method to 

Without further delay, the results of the election are as follows:

#### Total votes: cast in this congressional election?
- 369711

#### Number and percentage of total votes for each county in the precinct.
- Jefferson: 10.5% (38,855)
- Denver: 82.8% (306,055)
- Arapahoe: 6.7% (24,801)

#### Largest County Turnout:
- Denver
- Denver Vote Count: 306055
- Denver Vote Percentage of total: 82.8%

#### Number and the percentage of the total votes each candidate received.
- Charles Casper Stockham: 23.0% (85,213)
- Diana DeGette: 73.8% (272,892)
- Raymon Anthony Doane: 3.1% (11,606)

#### Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
- Winner: Diana DeGette
- Winning Vote Count: 272892
- Winning Percentage: 73.8%

## Election and Audit Summary

```
for row in file_reader:
       total_votes += 1
```