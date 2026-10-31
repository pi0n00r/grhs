#!/usr/bin/env python3
"""Verify the immutable release artifacts listed in SHA256SUMS."""

from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "SHA256SUMS"


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def main() -> None:
    checked = 0
    for raw_line in MANIFEST.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        expected, relative = line.split(maxsplit=1)
        path = ROOT / relative
        assert path.is_file(), f"missing checksummed file: {relative}"
        actual = digest(path)
        assert actual == expected, f"checksum mismatch: {relative}"
        checked += 1
    assert checked > 0, "empty checksum manifest"
    print(f"CHECKSUMS_VALID files={checked}")


if __name__ == "__main__":
    main()

