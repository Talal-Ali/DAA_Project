# Part 2 — Pseudocode

## (i) Closest Pair of Points (2-D), divide and conquer

```
ALGORITHM ClosestPair(P)
// Input: set P of n ≥ 2 points (x, y)
// Output: (d, p, q) — minimum distance and the pair achieving it
Px ← P sorted by x
Py ← P sorted by y
return Rec(Px, Py)

ALGORITHM Rec(Px, Py)
n ← |Px|
if n ≤ 3
    return BruteForce(Px)                       // ≤ 3 pairs
mid ← ⌊n/2⌋
m ← Px[mid].x                                   // vertical dividing line
Lx ← Px[0..mid−1];  Rx ← Px[mid..n−1]
Ly ← points of Py that are in Lx (keeps y-order)
Ry ← points of Py that are in Rx
(dl, ...) ← Rec(Lx, Ly)
(dr, ...) ← Rec(Rx, Ry)
d ← min(dl, dr); best ← the corresponding pair
strip ← [p ∈ Py : |p.x − m| < d]                 // y-sorted, points near the line
for i ← 0 to |strip| − 1
    j ← i + 1
    while j < |strip| and strip[j].y − strip[i].y < d     // at most 7 inner iterations
        if dist(strip[i], strip[j]) < d
            d ← dist(strip[i], strip[j]); best ← (strip[i], strip[j])
        j ← j + 1
return (d, best)
```

Recurrence: sorting once Θ(n log n); each level splits Py and scans the strip in Θ(n);
`T(n) = 2T(n/2) + Θ(n)` → **Θ(n log n)**. Brute force is Θ(n²).

Why the inner loop is bounded: inside a d × 2d rectangle of the strip, points are at least d apart, so at most 8 fit; each point need only be compared with the next ≤ 7 points in y-order.

## (ii) Integer Multiplication (Karatsuba), divide and conquer

```
ALGORITHM Karatsuba(x, y)
// Input: non-negative integers x, y
// Output: x · y
if x < 10 or y < 10
    return x · y                                 // single-digit base case
n ← max(digits(x), digits(y))
h ← ⌊n/2⌋
split x = a·10^h + b,  y = c·10^h + d
ac ← Karatsuba(a, c)
bd ← Karatsuba(b, d)
ad_bc ← Karatsuba(a + b, c + d) − ac − bd        // (a+b)(c+d) = ac + ad + bc + bd
return ac·10^(2h) + ad_bc·10^h + bd
```

Three recursive multiplications of half-size numbers instead of four:
`M(n) = 3M(n/2) + Θ(n)` → Master Theorem a = 3, b = 2, d = 1, a > b^d →
**Θ(n^log₂3) ≈ Θ(n^1.585)**. Schoolbook multiplication is Θ(n²).

## Input file formats

```
closest_pair_XX.txt        multiplication_XX.txt
n                          <first integer>
x1 y1                      <second integer>
x2 y2
...
```

Sizes: points n = 150 … 80000, digits = 128 … 65536 (generate_inputs.py, seed 2026).
