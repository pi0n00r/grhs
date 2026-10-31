# GRHS

## A Modern Phonemic Latin Orthography for Hindustani

| Field | Value |
| --- | --- |
| Version | 0.4.0 |
| Date | 31 October 2026 |
| Status | Public review draft; not a final standard |
| Author | Gary Bajaj |
| Reference variety | Educated Delhi/Doabi Hindustani |
| Canonical normalization | Unicode NFC |
| License | AGPL-3.0-only |

Copyright © 2026 Gary Bajaj.

This draft is an individual proposal circulated for technical review. Publication does not imply endorsement, adoption, registration, or approval by any standards body, government, academic institution, or language community.

## 1. Scope

GRHS is a proposed phonemic Latin orthography for modern Hindustani, covering the shared spoken base conventionally associated with Hindi and Urdu. It is intended to provide a regular, teachable, digitally implementable spelling system that represents the contrastive sounds of the declared reference variety.

The established project name expands to *Gary Roman Hindustani Script*. In technical usage, however, GRHS is an orthography written in the Unicode Latin script. It is not a newly encoded script, a Devanagari transliteration, a Perso-Arabic transliteration, or a reversible representation of either source orthography.

This document specifies:

- the core and extended GRHS phoneme-to-grapheme inventory;
- canonical Unicode representation and normalization;
- rules for aspiration, retroflexion, nasalization, gemination, schwa, case, and punctuation;
- minimum conformance requirements for stored GRHS text and software;
- provisional input, search, and collation behavior; and
- known issues that require empirical and expert review.

It does not mandate replacement of Devanagari or Perso-Arabic Urdu, claim community adoption, define automatic source-script transliteration, or request new Unicode characters.

## 2. Conformance language

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHOULD**, **SHOULD NOT**, and **MAY** are to be interpreted as described by BCP 14 when, and only when, they appear in all capitals.

Normative sections define conformance. Examples, rationale, comparisons, and sections explicitly labelled *informative* do not.

## 3. Terminology

**Code point** means a Unicode scalar value such as U+02B0.

**Code-point sequence** means one or more ordered Unicode code points.

**GRHS grapheme** means a spelling unit defined by this specification. A GRHS grapheme can contain more than one Unicode code point. It is not necessarily identical to a Unicode extended grapheme cluster.

**Reference pronunciation** means the educated Delhi/Doabi Hindustani pronunciation selected for this draft. It is a declared model, not a claim that all speakers use one pronunciation.

**Source spelling** means a spelling in Devanagari, Perso-Arabic Urdu, or another orthography from which pronunciation evidence may be obtained.

## 4. Design principles

1. **Stable phonemic mapping.** Each contrastive phoneme receives one stable GRHS grapheme within the declared reference variety.
2. **Predictable sequences.** A grapheme may be a multicodepoint sequence when the sequence is explicitly defined and can be parsed deterministically.
3. **No silent letters.** Canonical spelling follows the selected pronunciation rather than preserving unpronounced source-script material.
4. **Modern Hindustani priority.** Sanskritic and Perso-Arabic etymology informs analysis but does not override the selected modern pronunciation.
5. **Stable lexical spelling.** Casual or individual phonetic variation does not automatically change the standard lexical form.
6. **Computable representation.** Canonical text is NFC-normalized and uses only existing Unicode characters.

The phrase “one phoneme, one grapheme” does not mean “one phoneme, one code point.” For example, `kʰ` is one GRHS grapheme represented by U+006B followed by U+02B0.

## 5. Normative inventory

### 5.1 Vowels

| ID | Phoneme | GRHS | Canonical code point(s) | Note |
| --- | --- | --- | --- | --- |
| V01 | /ə/ | `a` | U+0061 | Permitted realizations include [ə] and [ɐ] |
| V02 | /aː/ | `á` | U+00E1 | Long a |
| V03 | /ɪ/ | `i` | U+0069 | Dotless `ı` is not GRHS |
| V04 | /iː/ | `í` | U+00ED | Long i |
| V05 | /ʊ/ | `u` | U+0075 | Short u |
| V06 | /uː/ | `ú` | U+00FA | Long u |
| V07 | /eː/ | `e` | U+0065 | Mid front |
| V08 | /ɛː/ | `ai` | U+0061 U+0069 | One GRHS vowel grapheme |
| V09 | /oː/ | `o` | U+006F | Mid back |
| V10 | /ɔː/ | `au` | U+0061 U+0075 | One GRHS vowel grapheme |

