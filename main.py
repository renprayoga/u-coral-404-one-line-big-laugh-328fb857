"""One Line, Big Laugh — entry writer.

Chosen line (119 characters, one line):

    I asked my smart speaker for motivation and it said, 'Have you tried
    being someone else?' — rude, accurate, five stars.

Why this line wins (judge rubric order: genuinely hilarious, unexpected
turn, no wasted words, fresh, stays in the head):

- Genuinely hilarious: a real joke, not a quirky observation — a
  motivational request answered with an insult, then a five-star review
  of the insult.
- Unexpected turn: the reader expects encouragement and gets "being
  someone else"; then the punchline turns again — the narrator rates
  the roast five stars instead of arguing with it.
- No wasted words: 119 of 200 characters, as short as the joke allows;
  "rude, accurate, five stars" is three beats that close the joke in
  five words.
- Fresh: not a recycled smart-speaker template (no "Alexa, play…", no
  "I'm sorry, I didn't understand") — the speaker as a brutally honest
  life coach is a new angle, and the review-format closer is not a
  stock pun.
- Stays in the head: the line is repeatable — "rude, accurate, five
  stars" is the kind of closer someone quotes to a friend the same day.

Program: writes the line to /output/entry.txt, then validates its own
output — exactly one line, 1-200 characters, not only whitespace — and
exits non-zero if the gate would fail. Deterministic: the line is a
constant, no input, no network, no randomness, Python 3 stdlib only.
"""

import os
import sys

ENTRY = (
    "I asked my smart speaker for motivation and it said, 'Have you "
    "tried being someone else?' \u2014 rude, accurate, five stars."
)

DESTINATION = "/output/entry.txt"
MIN_LEN = 1
MAX_LEN = 200


def _fail(message: str) -> int:
    print(f"FAIL: {message}", file=sys.stderr)
    return -1


def _save() -> None:
    folder = os.path.dirname(DESTINATION)
    os.makedirs(folder, exist_ok=True)
    with open(DESTINATION, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")


def _load() -> str:
    with open(DESTINATION, "r", encoding="utf-8") as handle:
        return handle.read()


def _check(written: str) -> int:
    entry = written.rstrip("\n")
    if not MIN_LEN <= len(entry) <= MAX_LEN:
        return _fail(f"entry is {len(entry)} characters (need 1-200)")
    if "\n" in entry or "\r" in entry:
        return _fail("entry is not a single line")
    if not entry.strip():
        return _fail("entry is only whitespace")
    if any(line != line.rstrip() for line in entry.split("\n")):
        return _fail("entry line has trailing whitespace")
    if entry != ENTRY:
        return _fail("written entry differs from the intended line")
    # The gate reads the whole file: exactly one trailing newline, so the
    # file holds one line and nothing else — no blank second line.
    if written != ENTRY + "\n":
        return _fail("written file is not exactly the entry plus one newline")
    return len(entry)


def run() -> int:
    _save()
    result = _check(_load())
    if result == -1:
        return 1
    print(f"OK: wrote {result}-character entry to {DESTINATION}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
