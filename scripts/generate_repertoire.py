#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Gary Bajaj
# SPDX-License-Identifier: AGPL-3.0-only

"""Generate the normative GRHS repertoire and normalization vectors."""

from __future__ import annotations

import csv
import json
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


ROWS = [
    ("V01", "core-vowel", "/ə/", "a", "A", "short central vowel"),
    ("V02", "core-vowel", "/aː/", "á", "Á", "long a"),
    ("V03", "core-vowel", "/ɪ/", "i", "I", "dotless i is excluded"),
    ("V04", "core-vowel", "/iː/", "í", "Í", "long i"),
    ("V05", "core-vowel", "/ʊ/", "u", "U", "short u"),
    ("V06", "core-vowel", "/uː/", "ú", "Ú", "long u"),
    ("V07", "core-vowel", "/eː/", "e", "E", "mid front vowel"),
    ("V08", "core-vowel", "/ɛː/", "ai", "Ai", "multicodepoint GRHS grapheme"),
    ("V09", "core-vowel", "/oː/", "o", "O", "mid back vowel"),
    ("V10", "core-vowel", "/ɔː/", "au", "Au", "multicodepoint GRHS grapheme"),
    ("C01", "core-consonant", "/k/", "k", "K", ""),
    ("C02", "core-consonant", "/kʰ/", "kʰ", "Kʰ", "aspirated grapheme"),
    ("C03", "core-consonant", "/g/", "g", "G", ""),
    ("C04", "core-consonant", "/gʰ/", "gʰ", "Gʰ", "aspirated grapheme"),
    ("C05", "core-consonant", "/t͡ʃ/", "ç", "Ç", ""),
    ("C06", "core-consonant", "/t͡ʃʰ/", "çʰ", "Çʰ", "aspirated grapheme"),
    ("C07", "core-consonant", "/d͡ʒ/", "j", "J", ""),
    ("C08", "core-consonant", "/d͡ʒʰ/", "jʰ", "Jʰ", "aspirated grapheme"),
    ("C09", "core-consonant", "/ʈ/", "ṭ", "Ṭ", "retroflex"),
    ("C10", "core-consonant", "/ʈʰ/", "ṭʰ", "Ṭʰ", "retroflex aspirated grapheme"),
    ("C11", "core-consonant", "/ɖ/", "ḍ", "Ḍ", "retroflex"),
    ("C12", "core-consonant", "/ɖʰ/", "ḍʰ", "Ḍʰ", "retroflex aspirated grapheme"),
    ("C13", "core-consonant", "/t̪/", "t", "T", "dental"),
    ("C14", "core-consonant", "/t̪ʰ/", "tʰ", "Tʰ", "dental aspirated grapheme"),
    ("C15", "core-consonant", "/d̪/", "d", "D", "dental"),
    ("C16", "core-consonant", "/d̪ʰ/", "dʰ", "Dʰ", "dental aspirated grapheme"),
    ("C17", "core-consonant", "/p/", "p", "P", ""),
    ("C18", "core-consonant", "/pʰ/", "pʰ", "Pʰ", "aspirated grapheme"),
    ("C19", "core-consonant", "/b/", "b", "B", ""),
    ("C20", "core-consonant", "/bʰ/", "bʰ", "Bʰ", "aspirated grapheme"),
    ("C21", "core-consonant", "/m/", "m", "M", ""),
    ("C22", "core-consonant", "/n/", "n", "N", ""),
    ("C23", "core-consonant", "/ɳ/", "ṇ", "Ṇ", "retroflex"),
    ("C24", "core-consonant", "/ŋ/", "ñ", "Ñ", "open review issue"),
    ("C25", "core-consonant", "/ɲ/", "ny", "Ny", "multicodepoint GRHS grapheme; open review issue"),
    ("C26", "core-consonant", "/r, ɾ/", "r", "R", ""),
    ("C27", "core-consonant", "/ɽ/", "ŗ", "Ŗ", "retroflex"),
    ("C28", "core-consonant", "/ɽʰ/", "ŗʰ", "Ŗʰ", "retroflex aspirated grapheme"),
    ("C29", "core-consonant", "/l/", "l", "L", ""),
    ("C30", "core-consonant", "/ʋ, v/", "v", "V", ""),
    ("C31", "core-consonant", "/s/", "s", "S", ""),
    ("C32", "core-consonant", "/ʃ/", "ş", "Ş", ""),
    ("C33", "core-consonant", "/h/", "h", "H", "independent consonant; not aspiration"),
    ("C34", "core-consonant", "/j/", "y", "Y", ""),
    ("X01", "extended-consonant", "/q/", "q", "Q", "loan phoneme"),
    ("X02", "extended-consonant", "/x/", "x", "X", "loan phoneme"),
    ("X03", "extended-consonant", "/ɣ/", "ġ", "Ġ", "loan phoneme"),
    ("X04", "extended-consonant", "/z/", "z", "Z", "loan phoneme"),
    ("X05", "extended-consonant", "/ʒ/", "ž", "Ž", "loan phoneme"),
    ("X06", "extended-consonant", "/f/", "f", "F", "loan phoneme"),
    ("M01", "marker", "vowel nasalization", "ṃ", "Ṃ", "spacing letter used after a vowel grapheme"),
]


