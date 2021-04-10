#PRINT

print("Welcome to your first Python program")



#TYPE CONVERSION

aa = 22
print(aa)
print(type(aa))	# impression du typage

bb = float(aa)	# to float
print(bb)
print(type(bb))

cc = str(bb)	# to string
print(cc)
print(type(cc))

dd = int(aa)	# to integer
print(dd)
print(type(dd))

bool("1")		# cast to a boolean value
bool(1)
bool(0)
int(True)
int(False)

my_age = 39
print(my_age)
my_age += 1     #shortcut to update a value
print(my_age)



#NUMERIC EXPRESSIONS

a = 3
aa = a**2	# puissance
print(aa)
ii = 23
ff = ii // 5	# résultat de la division sans le reste
print(ff)
jj = ii / 5	# résultat de la division
print(jj)
kk = ii % 5	# reste de la division
print(kk)



#USER INPUT

Name = input("Enter your name: ")
print("Nice to meet you",Name)



#STRING OPERATIONS

Name[3]                                     # Print the element on index 3 in the string
Name[-1]                                    # Print the last element on index in the string
Name[3:8]                                   # Slicing a string

Name[::2]                                   # Retreive one out of two
Name[0:6:2]                                 # Retreive one out of two (first 6 only)
Good="GsoAo+d"
Good[::2]                                   # Retreive one out of two

print("Lionel \ Meylan")                    # Backslash
print("Lionel \\ Meylan")                   # Include back slash in string
print(r"Lionel \ Meylan")                   # r will tell python that string will be display as raw string

len(Name)                                   # Length of a string

Name + " is the best"                       # Concatenate two strings

3 * Name                                    # Print the string for 3 times

"\n"                                        # New line escape sequence

"\t"                                        # Tabulate



#STRING METHODS

up_Name = Name.upper()						# Convert all the characters in string to upper case
"uppercase".upper()
low_Name = Name.lower()						# Convert all the characters in string to lower case
"lowercase".lower()

Place = Name + "live in Switzerland"
D = Place.replace("Switzerland","CH")		# Replace the old substring with the new target substring is the segment has been found in the string

D.find("live")								# Find the substring in the string. Only the index of the first elment of substring in string will be the output
D.find("China")                             # If cannot find the substring in the string, answer is -1



#CONDITIONAL OPERATORS

	# <  Less than
	# <= Less than or Equal
	# == Equal to
	# >= Greater than or Equal
	# >  Greater than
	# != Not equal



#IF STATEMENT

inp = input("Enter your age:")
age = int(x)
if age > 65:
	print("congratulations")
elif age >= 18:
	print("enjoy your work")
else:
	print("keep dreaming")

if not (album_year == '1984'):				# The not statement checks if the statement is false
    print ("Album year is not 1984")



#LOOPS AND ITERATIONS

#DEFINITE LOOP

#REPEATED STEPS WITH WHILE

n = 5
while n > 0:
	print(n)
	n = n - 1
print("Game over",n)

PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 1
Rating = PlayListRatings[0]					# While loop example with length of a list and score less than 6 
while(i < len(PlayListRatings) and Rating >= 6):
    print(Rating)
    Rating = PlayListRatings[i]
    i = i + 1

squares = ['orange', 'orange', 'purple', 'blue ', 'orange'] 
new_squares = []							# While loop to copy the strings of the list squares to the list new_squares. Stop and exit the loop if the value on the list is not 'orange'
i = 0
while(i< len(squares) and squares[i] == "orange"):
    print(square)
    new_squares.append(squares[i])
    i = i + 1
print(new_squares)	


#IN RANGE

for i in range(5):
	print(i)
print("Voilà!")


#FOR ... IN

for i in("\n",12,"cats","\n",34,"dogs"):
	print(i)

friends = ["S ophie","O livier","R obert","R ichard","Y van"]
for friend in friends:
	print(friend)

dates = [1982,1980,1973]					# For loop example with length of a list
N = len(dates)
for i in range(N):
    print(dates[i])  

squares=['red','blue','green','purple']
for i, square in enumerate(squares):		# Loop through the list and iterate on both index and element value
    print(i, square)
	


