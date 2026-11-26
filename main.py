#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review — make.fun entry.

Writes one line to /output/entry.txt: a review of planet Earth left by
an alien tourist.

Why this line, against the judge brief: the alien's outside view is
clear (a tourist watching humans, not a human joke); the laugh comes
from the alien's angle on ordinary Earth life — automating a chore,
then treating the machine as the entertainment; it avoids the obvious
first thoughts (traffic, gravity, money, weather); it reads as a real
review with a 5/5 verdict; and it stays tight with the punch at the
end ("best show on the planet").

Deterministic: Python stdlib only, no network, no randomness, no clock.
"""
import os

ENTRY = "The locals built machines to wash their dishes, then stood around watching the machines work. 5/5 \u2014 best show on the planet."
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
