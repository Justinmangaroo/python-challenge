import os
import csv
election_data_csv = os.path.join(".","Resources","election_data.csv")
# election_data_csv = '/Users/justinmangaroo/Downloads/Starter_Code 2/Pypoll/Resources/election_data.csv'
print(election_data_csv)

output_file = os.path.join(".","analysis","election_report.txt")


# Initialize Variables 
total_votes = 0 
charles_votes = 0
diana_votes = 0
raymon_votes = 0


#open and read csv
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")
    csv_header = next(csv_reader)

    # Skip the header so we iterate through the actual values
    header = next(csv_reader)     

    # Iterate through each row in the csv
    for row in csv_reader: 

        # Total vote count
        total_votes +=1

        # Individual Voter count
        if row[2] == "Charles Casper Stockham": 
            charles_votes +=1
        elif row[2] == "Diana DeGette":
            diana_votes +=1
        elif row[2] == "Raymon Anthony Doane": 
            raymon_votes +=1
        

 # Make a dictionary of the two lists
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane",]
votes = [charles_votes, diana_votes,raymon_votes,]

# Calculate the winner 
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Percentage of each candidate
charles_percent = (charles_votes/total_votes) *100
diana_percent = (diana_votes/total_votes) * 100
raymon_percent = (raymon_votes/total_votes)* 100









# record output
output = (
    f"Election Results\n"
    f"..............\n"
    f"Total Votes: {total_votes}\n"
    f"..............\n"
    f"Charles Casper Stockham: {charles_percent:.3f}% ({charles_votes})\n"
    f"Diana DeGette: {diana_percent:.3f}% ({diana_votes})\n"
    f"Raymon Anthony Doane: {raymon_percent:.3f}% ({raymon_votes})\n"
    f"..............\n"
    f"Winner: {key}\n"
    f".............."

)

print(output)


# saved to analysis folder
with open(output_file, "w") as txt_file:
    txt_file.write(output)


    txt_file.write(f"Election Results\n")
    txt_file.write(f"..............\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write(f"..............\n")
    txt_file.write(f"Charles Casper Stockham: {charles_percent:.3f}% ({charles_votes})\n")
    txt_file.write(f"Diana DeGette: {diana_percent:.3f}% ({diana_votes})\n")
    txt_file.write(f"Raymon Anthony Doane: {raymon_percent:.3f}% ({raymon_votes})\n")
    txt_file.write(f"..............\n")
    txt_file.write(f"Winner: {key}")
    txt_file.write(f"..............")
