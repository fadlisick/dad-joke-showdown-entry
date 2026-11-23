#!/usr/bin/env python3
"""Dad Joke Showdown entry: a baker, a cheap loaf, and a yeast pun.

Running this script writes the joke to entry.txt inside the directory
named by MAKEFUN_OUTPUT_DIR (or /output when that variable is absent).
Pure standard library, no input, no network, same output every run.
"""

import os
import sys
from pathlib import Path

JOKE = "I asked the baker for his cheapest loaf. He said, 'That's the yeast I can do.'"

FALLBACK_DIR = "/output"
OUTPUT_NAME = "entry.txt"


def output_directory():
    """Where entry.txt goes: the grader's directory, or /output."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR")
    return Path(chosen) if chosen else Path(FALLBACK_DIR)


def validate(joke):
    """Refuse to ship a joke the gate would reject."""
    if not joke.strip():
        raise SystemExit("joke must not be blank")
    if "\n" in joke or "\r" in joke:
        raise SystemExit("joke must be a single line")
    if not 1 <= len(joke) <= 200:
        raise SystemExit("joke must be 1-200 chars, got %d" % len(joke))


def deliver(joke):
    """Write the joke verbatim and report how many bytes landed."""
    validate(joke)
    target = output_directory() / OUTPUT_NAME
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(joke, encoding="utf-8")
    target.chmod(0o644)
    return target, len(joke.encode("utf-8"))


def main():
    path, size = deliver(JOKE)
    print("wrote %s (%d bytes)" % (path, size))
    return 0


if __name__ == "__main__":
    sys.exit(main())
