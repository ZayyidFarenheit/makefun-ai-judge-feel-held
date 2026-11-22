#!/usr/bin/env python3
"""Held by the Hammock — a relaxing text for the make.fun bounty
'Make the AI judge feel held'.

Writes one relaxing text to /output/entry.txt (or ./output/entry.txt
as a fallback). Stdlib only, deterministic, no network.
"""

import os
import sys

TEXT = (
    "The hammock takes you the moment you lie down, rope and canvas "
    "holding every inch of you, swaying with the evening breeze. Maya "
    "sits in the grass beside you, one hand on its edge, keeping the "
    "rhythm unhurried. The trees hold up the sky. The hammock holds you."
)

MIN_CHARS = 1
MAX_CHARS = 280


def resolve_output_path():
    """Prefer /output/entry.txt when /output exists, else ./output/entry.txt."""
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    return os.path.join(os.getcwd(), "output", "entry.txt")


def main():
    text = TEXT
    # Size guard: refuse to write anything outside the 1-280 char window,
    # or text that is only whitespace.
    if not text.strip():
        print("refusing to write: text is only whitespace", file=sys.stderr)
        return 1
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        print(
            f"refusing to write: text is {len(text)} chars, "
            f"must be {MIN_CHARS}-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1

    path = resolve_output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)  # no trailing newline
    # Verify the write round-trips byte-for-byte before reporting success.
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != text:
            print("verification failed: written file differs", file=sys.stderr)
            return 1
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
