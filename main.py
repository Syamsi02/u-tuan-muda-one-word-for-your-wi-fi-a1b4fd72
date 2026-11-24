#!/usr/bin/env python3
"""One Word for Your Wi-Fi: the entry program.

Writes a single word to the output file the harness grades,
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (``/output/entry.txt`` in the sandbox).

The word is "Laggy": the adjective everyone already groans about home
Wi-Fi. The video freezes, the call stutters, the page hangs halfway --
lag is the one Wi-Fi complaint every household recognises at once, so
the word is funny the moment you read it and true to how home Wi-Fi
actually behaves. Pure standard library, deterministic: the same five
bytes on every run, no network, no randomness, no input.
"""

import os
from pathlib import Path

WORD = "Laggy"

MIN_LENGTH = 1
MAX_LENGTH = 20


def choose_word() -> str:
    """Return the entry word, checked against the gate's shape rules."""
    word = WORD.strip()
    if not MIN_LENGTH <= len(word) <= MAX_LENGTH:
        raise ValueError("entry word must be 1 to 20 characters")
    if len(word.split()) != 1:
        raise ValueError("entry must be a single word")
    if not word.isalpha():
        raise ValueError("entry word must be plain letters")
    return word


def output_path() -> Path:
    """Where the harness collects the entry text."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(base) / "entry.txt"


def main() -> int:
    word = choose_word()
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(word, encoding="utf-8")  # exactly the word, no newline:
    # the gate counts characters, and a trailing newline would be judged
    # as part of the entry text.
    print(f"Wrote {len(word)}-character entry to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
