#####################################################
########### I'm commenting! #########################
#####################################################

#####################################################
########### Section 1 - Variables #########################
#####################################################

variable = "hello"
print variable 
## hello
type(variable)
## <type 'str'>


variable = 12
type(variable)
## <type 'int'>

variable = {"apple","banana"}
type(variable) 
## <type 'set'>

variable = ['1','1','1']
type(variable)
## <type 'list'>

variable = "some string"
print variable
variable[0]
variable[2]
variable[2:4]
variable[0:5]
variable[:5]
variable[5:]

## Return the lowest index in the string where substring sub is found, such that sub is contained in the slice s[start:end].(Case sensitive)
print variable.find("me")
print variable.find("mE")

## Return a copy of the string with its first character capitalized and the rest lowercased.
print variable.capitalize()

## No this attribute (lowercase).
print 'HEllo'.lowercase()

## Return the highest index in the string where substring sub is found (first index of the last instance in the string), such that sub is contained within s[start:end]. 
print 'Hello hllo'.rfind()
## 7

## Return a copy of the string with trailing characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a suffix; rather, all combinations of its values are stripped.
print 'mississippi'.rstrip('ipz')
## mississ

## Return a copy of the string with all occurrences of substring old replaced by new. If the optional argument count is given, only the first count occurrences are replaced.
print 'mississippi'.replace('iss',' ',1)
## m issippi


numberVariable = 42
print "the answer to life, universe, and everything is.. " + `numberVariable`
print "the answer to life, universe, and everything is.. " + str(numberVariable)
## showes no difference.

##############################################################################
#
# Part 1
##############################################################################
# the requisite hello world print statement
print "Hello Pittsburgh!\n";

# create two string variables
# scalar variable (as opposed to array or hash) names are preceded by a 
# do not need to declare the variables (in this case)
course = "2725";
dept = "INFSCI";

# different ways to print statements
print course + " " + dept
# or (using %s corresponding to string)
print "%s %s" % (course,dept)
# choice is yours

# let's concatenate the strings using +
courseAndDept = course + " " + dept
print courseAndDept

# just insert the variable into your print statement to print it
print "i am currently sitting in " + courseAndDept
# or 
print "i am currently sitting in %s" % (courseAndDept)
# or (notice no space after in)
print "i am currently sitting in" , courseAndDept

##############################################################################
#
# Part 2
##############################################################################

# here we're playing with comparison operators
num1 = 101
num2 = 102

# <, >, <= etc. will compare them numerically
if num1 > num2:
	print "num1 is greater"
else:
	print "num2 is greater"
	
# comparing strings
num1 = "101"
num2 = "102"

# comparing strings (notice elif) (-1 when num1 is less than, 0 when they are the same, 1 when num1 is greater)
if cmp(num1,num2) == 1:
	print "num1 is greater"
elif cmp(num1,num2) == 0:
	print "num1 is the same as num2"	
elif cmp(num1,num2) == -1:
	print "num2 is greater"
	
# while loop (let's count to 10!)
# notice the ` ` (these are the brackets for ` / ~)
count = 0
while (count <= 10):
	print "The count is: " + `count`
	count = count + 1
	
# for loop (read out letters) good for lists as well
# notice str()
count = 0
for letter in 'Pittsburgh':     
	print "Letter number : " + str(count) + " is " + letter
	count = count + 1
	
count = 0
city = 'Pittsburgh'
while (count < len(city)):
	print "Letter number : " + str(count) + " is " + city[count]
	count = count + 1
	
#####################################################
########### Section 2 - Arrays/Lists ##############
#####################################################

## index starts from 0
arrayOfNumbers = [0,1,2,3,4,5,6]
print arrayOfNumbers[1]

arrayOfStrings = ["apple", "banana", "carrot"]
print arrayOfNumbers[1]

print arrayOfNumbers[0]

pals = list()
pals.append("Glenn")
pals.append("Sally")
pals.append("Joe")

print pals
## ['Glenn', 'Sally', 'Joe']
print type(pals)

for friend in pals:
	print "I am friends with:" + friend
	
pals[1] = "Lisa"
for friend in pals:
	print "I am friends with:" + friend
	
print pals.index("Joe")

pals.reverse()
print pals.index("Joe")

pal = dict()
pal["first"] = "Glenn"
pal["last"] = "Golden"
pal["email"] = "glenng@some.edu"
pal["phone"] = "123-123-1221"

print pal
## {'phone': '123-123-1221', 'last': 'Golden', 'email': 'glenng@some.edu', 'first': 'Glenn'}
print pal.viewkeys()
## dict_keys(['phone', 'last', 'email', 'first'])
print pal.keys()
## ['phone', 'last', 'email', 'first']
print pal.viewvalues()
## dict_values(['123-123-1221', 'Golden', 'glenng@some.edu', 'Glenn'])
print pal.values()
## ['123-123-1221', 'Golden', 'glenng@some.edu', 'Glenn']
type(pal.values())
## <type 'list'>


print type(pal)
for contactInfo in pal:
	print contactInfo, pal[contactInfo]
	


