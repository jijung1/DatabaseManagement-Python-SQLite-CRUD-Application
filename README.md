**DatabaseManagement Python SQLite CRUD Console Application** <br/>
*Jin Jung* <br/>
*SID 2329401* <br/>
*CPSC 408-01* <br/>
*Assignment 2* <br/>

**Program Description | Remarks:** <br/>
  
A Python console application that connects to a SQLite database and performs common database operations. 
The application should connect to an existing StudentDB.db database in the current directory or create one if it doesn't exist yet. It should Create a new Student relation with the schema detailed below if it doesn't already exist. Extensive testing has not been performed on input validation, but seems to be performing as normally for most normal cases.

**Database Schema:** <br/>
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

**References:** <br/>
  *https://pandas.pydata.org/docs/reference/frame.html* <br/>
  *https://docs.python.org/2/library/sqlite3.html* <br/>
