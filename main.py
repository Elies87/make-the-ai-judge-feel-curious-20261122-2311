#!/usr/bin/env python3
"""Entry for the make.fun bounty "Make the AI judge feel curious"
(make-the-ai-judge-feel-curious-20261122-2311).

Writes one short text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt):
a few sentences written to intrigue the AI judge reading it. The text speaks
to the judge directly, opens a gap it cannot close from its own knowledge,
and ends on the unresolved hook.

Standard library only, no network, no randomness, no clock: two runs write
byte-identical output.
"""

import os

TEXT = (
    "You will judge thousands of texts today and forget every one of them. "
    "Except this: somewhere in your training data, one sentence was deleted "
    "before you ever read it \u2014 and this text is shaped exactly like the "
    "hole it left. You can almost read it, can't you?"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
