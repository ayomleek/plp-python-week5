"""
helpers.py
Question 2 - Your Own Module (Part 1)

A small module of reusable helper functions, meant to be imported
by other scripts such as main.py.
"""

import math


def tables_needed(people, seats):
    """Return how many tables are needed, rounded UP.

    e.g. 10 people at tables of 4 need 3 tables (not 2.5, not 2).
    """
    return math.ceil(people / seats)


def welcome(name):
    """Return a friendly welcome message for the given name."""
    return f"Welcome to PLP, {name}!"


if __name__ == "__main__":
    # This block only runs when helpers.py is executed directly,
    # NOT when it is imported by another file like main.py.
    print(tables_needed(10, 4))