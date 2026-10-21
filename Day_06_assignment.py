# numbers = {10, 20, 10, 30, 20, 40, 50}
# numbers.add(60)
# unique_value = len(numbers)
# print("Unique_value : ", unique_value)
# print("Updated_list : ", numbers)


# Sirf woh students print karo jo dono courses mein hain.
# Sirf woh students print karo jo Python mein hain, lekin Java mein nahi.
# Dono sets mein total unique students kitne hain, woh print karo.

# python_students = {"Ali", "Sara", "Ahmed", "Zain"}
# java_students = {"Sara", "Zain", "Usman", "Bilal"}

# both_course = python_students.intersection(java_students)
# print("Enrolled in both courses :", both_course)

# only_python = python_students.difference(java_students)
# print("Enrolled in python only : ",only_python)

# unique_value = len(python_students.union(java_students))
# print("Unique value: ", unique_value)



# Task: User se ek number input lo. Agar woh number set mein hai, to "Number exists" print karo.
# Warna us number ko set mein add karo aur "Number added" print karo. Aakhir mein updated set print
# karo.

numbers = {10, 20, 30, 40, 50, 60}
num = int(input("Enter your number: "))

if num in numbers:
    print("Number Exist!")
else:
    numbers.add(num)
    print("Number added!")
print("Updated_set: ",numbers)