# Modulescd
import os
import csv
from collections import Counter

# Set path for file
csvpath = os.path.join("Resources", "election_data_2.csv")
output_path = os.path.join("Resources", "output_Poll.txt")

data=[]
candidate=[]
Votes=0
output=[]


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
    a=(item+":",str(round(percentage,2))+"% "+"("+str(counter[item])+")")
    print(item+":",str(round(percentage,2))+"% "+"("+str(counter[item])+")")
    output.append(a)
    
print("-----------------------------")
print("Winner:",maximum)
print("-----------------------------")

with open(output_path, 'w', newline='') as textfile:
    textfile.write("Election Results\n")    
    textfile.write("-----------------------------\n")
    textfile.write("Total Votes: "+str(Votes))
    textfile.write("\n-----------------------------\n")
    for item in output:
        textfile.write("%s %s\n" % item)
    textfile.write("-----------------------------\n")
    textfile.write("Winner:"+maximum)
    textfile.write("\n-----------------------------\n")
    
    

