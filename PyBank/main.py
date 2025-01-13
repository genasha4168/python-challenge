# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
changes = []
change = 0
average_change = 0.0
previous_value = None
month_of_change = []
greatest_decrease = ["", 0]
greatest_increase = ["", 0]


# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data, delimiter=",")

    # Skip the header row
    header = next(reader)
    
    # Extract first row to avoid appending to net_change_list
    # total_months  = sum(1 for _ in reader)


    # Track the total and net change
    
    # Process each row of data
    for row in reader:
        total_months = total_months  + 1 
        value = int(row[1])
               
        # Track the total
        total_net = total_net + value
      
        # Track the net change
        if previous_value is not None:
            change = value - previous_value
            changes.append(change)        
            month_of_change = [month_of_change] + [row[0]]

        # Calculate the greatest increase in profits (month and amount)
        if change > greatest_increase[1]:
            greatest_increase[1]= change
            greatest_increase[0] = row[0]


        # Calculate the greatest decrease in losses (month and amount)
        if change < greatest_decrease[1]:
            greatest_decrease[1]= change
            greatest_decrease[0] = row[0]

        previous_value = value


# Calculate the average net change across the months
if changes:
        average_change = sum(changes) / len(changes)

# print(average_change)

# Generate the output summary

# Print the output
print("Financial Analysis\n")
print(" ")
print("---------------------\n")
print(" ")
print("Total Months: %d\n" % total_months)
print("Total: $%d\n" % total_net)
print("Average Change $%f\n" % round(average_change ,2))
print("Greatest Increase in Profit: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
print("Greatest Decrease in Profit: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write(" \n")
    txt_file.write("---------------------\n")
    txt_file.write(" \n")
    txt_file.write("Total Months: %d\n" % total_months)
    txt_file.write("Total: $%d\n" % total_net)
    txt_file.write("Average Change $%f\n" % round(average_change ,2))
    txt_file.write("Greatest Increase in Profit: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
    txt_file.write("Greatest Decrease in Profit: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))
