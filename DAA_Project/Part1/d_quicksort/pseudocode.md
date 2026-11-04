# 1(d) Quicksort: Best-case and Worst-case Complexity — Levitin §5.2

## Pseudocode (Hoare partition, as in Levitin)

```
ALGORITHM Quicksort(A[l..r])
if l < r
    s ← HoarePartition(A[l..r])      // s is the split position
    Quicksort(A[l..s-1])
    Quicksort(A[s+1..r])

ALGORITHM HoarePartition(A[l..r])
p ← A[l]                               // pivot = first element
i ← l; j ← r + 1
repeat
    repeat i ← i + 1 until A[i] ≥ p
    repeat j ← j − 1 until A[j] ≤ p
    swap(A[i], A[j])
until i ≥ j
swap(A[i], A[j])                       // undo last swap when i ≥ j
swap(A[l], A[j])
return j
```

## Best case

The pivot lands in the middle every time, so both subarrays have size ≈ n/2.
Partitioning an array of size n costs n + 1 comparisons (the two scans cross).

```
C_best(n) = 2·C_best(n/2) + n,   C_best(1) = 0
```
Master Theorem: a = 2, b = 2, d = 1 → **C_best(n) ∈ Θ(n log₂ n)**.
Exact for n = 2^k: C_best(n) = n log₂ n.

## Worst case

Happens when the pivot is the smallest or largest element every time, e.g. an already sorted (or reverse-sorted) array with first-element pivot. One subarray is empty, the other has n − 1 elements.

```
C_worst(n) = (n + 1) + n + (n − 1) + ... + 3
           = (n + 1)(n + 2)/2 − 3
```
so **C_worst(n) ∈ Θ(n²)**.

## Average case (for reference)

Levitin derives `C_avg(n) ≈ 2n ln n ≈ 1.39 n log₂ n`, so quicksort is only ~39% slower than its best case on average, which is why it is fast in practice despite the Θ(n²) worst case. Randomised pivot selection or median-of-three makes the worst case very unlikely.

| Case    | Input that triggers it            | Comparisons        |
|---------|-----------------------------------|--------------------|
| Best    | pivot always splits evenly        | Θ(n log n)         |
| Average | random data                       | ≈ 1.39 n log₂ n    |
| Worst   | sorted / reverse-sorted, 1st pivot| Θ(n²)              |
