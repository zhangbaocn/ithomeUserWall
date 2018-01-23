import os
import PIL.Image as Image
from os import listdir
import math

imgList=os.listdir('faces/')
numImages=len(imgList)
print('I got ',numImages,'image(s)')

import math
eachSize=64
eachLine=int(math.sqrt(numImages))+1
print("singular image width",eachSize,"pixel, 1 line",eachLine,"final length",eachSize*eachLine)

import PIL.Image as Image
toImage = Image.new('RGBA', (eachSize*eachLine,eachSize*eachLine))
x = 0
y = 0

os.chdir('faces/')
for i in imgList:
    """
    try:
        img = Image.open(i)
    except IOError:
        print("Error: fail to read file",i)
    else:
        """
    img = Image.open(i)
    img = img.resize((eachSize, eachSize), Image.ANTIALIAS)
    toImage.paste(img, (x * eachSize, y * eachSize))
    x += 1
    if x == eachLine:
        x = 0
        y += 1
print("done coll")

os.chdir(os.path.pardir)
os.getcwd()

toImage.save("soobin"+str(eachSize)+".png")