#!/usr/bin/env python3
"""Validate GRHS release data and canonical source consistency."""

from __future__ import annotations

import csv
import json
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def cps(text: str) -> str:
    return " ".join(f"U+{ord(char):04X}" for char in text)


def names(text: str) -> str:
    return " + ".join(unicodedata.name(char) for char in text)


def require(condition: bool, message: str) -> None:
    """Fail release validation even when Python assertions are optimized out."""
    if not condition:
        raise ValueError(message)


def main() -> None:
    required = [
        ROOT / "README.md",
        ROOT / "SPECIFICATION.md",
        ROOT / "CHANGELOG.md",
        ROOT / "LICENSE",
        ROOT / "LICENSE-NOTICE.md",
        ROOT / "SHA256SUMS",
        ROOT / "data" / "repertoire.csv",
        ROOT / "tests" / "normalization.json",
    ]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
    require(not missing, f"missing release files: {missing}")

    spec = (ROOT / "SPECIFICATION.md").read_text(encoding="utf-8")
    require("Version | 0.4.0" in spec, "specification version marker is missing")
    require("AGPL-3.0-only" in spec, "specification license marker is missing")
    require("Dotless `ı` is not GRHS" in spec, "dotless-i exclusion is missing")

    seen_ids: set[str] = set()
    seen_graphemes: set[str] = set()
    with (ROOT / "data" / "repertoire.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    require(len(rows) == 51, f"expected 51 repertoire rows, got {len(rows)}")
    for row in rows:
        identifier = row["id"]
        grapheme = row["grapheme"]
        require(identifier not in seen_ids, f"duplicate ID: {identifier}")
        require(grapheme not in seen_graphemes, f"duplicate grapheme: {grapheme}")
        seen_ids.add(identifier)
        seen_graphemes.add(grapheme)
        require(
            grapheme == unicodedata.normalize("NFC", grapheme),
            f"not NFC: {identifier}",
        )
        require(row["codepoints"] == cps(grapheme), f"code-point mismatch: {identifier}")
        require(
            row["unicode_names"] == names(grapheme),
            f"Unicode-name mismatch: {identifier}",
        )
        require(
            row["nfd_codepoints"] == cps(unicodedata.normalize("NFD", grapheme)),
            f"NFD code-point mismatch: {identifier}",
        )

    vectors = json.loads((ROOT / "tests" / "normalization.json").read_text(encoding="utf-8"))
    require(
        vectors["specification_version"] == "0.4.0",
        "normalization fixture version mismatch",
    )
    for vector in vectors["canonical_equivalence"]:
        actual = unicodedata.normalize("NFC", vector["input"])
        require(actual == vector["output"], f"normalization mismatch: {vector!r}; got {actual!r}")

    print(f"RELEASE_VALID rows={len(rows)} normalization_vectors={len(vectors['canonical_equivalence'])}")


if __name__ == "__main__":
    main()

