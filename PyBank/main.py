#import 
import os
import csv

#use budget_data.csv 
budget_csv = os.path.join("Pybank", "Resources", "budget_data.csv")

#Display header for analysis
print("Financial Analysis\n--------------------------")


#Open and read csv
with open(budget_csv) as budget_file:
    budget_reader = csv.reader(budget_file, delimiter=",")


    #Count the number of months by counting the rows, skipping the header row
    num_months = -1
    for row in budget_reader:
        num_months += 1

    #Display the total number of months    
    print(f"Total Months: {num_months}")

    #Total the amount of "Profit/Losses" -- I think I need to organize the "column" into a list so something like .zip? but the reverse of that
    net_total = sum()
    #for row in budget_reader:
    #    net_total += float(row.split()[1])
        

    #Display the net total amount of "Profit/Losses"
    print(f"Total: ${net_total}")

#Display the average of changes in "Profit/Losses"


#Output the greatest increase in profits (date and amount) over the entire period


#Output the greatest decrease in profits (date and amount) over the entire period


#Export a textfile of results to "analysis" folder

print ("Yay! No bugs!")