################################
### Creates Database
### Updates Database with Data
################################

import sqlite3 as lite
import sys
import os 
import csv
import urllib

PopulationAndDensity = "http://boxnumbertwo.com/PittsburghData/Population_and_Density.csv"

fhand = urllib.urlopen(PopulationAndDensity)
pop1940 = dict()
pop1950 = dict()
pop1960 = dict()
pop1970 = dict()
pop1980 = dict()
pop1990 = dict()
pop2000 = dict()
pop2010 = dict()
try:
	reader = csv.reader(fhand)
	next(reader, None)  # skip the headers
	for row in reader:
		pop1940[row[0]] = row[2].replace(',', '')
		pop1950[row[0]] = row[3].replace(',', '')
		pop1960[row[0]] = row[4].replace(',', '')
		pop1970[row[0]] = row[5].replace(',', '')
		pop1980[row[0]] = row[6].replace(',', '')
		pop1990[row[0]] = row[7].replace(',', '')
		pop2000[row[0]] = row[8].replace(',', '')
		pop2010[row[0]] = row[9].replace(',', '')
finally:
	fhand.close()

	
	
Employment = "http://boxnumbertwo.com/PittsburghData/Employment.csv"

fhand = urllib.urlopen(Employment)
jobConstruction = dict()
jobManufacturing = dict()
jobRetail = dict()
jobTransportUtilities = dict()
jobInformation = dict()
jobFinance = dict()
jobScientific = dict()
jobEduHealthSoc = dict()
jobArtsRecreation = dict()
jobPublicAdmin = dict()
jobOther = dict()

try:
	reader = csv.reader(fhand)
	next(reader, None)  # skip the headers
	for row in reader:
		jobConstruction[row[0]] = float(row[16].replace('%', '')) * (.01)
		jobManufacturing[row[0]] = float(row[17].replace('%', '')) * (.01)
		jobRetail[row[0]] = float(row[18].replace('%', '')) * (.01)
		jobTransportUtilities[row[0]] = float(row[19].replace('%', '')) * (.01)
		jobInformation[row[0]] = float(row[20].replace('%', '')) * (.01)
		jobFinance[row[0]] = float(row[21].replace('%', '')) * (.01)
		jobScientific[row[0]] = float(row[22].replace('%', '')) * (.01)
		jobEduHealthSoc[row[0]] = float(row[23].replace('%', '')) * (.01)
		jobArtsRecreation[row[0]] = float(row[24].replace('%', '')) * (.01)
		jobPublicAdmin[row[0]] = float(row[25].replace('%', '')) * (.01)
		jobOther[row[0]] = float(row[26].replace('%', '')) * (.01)
	
finally:
	fhand.close()


con = None

## Creates a folder for the database
## Set directory to YOUR computer and folder
directoryForDB = "./"
if not os.path.exists(directoryForDB):
	os.makedirs(directoryForDB)

directoryForDB = directoryForDB + "pittsburghData.db"
## If database does not exist, creates items
## If database does exist, opens it
con = lite.connect(directoryForDB)

########################################
##### add data for popANDdensity
########################################
with con:

	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS popANDdensity") 
	cur.execute("CREATE TABLE popANDdensity(neighborhood TEXT, pop1940 INT, pop1950 INT, pop1960 INT, pop1970 INT, pop1980 INT, pop1990 INT, pop2000 INT, pop2010 INT)")
	for key in pop1940:
		# insertStatement = 'INSERT INTO popANDdensity(neighborhood,pop1940,pop1950,pop1960,pop1970,pop1980,pop1990,pop2000,pop2010) VALUES(?,?,?,?,?,?,?,?,?)'
		insertStatement = 'INSERT INTO popANDdensity VALUES(?,?,?,?,?,?,?,?,?)'
		parms = (key,pop1940[key],pop1950[key],pop1960[key],pop1970[key],pop1980[key],pop1990[key],pop2000[key],pop2010[key])
		cur.execute(insertStatement, parms)
	## NEEDED, if not, database does not update
	con.commit()

########################################
##### add data for employment
########################################	
con = lite.connect(directoryForDB)
with con:
	# print "add here"
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS Employment") 
	cur.execute("CREATE TABLE Employment(neighborhood TEXT, jobConstruction REAL,jobManufacturing REAL, jobRetail REAL, jobTransportUtilities REAL, jobInformation REAL, jobFinance REAL, jobScientific REAL, jobEduHealthSoc REAL, jobArtsRecreation REAL, jobPublicAdmin REAL, jobOther REAL)")
	for key in jobConstruction:
		employmentInsertStatement = 'INSERT INTO Employment VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'
		parms = (key, jobConstruction[key],jobManufacturing[key], jobRetail[key], jobTransportUtilities[key], jobInformation[key], jobFinance[key], jobScientific[key], jobEduHealthSoc[key], jobArtsRecreation[key], jobPublicAdmin[key], jobOther[key])
		cur.execute(employmentInsertStatement, parms)
	con.commit()
	######################################################
	##### NOTE! to use double/float in sqlite, use REAL
	######################################################	



