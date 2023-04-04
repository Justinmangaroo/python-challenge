import os
import csv
budget_data_csv = os.path.join(".","Resources","budget_data.csv")
# budget_data_csv = '/Users/justinmangaroo/Downloads/Starter_Code 2/PyBank/Resources/budget_data.csv'
print(budget_data_csv)

output_file = os.path.join(".","analysis","budget_report.txt")

# initialize variables
total_months = 0


#open and read csv
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)

    # print header
    print(f"Header: {csv_header}")


    # The total number of months included in the dataset
    # total_months = total_months + 1


    # iterate through all rows
    for row in csv_reader:

        # track total months
        total_months = total_months + 1


# record output
output = (
    f"Financial Analysis\n"
    f".......\n"
    f"Total Months: {total_months}\n"

)

print(output)


# saved to analysis folder
with open(output_file, "w") as txt_file:
    txt_file.write(output)