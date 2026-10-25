class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def show_details(self):
        print(
            f"My name is {self.name} and i am {self.age} years old and i got {self.marks} marks."
        )

    def check_results(self):
        if self.marks >= 50:
            return "Pass!"
        else:
            return "Fail!"

    def get_grade(self):
        if   90 <= self.marks <= 100:
            return "Grade A!"
        elif  80 <= self.marks <= 89:
            return "Grade B!"
        elif 70 <= self.marks <= 79:
            return "Grade C!"
        elif 60 <= self.marks <= 69:
            return "Grade D!"
        elif 0 <= self.marks <= 59:
            return "Fail"
        else:
            return "Invalid marks"


student1 = Student("Saad", 21, 89)
student2 = Student("Ahmad", 22, 42)
student1.show_details()
result = student1.check_results()
get_grade1 = student1.get_grade()
print(get_grade1)
print("You are :", result)

student2.show_details()
result = student2.check_results()
get_grade2 = student2.get_grade()
print(get_grade2)
print("You are :", result)
