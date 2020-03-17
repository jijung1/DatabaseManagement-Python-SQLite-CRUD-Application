class Student:

    #constructor
    def __init__(self, studentID, firstName, lastName, gpa, major, facAdvisor, isDeleted):
        self.studentID = studentID
        self.firstName = firstName
        self.lastName = lastName
        self.gpa = gpa
        self.major = major
        self.facAdvisor = facAdvisor
        self.isDeleted = isDeleted

    def getStudentID(self):
        return self.studentID

    def setStudentID(self, studentID):
        self.studentID = studentID

    def getFirstName(self):
        return self.firstName
    def setFirstName(self, firstName):
        self.firstName = firstName

    def getLastName(self):
        return self.lastName

    def setLastName(self,lastName):
        self.lastName = lastName

    def getGPA(self):
        return self.gpa

    def setGPA(self, gpa):
        self.gpa = gpa

    def getMajor(self):
        return self.major

    def setMajor(self, major):
        self.major = major

    def getFacAdvisor(self):
        return self.facAdvisor

    def setFacAdvisor(self, facAdvisor):
        self.facAdvisor = facAdvisor

    def getIsDeleted(self):
        return self.isDeleted

    def setIsDeleted(self, isDeleted):
        self.isDeleted = isDeleted

    def getStudent(self):
        return (self.studentID, self.getFirstName(), self.getLastName(), self.gpa, self.getMajor(), self.facAdvisor, self.isDeleted)
