#!/bin/python3

import sys

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

sum1 = sum(a[a_i][a_i] for a_i in range(n))
sum2 = sum(a[a_i][n-a_i-1] for a_i in range(n))
print(abs(sum1-sum2))
