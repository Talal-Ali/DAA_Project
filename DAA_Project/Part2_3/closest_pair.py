import math
import sys


def dist(p, q):
    return math.hypot(p[0] - q[0], p[1] - q[1])


def brute(pts):
    best = (float("inf"), None, None)
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            d = dist(pts[i], pts[j])
            if d < best[0]:
                best = (d, pts[i], pts[j])
    return best


def rec(px, py):
    n = len(px)
    if n <= 3:
        return brute(px)
    mid = n // 2
    mid_x = px[mid][0]
    lx, rx = px[:mid], px[mid:]
    left_set = set(lx)
    ly = [p for p in py if p in left_set]
    ry = [p for p in py if p not in left_set]
    best = min(rec(lx, ly), rec(rx, ry), key=lambda t: t[0])
    d = best[0]
    strip = [p for p in py if abs(p[0] - mid_x) < d]
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and strip[j][1] - strip[i][1] < d:
            dd = dist(strip[i], strip[j])
            if dd < best[0]:
                best = (dd, strip[i], strip[j])
            j += 1
    return best


def closest_pair(pts):
    px = sorted(pts)
    py = sorted(pts, key=lambda p: (p[1], p[0]))
    return rec(px, py)


def read_points(path):
    with open(path) as f:
        n = int(f.readline())
        return [tuple(map(float, f.readline().split())) for _ in range(n)]


if __name__ == "__main__":
    pts = read_points(sys.argv[1])
    d, p, q = closest_pair(pts)
    print("n =", len(pts))
    print("closest pair:", p, q)
    print("distance:", d)
