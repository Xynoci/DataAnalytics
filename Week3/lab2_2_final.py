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
	cur.execute('SELECT neighborhood, pop2010-pop1940 as difference FROM popANDdensity ORDER BY difference DESC;')
	rows = cur.fetchall()
	for row in rows:
		print row[0],row[1]

##########################################
#### Output: Neighborhood, pop2010, Information
##########################################
with con:
	cur = con.cursor()    
	cur.execute('SELECT p.neighborhood, p.pop2010, e.Information FROM popANDdensity p, employment e WHERE p.neighborhood = e.neighborhood;')
	rows = cur.fetchall()
	for row in rows:
		print row[0],row[1], row[2]	
		
##########################################
#### Output: Neighborhood, MAX(pop2010)
##########################################
with con:
	cur = con.cursor()    
	cur.execute('SELECT neighborhood, pop2010 FROM popANDdensity WHERE pop2010 = (SELECT MAX(pop2010) FROM popANDdensity);')
	rows = cur.fetchall()
	for row in rows:
		print row[0],row[1]
		
		
##########################################
#### Output: Neighborhood, MAX(pop2010), Scientific
##########################################
with con:
	cur = con.cursor()    
	cur.execute('SELECT p.neighborhood, p.pop2010, e.Scientific FROM popANDdensity p, employment e WHERE p.neighborhood = e.neighborhood AND p.pop2010 = (SELECT MAX(pop2010) FROM popANDdensity);')
	rows = cur.fetchall()
	for row in rows:
		print row[0],row[1],row[2] 
