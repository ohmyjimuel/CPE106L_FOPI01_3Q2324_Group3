import pandas as pd
import matplotlib.pyplot as plt

data = {"Course": ["CSCI112", "CSCI312", "PHIL258"],
        "Enrollment": [40, 32, 19]}
frame = pd.DataFrame(data)
frame.plot(x="Course", y="Enrollment", marker='o', linestyle='-', color='#1f77b4')
plt.title("Enrollment in Courses", fontsize=16)
plt.xlabel("Course", fontsize=14)
plt.ylabel("Enrollment", fontsize=14)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

data = {"Course": ["CSCI112", "CSCI312", "PHIL258"],
        "Enrollment": [40, 32, 19]}
frame = pd.DataFrame(data, index=data["Course"])

frame.plot(y="Enrollment", marker='o', linestyle='-', color='#1f77b4')
plt.title("Enrollment in Courses", fontsize=16)
plt.xlabel("Course", fontsize=14)
plt.ylabel("Enrollment", fontsize=14)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

frame.plot.barh(x="Course", y="Enrollment", color='#1f77b4')
plt.title("Enrollment in Courses", fontsize=16)
plt.xlabel("Enrollment", fontsize=14)
plt.ylabel("Course", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
