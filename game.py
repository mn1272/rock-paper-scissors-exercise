import random

print("Welcome 'Plaayer One' to my Rock Paper Scissors Game.....")

# user inputs

you = input("Please choose either ('rock','paper','scissors'):")
you = you.lower()
## print ("you chose:", you)
print (f"you chose: '{you}' ")

# valid user inputs
valid_options = ["rock","paper","scissors"]
computer_choice = random.choice(valid_options)
#breakpoint()
if you not in valid_options: 
    print("Oops Invalid Try Again") 
    exit()

# computer choice



# import random


print (f"Computer Chose:: '{computer_choice}' ")


# determine the winner, code adapted from shared in slack by Bonnie

if you == computer_choice: print("It's a tie!")
elif you == "rock": 
    if computer_choice == "scissors": print("Rock crushes scissors. You win! Thanks for playing. Please play again!")
    else: print("Paper covers rock. You lose! Thanks for playing. Please play again!")
elif you == "paper":
    if computer_choice == "rock": print ("Paper covers rock. You win! Thanks for playing. Please play again!")
    else: print("Scissors cuts paper. You lose! Thanks for playing. Please play again!")
elif you == "scissors":
    if computer_choice == "paper": print ("Scissors cuts paper. You win! Thanks for playing. Please play again!")
    else: print("Rock crushes scissors. You lose! Thanks for playing. Please play again!")



# display results
# 
# -------------------
# Welcome 'Player One' to my Rock-Paper-Scissors game...
# -------------------
# Please choose either 'rock', 'paper', or 'scissors': rock
# You chose: 'rock'
# The computer chose: 'paper'
# -------------------
# Oh, the computer won. It's ok.
# -------------------
# Thanks for playing. Please play again!

