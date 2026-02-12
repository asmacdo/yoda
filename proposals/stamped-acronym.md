# Proposal: STAMPED as the encompassing acronym for all 7 dimensions

## Context

With the addition of three new dimensions beyond the original four VAMP pillars — Self-Containment (#27), Ephemerality (#29), and Actionability-as-cross-cutting (#31) — we need an acronym that covers all seven concepts.

Issue #31 is particularly consequential: it reframes Actionability from a qualifier on provenance ("**A**ctionable provenance" in VAMP) to a **cross-cutting quality** that applies to all dimensions. This means Provenance needs its own slot, and Actionability applies everywhere.

## The Seven Dimensions

They are not all at the same level:

```
Foundation:     Self-Containment (boundary definition, P0)
Core Pillars:   Version Control | Modularity | Provenance | Portability
Discipline:     Ephemerality (execution validation)
Cross-cutting:  Actionability (operational, not just declarative)
```

- **Self-Containment** is the prerequisite — the research object must be a complete retrieval unit (#27, P0)
- **Version Control, Modularity, Provenance, Portability** are the structural principles (original VAMP, with "A" now promoted)
- **Ephemerality** is the validation discipline — if it works in a throwaway environment, your other principles provably hold (#29)
- **Actionability** is the quality requirement that elevates everything from metadata-only to operationally useful (#31)

Actionability across dimensions:

| Dimension | Declarative (metadata only) | Actionable (operational) |
|---|---|---|
| Version Control | "this is version X" | `git checkout`, `datalad get` — **retrieve** any version |
| Provenance | W3C PROV record exists | `datalad rerun` — **re-execute** the recorded command |
| Modularity | subdirectories exist | `git submodule init`, `datalad install` — **compose/decompose** |
| Portability | Dockerfile present | `singularity run` — **move and execute** across environments |

## Proposed Acronym: STAMPED

- **S** — **S**elf-contained (#27): research object is a complete retrieval unit; "do not look up" (#1)
- **T** — **T**racked (version-controlled): all assets under content-addressed VCS
- **A** — **A**ctionable (cross-cutting, #31): every dimension must be operationally useful, not just recorded
- **M** — **M**odular: independently versioned, composable components
- **P** — **P**rovenance-recorded: modifications annotated in VCS history; code-driven provenance programmatic
- **E** — **E**phemeral (#29): compute in throwaway environments; validates containment and portability
- **D** — **D**eployable (portable): environments explicitly specified, machine-reproducible, transferable

### Why STAMPED works

**As a word:**
- Real English word with professional tone
- Connotation of **certification/approval** — "STAMPED-compliant" reads naturally
- Evokes **timestamping** — a core VCS concept
- "Stamped with provenance" is almost literal
- Works as noun ("the STAMPED principles"), adjective ("a STAMPED dataset"), or verb ("we STAMPED this workflow")

**As an acronym:**
- 7 letters, 7 concepts, clean 1-to-1 mapping
- Each letter maps to a distinct, well-defined dimension
- No forced or obscure expansions
- Alphabetically groups related concepts (S-T for foundation+tracking, A-M-P for core qualities, E-D for execution+deployment)

**Practically:**
- Sidesteps Star Wars trademark concerns raised in #7
- More professionally descriptive than VAMP
- Enables natural compliance language: "Is your research object STAMPED?"
- Could frame the paper as: principles formalized through STAMPED

### Prior art check

- **No existing use of "STAMPED" as an acronym** in research data management, reproducibility, or version control domains
- The hose assembly industry uses STAMPED (Size, Temperature, Application, Materials, Pressure, Ends, Delivery) — zero audience overlap
- CODATA published "STAMP" (Standardized Data Management Plan for Educational Research, [doi:10.5334/dsj-2024-007](https://datascience.codata.org/articles/10.5334/dsj-2024-007)) — related domain but: (a) different acronym (STAMP vs STAMPED), (b) narrowly focused on educational research DMPs, (c) limited visibility, (d) conceptually distinct (DMP templates vs dataset organization principles)
- Leveson's STAMP (System-Theoretic Accident Model and Processes) is very prominent in safety engineering — completely different domain, and consistently using "STAMPED" (not "STAMP") avoids confusion

## Alternative: PREVAMP (VAMP lineage)

If preserving continuity with the established VAMP name is preferred:

- **P** — Provenance-recorded
- **R** — Ringed/Bounded (self-contained)? Reproducible?
- **E** — Ephemeral
- **V** — Versioned
- **A** — Actionable
- **M** — Modular
- **P** — Portable

**Pros:**
- Extends the VAMP brand ("evolved VAMP")
- Maintains recognition for audiences familiar with VAMP

**Cons:**
- Two P's for different concepts (Provenance, Portable)
- "R" mapping is weak — no clean word for self-containment starting with R
- "Pre-VAMP" linguistically reads as "before VAMP" rather than "beyond VAMP"
- Less intuitive as a standalone word

If VAMP lineage is important, an alternative framing could be to keep VAMP as the core four pillars and present Self-Containment (P0), Ephemerality, and cross-cutting Actionability as the **governing qualities** around them — though this loses the single-acronym simplicity.

## Recommendation

**STAMPED** as the primary proposal. It is clean, available in our domain, professionally appropriate, and covers all seven dimensions with natural language mappings. The relationship to YODA/VAMP can be stated in the paper: "Building on the YODA organizational philosophy and the VAMP formalization, we present the STAMPED principles..."

## Mapping to current manuscript structure

| STAMPED | Manuscript Section | Principles |
|---|---|---|
| **S** Self-contained | P0, "Do not look up" (#1) | P0, P2.4 |
| **T** Tracked | Version Control Everything | P1.1, P1.2 |
| **A** Actionable | Cross-cutting (#31) | Applies to all |
| **M** Modular | Modularity | P2.1, P2.2, P2.3 |
| **P** Provenance | Incorporating Provenance | P3.1, P3.2 |
| **E** Ephemeral | New section needed (#29) | New P-statements |
| **D** Deployable | Portable Environments | P4.1, P4.2, P4.3, P4.4 |
