#Stephanie McNutt - CWR Data Boot Camp WInter 2021
# Python Homework Week 3 
# PyBank


#import library
import os
import csv

#joining path
budget_data = os.path.join("Resources", "budget_data.csv")

# open and read csv
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    # skip header row
    print(f"Header: {csv_header}")
    
    #make new lists
    profit = []
    months = []
    chg_rev = []

    #read in each row into lists
    for rows in csvreader:
        profit.append(int(rows[1]))
        months.append(rows[0])
        
    #number of months 
    ttl_months =len(months)
    
    
    #calculate net profit/loss
    net_profit = sum(profit)
   
    
    #calculate change in revenue from month to month
    for mth in range(1, len(profit)):
        chg_rev.append((int(profit[mth]) - int(profit[mth-1])))   
  
    #Average revenue change
    avg_rev = sum(chg_rev) / len(chg_rev)
       
    #calculate greatest increase revenue
    max_profit = max(chg_rev)
    
    #calculate greatest Loss revenue
    max_loss = min(chg_rev)
   
    
   
    #**********print report**********#
    print("Financial Analysis")
    print("--------------------------")
    print("Total Months: " + str(ttl_months))
    print("Total Revenue: $" + str(net_profit))
    print("Average Change: $" + str(avg_rev))
    print("Greatest Increase in Profit: " + str(months[chg_rev.index(max(chg_rev)) + 1]) + " ($" + str(max_profit) + ")")
    print("Greatest Decrease in Profit: " + str(months[chg_rev.index(min(chg_rev)) + 1]) + " ($" + str(max_loss) + ")")
    
    #Output to txt file
    
    with open("report.txt", "w") as f:
  
        f.write("Financial Analysis \n")
        f.write("-------------------------- \n")
        f.write("Total Months: " + str(ttl_months) + "\n")
        f.write("Total Revenue: $" + str(net_profit) + "\n")
        f.write("Average Change: $" + str(avg_rev) + "\n")
        f.write("Greatest Increase in Profit: " + str(months[chg_rev.index(max(chg_rev)) + 1]) + " ($" + str(max_profit) + ") \n")
        f.write("Greatest Decrease in Profit: " + str(months[chg_rev.index(min(chg_rev)) + 1]) + " ($" + str(max_loss) + ") \n")
    
    f.close
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    