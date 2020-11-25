#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/22 19:29
# @Author  : Mark
# @File    : test_calcu.py
# @Software: PyCharm
import pytest
import allure
import yaml
from code3_calculator.calculatorCode.calculator import Calculator

"""
pytest 命名规则
文件名：以test_开头_   (test_*.py)
类名：以Test开头
方法名：以test_开头
识别规则：先识别文件名，再去识别类名，最后是方法名；如果类名不符合，那方法名也不会被识别；
"""

def get_datas():
    with open('./calc.yml',encoding='utf-8') as f:
        mydatas=yaml.safe_load(f)
        adddatas=mydatas['add']['mydatas']
        myids=mydatas['add']['myids']
    return [adddatas,myids]

class TestCalc:
    # 类级setup_class.teardown_class（在类中）,只在类中前后运行一次
    def setup_class(self):
        self.calcu = Calculator()
        print("\nsetup_calss在类开始时运行一次")

    def teardown_class(self):
        print("\nteardown_calss在类结束时运行一次")

    def setup(self):
        print("\n-开始计算-")
        #self.calcu = Calculator()

    def teardown(self):
        print("\n-结束计算-")

    @pytest.mark.parametrize("a,b,expected", get_datas()[0],ids=get_datas()[1])
    @allure.story("加法用例")
    @pytest.mark.add
    def test_add(self, a, b, expected):
        result = round(self.calcu.add(a, b),2)
        assert result == expected

    @pytest.mark.parametrize("a,b,expected", [
        (2, 1, 1),
        (-1, -1,0),
        (0, 0, 0)
    ], ids=["整数减法", "负数减法", "为零减法"])
    @allure.story("减法用例")
    @pytest.mark.sub
    def test_sub(self, a, b, expected):
        result = self.calcu.sub(a, b)
        assert result == expected

    @pytest.mark.parametrize("a,b,expected", [
        (2, 1, 2),
        (-1, -2, 2),
        (0, 0, 0),
        (25,25,625)
    ], ids=["整数相乘", "负数相乘", "零相乘","两位数相乘"])
    @allure.story("乘法用例")
    @pytest.mark.mul
    def test_mul(self,a,b,expected):
        result = self.calcu.mul(a, b)
        assert result == expected

    @pytest.mark.parametrize("a,b,expected", [
        (2, 1, 2),
        (1, 2, 0.5),
        (0.1, 0.01, 10)
    ], ids=["整数相除", "负数相除", "零相除"])
    @allure.story("除法用例")
    @pytest.mark.div
    def test_div(self,a,b,expected):
        result = self.calcu.div(a,b)
        assert result == expected

    def test_fu(self):
        print("test")