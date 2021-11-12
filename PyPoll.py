#The data we need to retrieve:
#1)Total number of votes cast
#2)A complete list of candidates who received votes
#3)Total number of votes each candidate received
#4)Percentage of votes each candidate won
#5)The winner of the election based on popular vote

#import csv and os modules
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize accumulator
total_votes = 0

#1)Total number of votes cast - declare an empty dictionary
candidate_votes = {}

#2)List for candidate options
candidate_options = []

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
    
        #Increment the accumulator by 1
        total_votes += 1

        # Print the candidate name from each row 
        candidate_name = row[2]

        #Add any new name to the list of candidates
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

           #3) Begin tracking that candidate's total number of votes
            candidate_votes[candidate_name] = 0   
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1             

#4) Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    # To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #5) Determine winning vote count and candidate
    # Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent = vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)


# Close the file.
election_data.close()


# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:
#      # Write three counties to the file.
#      txt_file.write("Counties in the election\n----------------------------\nArapahoe\nDenver\nJefferson")

# # Close the file
# txt_file.close()