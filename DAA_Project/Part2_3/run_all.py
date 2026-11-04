import glob
import time

from closest_pair import brute, closest_pair, read_points
from karatsuba import karatsuba, read_numbers

lines = []

lines.append("CLOSEST PAIR OF POINTS")
lines.append(f"{'file':22}{'n':>8}{'distance':>14}{'D&C ms':>12}{'brute ms':>12}  pair")
for path in sorted(glob.glob("inputs/closest_pair_*.txt")):
    pts = read_points(path)
    t = time.perf_counter()
    d, p, q = closest_pair(pts)
    dc = (time.perf_counter() - t) * 1000
    if len(pts) <= 5000:
        t = time.perf_counter()
        db, _, _ = brute(pts)
        bf = f"{(time.perf_counter() - t) * 1000:.1f}"
        assert abs(db - d) < 1e-9
    else:
        bf = "skipped"
    lines.append(f"{path[7:]:22}{len(pts):>8}{d:>14.4f}{dc:>12.1f}{bf:>12}  {p} {q}")

lines.append("")
lines.append("INTEGER MULTIPLICATION (KARATSUBA)")
lines.append(f"{'file':22}{'digits':>8}{'product digits':>16}{'Karatsuba ms':>14}{'schoolbook ms':>15}  correct")
for path in sorted(glob.glob("inputs/multiplication_*.txt")):
    x, y = read_numbers(path)
    t = time.perf_counter()
    r = karatsuba(x, y)
    km = (time.perf_counter() - t) * 1000
    if len(str(x)) <= 16384:
        t = time.perf_counter()
        s = 0
        for i, dgt in enumerate(reversed(str(y))):
            s += x * int(dgt) * 10 ** i
        sm = f"{(time.perf_counter() - t) * 1000:.1f}"
        assert s == r
    else:
        sm = "skipped"
    lines.append(f"{path[7:]:22}{len(str(x)):>8}{len(str(r)):>16}{km:>14.1f}{sm:>15}  {r == x * y}")

out = "\n".join(lines)
print(out)
open("results.txt", "w").write(out + "\n")
