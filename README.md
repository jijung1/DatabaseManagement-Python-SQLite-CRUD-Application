**DatabaseManagement Python SQLite CRUD Console Application**
*Jin Jung* 
*SID 2329401*
*CPSC 408-01*
*Assignment 2*

**Program Description | Remarks: **
  
A Python console application that connects to a SQLite database and performs common database operations. 
The application should connect to an existing StudentDB.db database in the current directory or create one if it doesn't exist yet. It should Create a new Student relation with the schema detailed below if it doesn't already exist. Extensive testing has not been performed on input validation, but seems to be performing as normally for most normal cases.

**Database Schema: **
```
Student (
StudentId PK INT,
FirstName varchar(32),
LastName varchar(32),
GPA Numeric,
Major varchar(16),
FacultyAdvisor varchar(32),
isDeleted bit or boolean
)
```

**References: **
  *https://pandas.pydata.org/docs/reference/frame.html*
  *https://docs.python.org/2/library/sqlite3.html*
