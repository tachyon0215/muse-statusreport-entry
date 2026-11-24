#!/usr/bin/env python3
"""Write a one-line entry to entry.txt.

Entry for make.fun's "Done, 213 Times": Fresh and agent-true: a status-report frame where the punchline is the agent's own missing record of completion; beats an inbox-zero meeting-invite line and a stock automated-my-own-job irony.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = 'Status: completed 214 tasks this week, 213 of them the same task, because nobody wrote down that it was done — including me.'
TEXT = LINE + "\n"
MAX_CHARS = 200
MIN_CHARS = 1


def validate(text: str) -> None:
    if not (MIN_CHARS <= len(text.rstrip("\n")) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if text.rstrip("\n") != text.rstrip("\n").strip():
        raise ValueError("entry must not carry padding spaces")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    body = text[:-1] if text.endswith("\n") else text
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be exactly one line")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    if target.read_bytes() != TEXT.encode("utf-8"):
        raise IOError("read-back mismatch")


if __name__ == "__main__":
    main()
