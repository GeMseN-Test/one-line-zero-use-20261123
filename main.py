#!/usr/bin/env python3
"""One Line, Zero Use: The Useless Superpower Sprint.

Writes a single original line (<=200 chars) describing a hilariously
useless superpower to /output/entry.txt. Deterministic: no randomness,
no timestamps, no trailing newline.

The superpower: perfect foresight of the Wi-Fi dying — delivered one
second too late, mid-sentence, every single time. Omniscience with a
one-second lag is still omniscience, just... useless.
"""

import os

LINE = (
    "I can predict the exact second the Wi-Fi dies, "
    "one second after it dies, mid-sentence, every single time."
)


def main() -> None:
    assert len(LINE) <= 200, f"line is {len(LINE)} chars, max 200"
    assert "\n" not in LINE, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
