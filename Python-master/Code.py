#!/bin/python3

import os
import re

def get_files():
    files = os.listdir(os.getcwd())
    py_list=[]
    for f in files:
        if f.split('.')[-1] == 'py':
            print("This py is:",f)
            py_list.append(f)
    return py_list

def count(files):
    code_line,blank,comments = 0,0,0
    for fname in files:
        f = open(fname,'r')
        for line in f:
            code_line += 1
            if line == '/n':
                blank += 1
            if re.search(r'#',line):
                comments +=1
        f.close()
    return [code_line,blank,comments]

if __name__ == '__main__' :
    files = get_files()
    lines = count(files)
    print("Alright,the result is; %d ,blank: %d, comments: %d" % (lines[0],lines[1],lines[2]))