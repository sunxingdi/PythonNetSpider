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
    'Referer':'http://www.mzitu.com/xinggan/'
}

#存放数据
global download_links
download_links = [] #初始化列表，存入图片urls
save_path = r'C:\\Users\\xxxxxx\\Desktop\\pySpiderResult\\photo\\'

PageCountMax = 10  # 页数
PhotoCountMax = 2  # 每页中获取数据个数

'''
获取脚本绝对路径（包含脚本名）：os.path.realpath(__file__)
获取脚本绝对目录：os.path.split(os.path.realpath(__file__))[0]
'''

def get_links(url,num=PhotoCountMax):

    wb_data = requests.get(url, headers = headers)#get方法加入请求头
    #print(wb_data)#打印网页响应值

    soup = BeautifulSoup(wb_data.text, 'lxml')  #对返回的结果进行解析
    imgs = soup.select('#pins > li > a > img')

    for img in imgs:
        print(img.get('data-original'))
        global download_links
        download_links.append(img.get('data-original'))

def get_photo(url):
    photo_data = requests.get(url, headers=headers)
    fp = open(save_path + url[-20:],'wb')
    fp.write(photo_data.content)  # 把图片内容写入文件
    fp.close()  # 关闭文件

def main():

    urls=['http://www.mzitu.com/xinggan/page/{}/'.format(PageNum) for PageNum in range(1,PageCountMax)]
    #print(urls)

    for single_url in urls:
        get_links(single_url)
        time.sleep(1)

    print download_links

    for single_link in download_links:
        get_photo(single_link)
        time.sleep(1)

if __name__ == '__main__':
    main()
