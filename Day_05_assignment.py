# student = {"name": "Saad", "age": 21, "city": "peshawer"}
# student["age"] = 22
# student["city"] = "islamabad"
# student["course"] = "Python"
# print(student["name"])
# print(student["age"])
# print(student["city"])
# print(student["course"])

# student = {"name": "Saad", "age": 21, "city": "Peshawer"}

# for key in student:
#     print(key,student[key])
# for key in student:
# print(key)


# student = {
#     "name": "Saad",
#     "age": 21,
#     "city": "Peshawer"
# }
# for key in student:
#     print(key,student[key])
# student["course"] = input("enter your course: ")
# for key in student:
#     print(key,student[key])


# numbers = {10, 20, 10, 30, 20, 40}
# numbers.add(50)
# numbers.remove(20)
# if 30 in numbers:
#     print("30 is Present")
# else:
#     print("30 is not present")

# courses = {"Python", "Java", "HTML"}
# user = input("Enter your course: ")
# if user in courses:
#     print("Course already exists")
# else:
#     courses.add(user)
#     print("Course added successfully")

# print("Updated set: ", courses)


# numbers = {10, 20, 30, 10, 40, 20, 50}
# numbers.remove(20)
# numbers.add(60)
# if 40 in numbers:
#     print("Found")
# else:
#     print("Not found")

# print("Updated set length : ", len(numbers))


# A = {10, 20, 30, 40, 50}
# B = {30, 40, 50, 60, 70}

# print(A.intersection(B))
# print(A.difference(B))
# print(B.difference(A))

# A = {10, 20, 30, 40, 50}
# B = {30, 40, 50, 60, 70}
# print(A.symmetric_difference(B))

# python_students = {"Ali", "Sara", "Ahmed", "Zain"}
# java_students = {"Sara", "Zain", "Usman", "Bilal"}

# print(python_students.intersection(java_students))

# python_students = {"Ali", "Sara", "Ahmed", "Zain"}
# java_students = {"Sara", "Zain", "Usman", "Bilal"}
# print(python_students.difference(java_students))

# available_courses = {"python", "java", "html", "css"}

# course = input("Enter your course: ").lower()
# if course in available_courses:
#     print("Course available")
# else:
#     print("Course not available")

available_courses = {"python", "java", "html", "css"}
course = input("Enter your course: ").lower()
if course in available_courses:
    print("Course already exists")
else:
    available_courses.add(course)
    print("Course added successfully")
print("Updated set: ",available_courses)
