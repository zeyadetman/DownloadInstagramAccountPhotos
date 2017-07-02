from bs4 import BeautifulSoup
import requests
import os
import urllib.request

imgslin = []
linksimg = []

def creat(fil):
    c = 0
    #you can change the path of file
    fw = open('ffffff.txt','r') 
    ss = fw.read()
    imgs = ss.split("src=")
    for i in range(len(imgs)):
        if (i % 1 is 0) and (i is not 0):
            imgslin.append(imgs[i].split('"'))
    fw.close()
    for i in range(len(imgslin)):
        linksimg.append(imgslin[i][1])
    return linksimg

sss = creat('ffffff.txt')
c = int(0)
for link in sss:
    #you can change the path of download folder
    urllib.request.urlretrieve(link, str(c)+".jpg")
    c += 1
