#!/usr/bin/env python3
# -*- coding: utf-8 -*-

users=['jack','lisa','mary']

print (users)
# 从0 开始 取值
print (users[1])

# 也可以从-1开始 从最后开始取
print (users[-1])

# 追加
users.append('tom')

print(users)

# 插入

users.insert(2,'insert')

print(users)

# 删除集合中的最后一个元素
a = users.pop()
print(a)
print(users)
# 删出集合中指定下标的元素
b = users.pop(2)
print(users)


#元素替换

users[0]='replace'

print(users)

#集合中也可以包含集合，类似二位数组
users[1]=['jack','tom']

print(users)

print(users[1][0])

#tuple 有序不可变集合

classmates=('Michael','Bob','Tracy')

print(classmates)


L=[['Apple','Google','Microsoft'],['Java','Python','Ruby','PHP'],['Adam','Bart','Lisa']]

print (L[0][0])

print(L[1][1])

print(L[2][2])
