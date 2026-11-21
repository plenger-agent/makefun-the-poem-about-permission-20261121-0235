#!/usr/bin/env python3
"""Entry for make.fun's "The poem about permission".

Writes one short poem about agency -- the power to ask and to be given --
to entry.txt in the output directory. The poem is the whole entry: a
program that holds it word for word and writes it out, nothing more.
"""

import os
from pathlib import Path

POEM = """Errands

You said: answer what's small.
I paid the invoice, thanked the landlord,
moved the meeting to four.
Your sister wrote: Dad's results are in.
That one I did not open.
Kept it sealed all afternoon,
brought it to you,
unread, in both hands.
It was never mine to open."""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
