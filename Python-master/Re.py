#!/bin/python3

import re
def get_word_frequencies(file_name):
    dic = {}
    txt = open(file_name, 'r').read().splitlines()
    no_flag=0
    for line in txt:
        line = re.sub(r'[.?!,""/\W]', ' ', line)
        for word in line.split():

            if word.isdigit():
                    pass

            else:
                 dic.setdefault(word.lower(), 0)
                 dic[word.lower()] += 1
    print (dic)

if __name__ == '__main__':
        get_word_frequencies("WhatisPython.txt")