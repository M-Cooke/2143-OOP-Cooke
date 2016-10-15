##Micah Cooke


### Questions

**1)** What does Python print for each of the following:

```python 
johns_bag = Bag()
johns_bag.print_bag()
# what prints?

for color in [’blue’, ’red’, ’green’, ’red’]:
    johns_bag.add_skittle(Skittle(color))
johns_bag.print_bag()
# what prints?

s = johns_bag.take_skittle()
print(s.color)
# what prints?

print(johns_bag.number_sold)
# what prints?

print(Bag.number_sold)
# what prints?

soumyas_bag = Bag()
soumyas_bag.print_bag()

print(johns_bag.print_bag())
# what prints?

print(Bag.number_sold)
# what prints?

print(soumyas_bag.number_sold)
# what prints?
```

### Answer 1

```python
# What prints #1:
[]
# What prints #2:
['blue','red','green','red']
# What prints #3:
blue
# What prints #4:
1
# What prints #5:
1
# What prints #6:
[]
['red','green','red']
# What prints #7:
2
# What prints #8:
2

```

**2)**  Write a new method for the Bag class called take color, which takes a color and
removes (and returns) a Skittle of that color from the bag. If there is no Skittle
of that color, then it returns `None`.

```python
def take_color(self, color):






```


### Answer 2

```python
def take_color(self, color):
    for i in range(len(self.skittles)):
        take_skittle = self.skittles[i].color
        if take_skittle == color:
            return self.skittles.pop(i)
        else:
            return None

```

**3.** Write a new method for the Bag class called take all, which takes all the Skittles
in the current bag and prints the color of the each Skittle taken from the bag.

```python
def take_all(self):




```

### Answer 3

```python
def take_all(self):
    for i in range(len(self.skittles)):
        print(self.take_skittle().color)

```
