import sys

sys.set_int_max_str_digits(0)


def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    n = max(len(str(x)), len(str(y)))
    half = n // 2
    p = 10 ** half
    a, b = divmod(x, p)
    c, d = divmod(y, p)
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    mid = karatsuba(a + b, c + d) - ac - bd
    return ac * p ** 2 + mid * p + bd


def read_numbers(path):
    with open(path) as f:
        return int(f.readline()), int(f.readline())


if __name__ == "__main__":
    x, y = read_numbers(sys.argv[1])
    r = karatsuba(x, y)
    print("digits:", len(str(x)), "x", len(str(y)))
    print("product digits:", len(str(r)))
    print("product:", r if len(str(r)) <= 80 else str(r)[:40] + "..." + str(r)[-40:])
    print("matches built-in:", r == x * y)
