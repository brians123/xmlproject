import csv
import sys
from weather import weather

def main():
    
    #fileName = raw_input("Which file would you like to print?")
    #print("The file you have selected is: " + fileName)
    dict = {}
    
    if len(sys.argv) < 2:
        #print("Which file would you like to open?: ")
        #exit()
        
        openedFile = sys.argv[1]
    
    
    with open(openedFile) as File:
        reader = csv.reader(File)
        for row in reader:
            #print (row)
            cityName = row[0]
            myDate = row[1]
            maxTemp = row[2]
            minTemp = row[3]
            #print(cityName)
            #print(maxTemp)
            #dict[cityName] = maxTemp
            
            myWeather=weather(cityName, myDate, maxTemp, minTemp)
        
            if cityName in dict:
                oldWeather = dict[cityName]
                if int(oldWeather.high) < int(myWeather.high):
                    oldWeather.high=myWeather.high
                    #print(oldWeather.high)
                    #print("inasdfjkasdf: " + str(dict[cityName]))
                    #print("max: " + str(maxTemp))
                if int(oldWeather.low) > int(myWeather.low):
                    oldWeather.low=myWeather.low
                    
                    
            else:
                dict[cityName] = myWeather
                #print myWeather.printWeather()
                
                
    for key in dict:
        #print key 
        dict[key].printWeather()
            
if __name__ == "__main__":
    main()