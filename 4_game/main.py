"""
1 for snake 
-1 for water
0 for gun

game rules:
Snake vs. Water: Snake drinks water, so it wins.
Water vs Gun: The gun will sink in water, so it’s a point for water.
Snake vs. Gun: The gun will win because it will kill the snake.
If both players choose the same object, the game will end in a tie.
"""

# Importing the random module to generate a random choice for the computer
import random

# Define the set of numbers corresponding to the choices: -1 (water), 0 (gun), 1 (snake)
numbers = [-1, 0, 1]

# Generate a random number for the computer's choice using random.choice()
# This simulates the computer randomly picking one of the three options
computer = random.choice(numbers)

# Prompt the user to input their choice: 's' for snake, 'w' for water, 'g' for gun
print("write _s_ for snake, _w_ for water, and _g_ for gun")
youstr = input("enter your choice: ")

# A dictionary to map the user's string input ('s', 'w', 'g') to numerical values (-1, 0, 1)
youDict = {"s": 1, "w": -1, "g": 0}

# A reverse dictionary to map numerical values back to their string representations
reverseDict = {1: "snake", -1: "water", 0: "gun"}

# Convert the user's input into a numerical value using the youDict dictionary
you = youDict[youstr]

# Print the choices made by the user and the computer in a human-readable format
print(f"you chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

# Check if the game is a tie (both the user and the computer chose the same option)
if (computer == you):
    print("tie")  # If both choices are the same, it's a tie

# If it's not a tie, evaluate the winner based on the game rules
else:
    # Case 1: Computer chose water (-1) and you chose snake (1)
    # Snake drinks water, so you win
    if (computer == -1 and you == 1):
        print("you win")

    # Case 2: Computer chose water (-1) and you chose gun (0)
    # Gun sinks in water, so you lose
    elif (computer == -1 and you == 0):
        print("you lose")

    # Case 3: Computer chose snake (1) and you chose water (-1)
    # Snake drinks water, so you lose
    elif (computer == 1 and you == -1):
        print("you lose")

    # Case 4: Computer chose snake (1) and you chose gun (0)
    # Gun kills snake, so you win
    elif (computer == 1 and you == 0):
        print("you win")

    # Case 5: Computer chose gun (0) and you chose water (-1)
    # Gun sinks in water, so you win
    elif (computer == 0 and you == -1):
        print("you win")

    # Case 6: Computer chose gun (0) and you chose snake (1)
    # Gun kills snake, so you lose
    elif (computer == 0 and you == 1):
        print("you lose")

    # Default case: If none of the above conditions are met, something went wrong
    else:
        print("wrong")