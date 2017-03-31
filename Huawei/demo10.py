#coding=utf-8
'''
题目描述
把 M 个同样的苹果放在 N 个同样的盘子里，允许有的盘子空着不放，问共有多少种不同的分法？
注意：5、1、1 和 1、5、1 是同一种分法，即顺序无关。

输入描述:
输入包含多组数据。

每组数据包含两个正整数 m和n（1≤m, n≤20）。


输出描述:
对应每组数据，输出一个整数k，表示有k种不同的分法。

输入例子:
7 3

输出例子:
8
'''
def dp(m,n):
    if m == 0:
        return 1
    elif n == 1:
        return 1
    elif  n > m:
        return dp(m,m)
    else :
        return  dp(m,n-1) + dp(m-n,n)

while True:
    try:
        str = raw_input()
        M = int((str.split(' '))[0])
        N = int((str.split(' '))[1])
        print dp(M,N)
    except:
        break
