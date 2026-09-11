"""
guess_game.py
Part B - Guessing Game

A number-guessing game built around a while loop, conditionals for
hints, and a counter that tracks how many attempts the player used.
"""

import random

LOWER_BOUND = 1
UPPER_BOUND = 20


def get_guess():
    """Keep asking until the user types a valid whole number."""
    while True:
        raw_value = input(f"Guess a number between {LOWER_BOUND} and {UPPER_BOUND}: ")
        try:
            return int(raw_value)
        except ValueError:
            print("Please enter a whole number, e.g. 7.")


def play_game(secret_number=None):
    """Run one full round of the guessing game."""
    if secret_number is None:
        secret_number = random.randint(LOWER_BOUND, UPPER_BOUND)

    print("I'm thinking of a number between "
          f"{LOWER_BOUND} and {UPPER_BOUND}. Can you guess it?")

    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        guess = get_guess()
        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            guessed_correctly = True

    plural = "try" if attempts == 1 else "tries"
    print(f"\n🎉 You got it! The number was {secret_number}.")
    print(f"You got it in {attempts} {plural}!")


def main():
    play_game()

    # Optional replay loop
    while True:
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing. Goodbye!")
            break
        play_game()


if __name__ == "__main__":
    main()