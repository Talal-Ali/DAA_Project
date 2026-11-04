# 1(b) Exponentiation a^n by Divide and Conquer — Levitin Ex. 5.1(3)

## 1. Pseudocode

```
ALGORITHM Power(a, n)
// Input: real a, positive integer n
// Output: a^n
if n = 1
    return a
half ← Power(a, ⌊n/2⌋)
if n is even
    return half · half                 // 1 multiplication
else
    return half · half · a             // 2 multiplications
```

The idea: a^n = (a^⌊n/2⌋)² when n is even, and (a^⌊n/2⌋)² · a when n is odd. One recursive call instead of two, because both halves are the same value.

## 2. Recurrence for multiplications

Taking n = 2^k (always even until n = 1):

```
M(n) = M(n/2) + 1      for n > 1
M(1) = 0
```

```
M(2^k) = M(2^(k-1)) + 1 = M(2^(k-2)) + 2 = ... = M(1) + k = k = log₂ n
```

So **M(n) = log₂ n ∈ Θ(log n)** for n a power of 2.

For general n the odd case adds one extra multiplication, so
`⌊log₂ n⌋ ≤ M(n) ≤ 2⌊log₂ n⌋`, still Θ(log n).

## 3. Comparison with brute force

Brute force multiplies a by itself n − 1 times: `M_bf(n) = n − 1 ∈ Θ(n)`.

| n     | Divide & conquer log₂ n | Brute force n − 1 |
|-------|-------------------------|-------------------|
| 16    | 4                       | 15                |
| 1024  | 10                      | 1023              |
| 2^20  | 20                      | 1,048,575         |

D&C is exponentially better: linear → logarithmic. This is the standard way large exponents are computed (e.g. modular exponentiation in cryptography).
