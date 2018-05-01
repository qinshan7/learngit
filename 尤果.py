import urllib
from urllib import request
import re
import os

p = os.getcwd()
try:
    os.makedirs( r'%s\Female'%p )
except:
    pass
os.chdir('%s\Female'%p)
y = 170

def getImg(html):
    a = "http://img.ugirls.tv/uploads/magazine/content/\w*.jpg"
    imgre = re.compile(a)
    imglist = re.findall(imgre,html)
    return imglist

if __name__ == '__main__':

    urls =[]
    baseurl = 'http://www.ugirls.com/Content/List/Magazine-%s.html'

    for i in range(y,200):
        pn = i
        urls.append(baseurl%i)

    for url in urls:
        try:
            rsp = request.urlopen(url)
            html = rsp.read().decode("utf-8")
            x = 1
            for imgurl in getImg(html):
                #保存到本地
                urllib.request.urlretrieve(imgurl, '%s-%s.jpg' %(y,x))
                x += 1
            y += 1
        except:
            pass
