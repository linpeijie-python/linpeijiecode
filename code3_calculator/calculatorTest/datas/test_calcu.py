#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/22 19:29
# @Author  : Mark
# @File    : test_calcu.py
# @Software: PyCharm
import pytest
import allure
from code3_calculator.calculatorCode.calculator import Calculator

"""
文件名：以test_开头_   (test_*.py)
类名：以Test开头
方法名：以test_开头
"""


class TestCalc:
    def setup(self):
        print("开始计算")
        self.calcu=Calculator()

    def teardown(self):
        print("结束计算")
    @pytest.mark.parametrize("a,b,expected", [
        (1,1,2),
        (-1,-1,-2),
        (0,0,0)
    ],ids=["整数","负数","零"])
    @allure.story("加法用例")
    def test_add1(self,a,b,expected):
        result = self.calcu.add(a,b)
        assert result == expected
    @pytest.mark.add
    def test_sub(self):
        #calc = Calculator()
        result = self.calcu.sub(1,3)
        assert result == 4
    def test_add3(self):
        #calc = Calculator()
        result = self.calcu.sub(6,3)
        assert result == 3
    def test_sub(self):
        #calc=Calculator()
        result = self.calcu.sub(6,4)
        b=self.calcu.div(9,3)
        assert result ==2
        assert b==3

    def test_func(self):
        print("test")