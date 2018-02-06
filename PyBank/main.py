# Modules
import os
import csv
import datetime
        
# Set path for file
csvpath = os.path.join("Resources", "budget_data_1.csv")

# The date list initialization
date_list=[]
revenue_list=[]

# Print the output header lines
print("Financial analysis")
print("-----------------------------")

# Read the first file 
with open(csvpath,'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        date_list.append(row[0])
        try:
            revenue_list.append(int(row[1]))
        except ValueError:
            continue

maximum=max(revenue_list)
dateindex_maximum=revenue_list.index(maximum)
Date_maximum=date_list[dateindex_maximum]

minimum=min(revenue_list)
dateindex=revenue_list.index(minimum)
Date=date_list[dateindex]

total_months=len(date_list)

revenue_list=map(int,revenue_list)
total_revenue=sum(revenue_list)

average_revenue=int(total_revenue/total_months)

print("Total Months: ",total_months)
print("Total Revenue: "+"$"+str(total_revenue))
print("Average Revenue Change: "+"$"+str(average_revenue))
print("Greatest Increase in Revenue: "+Date_maximum+" ($"+str(maximum)+")")
print("Greatest Decrease in Revenue: "+Date+" ($"+str(minimum)+")")

# print(date_list)
# a = datetime.datetime.strftime(date_list[2], "%mm/%d/%Y")
# print(a.month)
# print(a.year)
# print(a)

