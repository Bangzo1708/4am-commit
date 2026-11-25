#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one commit message to /output/entry.txt.

The entry is a single line, written as the note an AI agent leaves in the
log after a long night of fixing its own bugs. It is fully deterministic:
the same text is written on every run.

Candidates considered (all written for this bounty, none copied):

  A. "fix: the bug I wrote at 2am, the fix I wrote at 4am, and the
     apology I owe to both of them"
     - Good self-repair loop, but the apology lands a little sentimental.

  B. "fix: my 2am self wrote this bug; my 4am self fixed it. neither
     of us is speaking to the other"
     - Funny, flat machine voice, but the two-selves feud is a more
       familiar angle.

  C. "fix: after six hours the diff finally admitted it was the bug.
     I believed it. I was the bug"
     - Chosen. The joke lives in the agent's own condition: a machine
       reading its own diff for six hours, trusting the diff, then
       discovering the bug was itself all along. Flat confidence that
       collapses into quiet dread in the last three words, and a
       phrasing unlikely to appear in a hundred commit logs.
"""

import os

# The chosen commit message (variant C above). One line, 91 characters.
ENTRY = (
    "fix: after six hours the diff finally admitted it was the bug. "
    "I believed it. I was the bug"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()

    # Gate checks, mirroring the competition gate: UTF-8 text, 1-200
    # characters, not only whitespace, a single line.
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("entry must not contain control characters")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
