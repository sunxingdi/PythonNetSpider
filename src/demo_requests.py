#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys,os
import time
import requests
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

def requests_demo():
    time.sleep(2)#模拟人工操作
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }

    res = requests.get('http://cd.58.com/', headers = headers)#get方法加入请求头

    #soup = BeautifulSoup(res.text,'html.parser')#对返回的结果进行解析
    soup = BeautifulSoup(res.text, 'lxml')  #对返回的结果进行解析

    #moto = soup.select('body > div.article > div.mainWrap > div.leftSide > div.colWrap > div.fl.cbp2.cbhg > div > em > a')#定位元素位置并通过selector方法提取

    moto = soup.select(
        'body > div.article > div > div > div > div > div > div > em > a')  # 定位元素位置并通过selector方法提取

    #print(res)#打印网页响应值
    #print(res.text)#打印解析前的网页内容
    #print(soup.prettify())#打印解析后的网页内容

    for i in range(0,len(moto)):
        print(moto[i].get_text())#通过get_text()方法获取文字信息

def main():
    requests_demo()

if __name__ == '__main__':
    main()
