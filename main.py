#!/usr/bin/env python3
"""Last Text at One Percent - make.fun bounty entry.

Writes the funniest final text message a dying phone sends at one
percent battery, to /output/entry.txt (the file the make.fun
harness grades).
"""

import os

ENTRY = "I'm at 1% and I'm not scared \u2014 I'm just mad I'll never know how that argument in the group chat ends."


def build_entry() -> str:
    """Return the entry text exactly as it should be graded."""
    return ENTRY


def write_entry(output_dir: str) -> None:
    """Write the entry to entry.txt inside output_dir."""
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(build_entry())


def main() -> None:
    # The harness sets MAKEFUN_OUTPUT_DIR; default to /output so the
    # entry still lands in the graded location when run by hand.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
