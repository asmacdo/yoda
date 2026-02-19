# Nature Scientific Data — Article Requirements

Source: https://www.nature.com/sdata/submission-guidelines and https://www.nature.com/sdata/aims-and-scope

## Article Type: Article (not Data Descriptor)

Scientific Data publishes two article types:

1. **Data Descriptor** — describes new, open research datasets for reuse (the primary format)
2. **Article** — covers data policy, repositories, standards, ontologies, workflows, or any topic relating to the mechanics of data sharing. May also present commentaries or opinions on research data policy, workflows, or infrastructure. (Absorbed the former "Comment" type.)

**Scope**: Scientific Data does *not* publish traditional research articles using data to validate scientific hypotheses. Articles must relate to data sharing mechanics, infrastructure, or policy.

STAMPED fits the Article type: it formalizes properties for reproducible research objects — squarely about data management standards and workflows.

## Structure

Required sections for Articles:

1. **Title**
2. **Author list** (no heading needed)
3. **Abstract**
4. **Main sections** — IMRaD (Introduction, Methods, Results, Discussion) recommended but **not mandated**; more speculative or non-study works may use a different structure
5. **Data Availability**
6. **Code Availability**
7. **References**
8. **Author Contributions**
9. **Competing Interests**
10. **Acknowledgements** (optional)
11. **Funding**
12. **Ethics statement** (where relevant)

Compare to Data Descriptors which require rigid sections: Background & Summary, Methods, Data Records, Technical Validation, Usage Notes.

## Limits

- **Main text**: No word limit. The journal is online-only and not printed.
- **Abstract**: 170 words recommended, unstructured (no sub-headings), unreferenced. Should not make claims regarding new scientific findings. No URLs for data access.
- **Title**: Maximum 110 characters including spaces. No colons or parentheses. Capitalize only first word and proper nouns. No acronyms (except common ones like DNA), no "novel"/"first"/"AI-ready" claims.
- **Figures**: Recommended no more than 8 (not a hard limit).
- **Figure legends**: No more than 350 words total.
- **Tables**: Recommended no more than 10. Tables exceeding one A4 page go to Supplementary.
- **References**: No explicit limit.
- **Supplementary**: Should not extend paper by more than ~10 pages; journal discourages supplementary material and prefers content in main manuscript.

## LaTeX

- **No official template** — the journal explicitly discourages templates: "We do not provide, suggest or recommend the use of a LaTeX template so if you find a previous or legacy version of this via platforms such as Overleaf please do not use them."
- Use standard article class; Nature applies their own style at publication.
- For initial submission: a single PDF with embedded figures is sufficient.
- For revised manuscripts: a single standalone .TEX file required, compilable without .bib files, style sheets, or other dependencies.
- References MUST be embedded in the .TEX file (no separate .bib/.bbl).
- Recommended font: Computer Modern.
- Use graphicx.sty for figures.
- Do not use internal hyperlinks (\cref or similar).
- The Springer Nature template (`sn-jnl` with `sn-nature` option) exists on Overleaf but is discouraged by the journal.

## References Format

- Standard Nature referencing style — numbered sequentially, superscript in text.
- One publication per reference number.
- Only published/accepted papers or recognized preprints.
- Titles required for cited articles.

Example:
> Schott, D. H., Collins, R. N. & Bretscher, A. Secretory vesicle transport velocity in living cells depends on the myosin V lever arm length. J. Cell Biol. 156, 35–39 (2002).

For 6+ authors: first author et al.

### Data Citations

Datasets must be cited in the reference list:
> Author(s). Title. Repository https://doi.org/XXXXX (Year).

## Figures

- Arabic numbering, in order of occurrence.
- Clear, sans-serif typeface (e.g., Helvetica).
- White background.
- Multi-panel: lowercase bold a, b, c labels.
- Scale bars preferred over magnification factors.
- SI units with single space between number and unit.
- Error bars with statistical treatment in legend.

## Peer Review

- All in-scope manuscripts meeting technical requirements are sent for review.
- **Not assessed on perceived significance, importance, or impact.**
- All technically sound papers are accepted.
- Manuscripts are not subject to in-depth copy editing; authors responsible for language quality.

## Open Access

- Fully open access, online only.
- APC: ~$2,690 / GBP 2,150 / EUR 2,390 (waivers available for low-income countries).
- CC BY or CC BY-NC-ND license.

## Journal Info

- ISSN: 2052-4463 (online)
- Abbreviation: Sci. Data
