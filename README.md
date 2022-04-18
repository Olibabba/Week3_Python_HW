# Election_Analysis

## Overview

The tri-county area containing Jefferson, Denver, and Arapahoe counties requested a vote tabulation program to quickly calculate the vote spread, declare a winner, and audit the results. This report contains the results of the recent election with a break down by candidate and county. I will highlight relevent code to provide insight into the methods used to calculate the results. If anyone so wishes to audit my full code it is included in my public repository for review here: https://github.com/Olibabba/Week3_Python_HW/tree/main

## Election and Audit Results

A great thing about election data is it's simplicity. With each vote occupying one row, we can capture all of our data by analyzing each row in one pass. In fact counting the total votes is essentialy as easy as this short code:
```
for row in file_reader:
       total_votes += 1
```
Creating a list of candidates and tallying their votes is only a little more complicated:
```
       candidate_name = row[2]
       if candidate_name not in candidate_options: 
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

       candidate_votes[candidate_name] += 1
```
The county tally is nearly identical to the candidate tally above. Of course much of the complexity comes in the planning. In order to complete the analysis and calculations in one pass, we needed to initialize and manage 11 variables!

More details can be found in the summary below. So W=without further delay, the results of the election are as follows:

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

The results above were also written to a .txt document in order to facilitate sharing of the results. Because I know you're curious (and because it was actually the most complicated portion), I will share the code here:

![Write to txt code]{https://github.com/Olibabba/Week3_Python_HW/blob/main/Resources/Write_txt_code.png}

## Election and Audit Summary

I think it is clear that this proof of concept was a success, and I believe that with some modifications the accuracy and time saved could be brought to any election. I propose that *Olibabba Original Outomes &copy;* be hired to expand upon this success to add a versatile election auditing solution to your toolbelt.

There are two primary changes needed to make this program usable on any election:

-- Add functionality to input which column the cadidate and county is in, in case the csv format is not the same as this one.

-- Adjust the code to parse multiple elections and precints in one data set.. 

As you can see from my examples above, I can also create multiple documents and summaries to be distrubuted to an email list or website of your choosing immedietly upon completion of the audit.

My one and only offer to do this comes at the low price of **Exposure!**