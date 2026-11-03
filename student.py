class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, g):
        self.grades.append(g)

    def compute_average(self):
        if len(self.grades) == 0:
            return 0

        return sum(self.grades) / len(self.grades)


student1 = Student("Ana")
student1.add_grade(12)
student1.add_grade(16)

student2 = Student("Ben")

print(student1.name, student1.compute_average())
print(student2.name, student2.compute_average())