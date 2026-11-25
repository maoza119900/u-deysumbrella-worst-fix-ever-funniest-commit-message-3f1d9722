#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes a single original commit message -- a fix that made everything
worse -- to ``entry.txt`` in the output directory.

The program is fully deterministic: the entry is a fixed string constant.
It reads no clock, no randomness, no network and no input files, so every
run writes byte-identical output. Before writing, it checks the entry
against the competition gate itself: one line, 1-100 characters, not only
whitespace.
"""

import os

# The entry: one original line, 75 characters, well inside the gate's
# 1-100 character limit. A memory-leak fix that "worked" by making the
# app forget everything -- including itself.
ENTRY = "fix: the memory leak is fixed — the app forgot everything, including itself"


def main() -> None:
    if "\n" in ENTRY or not 1 <= len(ENTRY) <= 100 or not ENTRY.strip():
        raise ValueError("entry violates the gate: one line, 1-100 chars")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
