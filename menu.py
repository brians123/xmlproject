import csv
import sys
from weather import weather
from datetime import date

file = open("test.csv", "w")

def main():
    
    while True:
        choice = raw_input("MAIN MENU\nEnter weather data? ")
        
        if choice == "Y":
            getWeather()
        else:
            break
    file.close()
        
def getWeather():
    myCity = raw_input("Enter city name: ")
    myDate = raw_input("Enter date: ")
    while True:
        myMax = raw_input("Enter max: ")
        if myMax.isdigit():
            break
    while True:
        myMin = raw_input("Enter min: ")
        if myMin.isdigit():
            break
    print(myCity)
    print(myDate)
    print(myMax)
    print(myMin)
    file.write("%s, %s, %s, %s\n" % (myCity, myDate, myMax, myMin))
    

if __name__ == "__main__":
    main()