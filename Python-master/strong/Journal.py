#!/bin/python3

import re,os
from collections import Counter

file_path = 'C:\\Users\\Administrator\\Documents\\GitHub\\Python\\Python-master\\strong'
filter_word = ['the','in','of','to','has','that','is','are','a','with','as','an']

def getCounter(filesource):
    wordC = r'''[A-Za-z]+|$\d+%?$'''
    with open(filesource) as f:
        result = re.findall(wordC,f.read())
        return Counter(result)

def run(file_path):
    os.chdir(file_path)
    counter_all = Counter()
    for i in os.listdir(os.getcwd()):
        if os.path.splitext(i)[1] == '.txt':
            counter_all += getCounter(i)
    for j in filter_word :
        counter_all[j]=0
    print (counter_all.most_common()[0][0])

if __name__ == '__main__':
    run(file_path)