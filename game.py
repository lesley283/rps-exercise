


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#




# ASK FOR USER INPUT
user_choice = input("Please select your choice: 'rock', 'paper', or 'scissors': ")


# VALIDATIONS
# convert user input into all lowercase
user_choice = user_choice.lower()

# determine if the user entered a valid choice and print; quit program if NOT
if user_choice == "rock" or user_choice == "paper" or user_choice == "scissors":
    print("Your choice:", user_choice)
else:
    print("You entered an invalid choice. The program will now terminate.")
    exit()


# COMPUTER CHOICE
# store possible choices into a list
possible_choices = ["rock", "paper", "scissors"]

# simulate computer selection using the random module
import random # loads the module
computer_choice = random.choice(possible_choices)

# print computer choice
print("Computer choice:", computer_choice)


# DETERMINE THE WINNER
# unless in the case of a tie, for each user choice, determine the possible outcomes based on the computer's choice
# using nested if / else if statements
if user_choice == computer_choice:
    winner = "none" # neither player won
elif user_choice == "rock":
    if computer_choice == "paper":
        winner = "computer"
    elif computer_choice == "scissors":
        winner = "user"
elif user_choice == "paper":
    if computer_choice == "rock":
        winner = "user"
    elif computer_choice == "scissors":
        winner = "computer"
elif user_choice == "scissors":
    if computer_choice == "rock":
        winner = "computer"
    elif computer_choice == "paper":
        winner = "user"

# test
print(winner)


# FINAL RESULTS


# BONUS:
# PLAYER NAME
# TESTING
