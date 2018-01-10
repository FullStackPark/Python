#!/bin/python3

from bs4 import BeautifulSoup
import requests

def get_html():
    r = 'https://www.toutiao.com/a6506644387580084750/'
    headers = {'user-agent':
               'Mozilla/5.0 (Windows NT 6.1 Win64: x64) AppleWebKit/537.36     \
               (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'      }
    url = requests.get(r,headers=headers)
    soup = BeautifulSoup(url.text,'lxml')
    [script.extract() for script in soup.findAll('script')]
    [style.extract() for style in soup.findAll('script')]

    return soup.get_text()

if __name__ == '__main__' :
         print(get_html())