class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

student1 = Student("Saad", 21)
student2 = Student("Ahmad", 22)
student1.introduce()
student2.introduce()

