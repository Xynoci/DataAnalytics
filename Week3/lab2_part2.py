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
directoryForDB = "./DBClass/" + "pittsburghData.db"

con = lite.connect(directoryForDB)
##########################################
#### Output: Neighborhood, (pop2010 - pop1940) as difference: ORDER by difference DESC
##########################################
print "########## Neighborhood, pop2010-pop1940 ORDER by DESC ##########"
with con:
	cur = con.cursor()    
	cur.execute('SELECT Neighborhood, pop2010 - pop1940 FROM popANDdensity ORDER BY pop2010-pop1940 DESC')
	rows = cur.fetchall()
	for row in rows:
		print row[0],row[1]

##########################################
#### Output: Neighborhood, pop2010, Information
##########################################
print "########## Neighborhood, pop2010, Information ##########"
with con:
	cur = con.cursor()    
	cur.execute('SELECT p.Neighborhood, p.pop2010, e.jobInformation FROM popANDdensity p, Employment e WHERE p.Neighborhood=e.Neighborhood')
	rows = cur.fetchall()
	for row in rows:
		print row[0],row[1], row[2]	
		
##########################################
#### Output: Neighborhood, MAX(pop2010)
##########################################
print "########## Neighborhood, MAX(pop2010)##########"
with con:
	cur = con.cursor()    
	cur.execute('SELECT Neighborhood, MAX(pop2010) AS MAX_pop2010 FROM popANDdensity')
	rows = cur.fetchall()
	for row in rows:
		print row[0],row[1]
		
		
##########################################
#### Output: Neighborhood, MAX(pop2010), Scientific
##########################################
print "########## Neighborhood, MAX(pop2010), jobScientific ##########"
with con:
	cur = con.cursor()    
	cur.execute('SELECT p.Neighborhood, MAX(p.pop2010), e.jobScientific FROM popANDdensity p, Employment e WHERE p.Neighborhood=e.Neighborhood')
	rows = cur.fetchall()
	for row in rows:
		print row[0],row[1],row[2] 
