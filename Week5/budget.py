################################
### Creates Database
### Updates Database with Data
################################

from BeautifulSoup import *
import urllib
import os
import sqlite3 as lite
import sys


siteHTML = "http://boxnumbertwo.com/MovieData/budget.html"
html = urllib.urlopen(siteHTML).read()
soup = BeautifulSoup(html)
# Retrieve all of the anchor tags
tables = soup.findAll("table")
rows = tables[0].findAll('tr')
c = 0 
movies = dict()
for row in rows:
	cols = row.findAll('td')
	if cols == []: continue
	#if c == 10: break
	#else: c = c + 1
	num = cols[0].text.strip()
	date = cols[1].text.strip().split("/")
	month = date[0]
	day = date[1]
	year = date[2]
	title = cols[2].text.strip()
	budget = cols[3].text.strip().replace("$","").replace(",","")
	dGross = cols[4].text.strip().replace("$","").replace(",","")
	wGross = cols[5].text.strip().replace("$","").replace(",","")
	movies[title] = [budget, dGross, wGross, year, month, day]
## Set directory to YOUR computer and folder
directoryForDB = "C:/Users/Pudders/Desktop/MovieData/"
if not os.path.exists(directoryForDB):
	os.makedirs(directoryForDB)

directoryForDB = directoryForDB + "movies.db"
## If database does not exist, creates items
## If database does exist, opens it
con = lite.connect(directoryForDB)

########################################
##### add data for budget
########################################
with con:

	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS budget") 
	cur.execute("CREATE TABLE budget(title TEXT, budget INT, dGross INT, wGross INT, year INT, month INT, day INT)")
	for key in movies:
		try: 
			insertStatement = """INSERT INTO budget VALUES('%s',%s,%s,%s,%s)""" % (key, movies[key][0], movies[key][1], movies[key][2], movies[key][3], movies[key][4], movies[key][5])
			cur.execute(insertStatement)
		except:
			continue
	## NEEDED, if not, database does not update
	con.commit()	
