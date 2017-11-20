#!/bin/python3

import sys


n = int(input().strip())
for i in range(1, 11):
    result = n * i
    print('{nn} x {ii} = {results}'.format(nn=n, ii=i, results=result))
