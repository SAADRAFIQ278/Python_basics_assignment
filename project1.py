# num1 = float(input("Enter num 1: "))
# num2 = float(input("Enter num 2: "))
# operator = input("Enter operator: +, -, *, / : ")

# if operator == "+":
#     print("Sum of Values : ", num1 + num2)

# elif operator == "-":
#     print("Subtraction of values : ", num1 - num2)

# elif operator == "*":
#     print("Multiplication of values : ", num1 * num2)

# elif operator == "/":
#     if num2 == 0:
#         print("Cannot divide by Zero!")

#     else:
#         print("Division of value : ", num1 / num2)

# else:
#     print("Invalid Operator! plzz try Valid operator!")


##_____Calculater with function______


# operator = input("Enter operator: +, -, *, / : ")


# def calculator(num1, num2):
#     if operator == "+":
#         return num1 + num2
#     elif operator == "-":
#         return num1 - num2
#     elif operator == "*":
#         return num1 * num2
#     elif operator == "/":
#         return num1 / num2
#     else:
#         return "Invalid Operator!"


# result = calculator(10, 2)
# print(result)


def add(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiply(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Cannot divide by Zero"
    else:
        return a / b


num1 = float(input("Enter your 1st value: "))
num2 = float(input("Enter your 2nd value: "))
operator = input("Enter Operator (+, -, *, / ): ")
if operator == "+":
    result_addition = add(num1, num2)
    print("result: ", result_addition)

elif operator == "-":
    result_subtraction = subtraction(num1, num2)
    print("result: ", result_subtraction)

elif operator == "*":
    result_multiplication = multiply(num1, num2)
    print("result: ", result_multiplication)
elif operator == "/":
    result_division = division(num1, num2)
    print("result: ", result_division)
else:
    print("Invalid Operator!")
