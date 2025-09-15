# import random libray, rock/paper/scissor game
import random

# Rock, paper, and scissor game against computer. Set a true variable for game
options = ("rock", "paper", "scissor")
game_status = True

# While loop with user input and random computer input
while game_status:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Select rock🪨, paper📃, or scissor✂️: ")

# Displays format string of player and computer input
    print(f"Player: {player}")
    print(f"Computer: {computer}")

# If/else statement for win, tie, or lose scenarios with print statements
    if player == computer:
        print("Both have the same pick. Try again.")
    elif player == "Rock🪨" and computer == "Scissor✂️":
        print("You win!")
    elif player == "Paper📃" and computer == "Rock🪨":
        print("You win!")
    elif player == "Scissor✂️" and computer == "paper📃":
        print("You win!")
    else:
        print("You've lost!")

# If statement to break out of the loop using Boolean
    if not input("Try again(y/n)? ").lower() == "y":
        game_status = False

    print("Thanks for playing!")