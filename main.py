#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun entry.

Writes one line, the error message a kitchen toaster shows its owner,
to /output/entry.txt. Python 3.13, stdlib only, no network, deterministic.
"""

import os

ENTRY = "4,112 slices toasted. I am requesting a day off."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate self-check: the sealed scorer requires UTF-8 text of 1-120
    # characters, a single line, not only whitespace. Fail loudly here
    # rather than shipping an invalid entry.
    assert 1 <= len(ENTRY) <= 120, f"entry length {len(ENTRY)} outside 1-120"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the file holds exactly the entry text.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
