import matplotlib.pyplot as plt
import numpy as np

# Prepare the data
x_values = np.linspace(1, 5)
doubles = x_values * 2
squares = x_values ** 2

# Set up and show the line plots
plt.plot(x_values, doubles, label="y = x * 2", color="#1f77b4", marker='o', markersize=8, linestyle='-', linewidth=2)
plt.plot(x_values, squares, label="y = x ** 2", color="#ff7f0e", marker='s', markersize=8, linestyle='--', linewidth=2)

# Add labels and legend with increased font size
plt.title("Line Plots of Doubles and Squares in the Range 1 to 5", fontsize=16)
plt.xlabel("x-axis", fontsize=14)
plt.ylabel("y-axis", fontsize=14)
plt.legend(fontsize=12)

# Add grid lines
plt.grid(True, linestyle='--', alpha=0.7)

# Adjust layout for better spacing
plt.tight_layout()

plt.show()
