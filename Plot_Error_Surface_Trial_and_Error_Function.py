import numpy as np
import matplotlib.pyplot as plt

# Target value
target = 20

# Error function
def compute_error(a, b):
    return np.abs(3 * a + b - target)

# Generate a grid of (a, b) values
a_vals = np.linspace(-10, 10, 100)
b_vals = np.linspace(-10, 10, 100)
A, B = np.meshgrid(a_vals, b_vals)

# Calculate error at each grid point
Error = compute_error(A, B)

# Plotting the contour plot
plt.figure(figsize=(10, 6))
contour = plt.contourf(A, B, Error, levels=50, cmap='viridis')
plt.colorbar(contour, label='Error')
plt.title('Error Surface for f(a, b) = 3a + b (Target = 20)')
plt.xlabel('a')
plt.ylabel('b')
plt.grid(True)
plt.show()
