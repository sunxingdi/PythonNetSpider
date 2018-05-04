#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys,os
import time
import json
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool #导入相应的库文件

reload(sys)
sys.setdefaultencoding('utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}

#存放数据
list_dict_RstData=[]
json_RstData= os.path.split(os.path.realpath(__file__))[0] + '\RstData_MultiProcess.json'

'''
获取脚本绝对路径（包含脚本名）：os.path.realpath(__file__)
获取脚本绝对目录：os.path.split(os.path.realpath(__file__))[0]
'''

def get_links(url,num=36):

    wb_data = requests.get(url, headers = headers)#get方法加入请求头
    #print(wb_data)#打印网页响应值

    soup = BeautifulSoup(wb_data.text, 'lxml')  #对返回的结果进行解析

    for num in range(1, num):
        titles = soup.select(       'body > div.mainbox > div.main > div.content > div.listBox > ul > li:nth-of-type(' + str(num) +') > div.des > h2 > a')  # 定位元素位置并通过selector方法提取
        housetypes = soup.select(   'body > div.mainbox > div.main > div.content > div.listBox > ul > li:nth-of-type(' + str(num) +') > div.des > p.room')
        prices = soup.select(       'body > div.mainbox > div.main > div.content > div.listBox > ul > li:nth-of-type(' + str(num) +') > div.listliright > div.money > b')
        addresses = soup.select(    'body > div.mainbox > div.main > div.content > div.listBox > ul > li:nth-of-type(' + str(num) +') > div.des > p.add > a:nth-of-type(1)')
        villages = soup.select(     'body > div.mainbox > div.main > div.content > div.listBox > ul > li:nth-of-type(' + str(num) +') > div.des > p.add > a:nth-of-type(2)')

        #print(soup.prettify())  # 打印解析后的网页内容

        for title,housetype,price,address,village in zip(titles,housetypes,prices,addresses,villages):
            dict_data={
                'address':address.get_text().strip(),
                'village': village.get_text().strip(),
                'price': price.get_text().strip(),
                'housetype': housetype.get_text().strip().replace(' ', ''),
                'title': title.get_text().strip()  # 通过get_text()方法获取文字信息
            }

            global list_dict_RstData  # global声明
            list_dict_RstData.append(dict_data)

def main():
    PageCountMax = 10#页数
    HouseCountMax = 36#每页中获取的租房数据个数
    urls=['http://cd.58.com/pixian/zufang/pn{}/'.format(PageNum) for PageNum in range(1,PageCountMax)]
    print(urls)
    start_1 = time.time()
    for single_url in urls:
        get_links(single_url)
        time.sleep(3)
    end_1 = time.time()
    print('串行爬虫:', end_1 - start_1)

    start_2 = time.time()
    pool = Pool(processes=2)  # 2个进程
    pool.map(get_links,urls)
    time.sleep(3)
    end_2 = time.time()
    print('两个进程:',end_2 - start_2)

    start_4 = time.time()
    pool = Pool(processes=4)  # 4个进程
    pool.map(get_links,urls)
    time.sleep(3)
    end_4 = time.time()
    print('四个进程:',end_4 - start_4)

    start_8 = time.time()
    pool = Pool(processes=8)  # 8个进程
    pool.map(get_links,urls)
    time.sleep(8)
    end_8 = time.time()
    print('四个进程:',end_8 - start_8)

if __name__ == '__main__':
    main()
