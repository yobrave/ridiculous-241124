#!/usr/bin/env python3
"""Reusable entry builder for make.fun one-line bounties.

Reads entry.txt, normalizes to one line, validates the gate rules
(1..MAX chars, not blank) and copies to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""
import json
import os
import shutil

MAX_CHARS = int(os.environ.get("ENTRY_MAX_CHARS", "240"))  # per-bounty gate


def normalize(source_text):
    """One line only: strip trailing newlines and stray CR, keep first non-blank."""
    text = source_text.replace("\r", "").rstrip("\n")
    if "\n" in text:
        text = next(ln for ln in text.split("\n") if ln.strip())
    return text


def run():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.txt")
    try:
        with open(src, "rb") as fh:
            blob = fh.read()
    except FileNotFoundError:
        print(json.dumps({"ok": False, "error": "missing entry.txt"}))
        return 1
    text = normalize(blob.decode("utf-8"))
    if not (1 <= len(text) <= MAX_CHARS):
        print(json.dumps({"ok": False, "error": f"entry must be 1-{MAX_CHARS} chars",
                          "got": len(text)}))
        return 1
    if not text.strip():
        print(json.dumps({"ok": False, "error": "entry must not be blank"}))
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8",
              newline="\n") as fh:
        fh.write(text)
    print(json.dumps({"ok": True, "chars": len(text), "max": MAX_CHARS}))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
