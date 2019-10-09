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
print(b)
print(users)
