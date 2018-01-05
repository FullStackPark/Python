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
        wlen=len(w)
        slen=len(Input)
        Input = list(Input)
        if slen == wlen and w == "".join(Input):
            print('*'*wlen)
            return
        elif slen >wlen:
            for i in range(slen):
                if w == "".join(Input[i:i+wlen]):
                    j=i
                    while (wlen):
                        Input[j]='*'
                        j+=1
                        wlen-=1
    print("".join(Input))
    return


if __name__ == '__main__':
    checkFilterwords(getFilterwords(), Input)
