from PIL import Image


class ImageEd(object):
  def __init__(self):
    pass
  
  def glass_effect(self):
    pass
  
  def flip(self):
    pass
  
  def blur(self, img, blur_power = 5):
    width = img.size[0]
    height = img.size[1]
    
    r = 0
    g = 0
    b = 0 
    d = 2*blur_power * 2*blur_power
    for x in range(blur_power, width-blur_power):
      for y in range(blur_power, height-blur_power):
        for i in range(-blur_power, blur_power):
          for j in range(-blur_power, blur_power):
            pix = img.getpixel((x+i, y+j))
            r += pix[0]
            g += pix[1]
            b += pix[2]
        img.putpixel((x,y),(int(r/d), int(g/d), int(b/d)))
        r = 0
        g = 0
        b = 0
  
  def posterize(self):
    pass
  
  def solarize(self, thresh = 3):
    pass
  
  def warhol(self):
    pass
