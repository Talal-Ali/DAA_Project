import glob
import json
import math
import os
import sys
import time
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import parse_qs, urlparse

sys.set_int_max_str_digits(0)
HERE = os.path.dirname(os.path.abspath(__file__))
INPUT_DIRS = [os.path.join(HERE, "inputs"), os.path.join(HERE, "..", "Part2_3", "inputs")]
MAX_DEPTH = 5


def dist(p, q):
    return math.hypot(p[0] - q[0], p[1] - q[1])


def brute(pts):
    best = (float("inf"), None, None)
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            d = dist(pts[i], pts[j])
            if d < best[0]:
                best = (d, pts[i], pts[j])
    return best


def cp_rec(px, py, depth, steps, box):
    n = len(px)
    if n <= 3:
        best = brute(px)
        if depth <= MAX_DEPTH:
            steps.append({"type": "base", "box": box, "pts": px, "d": best[0], "pair": [best[1], best[2]]})
        return best
    mid = n // 2
    mid_x = px[mid][0]
    lx, rx = px[:mid], px[mid:]
    left_set = set(lx)
    ly = [p for p in py if p in left_set]
    ry = [p for p in py if p not in left_set]
    if depth <= MAX_DEPTH:
        steps.append({"type": "split", "box": box, "x": mid_x, "n": n, "depth": depth})
    lbox = [box[0], mid_x, box[2], box[3]]
    rbox = [mid_x, box[1], box[2], box[3]]
    bl = cp_rec(lx, ly, depth + 1, steps, lbox)
    br = cp_rec(rx, ry, depth + 1, steps, rbox)
    best = min(bl, br, key=lambda t: t[0])
    d = best[0]
    strip = [p for p in py if abs(p[0] - mid_x) < d]
    checked = 0
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and strip[j][1] - strip[i][1] < d:
            checked += 1
            dd = dist(strip[i], strip[j])
            if dd < best[0]:
                best = (dd, strip[i], strip[j])
            j += 1
    if depth <= MAX_DEPTH:
        steps.append({"type": "strip", "box": box, "x": mid_x, "d": d, "strip": strip[:400], "stripN": len(strip),
                      "checked": checked, "dl": bl[0], "dr": br[0], "best": best[0], "pair": [best[1], best[2]],
                      "improved": best[0] < d})
    return best


def run_closest_pair(path):
    with open(path) as f:
        n = int(f.readline())
        pts = [tuple(map(float, f.readline().split())) for _ in range(n)]
    t = time.perf_counter()
    px = sorted(pts)
    py = sorted(pts, key=lambda p: (p[1], p[0]))
    steps = []
    box = [px[0][0], px[-1][0], py[0][1], py[-1][1]]
    d, p, q = cp_rec(px, py, 0, steps, box)
    ms = (time.perf_counter() - t) * 1000
    bf = None
    if n <= 5000:
        t = time.perf_counter()
        bd, bp, bq = brute(pts)
        bf = {"d": bd, "ms": (time.perf_counter() - t) * 1000}
    return {"kind": "points", "file": os.path.basename(path), "n": n, "points": pts[:20000], "box": box,
            "steps": steps, "result": {"d": d, "pair": [p, q], "ms": ms}, "brute": bf}


def short(v):
    s = str(v)
    return s if len(s) <= 14 else s[:6] + "…" + s[-5:] + f" ({len(s)} digits)"


def kara(x, y, depth, node):
    if x < 10 or y < 10:
        node.update({"x": short(x), "y": short(y), "base": True, "result": short(x * y)})
        return x * y
    n = max(len(str(x)), len(str(y)))
    half = n // 2
    p = 10 ** half
    a, b = divmod(x, p)
    c, d = divmod(y, p)
    children = [{}, {}, {}] if depth < 3 else None
    ac = kara(a, c, depth + 1, children[0] if children else {})
    bd = kara(b, d, depth + 1, children[1] if children else {})
    s = kara(a + b, c + d, depth + 1, children[2] if children else {})
    mid = s - ac - bd
    r = ac * p ** 2 + mid * p + bd
    node.update({"x": short(x), "y": short(y), "n": n, "h": half, "a": short(a), "b": short(b), "c": short(c),
                 "d": short(d), "ac": short(ac), "bd": short(bd), "sum": short(s), "mid": short(mid),
                 "result": short(r), "children": children})
    return r


def run_multiplication(path):
    with open(path) as f:
        x, y = int(f.readline()), int(f.readline())
    tree = {}
    t = time.perf_counter()
    r = kara(x, y, 0, tree)
    ms = (time.perf_counter() - t) * 1000
    t = time.perf_counter()
    check = x * y
    bms = (time.perf_counter() - t) * 1000
    calls = [0]

    def count(a, b):
        calls[0] += 1
        if a < 10 or b < 10:
            return
        h = max(len(str(a)), len(str(b))) // 2
        p = 10 ** h
        a1, a0 = divmod(a, p)
        b1, b0 = divmod(b, p)
        count(a1, b1)
        count(a0, b0)
        count(a1 + a0, b1 + b0)

    if len(str(x)) <= 4096:
        count(x, y)
    return {"kind": "integers", "file": os.path.basename(path), "digits": [len(str(x)), len(str(y))],
            "x": str(x), "y": str(y), "tree": tree, "calls": calls[0] or None,
            "result": {"product": str(r), "digits": len(str(r)), "ms": ms, "correct": r == check, "builtin_ms": bms}}


def list_files():
    out = []
    for d in INPUT_DIRS:
        for p in sorted(glob.glob(os.path.join(d, "*.txt"))):
            out.append({"name": os.path.basename(p), "path": p, "size": os.path.getsize(p)})
    seen, uniq = set(), []
    for f in out:
        if f["name"] not in seen:
            seen.add(f["name"])
            uniq.append(f)
    return uniq


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=HERE, **k)

    def send_json(self, obj):
        data = json.dumps(obj).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        u = urlparse(self.path)
        if u.path == "/files":
            return self.send_json(list_files())
        if u.path == "/run":
            name = parse_qs(u.query)["file"][0]
            path = next(f["path"] for f in list_files() if f["name"] == name)
            return self.send_json(run_closest_pair(path) if name.startswith("closest") else run_multiplication(path))
        if u.path == "/":
            self.path = "/index.html"
        return super().do_GET()

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    print(f"open http://localhost:{port}")
    if "--no-browser" not in sys.argv:
        webbrowser.open(f"http://localhost:{port}")
    HTTPServer(("localhost", port), Handler).serve_forever()
