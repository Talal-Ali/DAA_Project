# 1(g) Kleinberg & Tardos, Chapter 5, Solved Exercise 2 — Significant Inversions

## Problem

Given n distinct numbers a₁..aₙ, a pair i < j is a **significant inversion** if aᵢ > 2·aⱼ. Count them in O(n log n).

## Idea

Same merge-sort skeleton as ordinary inversion counting, but the "> 2·aⱼ" test is not the same as the ordering test, so the merge can't count while it sorts. Fix: before merging two sorted halves L and R, do one separate two-pointer pass that counts pairs (x ∈ L, y ∈ R) with x > 2y, **then** merge normally. Both passes are linear, so the recurrence is unchanged.

Counting pass: walk j over R. For each R[j], advance i over L while L[i] ≤ 2·R[j]; every element of L from i onward is > 2·R[j]. Since both lists are sorted, i never moves backwards.

## Pseudocode

```
ALGORITHM SigInv(A[0..n-1])
// Output: (sorted A, number of significant inversions)
if n ≤ 1 return (A, 0)
mid ← ⌊n/2⌋
(L, cL) ← SigInv(A[0..mid-1])
(R, cR) ← SigInv(A[mid..n-1])
cross ← CountCross(L, R)
S ← Merge(L, R)                      // ordinary merge
return (S, cL + cR + cross)

ALGORITHM CountCross(L[0..p-1], R[0..q-1])
i ← 0; count ← 0
for j ← 0 to q − 1
    while i < p and L[i] ≤ 2·R[j]
        i ← i + 1
    count ← count + (p − i)
return count
```

## Efficiency

CountCross is O(p + q), Merge is O(p + q), so
```
T(n) = 2T(n/2) + O(n)  →  T(n) ∈ O(n log n)
```

Example: A = [5, 1, 3, 2] → significant pairs: (5,1), (5,2) → 2. ((5,3) is an inversion but 5 ≤ 6, so not significant.)
