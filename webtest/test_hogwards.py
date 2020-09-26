#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 21:34
# @Author  : Mark
# @File    : test_hogwards.py
# @Software: PyCharm
from time import sleep

from selenium import webdriver

class TestHogwards():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        sleep(3)
        self.driver.quit()

    def test_hogwards(self):
        self.driver.get("http://www.testerhome.com")
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_link_text("求职面试圈").click()
