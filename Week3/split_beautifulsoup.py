#### split(str,maxsplit) #####################
# takes a string and splits the string to create a list (array)
stringHello = "hello from Pittsburgh"
stringHello.split(" ")
#OUTPUT: ['hello', 'from', 'Pittsburgh']
words = stringHello.split(" ")
print words[0]
#OUTPUT: hello
stringHello.split(" ",1)
#OUTPUT: ['hello', 'from Pittsburgh']
words = stringHello.split(" ",1)
print words[1]
#OUTPUT: from Pittsburgh

#### BeautifulSoup Example #
from BeautifulSoup import *
import urllib
siteHTML = "http://www.pitt.edu/~pmd18/htmlTest/"
html = urllib.urlopen(siteHTML).read()
soup = BeautifulSoup(html)
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
 print "# " + tag.get('href', None)
 
# http://www.sis.pitt.edu
# http://www.chrisharrison.net/projects/visualization.html
# http://vis.robbymacdonell.com/stanley-cup/
# http://www.ted.com/talks/david_mccandless_the_beauty_of_data_visualization.html
# http://www.thewildernessdowntown.com/

# Idea from: http://www.briancarpio.com/2012/12/02/website-scraping-with-python-and-beautiful-soup/
soup = BeautifulSoup(urllib.urlopen('http://www.usamega.com/mega-millions-history.asp?p=1').read())
#print soup
#print(soup.prettify())
#print soup('table')[4].findAll('tr')[1].findAll('td')[1].a.text

#for row in soup('table')[4].findAll('tr'):
# tds = row('td')
# print tds

#for row in soup('table')[4].findAll('tr'):
# for col in row.findAll('td'):
#  print col.text
