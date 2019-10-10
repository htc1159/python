#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
names= ['jack','tom','mary']
for name in names:
    print (name)
# for 循环
num = 0
for a in [1,2,3,4,5,6,7,8,9,10]:
    num+=a
print (num)

sum = 0
for a in range(10):
    sum +=a

print (sum)
# range 函数 自动生成小于指定数值的整数队列 通过list()函数转换为 list
numbers = list(range(10))
print (numbers)

sum = 0 

for a in range(101):
    sum+=a
print (sum)


#while 函数

sum=0
a = 99
while a>0:
    sum+=a
    a=a-2
print(sum)

names = ['Bart','Lisa','Adam']

for name in names:
    print('hello,%s' % name)


n =0
while n <10 :
    n = n+1
    print (n)


n = 0
# break 跳出当前循环
while n<=100:
    if n>10:
        break
    print(n)
    n=n+1
print ('END')

# continue 跳过当前循环 进行下一次循环
n = 0
while n<10:
    n=n+1
    if n%2==0:
        continue
    print(n)

