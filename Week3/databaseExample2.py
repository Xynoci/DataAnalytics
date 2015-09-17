################################
### Connects to Database
### Gets Data from Database
################################

import sqlite3 as lite
import sys
import os 


con = None


directoryForDB = "C:/Users/Pudders/Desktop/DBClass/" + "carsDatabase.db"

con = lite.connect(directoryForDB)
############################
## Reminder!
## "CREATE TABLE Cars(Id INT, Name TEXT, Price INT)"
###########################
with con:
	cur = con.cursor()    
	cur.execute('SELECT * FROM Cars')
	rows = cur.fetchall()
	#for row in rows:    
	#	print """%s %s %s""" % (row[0], row[1], row[2])
		
with con:
	cur = con.cursor()    
	cur.execute('SELECT Name FROM Cars')
	rows = cur.fetchall()
	#for row in rows:    
	#	print """%s""" % (row[0])

############################
## Distinct
###########################	
with con:
	cur = con.cursor()    
	cur.execute('SELECT DISTINCT(Price) FROM Cars')
	rows = cur.fetchall()
	#for row in rows:    
	#	print """%s""" % (row[0])

############################
## Where
###########################		
with con:
	cur = con.cursor()    
	cur.execute('SELECT * FROM Cars WHERE Price > 40000')
	rows = cur.fetchall()
	#for row in rows:    
	#	print """%s %s %s""" % (row[0], row[1], row[2])

############################
## Between
###########################			
with con:
	cur = con.cursor()    
	cur.execute('SELECT * FROM Cars WHERE Price between 10000 and 40000')
	rows = cur.fetchall()
	#for row in rows:    
	#	print """%s %s %s""" % (row[0], row[1], row[2])		
	
############################
## Like/Wildcard
###########################			
with con:
	cur = con.cursor()    
	cur.execute('SELECT * FROM Cars WHERE Name LIKE "Vo%"')
	rows = cur.fetchall()
	#for row in rows:    
	#	print """%s %s %s""" % (row[0], row[1], row[2])	

############################
## Order 
###########################			
with con:
	cur = con.cursor()    
	cur.execute('SELECT * FROM Cars ORDER BY Name')
	rows = cur.fetchall()
	#for row in rows:    
	#	print """%s %s %s""" % (row[0], row[1], row[2])
		
with con:
	cur = con.cursor()    
	cur.execute('SELECT * FROM Cars ORDER BY Name ASC')
	rows = cur.fetchall()
	#for row in rows:    
	#	print """%s %s %s""" % (row[0], row[1], row[2])

with con:
	cur = con.cursor()    
	cur.execute('SELECT * FROM Cars ORDER BY Name DESC')
	rows = cur.fetchall()
	#for row in rows:    
	#	print """%s %s %s""" % (row[0], row[1], row[2])		
	
############################
## Count 
###########################	
with con:
	cur = con.cursor()    
	cur.execute('SELECT Count(*) FROM Cars')
	rows = cur.fetchall()
	#for row in rows:    
	#	print """%s""" % (row[0])		
		
with con:
	cur = con.cursor()    
	cur.execute('SELECT Count(*) FROM Cars WHERE Price between 10000 and 40000')
	rows = cur.fetchall()
	#for row in rows:    
	#	print """%s""" % (row[0])			
############################
## Sum 
###########################	
with con:
	cur = con.cursor()    
	cur.execute('SELECT SUM(Price) FROM Cars')
	rows = cur.fetchall()
	#for row in rows:    
	#	print """%s""" % (row[0])	
############################
## Max 
###########################	
with con:
	cur = con.cursor()    
	cur.execute('SELECT MAX(Price) FROM Cars')
	rows = cur.fetchall()
	#for row in rows:    
	#	print """%s""" % (row[0])
		
with con:
	cur = con.cursor()    
	cur.execute('SELECT Name, MAX(Price) FROM Cars;')
	rows = cur.fetchall()
	#for row in rows:    
	#	print """%s %s""" % (row[0], row[1])	

with con:
	cur = con.cursor()    
	cur.execute('SELECT Name, Price FROM Cars WHERE Price = (SELECT MAX(Price) FROM Cars);')
	rows = cur.fetchall()
	#for row in rows:    
	#	print """%s %s""" % (row[0], row[1])		

############################
## Basic Math 
###########################		

with con:
	cur = con.cursor()    
	cur.execute('SELECT Name, Price*1.1 FROM Cars ;')
	rows = cur.fetchall()
	#for row in rows:    
	#	print """%s %s""" % (row[0], row[1])	
	
	
	
directoryForDB = "C:/Users/Pudders/Desktop/DBClass/" + "pittsburghData.db"
con = lite.connect(directoryForDB)
############################
## JOIN (simple)
###########################
with con:
	cur = con.cursor()    
	cur.execute('SELECT p.neighborhood, p.pop1940, e.Construction FROM popANDdensity p, employment e WHERE p.neighborhood = e.neighborhood')
	rows = cur.fetchall()
	#for row in rows:    
	#	print """%s %s %s""" % (row[0], row[1], row[2])
	
with con:
	cur = con.cursor()    
	cur.execute('SELECT p.neighborhood, p.pop1940, e.Construction FROM popANDdensity p, employment e WHERE p.neighborhood = e.neighborhood AND p.pop1940 between 0 and 1000 ')
	rows = cur.fetchall()
	#for row in rows:    
	#	print """%s %s %s""" % (row[0], row[1], row[2])
