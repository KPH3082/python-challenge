#Import modules
import os
import csv

#Setting a path to the data file
csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')

#Opening the file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    #Setting the variables
    num_of_votes = 0
    percentKhan = 0
    percentCorrey = 0
    percentLi = 0
    percentOTooley = 0
    totKhan = 0
    totCorrey = 0
    totLi = 0
    totOTooley = 0
    winner = ""

    #Skipping the header row
    header = next(csvreader)

    #Looping through each row
    for row in csvreader:
        #Calculating total votes cast
        num_of_votes = num_of_votes + 1
        #Adding up votes for each canidate
        if row[2] == "Khan":
            totKhan +=1
        elif row[2] == "Correy":
            totCorrey += 1
        elif row[2] == "Li":
            totLi += 1
        else:
            totOTooley += 1
    #Calc percentages for each canidate
    percentKhan = totKhan / num_of_votes
    percentCorrey = totCorrey / num_of_votes
    percentLi = totLi / num_of_votes
    percentOTooley = totOTooley / num_of_votes


    #Building a dictionary for results and populating 'winner'
    candidates = {'Khan': totKhan, 'Correy': totCorrey, 'Li': totLi, 'O\'Tooley': totOTooley}
    winner = max(candidates, key = candidates.get)

    #Print out table
    print(f'\nElection Results\n-------------------\nTotal Votes: {num_of_votes}\n-------------------\nKhan: {"{:.3%}".format(percentKhan)} ({totKhan})\nCorrey: {"{:.3%}".format(percentCorrey)} ({totCorrey})\nLi: {"{:.3%}".format(percentLi)} ({totLi})\nO\'Tooley: {"{:.3%}".format(percentOTooley)}% ({totOTooley})\n-------------------\nWinner: {winner}\n-------------------\n\n')

    #Exporting a text file
    #Specifying the file to write to
    output_path = os.path.join('PyPoll', 'HWOutput','HWtextFilePoll.txt')
    
    #Opening the file and printing to text file
    with open(output_path, 'w') as f:
        print(f'\nElection Results\n-------------------\nTotal Votes: {num_of_votes}\n-------------------\nKhan: {"{:.3%}".format(percentKhan)} ({totKhan})\nCorrey: {"{:.3%}".format(percentCorrey)} ({totCorrey})\nLi: {"{:.3%}".format(percentLi)} ({totLi})\nO\'Tooley: {"{:.3%}".format(percentOTooley)}% ({totOTooley})\n-------------------\nWinner: {winner}\n-------------------\n\n', file=f)