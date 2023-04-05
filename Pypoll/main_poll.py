import os
import csv
election_data_csv = os.path.join(".","Resources","election_data.csv")
# election_data_csv = '/Users/justinmangaroo/Downloads/Starter_Code 2/Pypoll/Resources/election_data.csv'
print(election_data_csv)

output_file = os.path.join(".","analysis","election_report.txt")


# Declare Variables 
total_votes = 0 
charles_votes = 0
Diana_votes = 0
Raymon_votes = 0


#open and read csv
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)

   















# record output
output = (
    f"Election Results\n"
    f".......\n"

)

print(output)


# saved to analysis folder
with open(output_file, "w") as txt_file:
    txt_file.write(output)