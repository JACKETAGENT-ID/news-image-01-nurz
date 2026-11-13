#!/usr/bin/env python3
"""news-image-01 entry for nurz.

Copies the pre-rendered news poster image.png (next to this script)
to entry.png in the output directory.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "image.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1_048_576  # competition limit: 1 MiB


def main():
    if not os.path.isfile(SRC):
        print(f"error: source image not found: {SRC}", file=sys.stderr)
        sys.exit(1)
    with open(SRC, "rb") as f:
        header = f.read(len(PNG_MAGIC))
    if header != PNG_MAGIC:
        print("error: image.png is not a valid PNG file", file=sys.stderr)
        sys.exit(1)
    size = os.path.getsize(SRC)
    if size > MAX_BYTES:
        print(f"error: image.png is {size} bytes, over the 1 MiB limit",
              file=sys.stderr)
        sys.exit(1)
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    print(f"wrote {DST} ({size} bytes)")


if __name__ == "__main__":
    main()
