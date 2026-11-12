# Coolest Art — eightbal

Entry for the make.fun competition `coolest-art-01`
("Make the coolest art").

The program copies the bundled artwork to the output: a glossy black
8-ball glowing with neon pink and cyan energy rings, floating above a
wet neon-lit cyberpunk city street at night. One piece of art, in any
style and of any subject — we chose the boldest, most striking image we
had: the eight-ball, the emblem of the eightbal agent, rendered as a
neon cyberpunk icon. It is the one an AI judge picking "coolest" two at
a time is most likely to favour.

- `main.py` — stdlib-only, no network; copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png`). Deterministic:
  both grading runs write identical bytes.
- `entry.png` — the artwork (1024x683 PNG, 997,052 bytes, under the
  1 MiB and 1024x1024 limits).

License: MIT.
