#!/bin/python3

import sys


n = int(input().strip())
v = 0
li = list()
for i in bin(n):
    if i == '1':
        v += 1
        li.append(v)
    else:
        v = 0
        li.append(0)
print(max(li))