### 5.2 Core consonants

| ID | Phoneme | GRHS | ID | Phoneme | GRHS |
| --- | --- | --- | --- | --- | --- |
| C01 | /k/ | `k` | C02 | /kʰ/ | `kʰ` |
| C03 | /g/ | `g` | C04 | /gʰ/ | `gʰ` |
| C05 | /t͡ʃ/ | `ç` | C06 | /t͡ʃʰ/ | `çʰ` |
| C07 | /d͡ʒ/ | `j` | C08 | /d͡ʒʰ/ | `jʰ` |
| C09 | /ʈ/ | `ṭ` | C10 | /ʈʰ/ | `ṭʰ` |
| C11 | /ɖ/ | `ḍ` | C12 | /ɖʰ/ | `ḍʰ` |
| C13 | /t̪/ | `t` | C14 | /t̪ʰ/ | `tʰ` |
| C15 | /d̪/ | `d` | C16 | /d̪ʰ/ | `dʰ` |
| C17 | /p/ | `p` | C18 | /pʰ/ | `pʰ` |
| C19 | /b/ | `b` | C20 | /bʰ/ | `bʰ` |
| C21 | /m/ | `m` | C22 | /n/ | `n` |
| C23 | /ɳ/ | `ṇ` | C24 | /ŋ/ | `ñ` |
| C25 | /ɲ/ | `ny` | C26 | /r, ɾ/ | `r` |
| C27 | /ɽ/ | `ŗ` | C28 | /ɽʰ/ | `ŗʰ` |
| C29 | /l/ | `l` | C30 | /ʋ, v/ | `v` |
| C31 | /s/ | `s` | C32 | /ʃ/ | `ş` |
| C33 | /h/ | `h` | C34 | /j/ | `y` |

Phonemic /h/ permits phonetic realizations [h~ɦ]. U+02B0 MODIFIER LETTER SMALL H marks aspiration and is distinct from independent `h`.

### 5.3 Extended loan-phoneme inventory

| ID | Phoneme | GRHS | Canonical code point(s) |
| --- | --- | --- | --- |
| X01 | /q/ | `q` | U+0071 |
| X02 | /x/ | `x` | U+0078 |
| X03 | /ɣ/ | `ġ` | U+0121 |
| X04 | /z/ | `z` | U+007A |
| X05 | /ʒ/ | `ž` | U+017E |
| X06 | /f/ | `f` | U+0066 |

The extended graphemes are lexical spellings when the reference form preserves the corresponding phoneme. A colloquial merger does not by itself alter the standard spelling.

## 6. Structural rules

### 6.1 Longest-match parsing

A GRHS parser MUST apply longest-match parsing within words. It MUST recognize, before their component letters:

1. aspirated consonant sequences ending in `ʰ`;
2. the vowel graphemes `ai` and `au`;
3. the palatal nasal grapheme `ny`; and
4. a vowel grapheme followed by the nasalization marker `ṃ`.

This rule is orthographic. It does not modify Unicode’s default grapheme-cluster boundaries.

### 6.2 Aspiration

Aspiration is written with U+02B0 MODIFIER LETTER SMALL H after an eligible consonant: `kʰ gʰ çʰ jʰ ṭʰ ḍʰ tʰ dʰ pʰ bʰ ŗʰ`.

Canonical GRHS text MUST use `ʰ`, not ordinary `h`, for aspiration. An input method MAY accept ordinary `h` after an eligible consonant and convert it before storage. A search interface MAY treat the typed form as a forgiving query equivalent, but MUST NOT silently rewrite canonical stored text to ordinary `h`.

### 6.3 Retroflexion

| Dental or alveolar | Retroflex |
| --- | --- |
| `t` | `ṭ` |
| `tʰ` | `ṭʰ` |
| `d` | `ḍ` |
| `dʰ` | `ḍʰ` |
| `n` | `ṇ` |
| `r` | `ŗ` |

