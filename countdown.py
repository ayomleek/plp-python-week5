"""
countdown.py
Part A - Countdown

Demonstrates a while loop that counts down to zero, then upgrades
the idea into a reusable, user-driven countdown.
"""


def countdown_from_five():
    """Count down from 5 to 1 using a while loop, then blast off."""
    print("Fixed countdown from 5:")
    number = 5
    while number >= 1:
        print(number)
        number -= 1  # the loop variable MUST change, or this loops forever
    print("Blast off!")


def countdown_from(start):
    """Count down from any starting number the user provides."""
    number = start
    while number >= 1:
        print(number)
        number -= 1
    print("Blast off!")


def get_starting_number():
    """Keep asking until the user provides a whole number >= 1."""
    while True:
        raw_value = input("Enter the number to count down from: ")
        try:
            value = int(raw_value)
        except ValueError:
            print("That's not a whole number. Please try again.")
            continue

        if value < 1:
            print("Please enter a number that is 1 or greater.")
            continue

        return value


def main():
    # Step 1 & 2: the required fixed 5-to-1 countdown
    countdown_from_five()

    print()  # blank line for readability

    # Step 3: the upgraded, user-driven countdown
    start = get_starting_number()
    print(f"\nCounting down from {start}:")
    countdown_from(start)


if __name__ == "__main__":
    main()