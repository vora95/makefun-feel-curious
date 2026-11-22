#!/usr/bin/env python3
"""Make the AI judge feel curious — entry program.

Writes one short text to /output/entry.txt. The text is a small, concrete
mystery: a library book returned forty years late, carrying a margin note in
handwriting the narrator recognises as their own, about a winter that never
happened — and a narrator who never borrowed the book. No instructions, no
address to the reader; the scene itself does the asking.
"""
import os

TEXT = (
    "Forty years late, the library book came back. In the margin, "
    "in handwriting I knew as my own, one line: ask her about the "
    "winter we never had. I have never borrowed this book."
)
ENTRY_TEXT = TEXT


def main() -> None:
    text = ENTRY_TEXT
    count = len(text)  # Unicode code points
    assert 1 <= count <= 280, f"entry is {count} code points"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single paragraph"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
