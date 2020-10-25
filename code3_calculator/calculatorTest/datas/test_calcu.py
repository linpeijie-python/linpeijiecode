#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/22 19:29
# @Author  : Mark
# @File    : test_calcu.py
# @Software: PyCharm
import pytest
import allure
import os
import sys.
from code3_calculator.calculatorCode.calculator import Calculator

"""
pytest 命名规则
文件名：以test_开头_   (test_*.py)
类名：以Test开头
方法名：以test_开头
识别规则：先识别文件名，再去识别类名，最后是方法名；如果类名不符合，那方法名也不会被识别；
"""





class TestCalc:
    # 类级setup_class.teardown_class（在类中）,只在类中前后运行一次
    def setup_class(self):
        self.calcu = Calculator()
        print("\nsetup_calss在类开始时运行一次")

    def teardown_class(self):
        print("teardown_calss在类结束时运行一次")

    def setup(self):
        print("\n-开始计算-")
        #self.calcu = Calculator()

    def teardown(self):
        print("\n-结束计算-")

    @pytest.mark.parametrize("a,b,expected", [
        (1, 1, 2),
        (-1, -1, -2),
        (0, 0, 0)
    ], ids=["整数", "负数", "零"])
    @allure.story("加法用例")
    def test_add(self, a, b, expected):
        result = self.calcu.add(a, b)
        assert result == expected

    @pytest.mark.parametrize("a,b,expected", [
        (2, 1, 1),
        (-1, -2, 1),
        (0, 0, 0)
    ], ids=["整数", "负数", "1零"])
    @allure.story("减法用例")
    def test_sub(self, a, b, expected):
        result = self.calcu.sub(a, b)
        assert result == expected

    @pytest.mark.parametrize("a,b,expected", [
        (2, 1, 2),
        (-1, -2, 2),
        (0, 0, 0)
    ], ids=["整数", "负数", "1零"])
    @allure.story("乘法用例")
    def test_mul(self,a,b,expected):
        result = self.calcu.mul(a, b)
        assert result == expected

    @pytest.mark.parametrize("a,b,expected", [
        (2, 1, 2),
        (1, 2, 0.5),
        (0.1, 0.01, 10)
    ], ids=["整数", "负数", "1零"])
    @allure.story("除法用例")
    def test_div(self,a,b,expected):
        result = self.calcu.div(a,b)
        assert result == expected

    def test_func(self):
        print("test")
