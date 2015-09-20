import csv
import urllib

PopulationAndDensity = "http://boxnumbertwo.com/PittsburghData/Population_and_Density.csv"

fhand = urllib.urlopen(PopulationAndDensity)

pop1940to2010 = dict()
try:
	reader = csv.reader(fhand)
	next(reader, None)  # skip the headers
	for row in reader:
		pop1940to2010['%s' % row[0]] = {'pop1940': int(row[2].replace(',','')), 'pop1950': int(row[3].replace(',','')), 'pop1960': int(row[4].replace(',','')), 'pop1970': int(row[5].replace(',','')), 'pop1980': int(row[6].replace(',','')), 'pop1990': int(row[7].replace(',','')), 'pop2000': int(row[8].replace(',','')), 'pop2010': int(row[9].replace(',',''))} 
finally:
	fhand.close()
	
popDifference4050 = dict()	#Unused
diff = [0,0,0,0,0,0,0] 	#store difference between differeng years
for key in pop1940to2010:
	diff[0] += pop1940to2010[key]['pop1950']-pop1940to2010[key]['pop1940']
	diff[1] += pop1940to2010[key]['pop1960']-pop1940to2010[key]['pop1950']
	diff[2] += pop1940to2010[key]['pop1970']-pop1940to2010[key]['pop1960']
	diff[3] += pop1940to2010[key]['pop1980']-pop1940to2010[key]['pop1970']
	diff[4] += pop1940to2010[key]['pop1990']-pop1940to2010[key]['pop1980']
	diff[5] += pop1940to2010[key]['pop2000']-pop1940to2010[key]['pop1990']
	diff[6] += pop1940to2010[key]['pop2010']-pop1940to2010[key]['pop2000']
	

print "Difference between 1940 - 1950: ", diff[0]
print "Difference between 1950 - 1960: ", diff[1]
print "Difference between 1960 - 1970: ", diff[2]
print "Difference between 1970 - 1980: ", diff[3]
print "Difference between 1980 - 1990: ", diff[4]
print "Difference between 1990 - 2000: ", diff[5]
print "Difference between 2000 - 2010: ", diff[6]

#Difference between 1940 - 1950:  5148
#Difference between 1950 - 1960:  -61563
#Difference between 1960 - 1970:  -95088
#Difference between 1970 - 1980:  -96216
#Difference between 1980 - 1990:  -54059
#Difference between 1990 - 2000:  -36352
#Difference between 2000 - 2010:  -27823

print "#Difference between 1940 - 1950 for Mount Washington: ", pop1940to2010['Mount Washington']['pop1950'] - pop1940to2010['Mount Washington']['pop1940']
print "#Difference between 1950 - 1960 for Mount Washington: ", pop1940to2010['Mount Washington']['pop1960'] - pop1940to2010['Mount Washington']['pop1950']
print "#Difference between 1960 - 1970 for Mount Washington: ", pop1940to2010['Mount Washington']['pop1970'] - pop1940to2010['Mount Washington']['pop1960']
print "#Difference between 1970 - 1980 for Mount Washington: ", pop1940to2010['Mount Washington']['pop1980'] - pop1940to2010['Mount Washington']['pop1970']
print "#Difference between 1980 - 1990 for Mount Washington: ", pop1940to2010['Mount Washington']['pop1990'] - pop1940to2010['Mount Washington']['pop1980']
print "#Difference between 1990 - 2000 for Mount Washington: ", pop1940to2010['Mount Washington']['pop2000'] - pop1940to2010['Mount Washington']['pop1990']
print "#Difference between 2000 - 2010 for Mount Washington: ", pop1940to2010['Mount Washington']['pop2010'] - pop1940to2010['Mount Washington']['pop2000']
#Difference between 1940 - 1950 for Mount Washington:  -953
#Difference between 1950 - 1960 for Mount Washington:  -1645
#Difference between 1960 - 1970 for Mount Washington:  -2628
#Difference between 1970 - 1980 for Mount Washington:  -2992
#Difference between 1980 - 1990 for Mount Washington:  -1095
#Difference between 1990 - 2000 for Mount Washington:  -822
#Difference between 2000 - 2010 for Mount Washington:  -1079

