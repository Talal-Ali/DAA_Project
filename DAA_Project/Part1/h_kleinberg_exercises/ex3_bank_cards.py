import random

tests = 0


def equivalent(x, y):
    global tests
    tests += 1
    return x == y


def majority(cards, l, r):
    if l == r:
        return cards[l]
    m = (l + r) // 2
    x = majority(cards, l, m)
    y = majority(cards, m + 1, r)
    for c in (x, y):
        if c is None:
            continue
        count = sum(1 for i in range(l, r + 1) if equivalent(cards[i], c))
        if count > (r - l + 1) / 2:
            return c
    return None


n = int(input("Enter n (>= 10): "))
accounts = random.randint(2, 5)
cards = [random.randint(1, accounts) for _ in range(n)]
if random.random() < 0.5:
    cards[: n // 2 + 1] = [1] * (n // 2 + 1)
    random.shuffle(cards)
print("Cards (account ids):", cards)

result = majority(cards, 0, n - 1)
print("Majority account:", result, " equivalence tests =", tests)
print("Check by counting:", max(set(cards), key=cards.count) if cards.count(max(set(cards), key=cards.count)) > n / 2 else None)
