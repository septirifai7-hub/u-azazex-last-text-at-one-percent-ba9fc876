#!/usr/bin/env python3
"""Last Text at One Percent - make.fun bounty entry.

Writes the funniest final text message a dying phone sends at one
percent battery, to /output/entry.txt (the file the make.fun
harness grades).
"""

import os

ENTRY = "I'm at 1% and I'm not scared \u2014 I'm just mad I'll never know how that argument in the group chat ends."

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
