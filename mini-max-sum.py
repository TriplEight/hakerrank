#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))
l = list()
for i in arr:
    s = sum(arr) - i
    l.append(s)
print(min(l), max(l))
