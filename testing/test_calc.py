#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/15 18:36
# @Author  : Mark
# @File    : test_calc.py
# @Software: PyCharm
from pythoncode.calculator import Calculator
"""
文件名：以test_开头_   (test_*.py)
类名：以Test开头
方法名：以test_开头
"""

class TestCalc:
    def test_add1(self):
        calc = Calculator()
        result = calc.add(1,2)
        assert result == 3
    def test_add2(self):
        calc = Calculator()
        result = calc.add(1,3)
        assert result == 3
    def test_add3(self):
        calc = Calculator()
        result = calc.add(1,4)
        assert result == 3

    def test_func(self):
        print("test")