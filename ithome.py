from bs4 import BeautifulSoup
import urllib
import os
from PIL import Image
from os import listdir
import math
import thread
import shutil
import requests
import csv



thread_base_url = 'https://quan.ithome.com/thread/'
image_url_list = []
all_threads_url = []
all_user = []



def getAllThreadUrl(num1, num2):

	for i in range(num1, num2+1):
		#open a url/page
		#find all div with the thread url
		curr_thread_url = thread_base_url+str(i)+'/'
		curr_thread_page = urllib.urlopen(curr_thread_url).read()
		curr_thread_soup = BeautifulSoup(curr_thread_page,"html.parser")
		t_post = curr_thread_soup.find_all("a", class_="t_cate_title")
		#
		
		for t_a in t_post:
			if t_a == None:
				continue
			all_threads_url.append(t_a['href'])
	return



def getAllUserInThread(url):
	new_url = "https://quan.ithome.com"+url
	curr_thread_page = urllib.urlopen(new_url).read()
	curr_thread_soup = BeautifulSoup(curr_thread_page,"html.parser")
	t_post = curr_thread_soup.find_all("div", class_="comm_con")
	for div in t_post:
		addToUser(div.a['href'])
	return

def addToUser(user):
	curr_u = user[6:len(user)-1]
	#[6:13]
	if curr_u in all_user:
		return
	all_user.append(curr_u)
	print("added "+str(curr_u))
	return

def getAllUserID(num1, num2):
	getAllThreadUrl(num1, num2)
	for uri in all_threads_url:
		getAllUserInThread(uri)
	with open("User.csv",'wb') as resultFile:
		wr = csv.writer(resultFile, dialect='excel')
		wr.writerow(all_user)
	getAllUserPhotos()
	return

def getAllUserPhotos():
	os.chdir("img/")
	for user_id in all_user:
		user_page_url = "https://quan.ithome.com/user/"+str(user_id)

		user_page = urllib.urlopen(user_page_url).read()
		user_soup = BeautifulSoup(user_page, "html.parser")
		div = user_soup.find("img", class_="t_head")
		name_tag = user_soup.find("div", class_="nick")
		name = name_tag.contents
		source=div['src']
		url = "http:"+source
		response = requests.get(url, stream=True)
		with open(str(user_id)+'.jpg', 'wb') as out_file:
    			shutil.copyfileobj(response.raw, out_file)
		del response
		print("got "+str(user_id)+"'s photo")
	return



try:
   thread.start_new_thread( getAllUserID, (1, 4) )
   thread.start_new_thread( getAllUserID, (5, 8) )
   thread.start_new_thread( getAllUserID, (9, 12) )
   thread.start_new_thread( getAllUserID, (13, 16) )
except:
   print "Error: unable to start thread"
while 1:
   pass