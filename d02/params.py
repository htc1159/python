#!/usr/bin/env python3
# \表示转义
print ('I\'m \"OK\"')

# r'' 标识字符不被转义
print (r'\\\t\\')

# '''xxxx''' 表示换行
print (''' line1
line2 
line3 ''')

print (r'''hello,\n
world''')
# a赋值为整型
a = 123 

print (a)
# a赋值为字符串
a= 'ABC'

print(a)

# 由于变量a没有固定的类型，所以称之为动态语言， 
# 对应的静态语言，实在变量定义时就指定了类型

x = 10 
x += 2

print(x)

a = 'ABC'

b = a 

a = 'XYZ'

#结果为 ABC 值传递
print(b)

#常量  全部大写来定义变量名称

PI = 3.141592653

print (PI)

# python中的除法

print (10/3)
# 除法的计算结果是浮点数，两个整数相除，结果也是浮点数
print(9/3)
# 地板除， 结果仍然是整数
print (10//3)

# 求
print(10%3)


# 联系


print(123)

print (456.789)

print ('hello,world')

print ('hello, \'Adam\'')

print (r'hello,"Bart"')

print (r'''hello,
Lisa!''')


