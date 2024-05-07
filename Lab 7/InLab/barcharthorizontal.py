import matplotlib.pyplot as plt
import numpy as np

data = {
    "Data Structures": 40,
    "Programming Language Design": 32,
    "Freud Seminar": 19
}

courses = list(data.keys())
enrollments = list(data.values())

fig, ax = plt.subplots(figsize=(8, 6))
colors = ['lightblue', 'lightgreen', 'lightcoral']
ax.barh(courses, enrollments, height=0.5, color=colors)

ax.set_title("Students Enrolled in Ken's Courses", fontsize=16)
ax.set_xlabel("Number of Students", fontsize=12)
ax.set_ylabel("Course", fontsize=12)

for index, value in enumerate(enrollments):
    ax.text(value, index, str(value), ha='left', va='center', fontsize=10, color='black')

ax.invert_yaxis()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
