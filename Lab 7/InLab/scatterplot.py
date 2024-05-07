import matplotlib.pyplot as plt
import numpy as np
import stats  # Assuming stats module contains getRandomList function

# Prepare the data
positions = np.arange(1, 101)  # Generating positions array using numpy
numbers = stats.getRandomList(100, 1, 100, unique=True)

# Set up and show the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(positions, numbers, color="purple", marker='.', label="Random Numbers", alpha=0.7, s=50)
plt.title("Scatter Plot of Unique Random Numbers from 1 to 100")
plt.xlabel("Position")
plt.ylabel("Random Number")

# Adding grid for better readability
plt.grid(True, linestyle='--', alpha=0.7)

# Adding legend
plt.legend()

plt.show()
