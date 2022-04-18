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
# Make a list for counties
county_list = []
# Make a candidate vote counter
candidate_votes = {}
# Make a county vote counter
county_votes = {}

# Winning candidate and winning count tracker
# Winning county and winning county tracker
winning_candidate = ""
winning_county = ""
winning_count = 0
winning_county_count = 0
winning_percentage = 0
winning_county_percentage = 0

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

        # make a list of counties and find total number of votes each candidate received
       county_name = row[1]
       if county_name not in county_list:
           county_list.append(county_name)
           county_votes[county_name] = 0
        
       county_votes[county_name] += 1

print(total_votes)
print(candidate_options)
print(candidate_votes)
print(county_votes)
print("----")
print(f'Vote tally check. Sum of candidate votes = {sum(candidate_votes.values())}')
print(f'Vote tally check. Sum of county votes = {sum(county_votes.values())}\n')
print(f"Election Results\n---------------------\nTotal votes: {total_votes}\n---------------------\n")
# Calculate Percentage of votes each candidate won and determine the winner
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})")
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
winning_candidate_summary = (
    f"\n-------------------------\n\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count}\n"
    f"Winning Percentage: {winning_percentage:.1f}%"
    f"\n\n-------------------------\n")
print(winning_candidate_summary)

# Calculate Percentage of votes each county won and determine the county with the largest turnout
print("County Votes:")
for county_name in county_votes:
    c_votes = county_votes[county_name]
    c_vote_percentage = float(c_votes) / float(total_votes) * 100
    print(f"{county_name}: {c_vote_percentage:.1f}% ({c_votes:,})")
    if (c_votes > winning_county_count) and (c_vote_percentage > winning_county_percentage):
        winning_county_count = c_votes
        winning_county_percentage = c_vote_percentage
        winning_county = county_name
winning_county_summary = (
    f"\n-------------------------\n"
    f"Largest County Turnout: {winning_county}\n"
    f"Winning Vote Count: {winning_county_count}\n"
    f"Winning Percentage: {winning_county_percentage:.1f}%"
    f"\n-------------------------\n")
print(winning_county_summary)

#using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:

# Write the results to the file
    txt_file.write(f"\nElection Results\n---------------------\nTotal votes: {total_votes}\n---------------------\n")
    txt_file.write("Candidate Votes:\n")
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes) * 100
        txt_file.write(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    txt_file.write(f'{winning_candidate_summary}')
    txt_file.write("County Votes:\n")
    for county_name in county_votes:
        c_votes = county_votes[county_name]
        c_vote_percentage = float(c_votes) / float(total_votes) * 100
        txt_file.write(f"{county_name}: {c_vote_percentage:.1f}% ({c_votes:,})\n")
    txt_file.write(f'{winning_county_summary}')
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