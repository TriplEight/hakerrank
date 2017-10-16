#!/bin/python3

t = int(input())
for i in range(1, t + 1):
    s = str(input())
    print(s[::2], s[1::2])
