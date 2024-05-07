import matplotlib.pyplot as plt

data = {"CSCI112": 40, "CSCI312": 32, "PHIL258": 19}
courses, enrollments = zip(*data.items())

plt.figure(figsize=(8, 6))
colors = ['lightblue', 'lightgreen', 'lightcoral']
plt.bar(courses, enrollments, width=0.6, color=colors)
plt.title("Students Enrolled in Ken's Courses", fontsize=16)
plt.xlabel("Course", fontsize=12)
plt.ylabel("Number of Students", fontsize=12)

for course, enrollment in zip(courses, enrollments):
    plt.text(course, enrollment, str(enrollment), ha='center', va='bottom', fontsize=10, color='black')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
