# The data to retireive
# 1. Count total number of votes cast
# 2. List of all candidates who received votes
# 3. The percentage of votes cast for each candidate
# 4. Total votes for each candidate
# 5. Winner of the election by popular vote - most votes
# Assign a varialbe for file to load
import csv
import os
# file from path
#file_to_load = os.path.join("Resources", "election_results.csv")
# file to save
#file__to_save - os.path.join("Resources", "election_analysis.txt")
#
import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Analysis", "election_analysis.txt")
# set vote counter to zero
total_votes = 0
#Get Candidate Names - empty list
candidate_options = []
#Empty dictionary for candidate and votes
candidate_votes ={}
#Winning Candidate adn count tracker varialbes initialized
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#open election data file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
        total_votes +=1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
#
#Determine winning vote count and candidate
#Determine if the votes is greater than the winning count
    if(votes > winning_count) and (vote_percentage > winning_percentage):
        #if true then set winning count = votes and percent = vote percent
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name



winning_candidate_summary = (
    f"-----------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"------------------------\n")
print(winning_candidate_summary)

