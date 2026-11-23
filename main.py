#!/usr/bin/env python3
"""One Letter for Your Day (make.fun bounty u-puan-one-letter-for-your-day-e54e9c36).

The entry is exactly one letter: Z, for "zero sleep".
Standard library only; no arguments; deterministic.
"""

import os

LETTER = "Z"


def main():
    # The brief: exactly one character, A-Z, and nothing else.
    assert len(LETTER) == 1 and LETTER.isalpha() and LETTER.isupper(), \
        "entry must be exactly one uppercase letter"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LETTER)
    print(LETTER)


if __name__ == "__main__":
    main()
