import random

probes = 0


def unimodal_max(a, l, r):
    global probes
    if l == r:
        return a[l]
    m = (l + r) // 2
    probes += 2
    if a[m] < a[m + 1]:
        return unimodal_max(a, m + 1, r)
    return unimodal_max(a, l, m)


n = int(input("Enter n (>= 10): "))
p = random.randint(0, n - 1)
values = sorted(random.sample(range(1, 10 * n), n))
a = values[:p] + values[p:][::-1]
print("Unimodal array:", a)
print("Peak found:", unimodal_max(a, 0, n - 1), " probes =", probes)
print("Check max():", max(a))