print "#Difference between 1940 - 1950 for North Oakland: ", pop1940to2010['North Oakland']['pop1950'] - pop1940to2010['North Oakland']['pop1940']
print "#Difference between 1950 - 1960 for North Oakland: ", pop1940to2010['North Oakland']['pop1960'] - pop1940to2010['North Oakland']['pop1950']
print "#Difference between 1960 - 1970 for North Oakland: ", pop1940to2010['North Oakland']['pop1970'] - pop1940to2010['North Oakland']['pop1960']
print "#Difference between 1970 - 1980 for North Oakland: ", pop1940to2010['North Oakland']['pop1980'] - pop1940to2010['North Oakland']['pop1970']
print "#Difference between 1980 - 1990 for North Oakland: ", pop1940to2010['North Oakland']['pop1990'] - pop1940to2010['North Oakland']['pop1980']
print "#Difference between 1990 - 2000 for North Oakland: ", pop1940to2010['North Oakland']['pop2000'] - pop1940to2010['North Oakland']['pop1990']
print "#Difference between 2000 - 2010 for North Oakland: ", pop1940to2010['North Oakland']['pop2010'] - pop1940to2010['North Oakland']['pop2000']
#Difference between 1940 - 1950 for North Oakland:  1936
#Difference between 1950 - 1960 for North Oakland:  -610
#Difference between 1960 - 1970 for North Oakland:  1213
#Difference between 1970 - 1980 for North Oakland:  42
#Difference between 1980 - 1990 for North Oakland:  2128
#Difference between 1990 - 2000 for North Oakland:  -979
#Difference between 2000 - 2010 for North Oakland:  694

	
print "#Difference between 1940 - 1950 for Shadyside: ", pop1940to2010['Shadyside']['pop1950'] - pop1940to2010['Shadyside']['pop1940']
print "#Difference between 1950 - 1960 for Shadyside: ", pop1940to2010['Shadyside']['pop1960'] - pop1940to2010['Shadyside']['pop1950']
print "#Difference between 1960 - 1970 for Shadyside: ", pop1940to2010['Shadyside']['pop1970'] - pop1940to2010['Shadyside']['pop1960']
print "#Difference between 1970 - 1980 for Shadyside: ", pop1940to2010['Shadyside']['pop1980'] - pop1940to2010['Shadyside']['pop1970']
print "#Difference between 1980 - 1990 for Shadyside: ", pop1940to2010['Shadyside']['pop1990'] - pop1940to2010['Shadyside']['pop1980']
print "#Difference between 1990 - 2000 for Shadyside: ", pop1940to2010['Shadyside']['pop2000'] - pop1940to2010['Shadyside']['pop1990']
print "#Difference between 2000 - 2010 for Shadyside: ", pop1940to2010['Shadyside']['pop2010'] - pop1940to2010['Shadyside']['pop2000']
#Difference between 1940 - 1950 for Shadyside:  1599
#Difference between 1950 - 1960 for Shadyside:  -1102
#Difference between 1960 - 1970 for Shadyside:  -2329
#Difference between 1970 - 1980 for Shadyside:  -1903
#Difference between 1980 - 1990 for Shadyside:  -560
#Difference between 1990 - 2000 for Shadyside:  369
#Difference between 2000 - 2010 for Shadyside:  161

totalDiff20101940 = dict()  
for key in pop1940to2010:
	totalDiff20101940[key]=pop1940to2010[key]['pop2010']-pop1940to2010[key]['pop1940']
### USE THIS TO SORT, Returns a list (array) ###
totalDiff20101940 = sorted(totalDiff20101940.items(), key=lambda x:x[1])
print "Top 10 - Worst"
for worst in totalDiff20101940[0:10]:   ### print the top 10 worst
	print '\t',worst

print "Top 10 - Best"	
for best in totalDiff20101940[-11:-1]:   ### print the top 10 best
	print '\t',best
	
#Top 10 - Worst

#  ('South Side Flats', -15879)
#  ('Middle Hill', -15322)
#  ('Crawford-Roberts', -14789)
#  ('Bloomfield', -12266)
#  ('Larimer', -11610)
#  ('Mount Washington', -11214)
#  ('East Allegheny', -10835)
#  ('Homewood South', -10678)
#  ('South Side Slopes', -10660)
#  ('Perry South', -10521)
#  ('Homewood North', -10319)
#Top 10 - Best
#  ('Stanton Heights', -9)
#  ('Bon Air', -6)
#  ('Swisshelm Park', 23)
#  ('Oakwood', 290)
#  ('New Homestead', 301)
#  ('Northview Heights', 552)
#  ('Westwood', 618)
#  ('Squirrel Hill North', 928)
#  ('Windgap', 1151)
#  ('Banksville', 2930)
#  ('North Oakland', 4424)
	
