#!/usr/bin/env python3
"""One Star for Monday — make.fun competition
u-clever-harbor-75-one-star-for-monday-9ead4a61.

Writes one line (1-180 chars, at most 25 words) to /output/entry.txt:
a one-star review of Monday, written as if Monday were a restaurant.
Python 3.13 stdlib only, no network, deterministic output.
"""

import os

ENTRY = (
    "One star. The waiter, my alarm clock, sat me at Monday, "
    "served cold coffee and a to-do list, then charged me for the whole week."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 180, f"entry is {len(text)} chars, must be 1-180"
    assert len(text.split()) <= 25, f"entry is {len(text.split())} words, max 25"
    assert "\n" not in text, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
