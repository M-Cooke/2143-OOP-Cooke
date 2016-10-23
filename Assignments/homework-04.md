##Micah Cooke

###Question 1
```
python

@Class: cat
@Description: sets up a template for cat information
@Methods:
__init__ : constructor that inherits from Pet and adds self.lives
talk: inherits from Pet and specifies what the cat says
lose_life: if the cat's lives are greater than one, then it loses a life and is still considered alive.
	Otherwise, once the life is removed the cat is no longer considered alive.
class Cat(Pet):
	def __init__(self, name, owner, lives=9):
		self.lives = lives

	def talk(self):
		print('meow!')

	def lose_life(self):
		if self.lives >= 1:
			self.lives -= 1
		else:
			self.is_alive = False
```

###Question 2
```
python
class Foo(object):
    def __init__(self, a):
        self.a = a
    def garply(self):
        return self.baz(self.a)

class Bar(Foo):
    a = 1
    def baz(self, val):
        return val

f = Foo(4)
b = Bar(3)
print(f.a)
# prints: 4 

print(b.a)
# prints: 3

print(f.garply())
# prints: Error because baz is defined in Bar not Foo, and Foo does not inherit from Bar.
print(b.garply())
# prints: 3

b.a = 9
print(b.garply())
# prints: 9

f.baz = lambda val: val * val
print(f.garply())
# prints: 16
```
