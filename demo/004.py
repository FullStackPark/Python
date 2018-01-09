#!bin/python3

import re
def get_word_frequencies(file_name):
    dic = {}
    txt = open(file_name,'r').read().splitlines()
    no_flag = 0
    for line in txt:
        line = re.sub(r'[.?!,""/\W]',' ',line)    #要替换的标点符号,英文字符可能出现的
        for word in line.split():
            #当字符为纯数字的时候,跳过不统计
            if word.isdigit():
                pass
            else:
                dic.setdefault(word.lower(),0)  #不区分大小写
                dic[word.lower()] += 1
    print(dic)
if __name__=='__main__':
    get_word_frequencies("WhatisPyth)on.txt"