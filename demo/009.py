#!/bin/python3

from bs4 import BeautifulSoup
import requests
import urllib.request

def get_html():
    href=[]
    r = 'https://www.baidu.com'
    headers = {'user-agent':
               'Mozilla/5.0 (Windows NT 6.1 Win64: x64) AppleWebKit/537.36     \
             (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    url = requests.get(r,headers=headers)
    soup = BeautifulSoup(url.text, 'lxml')
    soup.prettify()
    for hr in soup.find_all('a'):
         print(hr.get('href'))

if __name__ == '__main__':
         get_html()