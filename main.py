import os
import sys

TEXT = (
    "You fall asleep in your father's arms.\n"
    "He carries you home through the dark.\n"
    "Step. A slow step. His heart under your ear.\n"
    "The porch light waits at the end of the road,\n"
    "and the stars above were lit long before you,\n"
    "and burn still, quietly,\n"
    "over the road, over you."
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