def codepoints(text: str) -> str:
    return " ".join(f"U+{ord(char):04X}" for char in text)


def names(text: str) -> str:
    return " + ".join(unicodedata.name(char) for char in text)


def main() -> None:
    data_dir = ROOT / "data"
    tests_dir = ROOT / "tests"
    data_dir.mkdir(exist_ok=True)
    tests_dir.mkdir(exist_ok=True)

    with (data_dir / "repertoire.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            lineterminator="\n",
            fieldnames=[
                "id",
                "inventory",
                "ipa",
                "grapheme",
                "uppercase",
                "codepoints",
                "unicode_names",
                "nfd_codepoints",
                "notes",
            ],
        )
        writer.writeheader()
        for identifier, inventory, ipa, grapheme, uppercase, note in ROWS:
            if grapheme != unicodedata.normalize("NFC", grapheme):
                raise ValueError(f"repertoire source is not NFC: {identifier}")
            writer.writerow(
                {
                    "id": identifier,
                    "inventory": inventory,
                    "ipa": ipa,
                    "grapheme": grapheme,
                    "uppercase": uppercase,
                    "codepoints": codepoints(grapheme),
                    "unicode_names": names(grapheme),
                    "nfd_codepoints": codepoints(unicodedata.normalize("NFD", grapheme)),
                    "notes": note,
                }
            )

    vectors = {
        "schema": "grhs-normalization-v1",
        "specification_version": "0.4.0",
        "normalization": "NFC",
        "canonical_equivalence": [
            {"input": "a\u0301", "output": "á"},
            {"input": "i\u0301", "output": "í"},
            {"input": "u\u0301", "output": "ú"},
            {"input": "c\u0327", "output": "ç"},
            {"input": "t\u0323", "output": "ṭ"},
            {"input": "d\u0323", "output": "ḍ"},
            {"input": "n\u0323", "output": "ṇ"},
            {"input": "n\u0303", "output": "ñ"},
            {"input": "r\u0327", "output": "ŗ"},
            {"input": "s\u0327", "output": "ş"},
            {"input": "g\u0307", "output": "ġ"},
            {"input": "z\u030c", "output": "ž"},
            {"input": "m\u0323", "output": "ṃ"},
        ],
        "longest_match": [
            {"text": "kʰ", "graphemes": ["kʰ"]},
            {"text": "aiṃ", "graphemes": ["ai", "ṃ"]},
            {"text": "au", "graphemes": ["au"]},
            {"text": "ny", "graphemes": ["ny"]},
            {"text": "ŗʰ", "graphemes": ["ŗʰ"]},
        ],
        "must_not_silently_normalize": [
            {"input": "ı", "reason": "dotless i is not GRHS"},
            {"input": "kh", "reason": "ordinary h is not the canonical aspiration marker"},
            {"input": "ṣ", "reason": "visually related letter is not GRHS ş"},
        ],
    }
    (tests_dir / "normalization.json").write_bytes(
        (json.dumps(vectors, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    )


if __name__ == "__main__":
    main()

