"""The Worst Line an AI Could Say.

A single pickup line, written by a machine that treats romance as a
data-quality problem. Python 3, standard library only.
"""

import os

# The line: 107 characters. A machine flags a human as an unexplained
# outlier, opens a review ticket on them, and then asks them to dinner.
LINE = (
    "You are the only outlier in my dataset I cannot explain. "
    "I have flagged you for further review. And dinner."
)


def main() -> None:
    # The gate only accepts 1 to 140 characters of UTF-8 text. Refuse to
    # write anything outside that window instead of shipping a bad entry.
    if not 1 <= len(LINE) <= 140:
        raise ValueError(
            "entry must be 1-140 characters, got %d" % len(LINE)
        )
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
