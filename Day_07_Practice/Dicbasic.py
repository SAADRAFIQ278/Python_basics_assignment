# Task 1: Is dictionary mein se student ka naam print karna hai.

student = {"name": "Ali", "age": 20, "city": "Peshawar"}
student["Course"] = "Python"
student["age"] = 21
del student["city"]
print(student["name"])
print(student["age"])
print(student["city"])
print("Updated Dictionary:", student)
