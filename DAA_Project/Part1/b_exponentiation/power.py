mults = 0


def power(a, n):
    global mults
    if n == 1:
        return a
    half = power(a, n // 2)
    if n % 2 == 0:
        mults += 1
        return half * half
    mults += 2
    return half * half * a


def brute_force(a, n):
    result = a
    for _ in range(n - 1):
        result *= a
    return result, n - 1


a = int(input("Enter base a: "))
n = int(input("Enter exponent n (>= 10): "))

r = power(a, n)
print("Divide & conquer:", r, "multiplications =", mults)

r, c = brute_force(a, n)
print("Brute force:     ", r, "multiplications =", c)
