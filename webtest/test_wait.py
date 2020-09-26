#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/20 0:11
# @Author  : Mark
# @File    : test_wait.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://baidu.com/")
    def test_wait(self):
        #self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys("霍格沃兹测试学院")
        #self.driver.find_element(By.ID,"kw").send_keys("霍格沃兹")
        self.driver.find_element(By.CSS_SELECTOR, "#kw").send_keys("霍格")
        self.driver.find_element(By.ID, "su").click()