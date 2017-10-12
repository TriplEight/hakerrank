#!/bin/python3

import sys

def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    a_score = b_score = 0
    a = (a0, a1, a2)
    b = (b0, b1, b2)
    for i in range(len(a)):
	    if a[i] > b[i]:
	        a_score += 1
	    elif a[i] < b[i]:
		    b_score +=1
	    else:
		    pass

    return(a_score, b_score)

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))
