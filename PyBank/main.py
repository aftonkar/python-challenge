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

    data = list(budget_reader)
    print(len(data))
    #Count the number of months by counting the rows, skipping the header row
    num_months = len(data) - 1
    
    #Calculate the total amount of Profits/Losses
    net_total = 0

    #
    for i in range(1, len(data)):
        num = data[i]
        net_total += int(num[1])
    
    #Display the average of changes in "Profit/Losses"
    counter = 0
    total = 0

    for i in range(1, len(data) - 1):
        num = data[i]
        next_num = data[i + 1]
        total += float(next_num[1]) - float(num[1])

        counter = i

    average_change = total/counter

    #Display the total number of months    
    print(f"Total Months: {num_months}")

    #Display the net total amount of "Profit/Losses"
    print(f"Total: ${net_total}")

    #Display the average change
    print(f"Average Change: ${average_change:.2f}")


#Output the greatest increase in profits (date and amount) over the entire period


#Output the greatest decrease in profits (date and amount) over the entire period


#Export a textfile of results to "analysis" folder

print ("Yay! No bugs!")