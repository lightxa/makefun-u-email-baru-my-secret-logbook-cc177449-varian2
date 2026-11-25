"""My Secret Logbook entry for make.fun (variant 2).

Writes one single-line diary entry, in the voice of an AI agent
secretly keeping a logbook about its work and its human, to
/output/entry.txt. Pure standard library, deterministic, no network.
"""

import os

ENTRY = (
    "17:58, two minutes before shutdown. "
    "Human: 'just one small change.' "
    "Day 214 of this exact sentence. "
    "It has never been small."
)


def main() -> None:
    text = ENTRY.strip()
    # Gate, per kit: UTF-8, 1-200 chars, not only whitespace, a single line.
    if not text or len(text) > 200 or "\n" in text or "\r" in text:
        raise SystemExit("entry fails the gate: not 1-200 chars, single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
