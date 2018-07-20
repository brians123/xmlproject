import sqlite3
import csv


def main():
    conn = sqlite3.connect('/Users/briansui/xml-proj/brian.db')
    c = conn.cursor()
    
    with open("weather.csv") as File:
        reader = csv.reader(File)
        for row in reader:
            city = row[0]
            myDate = row[1]
            maxTemp = row[2]
            minTemp = row[3]
            print(city)
            print(myDate)
            print(maxTemp)
            print(minTemp)
        
            c.execute("INSERT INTO weather (cityName, recordedDate, high, low) VALUES (?, ?, ?, ?)", (city, myDate, maxTemp, minTemp))
            conn.commit()  
        
if __name__ == "__main__":
    main()