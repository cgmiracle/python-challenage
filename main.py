# Code resources:
# https://www.youtube.com/watch?v=0Juk_Ufyea4
# https://stackoverflow.com/questions/36247277/using-python-to-find-the-most-common-values-in-the-column-of-csv-file

# Import Modules
import csv
import pandas
import os
from pathlib import Path

# Import data
poll_data = pandas.read_csv('02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv', delimiter = ',')
csvpath = os.path.join('02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Opening Statements 
    print("Election Results : ")
    print("--------------------")
    print("")
    
    # Pandas for poll data
    poll_data = pandas.read_csv('02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv', delimiter = ',')
    
    # Count of total votes
    vote_count = sum(1 for row in csvfile)
    print("----------------")
    print("Total Votes : " + str(vote_count - 1))
    print("----------------")
    print("")
    
    # Counts amount of votes for each candidate
    can_count = poll_data.groupby('Candidate')['Candidate'].count()
    print("The total votes for each canidate are: ")
    #print(can_count)
    
    
    #counts percentage of votes
    per_votes = (can_count / vote_count * 100)
    
    
    #Print totals
    vote_total = [[can_count, per_votes]]
    print(vote_total)
 

    # Print Winner
from collections import Counter
filename='02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv'
with open(filename, 'r') as f:
    column = (row[2] for row in csv.reader(f))
    
    # Winner Statement
    print("------------------")
    print("The Winner Is :")
    print("{0}".format(Counter(column).most_common()[0][0]))
    print("------------------")

    output_file = Path("poll.txt")

    with open(output_file,"w") as file:
        file.write(f"Election Results : ")
        file.write("\n")
        file.write(f"--------------------")
        file.write("\n")
        file.write(f"")
        file.write("\n")
        file.write(f"----------------")
        file.write("\n")
        file.write(f"Total Votes : " + str(vote_count - 1))
        file.write("\n")
        file.write(f"----------------")
        file.write("\n")
        file.write(f"")
        file.write("\n")
        file.write(f"The total votes for each canidate are: ")
        file.write("\n")
        file.write(str(vote_total))
        file.write("\n")
        file.write(f"------------------")
        file.write("\n")
        file.write(f"The Winner Is :")
        file.write(str(winner))
        file.write("------------------")
