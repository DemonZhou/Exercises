#coding=utf-8
'''
题目描述
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。

输入描述:
输入一个int型整数


输出描述:
按照从右向左的阅读顺序，返回一个不含重复数字的新的整数

输入例子:
9876673

输出例子:
37689
'''

str = raw_input()
result = ""
str = str[::-1]
for i in range(0,len(str)):
    if str[i] not in result:
        result += str[i]
print result