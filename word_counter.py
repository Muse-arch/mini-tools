#!/usr/bin/env python3
"""word_counter.py - count words, characters, and lines in a text file.

Usage:
    python word_counter.py <path-to-file>
"""

import sys
from pathlib import Path


def count_text(text: str) -> dict:
    return {
        "lines": len(text.splitlines()),
        "words": len(text.split()),
        "characters": len(text),
    }


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 1
    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"File not found: {path}")
        return 1
    stats = count_text(path.read_text(encoding="utf-8"))
    for label, value in stats.items():
        print(f"{label}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
