import sqlite3
import csv
conn = sqlite3.connect('/Users/briansui/xml-proj/brian.db', timeout=1)
c = conn.cursor() 

def main():
    while True:
        choice = raw_input("MAIN MENU\n Press any key to continue OR press 'q' to quit")
        if choice == "q":
            break
        else:
            subMenu()
    conn.close()

def subMenu():
    print(" 1. List\n 2. Delete\n 3. Update\n 4. Insert\n 5. Import\n")
    response = raw_input("Enter number: ")
    if response == "1":
        listTable()
    elif response == "2":
        deleteStudent()
    elif response == "4":
        insertStudent()
    elif response == "3":
        updateStudent()
    elif response == "5":
        importStudent()
        

def listTable():
    c.execute("SELECT * FROM student")
    databaseList = c.fetchall()
    for i in databaseList:
        print i
    #c.close() 
    
def deleteStudent():
    askID = raw_input("What is the student's ID that you want to delete? ")
    c.execute("DELETE FROM student WHERE ID=?", (askID))
    conn.commit()
    c.close()
    
def updateStudent():
    askID = raw_input("Enter student ID: ")
    firstName = raw_input("Enter student's first name: ")
    lastName = raw_input("Enter student's last name: ")
    counter = c.execute("UPDATE student SET FirstName=?, LastName=? WHERE ID=?", (firstName, lastName, askID))
    print(counter)
    conn.commit()
    c.close()

def insertStudent():
    firstName = raw_input("Enter student's first name: ")
    lastName = raw_input("Enter student's last name: ")
    c.execute("INSERT INTO student (FirstName, LastName) VALUES (?, ?)", (firstName, lastName))
    conn.commit()
    c.close()

def importStudent():
    fileOfChoice = raw_input("Enter name of file: ")
    with open(fileOfChoice, 'rb') as File:
        reader=csv.reader(File)
        for i in reader:
            firstName=i[0]
            lastName=i[1]
            c.execute("INSERT INTO student (FirstName, LastName) VALUES (?, ?)", (firstName, lastName))
            conn.commit()
    c.close()
    File.close()
        
        
    
        
if __name__ == "__main__":
    main()