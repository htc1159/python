#!/usr/bin/env python3
# 设置文件编码
# -*- coding: utf-8 -*-

print ('宝行中文的str')

# 字符转十进制
print (ord ('a'))

print (ord('中'))

print (chr(66))

print (chr(25991))

x = b'abc'

print(x)

# encode 将unicode转为字节
print('ABC'.encode('ascii'))

print('中文'.encode('utf-8'))

# decode 将字节转为字符
print (b'ABC'.decode('utf-8'))

print (b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# errors ignore 忽略错误的字节
print(b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore'))


# len 计算字符长度  一个 字占用一个字节 一个中文一般占用三个字节
print(len(B'ABC'))

print(len(b'\xe4\xb8\xad'))

print(len('中'))
