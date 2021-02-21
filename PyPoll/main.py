#Stephanie McNutt - CWR Data Boot Camp WInter 2021
# Python Homework Week 3 
# PyPoll

#import library
import os
import csv
#import numpy
#import pandas as pd
    

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
    print(ttl_votes)
    
    #count candidate votes
    l = candidate
    ul = ["Khan", "Correy", "Li", "O'Tooley"]
    result = sorted([(x, l.count(x)) for x in ul], key=lambda y: y[1])
    #print(result)
    cand_ttl = []
    for rows in result:
        cand_ttl.append(rows[1])
    print(cand_ttl)
   
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   