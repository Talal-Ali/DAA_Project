# 1(a) Max and Min by Divide and Conquer — Levitin Ex. 5.1(2)

## 1. Pseudocode

```
ALGORITHM MaxMin(A, l, r)
// Input: array A[0..n-1], indices l ≤ r
// Output: (max, min) of A[l..r]
if l = r
    return (A[l], A[l])                      // 0 comparisons
if r = l + 1
    if A[l] > A[r] return (A[l], A[r])       // 1 comparison
    else           return (A[r], A[l])
mid ← ⌊(l + r) / 2⌋
(max1, min1) ← MaxMin(A, l, mid)
(max2, min2) ← MaxMin(A, mid + 1, r)
max ← larger of (max1, max2)                 // 1 comparison
min ← smaller of (min1, min2)                // 1 comparison
return (max, min)
```

Call with `MaxMin(A, 0, n-1)`.

## 2. Recurrence for key comparisons (n = 2^k)

Each call on n > 2 elements splits into two halves of n/2, then does 2 comparisons to combine.

```
C(n) = 2·C(n/2) + 2      for n > 2
C(2) = 1
C(1) = 0
```

Solve by backward substitution with n = 2^k:

```
C(2^k) = 2·C(2^(k-1)) + 2
       = 2·[2·C(2^(k-2)) + 2] + 2 = 2²·C(2^(k-2)) + 2² + 2
       = ...
       = 2^(k-1)·C(2) + 2^(k-1) + 2^(k-2) + ... + 2
       = 2^(k-1)·1 + (2^k − 2)
       = n/2 + n − 2
       = 3n/2 − 2
```

So **C(n) = 3n/2 − 2 ∈ Θ(n)**.

Check: n = 4 → C = 2·C(2) + 2 = 4 = 3·4/2 − 2 ✓. n = 8 → 2·4 + 2 = 10 = 12 − 2 ✓.

## 3. Comparison with brute force

Brute force scans once and compares every element with the current max and the current min:
`C_bf(n) = 2(n − 1) = 2n − 2`.

| n   | Divide & conquer 3n/2 − 2 | Brute force 2n − 2 |
|-----|---------------------------|--------------------|
| 8   | 10                        | 14                 |
| 64  | 94                        | 126                |
| 1024| 1534                      | 2046               |

Both are Θ(n). D&C saves about 25% of the comparisons (ratio → 3/4), but it pays for a recursion stack of depth log n and more bookkeeping, so in practice the gain is marginal. The same 3n/2 − 2 count is also achievable iteratively by processing elements in pairs.
