print """<?xml version="1.0" encoding="UTF-8"?>\n"""
print """<gexf xmlns="http://www.gexf.net/1.2draft" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.gexf.net/1.2draft http://www.gexf.net/1.2draft/gexf.xsd" version="1.2">\n"""
now = datetime.datetime.now()
currentDate = now.strftime("%Y-%m-%d")		
writeDateCreated = """\t<meta lastmodifieddate="%s">\n""" % (currentDate)
writeToFile.write(writeDateCreated)
print """\t\t<creator>DTNA</creator>\n"""
print """\t</meta>\n"""
print """\t<graph mode="dynamic" defaultedgetype="directed" timeformat="dateTime">\n"""

########################################################
############# NODES ####################################
########################################################
print """\t\t<nodes>\n"""

for node in nodes:
	print """\t\t\t<node id="%s" label="%s" start="%s"/>\n""" % (id, userName, dateOfPost)
print """\t\t</nodes>\n"""	
########################################################
############# EDGES ####################################
########################################################
print """\t\t<edges>\n"""
for row in results:
	edgeWriteStatement = """\t\t\t<edge source="%s" target="%s" start="%s"/>\n""" % (source, target, dateOfPost)
print """\t\t</edges>\n"""	

print """\t</graph>\n"""
print """</gexf>\n"""