### 6.4 Nasalization

Nasal consonants are written `n`, `m`, `ṇ`, and `ñ`. Vowel nasalization is written by placing U+1E43 LATIN SMALL LETTER M WITH DOT BELOW (`ṃ`) immediately after the vowel grapheme.

`ṃ` is a spacing Latin letter used as an orthographic marker. It is not a combining mark. In `maiṃ`, longest-match parsing identifies `ai` as the vowel grapheme and `ṃ` as its nasalization marker.

| Source-oriented form | GRHS | Function |
| --- | --- | --- |
| hā̃ | `háṃ` | Nasalized vowel |
| maiṅ | `maiṃ` | Nasalized vowel |
| kahā̃ | `kaháṃ` | Nasalized vowel |
| rang | `rañg` | Velar nasal consonant |

### 6.5 Gemination

A geminate consonant is written by doubling its consonant grapheme. `patá` and `pattá`, for example, remain distinct.

### 6.6 Schwa

GRHS writes pronounced vowels only. Automatic conversion from Devanagari therefore requires a pronunciation or schwa-deletion analysis before deterministic IPA-to-GRHS conversion. This draft does not define a complete source-script schwa-deletion algorithm.

### 6.7 Source-script artifacts

GRHS represents the selected modern pronunciation rather than mechanically preserving historical categories or conjuncts.

| Traditional form | Provisional GRHS treatment |
| --- | --- |
| ऋ | `ri` or the selected modern reflex |
| क्ष | `kş` when pronounced /kʃ/ |
| श्र | `şr` |
| ज्ञ | `gny` or the selected modern pronunciation |
| ष / श | `ş` when pronounced /ʃ/ |
| ङ | `ñ` |
| ञ | `ny` |

These mappings are informative conversion guidance, not reversible transliteration rules.

## 7. Case, punctuation, and word form

GRHS uses ordinary Latin sentence case and international punctuation. Diacritic distinctions remain part of the spelling under case conversion. The uppercase of `ŗ` is `Ŗ`; the aspiration marker remains `ʰ`. A multicodepoint grapheme capitalizes its initial cased letter when required.

Examples:

```text
Hindustán   Dillí   Nyáy   Ŗám
Kyá áp taiyár haiṃ?
Nahíṃ, abʰí nahíṃ.
```

Hyphenation and word division follow ordinary editorial practice unless a later GRHS style guide specifies a lexical convention.

## 8. Unicode representation

### 8.1 Canonical storage

Conformant stored GRHS text MUST be valid Unicode and MUST be normalized to NFC. Input software MAY accept canonically equivalent decomposed sequences, but MUST normalize them before canonical storage or interchange.

The repertoire uses existing Unicode Latin characters. GRHS does not require a new Unicode block or script code.

### 8.2 Complete repertoire data

The normative machine-readable repertoire is `data/repertoire.csv`. It records every grapheme ID, IPA value, canonical spelling, code-point sequence, Unicode name, uppercase form, and inventory status. An implementation MUST NOT infer GRHS membership merely from visual similarity.

### 8.3 Confusables and invalid substitutions

The following distinctions are significant:

- `i` is U+0069; dotless `ı` is not GRHS.
- `ʰ` is U+02B0; ordinary `h` is the independent consonant.
- `ş` is U+015F and is not `ṣ`, `ś`, or `s` plus an arbitrary mark.
- `ŗ` is U+0157 and is not `ṛ`, `r`, or a visually similar sequence.
- `ṃ` is U+1E43 and is not a generic anusvara transliteration rule.

Software SHOULD display a diagnostic for non-GRHS confusables rather than silently changing lexical content. Security-sensitive identifiers SHOULD use a separately defined identifier profile; ordinary GRHS prose is not, by itself, an identifier-safety profile.

## 9. Input, search, and collation

### 9.1 Input

A conformant input method MUST be able to produce every normative grapheme without copy-and-paste. A mnemonic input layer MAY accept ASCII sequences, but its output MUST use canonical GRHS spelling and NFC.

### 9.2 Search

