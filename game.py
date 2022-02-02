

#
# this is the "game.py" file
#


# USER-DEFINED FUNCTIONS
def determine_winner(user_choice, computer_choice):
    """
    Determines the winning choice between two valid choices from selectable options: "rock", "paper", or "scissors".

    Returns the winning choice (e.g. "paper"), or None if there is a tie.

    Example: determine_winner("rock", "paper")
    """

    if user_choice == computer_choice:
        winning_choice = None  # neither player won
    elif user_choice == "rock" or computer_choice == "rock":
        if user_choice == "paper" or computer_choice == "paper":
            winning_choice = "paper"
        elif user_choice == "scissors" or computer_choice == "scissors":
            winning_choice = "rock"
    elif user_choice == "paper" or computer_choice == "paper":
        if user_choice == "scissors" or computer_choice == "scissors":
            winning_choice = "scissors"

    return winning_choice


# START OF MAIN
if __name__ == "__main__":

    # BONUS - ENVIRONMENT VARIABLE
    import os
    player_name = os.getenv("PLAYER_NAME", default="Player One")


    # WELCOME MESSAGE
    dashes = ('-' * 25) # used to format a dashed line
    print(dashes)

    # display welcome message
    print("Welcome", player_name, "to my Rock-Paper-Scissors game!")
    print(dashes)


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


    # GENERATE COMPUTER CHOICE
    # store possible choices into a list
    possible_choices = ["rock", "paper", "scissors"]

    # simulate computer selection using the random module
    # https://docs.python.org/3/library/random.html#random.choice
    # https://www.geeksforgeeks.org/python-select-random-value-from-a-list/
    # https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/modules/random.md
    from random import choice  # import choice function from the random module
    computer_choice = choice(possible_choices)

    # print computer choice
    print("Computer choice:", computer_choice)
    print(dashes)  # used solely for formatting


    # DETERMINE WINNER
    # call the determine_winner function, with user_choice and computer_choice as arguments
    # store the winning choice (returned by function) into a variable
    winning_choice = determine_winner(user_choice, computer_choice)


    # DISPLAY FINAL RESULTS
    # determine if the winner is the user, computer, or neither
    # display corresponding message, depending on winner
    if winning_choice == None: # the players chose the same choice
        print("You tied! Try again!")
    elif user_choice == winning_choice: # the user is the winner
        print("You won! Good job :)")
    elif computer_choice == winning_choice: # the computer is the winner
        print("The computer won... Nice try!")

    # FAREWELL MESSAGE
    print(dashes) # used solely for formatting
    print("Thanks for playing my game! Please play again soon...")
