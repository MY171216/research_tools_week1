"""Count the ten most frequent words in a text file."""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path


def count_words(text: str) -> Counter[str]:
    """Return case-insensitive word counts, excluding punctuation."""
    words = re.findall(r"[\w']+", text.lower(), flags=re.UNICODE)
    return Counter(words)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Print the ten most frequent words in a text file."
    )
    parser.add_argument("text_file", type=Path, help="path to the text file to analyse")
    args = parser.parse_args()

    try:
        text = args.text_file.read_text(encoding="utf-8")
    except FileNotFoundError:
        parser.error(f"file not found: {args.text_file}")
    except UnicodeDecodeError:
        parser.error(f"cannot decode as UTF-8: {args.text_file}")

    counts = count_words(text)
    for word, count in sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:10]:
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
