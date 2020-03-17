import sqlite3
from pandas import DataFrame

from Student import Student


#studentID, firstName, lastName, gpa, major, facAdvisor, isDeleted

conn = sqlite3.connect('StudentDB.db')
c = conn.cursor() #allows to python code to execute SQL statements

c.executescript("""
    CREATE TABLE IF NOT EXISTS Student ( StudentId INT PRIMARY KEY, FirstName VARCHAR(32), LastName VARCHAR(32), GPA FLOAT, Major VARCHAR(16), FacultyAdvisor VARCHAR(32), IsDeleted BOOLEAN );
    """)

c.execute ("CREATE TABLE IF NOT EXISTS Student ( StudentId INT PRIMARY KEY, FirstName VARCHAR(32), LastName VARCHAR(32), "
 "GPA FLOAT, Major VARCHAR(16), FacultyAdvisor VARCHAR(32), IsDeleted BOOLEAN );")

print('please select from the following choices:\n1. Display All Student Info\n2. Add New Student\n3. Update Advisor/Major\n4. Delete by Student ID\n5. Query by Major/GPA/Advisor\n6. exit')
choice = int(input())

while choice != 6:

    #Display all student info
    if choice == 1:
        c.execute('SELECT "StudentId", "FirstName", "LastName", "GPA", "Major", "FacultyAdvisor" FROM Student')
        all_rows = c.fetchall()
        df = DataFrame(all_rows, columns=["StudentId", "FirstName", "LastName", "GPA", "Major", "FacultyAdvisor"])
        if df.empty:
            print('Table is empty.')
        else:
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
            if type(firstname) == str:
                break
            print('You have entered an invalid First Name.')
        while True:
            print('Please enter Last Name: ')
            lastname = input()
            if type(lastname) == str:
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
            if type(major) == str:     #maybe add checks from a list of valid majors
                break
            print('You have entered an invalid Major')
        while True:
            print('Please enter Student\'s Faculty Advisor:')
            facadvisor = input()
            if type(facadvisor) == str:
                break
            print('You have entered an invalid Faculty Advisor.')
        stu = Student(studentid, firstname, lastname, gpa, major, facadvisor, False)
        c.execute ('INSERT INTO Student("StudentId", "FirstName","LastName", "GPA", "Major", "FacultyAdvisor", IsDeleted) VALUES (?,?,?,?,?,?,?)', stu.getStudent())
        rowID = c.lastrowid
        print("record created", rowID)

    elif choice == 3:
        count = 0 #counter to time out if student id not found too many times
        while True:

            print('Please enter the Student ID of student to change Major/Advisor: ')
            try:
                student_id = int(input())
                stmt = "SELECT StudentId FROM Student WHERE StudentId = " + str(student_id)
                print("stmt: " + stmt)
                c.execute(stmt)
                r = c.fetchone()
                if type(r) == tuple:
                    break
                else:
                    count += 1
                    print('Student ID not in Database.')
                    if count == 3:
                        break
            except:
                print('You have entered an invalid Student ID.')
        if count == 3:
            break;
        print ('Please enter Student\'s new major: ')
        major = input()







       # c.execute("UPDATE Student SET Major = ? WHERE StudentId = ?", ('CS', 11,))
    elif choice == 4:
        # c.execute("DELETE FROM Student WHERE (FirstName = 'Covid')")

        print('hello')

    elif choice == 5:
        print('hello')

    elif choice == 6:
        print('hello')

    else:
        print("invalid input!")
    print('please select from the following choices:\n1. Display All Student Info\n2. Add New Student\n3. Update Advisor/Major\n4. Delete by Student ID\n5. Query by Major/GPA/Advisor\n6. exit')
    choice = int(input())



#update example
"""
c.execute("UPDATE Student SET Major = ? WHERE StudentId = ?", ('CS', 11,))
"""
"""
#select
input_param = ('Rene', 'CS',)
c.execute('SELECT FirstName, LastName, Major FROM Student WHERE FirstName = ? AND Major = ?', input_param)
all_rows = c.fetchall()



studentId = c.lastrowid
print("record created", studentId)

"""
#save (commit) the changes
conn.commit()