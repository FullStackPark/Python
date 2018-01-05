#!/bin/python

from PIL import Image,ImageDraw,ImageFilter,ImageFont
import random

def randomChar():
    if random.randint(0,1)==0 :
        return(chr(random.randint(65,90)))
    else:
        return chr(random.randint(97,122))
def randomBlackgroundColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
def randomWordColor():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

def createImage():
    im = Image.new('RGB',(240,60),(255,255,255))
    font = ImageFont.truetype('./simhei.ttf',40)
    draw = ImageDraw.Draw(im)
    for x in range(240):
        for y in range(60):
            draw.point((x,y),randomBlackgroundColor())
    words =' '
    for i in range(4):
        word = randomChar()
        draw.text((50*i+random.randint(10,40),random.randint(0,20)),word,font=font,fill=randomWordColor())
        words += word

    img = im.filter(ImageFilter.BLUR)
    im.save('result.png')
    print(words)
if __name__ == '__main__':
     createImage()