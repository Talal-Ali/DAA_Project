# 1(h) Kleinberg & Tardos, Chapter 5 Exercises — three chosen: 1, 3, 5

(Numbering follows the 1st edition, pp. 246–249. Check against your copy before submitting.)

---

## Exercise 1 — Maximum of a unimodal array in O(log n)

**Problem.** A[1..n] is unimodal: strictly increasing up to some index p, strictly decreasing after it. All entries distinct. Find the maximum (A[p]) in O(log n) probes.

**Idea.** Look at the middle element and its right neighbour. If A[m] < A[m+1] we are on the rising slope, so the peak is to the right; otherwise we are on the falling slope (or at the peak), so the peak is at m or to the left. Halve the range each time.

```
ALGORITHM UnimodalMax(A, l, r)
if l = r return A[l]
m ← ⌊(l + r)/2⌋
if A[m] < A[m + 1]
    return UnimodalMax(A, m + 1, r)
else
    return UnimodalMax(A, l, m)
```
Recurrence: T(n) = T(n/2) + O(1) → **O(log n)**.
Correctness: on a unimodal array A[m] < A[m+1] holds iff m < p, so the peak is never discarded.

---

## Exercise 3 — Bank cards: is there an equivalence class of size > n/2?

**Problem.** n cards; the only operation is an equivalence tester on two cards (same account or not). Decide whether more than n/2 cards belong to the same account, using **O(n log n)** tests.

**Idea (divide and conquer).** If some account holds a majority of all n cards, it must hold a majority of at least one of the two halves (otherwise it has ≤ n/4 + n/4 = n/2 cards, not a majority). So: recursively find the majority card of each half (if any), then verify each candidate against the whole range with n − 1 tests. At most 2 candidates per level, so the combine step is O(n).

```
ALGORITHM Majority(C[l..r])
// Output: a card from the majority account of C[l..r], or NONE
if l = r return C[l]
m ← ⌊(l + r)/2⌋
x ← Majority(C[l..m])
y ← Majority(C[m+1..r])
for each candidate c in {x, y} that is not NONE
    count ← number of cards in C[l..r] equivalent to c      // r − l tests
    if count > (r − l + 1)/2 return c
return NONE
```
Recurrence: T(n) = 2T(n/2) + O(n) → **O(n log n)** tests.

(A linear-time alternative exists — pair cards up, discard non-equivalent pairs — but the question asks for O(n log n) and the above is the natural divide-and-conquer answer.)

---

## Exercise 5 — Local minimum in a complete binary tree in O(log n) probes

**Problem.** T is a complete binary tree with n = 2^d − 1 nodes, each labelled with a distinct real number x_v. A node is a **local minimum** if its label is smaller than the labels of all its neighbours (parent and children). Find a local minimum with O(log n) probes.

**Idea.** Start at the root. If the current node is smaller than both children it is a local minimum (the root has no parent; an internal node reached by walking down is already smaller than its parent). Otherwise move to the smaller child — the labels strictly decrease along the walk, so the walk can never go back up, and it must stop by a leaf at the latest. The path has length ≤ d = log₂(n + 1).

```
ALGORITHM LocalMin(v)
// v starts at the root
loop
    if v is a leaf return v
    c ← child of v with the smaller label
    if x_v < x_c return v               // v smaller than both children (and its parent)
    v ← c
```
Each iteration probes at most 3 labels and descends one level → **O(log n)** probes.
Correctness: when we move from v to child c, x_c < x_v, so c already beats its parent; at the stopping node it also beats both children (or has none), hence it is a local minimum.
