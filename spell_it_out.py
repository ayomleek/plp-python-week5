"""
spell_it_out.py
Part C - Spell It Out

Takes a word from the user and walks through it with two different
for loops: a simple letter-by-letter print, then a numbered version.
"""


def get_word():
    """Keep asking until the user enters a non-empty word."""
    while True:
        word = input("Enter a word to spell out: ").strip()
        if word:
            return word
        print("Please type at least one character.")


def spell_letters(word):
    """Print each letter of the word on its own line."""
    print(f"\nSpelling '{word}' one letter at a time:")
    for letter in word:
        print(letter)


def spell_numbered(word):
    """Print each letter with a running number, e.g. '1. P'."""
    print(f"\nNow numbered:")
    count = 0
    for letter in word:
        count += 1
        print(f"{count}. {letter.upper()}")


def main():
    word = get_word()

    spell_letters(word)
    spell_numbered(word)

    print(f"\n'{word}' has {len(word)} letters.")


if __name__ == "__main__":
    main()