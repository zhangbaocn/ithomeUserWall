import face_recognition
import os
from os import listdir
import shutil
import math

image = face_recognition.load_image_file('52678.jpg')
face_locations = face_recognition.face_locations(image)

print len(face_locations)

"""
imgList=os.listdir('img/')
numImages=len(imgList)
print('I got ',numImages,'image(s)')

path = os.getcwd()+'/img/'
moveto = os.getcwd()+'/faces/'
count = 0
ct = 0
os.chdir("img/")
for i in imgList:
	image = face_recognition.load_image_file(i)
	face_locations = face_recognition.face_locations(image)
	ct += 1
	if(len(face_locations)>0):
		#src = path+i
		#dst = moveto+i
		count += 1
		#shutil.move(src,dst)
		#print(src)
		#print(dst)
		print count


print ct

"""