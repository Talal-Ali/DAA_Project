# 1(f) Kleinberg & Tardos, Chapter 5, Solved Exercise 1 — Median of Two Databases

## Problem

Two databases each hold n distinct numerical values (2n values in total, all distinct). The only allowed operation is a query `kth(D, k)` that returns the k-th smallest value in database D. Find the median (the n-th smallest of the 2n values) using **O(log n)** queries.

## Idea

Ask each database for its own k-th smallest where k = ⌈n/2⌉. Suppose `a = kth(A, k)` and `b = kth(B, k)` with a < b. Then the k smallest values of A are all < b, so the elements of A ranked 1..k−1 are too small to be the overall median — at most k−1 + (k−1) = 2k−2 < n elements of the whole set are smaller than a, so a and everything below it in A can be discarded. Symmetrically, everything **above** b in B can be discarded (b is larger than at least 2k−1 ≥ n elements... i.e. b and above are too large). Each round throws away ⌈n/2⌉−1 elements from each side and the problem shrinks to half the size with the same median, so log₂ n rounds of 2 queries suffice.

## Pseudocode

```
ALGORITHM Median(A, B, n)
// A, B: databases with n values each; kth(D, k) is the only access
// Output: n-th smallest of the 2n values
return Rec(A, 0, B, 0, n)

ALGORITHM Rec(A, offA, B, offB, m)
// we are looking for the m-th smallest among
//   A[offA+1 .. offA+m]  ∪  B[offB+1 .. offB+m]
if m ≤ 2
    query all 2m values in the two ranges and return the m-th smallest   // ≤ 4 queries
k ← ⌈m/2⌉                                   // k − 1 ≥ 1 when m ≥ 3, so progress is guaranteed
a ← kth(A, offA + k)
b ← kth(B, offB + k)
if a < b
    // drop the k−1 smallest of A's range and the k−1 largest of B's range
    return Rec(A, offA + (k − 1), B, offB, m − (k − 1))
else
    return Rec(A, offA, B, offB + (k − 1), m − (k − 1))
```

Sizes: when a < b we discard the k−1 smallest from A (`offA += k − 1`) and the k−1 largest from B (B's range shrinks from the top because m shrinks). The number sought is now the m′-th smallest of the remaining 2m′ values, m′ = m − (k − 1) ≤ ⌈m/2⌉, because exactly k−1 values smaller than the target were removed.

## Query count

```
Q(m) = Q(⌈m/2⌉) + 2,   Q(2) = 4, Q(1) = 2
```
so **Q(n) ≤ 2⌈log₂ n⌉ + 4 ∈ O(log n)**.

## Correctness sketch

Invariant: the median of the original 2n values is always the m-th smallest of the current 2m candidates. When a < b, every one of the k−1 values below a in A is below at least (k−1) values of A and k values of B... in total it has fewer than m values below it in the pool of 2m, so it can't be the m-th. Likewise each value above b in B has more than m values below it. Removing equal numbers from both ends of the pool shifts the target rank by exactly the number removed from the bottom.
