# Modulescd
import os
import csv
from collections import Counter

# Set path for file
csvpath = os.path.join("Resources", "election_data_1.csv")

data=[]
candidate=[]
Votes=0

# Print the output header lines
print()
print("Election Results")
print("-----------------------------")

# Read the first file and count number of rows with data
with open(csvpath,'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        data.append(row[2])
        Votes+=1

print("Total Votes: "+str(Votes))
print("-----------------------------")
for item in data:
    if item not in candidate:
        candidate.append(item)

counter=dict(Counter(data))
v=list(counter.values())
k=list(counter.keys())
maximum=k[v.index(max(v))]
for item in counter:
    percentage=float(counter[item]/Votes*100)
    print(item+":",str(percentage)+"% "+"("+str(counter[item])+")")
    
print("-----------------------------")
print("Winner:",maximum)
print("-----------------------------")



