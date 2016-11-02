# Study Guide

##Q:

### Color Class

- Create a class called "Color" that will store a tuple of (r,g,b). 
- The tuple should be stored in a data member called color.
- The components of the color tuple should be stored in data members: red, green, blue as well 
- Add a __str__ method to print out the color class so it looks like: "(red: redVal, green: greenVal, blue: blueVal)"
- Here is some usage:

```python

c1 = Color((255,0,0))
print(c1.red)
#prints: 255

c1.blue = 255
print(c1)
#prints: (red: 255, green: 0, blue: 255)

c1.setColor((0,0,0))
print(c1)
#prints: (red: 0, green: 0, blue: 0)

```
----
##Answer:
```python
class Color(object):
    def __init__(self, color =(0,0,0)):
		self.color = color 
		self.red = self.color[0]
		self.green = self.color[1]
		self.blue = self.color[2]
		
    def setColor(self,(r,g,b)):
		self.color = (r,g,b)
		self.red = r 
		self.green = g 
		self.blue = b
		
    def __str__(self):
		return "(red: %d, green: %d, blue: %d)" % (self.red, self.green, self.blue)
	
    def __repr__(self):
		return self.__str__()
```
----

##Q:

Overload the addition operator so that we can add two colors. Adding colors is a pretty wierd experience, so we will create our own addition method. Basically we will average each color. 

For example:

```python

c1 = Color(255,255,255)
c2 = Color(0,0,0)
c3 = c1 + c2

print(c3)
#prints: (red: 128,green: 128,blue: 128)
```
----
##Answer:
```python
    def __add__(self, rhs = (0,0,0)):
        nred = (self.color[0] + rhs.color[0])/2
        ngreen = (self.color[1] + rhs.color[1])/2
        nblue = (self.color[2] + rhs.color[2])/2        
        return "(red: %d, green: %d, blue: %d)" % (nred, ngreen, nblue)
```
----

##Q:

### Grayscale Class

This class will ***extend*** the color class.

So what is gray scale? Its where you take the 3 individual parts of a color and using those values you calculate a single value that will be assigned to each of the 3 components, making it some shade of gray.
 
For example here is red: `(0,255,0)` and here is the gray scale equivalent: `(85,85,85)` (using the average method from below).

Your `GrayScaler` class is serious about its grayscalin` powers and has three methods to turn a color into its monochromatic equivalent:
- lightness
- average
- luminosity
- custom

**Lightness**

The lightness method averages the most prominent and least prominent colors: `(max(R, G, B) + min(R, G, B)) / 2`.

**Average**

The average method simply averages the values: `(R + G + B) / 3`.

**Luminosity**

This method also averages the values, but it forms a weighted average to account for human perception. We’re more sensitive to green than other colors, so green is weighted most heavily. The formula for luminosity is `0.21 * R + 0.72 * G + 0.07 * B`

**Custom**

This method allows the user to pass in three floats to act as the weights in your formula: `w1 * R + w2 * G + w3 * B`

Here is some example usage to help you determine how to design your class:

```python

myColor = (255,0,0)
grayish = GrayScaler(myColor)
gray1 = grayish.Average()
gray2 = grayish.Custom(.33,.44,.23)


grayish2 = GrayScaler() # defaults to black in the class if no color provided
grayish2.SetColor(255,192,203)
gray3 = grayish2.Luminosity()
```

```python
"""
@Description: Gets an RGB color represented as a tuple, and converts it to a 
				gray scale equivalent based on chosen method.
@Methods:
    Lightness - as described above
    Average - as described above
    Luminosity - as described above
    Custom - as described above
    SetColor - Lets user change the color originally passed in.
"""
class GrayScaler(Color):







```
----
##Answer:
```python
class GrayScaler(Color):
    def __init__(self, color = (0,0,0)):
        Color.__init__(self, color = (0,0,0))
    def SetColor(self, (r,g,b)):
        Color.setColor(self, (r,g,b))
    def __str__(self):
        return "(red: %d, green: %d, blue: %d)" % (self.color[0], self.color[1], self.color[2])
        
    def Lightness(self):
        L = (max(self.red, self.green, self.blue) + min(self.red, self.green, self.blue))/2
        return Color((L,L,L))
    def Average(self):
        A = (self.red + self.green + self.blue) / 3
        return Color((A,A,A))
    def Luminosity(self):
        R = 0.21 * self.red
        G = 0.72 * self.green
        B = 0.07 * self.blue
        return Color((R, G, B))
    def Custom (self, w1, w2,w3):
        R = w1 * self.red
        G = w2 * self.green
        B = w3 * self.blue
        return Color((R, G, B))
```
----

## Q:

Create a point class, line class, and a rectangle class. 

- A point is a tuple of two integers: (3,6)
- A line consists of two points: (3,6),(7,8)
    - Add a length method 
- A rectangle consists of two points as well, the upper right, and the lower left.
    - Add an area and perimeter method

----
##Answer:
```python
import math

class Point(object):
    def __init__ (self, x, y):
        self.x= x
        self.y= y 
        self.point = (self.x, self.y)

    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)

    def __repr(self):
        return self.__str__()

class Line(Point):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.line = (p1,p2)

    def length(self):
        return math.sqrt(pow((self.p2.x-self.p1.x),2) + pow((self.p2.y -self.p1.y),2))
```

----

## Q:

```python
class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_old(self):
        return self.age > 40

        
person = Person('G. H. Hardy', 70)  
print person.is_old() # Prints True
```

Write a `Student` class that extends the `Person` class and add a method: `is_honor_student` that would print `True` if the students gpa is greater than 3.0

```python
student = Student('G. H. Hardy', 70, 4.0)
print student.is_old()	# prints True
print student.is_honor_student()	# prints True
```
----
##Answer:
```python
class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_old(self):
        return self.age > 40