Exact search MUST compare NFC-normalized text. A user-facing search MAY additionally offer diacritic-insensitive or ASCII-mnemonic matching. Such forgiving matching MUST be labelled or otherwise distinguishable from exact GRHS matching because it can collapse phonemic contrasts.

### 9.3 Collation

Until a complete tailored collation is adopted, implementations SHOULD use a documented locale-aware Unicode collation and MUST identify the locale and Unicode/CLDR version used. A future GRHS tailoring should keep an aspirated grapheme adjacent to its unaspirated counterpart and preserve phonemic distinctions at a primary or explicitly documented level.

The present draft does not claim a CLDR tailoring.

## 10. Conformance classes

### 10.1 Conformant GRHS text

A text is *GRHS 0.4 conformant* when it:

1. uses only the normative inventory plus ordinary punctuation, numbers, spaces, and explicitly marked foreign material;
2. is NFC-normalized;
3. uses `ʰ` rather than ordinary `h` for aspiration;
4. follows the structural rules in Section 6; and
5. identifies itself as GRHS 0.4 or a compatible later version.

### 10.2 Conformant normalizer

A GRHS normalizer MUST:

1. accept valid Unicode text;
2. normalize canonical input to NFC;
3. preserve all phonemic distinctions;
4. reject or report ambiguous non-GRHS substitutions; and
5. pass the published normalization vectors.

### 10.3 Conformant validator

A GRHS validator MUST report invalid code points and invalid grapheme sequences with their positions. It MUST NOT claim that lexical spelling or pronunciation has been validated merely because character-level validation passes.

## 11. Reference-pronunciation decisions

| Item | Reference form | GRHS |
| --- | --- | --- |
| roman | /roːmən/ | `roman` |
| aur | /ɔːr/ | `aur` |
| liye | /lɪjeː/ | `liye` |
| mujhe | /mʊd͡ʒʱeː/ | `mujʰe` |
| vah | /ʋəh/ | `vah` |
| Hindi h | phonemic /h/; [h~ɦ] | `h` |

## 12. Deterministic sample

The sample is mechanically consistent with its declared IPA source and the inventory. The reference pronunciation has not yet been empirically validated.

### 12.1 IPA source

Sentence 1:

```text
/t̪ʊrkiː bʱaːʃaː roːmən lɪpiː meː̃ pəɽʱneː pər mʊd͡ʒʱeː ləɡaː kiː d̪eːʋənaːɡəriː lɪpiː meː̃ lɪkʱeː d͡ʒaːneː ʋaːleː ʃəbd̪oː̃ koː roːmən lɪpiː meː̃ d͡ʒɪs t̪ərəh lɪkʱaː d͡ʒaːt̪aː hɛː ʋəh ənʊt͡ʃɪt̪ ɔːr əpuːrɳ hɛː/
```

Sentence 2:

```text
/səʈiːkət̪aː keː lɪjeː həmeː̃ aːd̪ʱʊnɪk d̪ʊnɪjaː meː̃ eːk nəjiː roːmən lɪpiː kiː aːʋəʃjəkt̪aː hɛː d͡ʒɪs keː pəɽʱneː lɪkʱneː meː̃ st̪ʰɪrət̪aː hoː/
```

### 12.2 GRHS output

```text
Turkí bʰáşá roman lipí meṃ paŗʰne par mujʰe lagá kí Devanágarí lipí meṃ likʰe jáne vále şabdoṃ ko roman lipí meṃ jis tarah likʰá játá hai vah anuçit aur apúrṇ hai.

Saṭíkatá ke liye hameṃ ádʰunik duniyá meṃ ek nayí roman lipí kí ávaşyaktá hai jis ke paŗʰne-likʰne meṃ stʰiratá ho.
```

## 13. Prior art and positioning

GRHS addresses a different problem from source-script transliteration standards. ISO 15919 transliterates Devanagari and related Indic scripts into Latin characters; ALA-LC provides cataloguing romanization tables for Hindi and Urdu. GRHS instead proposes a pronunciation-based Hindustani orthography. That difference does not remove the obligation to compare usability, reversibility, familiarity, and technical behavior with established systems.

