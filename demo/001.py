#!/bin/python3

from PIL import Image,ImageDraw,ImageFont

def add_number(img):
     draw = ImageDraw.Draw(img)
     myfont=ImageFont.truetype("C:\\Users\\dell\\Desktop\\Python-master\\Python-master\\Python\\Python\\demo\\simhei.ttf",80)
     fillcolor ="#ccff00"
     width,height = img.size
     draw.text((width-50,10),'X',font = myfont, fill = fillcolor)
     img.save('result.jpg','jpeg')

if __name__ == '__main__':
     image = Image.open("C:\\Users\\dell\\Desktop\\Python-master\\Python-master\\Python\\Python\\demo\\text.jpg")
     add_number(image)
