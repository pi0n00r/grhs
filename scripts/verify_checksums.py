#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Gary Bajaj
# SPDX-License-Identifier: AGPL-3.0-only

"""Verify the immutable release artifacts listed in SHA256SUMS."""

from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "SHA256SUMS"
REQUIRED_ARTIFACTS = {
    "SPECIFICATION.md",
    "data/repertoire.csv",
    "tests/normalization.json",
    "GRHS-v0.4.0.docx",
    "GRHS-v0.4.0.pdf",
    "archive/v0.3/GRHS-v0.3.docx",
    "LICENSE",
}


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def require(condition: bool, message: str) -> None:
    """Fail checksum validation even when Python assertions are optimized out."""
    if not condition:
        raise ValueError(message)


def main() -> None:
    checked: set[str] = set()
    for raw_line in MANIFEST.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        expected, relative = line.split(maxsplit=1)
        require(relative not in checked, f"duplicate checksum entry: {relative}")
        require(
            len(expected) == 64 and all(char in "0123456789abcdef" for char in expected),
            f"invalid SHA-256 digest: {relative}",
        )
        path = ROOT / relative
        require(path.is_file(), f"missing checksummed file: {relative}")
        actual = digest(path)
        require(actual == expected, f"checksum mismatch: {relative}")
        checked.add(relative)
    missing = REQUIRED_ARTIFACTS - checked
    unexpected = checked - REQUIRED_ARTIFACTS
    require(not missing, f"missing checksum entries: {sorted(missing)}")
    require(not unexpected, f"unexpected checksum entries: {sorted(unexpected)}")
    print(f"CHECKSUMS_VALID files={len(checked)}")


if __name__ == "__main__":
    main()

