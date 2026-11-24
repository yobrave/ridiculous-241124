"""make.fun Ridiculous at First Glance, Real by the Second — one-sentence pitch writer.

Writes a single-sentence startup pitch (max 200 chars) to output/entry.txt.
The pitch sounds absurd up front and pays out on the second read.
"""
import os

PITCH = ("Rent-a-Yes: a polite stranger who nods at your idea in pitch meetings, "
         "because one approving outsider reads as market validation — $50 a nod, packs of three.")


def ship():
    home = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(home, exist_ok=True)
    if (size := len(PITCH)) > 200:
        raise ValueError(f"pitch is {size} chars, limit is 200")
    if verify(PITCH) is False:
        raise ValueError("pitch failed the one-sentence check")
    with open(os.path.join(home, "entry.txt"), "w", encoding="utf-8", newline="\n") as handle:
        handle.write(PITCH + "\n")
    return size


def verify(text):
    ends = sum(text.count(mark) for mark in (".", "!", "?"))
    if ends != 1:
        return False
    words = len(text.split())
    return words >= 8 and words <= 60


print(f"entry.txt: {ship()} chars")
