import random

probes = 0


def label(tree, v):
    global probes
    probes += 1
    return tree[v]


def local_min(tree):
    n = len(tree)
    v = 0
    while True:
        left, right = 2 * v + 1, 2 * v + 2
        if left >= n:
            return v
        c = left if label(tree, left) < label(tree, right) else right
        if label(tree, v) < label(tree, c):
            return v
        v = c


def is_local_min(tree, v):
    n = len(tree)
    neighbours = [(v - 1) // 2] if v > 0 else []
    neighbours += [c for c in (2 * v + 1, 2 * v + 2) if c < n]
    return all(tree[v] < tree[u] for u in neighbours)


d = int(input("Enter depth d (tree has 2^d - 1 nodes, d >= 4): "))
n = 2 ** d - 1
tree = random.sample(range(1, 10 * n), n)
print("Tree labels (level order):", tree)

v = local_min(tree)
print("Local minimum at node", v, "with label", tree[v], " probes =", probes, " verified =", is_local_min(tree, v))
