# Modules
import os
import csv
from itertools import zip_longest
import datetime
import re

# Set path for file
csvpath_1 = os.path.join("Resources", "employee_data2.csv")
output_path = os.path.join("Resources", "output_employee.csv")

# Initialize lists
Emp_Id=[]
Name=[]
FirstName=[]
LastName=[]
DOB=[]
SSN=[]
State=[]

# Read the first file 
with open(csvpath_1,'r', newline="") as csvfile_1:
    csvreader_1 = csv.reader(csvfile_1, delimiter=",")
    next(csvreader_1, None)
    for row in csvreader_1:
        Emp_Id.append(row[0])
        Name.append(row[1])
        DOB.append(row[2])
        SSN.append(row[3])
        State.append(row[4])

for item in Name:
    loc = Name.index(item)
    a=Name[loc].split(" ",2)
    FirstName.append(a[0])
    LastName.append(a[1])

for item in DOB:
    loc = DOB.index(item)
    dt = datetime.datetime.strptime(DOB[loc], '%Y-%m-%d').strftime('%m/%d/%Y')
    DOB.remove(item)
    DOB.insert(loc,dt)

for item in SSN:
    loc = SSN.index(item)
    sn=item[-5:]
    encryption="***-**"+sn
    SSN.remove(item)
    SSN.insert(loc,encryption)    

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}     
for item in State:
    loc = State.index(item)
    for key,value in us_state_abbrev.items():
        if item==key:
            sta=value
    State.remove(item)
    State.insert(loc,sta)



newlist=[Emp_Id,FirstName,LastName,DOB,SSN,State]
export_data=zip_longest(*newlist, fillvalue='')

with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')     
    csvwriter.writerow(("Emp ID","First Name","Last Name","DOB","SSN","State"))
    csvwriter.writerows(export_data)
       

