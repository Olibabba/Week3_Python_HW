import datetime

now = datetime.datetime.now()
print(f'The current time is {now}')

# Add our dependencies
import csv
import os

#A ssign a variable for the file to load and the path.
file_to_load =  os.path.join('Resources', 'election_results.csv')
# Assign a variable to the file to a path.
file_to_save = os.path.join('analysis', 'election_analysis.txt')
# Initialize a vote counter
total_votes = 0
# Make an empty list for candidates
candidate_options = []
# Make a candidate vote counter
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
 
    # Read the header row
    headers = next(file_reader)

    # Find Total number of votes cast
    for row in file_reader:
       total_votes += 1

       # make a list of candidates and #Find Total number of votes each candidate received
       candidate_name = row[2]
       if candidate_name not in candidate_options: 
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

       candidate_votes[candidate_name] += 1

print(total_votes)
print(candidate_options)
print(candidate_votes)
print(f'Vote tally check. Sum of candidate votes = {sum(candidate_votes.values())}')
# Calculate Percentage of votes each candidate won
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count}\n"
    f"Winning Percentage: {winning_percentage:.1f}%")
    #f"-------------------------\n")
print(winning_candidate_summary)


#using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:

# Write the results to the file
    txt_file.write(f"\nElection Results\n---------------------\nTotal votes: {total_votes}\n---------------------\n")
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes) * 100
        txt_file.write(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    txt_file.write(f'{winning_candidate_summary}\n---------------------\n')
    txt_file.write(f'\n-- time of last edit {now}--')
    
   
    #Declare The winner of the election based on popular vote


# Dead Code
    #election_data = open(file_to_load, 'r')

    #Close the file.
    #election_data.close()

    # Close the file
    #outfile.close()
    #txt_file.write(f'\nCounties in the Election\n---------------------\nArapahoe \nDenver \nJefferson \n-- time of last edit {now}--')
    #Candidate Options: {candidate_options}\nCandidate Votes Received: {candidate_votes}\n