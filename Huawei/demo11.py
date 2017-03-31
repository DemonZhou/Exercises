#coding=utf-8
import sys
import string
'''
题目描述
实现删除字符串中出现次数最少的字符，若多个字符出现次数一样，则都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。

输入描述:
字符串只包含小写英文字母, 不考虑非法输入，输入的字符串长度小于等于20个字节。


输出描述:
删除字符串中出现次数最少的字符后的字符串。

输入例子:
abcdd

输出例子:
dd
'''

while True:
    try:
        dic = {}
        str = raw_input()
        for ch in str:
            if ch not in dic.keys():
                dic[ch] = 1
            else:
                dic[ch] += 1

        chlist = []
        min = sys.maxint
        for key,value in dic.items():
            if min > value:
                min = value

        for key,value in dic.items():
            if value == min:
                chlist.append(key)

        for ch in chlist:
            str = string.replace(str,ch,'')

        print str
    except:
        break
