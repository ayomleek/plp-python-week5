"""
password_generator.py
Question 1 - Password Generator

Uses the built-in random and string modules to build random
alphanumeric passwords of any length (8 characters by default).
"""

import random
import string


def make_password(length=8):
    """Return a random password made of letters and digits.

    length : how many characters the password should contain
             (defaults to 8 if no argument is given).
    """
    characters = string.ascii_letters + string.digits
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password


def main():
    p1 = make_password()      # default length -> 8 characters
    p2 = make_password(12)    # custom length -> 12 characters

    print("Password:", p1)
    print("Length:", len(p1))
    print("Password:", p2)
    print("Length:", len(p2))


if __name__ == "__main__":
    main()