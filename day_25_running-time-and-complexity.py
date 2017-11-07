def is_prime(n):
    square_root = int(n ** 0.5)
    if n == 1 or (n != 2 and n % 2 == 0):
        return False
    else:
        for i in range(3, square_root + 1):
            if ((n % i) == 0) and (i != n):
                return False
        return True


t = int(input())
for k in range(t):
    n = int(input())
    if is_prime(n):
        print("Prime")
    else:
        print("Not prime")
