    class Difference:
    def __init__(self, a):
        self.__elements = a
    
# ===================================================================================
# SOLUTION:
    
    def computeDifference(self):
        diff = list()
        [diff.append(abs(i - j)) for i in a for j in a]  # if i != j for different values
        self.maximumDifference = max(diff)
        
# ===================================================================================
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
