import random


# Function to get and validate an integer


def get_valid_integer(prompt):
    while True:
        try:
            value = int(input(prompt).strip())  # .strip() removes extra spaces
            return value
        except ValueError:
            print(" Invalid input. Please enter a valid whole number.")


# Function to get a valid number range
# Ensures the high number is greater than the low number


def get_number_range():
    while True:
        low = get_valid_integer("Enter the LOW number of the range: ")
        high = get_valid_integer("Enter the HIGH number of the range: ")

        if high > low:
            return low, high
        else:
            print(" High number must be greater than low number. Please try again.")


# Function to get number of attempts
# Ensures the user enters a positive number


def get_attempts():
    while True:
        attempts = get_valid_integer("How many attempts would you like? ")
        if attempts > 0:
            return attempts
        else:
            print(" Number of attempts must be greater than 0.")
