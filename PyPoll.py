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
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
