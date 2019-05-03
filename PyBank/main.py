#Import modules
import os
import csv

#Path to data file
csvpath =os.path.join('PyBank', 'Resources','budget_data.csv')

#Opening  file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    #Setting the variables and a list
    total_months = 0
    total_profit = 0
    diff_of_rows = 0
    previous_pnl = None
    diff_row_list = []
    maxdiff = None
    mindiff = None
    maxmonth = None
    minmonth = None
    avgchange = 0

    #Skipping the header row
    header = next(csvreader)

    #Move through every line of file
    for row in csvreader:
        #Counting for total months
        total_months = total_months + 1
        #Summing PnL
        total_profit = int(row[1]) + total_profit
        #Finding the difference in rows 
        if previous_pnl == None:
            previous_pnl = row[1]
        else:
            diff_of_rows = int(row[1]) - int(previous_pnl)
            diff_row_list.append(diff_of_rows)
            #Set the previous row for the next loop
            previous_pnl = int(row[1])
            #Getting the max and min for differences in rows
            if maxdiff == None or diff_of_rows > maxdiff:
                maxdiff = diff_of_rows
                maxmonth = row[0]
            elif mindiff == None or diff_of_rows < mindiff:
                mindiff = diff_of_rows
                minmonth = row[0]
            else:
                pass
    #Calc average change in differences
    avgchange = round(sum(diff_row_list)/len(diff_row_list), 2)

    #Printing a table of results
    print(f'\nFinancial Analysis: \n\n------------------------\nTotal Months: {total_months}\nTotal Profit/Loss: ${total_profit}\nAverage Change: ${avgchange}\nGreatest Increase in Profits: {maxmonth} (${maxdiff})\nGreatest Decrease in Profits: {minmonth} (${mindiff})\n')

    #Exporting a text file
    #Specifying the file to write to
    output_path = os.path.join('Pybank', 'HWOutput','HWtextFileBank.txt')
    
    #Opening the file and printing to text file
    with open(output_path, 'w') as f:
        print(f'\nFinancial Analysis: \n\n------------------------\nTotal Months: {total_months}\nTotal Profit/Loss: ${total_profit}\nAverage Change: ${avgchange}\nGreatest Increase in Profits: {maxmonth} (${maxdiff})\nGreatest Decrease in Profits: {minmonth} (${mindiff})\n', file=f)