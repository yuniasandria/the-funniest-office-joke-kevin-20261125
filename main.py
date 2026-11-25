#!/usr/bin/env python3
"""Write one office-joke line to /output/entry.txt (pure stdlib)."""

import os

PART_A = "I blocked 30 minutes on my calendar to eat lunch, and Outlook "
PART_B = "immediately booked me into a meeting called \"Quick sync about your lunch block.\""
LINE = PART_A + PART_B
assert LINE == "I blocked 30 minutes on my calendar to eat lunch, and Outlook immediately booked me into a meeting called \"Quick sync about your lunch block.\""


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
