#!/usr/bin/python 
#!coding=utf-8
list = [5,8,6,9,3,4,8,9,5,1,4]
list_len = len(list)
#倒叙排列
l_len = list_len/2
for i in range(l_len):
    list[i],list[list_len-1-i] = list[list_len-1-i], list[i]
print list
#冒泡排序
for i in range(list_len - 1):
    for j in range(i,list_len):
        if list[i] > list[j]:
            list[i],list[j] = list[j],list[i]
print list