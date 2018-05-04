#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys,os
import time
import json
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool #导入相应的库文件
#from urllib.request import urlretrieve
#import urlretrieve
from lxml import etree

reload(sys)
sys.setdefaultencoding('utf-8')

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    'Referer':'http://www.91porn.com',
    'Accept-Language':'zh-CN,zh;q=0.9'
}

#存放数据
global list_dict_RstData
list_dict_RstData=[]
json_RstData= os.path.split(os.path.realpath(__file__))[0] + '\RstData_91.json'

PageCountMax = 20  # 页数
PhotoCountMax = 2  # 每页中获取数据个数

'''
获取脚本绝对路径（包含脚本名）：os.path.realpath(__file__)
获取脚本绝对目录：os.path.split(os.path.realpath(__file__))[0]
'''

def get_links(url,num=20):

    wb_data = requests.get(url, headers = headers)#get方法加入请求头
    #print(wb_data)#打印网页响应值
    #print wb_data.text
    soup = BeautifulSoup(wb_data.text, 'lxml')  #对返回的结果进行解析
    #print soup

    Contents = soup.select('#videobox > table  > tr > td > div.listchannel > a')

    for Content in Contents:
        #print Content
        dict_data = {
            'title': Content.get('title'),
            'href': Content.get('href')
         }
        print dict_data['title'],dict_data['href']

        global list_dict_RstData
        list_dict_RstData.append(dict_data)

def main():

    urls=['http://www.91porn.com/v.php?next=watch&page={}'.format(PageNum) for PageNum in range(1,PageCountMax)]
    #print(urls)

    for single_url in urls:
        get_links(single_url)
        time.sleep(2)

    #print list_dict_RstData

if __name__ == '__main__':
    main()
