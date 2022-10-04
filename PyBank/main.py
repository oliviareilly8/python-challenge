# Print the title lines as shown in the instructions
print("Financial Analysis")
print("------------------")

# Import modules and files
from datetime import date
from operator import index
import os
import csv

# import and open budget_data from Resources folder
budget_data_csv = os.path.join('Resources', 'budget_data.csv')
with open(budget_data_csv,encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

# Make budget_data a list
with open(budget_data_csv, newline="") as f:
    reader = csv.reader(f)
    data = list(reader)

# The total number of months included in the dataset
reader = csv.reader(open(budget_data_csv))
linecount = len(list(reader))-1

print(f"Total Months: {linecount}")

# The net total amount of "Profit/Losses" over the entire period (total income)
sum = 0
for index, row in enumerate(data):
    if index != 0:
        current = (row[1])
        sum += int(current)

print(f"Total: ${sum}")

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
index = 0
total_change = 0
for index, row in enumerate(data):
    if(index > 1):
        previous_row = data [index-1]
        a = previous_row[1]
        b = row[1]
        change = int(a) - int(b)
        total_change = total_change + change

average_change = total_change/linecount

print(f"Average Change: ${average_change}")

# The greatest increase in profits over the entire period
index = 0
greatest_increase = 0
greatest_increase_index = 0
for index, row in enumerate(data):
    if index != 0:
        current_value = row[1]
        current_value_int = int(current_value)
        if current_value_int > greatest_increase:
            greatest_increase = current_value_int
            greatest_increase_index = index

greatest_increase_line_data = data[greatest_increase_index]
greatest_increase_value = greatest_increase_line_data[1]
greatest_increase_date = greatest_increase_line_data[0]
print(f"Greatest Increase in Profits: {greatest_increase_date, greatest_increase_value}")

# The greatest decrease in profits over the entire period
index = 0
greatest_decrease = 0
greatest_decrease_index = 0
for index, row in enumerate(data):
    if index != 0:
        current_value_decrease = row[1]
        current_value_int_decrease = int(current_value_decrease)
        if current_value_int_decrease < greatest_decrease:
            greatest_decrease = current_value_int_decrease
            greatest_decrease_index = index

greatest_decrease_line_data = data[greatest_decrease_index]
greatest_decrease_value = greatest_decrease_line_data[1]
greatest_decrease_date = greatest_decrease_line_data[0]
print(f"Greatest Decrease in Profits: {greatest_decrease_date, greatest_decrease_value}")

# Export to .txt file
f = open("budget_results.txt", "w")
f.write("Financial Analysis")
f.write('\n')
f.write("--------------------")
f.write('\n')
f.write(f"Total Months: {linecount}")
f.write('\n')
f.write(f"Total: ${sum}")
f.write('\n')
f.write(f"Average Change: ${average_change}")
f.write('\n')
f.write(f"Greatest Increase in Profits: {greatest_increase_date, greatest_increase_value}")
f.write('\n')
f.write(f"Greatest Decrease in Profits: {greatest_decrease_date, greatest_decrease_value}")
f.write('\n')