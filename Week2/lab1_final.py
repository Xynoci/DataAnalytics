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
	
popDifference4050 = dict()	
popDifference5060 = dict()	
popDifference6070 = dict()	
popDifference7080 = dict()	
popDifference8090 = dict()	
popDifference9000 = dict()	
popDifference0010 = dict()	

for key in pop1940:
	popDifference4050[key] = (int(pop1950[key]) - int(pop1940[key]))
	popDifference5060[key] = (int(pop1960[key]) - int(pop1950[key]))
	popDifference6070[key] = (int(pop1970[key]) - int(pop1960[key]))
	popDifference7080[key] = (int(pop1980[key]) - int(pop1970[key]))
	popDifference8090[key] = (int(pop1990[key]) - int(pop1980[key]))
	popDifference9000[key] = (int(pop2000[key]) - int(pop1990[key]))
	popDifference0010[key] = (int(pop2010[key]) - int(pop2000[key]))
	#print key, pop1940[key], pop2010[key], (int(pop2010[key]) - int(pop1940[key]))
	
diff = 0	
for key in popDifference4050:	
	diff = diff + popDifference4050[key]
print "Difference between 1940 - 1950: ", diff

diff = 0	
for key in popDifference5060:	
	diff = diff + popDifference5060[key]
print "Difference between 1950 - 1960: ", diff

diff = 0	
for key in popDifference6070:	
	diff = diff + popDifference6070[key]
print "Difference between 1960 - 1970: ", diff

diff = 0	
for key in popDifference7080:	
	diff = diff + popDifference7080[key]
print "Difference between 1970 - 1980: ", diff

diff = 0	
for key in popDifference8090:	
	diff = diff + popDifference8090[key]
print "Difference between 1980 - 1990: ", diff

diff = 0	
for key in popDifference9000:	
	diff = diff + popDifference9000[key]
print "Difference between 1990 - 2000: ", diff

diff = 0	
for key in popDifference0010:	
	diff = diff + popDifference0010[key]
print "Difference between 2000 - 2010: ", diff

#Difference between 1940 - 1950:  5148
#Difference between 1950 - 1960:  -61563
#Difference between 1960 - 1970:  -95088
#Difference between 1970 - 1980:  -96216
#Difference between 1980 - 1990:  -54059
#Difference between 1990 - 2000:  -36352
#Difference between 2000 - 2010:  -27823

print "#Difference between 1940 - 1950 for Mount Washington: ", popDifference4050["Mount Washington"]
print "#Difference between 1950 - 1960 for Mount Washington: ", popDifference5060["Mount Washington"]
print "#Difference between 1960 - 1970 for Mount Washington: ", popDifference6070["Mount Washington"]
print "#Difference between 1970 - 1980 for Mount Washington: ", popDifference7080["Mount Washington"]
print "#Difference between 1980 - 1990 for Mount Washington: ", popDifference8090["Mount Washington"]
print "#Difference between 1990 - 2000 for Mount Washington: ", popDifference9000["Mount Washington"]
print "#Difference between 2000 - 2010 for Mount Washington: ", popDifference0010["Mount Washington"]
#Difference between 1940 - 1950 for Mount Washington:  -953
#Difference between 1950 - 1960 for Mount Washington:  -1645
#Difference between 1960 - 1970 for Mount Washington:  -2628
#Difference between 1970 - 1980 for Mount Washington:  -2992
#Difference between 1980 - 1990 for Mount Washington:  -1095
#Difference between 1990 - 2000 for Mount Washington:  -822
#Difference between 2000 - 2010 for Mount Washington:  -1079

print "#Difference between 1940 - 1950 for North Oakland: ", popDifference4050["North Oakland"]
print "#Difference between 1950 - 1960 for North Oakland: ", popDifference5060["North Oakland"]
print "#Difference between 1960 - 1970 for North Oakland: ", popDifference6070["North Oakland"]
print "#Difference between 1970 - 1980 for North Oakland: ", popDifference7080["North Oakland"]
print "#Difference between 1980 - 1990 for North Oakland: ", popDifference8090["North Oakland"]
print "#Difference between 1990 - 2000 for North Oakland: ", popDifference9000["North Oakland"]
print "#Difference between 2000 - 2010 for North Oakland: ", popDifference0010["North Oakland"]
#Difference between 1940 - 1950 for North Oakland:  1936
#Difference between 1950 - 1960 for North Oakland:  -610
#Difference between 1960 - 1970 for North Oakland:  1213
#Difference between 1970 - 1980 for North Oakland:  42
#Difference between 1980 - 1990 for North Oakland:  2128
#Difference between 1990 - 2000 for North Oakland:  -979
#Difference between 2000 - 2010 for North Oakland:  694

	
print "#Difference between 1940 - 1950 for Shadyside: ", popDifference4050["Shadyside"]
print "#Difference between 1950 - 1960 for Shadyside: ", popDifference5060["Shadyside"]
print "#Difference between 1960 - 1970 for Shadyside: ", popDifference6070["Shadyside"]
print "#Difference between 1970 - 1980 for Shadyside: ", popDifference7080["Shadyside"]
print "#Difference between 1980 - 1990 for Shadyside: ", popDifference8090["Shadyside"]
print "#Difference between 1990 - 2000 for Shadyside: ", popDifference9000["Shadyside"]
print "#Difference between 2000 - 2010 for Shadyside: ", popDifference0010["Shadyside"]
#Difference between 1940 - 1950 for Shadyside:  1599
#Difference between 1950 - 1960 for Shadyside:  -1102
#Difference between 1960 - 1970 for Shadyside:  -2329
#Difference between 1970 - 1980 for Shadyside:  -1903
#Difference between 1980 - 1990 for Shadyside:  -560
#Difference between 1990 - 2000 for Shadyside:  369
#Difference between 2000 - 2010 for Shadyside:  161
totalDiff20101940 = dict() 
for key in pop1940:
	totalDiff20101940[key] = (int(pop2010[key]) - int(pop1940[key]))

totalDiff20101940 = sorted(totalDiff20101940.items(), key=lambda x:x[1])
print "Top 10 - Worst"
print type(totalDiff20101940)
for pitt in totalDiff20101940[0:10]:
	print "# ", pitt
print "Top 10 - Best"	
for pitt in totalDiff20101940[len(totalDiff20101940)-11:len(totalDiff20101940)]:
	print "# ", pitt
