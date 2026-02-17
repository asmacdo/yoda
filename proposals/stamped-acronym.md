# Proposal: STAMPED as the encompassing acronym for all 7 dimensions

## Terms

**Provenance**: the detailed history of how a research object was created, modified, and executed over time.
It captures the lineage and transformations of data and code, providing a transparent record of the workflow's evolution.

Provenance can have many specific types:
- a history of modifications, which may include details of who made the change, when, and what was changed.
  - Examples: version control histories, file metadata such as modification records (stat, EXIF, headers).
- details about the computational environment, including software versions, dependencies, and configuration settings.
  - Examples: Container tags and digests, frozen environment records (`pip freeze`, `conda list`, `package-lock.json`), system information (OS version, hardware details).
- a record of the commands or scripts executed, along with their inputs and outputs.
  - 
- a trace of the workflow execution, showing how data and code were transformed over time.

**Research object**: a collection of data, code, and metadata that together represent a complete unit of research output.
**Component**: any individual part of a research object, including both assets (data, code) and metadata (provenance records, README files).

> an independently versioned unit within a research object (e.g., an input dataset, a container repository, an analysis pipeline). A component contains assets, but not every asset is its own component. (Could also be called a "module")

**Asset**: data-containing contents of a research object (e.g., raw data files, processed data, code scripts) as opposed to metadata (e.g., README, provenance records).

> any file or artifact within a research object (data files, code scripts, config, container definitions, documentation)  


## Proposed Acronym: STAMP(ED)

A scientific workflow follows **STAMP** guidelines when it adheres to the following principles:

- **S** — **S**elf-contained: a research object is a complete retrieval unit
- **T** — **T**racked: all component states and modifications are recorded
- **A** — **A**ctionable: every dimension must be operationally useful
- **M** — **M**odular: all components are independent and composable
- **P** — **P**ortable: all components are operational across differing system architectures

A scientific workflow is fully **STAMPED** if it additionally meets the following ideal criteria:

- **E** — **E**phemeral: is able to perform all computation within a throwaway environment
- **D** — **D**istributable: all components shareable in a persistent state

These principles are ordered according to their importance; Self-Containment is the foundation, Actionability is the cross-cutting quality, and Ephemerality and Distributability are aspirational ideals.



## Context

With the addition of three new dimensions beyond the original four VAMP pillars — Self-Containment (#27), Ephemerality (#29), and Actionability-as-cross-cutting (#31) — we need an acronym that covers all seven concepts.

Issue #31 is particularly consequential: it reframes Actionability from a qualifier on provenance ("**A**ctionable provenance" in VAMP) to a **cross-cutting quality** that applies to all dimensions. This means Provenance needs its own slot, and Actionability applies everywhere.



## The Seven Dimensions

They are not all at the same level:

```
Foundation:     Self-Containment (boundary definition, P0)
Cross-cutting:  Actionability (operationally, not just declarative)
Core Pillars:   Tracking | Modularity | Portability
Ideals:         Ephemerality | D
```

- **Self-Containment** is the prerequisite — the research object must be a complete retrieval unit (#27, P0)
- **Actionability** is the quality requirement that elevates everything from metadata-only to operationally useful (#31)
- **Tracking, Modularity, Portability** are the structural principles (original VAMP, with "A" now promoted more broadly)
- **Ephemerality** can be a form of validation — if it works in a throwaway environment, your other principles provably hold (#29)

Actionability across dimensions:

| Dimension | Declarative (metadata only) | Actionable (operational) |
|---|---|---|
| Version Control | "this is version X" | `git checkout`, `datalad get` — **retrieve** any version |
| Provenance | W3C PROV record exists | `datalad rerun` — **re-execute** the recorded command |
| Modularity | subdirectories exist | `git submodule init`, `datalad install` — **compose/decompose** |
| Portability | Dockerfile present | `singularity run` — **move and execute** across environments |



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



### Usages of acronym in other domains

- **No existing use of "STAMPED" as an acronym** in research data management, reproducibility, or version control domains

- CODATA published "STAMP" (Standardized Data Management Plan for Educational Research, [doi:10.5334/dsj-2024-007](https://datascience.codata.org/articles/10.5334/dsj-2024-007)) — related domain but: (a) different acronym (STAMP vs STAMPED), (b) narrowly focused on educational research DMPs, (c) limited visibility, (d) conceptually distinct (DMP templates vs dataset organization principles)
  - This work is from 2024 and has never been cited according to Google Scholar
  - They also don't capitalize all the letters of the 'Stamp' acronym in their paper
  - Likely as a consequence of their acronym not actually mapping word for word to the items in their title
    - (Sta)ndardized Data (M)anagement (P)lan for Educational Research
    - TBH, StaMPER seems better for them anyway

- The hose assembly industry uses STAMPED (Size, Temperature, Application, Materials, Pressure, Ends, Delivery) — zero audience overlap
- Leveson's STAMP (System-Theoretic Accident Model and Processes) is very prominent in safety engineering — zero audience overlap
