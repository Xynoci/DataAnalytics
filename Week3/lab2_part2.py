################################
### Connects to Database
### Gets Data from Database
################################

import sqlite3 as lite
import sys
import os 

con = None

## Creates a folder for the database
## Set directory to YOUR computer and folder
directoryForDB = "C:/Users/Pudders/Desktop/DBClass/" + "pittsburghData.db"

con = lite.connect(directoryForDB)
##########################################
#### Output: Neighborhood, (pop2010 - pop1940) as difference: ORDER by difference DESC
##########################################
with con:
	cur = con.cursor()    
	cur.execute('ADD HERE')
	rows = cur.fetchall()
	for row in rows:
		print row[0],row[1]

##########################################
#### Output: Neighborhood, pop2010, Information
##########################################
with con:
	cur = con.cursor()    
	cur.execute('ADD HERE')
	rows = cur.fetchall()
	for row in rows:
		print row[0],row[1], row[2]	
		
##########################################
#### Output: Neighborhood, MAX(pop2010)
##########################################
with con:
	cur = con.cursor()    
	cur.execute('ADD HERE')
	rows = cur.fetchall()
	for row in rows:
		print row[0],row[1]
		
		
##########################################
#### Output: Neighborhood, MAX(pop2010), Scientific
##########################################
with con:
	cur = con.cursor()    
	cur.execute('ADD HERE')
	rows = cur.fetchall()
	for row in rows:
		print row[0],row[1],row[2] 
