import numpy as np

# Objective: Minimize error between 3a + b and target
def compute_error(a, b, target):
    return abs(3 * a + b - target)

# Trial ranges
a_range = np.linspace(-10, 10, 100)
b_range = np.linspace(-10, 10, 100)

target = 20
min_error = float('inf')
best_a, best_b = None, None

# Trial and Error Search
for a in a_range:
    for b in b_range:
        error = compute_error(a, b, target)
        if error < min_error:
            min_error = error
            best_a = a
            best_b = b

# Results
print(f"Best a: {best_a:.2f}, Best b: {best_b:.2f}")
print(f"Minimum Error: {min_error:.2f}")
print(f"Function value: {3 * best_a + best_b:.2f} (Target: {target})")
