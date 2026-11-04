# 1(e) One-dimensional Closest Pair by Divide and Conquer — Levitin Ex. 5.5(1)

## 1. Algorithm

Sort the numbers first, then split at the median. The closest pair is either entirely in the left half, entirely in the right half, or straddles the split — and in sorted order the only straddling candidate is (last of left, first of right).

```
ALGORITHM ClosestPair1D(P[0..n-1])
// Input: n ≥ 2 real numbers
// Output: minimum distance between two of them
sort P in nondecreasing order               // Θ(n log n), done once
return CP(P, 0, n − 1)

ALGORITHM CP(P, l, r)
if r − l = 1
    return P[r] − P[l]
if r − l = 0
    return ∞
m ← ⌊(l + r)/2⌋
dl ← CP(P, l, m)
dr ← CP(P, m + 1, r)
return min(dl, dr, P[m + 1] − P[m])        // only one cross pair possible
```

## Efficiency class

Recursive part: `T(n) = 2T(n/2) + Θ(1)` → Master Theorem a = 2, b = 2, d = 0, a > b^d → T(n) ∈ Θ(n).
Plus the initial sort Θ(n log n). Total: **Θ(n log n)**.

## 2. Is it a good algorithm?

It is asymptotically optimal — Θ(n log n) is a lower bound for this problem in the comparison model (it is at least as hard as element uniqueness). So the efficiency class is fine.

But the divide-and-conquer step is pointless: once the array is sorted, a single linear scan of adjacent differences gives the same answer with no recursion at all:

```
sort P
dmin ← ∞
for i ← 0 to n − 2
    dmin ← min(dmin, P[i+1] − P[i])
```

Same Θ(n log n) class, simpler, no recursion overhead. Divide and conquer is the right tool for the 2-D version (Part 2 of this project), where the cross-boundary step is non-trivial; in 1-D it adds nothing over "sort then scan". Verdict: correct and optimal in class, but not the algorithm one should actually choose.
