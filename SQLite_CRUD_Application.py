import sqlite3
from pandas import DataFrame

from Student import Student


#studentID, firstName, lastName, gpa, major, facAdvisor, isDeleted

conn = sqlite3.connect('C:\\Users\\jinju\\Documents\\CPSC_COURSES2\\CPSC_COURSES\\StudentDB')
c = conn.cursor() #allows to python code to execute SQL statements
#c.execute("DELETE FROM Student WHERE (FirstName = 'Covid')")
#stu = Student(2329400, 'Jin', 'Jung', 3.96, 'CS', 'Rene German', False)

print('please select from the following choices:\n1. Display All Student Info\n2. Add New Student\n3. Update Advisor/Major\n4. Delete by Student ID\n5. Query by Major/GPA/Advisor\n6. exit')
choice = int(input())

while choice != 6:

    #Display all student info
    if choice == 1:
        c.execute('SELECT * FROM Student')
        all_rows = c.fetchall()
        df = DataFrame(all_rows, columns=["StudentId", "FirstName","LastName", "GPA", "Major", "FacultyAdvisor","IsDeleted"])
        print(df)
    #Add new student with input validation (basic type check and add better during test phase)
    elif choice == 2:
        print('All information MUST be entered for record to be saved.')
        while True:
            print('Please enter the Student ID: ')
            try:
                studentid = int(input())
                break
            except:
                print('You have entered an invalid ID')
        while True:
            print('Please enter First Name: ')
            firstname = input()
            if firstname.isalpha():
                break
            print('You have entered an invalid First Name.')
        while True:
            print('Please enter Last Name: ')
            lastname = input()
            if lastname.isalpha():
                break
            print('You have entered an invalid Last Name.')
        while True:
            print('Please enter GPA: ')
            try:
                gpa = float(input())
                break;
            except:
                print('You have entered an invalid GPA.')
        while True:
            print('Please enter Major:')
            major = input()
            if major.isalpha():     #maybe add checks from a list of valid majors
                break
            print('You have entered an invalid Major')
        while True:
            print('Please enter Student\'s Faculty Advisor:')
            facadvisor = input()
            if facadvisor.isalpha():
                break
            print('You have entered an invalid Faculty Advisor.')
        stu = Student(studentid, firstname, lastname, gpa, major, facadvisor, False)
        c.execute ('INSERT INTO Student("StudentId", "FirstName","LastName", "GPA", "Major", "FacultyAdvisor", IsDeleted) VALUES (?,?,?,?,?,?,?)', stu.getStudent())

        #print(type(studentid))
        #print(studentid)

    elif choice == 3:
        print('hello')
    elif choice == 4:
        print('hello')

    elif choice == 5:
        print('hello')

    elif choice == 6:
        print('hello')

    else:
        print("invalid input!")
    print('please select from the following choices:\n1. Display All Student Info\n2. Add New Student\n3. Update Advisor/Major\n4. Delete by Student ID\n5. Query by Major/GPA/Advisor\n6. exit')
    choice = int(input())
"""
prompt user with switch options
do either add record, (prompt Firstname, LastName, Major)
 delete records, (delete based on Firstname, Lastname) 
  delete all records, (delete from table)
   update attributes, ( query records by: first name, major, last name match

"""

#c.execute ('INSERT INTO Student("StudentId", "FirstName","LastName", "GPA", "Major", "FacultyAdvisor", IsDeleted) VALUES (?,?,?,?,?,?,?)', stu.getStudent())
#c.execute("INSERT INTO Student('FirstName', 'LastName')" "VALUES ('Covid', 'German')")


#update example
"""
c.execute("UPDATE Student SET Major = ? WHERE StudentId = ?"
          , ('CS', 11,)
          )
"""
"""
#select
input_param = ('Rene', 'CS',)
c.execute('SELECT FirstName, LastName, Major FROM Student WHERE FirstName = ? AND Major = ?', input_param)
all_rows = c.fetchall()
df = DataFrame(all_rows, columns=['StudentId', 'LastName', 'LastName', 'Major'])
print(df)


studentId = c.lastrowid
print("record created", studentId)

"""
#save (commit) the changes
conn.commit()