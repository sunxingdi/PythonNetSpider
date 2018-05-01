#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys,os
import time
import json
import requests
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}

#存放数据
list_dict_RstData=[]
json_RstData= os.path.split(os.path.realpath(__file__))[0] + '\RstData.json'

'''
获取脚本绝对路径（包含脚本名）：os.path.realpath(__file__)
获取脚本绝对目录：os.path.split(os.path.realpath(__file__))[0]
'''

def get_links(url,num):

    wb_data = requests.get(url, headers = headers)#get方法加入请求头
    print(wb_data)#打印网页响应值

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
    PageCountMax = 2#页数
    HouseCountMax = 36#每页中获取的租房数据个数
    urls=['http://cd.58.com/pixian/zufang/pn{}/'.format(PageNum) for PageNum in range(1,PageCountMax)]
    print(urls)
    for single_url in urls:
        get_links(single_url,HouseCountMax)
        time.sleep(3)

    #print list_dict_RstData

    json_data = json.dumps(list_dict_RstData).decode('unicode-escape')#解决字典打印中文乱码问题
    print(json_data)

    f_json_RstData=open(json_RstData,'w')
    f_json_RstData.write(json_data)
    f_json_RstData.close()

if __name__ == '__main__':
    main()
