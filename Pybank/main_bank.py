import os
import csv
budget_data_csv = os.path.join(".","Resources","budget_data.csv")
budget_data_csv = '/Users/justinmangaroo/Downloads/Starter_Code 2/PyBank/Resources/budget_data.csv'
print(budget_data_csv)
#open and read csv
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    print(f"Header: {csv_header}")
