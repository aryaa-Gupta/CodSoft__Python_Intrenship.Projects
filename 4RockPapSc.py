# TASK 4

# User input to select Rock/Paper/Scissors , Computer random choice for one of the three
# Display Result - win/ lose /tie , Score Tracking for multiple rounds
# Ask to play again yes/ no ?
# I have designed it user friendly with clear instructions and also included ASCII arts .
import random

print("-- Welcome to ROCK, PAPER, SCISSORS Game --")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = 1
user_win = 0
computer_win = 0

while user_choice == 1:

    user_choice = int(input("What do you want to choose ? \n Type 0 for Rock, 1 for Paper or 2 for Scissors -> \n"))

    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number, you lose!")
    else:
        print(game_images[user_choice])

        computer_choice = random.randint(0, 2)
        print("Computer chose :")
        print(game_images[computer_choice])

        if user_choice == 0 and computer_choice == 2:
            print("You WIN!")
            user_win += 1
            print("Your Score : ", user_win)
            print("Computer Score : ", computer_win)

        elif computer_choice == 0 and user_choice == 2:
            print("You LOSE")
            computer_win += 1
            print("Your Score : ", user_win)
            print("Computer Score : ", computer_win)

        elif computer_choice > user_choice:
            print("You LOSE")
            computer_win += 1
            print("Your Score : ", user_win)
            print("Computer Score : ", computer_win)

        elif user_choice > computer_choice:
            print("You WIN")
            user_win += 1
            print("Your Score : ", user_win)
            print("Computer Score : ", computer_win)

        elif computer_choice == user_choice:
            print("It's a DRAW")
            print("Your Score : ", user_win)
            print("Computer Score : ", computer_win)

    ch = input("Do you want to continue game ? (yes/no)")
      # choice for continuing
    if ch == "yes":
        user_choice = 1
    else:
        break

