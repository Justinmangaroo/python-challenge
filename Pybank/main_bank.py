import os
import csv
budget_data_csv = os.path.join(".","Resources","budget_data.csv")
# budget_data_csv = '/Users/justinmangaroo/Downloads/Starter_Code 2/PyBank/Resources/budget_data.csv'
print(budget_data_csv)

output_file = os.path.join(".","analysis","budget_report.txt")

# initialize variables
total_months = 0
total_profit = 0
previous_value = 0
total_changes = 0
greatest_increase = 0
greatest_decrease = 99999999

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
        total_months += 1
        total_profit+=float(row[1])

        current_value = float(row[1])
        change = current_value - previous_value

        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_month = row[0]


        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_month = row[0]
  



        previous_value = float(row[1])

        total_changes+=change

average_change = total_changes / total_months        

        
    


# record output
output = (
    f"Financial Analysis\n"
    f".......\n"
    f"Total Months: {total_months}\n"
    f"Total: {total_profit}\n"
    f"Average Change: {average_change}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} ({greatest_increase})\n"
    f"Greatest Increase in Profits: {greatest_decrease_month} ({greatest_decrease})\n"


)

print(output)


# saved to analysis folder
with open(output_file, "w") as txt_file:
    txt_file.write(output)