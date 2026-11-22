import os
import sys

TEXT = (
    "You are being carried, one arm under your knees and one behind "
    "your shoulders, your head finding the hollow of a neck on its own. "
    "The floor moves beneath you and you do not have to. "
    "The hallway is warm and the dark knows you. "
    "Nothing is asked of you here."
)


MAX_CHARS = 280


def resolve_output_path():
    if len(sys.argv) > 1:
        return sys.argv[1]
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    return os.path.join(os.getcwd(), "output", "entry.txt")


def main():
    if len(TEXT) > MAX_CHARS:
        raise ValueError("entry text exceeds %d characters" % MAX_CHARS)
    out_path = resolve_output_path()
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
