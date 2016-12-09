#Micah Cooke
#2143 OOP
#12/9/2016
#Program 3 
#imageEdit.py code


from PIL import Image
import urllib, cStringIO
import random

#@ClassName: ImageEd
#@Inheritance: Object
class ImageEd(object):
    #@Name: __init__
    #@Parameters: self, file
    #@Description: Constructor that opens a file and saves
    #   it in self.img, then sets the width and height
    #@Return: None
    def __init__(self, file = None):
        self.img = Image.open(file)
        self.width = self.img.size[0]
        self.height = self.img.size[1]

    #@Name: glass_effect
    #@Parameters: self, image, distance value
    #@Description: This uses for loops starting away from the edges
    #   by the distance value to work with each individual pixel. Then 
    #   the pixel is switched with a random neighbor.
    #@Return: self.img
    def glass_effect(self, img = None, dist = 5):
        nums = [x for x in range(0-dist, 0+dist) if x >=0]
        for x in range(dist, self.width-dist):
            for y in range(dist, self.height-dist):
                choice = random.choice(nums)
                rgb = self.img.getpixel((x,y))
                self.img.putpixel((x+choice,y+choice))
        return self.img
    
    #@Name: flip
    #@Parameters: self, image
    #@Description: Nested for loop with half the width allow us to
    #   exchange a pixel's position with another pixel further down
    #   the row. 
    #Return: self.img
    def flip(self, img = None):
        for y in range(self.height):
            for x in range(self.width//2):
                rgb = self.img.getpixel((x,y))
                self.img.putpixel((self.width - x, y))
        return self.img
                
    #@Name: blur
    #@Parameters: self, image, blur_power value
    #@Description: This is the example code we used in class.
    #   Multiple for loops are inefficient, but it works :)
    #Return: self.img
    def blur(self, img = None, blur_power = 3):
        r = 0
        g = 0
        b = 0
        d = 2*blur_power * 2*blur_power
        for x in range(blur_power, self.width-blur_power):
            for y in range(blur_power, self.height-blur_power):
                for i in range(-blur_power, blur_power):
                    for j in range(-blur_power, blur_power):
                        pix = self.img.getpixel((x+i, y+j))
                        r += pix[0]
                        g += pix[1]
                        b += pix[2]
                self.img.putpixel((x,y), (int(r/d), int(g/d), int(b/d)))
                r = 0
                g = 0
                b = 0
        return self.img
                        
        
        
    #@Name: posterize
    #@Parameters: self, image, snap_val
    #@Description: Nested for loop give access to each pixel.
    #   If the module of each rgb value and half the snap_val is
    #   less than snap, then we subract, otherwise we add.
    #Return: self.img
    def posterize(self, img = None, snap_val = 150):
        snap = snap_val // 2
        for x in range(self.width):
            for y in range(self.height):
                rgb = self.img.getpixel((x,y))
                r = rgb[0]
                g = rgb[1]
                b = rgb[2]

                if (r%snap) < snap:
                    r -= r%snap
                else:
                    r += (snap_val - snap)
                
                if (g%snap) < snap:
                    g -= g%snap
                else:
                    g += (snap_val - snap) 

                if (b%snap) < snap:
                    b -= b%snap
                else:
                    b += (snap_val - snap)

                self.img.putpixel((x,y), (r,g,b))
        return self.img


    #@Name: solarize
    #@Parameters: self, image, thresh
    #@Description: Nested for loop give access to each pixel. For each
    #   rbg value, if it is less than the thresh then we subtract our value 
    #   from thresh, otherwise we add thresh to our value
    #Return: self.img
    def solarize(self, img = None, thresh = 125):
        for x in range(self.width):
            for y in range(self.height):
                rgb = self.img.getpixel((x,y))
                r = rgb[0]
                g = rgb[1]
                b = rgb[2]
                
                if r < thresh:
                    r -= thresh
                else:
                    r += thresh
                    
                if g < thresh:
                    g -= thresh
                else:
                    g += thresh

                if b < thresh:
                    b -= thresh
                else:
                    b += thresh                                        
                
                self.img.putpixel((x,y), rgb)

        return self.img

                
               
    #@Name: warhol
    #@Parameters: self, image, snap_val
    #@Description: Num determines how many intervals we have. Intervals
    #   creates a list of the boundaries for each interval. Colors is a 
    #   list of random colors. Nested for loops give us access to each 
    #   individual pixel, which we grayscale then posterize. Then a for 
    #   loop allows us to figure out which interval the new value of the 
    #   pixel belongs to, then we assign it a new color.
    #Return: imgcopy2
    def warhol(self, img = None, snap_val = 51):
        num = int(255//snap_val)
        intervals = []
        for i in num:
            intervals.append(0+snap_val*i)
        color = [(0,0,0),(85,85,85),(0,255,0),(255,0,0),(0,0,255),(255,255,255)]
        for x in range(self.width):
            for y in range(self.height):
                rgb = self.img.getpixel((x,y))
                gray = int((rgb[0]+rgb[1]+rgb[2])/3)
                imgcopy = self.img.putpixel((x,y), rgb)
                imgcopy2 = posterize(imgcopy, snap_val)
                rgb2 = imgcopy2.getpixel((x,y))
                for j in intervals:
                    if rgb2 <= intervals[j]:
                        rgb2 = color[j]
                        imgcopy2.putpixel((x,y), rgb2)
                        break    
        return imgcopy2
