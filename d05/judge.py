#!/usr/bin/env python3
# -*- coding: utf-8 -*-

age = input('please input your age: \n') 
age = int(age)
if age >= 18:
    print('age:%d' % age)
    print ('adult')
else :
    print('kid')

if age >=18 :
    print ('a')
elif age>=6:
    print('b')
else:
    print('c')



height = 1.75
weight = 80.0

bmi = weight/(height**2)

if bmi > 32 :
    print('严重')
elif bmi >28:
    print('肥胖')

elif bmi >25:
    print('过重')
elif bmi>18.5:
    print ('正常')
else:
    print ('过轻')

