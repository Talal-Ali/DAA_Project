import os
import random

random.seed(2026)
os.makedirs("inputs", exist_ok=True)

point_sizes = [150, 300, 600, 1200, 2500, 5000, 10000, 20000, 40000, 80000]
digit_sizes = [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]

for i, n in enumerate(point_sizes, 1):
    with open(f"inputs/closest_pair_{i:02}.txt", "w") as f:
        f.write(f"{n}\n")
        for _ in range(n):
            f.write(f"{random.uniform(0, 10000):.3f} {random.uniform(0, 10000):.3f}\n")

for i, d in enumerate(digit_sizes, 1):
    with open(f"inputs/multiplication_{i:02}.txt", "w") as f:
        for _ in range(2):
            f.write(str(random.randint(1, 9)) + "".join(random.choice("0123456789") for _ in range(d - 1)) + "\n")

print("generated 20 files in inputs/")