#INDEFINITE LOOP

#BREAKING OUT OF AN INDEFINITE LOOP (keeps going until a logical condition become False)

while True:
	inp = input("Enter 'yes', 'no' or 'quit': ")
	if inp == "quit":
		break
	print(inp)
print("Au revoir")


#TRY & EXCEPT

x = input("Enter your age: ")
try:
	age=int(x)
except:
	print("Not a number")
print("Voilà")


a = 1
try:                            			# Python tries to execute the code in the try block. In this case if there is any exception raised by the code in the try block it will be caught and the code block in the except block will be executed.
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:       			# A specific try except allows you to catch certain exceptions and also execute certain code depending on the exception
    print("The number you provided can't divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:                         			# You can also have an empty except at the end to catch an unexpected exception:
    print("Something went wrong")
else:                           			# Else allows one to check if there was no exception when executing the try block. This is useful when we want to execute something only if there were no errors.
    print("success a=",a)
finally:                        			# Finally allows us to always execute something even if there is an exception or not. This is usually used to signify the end of the try except
    print("Processing Complete")



#THE USE OF CONTINUE IN A LOOP

count = 0
sum = 0
while True:
	inp = input("Enter a number ('quit' to interrupt): ")
	try:
		x = int(inp)
		sum = sum + x
		count = count + 1
		print("Step: ",count,"Sum: ",sum)
	except:
		if inp == "quit":
			break
		else:
			print("Not a number!")
			continue
print("Have a good day !")



#LOOP IDIOMS

#FINDING THE LARGEST VALUE

largest_so_far = None
print("Before",largest_so_far)
for num in [89,34,3,5,34,65,23,54,234,54,345]:
	if largest_so_far is None or largest_so_far < num:
		largest_so_far = num
	print(largest_so_far,num)
print("After",largest_so_far)


#FINDING THE SMALLEST VALUE

smallest_so_far = None
print("Before",smallest_so_far)
for num in [89,34,3,5,34,65,23,54,234,54,345]:
	if smallest_so_far is None:
		smallest_so_far = num
	elif smallest_so_far > num:
		smallest_so_far = num
	print(smallest_so_far,num)
print("After",smallest_so_far)


#COUTING IN A LOOP

friends = ["Robert","Fred","John","Paul","Jean","Marie","Anna"]
count = 0
for friend in friends:
	count = count + 1
	print(count,friend)

	
#SUMMING IN A LOOP

scores = [4,5,67,54,56,78,7]
total = 0
count = 0
for score in scores:
	total = total + score
	count = count + 1
	print("After",count,"Total is",total)
	print("Average is",total/count)


#SEARCH USING A BOOLEAN VARIABLE

found = False
print("Before",found)
for value in[56,4,67,34,2,34,54,66,77]:
	if value == 34:
		found = True
	print(found,value)
print("After",found)
	


#LISTS are mutable

Lists = [1,5.556,"Restaurant",3.20]

Lists = [1,5.556,[23,43,"%"],3.20]          # Nested list in a list
Lists = [1,5.556,("name","ddb",176),3.20]   # Nested tuple in a list

Lists2 = Lists + (8,9.9,"Mean",4,5.77)      # Concatenate two lists
Lists.extend(["dessert","café"])            # Use extend to add elements to list
Lists.append(["Pop",10])                    # Use append to add elements to list

Lists[1] = "Lionel"                         # Change the element based on the index
del(Lists[1])                               # Delete the element based on the index

"Lionel Meylan".split()                     # Split the string, default is by space
"Today, now, here, it's warm.".split(",")   # Split the string by comma (specified delimiter)

ratings = [4,56,76,4,89,34,99]              # Sort a list in a new list
sorted_ratings = sorted(ratings)
print(sorted_ratings)

ratings.sort()                              # Sort a list ascending
print(ratings)

ratings.reverse()							# Sort a list descending
print(ratings)


A = ["hard rock", 10, 1.2] ; B = A			# COPY (copy by reference) the list A : When B equal to A; both A and B are referencing the same list in memory
print('A:', A)
print('B:', B)
print('B[0]:', B[0])
A[0] = "banana"
print('B[0]:', B[0])                        # If we change the first element in A to banana, then list B also changes

B = A[:]                                    # CLONE (clone by value) the list A : When B references a new copy or clone of the original list
print('B[0]:', B[0])
A[0] = "hard rock"                          # If you change A, B will not change
print('B[0]:', B[0])

	

#TUPLES are immutable which means you cannot update or change the values of tuple elements

Ratings = (10,9.5,"Good",4,"A",6.66,"C","Bad")
Ratings[5]
Ratings[2:3]
len(Ratings)
print(type(Ratings[0]))
print(type(Ratings[1]))
print(type(Ratings[2]))

Ratings2 = Ratings + (8,9.9,"Mean",4,5.77)  # Concatenate two tuples
Ratings2

Ratings3 = (0, 9, 6, 5, 10, 8, 9, 6, 2)
Ratings3Sorted = sorted(Ratings3)           # Sort the tuple
Ratings3Sorted

Ratings = (2,3,(33,44,"Perfect"),"Bad")     # Nested tuples
Ratings[2]
Ratings[2][2]
Ratings[2][2][3]                            # We can access strings in the second nested tuples using a third index

Ratings.index("Perfect")                    # Find the first index of "Perfect"



#SETS are unordered (unlike lists and tuples)

album_list = ["Michael Jackson","Thriller","Thriller",1982]
album_set = set(album_list)                 # Transform a list into a set
album_set

album_set.add("Ghost of Ushiiro")           # Add element to set
album_set.add("Michael Jackson")            # Try to add duplicate element to the set
album_set.remove("Michael Jackson")         # Remove an element from a set

check = "Thriller" in album_set
print(check)

album_set2 = {"Ghost of Ushiiro","PES4"}
album_set3 = album_set & album_set2			# Intersection of 2 sets
album_set1.intersection(album_set2)			# Use intersection method to find the intersection of album_list1 and album_list2

album_set4 = album_set.union(album_set2)        # Union of 2 sets
album_set5 = album_set1.difference(album_set2)  # Find the difference in set1 but not set2
album_set3.issubset(album_set4)                 # Check if a set is in a subset
album_set4.issubset(album_set3)                 # Check if a set is in a superset



#DICTIONARIES

dict = {"key1":1,"key2":"2","key3":[3,4,5],"key4":(4,5,6),('key5'):5}
dict["key3"]                                # Returns the value
dict["key6"] = "2007"                       # Append value with key into dictionary
del(dict["key1"])                           # Delete entries by key
"key6" in dict                              # Check if a key is in a dictionary
dict.keys()                                 # All the keys in a dictionary
dict.values()                               # All the values in a dictionary



#FUNCTIONS

def hello_world():
    print("Hello world")

hello_world()


def hello():								# Defines the function
	x = input("Enter your name: ")
	print("Hello ",x)
	print("Max",max(x))
	print("Min",min(x))
	if x == "Lionel":
		print("I know you !")
	else:
		print("Nice to meet you !")

hello()										# Calls the function (never executed before)


def greet(lang):
	"""
	The documentation appears in triple quotes 
	"""
	if lang =="french":
		print("Bonjour")
	elif lang =="german":
		print("Guten Morgen")
	else:
		print("Hello")

help(greet)									# Print the documentation stored within """
greet("french")
greet("german")
greet("wathEver")


def addtwo():
	inpA = input("Enter a first number: ")
	intA = int(inpA)
	inpB = input("Enter a second number: ")
	intB = int(inpB)
	added = intA + intB
	return added                            # Returns the result of the function
	
print("Sum is",addtwo())
print("Sum is",addtwo())


def square(a):
    return print(a*a)

x = 3										# Initialize a Global variable
square(x)

square(3)                       			# Directly enter a parameter

def standard(unit=0):						# Set the default value
    if unit == 0:
        print("not started")
    else:
        print("started")
        
standard()									# With default value
standart(9)                     			# With a value of 9


def PrintList(the_list):					# Print a list using for loop
    for element in the_list:
        print(element)
        
PrintList(['1', 1, 'the man', "abc"])


def addItems(list):							# Use function to append in a list
    list.append("Three")
    list.append("Four")

myList = []
addItems(myList)
myList


def printAll(*args):						# All the arguments are into args like a tuple
    print("No of arguments:", len(args)) 
    for argument in args:
        print(argument)

printAll('Horsefeather','Adonis','Bone')


def printDictionary(**args):				# Arguments can also be packed into a dictionary
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')


def triangle_area(base, height):            # Compute the area of a triangle
    """
    Returns the area of a triangle, given the lenght of
    its base and height
    """
    area = (1.0 / 2) * base * height
    return area

print(triangle_area(2,4))


def fahrenheit2celcius(fahrenheit):         # Convert fahrenheit to celcius
    celcius = (5.0 / 9) * (fahrenheit - 32)
    return celcius

print(fahrenheit2celcius(32))


def fahrenheit2kelvin(fahrenheit):          # A function inside a function
    celcius = fahrenheit2celcius(fahrenheit)
    kelvin = celcius + 273.15
    return kelvin

print(fahrenheit2kelvin(32))


def greet(friend, money):                   # A loop (with booelan) in a function
    if friend and (money > 20):
        print('Hi!')
        money = money - 20
    elif friend:
        print('Hello')
    else:
        print('Ha ha')
        money = money + 10
    return money

money = 25

money = greet(True, money)
print("Money:", money,"\n")

money = greet(False, money)
print("Money:", money,"\n")

money = greet(True, money)
print("Money:", money,"\n")


def is_leap_year(year):                 # Return True if year is a leap year, false otherwise
    if (year % 400) == 0:
        return True
    elif (year % 100) == 0:
        return False
    elif (year % 4) == 0:
        return True
    else:
        return False

year = 2012
leap_year = is_leap_year(year)
    
if leap_year:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
    


#CLASS AND OBJECT

#DEFINITION

	#CLASS - a template
	#ATTRIBUTE - A variable within a class
	#METHOD - A function within a class
	#OBJECT - A particular instance of a class
	#CONSTRUCTOR - Code that runs when an object is created
	#INHERITANCE - The ability to extend a class to make a new class

class PartyAnimal:							# Template
	x = 0
	
	def party(self):
		self.x = self.x + 1
		print("So far", self.x)
	
an = PartyAnimal()							# Object : variable & instance of PartyAnimal class

an.party()									# 1st execution of def party
an.party()
an.party()

print("Type: ",type(an))
print("Dir : ",dir(an))


#OBJECT LIFE CYCLE

class PartyAnimal:
	x = 0
	
	def __init__(self):
		print("I'm constructed",self.x)
		
	def party(self):
		self.x = self.x + 1
		print("So far: ",self.x)
	
	def __del__(self):
		print("I'm destructed",self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42
print("an contains: ",an)


#ADDITIONAL PARAMETERS

class PartyAnimal:
	x = 0
	name = ""
	def __init__(self,z):
		self.name = z
		print(self.name,"constructed")
	
	def party(self):
		self.x = self.x + 1
		print(self.name,"party count",self.x)
		
s = PartyAnimal("Sally")
s.party()

j = PartyAnimal("Michael")
j.party()

s.party()


#OBJECT INHERITANCE

class FootballFan(PartyAnimal):				#FootbalFan is a class which extends PartyAnimal above
	points = 0
	def touchdown(self):
		self.points = self.points + 7
		self.party()
		print(self.name,"points",self.points)

s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()


#OBJECT EXAMPLE

class Rectangle (object):					# Definition of a clase rectangle with default values
    def __init__(self, color='yellow', height=10, width=25):
        self.color = color;
        self.height = height;
        self.width = width;

class Circle (object):						# Definition of a class circle   
    def __init__(self, radius, color):
        self.radius = radius;
        self.color = color;
        
    def add_radius(self,r):					# Definition of a method (to add r to radius)
        self.radius = self.radius + r
        return (self.radius)

dir(Circle)									# Plot the methods associated with the class object (including add_radius)

RedCircle = Circle(10, "red")				# Definition of an object RedCircle within the class Circle
print(RedCircle.radius)
print(RedCircle.color)

RedCircle.radius = 100						# Changes the parameter of the object
RedCircle.add_radius(-100)					# Execute the method add_radius


********************************************#