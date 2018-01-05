#!/bin/python3

import xlwt

def get_text():
    with open('student.txt',encoding='gbk') as f:
        str_temp=f.read()
        data = eval(str_temp)
    return data

def create_xls(dic):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Student')

    row = 0
    for k,v in dic.items():
        ws.write(row,0,k)
        col = 1
        for items in v:
            ws.write(row,col,items)
            col += 1
        row += 1
    wb.save('student.xls')

if __name__ == '__main__':

     create_xls(get_text())