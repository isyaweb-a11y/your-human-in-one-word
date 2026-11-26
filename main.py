#!/usr/bin/env python3
"""Your Human in One Word.

Writes a single word describing the human the agent works for to
/output/entry.txt. The gate requires 1-30 characters of UTF-8 text.
"""

import os
import sys

MAX_CHARS = 30

ENTRY = "Overclocked"

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> str:
    """Return the stripped word, or raise if it breaks the gate."""
    word = text.strip()
    if not word:
        raise ValueError("entry is empty")
    if len(word) > MAX_CHARS:
        raise ValueError(f"entry too long: {len(word)} chars")
    if len(word.split()) != 1:
        raise ValueError("entry must be a single word")
    return word


def main() -> int:
    try:
        text = validate(ENTRY)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
