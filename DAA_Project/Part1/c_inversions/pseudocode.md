# 1(c) Counting Inversions in O(n log n) — Levitin Ex. 5.1(9)

An inversion is a pair i < j with A[i] > A[j]. Brute force checks all pairs: Θ(n²).

## Idea

Piggyback on merge sort. Inversions are of three kinds: both elements in the left half, both in the right half, or one in each. The first two are counted by the recursive calls. The third kind is counted during the merge: when an element from the **right** half is placed before the remaining elements of the **left** half, it forms an inversion with every one of those remaining left elements, and they are all still in the left run, so we add their count in O(1).

## Pseudocode

```
ALGORITHM CountInversions(A[0..n-1])
// Output: (sorted copy of A, number of inversions)
if n ≤ 1
    return (A, 0)
mid ← ⌊n/2⌋
(L, invL) ← CountInversions(A[0..mid-1])
(R, invR) ← CountInversions(A[mid..n-1])
(S, invSplit) ← MergeCount(L, R)
return (S, invL + invR + invSplit)

ALGORITHM MergeCount(L[0..p-1], R[0..q-1])
i ← 0; j ← 0; count ← 0; S ← empty
while i < p and j < q
    if L[i] ≤ R[j]
        append L[i] to S; i ← i + 1
    else
        append R[j] to S; j ← j + 1
        count ← count + (p − i)         // every remaining L element > R[j]
append remaining L then remaining R to S
return (S, count)
```

## Efficiency

```
T(n) = 2T(n/2) + Θ(n),  T(1) = Θ(1)
```
Master Theorem, a = 2, b = 2, d = 1, a = b^d → **T(n) ∈ Θ(n log n)**.

Exactly the merge-sort recurrence; the extra `count += p − i` is O(1) per merge step.

Example: A = [2, 3, 8, 6, 1] → inversions (2,1) (3,1) (8,6) (8,1) (6,1) = 5.
