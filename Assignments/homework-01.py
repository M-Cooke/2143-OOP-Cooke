"""
Micah Cooke
micahcooke75@gmail.com
Homework 1 - Lists and Dictionaries
19 Sep @ 1:00 p.m.

"""

# 1.1 Basics
# A:
a = [1,5,4,2,3]
print(a[0], a[-1])
#Prints: 1 3
a[4] = a[2] + a[-2]
print(a)
#Prints: [1,5,4,2,6]
print(len(a)) 
#Prints: 5
print(4 in a)
#Prints: True
a[1] = [a[1],a[0]]
print(a)
#Prints: [1,[5,1],4,2,6]

# 1.2 List Methods
# B:
x = [3,1,2,1,5,1,1,7]
def remove_all(el,lst):
	while el in lst:
		lst.remove(el)
remove_all(1,x)
print(x)
#Prints: [3,2,5,7]

# C:
lst = [1,2,4,2,1]
def add_this_many(x,y,lst):
	for i in lst:
		if i == x:
			lst.append(y)
	print(lst)
add_this_many(1,5,lst)
#Prints: [1,2,4,2,1,5,5]

# 1.3 Slicing
# D:
a = [3,1,4,2,5,3]
print(a[:4])
#Prints: [3,1,4,2]
print(a)
#Prints: [3,1,4,2,5,3]
print(a[1::2])
#Prints: [1,2,3]
print(a[:])
#Prints: [3,1,4,2,5,3]
print(a[4:2])
#[]
print(a[1:-2])
#Prints: [1,4,2]
print(a[::-1])
#Prints: [3,5,2,4,1,3]

# 1.4 For Loops
# E:
x = [3,2,4,5,1]
def reverse(x):
	x.reverse()
	print(x)
reverse(x)
#Prints: [1,5,4,2,3]
# The "in place" solution is preferred because it is faster and more simple.

# F:
x = [1,2,3,4,5]
def rotate(lst, k):
	print(lst[-k:] + lst[:-k])
rotate(x,3)

#Prints: [3,4,5,1,2]

# 2 Dictionaries
# H:
superbowls = {'joe montana': 4, 'tom brady':3, 'joe flacco': 0}
print(superbowls['tom brady'])
# Prints: 3

superbowls['peyton manning'] = 1
print(superbowls)
# Prints: {'peyton manning': 1, 'tom brady': 3, 'joe flacco': 0, 'joe montana': 4}

superbowls['joe flacco'] = 1
print(superbowls)
# Prints:{'peyton manning': 1, 'tom brady': 3, 'joe flacco': 1, 'joe montana': 4}

print(superbowls['peyton manning'] == superbowls['joe montana'])
#Prints: False

superbowls[('eli manning', 'giants')] = 2
print(superbowls)
#Prints: {('eli manning', 'giants'): 2, 'tom brady': 3, 'peyton manning': 1, 'joe montana': 4, 'joe flacco': 1}

superbowls[3] = 'cat'
print(superbowls)
#Prints: {3: 'cat', 'joe montana': 4, 'tom brady': 3, ('eli manning', 'giants'): 2, 'peyton manning': 1, 'joe flacco': 1}


superbowls[('eli manning', 'giants')] =  superbowls['joe montana'] + superbowls['peyton manning']
print(superbowls)
#Prints: {3: 'cat', 'joe montana': 4, 'tom brady': 3, ('eli manning', 'giants'): 5, 'peyton manning': 1, 'joe flacco': 1}

superbowls[('steelers', '49ers')] = 11
print(superbowls)
#Prints: {'joe flacco': 1, 3: 'cat', 'joe montana': 4, ('steelers', '49ers'): 11, ('eli manning', 'giants'): 5, 'peyton manning': 1, 'tom brady': 3}

# I:
d = {1:{2:3, 3:4}, 2: {4:4, 5:3}}
def replace_all(d, x, y):
	for k in d.keys():
		if type(d[k]) == dict:
			replace_all(d[k], x, y)
		else:
			d[k] = y if d[k] == x else d[k]

replace_all(d, 3, 1)
print(d)
#Prints: {1: {2: 1, 3: 4}, 2: {4: 4, 5:1}}

# J:
d = {1:2, 2:3, 3:2, 4:3}
def rm(d,x):
	temp = [k for k in d.keys() if d[k] == x]
	for k in temp:
		del d[k]
	print(d)
rm(d,2)
#Prints: {2: 3, 4: 3}

