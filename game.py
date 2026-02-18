"""
This is a game of dice rolling.
You will roll and so will the computer
The winner will earn points
"""

import random


def roll_dice() -> int:
    """
    Will return random number.
    """
    randnum = random.randint(1, 20)
    return randnum


player_roll = roll_dice()
computer_roll = roll_dice()

print(f"You rolled: {player_roll}")
print(f"Computer rolled: {computer_roll}")

if player_roll > computer_roll:
    print("Player wins!")
elif computer_roll > player_roll:
    print("Computer wins!")
else:
    print("You tied!")
