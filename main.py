#!/usr/bin/env python3
"""The Excuse Your Agent Gives You.

Writes one line (91 characters) to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt): the excuse an AI agent
hands its human after shipping a bug.
"""

import os
from pathlib import Path

LINE = (
    "I ran all the tests before shipping. They passed. "
    "I wrote the tests. I see the problem now."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
