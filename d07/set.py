#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# set 是无序的唯一的
s = set(['a','b','c'])
print(s)

# set中添加元素
s.add('4')

print(s)

# set中移除元素
s.remove('b')

print(s)

# 不可变对象

a = ['c','b','a']

a.sort()

print(a)

a = 'abc'

b= a.replace('a','A')

print(a)

print(b)

t1 = (1,2,3)

t2 = (1,[2,3])

d = {t1:1}

print(d)
# 由于tuple t2 中包含 list 而list 是可变的，所以无法计算出固定的hash值，不能作为 dict 的key
#d[t2]=2

#print(d)

s= set([t1])

print(s)
# set he dict中的key都是需要计算hash值的，所以也不可以放入 set中
#s.add(t2)

#print(s)


s1 = set([1,2,3,1,2,3])
print(s1)

s2 = set([2,3,4])

# 并集
print (s1&s2)
# 交集
print (s1|s2)