A comparative study against ISO 15919, ALA-LC Hindi and Urdu, IAST, Hunterian practice, and informal Roman Urdu/Hinglish remains required before any claim of practical superiority.

## 14. Validation status

| Area | Status at 0.4.0 |
| --- | --- |
| Core inventory consistency | Mechanically specified |
| Canonical Unicode representation | Specified and machine-readable |
| NFC normalization | Specified; test vectors included |
| IPA-to-GRHS sample consistency | Mechanically reviewed for the reference sample |
| Input method | Requirements stated; implementation pending |
| Collation | Requirements stated; tailoring pending |
| Source-script conversion | Out of scope without pronunciation analysis |
| Speaker validation | Pending |
| Hindi and Urdu linguistic review | Pending |
| Reader and accessibility testing | Pending |
| Community adoption | Not claimed |

## 15. Open review issues

The following choices are deliberately exposed for review rather than disguised as settled facts:

1. whether `ñ` for /ŋ/ and `ny` for /ɲ/ are learnable enough across Hindi, Urdu, and international Latin-script audiences;
2. whether `ai` and `au` should remain single vowel graphemes for the selected reference analysis;
3. whether the acute-accent length convention offers enough benefit over macrons or other established practice;
4. whether the aspiration marker `ʰ` is sufficiently typable, accessible, and robust in common fonts;
5. how lexical spelling should handle dialect and register variation;
6. how schwa deletion and pronunciation selection should be documented for source-script conversion;
7. the final collation order and forgiving-search profile; and
8. whether screen readers pronounce the repertoire intelligibly in realistic running text.

## 16. Versioning and governance

GRHS uses semantic versioning for the published specification:

- a **major** version may change canonical spelling or the phonemic model incompatibly;
- a **minor** version may add backward-compatible rules, data, or conformance detail; and
- a **patch** version may correct editorial or machine-readable defects without changing intended spelling.

Every published version MUST include a changelog and immutable tagged source. Proposals and review comments are tracked publicly, but Gary Bajaj remains the specification owner until a later governance document explicitly changes that arrangement.

## 17. License

This specification and its repository materials are licensed under the GNU Affero General Public License, version 3.0 only (`AGPL-3.0-only`). The license governs copying and modification of the specification and accompanying software or data. It does not impose the license on independent text merely because that text is written in GRHS.

## 18. References

### Normative

1. IETF, BCP 14: RFC 2119 and RFC 8174, requirement-level key words. <https://www.rfc-editor.org/info/bcp14/>
2. Unicode Standard Annex #15, *Unicode Normalization Forms*. <https://www.unicode.org/reports/tr15/>
3. Unicode Standard Annex #29, *Unicode Text Segmentation*. <https://www.unicode.org/reports/tr29/>

### Informative

1. Unicode Technical Standard #10, *Unicode Collation Algorithm*. <https://www.unicode.org/reports/tr10/>
2. Unicode Technical Standard #39, *Unicode Security Mechanisms*. <https://www.unicode.org/reports/tr39/>
3. IETF RFC 5646, *Tags for Identifying Languages*. <https://www.rfc-editor.org/rfc/rfc5646>
4. ISO 15919:2001, *Transliteration of Devanagari and related Indic scripts into Latin characters*. <https://www.iso.org/standard/28333.html>
5. Library of Congress, *ALA-LC Romanization Tables: Hindi*. <https://www.loc.gov/catdir/cpso/romanization/hindi.pdf>

## Annex A. Changes from v0.3

- Preserved the v0.3 alphabet and modifier-letter aspiration design.
- Reframed GRHS precisely as a Latin-script orthography, not a separately encoded script.
- Added normative conformance language, terminology, stable grapheme IDs, and machine-readable repertoire data.
- Clarified that `ṃ` is a spacing letter used as an orthographic nasalization marker.
- Defined longest-match parsing and distinguished GRHS graphemes from Unicode grapheme clusters.
- Added explicit input, search, collation, confusable-character, governance, versioning, and licensing rules.
- Added prior-art positioning and a candid open-issues register.
- Preserved empirical speaker, reader, and accessibility validation as pending work.

