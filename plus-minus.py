#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

posi = 0
zero = 0
nega = 0
for a in arr:
    if a > 0:
        posi += 1
    elif a == 0:
        zero += 1
    else:
        nega += 1

posif = posi/(posi + zero + nega)
zerof = zero/(posi + zero + nega)
negaf = nega/(posi + zero + nega)
print('%.6f' % posif)
print('%.6f' % negaf)
print('%.6f' % zerof)
