#!/bin/python3

import random

def create_list():
    base = []
    for x in range(65,91):
        a=str(chr(x))
        base.append(a)
    for x in range(97,123):
        a=str(chr(x))
        base.append(a)
    for x in range(10):
        base.append(str(x))
    return base

def gen_code(base):
    s=''
    for x in range(16):
        a=random.choice(base)
        s=s+a
    print(s)
    return (s)

def create_txt(newlist):
    strlist="".join(newlist)
    txtnew=open("problem0001.txt","w")
    txtnew.write(strlist)
    txtnew.close()

if __name__ == '__main__':

    store_list = ['']
    new_list   = create_list()

    for x in range(200):
        store_list.append(gen_code(new_list))
        store_list.append('\n')
    create_txt(store_list)