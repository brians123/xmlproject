class Patient:
    def __init__(self, name, startwaittime1, waittime, visittime, doctorname):
        self.name = name
        self.startwaittime1 = startwaittime1
        self.waittime = waittime
        self.visittime = visittime
        self.startvisittime1 = ""
        self.doctorname = doctorname
     
    
    def printpatient(self):
        print self.name
        print self.startwaittime1
        print self.waittime
        print self.visittime
        print self.doctorname
        print self.startvisittime1
    
    def setinitialvisittime(self, startvisittime1):
        self.startvisittime1 = startvisittime1
        
        
        