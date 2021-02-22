#Stephanie McNutt - CWR Data Boot Camp WInter 2021
# Python Homework Week 3 
# PyPoll

#import library
import os
import csv
 
#joining path
election_data = os.path.join("Resources", "election_data.csv")

# open and read csv
with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    # skip header row
    print(f"Header: {csv_header}")
    
    #Create arrays
    voter_id = []
    county = []
    candidate = []
    
    for rows in csvreader:
        voter_id.append(rows[0])
        county.append(rows[1])
        candidate.append(rows[2])
        
    #calculate total votes
    ttl_votes = len(candidate)
    #print(ttl_votes)
    
    #count candidate votes
    
    #create array to count
    l = candidate
    ul = ["Khan", "Correy", "Li", "O'Tooley"]
    result = sorted([(x, l.count(x)) for x in ul], key=lambda y: y[1])
    #print(result)
    
    #apprend results
    cand_ttl = []
    for rows in result:
        cand_ttl.append(rows[1])
    #print(cand_ttl)
    
    #asign values
    khan_votes = cand_ttl[3]
    correy_votes = cand_ttl[2]
    li_votes = cand_ttl[1]
    otooley_votes = cand_ttl[0]
     
    #Calculate percentage
    khan_percent = khan_votes/ttl_votes * 100
    correy_percent = correy_votes/ttl_votes * 100
    li_percent = li_votes/ttl_votes *100
    otooley_percent = otooley_votes/ttl_votes * 100
    
    #find winner
    
    
    w = max(cand_ttl)
    if w == khan_votes:
        winner = "Khan"
    #print(winner[0])
    
    
    #**********print report**********#
    print("Election Results")
    print("---------------------------------")
    print("Total Votes: " + str(ttl_votes))
    print("---------------------------------")
    print(str(f"Khan: {khan_percent:.3f}") + "% " + "(" + str(khan_votes) + ")")
    print(str(f"Correy: {correy_percent:.3f}") + "% " + "(" + str(correy_votes) + ")")
    print(str(f"Li: {li_percent:.3f}") + "% " + "(" + str(li_votes) + ")")
    print(str(f"O'Tooley: {otooley_percent:.3f}") + "% " + "(" + str(otooley_votes) + ")")
    print("---------------------------------")   
    if w == khan_votes:
        print("Khan")
    elif w == correy_votes:
        print("Correy")
    elif w == li_votes:
        print("Li")
    elif w == otooley_votes:
        print("O'Tooley")
    print("---------------------------------") 
    #*********************************#
    
    
    
    #**********output to file**********#
    with open("report.txt", "w") as f:
        f.write("Election Results \n")
        f.write("--------------------------------- \n")
        f.write("Total Votes: " + str(ttl_votes) + "\n")
        f.write("--------------------------------- \n")
        f.write(str(f"Khan: {khan_percent:.3f}") + "% " + "(" + str(khan_votes) + ") \n")
        f.write(str(f"Correy: {correy_percent:.3f}") + "% " + "(" + str(correy_votes) + ") \n")
        f.write(str(f"Li: {li_percent:.3f}") + "% " + "(" + str(li_votes) + ") \n")
        f.write(str(f"O'Tooley: {otooley_percent:.3f}") + "% " + "(" + str(otooley_votes) + ") \n")
        f.write("--------------------------------- \n")   
        f.write("Winner: " + str(winner) + "\n")
        f.write("--------------------------------- \n") 
    #*********************************#
    
    
       