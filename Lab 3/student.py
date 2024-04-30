"""
File: student.py
Resources to manage a student's name and test scores.
"""
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
    student1 = Student("Ken", 5)
    student2 = Student("John", 5)
    student3 = Student("Ken", 5)

    # Equality Test
    print("Equality Test:")
    print("student1 == student2:", student1.__eq__(student2))
    print("student1 == student3:", student1.__eq__(student3))

    # Less Than Test
    print("\nLess Than Test:")
    print("student1 < student2:", student1.__lt__(student2))
    print("student2 < student3:", student2.__lt__(student3))

    # Greater Than or Equal To Test
    print("\nGreater Than or Equal To Test:")
    print("student1 >= student2:", student1.__ge__(student2))
    print("student3 >= student2:", student3.__ge__(student2))

if __name__ == "__main__":
    main()