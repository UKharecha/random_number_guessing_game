# This is a random number guessing game between computer and the user.
import random


def ask_user():
    while True:
        computer_num = str(random.randint(1, 20))
        user_input = str(input("Please choose a number between 1-20\n"))
        if user_input == computer_num:
            print(f"Computer choose {computer_num} and you choose {user_input}. Congratulations! you win")
            break
        else:
            print(f"Computer choose {computer_num} and you choose {user_input}. Try again.")


ask_user()
