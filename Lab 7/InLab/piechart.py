import matplotlib.pyplot as plt

expenses = {
    "Rent": 1200,
    "Food": 700,
    "Healthcare": 500,
    "Transportation": 300,
    "Utilities": 600,
    "Entertainment": 200
}

labels = list(expenses.keys())
slices = list(expenses.values())

plt.figure(figsize=(10, 6))
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

explode = [0.1 if label == max(expenses, key=expenses.get) else 0 for label in labels]

plt.pie(slices, labels=labels, autopct="%1.1f%%", startangle=90, shadow=True, colors=colors, explode=explode)
plt.title("Pie Chart of Living Expenses", fontsize=16)
plt.axis('equal')
plt.tight_layout()
plt.show()
