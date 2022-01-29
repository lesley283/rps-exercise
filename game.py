


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#




# ASK FOR USER INPUT
user_choice = input("Please select your choice: 'rock', 'paper', or 'scissors': ")

# test
# print(type(user_choice))

# VALIDATIONS
# convert user input into all lowercase
user_choice = user_choice.lower()

# determine if the user entered a valid choice; quit program if NOT
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

#test
print("Computer choice:", computer_choice)
print(type(computer_choice))






# DETERMINE THE WINNER



# FINAL RESULTS


# BONUS:
# PLAYER NAME
# TESTING
