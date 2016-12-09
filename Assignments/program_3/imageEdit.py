from PIL import Image
import urllib, cStringIO
import random


class ImageEd(object):
    def __init__(self, file):
        self.img = Image.open(file)
        self.width = self.img.size[0]
        self.height = self.img.size[1]


    def glass_effect(self, img = self.img, dist = 5):
        nums = [x for x in range(i-dist, i+dist) if x >=0]
        choice = random.choice(nums)
        for x in range(dist, self.width-dist):
            for y in range(dist, self.height-dist):
                img.getpixel((x,y))
                img.putpixel((x+choice,y+choice))
    
                
    def flip(self, img = self.img):
        for y in range(self.height):
            for x in range(self.width):
                img.getpixel((x,y))
                img.putpixel((self.width - x, y))
        return img
                

    def blur(self, img = self.img, blur_power = 3):
        r = 0
        g = 0
        b = 0
        d = 2*blur_power * 2*blur_power
        for x in range(blur_power, self.width-blur_power):
            for y in range(blur_power, self.height-blur_power):
                for i in range(-blur_power, blur_power):
                    for j in range(-blur_power, blur_power):
                        pix = img.getpixel((x+i, y+j))
                        r += pix[0]
                        g += pix[1]
                        b += pix[2]
                img.putpixel((x,y), (int(r/d), int(g/d), int(b/d)))
                r = 0
                g = 0
                b = 0
        return img
                        
        
        

    def posterize(self, img = self.img, snap_val = 51):
        snap = snap_val // 2
        for x in range(self.width):
            for y in range(self.height):
                rgb = img.getpixel((x,y))
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

                img.putpixel((x,y), rgb)
        return img



    def solarize(self, img = self.img, thresh = 125):
        for x in range(self.width):
            for y in range(self.height):
                rgb = img.getpixel((x,y))
                r = rgb[0]
                g = rgb[1]
                b = rgb[2]
                
                if r < thresh:
                    r = thresh - r
                else:
                    r = r + thresh
                    
                if g < thresh:
                    g = thresh - g
                else:
                    g = g + thresh

                if b < thresh:
                    b = thresh - b
                else:
                    b = b + thresh                                        
                
                img.putpixel((x,y), rgb)

        return img

                
               

    def warhol(self, img = self.img, snap_val = 51):
        num = int(255//snap_val)
        intervals = []
        for i in num:
            intervals.append(0+snap_val*i)
        color = [(0,0,0),(85,85,85),(0,255,0),(255,0,0),(0,0,255),(255,255,255)]
        for x in range(self.width):
            for y in range(self.height):
                rgb = img.getpixel((x,y))
                gray = int((rgb[0]+rgb[1]+rgb[2])/3)
                imgcopy = img.putpixel((x,y), rgb)
                imgcopy2 = posterize(imgcopy, snap_val)
                rgb2 = imgcopy2.getpixel((x,y))
                for j in intervals:
                    if rgb2 <= intervals[j]:
                        rgb2 = color[j]
                        imgcopy2.putpixel((x,y), rgb2)
                        break    
        return imgcopy2



