import random
import sys

sys.setrecursionlimit(10000)
comparisons = 0


def hoare_partition(a, l, r):
    global comparisons
    p = a[l]
    i, j = l, r + 1
    while True:
        i += 1
        comparisons += 1
        while i <= r and a[i] < p:
            i += 1
            comparisons += 1
        j -= 1
        comparisons += 1
        while a[j] > p:
            j -= 1
            comparisons += 1
        if i >= j:
            break
        a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def quicksort(a, l, r):
    if l < r:
        s = hoare_partition(a, l, r)
        quicksort(a, l, s - 1)
        quicksort(a, s + 1, r)


def run(label, a):
    global comparisons
    comparisons = 0
    quicksort(a, 0, len(a) - 1)
    print(f"{label:12} n={len(a):5}  comparisons={comparisons:8}  sorted={a == sorted(a)}")


n = int(input("Enter n (>= 10): "))
run("random", [random.randint(1, 1000) for _ in range(n)])
run("sorted", list(range(n)))
run("reversed", list(range(n, 0, -1)))
