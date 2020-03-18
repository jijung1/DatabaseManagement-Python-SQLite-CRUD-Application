import sqlite3
from pandas import DataFrame

from Student import Student


conn = sqlite3.connect('StudentDB.db')
c = conn.cursor() #allows to python code to execute SQL statements

c.executescript("""
    CREATE TABLE IF NOT EXISTS Student ( StudentId INT PRIMARY KEY, FirstName VARCHAR(32), LastName VARCHAR(32), GPA FLOAT, Major VARCHAR(16), FacultyAdvisor VARCHAR(32), IsDeleted BOOLEAN );
    """)

c.execute ("CREATE TABLE IF NOT EXISTS Student ( StudentId INT PRIMARY KEY, FirstName VARCHAR(32), LastName VARCHAR(32), "
 "GPA FLOAT, Major VARCHAR(16), FacultyAdvisor VARCHAR(32), IsDeleted BOOLEAN );")

print('please select from the following choices:\n1. Display All Student Info\n2. Add New Student\n3. Update Advisor/Major\n'
      '4. Soft Delete by Student ID\n5. Query by Major/GPA/Advisor\n7. Permanently Delete Student by Student ID (NOT RECOMMENDED)\n6. exit'
      )
choice = int(input())

while choice != 7:

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
            print('Please enter the Student ID: ')  #Check if Student ID already exists, if so disallow and prompt deletion first
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
                break
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
            break
        print('Please enter Student\'s new major: ')
        major = input()
        print ('Please enter the student\'s new Faculty Advisor: ')
        facadvisor = input()

        c.execute("UPDATE Student SET Major = ? WHERE StudentId = ?", (major, student_id,))
        c.execute("UPDATE Student SET FacultyAdvisor = ? WHERE StudentId = ?", (facadvisor, student_id,))

    elif choice == 4:
        count = 0 #counter to time out if student id not found too many times
        while True:
            print('***Please enter the Student ID of student to soft delete: ***')
            try:
                student_id = int(input())
               # stmt = "SELECT StudentId FROM Student WHERE StudentId = " + str(student_id)
                c.execute("SELECT StudentId FROM Student WHERE StudentId = " + str(student_id))
                r = c.fetchone()
                if type(r) == tuple:
                    break
                else:
                    count += 1
                    print('***Student ID not in Database.***')
                    if count == 3:
                        break
            except:
                print('***You have entered an invalid Student ID.***')
        if count == 3:
            break
        c.execute("UPDATE Student SET IsDeleted = ? WHERE StudentId = ?", (True, student_id,))
        print('\n***Student has been flagged for deletion from database***\n')

    elif choice == 5:
        print('\n***Please type "major" to query by major, "gpa" to query by GPA, or "advisor" to query by Faculty Advisor: ***\n')
        qchoice = input()
        if qchoice.lower() == 'major':
            print('Please enter the major to query by: ')
            major = input()
            c.execute('SELECT "StudentId", "FirstName", "LastName", "GPA", "Major", "FacultyAdvisor" FROM Student WHERE Major = ?', (major,))
            all_rows = c.fetchall()
            if all_rows.__sizeof__() == 40: #40 is the size of no result query
                print('***\nNo records found for that major. ***\n')
            else:
                df = DataFrame(all_rows, columns=["StudentId", "FirstName", "LastName", "GPA", "Major", "FacultyAdvisor"])
                print(df)

        elif qchoice.lower() == 'gpa':
            print('please enter the gpa range to query by:\nlow: ')
            try:
                low = float(input())    #try catch block here
                print('high: ')
                high = (input())
                c.execute('SELECT "StudentId", "FirstName", "LastName", "GPA", "Major", "FacultyAdvisor" FROM Student WHERE GPA BETWEEN ? AND ?', (low, high,))
                all_rows = c.fetchall()
                if all_rows.__sizeof__() == 40:  # 40 is the size of no result query
                    print('***\nNo records found in specified range. ***\n')
                else:
                    df = DataFrame(all_rows,
                                   columns=["StudentId", "FirstName", "LastName", "GPA", "Major", "FacultyAdvisor"])
                    print(df)
            except:
                print("\n*** Invalid Specified Range. ***\n")


        elif qchoice.lower() == 'advisor':
            print('Please enter the Faculty Advisor name: ')
            advisor = input()
            c.execute('SELECT "StudentId", "FirstName", "LastName", "GPA", "Major", "FacultyAdvisor" FROM Student WHERE FacultyAdvisor = ?', (advisor,))
            all_rows = c.fetchall()
            if all_rows.__sizeof__() == 40:  # 40 is the size of no result query
                print('***\nNo records found with specified advisor. ***\n')
            else:
                df = DataFrame(all_rows,
                               columns=["StudentId", "FirstName", "LastName", "GPA", "Major", "FacultyAdvisor"])
                print(df)

        else:
            print("\n***Invalid input received.***\n")

    elif choice == 6:
        count = 0  # counter to time out if student id not found too many times
        while True:
            print('***Please enter the Student ID of student to Permanently delete: ***')
            try:
                student_id = int(input())
                stmt = "SELECT StudentId FROM Student WHERE StudentId = " + str(student_id)
                c.execute(stmt)
                r = c.fetchone()
                if type(r) == tuple:
                    break
                else:
                    count += 1
                    print('\n***Student ID not in Database.***\n')
                    if count == 3:
                        break
            except:
                print('***You have entered an invalid Student ID.***')
        if count == 3:
            break
        c.execute("DELETE FROM Student WHERE StudentId = ?", (student_id,))
        print('***Student has been permanently deleted from database***')
    elif choice == 7:
        print('\n***Exiting Program. Good bye. ***\n')
        break
    else:
        print("invalid input!")
    print(
        'please select from the following choices:\n1. Display All Student Info\n2. Add New Student\n3. Update Advisor/Major\n'
        '4. Soft Delete by Student ID\n5. Query by Major/GPA/Advisor\n6. Permanently Delete Student by Student ID (NOT RECOMMENDED)\n7. exit'
        )
    choice = int(input())

#save (commit) the changes
conn.commit()

