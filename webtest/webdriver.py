#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 21:32
# @Author  : Mark
# @File    : webdriver.py
# @Software: PyCharm
from selenium import webdriver
import time
def main():
    b=webdriver.Chrome()
    #b.get('http://www.baidu.com')
    b.get('https://admin.kuaipitest.com/#/login')
    time.sleep(5)
    #b.quit()
if __name__ == '__main__':
    main()