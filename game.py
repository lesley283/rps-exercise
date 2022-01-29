


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

if user_choice == "rock" or user_choice == "paper" or user_choice == "scissors":
    print("Your choice:", user_choice)
else:
    print("You entered an invalid choice. The program will now terminate.")
    exit()


# COMPUTER CHOICE



# DETERMINE THE WINNER



# FINAL RESULTS


# BONUS:
# PLAYER NAME
# TESTING
