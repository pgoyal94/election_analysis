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

# Open the election results and read the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)



# Close the file.
election_data.close()





# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:
#      # Write three counties to the file.
#      txt_file.write("Counties in the election\n----------------------------\nArapahoe\nDenver\nJefferson")

# # Close the file
# txt_file.close()