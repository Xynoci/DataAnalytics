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
movies = dict()
for line in response:
	words = re.sub(' +',' ',line.strip())
	
### ADD MORE HERE

## Set directory to YOUR computer and folder
directoryForDB = "C:/Users/Pudders/Desktop/MovieData/"
if not os.path.exists(directoryForDB):
	os.makedirs(directoryForDB)

directoryForDB = directoryForDB + "movies.db"
## If database does not exist, creates items
## If database does exist, opens it
con = lite.connect(directoryForDB)

### ADD MORE HERE
