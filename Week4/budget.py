from BeautifulSoup import *
import urllib
import os
import sqlite3 as lite
import sys


siteHTML = "http://boxnumbertwo.com/MovieData/budget.html"
html = urllib.urlopen(siteHTML).read()
soup = BeautifulSoup(html)
tables = soup.findAll("table")