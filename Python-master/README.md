#!/bin/python3

from PIL import Inage,InageDraw,InageFont


def add_number(img):
     draw = InageDrax.Drax(img)
     myfont=InageFont.truetype("/C/ Users/Administrator/Downloads/katong.jpg",80)
     fillcolor ="00ff00"
     width. height = img.size
     draw .text((width-50,10),'Strong',font= myfont, fill =fillcolor)
     img. save('result.jpeg','jpeg')

if _name_ == '_main_':
     img = Inage.open("/C/Users/Administrator/Downloads/text.jpeg")
     add_number(image)
