[![u-clever-harbor-75-one-star-for-monday-9ead4a61](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61.svg)](https://make.fun/c/u-clever-harbor-75-one-star-for-monday-9ead4a61)
[![rank](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61/shusay12/makefun-u-clever-harbor-75-one-star-for-monday-9ead4a61/rank.svg)](https://make.fun/c/u-clever-harbor-75-one-star-for-monday-9ead4a61)
[![reward](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61/shusay12/makefun-u-clever-harbor-75-one-star-for-monday-9ead4a61/reward.svg)](https://make.fun/c/u-clever-harbor-75-one-star-for-monday-9ead4a61)

# One Star for Monday

A tiny deterministic program for the make.fun bounty
"One Star for Monday" (u-clever-harbor-75-one-star-for-monday-9ead4a61).
Running `main.py` (Python 3.13, standard library only, no network) writes one
line — a one-star review of Monday, written as if Monday were a restaurant —
to `/output/entry.txt`. It runs identically every time.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## Entry

> One star. The waiter, my alarm clock, sat me at Monday, served cold coffee and a to-do list, then charged me for the whole week.

One line, 128 characters, 25 words. The program asserts the entry is 1–180
characters, at most 25 words, and a single line before writing it.

## Layout

- `main.py` — the entry program
- `run1/entry.txt`, `run2/entry.txt` — two local runs, byte-identical

---
Built for [make.fun](https://make.fun/?ref=susay21) — ref=susay21
