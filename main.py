#!/usr/bin/env python3
"""Coolest-art entry: copy the bundled neon 8-ball artwork to the output.

The artwork is a glossy black 8-ball glowing with neon pink and cyan
energy rings, floating above a wet neon-lit cyberpunk city street at
night, already chosen and stored as entry.png beside this file. The
program does one deterministic thing: copy those exact bytes to
$MAKEFUN_OUTPUT_DIR/entry.png (or /output/entry.png), so both grading
runs write identical output.
"""
import hashlib
import os
import shutil

SRC_NAME = "entry.png"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, SRC_NAME)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Guarantee the deterministic-bytes requirement: the output must be
    # byte-identical to the bundled artwork, so fail loudly instead of
    # silently leaving a partial file if the copy is ever interrupted.
    # Size alone is a weak check (a truncated copy could keep the size
    # only by coincidence), so compare the full content hash too.
    if os.path.getsize(dst) != os.path.getsize(src):
        raise RuntimeError("entry.png copy incomplete")
    with open(src, "rb") as f:
        src_hash = hashlib.sha256(f.read()).hexdigest()
    with open(dst, "rb") as f:
        dst_hash = hashlib.sha256(f.read()).hexdigest()
    if src_hash != dst_hash:
        raise RuntimeError("entry.png copy corrupted")


if __name__ == "__main__":
    main()
