#!/bin/python3

import re
import urllib
import requests


def get_html():
    response = requests.get("http://tieba.baidu.com/p/2166231880")
    new_f = open("te.html",'w')
    new_f.write(response.text)
    new_f.close()

    return response.text

def down_png(picHtml):
    image = re.compile(r'src="(.+?\.jpg)" pic_ext')
    imagelist = re.findall(image,picHtml)
    x = 0
    for imgurl in imagelist:
        urllib.request.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1

if __name__ == '__main__':
    down_png(get_html())