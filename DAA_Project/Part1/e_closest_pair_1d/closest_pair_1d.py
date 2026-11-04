import random


def cp(p, l, r):
    if r - l == 1:
        return p[r] - p[l], (p[l], p[r])
    if r - l == 0:
        return float("inf"), None
    m = (l + r) // 2
    dl, pl = cp(p, l, m)
    dr, pr = cp(p, m + 1, r)
    dm, pm = p[m + 1] - p[m], (p[m], p[m + 1])
    return min((dl, pl), (dr, pr), (dm, pm), key=lambda t: t[0])


def closest_pair_1d(p):
    p = sorted(p)
    return cp(p, 0, len(p) - 1)


def brute_force(p):
    best = (float("inf"), None)
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            d = abs(p[i] - p[j])
            if d < best[0]:
                best = (d, (p[i], p[j]))
    return best


n = int(input("Enter n (>= 10): "))
p = [round(random.uniform(0, 1000), 2) for _ in range(n)]
print("Numbers:", p)

d, pair = closest_pair_1d(p)
print("Divide & conquer: distance =", round(d, 4), "pair =", pair)

d, pair = brute_force(p)
print("Brute force:      distance =", round(d, 4), "pair =", pair)
