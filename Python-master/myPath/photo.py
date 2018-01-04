#!/bin/python3

import os,sys
from PIL import Image

def processImage(filesource, destsource, name, imgtype):


    imgtype = 'jpeg' if imgtype == '.jpg' else 'png'

    im = Image.open(filesource + name)

    rate = max(im.size[0]/640.0 if im.size[0] >640 else 0, im.size[1]/1136.0 if im.size[1] >1136 else 0)
    if rate:
        im.thumbnail((im.size[0]/rate, im.size[1]/rate))
    im.save(destsource + name, imgtype)

def run(myPath):

    os.chdir(myPath)
    for i in os.listdir(os.getcwd()):

        postfix = os.path.splitext(i)[1]
        if postfix == '.jpg' or postfix == '.png':
            processImage(myPath, "./new", i, postfix)

if __name__ == '__main__':
    run('./')