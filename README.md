# GRHS

GRHS is Gary Bajaj’s proposed phonemic Latin orthography for modern Hindustani. It is intended to represent the shared spoken base of Hindi and Urdu with explicit treatment of aspiration, retroflexion, vowel contrasts, nasalization, and gemination.

This repository publishes **GRHS 0.4.0**, a public review draft. It is not an adopted standard and does not claim endorsement by any language community, institution, government, or standards body.

## Read the draft

- [`SPECIFICATION.md`](SPECIFICATION.md) is the canonical source.
- [`GRHS-v0.4.0.pdf`](GRHS-v0.4.0.pdf) is the fixed-layout reading copy.
- [`GRHS-v0.4.0.docx`](GRHS-v0.4.0.docx) is the editable review copy.
- [`data/repertoire.csv`](data/repertoire.csv) is the normative machine-readable repertoire.
- [`review/REVIEW-GUIDE.md`](review/REVIEW-GUIDE.md) lists the questions on which review is most useful.

## What GRHS is

GRHS is a pronunciation-based orthography written with existing Unicode Latin characters. It is not a new Unicode script, not a reversible Devanagari transliteration, and not a reversible Perso-Arabic Urdu transliteration.

## Review status

The inventory and encoding profile are mechanically specified. Speaker validation, Hindi and Urdu linguistic review, reader testing, accessibility testing, a complete collation tailoring, and a production input method remain pending.

Please do not interpret publication as a claim that these gates have passed.

## Build and verification

Run with Python 3 and `python-docx`:

```powershell
python scripts/generate_repertoire.py
python scripts/build_docx.py
python scripts/validate_release.py
python scripts/verify_checksums.py
```

On Windows with Microsoft Word installed, create the PDF:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/export_pdf.ps1
```

The repository's GitHub Actions workflow regenerates the repertoire, rejects
uncommitted generated-data drift, validates the release, and verifies the
published artifact hashes on every push and pull request.

## License

The specification, data, and accompanying code are licensed under `AGPL-3.0-only`. Independent text is not covered merely because it is written in GRHS. See [`LICENSE-NOTICE.md`](LICENSE-NOTICE.md).

