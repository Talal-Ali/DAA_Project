# Part 4 — Visual UI

Pure Python standard library (no pip installs) + one HTML page.

```
cd Part4_UI
python app.py
```

Opens http://localhost:8000 in your browser. The sidebar lists every `.txt` in
`../Part2_3/inputs/` (or a local `inputs/` folder). Click a file to run the
matching algorithm and step through it with ⏮ ◀ Play ▶ ⏭ and the speed slider.

- **closest_pair_XX.txt** — points are drawn, each divide step shows the median
  line and the current region, each conquer step shows the strip of width 2d,
  the strip points, and the best pair so far; the final step shows the answer,
  time, and a brute-force cross-check (n ≤ 5000).
- **multiplication_XX.txt** — the Karatsuba recursion tree (3 children per
  call, node label = digit count, shown to depth 3) with the split values
  a, b, c, d and the combine equation ac·10^2h + (ad+bc)·10^h + bd for each
  call; header shows timing and a check against Python's built-in product.

`python app.py 9000` to use another port; `--no-browser` to not auto-open.
