#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/3 23:54
# @Author  : Mark
# @File    : appui01.py
# @Software: PyCharm
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time

from appium import webdriver

caps = {
    "platformName": "Android",
    #"platformVersion": "6.0"
    "deviceName": "127.0.0.1:7555",
    "appPackage": "com.xueqiu.android",
    "appActivity": ".common.MainActivity",
    "noReset": "true",
    "dontStopAppOnReset": "true",
    "shipDeviceInitialization": "true",
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)
el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el1.click()
el3 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el3.send_keys("alibaba")
el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
el4.click()
el5 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.TextView")
el5.click()
driver.back()
driver.implicitly_wait(2)
driver.back()
time.sleep(2)
driver.quit()