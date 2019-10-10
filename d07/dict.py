#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 中的dict 在其他语言中被称为 map key-value方式存储

names = ['Michael','Bob','Tracy']

scores=[95,75,85]
# dict 定义
d = {'Michael':95,'Bob':75,'Tracy':85}

print(d)

# dict 取值
print(d['Bob'])

# dict 添加
d['Jack']=87

print(d)

# dict 判断key是否存在
print('tom' in d)

print('Jack' in d)

# dict 删除元素
a = d.pop('Jack')

print (a)
# dict 取值
print (d.get('Tom'))
print (d.get('Jack'),-1)

for a in d:
    print (a)
    print (d.get(a))




