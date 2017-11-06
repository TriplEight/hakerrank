# Write your code here
from math import pow


class Calculator(object):
    # def __init__(self, n, p):
    #    self.n = n
    #    self.p = p

    def power(self, n, p):
        if n >= 0 and p >= 0:
            result = pow(n, p)
            return result
        else:
            raise ValueError("n and p should be non-negative")


myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)
