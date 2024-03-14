# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if user_choice.lower() in options:
    print("Computer chose:", computer_choice)

    # Determine the winner
    if user_choice.lower() == computer_choice:
        print("It's a tie!")
    elif (user_choice.lower() == "r" and computer_choice == "s") or \
         (user_choice.lower() == "p" and computer_choice == "r") or \
         (user_choice.lower() == "s" and computer_choice == "p"):
        print("You win!")
    else:
        print("You lose!")
else:
    print("Invalid choice. Please choose from (r)ock, (p)aper, or (s)cissors.")