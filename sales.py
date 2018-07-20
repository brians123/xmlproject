import csv
salesDict = {}

#a commment
# add another comment

def main():
    salesReader()
    #printSummaryReport()
    
def salesReader():
    with open("sales.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            cityName = row[0]
            subdivision = row[1]
            cost = row[2]
            sales = row[3]
            profit = int(sales) - int(cost)
            #print cityName
            #print subdivision
            #print cost
            #print sales
            
            if cityName not in salesDict:
                salesDict[cityName] = int(profit)
            else:
                currentProfit = int(sales) - int(cost)
                salesDict[cityName] = currentProfit + salesDict[cityName]
        reader.close()
                
    for key in salesDict:
        print "%s's profits are: " % key, salesDict[key]
        
#def printSummaryReport():
    
                
            
if __name__ == "__main__":
    main()