import random

queries = 0


def kth(db, k):
    global queries
    queries += 1
    return db[k - 1]


def rec(a, off_a, b, off_b, m):
    if m <= 2:
        pool = [kth(a, off_a + i) for i in range(1, m + 1)] + [kth(b, off_b + i) for i in range(1, m + 1)]
        return sorted(pool)[m - 1]
    k = (m + 1) // 2
    x = kth(a, off_a + k)
    y = kth(b, off_b + k)
    if x < y:
        return rec(a, off_a + k - 1, b, off_b, m - (k - 1))
    return rec(a, off_a, b, off_b + k - 1, m - (k - 1))


def median(a, b, n):
    return rec(a, 0, b, 0, n)


n = int(input("Enter n (>= 10): "))
values = random.sample(range(1, 10 * n), 2 * n)
a = sorted(values[:n])
b = sorted(values[n:])
print("Database A:", a)
print("Database B:", b)

m = median(a, b, n)
print("Median via queries:", m, " queries used =", queries)
print("Median by merging: ", sorted(values)[n - 1])
