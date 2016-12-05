from PIL import Image
import urllib, cStringIO
import random


class ImageEd(object):
    def __init__(self, file):
        self.img = Image.open(file)
        self.width = self.img.size[0]
        self.height = self.img.size[1]

    def glass_effect(self, img, dist = 5):
        nums = [x for x in range(i-dist, i+dist) if x >=0]
        choice = random.choice(nums)
        for x in range(dist, self.width-dist):
            for y in range(-dist, self.height-dist):
                for i in range(-dist, dist):
                    for j in range(-dist, dist):
                        pix = img.getpixel((x+i, y+j))
                        r = choice[0]
                        g = choice[1]
                        b = choice[2]
                img.putpixel((x,y),(r,g,b))

        #img.save('glasspic.jpg')
                
    def flip(self, img):
        for x in self.width:
            for y in self.height:
                opp = self.height - y
                y = opp

    def blur(self, img, blur_power = 3):
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
                        
        #img.save('blurpic.jpg')
        )

    def posterize(self, img):
        for p in getPixels(img):
            r = getRed(p)
            g = getGreen(p)
            b = getBlue(p)

            if(r < 64):
                setRed(p,31)
            elif(r < 128):
                setRed(p,95)
            elif(r < 192):
                setRed(p,159)
            elif(r < 256):
                setRed(p,223)

            if(g < 64):
                setGreen(p,31)
            elif(g < 128):
                setGreen(p,95)
            elif(g < 192):
                setGreen(p,159)
            elif(g < 256):
                setGreen(p,223)            

            if(b < 64):
                setBlue(p,31)
            elif(b < 128):
                setBlue(p,95)
            elif(b < 192):
                setBlue(p,159)
            elif(b < 256):
                setBlue(p,223)

    def solarize(self, img):
        for p in getPixels(img):
            setRed(p,255-getRed(p))
            setGreen(p,255-getGreen(p))
            setBlue(p,255-getBlue(p))       

    def warhol(self):
        pass


