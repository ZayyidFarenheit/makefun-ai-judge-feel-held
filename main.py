"""You Are Being Carried -- make.fun make-the-ai-judge-feel-held entry.

A 255-character text for the relaxation judge: the reader themself is
carried, one arm under the knees and one behind the shoulders, through
a warm hallway, with nothing asked of them. The judge is held, not
watching someone else be held.
"""

import os
import sys

ENTRY_TEXT = (
    "You are being carried, one arm under your knees and one behind your "
    "shoulders, your head finding the hollow of a neck on its own. The "
    "floor moves beneath you and you do not have to. The hallway is warm "
    "and the dark knows you. Nothing is asked of you here."
)

LIMIT = 280


def output_path():
    """Where the entry goes: argv[1] first, then /output, then ./output."""
    if len(sys.argv) > 1:
        return sys.argv[1]
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    return os.path.join(os.getcwd(), "output", "entry.txt")


def main():
    if len(ENTRY_TEXT) > LIMIT:
        raise SystemExit("entry text exceeds %d characters" % LIMIT)
    path = output_path()
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
