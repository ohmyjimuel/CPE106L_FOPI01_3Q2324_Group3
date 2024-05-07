import matplotlib.pyplot as plt
import stats  # Assuming stats module contains getRandomList function

# Prepare the data
scores = stats.getRandomList(50, 95, 100)

# Set up and show the histogram
plt.hist(scores, bins=10, color='skyblue', edgecolor='black')  # Added bin count and color
plt.title("Distribution of 50 Random Scores Between 95 and 100")
plt.xlabel("Score")
plt.ylabel("Frequency")

# Add grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()