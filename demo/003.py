#!/bin/pyhton3

import random
import pymysql
def create_db_table():        #创建数据库 表格,TESTDB需要提前创建
    db = pymysql.connect("localhost","root","12345","TESTDB")
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS KEY_CODE")
    sql = """CREATE TABLE KEY_CODE(\
            KEY_ID INT,
            KEY_VALUE CHAR(30)
            )"""
    cursor.execute(sql)
    db.close()

def make_insert():

    new_list=create_list()
    db = pymysql.connect("localhost","root","12345","TESTDB")
    cursor=db.cursor()
    for i in range(200):
        key_value = gen_code(new_list)
        sql = "INSERT INTO KEY_CODE(KEY_ID,\
        KEY_VALUE)\
        VALUES('%d','%s')" % (i,key_value)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

    db.close()

if __name__=='__main__':
    create_db_table()
    make_insert()