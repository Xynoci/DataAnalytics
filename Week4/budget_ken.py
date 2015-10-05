from BeautifulSoup import *
import sqlite3 as lite
# from bs4 import BeautifulSoup 
import urllib
import os
import sqlite3 as lite
import sys


siteHTML = "http://boxnumbertwo.com/MovieData/budget.html"
html = urllib.urlopen(siteHTML).read()
soup = BeautifulSoup(html)
tables = soup.findAll("table")

directoryForDB = "./MovieData/"
if not os.path.exists(directoryForDB):
	os.makedirs(directoryForDB)

directoryForDB = directoryForDB + "movies.db"
## If database does not exist, creates items
## If database does exist, opens it
con = lite.connect(directoryForDB)
#use 8-bit strings instead of unicode string
con.text_factory = str

with con:
	count=0
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS budget") 
	#Create a table named "budget", movieName as the primary key, and budget is another column.
	cur.execute("CREATE TABLE budget(movieName TEXT PRIMARY KEY, budget REAL, domestic REAL, worldwide REAL)")

	for row in soup('table')[0].findAll('tr'):
		budgetDic = dict()
		domesticDic=dict()
		worldwideDic=dict()
		key = ''
		if len(row.findAll('td')) != 0:
			for td in row.findAll('td')[2:3]:
				key+=td.text
	
			for td in row.findAll('td')[1:2]:
				key+=' ('+(str)(td.text)[-4:]+')'	
	
			for td in row.findAll('td')[3:4]:
				budgetValue = []
				budgetValue = td.text.replace(',','')
				budgetValue=budgetValue.replace('$','')
				budgetDic[key]=(str)(budgetValue)
	
			for td in row.findAll('td')[4:5]:
				domesticValue=[]
				domesticValue = td.text.replace(',','')
				domesticValue=domesticValue.replace('$','')
				domesticDic[key]=(str)(domesticValue)
	
			for td in row.findAll('td')[5:6]:
				worldwideValue=[]
				worldwideValue = td.text.replace(',','')
				worldwideValue = worldwideValue.replace('$','')
				worldwideDic[key] = (str)(worldwideValue)
			
			insertStatement = 'INSERT INTO budget VALUES(?,?,?,?)'
			parms = (key,budgetDic[key],domesticDic[key],worldwideDic[key])
			cur.execute(insertStatement, parms)
			print "Inserting: ", key
			count+=1
		con.commit()
	print 'Total records: ',count
