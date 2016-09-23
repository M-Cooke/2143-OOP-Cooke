
"""
Micah Cooke
micahcooke75@gmail.com
Homework 2- Fractions
26 Sep @ 1p.m.
"""
class fraction(object):
    def __init__(self,n=None,d=None):
        self.num = n
        self.den = d

    def __str__(self):
    	return (' %d %d/%d' % (self.num//self.den, self.num%self.den, self.den))

    def numerator(self,n):
        self.num = n 

    def denominator(self,d):
        self.den = d

    def __mul__(self,rhs):
        x = self.num * rhs.num
        y = self.den * rhs.denr
        return fraction(x,y)

    def __add__(self,rhs):
        x = (self.num * rhs.den) + (rhs.num * self.den)
        y = (self.den * rhs.den)
        return fraction(x,y)
        
   

if __name__ == '__main__':
	a = fraction(1,2)
	b = fraction(4,5)
	c = a + b
	print(c)
