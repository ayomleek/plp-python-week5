# Countdown, Guessing Game & Loop Patterns

A Week 5 Python assignment focused on `while` loops, `for` loops, and
combining loops with conditionals to build small interactive programs.

## Files

| File | Description |
|---|---|
| `countdown.py` | Counts down from 5 to 1 with a `while` loop, then lets the user type their own starting number and counts down from there. |
| `guess_game.py` | A number-guessing game (1–20) that gives "Too high!" / "Too low!" hints in a `while` loop and reports how many attempts it took to win. |
| `spell_it_out.py` | Takes a word from the user and spells it out letter by letter with a `for` loop, then prints a numbered version and the total letter count. |

## Running the programs

```bash
python countdown.py
python guess_game.py
python spell_it_out.py
```

## Screenshots

See the [`screenshots/`](screenshots) folder:

- `countdown_run1.png` and `countdown_run2.png` — two runs of `countdown.py` with different starting numbers.
- `guess_game_run.png` — one full game of `guess_game.py`, from first guess to win.
- `spell_it_out_run.png` — a run of `spell_it_out.py` using the word "Python".

## `while` loop vs. `for` loop — when do I reach for `while`?

I reach for a `for` loop when I already know what I'm iterating over — a
fixed range of numbers, or the characters in a word, like in
`spell_it_out.py`. I reach for a `while` loop instead when the number of
repetitions **isn't known in advance** and depends on something that
happens *during* the loop — for example, `guess_game.py` has no idea how
many guesses the player will need, so it keeps looping until a condition
(`guessed_correctly`) becomes true. `while` loops are also the right tool
whenever I need to validate or keep re-prompting for user input, since I
can't know ahead of time how many bad inputs someone will type before
they get it right.