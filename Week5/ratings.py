################################
### Creates Database
### Updates Database with Data
################################

import sqlite3 as lite
import sys
import os 
import csv
import urllib
import re

ratingsList = "http://boxnumbertwo.com/MovieData/ratings.list"
response = urllib.urlopen(ratingsList)
#c = 0 
movies = dict()
for line in response:
	words = re.sub(' +',' ',line.strip()).split(" ", 3)
	remove = words[0]
	votes = words[1]
	rating = words[2]
	titleData = words[3].split("(")
	title = titleData[0].strip()
	year = titleData[1].split(")")[0]
	year = year[0:4]
	if title in movies:
		if movies[title][0] < votes:
			movies[title] = [votes,rating,year]
	else: movies[title] = [votes,rating,year]
#	if c == 100: break
#	else: c = c + 1

## Creates a folder for the database
## Set directory to YOUR computer and folder
directoryForDB = "C:/Users/Pudders/Desktop/MovieData/"
if not os.path.exists(directoryForDB):
	os.makedirs(directoryForDB)

directoryForDB = directoryForDB + "movies.db"
## If database does not exist, creates items
## If database does exist, opens it
con = lite.connect(directoryForDB)

########################################
##### add data for ratings

########################################
with con:

	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS ratings") 
	cur.execute("CREATE TABLE ratings(title TEXT, votes INT, rating REAL, year INT)")
	for key in movies:
		try: 
			insertStatement = """INSERT INTO ratings VALUES('%s',%s,%s,%s)""" % (key, movies[key][0], movies[key][1], movies[key][2])
			cur.execute(insertStatement)
		except:
			continue
	## NEEDED, if not, database does not update
	con.commit()	
