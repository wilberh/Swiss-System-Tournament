# Swiss-System-Tournament
- Python &amp; Postgre SQL: Audacity Project 2 - Swiss System Tournament


This is an implementation of (the first round of) a Swiss-system tournament.

This project will be using a Python module (tournament.py) that uses a PostgreSQL database (created using the tournament.sql file) to keep track of players and matches in a Swiss-system game tournament.

This project consists of 2 Python version 2.7.9 files, and one sql file,
1.The tournament.py Python file stores the functions to be called.  
2.The tournament_test.py Python file store the tests for the functions stored in the tournament.py Python file.
3.The tournament.sql file can be viewed in a text editor and stores the Postgre sql version 9.3.6 instructions for:
- creating the database (tournament),
- connecting to the tournament database,
- creating 2 tables (players and matches) for this database  

The tournament_test.py Python file will have to be run to test the tournament.py Python file using the tournament.sql file to create the database and corresponding table.  The tournament_test.py file will print out the results of the test if successful or not on the command line or computer screen.


## WHAT'S INCLUDED
within the download you'll find the following files:
- tournament.py
- tournament.sql
- tournament_test.py
- README.txt


## BUGS AND FEATURE REQUESTS
Have a bug or a feature request? Please open an [issue](https://github.com/wilberh/Swiss-System-Tournament/issues/new).

## DOCUMENTATION
This Swiss-System-Tournament documentation included in this repo in the root directory is built with Python version 2.7.9, and PostgreSQL version 9.3.6.  The docs may also be run locally in your Linux database server, or Linux virtual databaser server.


## RUNNING DOCUMENTATION LOCALLY
- 1. If necessary, install Python version 2.7.9 and Postgre sql version 9.3.6 in a Linux database server or Linux virtual database server
- 2. From the root /Swiss-System-Tournament directory, run tournament_test.py in the command line by typing, "python tournament_test.py" 
- 3. The program will list or print out the results of the tests of the functions in the tournament.py Python file 


## CREATOR
**Wilber Hernandez**
- github.com/wilberh
- twitter.com/wilberh

