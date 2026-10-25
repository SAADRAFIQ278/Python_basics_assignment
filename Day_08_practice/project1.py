# import random

# secret_number = random.randint(1, 10)
# attempts = 0
# while attempts < 3:
#     try:
#         user_number = int(input("Guess your number from 1 to 10: "))
       

#         if user_number < 1 or user_number > 10:
#             print("Please enter number between 1 to 10!")
#             continue
#         attempts += 1

#         if user_number == secret_number:
#             print("Congratulation! You win!")
#             break
#         elif user_number < secret_number:
#             print("Too Low!")

#         else:
#             print("Too High!")

#         if attempts == 3:
#             print("Game Over: The number was:",secret_number)
#             print("You guessed it in", attempts, "attempts!")

#     except ValueError:
#         print("Please enter a valid number!")
