#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 11:19
# @Author  : Mark
# @File    : list.py
# @Software: PyCharm
#列表使用
list1=[1,2,3,4]
print(list1)
print(list1[0])
print(list1[1:2])
list1.append('test')
print(list1)
del list1[4]
print(list1)
print(len(list1))
print(max(list1))
print(min(list1))
list1.pop(1)
print(list1)

#元组使用
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"
print(tup1,tup2,tup3)
tup4=(50,)#元组中只包含一个元素时，需要在元素后面添加逗号
print(tup4)
print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])#访问元组
#修改元组
#tup2[2]=8 不能这样修改元组
print(tup1,tup2,tup3)
tup5=tup1+tup2
print(tup1,tup2,tup3,tup4,tup5)
#删除元组
#元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，如下实例:
del tup4
print(tup3)
print(len((1,2,3,4)))#计算元组长度
print((1,2)+(3,4))#元组相加
print(('hi')*4)#元组乘法
#print(('hi')**4)
print(3 in (1,2,3))#元素是否存在
