##Micah Cooke
1: Definitions:
Using python comments, label all lines that an OOP definition could be applied to.
class Employee:

   empCount = 0
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1

   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary


emp1 = Employee("Zara", 2000) 

emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()

print "Total Employee %d" % Employee.empCount



Answer 1
class Employee: 								#class

   empCount = 0   								#class variable
   def __init__(self, name, salary): 					#constructor
      self.name = name  							#instance attribute
      self.salary = salary 						#instance attribute
      Employee.empCount += 1

   def displayCount(self): 						#method
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self): 						#method
      print "Name : ", self.name,  ", Salary: ", self.salary


emp1 = Employee("Zara", 2000)  						#instantiation
emp2 = Employee("Manni", 5000) 						#instantiation

emp1.displayEmployee() 							#method call
emp2.displayEmployee() 							#method call

print "Total Employee %d" % Employee.empCount



2: List Functions
Given the list below:
States = ['Alabama','Illinois','Wyoming','New York', 'Vermont', 'New Hampshire', 'Maine', 'Texas']
A) Sort the list
B) Add 'Oklahoma' to the list in alphabetical order without sorting the list again. Actually, write a function that would add an item to the list in alphabetical order. Example:

Answer 2

States = ['Alabama','Illinois','Wyoming','New York', 'Vermont', 'New Hampshire', 'Maine', 'Texas']
States.sort()
def addInOrder(States,x):
	for i in range(len(States)):
		if x < States[i]:
			States.insert(i,x)
			break 
	return States
addInOrder(States, "Oklahoma")
print(States)
	


3: Looping over Lists
(10 Points)
Using the following list as an example: L = [10,20,30,40,50,60,70,80,90,100] write a function that would divide each value by its index location + 1. Our example list would turn into: L = [10,10,10,10,10,10,10,10,10,10]. Remember NOT to get caught up on these values. Your function should work on any list.
Usage:
L =  [10,20,30,40,50,60,70,80,90,100]
NList = addPrevious(L)
print(NList)
# prints: [10,10,10,10,10,10,10,10,10,10]
Your answer should consist of just the function definition and none of the usage I provided above.


Answer 3

def addPrevious(L):
	lst = []
	for i in range(len(L)):
		lst.append(L[i]/(i+1))
	return lst




4: Looping over Dictionaries
(10 Points)
Given the following dictionary:
months = { 1 : "January", 
        2 : "February", 
        3 : "March", 
        4 : "April", 
        5 : "May", 
        6 : "June", 
        7 : "July",
        8 : "August",
        9 : "September", 
        10 : "October", 
        11 : "November",
        12 : "December" }
Iterate over this dictionary, and create a new one that only uses the first three letters of the month. Also make the new months all lowercase. Your new dictionary should look like:
abbr_months = {1:"jan",
        2 :"feb",
        3 :"mar",
        4 : "apr", 
        5 : "may", 
        6 : "jun", 
        7 : "jul",
        8 : "aug",
        9 : "sep", 
        10 : "oct", 
        11 : "nov",
        12 : "dec" }


To help you look up string slicing and lower.
Your answer should include just the code that loops and creates the new dictionary.



Answer 4 
abbr_months = {}
for k,v in months.items():
	abbr_months[k] = v[:3].lower()
	

5: Min and Max
(10 Points)
Assume that pythons built in min , max , and sort functions are broken. Write a function that receives a list then traverses the list and returns the min , max, and average values in a tuple.
def miniStats(L):
""" 
@Description: Finds the min,max,and average values in a list
@Params: L (list)
@Returns: tuple (int,int,double)
"""
    # Start with a copy of the list so we don’t modify the original.
    L = L[:]




When writing your answer, include the entire function definition (without the comment block).

Answer 5

def miniStats(L):
	L = L[:]
	min = L[0]
	max = L[0]
	sum = 0
	for i in L:
		if i < min:
			min = i
		if i > max:
			max = i
		sum += i
	average = sum/len(L)
	return(min, max, round(average,2))
		

6: Prime Class
Write a class called myPrimes that represents a collection of your prime numbers.
addPrime :
receives a prime number and adds it to your collection of primes
it must be checked to make sure it's prime! (should be a private method that does this).
removePrime:
a method will remove a prime from your list
printPrimes:
this method will print your prime numbers out

Answer 6
class myPrimes(object):
	def __init__(self):
		self.lst = []
		
	def __check__(self, x):
		if x < 2:
			return False
		if x == 2: 
			return True    
		for i in range(2, x, 1):
			if x % i == 0:
				return False
			else:
				return True
		
	def addPrime(self, x):
		if self.__check__(x) == True:
			self.lst.append(x)
		else:
			print("%d is not a prime number." % (x))
	
	def removePrime(self, x):
		self.lst.remove(x)
	
	def printPrimes(self):
		print(self.lst)		
		
b = myPrimes()
b.addPrime(7)
b.addPrime(6)
b.addPrime(13)
b.addPrime(2)
b.removePrime(13)
b.printPrimes()
