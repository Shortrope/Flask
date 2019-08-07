class Student:

    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def display(self):
        print("Student: " + self.name)
        print("School: " + self.school)

    def avg(self):
        return sum(self.marks) / len(self.marks)

    def goto_school(self):
        print("I'm going to {}".format(self.school))

    def friend(self, friend_name):
        return Student(friend_name, self.school)

class WorkingStudent(Student):

    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary



anna = WorkingStudent("Anna", "MIT", 20.00)
josie = WorkingStudent("Josie", "Berkley", 16.00)
friend = anna.friend("jenna")


anna.display()
anna.marks.append(88)
anna.marks.append(94)
print(anna.avg())
anna.goto_school()
print(anna.salary)
print("")
josie.display()
print(josie.salary)
print("")
print(friend.name)
print(friend.school)



