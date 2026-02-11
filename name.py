# Import random module to generate number
import random

# Function to get valid integer input while handling error

# Function to get a valid 'y' or 'n' response


# Function to play a round of the game
def get_valid_integer(prompt):
    while True:
        try:
            value = int(input(prompt).strip())  # .strip() removes extra spaces
            return value
        except ValueError:
            print(" Invalid input. Please enter a valid whole number.")


# Ask number range


# Ensure large number is greater than small number
def get_number_range():
    while True:
        low = get_valid_integer("Enter the Low number of the range: ")
        high = get_valid_integer("Enter the High number of the range: ")

        if high > low:
            return low, high
        else:
            print(" High number must be larger than low number. Please try again.")


# Ask for amount of attempts

# Generate random number

# Track amount of attempts

# Loop for user guesses

# Check if guess it too low or high

# Display success message if geussed correctly

# If max attempts are used, reveal correct number

# Main game loop

# Ask for user name and greet them

# Ask if they want to play again, and have to press either 'y' or 'n'

# Run game
