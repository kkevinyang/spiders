# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import urllib2, urllib
import re
from reportlab.pdfgen import canvas
import os

#一些初始化
i = 1
url = 'http://www.yuesir.com/ipu/1504.html'
#获取html
request = urllib2.Request(url)
response = urllib2.urlopen(request)
html = response.read()#.decode('gbk')
# 获取标题
bs = BeautifulSoup(html)
title=bs.find("h2").string.split(' ')[0]# 把后面难看的‘吉他谱’三个字去掉
print title
# 获取url
pattern = re.compile('<img class="page-post-main-content-list-item-img" src="(.*?)".*?')
items = re.findall(pattern,html)
#初始化pdf
c = canvas.Canvas(title+".pdf")
#下载图片并添加到pdf中并保存
for item in items:
    print item
    # 写入图片
    u = urllib.urlopen(item)
    data = u.read()
    name = title + str(i)
    f = open(name, 'wb')
    f.write(data)
    f.close()
    i = i+1
    #写入pdf
    dim=c.drawImage(name,0,0)
    c.setPageSize(dim)
    c.showPage()
    #删除原gif
    os.remove(name)
c.save()


