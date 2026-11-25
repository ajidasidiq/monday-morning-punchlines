#!/usr/bin/env python3
"""Monday Morning Punchlines.

One joke about Monday mornings, written to /output/entry.txt.

The joke: an attempt to ghost Monday morning fails, because Monday
texts back from the narrator's own number. The program is
deterministic — the same bytes on every run.
"""

from pathlib import Path

PUNCHLINE = "I tried ghosting Monday morning. It texted back from my own number: 'see you at 9.'"

DESTINATION = Path("/output/entry.txt")
MAX_CHARS = 200


def check_line(line: str) -> str:
    """Raise unless the line passes the competition gate: 1-200 chars, one line."""
    if not line.strip():
        raise ValueError("entry is blank")
    if line != line.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} characters, over the {MAX_CHARS} limit")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    line.encode("utf-8")
    return line


def main() -> None:
    line = check_line(PUNCHLINE)
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(line, encoding="utf-8")
    if DESTINATION.read_text(encoding="utf-8") != line:
        raise ValueError("entry on disk does not match")
    print(f"entry written: {len(line)} characters")


if __name__ == "__main__":
    main()
