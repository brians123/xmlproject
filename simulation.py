import csv
from patient import Patient
from findertools import sleep
import patient
waitlist=[]
import datetime
import time
import sqlite3
conn = sqlite3.connect('/Users/briansui/xml-proj/brian.db')
c = conn.cursor()
doctordict = {}
doctordict2 = {}
# DOCTOR LISTS FOR THE THREE DOCTORS: THAI, PHILIP, ADRIAN
doclist1 = []
doclist2 = []
doclist3 = []
doctordict["Dr Thai"]=doclist1
doctordict["Dr Philip"]=doclist2
doctordict["Dr Adrian"]=doclist3

def main():
    cleanuplog()
    patientSetUp()
    waitTimeMonitor()
    printdoctorlist2()
    visitTimeMonitor()
    
def patientSetUp():
    with open("patientlist.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader: 
            patientName = row[0]
            waitTime = row[1] 
            visitTime = row[2]
            doctorName = row[3]
            startwaittime1=datetime.datetime.now()
            
            myPatient= Patient(patientName, startwaittime1, waitTime, visitTime, doctorName)
            waitlist.append(myPatient)
            #INSERTING PATIENT LOG INTO DATABASE
            insertlog(patientName, "checking in")
        for patient in waitlist:
            patient.printpatient()
        
def waitTimeMonitor():
    while True:
        for patient in waitlist:
            startWaitTime2= datetime.datetime.now()
            delta = startWaitTime2 - patient.startwaittime1
            delta_in_ms = int(delta.total_seconds()*1000)
            print "delta_in_ms: " + str(delta_in_ms)
            print "patient wait time: " + str(patient.waittime)
            if int(delta_in_ms) >= int(patient.waittime):
                print "conditions met"
                waitlist.remove(patient)
                #INSERTING PATIENT DATA INTO LOG TO INDICATE PATIENT IS LEAVING WAITING ROOM
                insertlog(patient.name, "leaving waiting room")
                addtodoctorlist2(patient)
                break
        time.sleep(1)
        print"length of list: " + str(len(waitlist))
        if len(waitlist)==0:
            print "No more in the list"
            break         
        
def cleanuplog():
    c.execute("DELETE FROM patientlog")
    conn.commit()

def insertlog(patientName, act):
    timestamp= datetime.datetime.now()
    c.execute("INSERT into patientlog (name, date, act) VALUES (?,?,?)", (patientName, timestamp, act))
    print "i executed"
    conn.commit()
    
def addtodoctorlist(patient):
    doctordict[patient.doctorname].append(patient)
    
def printdoctorlist():
    for key in doctordict:
        print "doctor: " + key
        for patient in doctordict[key]:
            patient.printpatient()
            print "\n\n"
            
def addtodoctorlist2(patient):
    patientDoctorName = patient.doctorname
    patientVisitTime1 = datetime.datetime.now()
    patient.setinitialvisittime(patientVisitTime1)
    insertlog(patient.name, "visiting doctor")
    if patientDoctorName not in doctordict2:
        doctordict2[patientDoctorName] = []
        doctordict2[patientDoctorName].append(patient)
    else:
        doctordict2[patientDoctorName].append(patient)
    
def printdoctorlist2():
    for key in doctordict2:
        print "doctor: " + key
        for patient in doctordict2[key]:
            patient.printpatient()
            print "\n\n"
            
def visitTimeMonitor():
    while True:
        for key in doctordict2.copy():
            list = doctordict2[key]
            if len(list)==0:
                del doctordict2[key]
            else:    
                for patient in list:
                    patientVisitTime2 = datetime.datetime.now()
                    delta = patientVisitTime2 - patient.startvisittime1
                    delta_in_ms = int(delta.total_seconds()*1000)
                    print "delta_in_ms: " + str(delta_in_ms)
                    print "patient visit time: " + str(patient.visittime)
                    if int(delta_in_ms) >= int(patient.visittime):
                        print "conditions met"
                        list.remove(patient)
                        insertlog(patient.name, "leaving %s doctor's office" % (patient.doctorname))
                        break
        if len(doctordict2)==0:
            print "dictionary has no keys"
            break
        
if __name__ == "__main__":
    main()