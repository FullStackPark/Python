#1/usr/bin/python3
from  sys import  argv

scripts,Input = argv

def getFilterwords():
    filterwords = []
    f=open('filterwords.txt')
    for word in f:
        filterwords.append(word[:-1])
    f.close()
    return filterwords

def checkFilterwords(filtWord,Input):
    for w in filtWord:
        if w == Input:
            print('Freedom')
            return
    print('Human Rights')
    return

if __name__ == '__main__':
    checkFilterwords(getFilterwords(),Input)