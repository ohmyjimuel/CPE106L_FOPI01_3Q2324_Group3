"""
File: student.py
Resources to manage a student's name and test scores.
"""

import random

class Student(object):
    """Represents a student."""

    def __init__(self, name, num):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(num):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name

    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]

    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)

    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)

    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name + "\nScores: " + \
               " ".join(map(str, self.scores))

    def __eq__(self, other):
        """Returns True if two students have the same name."""
        return self.name == other.name

    def __lt__(self, other):
        """Returns True if the name of the current student comes before the name of the other student."""
        return self.name < other.name

    def __ge__(self, other):
        """Returns True if the name of the current student comes after or is equal to the name of the other student."""
        return self.name >= other.name


def main():
    """A simple test."""
    # Create a list of Student objects
    students = [
        Student("Ken", 5),
        Student("John", 5),
        Student("Alice", 5),
        Student("Bob", 5),
        Student("Emma", 5)
    ]

    # Shuffle the list
    random.shuffle(students)

    # Sort the list
    students.sort()

    # Display student information
    for student in students:
        print(student)
        print()

if __name__ == "__main__":
    main()