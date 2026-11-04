import random

comparisons = 0


def max_min(a, l, r):
    global comparisons
    if l == r:
        return a[l], a[l]
    if r == l + 1:
        comparisons += 1
        return (a[l], a[r]) if a[l] > a[r] else (a[r], a[l])
    mid = (l + r) // 2
    max1, min1 = max_min(a, l, mid)
    max2, min2 = max_min(a, mid + 1, r)
    comparisons += 2
    return max(max1, max2), min(min1, min2)


def brute_force(a):
    c = 0
    mx = mn = a[0]
    for x in a[1:]:
        c += 2
        if x > mx:
            mx = x
        if x < mn:
            mn = x
    return mx, mn, c


n = int(input("Enter n (>= 10): "))
a = [random.randint(-1000, 1000) for _ in range(n)]
print("Array:", a)

mx, mn = max_min(a, 0, n - 1)
print("Divide & conquer: max =", mx, "min =", mn, "comparisons =", comparisons)

mx, mn, c = brute_force(a)
print("Brute force:      max =", mx, "min =", mn, "comparisons =", c)
