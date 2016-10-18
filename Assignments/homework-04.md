##Micah Cooke

###Question 1
```
python
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
# prints: 4

print(b.garply())
# prints: 3

b.a = 9
print(b.garply())
# prints: 9

f.baz = lambda val: val * val
print(f.garply())
# prints: 16
```
