#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys,os
import time
import requests
from bs4 import BeautifulSoup
import pymongo


reload(sys)
sys.setdefaultencoding('utf-8')

def mongo_demo():
    client = pymongo.MongoClient('localhost', 27017)  # 连接数据库
    mydb = client['mydb']
    test = mydb['test']
    test.col.insert_one({'name': 'Jan', 'sex': '男', 'grade': 89})  # 插入数据

def main():
    mongo_demo()

if __name__ == '__main__':
    main()
