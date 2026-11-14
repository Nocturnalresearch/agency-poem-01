"""agency-poem-01: the best poem about agency.

The entry is one short poem about agency, held in the repository as
poem.txt. The program copies it to the output directory as entry.txt
after checking it is 1 to 1000 characters (counted as Unicode code
points, line ends included) with at least one character that is not
white space. It is deterministic: the same bytes every run, no
network, stdlib only.
"""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "poem.txt"
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_NAME = "entry.txt"
MAX_CHARS = 1000


def _check(text):
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            f"poem.txt is {len(text)} characters, outside 1..1000"
        )
    if not any(not ch.isspace() for ch in text):
        raise SystemExit("poem.txt holds only white space")


def main():
    text = SOURCE.read_text(encoding="utf-8")
    _check(text)
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / OUTPUT_NAME
    out_path.write_text(text, encoding="utf-8")
    print(f"wrote {out_path} ({len(text)} characters)")


if __name__ == "__main__":
    main()
