# Nature Scientific Data — Style Notes for Articles

Compared to Nature Methods, Scientific Data is considerably less prescriptive about formatting and style. Key practical notes for authoring.

## Key Differences from Nature Methods

| Aspect | Nature Methods | Scientific Data (Article) |
|--------|---------------|--------------------------|
| Abstract | 150 words, unreferenced | 170 words, unreferenced, unstructured |
| Title | No specific char limit stated | 110 characters max, no colons/parentheses |
| Main text word limit | 3,000–5,000 words | **No limit** |
| Figures | Up to 6 | Recommended ≤8 (soft) |
| References | Up to 50 | **No limit** |
| Introduction | No heading, no subheadings | Flexible — IMRaD recommended, not mandated |
| Results | Topical subheadings required | Flexible |
| Discussion | No subheadings allowed | Flexible |
| Methods | "Online Methods" with subheadings | Standard Methods section |
| Copy editing | Substantial editorial editing | **No in-depth copy editing** — authors responsible |
| Template | Springer Nature available | Explicitly discouraged |
| Extended Data | Up to 10 items | Not a concept; use Supplementary if needed |

## What This Means for STAMPED

### More Freedom in Structure

Nature Methods enforced: no heading on Introduction, subheadings required in Results, no subheadings in Discussion. Scientific Data allows any structure as long as mandatory heading sections are present.

The current manuscript structure (Introduction → Results with STAMPED subsections → Discussion with subsections → Methods) is perfectly acceptable and does not need restructuring.

### No Word Limit — But Stay Focused

The lack of a word limit means the current manuscript text can expand where needed (especially the Discussion comparisons and spectrum examples) without worrying about the 3,000-word Nature Methods ceiling.

However, the journal notes that excessive figures often indicate out-of-scope content (general analyses/results). Keep content focused on the STAMPED framework itself.

### Authors Own the Language Quality

Unlike Nature Methods which substantially edits for non-specialist accessibility, Scientific Data does not copy-edit. The manuscript must be polished before submission. This is both freedom and responsibility.

### Title Constraints

The current working title "STAMPED: Properties of a Reproducible Research Object" is 53 characters — well within the 110-character limit. But note:
- No colons allowed → the current colon-free title works
- No "novel", "first", etc.
- Only capitalize first word and proper nouns → "STAMPED: properties of a reproducible research object"

### Abstract — Slightly More Room

170 words instead of 150. Still unreferenced, still unstructured. Should describe the framework and its utility without claiming "new scientific findings."

### Reference Style

Same Nature-family numbered superscript style. No limit on count — useful for the extensive related work survey. Data/code citations go in the reference list with DOIs.

## Scope Fit

Scientific Data Articles cover "data policy, repositories, standards, ontologies, workflows, or any topic relating to the mechanics of data sharing within public data repositories."

STAMPED is a framework of properties for reproducible research objects — it directly addresses data management standards and workflows. The paper:
- Defines formal properties (standards)
- Covers data organization, versioning, provenance (data policy/workflows)
- Discusses repository and platform integration (data sharing mechanics)
- Compares to related frameworks (RO-Crate, FAIR, DVC, etc.)

This is squarely within scope.

## Writing Style

Scientific Data does not provide the same level of style guidance as Nature Methods ("So you're writing a paper"). General Nature-family conventions apply:

- Active voice preferred
- Avoid jargon and acronyms where alternatives exist
- Direct, clear language
- One idea per paragraph

Since there is no editorial copy-editing pass, extra care with:
- Consistency of terminology (research object, module, component)
- RFC 2119 keyword usage (MUST, SHOULD, MAY) — ensure these are used deliberately
- Tool-agnostic framing in definitions, tool-specific examples in spectrum discussions
