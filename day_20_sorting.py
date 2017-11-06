import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
# =======================================================
# SOLUTION:

i = 0
num_swaps = 0
for i in range(n):

    j = 0
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            (a[j], a[j + 1]) = (a[j + 1], a[j])
            num_swaps += 1
    if num_swaps == 0:
        break

print('Array is sorted in ' + str(num_swaps) + ' swaps.')
print('First Element:', a[0])
print('Last Element:', a[-1])
