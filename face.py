import face_recognition
import os
from os import listdir
import shutil
import math

imgList=os.listdir('img/')
numImages=len(imgList)
print('I got ',numImages,'image(s)')

path = os.getcwd()+'/img/'
moveto = os.getcwd()+'/faces/'
os.chdir("img/")
for i in imgList:
	image = face_recognition.load_image_file(i)
	face_locations = face_recognition.face_locations(image)
	if(len(face_locations)>0):
		src = path+i
		dst = moveto+i
		shutil.move(src,dst)
