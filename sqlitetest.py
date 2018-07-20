import sqlite3

def main(lastname):
    conn = sqlite3.connect('/Users/briansui/xml-proj/brian.db')
    c = conn.cursor()   
    
    
    #c.execute("INSERT INTO student (FirstName, LastName) VALUES ('Mary', 'Sui')")
    #conn.commit()
    
    
    #c.execute("SELECT * FROM student WHERE LastName = '%s'" % lastname)
    c.execute("SELECT * FROM classTaken, student, class WHERE student.ID=classTaken.studentID and class.ClassName='Physics 1'")
    list = c.fetchall()
    
    for i in list:
        print i
    
    
if __name__=="__main__":
    main("Sui")