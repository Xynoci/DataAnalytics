################################
### Creates Database
### Updates Database with Data
################################

import sqlite3 as lite
import sys
import os 


con = None

## Creates a folder for the database
## Set directory to YOUR computer and folder
directoryForDB = "C:/Users/Pudders/Desktop/DBClass/"
if not os.path.exists(directoryForDB):
	os.makedirs(directoryForDB)

directoryForDB = directoryForDB + "carsDatabase.db"
## If database does not exist, creates items
## If database does exist, opens it
con = lite.connect(directoryForDB)
with con:

	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS Cars") 
	cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
	cur.execute("INSERT INTO Cars VALUES(1,'Audi',12345)")
	cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")
	cur.execute("INSERT INTO Cars VALUES(3,'Skoda',9000)")
	cur.execute("INSERT INTO Cars VALUES(4,'Volvo',29000)")
	cur.execute("INSERT INTO Cars VALUES(5,'Bentley',350000)")
	cur.execute("INSERT INTO Cars VALUES(6,'Citroen',21000)")
	cur.execute("INSERT INTO Cars VALUES(7,'Hummer',41400)")
	cur.execute("INSERT INTO Cars VALUES(8,'Volkswagen',29000)")
	## NEEDED, if not, database does not update
	con.commit()
	



