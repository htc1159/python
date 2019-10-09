#!/usr/bin/env python3

# -*- coding:utf-8 -*-

#格式化占位符
print('hello,%s' % 'world')

#! %s 表示字符串 %d 整数 %f 浮点数 %x 十六进制整数

print('age: %d ,name: %s, score:%.2f' % (12 ,'Lisa', 23.45))

#格式化整数和浮点数时可以指定位数，补0
print('%2d-%003d' % (3, 1))
print('%.2f' % 3.1415926)

print('hello,{0},提高了{1:.1f}%'.format('小明',17.231))


s1 = 72
s2 = 85

s3 = (85-72)/72

print (s3)

print ('%.1f%%' % s3 )
