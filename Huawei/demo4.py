#coding=utf-8
'''
题目描述
编写一个函数，计算字符串中含有的不同字符的个数。字符在ACSII码范围内(0~127)。不在范围内的不作统计。

输入描述:
输入N个字符，字符在ACSII码范围内。


输出描述:
输出范围在(0~127)字符的个数。

输入例子:
abc

输出例子:
3
'''
str = raw_input()
set = []
for c in str:
    if c not in set:
        set.append(c)

print len(set)