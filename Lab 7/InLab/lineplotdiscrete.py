import matplotlib.pyplot as plt

# Prepared the data
x_values = list(range(1, 6))
doubles = [x * 2 for x in x_values]
squares = [x ** 2 for x in x_values]

# Set up and show the line plots
plt.plot(x_values, doubles, label="y = x * 2", color="#1f77b4", marker='o', markersize=8, linestyle='-', linewidth=2)
plt.plot(x_values, squares, label="y = x ** 2", color="#ff7f0e", marker='s', markersize=8, linestyle='--', linewidth=2)

# Add labels and legend
plt.title("Line Plots of Doubles and Squares for Discrete Values 1 to 5", fontsize=16)
plt.xlabel("x-axis", fontsize=14)
plt.ylabel("y-axis", fontsize=14)
plt.legend(fontsize=12)

# Add grid lines
plt.grid(True, linestyle='--', alpha=0.7)

# Adjust layout for better spacing
plt.tight_layout()

plt.show()
