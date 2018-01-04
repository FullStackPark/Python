#!/bin/python3

from PIL import Image,ImageDraw,ImageFont


def add_number(img):
     draw = ImageDraw.Draw(img)
     myfont=ImageFont.truetype("C:\\Users\\Administrator\\Desktop\\Python-master\\simhei.ttf",80)
     fillcolor ="#00ff00"
     width,height = img.size
     draw.text((width-50,10),'V',font = myfont, fill = fillcolor)
     img.save('result.jpg','jpeg')

if __name__ == '__main__':
     image = Image.open("C:\\Users\\Administrator\\Desktop\\Python-master\\text.jpg")
     add_number(image)
