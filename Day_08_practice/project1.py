import random

secret_number = random.randint(1, 10)
attempts = 0
while attempts < 3:
    try:
        user_number = int(input("Guess your number from 1 to 10: "))
       

        if user_number < 1 or user_number > 10:
            print("Please enter number between 1 to 10!")
            continue
        attempts += 1

        if user_number == secret_number:
            print("Congratulation! You win!")
            break
               
        else:
            print("Incorrect guess! Try again!")

        if attempts == 3:
            print("Game Over: The number was:",secret_number)

    except ValueError:
        print("Please enter a valid number!")
