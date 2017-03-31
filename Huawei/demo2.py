#coding=utf-8
'''
题目描述
数据表记录包含表索引和数值，请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。

输入描述:
先输入键值对的个数
然后输入成对的index和value值，以空格隔开


输出描述:
输出合并后的键值对（多行）

输入例子:
4
0 1
0 2
1 2
3 4

输出例子:
0 3
1 2
3 4
'''
import sys
dict = {}
num = int(sys.stdin.readline())
for i in range(0,num):
    str = raw_input()
    key = int(str.split(' ')[0])
    value = int(str.split(' ')[1])
    if key not in dict.keys():
        dict[key] = value
    else :
        dict[key] += value
sorted(dict.keys())
for key,value in dict.items():
    print "%d %d"%(key,value)
