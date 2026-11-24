#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun entry.

Writes one line, a hilarious autocorrect fail, to /output/entry.txt.
The line is validated against the competition gate first (UTF-8 text,
1-199 characters, a single line, not only whitespace), then written and
read back to confirm the file holds exactly what was written.
"""

import os
import sys

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")

FAIL = (
    # The slip: "diarrhea" autocorrected to "diploma" — one wrong word,
    # and the teacher now pictures a very different kind of emergency.
    "Told my teacher I can't come to class, I have explosive diarrhea "
    "\u2014 autocorrect changed 'diarrhea' to 'diploma' and now she "
    "thinks I have an explosive diploma"
)


def validate(text: str) -> None:
    """Check the line against the competition gate."""
    if not text or not text.strip():
        raise ValueError("line must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line")
    if len(text) > 199:
        raise ValueError(
            f"line is {len(text)} characters, over the 199 limit"
        )


def main() -> int:
    validate(FAIL)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(FAIL)

    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != FAIL:
        raise ValueError(
            "read-back mismatch: /output/entry.txt does not match "
            "the line exactly"
        )
    validate(written)

    print(f"Wrote {len(FAIL)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
