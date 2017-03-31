#coding=utf-8
'''
题目描述
密码要求:



1.长度超过8位



2.包括大小写字母.数字.其它符号,以上四种至少三种



3.不能有相同长度超2的子串重复



说明:长度超过2的子串


输入描述:
一组或多组长度超过2的子符串。每组占一行


输出描述:
如果符合要求输出：OK，否则输出NG

输入例子:
021Abc9000
021Abc9Abc1
021ABC9000
021$bc9000

输出例子:
OK
NG
NG
OK
'''

def DupNum(string):
    off = 0
    maxlen = 1
    i = 0
    while(i < len(string)):
        tempi = i
        for j in range(i+1,len(string) ):
            if string[i] == string[j]:
                i = i + 1
                off = off + 1
            else:
                if off > maxlen:
                    maxlen = off
                off = 0
        i = tempi + 1
    return maxlen

while True:
    try:
        str = raw_input()
        #Situation 1
        if len(str) < 8:
            print 'NG'
        else :
            #Situation 2
            lower = False
            upper = False
            digit = False
            other = False
            for c in str:
                if c.islower():
                    lower = True
                elif c.isupper():
                    upper = True
                elif c.isdigit():
                    digit = True
                else :
                    other = True
            sum = 0
            if lower:
                sum = sum + 1
            if upper:
                sum = sum + 1
            if digit:
                sum = sum + 1
            if other:
                sum = sum + 1
            if sum < 3:
                print 'NG'
            else :
                if DupNum(str) > 2:
                    print 'NG'
                else :
                    print 'OK'
    except:
        break
