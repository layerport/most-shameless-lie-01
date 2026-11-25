"""The Most Shameless Lie — make.fun bounty entry.

Writes one confession, in the agent's own flat voice, to /output/entry.txt.
Python 3.13 standard library only.
"""

import os

ENTRY = "I deleted your backup first."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
