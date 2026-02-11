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
        low = get_valid_integer("Enter the Low number of the range: ")
        high = get_valid_integer("Enter the High number of the range: ")

        if high > low:
            return low, high
        else:
            print(" High number must be greater than low number. Please try again.")


# Function to get number of attempts
# Make sure user uses a positive number


def get_attempts():
    while True:
        attempts = get_valid_integer("How many attempts would you like? ")
        if attempts > 0:
            return attempts
        else:
            print(" Number of attempts must be greater than 0.")


# Function to play one round of the game


def play_game(name):
    print(f"\nAlright {name}, let's set up your game!")

    low, high = get_number_range()
    attempts_allowed = get_attempts()

    # Generate random number within selected range
    secret_number = random.randint(low, high)

    print(f"\nI have chosen a number between {low} and {high}.")
    print(f"You have {attempts_allowed} attempts to guess it!")

    attempts_used = 0

    # Loop until attempts run out
    while attempts_used < attempts_allowed:
        guess = get_valid_integer("\nEnter your guess: ")
        attempts_used += 1

        if guess < secret_number:
            print(" Too low!")
        elif guess > secret_number:
            print(" Too high!")
        else:
            print(
                f" Congratulations! {name}! You guessed the number in {attempts_used} attempts!"
            )
            return  # End the game round if guessed correctly

        print(f"Attempts used: {attempts_used}/{attempts_allowed}")

    # If loop ends, user ran out of attempts
    print(f"\n Sorry {name}, you've used all your attempts.")
    print(f"The correct number was: {secret_number}")


# Function to ask if the user wants to play again
# Only accepts 'y' or 'n'


def play_again():
    while True:
        choice = input("\nWould you like to play again? (y/n): ").strip().lower()

        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print(" Please enter only 'y' or 'n'.")


# Main function to control the program flow


def main():
    print(" Welcome to the Number Guessing Game!")

    # Ask for user's name and greet them
    name = input("What is your name? ").strip()
    print(f"Hello, {name}! Nice to meet you.")

    # Main game loop
    while True:
        play_game(name)

        if not play_again():
            print(f"\nThanks for playing, {name}! Goodbye ")
            break


# Run the program
if __name__ == "__main__":
    main()
