# Password Generator & My Own Module

A Week 5 Python assignment on using built-in modules (`random`, `string`,
`math`) and building a custom module that gets imported into another file.

## Files

| File | Description |
|---|---|
| `password_generator.py` | Uses `random` and `string` to build a random alphanumeric password; `make_password(length=8)` has a default value and is called once for 8 characters and once for 12. |
| `helpers.py` | A custom module with `tables_needed(people, seats)` (uses `math.ceil` to round up) and `welcome(name)`; guarded by `if __name__ == "__main__":` so its demo line only runs when the file is executed directly. |
| `main.py` | Imports `helpers` and calls both of its functions. |

## Running the programs

```bash
python3 password_generator.py
python3 main.py
python3 helpers.py
```

## Screenshots

See the [`screenshots/`](screenshots) folder:

- `password_generator_run1.png` and `password_generator_run2.png` — two separate runs of `password_generator.py`, showing different random passwords each time.
- `main_run.png` — `main.py` importing `helpers` and printing the welcome message and both table counts.
- `helpers_run.png` — `helpers.py` run on its own, printing only `3` (the `if __name__ == "__main__":` guard keeps this line from appearing when `main.py` imports it).

## Notes

- No file in this project is named `math.py`, `random.py`, or `string.py`, so Python always imports the real standard-library modules instead of shadowing them with a local file.
- `tables_needed()` uses `math.ceil()` rather than plain division, so 10 people at tables of 4 correctly returns 3 tables instead of 2.5 or 2.