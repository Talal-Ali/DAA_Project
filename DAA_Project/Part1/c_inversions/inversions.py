import random


def count_inversions(a):
    if len(a) <= 1:
        return a, 0
    mid = len(a) // 2
    left, inv_l = count_inversions(a[:mid])
    right, inv_r = count_inversions(a[mid:])
    merged, inv_split = merge_count(left, right)
    return merged, inv_l + inv_r + inv_split


def merge_count(left, right):
    i = j = count = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            count += len(left) - i
    merged += left[i:] + right[j:]
    return merged, count


def brute_force(a):
    return sum(1 for i in range(len(a)) for j in range(i + 1, len(a)) if a[i] > a[j])


n = int(input("Enter n (>= 10): "))
a = [random.randint(1, 100) for _ in range(n)]
print("Array:", a)

sorted_a, inv = count_inversions(a)
print("Divide & conquer inversions:", inv)
print("Brute force inversions:     ", brute_force(a))
print("Sorted:", sorted_a)
