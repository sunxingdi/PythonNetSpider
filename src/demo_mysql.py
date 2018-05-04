#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys,os
import time
import requests
from bs4 import BeautifulSoup
import pymongo
import pymysql


reload(sys)
sys.setdefaultencoding('utf-8')

def mysql_demo():
    conn = pymysql.connect(host='localhost', user=r'root', passwd=r'root',db='mydatabase')  # 连接数据库
    print conn
    #cursor = conn.cursor()

    # 关闭游标
    #cursor.close()
    # 关闭连接
    conn.close()

def main():
    mysql_demo()

if __name__ == '__main__':
    main()
