import random


def count_cross(left, right):
    i = count = 0
    for y in right:
        while i < len(left) and left[i] <= 2 * y:
            i += 1
        count += len(left) - i
    return count


def merge(left, right):
    i = j = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    return merged + left[i:] + right[j:]


def sig_inv(a):
    if len(a) <= 1:
        return a, 0
    mid = len(a) // 2
    left, cl = sig_inv(a[:mid])
    right, cr = sig_inv(a[mid:])
    cross = count_cross(left, right)
    return merge(left, right), cl + cr + cross


def brute_force(a):
    return sum(1 for i in range(len(a)) for j in range(i + 1, len(a)) if a[i] > 2 * a[j])


n = int(input("Enter n (>= 10): "))
a = random.sample(range(1, 10 * n), n)
print("Array:", a)

_, c = sig_inv(a)
print("Divide & conquer significant inversions:", c)
print("Brute force significant inversions:     ", brute_force(a))