class Student(Person):
	def __init__(self,name, age, gpa):
		Person.__init__(self,name,age)
		self.gpa = gpa
	
	def is_honor_student(self):
		return self.gpa > 3.0
```
----

## Q:

Run a binary search on the following values looking for key=55. Show the index values for `first` `mid` and `last` at each iteration.

| 0  | 1 |2 | 3  |  4|  5	|  6	|7|  8	| 9 	|  10	|  
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 5 | 13| 19 | 22	| 41	| 55	| 68	| 72	| 81	| 98 |

----
##Answer:
```python
nums = [0,5,13,19,22,41,55,68,72,81,98]


searchKey = 55
print(searchKey)


nums = sorted(nums)

print(nums)

f = 0
print("f = %d" % (f))
l = len(nums)
print("l = %d" % (l))
m = (f + l) // 2
print("m = %d" % (m))


Found = False

while not Found:
    if nums[m] == searchKey:
        Found = True
        print(m)
        break
    print("This is a new iteration")
    if searchKey > nums[m]:
        f = m 
       
    else:
        l = m
      

    m = (f + l) // 2
    print("f = %d" % (f))
    print("m = %d" % (m))
    print("l = %d" % (l))
```
----

## Q:

Write a function that removes all instances of an element from a list.

```python
def remove_all(el, lst):
"""Removes all instances of el from lst.
>>> x = [3, 1, 2, 1, 5, 1, 1, 7]
>>> remove_all(1, x)
>>> x
[3, 2, 5, 7]
"""



```
----
##Answer:
```python
def remove_all(el, lst):
	while el in lst:
		lst.remove(el)
		
x = [3, 1, 2, 1, 5, 1, 1, 7]
remove_all(1, x)
print(x)
```
----

## Q: 

Given a list of words like so:

```python 
words = [
   'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
   'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
   'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
   'my', 'eyes', "you're", 'under'
]
```

Write a python snippet to find the words that occur most often. You output should look something like the following: 

```python
[('eyes', 8), ('the', 5), ('look', 4)]
```
----
##Answer:
```python
words = [
   'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
   'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
   'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
   'my', 'eyes', "you're", 'under']
   
countList = []
for word in words:
	if not word in countList:
		countList.append(word)
summaryList = []
for target in countList:
	count = 0
	for word in words:
		if word == target:
			count += 1
	summaryList.append((target,count))
	summaryList = sorted(summaryList, key = lambda x: x[1], reverse = True)
print(summaryList[:3])
```
----

## Q:

Write a class called `book_analysis` that will do a word frequency analysis on a book. You can assume that the book has had all punctuation removed. Your class should count the number of unique words and be able to return the **n**<sup>th</sup> most frequent word. Below is some code that WILL actually do what I'm asking you to do (but not in a class).

```python
import string
import operator

#url for book = http://www.gutenberg.org/files/2701/2701.txt
#go to url and save book as moby_dick.txt on your computer
f = open('moby_dick.txt')


dict = {}

for line in f:
    exclude = set(string.punctuation)
    words = ''.join(ch for ch in line.strip() if ch not in exclude).lower()
    for word in words.split(' '):
        if not word in dict:
            dict[word] = 0
        dict[word] += 1

sorted_dict = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)

print(sorted_dict)
```

The `sorted_dict` looks like:

```

[('the', 14508), ('of', 6701), ('and', 6434), ('a', 4690), ('to', 4658), ('in', 4202), ('', 3491), ('that', 2955), ('his', 2520), ('it',2382), ('i', 1943), ('but', 1781), ('with', 1768), ('he', 1749), ('is', 1731), ('as', 1730), ('was', 1637), ('for', 1627), ('all', 1493),('this', 1411), ('at', 1326), ('by', 1219), .... ('repute', 1), ('aftman', 1), ('incredibly', 1), ('flexion', 1), ('shakespeares', 1), ('coursefor', 1), ('scabbards', 1), ('causesuch', 1), ('filial', 1), ('barwait', 1), ('hornsofplenty', 1), ('sash', 1), ('races', 1), ('linenow', 1), ('andromedaindeed', 1)]
```
where the word and occurence are in a tuple.

Your job is to organize into class form. Lets assume the constructor will load the book. Here is some usage:

```python
anlyz = BookAnalysis('moby_dick.txt')
most = anlyz.getnth(3)
print(most)
# ('and', 6434)
x = anlyz.occurs('barwait')
print(x)
# barwait occurs 1 times
print(anlyz.totalWords())
# total words: 20211
```

Some of the methods return a printed message (e.g. "barwait occurs 1 times"), this is ok for this test problem, but normally methods do not print messages and return values!

----
##Answer:
```python
import string
import operator

class Book_analysis(object):
	def __init__(self):
		self.f = open('moby_dick.txt')
		self.dict = {}
		for line in self.f:
    		self.exclude = set(string.punctuation)
    		self.words = ''.join(ch for ch in line.strip() if ch not in exclude).lower()
	    	for word in self.words.split(' '):
    	    	if not word in self.dict:
            		self.dict[word] = 0
        		self.dict[word] += 1

		self.orderlist = sorted(self.dict.items(), key=operator.itemgetter(1), reverse=True)

	def occurs(self,key):
		for zork in self.orderlist:
			if zork[0]==key:
				return zork
			else:
				return None
	
	def get_nth(self,rank):
		return self.oderlist[rank-1]
		
	def countem(self):
		return len(self.orderlist)
    ```

