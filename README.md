# An Analysis of Election Results
Performing analysis on election result data for the state of Colorado to help Tom find the winner of the local congressional election. 

## Overview of the Project
In this analysis, we helped Tom find the following: 

1. Total number of votes cast
2. A complete list of candidates who received votes
3. Total number of votes each candidate received
4. Percentage of votes each candidate won
5. The winner of the election based on popular vote

### Additional Election Audit
Additionally, we helped Tom find the following:

1. The voter turnout for each county
2. The percentage of votes from each county out of the total count
3. The county with the highest turnout

## Resources 
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.62.0

## Summary

### Election Audit Results
![image](https://user-images.githubusercontent.com/92613639/141409826-d288074f-8fb3-42b8-a615-b6bbd270d60b.png)

The analysis of the election result shows that:
- There were 369,711 votes cast in the election. 
- The candidates were Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane.
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was Diana DeGette received 73.8% of the vote and 272,892 number of votes.

![image](https://user-images.githubusercontent.com/92613639/141411661-2c7173f2-d0e8-4016-9208-cea2735df092.png)

### Additional Election Audit Results
![image](https://user-images.githubusercontent.com/92613639/141419054-c197e30b-947e-4a45-930b-fcba6559f5cd.png)

- The county results were:
    - Jefferson county accounted for 10.5% of the vote and 38,855 number of votes.
    - Denver county accounted for 82.8% of the vote and 306,055 number of votes.
    - Arapahoe county accounted for 6.7% of the vote and 24,801 number of votes.

![image](https://user-images.githubusercontent.com/92613639/141419091-75f28cab-85ac-4d8e-af28-a87c61b98187.png)

- The county with the largest number of votes was Denver.

### Election Audit Summary
The python script is able to be used in the future for analyzing additional elections results. Assuming the data is structured similarly (same number of columns, containing the same data in the same order from column 0 to column 2) and the result you are seeking is the same, a user would be able to run this code as is on any set of data and be provided with accurate results.

Original Data:

![image](https://user-images.githubusercontent.com/92613639/141419681-6b65c5ab-8a14-44f0-8d14-6b9104b82110.png)

Potential Data:

![image](https://user-images.githubusercontent.com/92613639/141419996-a2989f97-58e3-4fb7-b446-8451a8645631.png)

However, if the data contained in the data file is in a different order, a user can simply adjust which column is being called in the following line of code:

![image](https://user-images.githubusercontent.com/92613639/141420165-770fcd9f-1d90-43a1-bea3-07c1447d322c.png)

