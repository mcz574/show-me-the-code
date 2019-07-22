#!/usr/bin/python 
l = []
for i in range (2,101):
    flag = 0
    for j in range (2,i-1):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        l.append(i)
print l