# ithomeUserWall
A Python crawling program to generate a picture wall

## Dependency ##

### Beautiful Soup ###
[Installation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)

### Pillow ###
[Installation](https://pillow.readthedocs.io/en/latest/installation.html)

### Face Recognition ###
[Installation](https://github.com/ageitgey/face_recognition#installation)

## Step 1 ##
Run [job.sh](https://github.com/nerocui/ithomeUserWall/blob/master/job.sh), which is linked to [ithome.py](https://github.com/nerocui/ithomeUserWall/blob/master/ithome.py), with `./job.sh`
This will download all the pics into the `img` folder

## Step 2 ##
Run [photo.sh](https://github.com/nerocui/ithomeUserWall/blob/master/photo.sh), which is linked to [face.py](https://github.com/nerocui/ithomeUserWall/blob/master/face.py), with `./photo.sh`
This will get all the pics with at least 1 face to be moved to the `faces` folder

## Step 3 ##
Run [coll.sh](https://github.com/nerocui/ithomeUserWall/blob/master/coll.sh), which is linked to [li.py](https://github.com/nerocui/ithomeUserWall/blob/master/li.py), with `./coll.sh`
This will generate the final photo wall with the name `soobin64.png`

![alt text](https://github.com/nerocui/ithomeUserWall/blob/master/soobin64.png)
