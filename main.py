#!/usr/bin/env python3
"""Error message from a toaster that has toasted enough.

A small program for make.fun's "The Funniest Toaster Error Message":
after thousands of slices, the toaster files a polite request for
a day off. Python 3.13, stdlib only, no network, deterministic.
"""

import os

ENTRY = "4,112 slices toasted. I am requesting a day off."

OUTPUT_PATH = "/output/entry.txt"


def check_entry(text):
    """Refuse to ship an entry the sealed scorer would reject."""
    assert 1 <= len(text) <= 120, "entry length outside 1-120"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert text.strip(), "entry must not be only whitespace"


def main():
    check_entry(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Exact bytes only: the entry text, with no trailing newline added.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
