#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

smax = -9 * 7

for row in range(len(arr) - 2):
	for column in range(len(arr[row]) - 2):
		a = arr[row][column]
		b = arr[row][column + 1]
		c = arr[row][column + 2]
		d = arr[row + 1][column + 1]
		e = arr[row + 2][column]
		f = arr[row + 2][column + 1]
		g = arr[row + 2][column + 2]
		s = a + b + c + d + e + f + g
		smax = max(s, smax)

print(smax)
