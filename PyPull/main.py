print("Election Results")
print("----------------")

import os
import csv

# Define Variables
total_votes = 0

# Import csv files
csvpath=os.path.join('Resources', 'election_data.csv')
with open(csvpath,encoding="utf8") as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csv_reader)

# The total numbers of votes cast
    votes_per_person = {}
    for row in csv_reader:
        total_votes += 1
        if row[2] not in votes_per_person:
            votes_per_person[row[2]] = 1
        else:
            votes_per_person[row[2]] += 1

print("Total Votes: " + str(total_votes))
print("------------------")

# A complete list of candidates who received votes, the percentage of votes, and total votes
for candidate, votes in votes_per_person.items():
    print(candidate + ": " + "{:.3%}".format(votes/total_votes)
    + " (" + str(votes) +")")

print("--------------")

# The winner of the election based on popular vote
winner = max(votes_per_person, key=votes_per_person.get)

print(f"Winner: {winner}")
print("----------------")

# Export to .txt file
f = open("election_results.txt", "w")
f.write("Election Results")
f.write('\n')
f.write("--------------------")
f.write('\n')
f.write("Total Votes: " + str(total_votes))
f.write('\n')
f.write("--------------------")
f.write('\n')

for candidate, votes in votes_per_person.items():
    f.write(candidate + ": " + "{:.3%}".format(votes/total_votes)
    + " (" + str(votes) +")")
    f.write('\n')

f.write("--------------------")
f.write('\n')
f.write(f"Winner: {winner}")
f.write('\n')