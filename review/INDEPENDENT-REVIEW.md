# Independent review record

| Field | Value |
| --- | --- |
| Candidate | GRHS 0.4.0 public-review draft |
| Review status | Completed with changes |
| Reviewer | CodeRabbit automated third-party review service |
| Review medium | [GitHub pull request #1](https://github.com/pi0n00r/grhs/pull/1) |
| Reviewed revision | `dcaea2b3c7f275fcee1d0668d083ba9b30a8967d` |
| Review run | `07ae88b7-6e44-4467-aa3f-33d43a4ec319` |
| Disposition revisions | `1b3cf88dcb265275bdb612c19ee4b389188daffb`, `9873f99573e2141687818ebebcd326049c1b9497` |
| Disposition completed | Yes |

## Scope and limits

The independent review covered release integrity, deterministic generation,
automation security, checksum coverage, and the completeness of the review
record. It did not constitute linguistic peer review, speaker validation,
accessibility testing, or community acceptance. Those remain open work for the
public-review process described in `review/REVIEW-GUIDE.md`.

## Findings and dispositions

| ID | Review thread | Finding | Disposition | Evidence |
| --- | --- | --- | --- | --- |
| GRHS-RV-001 | [r4430581150](https://github.com/pi0n00r/grhs/pull/1#discussion_r4430581150) | GitHub Actions used mutable major-version tags. | Accepted. Both actions are pinned to the full commit IDs for checkout 7.0.1 and setup-python 7.1.0. | `9873f99` |
| GRHS-RV-002 | [r4430581152](https://github.com/pi0n00r/grhs/pull/1#discussion_r4430581152) | The review record lacked immutable revisions and per-finding dispositions. | Accepted. This record now identifies the reviewed commit, review run, finding IDs, disposition revisions, and outcome of every comment. | This record |
| GRHS-RV-003 | [r4430581154](https://github.com/pi0n00r/grhs/pull/1#discussion_r4430581154) | DOCX rebuilds could vary because ZIP timestamps were current. | Accepted. The builder now writes under `build/` and normalizes member order, timestamps, permissions, and compression metadata. Two consecutive rebuilds produced SHA-256 `02186edc4405d66e9c48c48381316bf4e2e7e00b392f2cc1f7255a8c3b887ec5`. | `9873f99` |
| GRHS-RV-004 | [r4430581156](https://github.com/pi0n00r/grhs/pull/1#discussion_r4430581156) | PDF export saved updated fields over the source DOCX. | Accepted. Export now works on an exact temporary copy and deletes it afterward. The source DOCX hash remained unchanged in the qualified export test. | `9873f99` |
| GRHS-RV-005 | [r4430581159](https://github.com/pi0n00r/grhs/pull/1#discussion_r4430581159) | The checksum verifier did not require every release artifact or reject duplicate entries. | Accepted. The verifier enforces the complete seven-file release set, unique paths, and valid lowercase SHA-256 digests. | `9873f99` |
| GRHS-RV-006 | [r4430581161](https://github.com/pi0n00r/grhs/pull/1#discussion_r4430581161) | CI found a platform-dependent normalization-fixture checksum. | Accepted. Generated CSV and JSON now use explicit LF bytes; canonical hashes were regenerated and both GitHub validation runs passed. | `1b3cf88` |

## Qualification evidence

- `RELEASE_VALID rows=51 normalization_vectors=13`
- `CHECKSUMS_VALID files=7`
- two consecutive DOCX rebuilds were byte-identical;
- Microsoft Word exported a 12-page PDF without changing the rebuilt DOCX;
- GitHub push and pull-request validation passed on the corrected generator;
- all six substantive CodeRabbit comments have an explicit disposition above.

