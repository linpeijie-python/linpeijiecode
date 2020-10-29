#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/30 0:00
# @Author  : Mark
# @File    : conftest.py
# @Software: PyCharm
def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid= item.nodeid.encode("utf-8").decode("unicode_escape")