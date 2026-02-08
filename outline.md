# YODA: The Four Pillars of Idiomatic Dataset Version Control

> Must follow requirements in [NMETH-ARTICLE-REQUIREMENTS.md](NMETH-ARTICLE-REQUIREMENTS.md)

## Abstract
- TODO: compose after other sections filled out (≤150 words, unreferenced)

## Introduction
- TODO: VIOLATION — must not have heading or subheadings. Remove "Introduction" heading and flatten "Related Work" subsection into introductory prose.
- Challenge: dataset scale, complexity, interdependency
- Workflows as formal specifications (code, config, data, provenance)
  - Table 1: Term definitions
- Components managed separately undermines reproducibility
- FAIR / FAIR4RS / WCI-FW foundation
- YODA as pragmatic best practices for FAIR-aligned research objects

- Related Work: Organizational Principles Across Domains (restrict to brief intro, especially to set us up with established concepts and definitions, more details later)
  - 19 frameworks (2003–2025) showing convergent evolution
  - Foundational principles (Noble 2009, FAIR, Good Enough Practices)
  - Version control extensions (git-annex, Git LFS, DVC, Pachyderm, Quilt)
  - Cloud platforms (Code Ocean, brainlife, Flywheel, Galaxy)
  - Framework tooling (Kedro, nipoppy, Cookiecutter Data Science)
  - Metadata standards (RO-Crate, BioComputeObject, BEP028)
  - Convergent patterns: separation of concerns, immutability, hierarchy, VCS, provenance
  - YODA's unique position: federated, interface-agnostic, local-first, git-annex flexibility

## Results

- Table 2 (all VAMP principles)

### Version Control Everything
- Problems with non-version-controlled data
- VCS as content-addressed identification (not just version numbering)
- Extending git to large datasets (git-annex, DataLad, DVC)
- All workflow components must be under VCS
- **P1.1** All assets MUST be included
- **P1.2** All assets SHOULD use the same VCS

### Modularity
- Monolithic structures impede reuse and maintenance
- Compositional approach: independently versioned components
- Idiomatic layout: code/, inputs/, envs/, docs/, results/
- **P2.1** Assets SHOULD be organized modularly
- **P2.2** Assets MAY be included directly or as subdatasets
- **P2.3** Components SHOULD accommodate domain-specific standards

### Portable Computational Environments
- Environmental drift as cause of irreproducibility
- Explicit specification and versioning of environments
- Container-based (Docker, Singularity) vs package-based (Nix, Guix)
- Mechanism-agnostic
- **P4.1** Environments MUST be explicitly specified
- **P4.2** Specifications SHOULD be machine-reproducible
- **P4.3** Definitions MUST be version controlled
- **P4.4** Environments SHOULD be self-contained within the dataset

### Incorporating Actionable Provenance into VCS History
- Provenance embedded in commit records, not separate systems
- Programmatic annotation for code-driven changes
- **P3.1** Provenance MUST be annotated
- **P3.2** Code-driven provenance SHOULD be programmatic, MUST include versions

- Provenance Format Targets
  - W3C PROV, BEP028, RO-Crate, BioComputeObject
  - Migration path: DataLad run records exportable to standard formats

### Principle Priorities
- Essential (MUST): P1.1, P3.1, P4.1
- Strong (SHOULD): P1.2, P2.1, P4.2
- Optional (MAY): P2.2, P2.3

## Discussion
- TODO: VIOLATION — must not contain subheadings. Flatten all subsections into continuous prose.

- Comparison to Related Approaches
  - DVC: shared philosophy, different architecture
  - Pachyderm: centralized/cloud vs local-first/federated
  - Kedro: within-project vs across-project modularity (complementary)
  - Cloud Platforms: turnkey vs local control, YODA can wrap platform outputs
- Trade-offs and Limitations
  - git-annex complexity vs Git LFS simplicity
  - When YODA excels vs when it may be more than needed
- Integration Opportunities
  - YODA + BIDS, RO-Crate, FAIR, workflow systems, platforms
- Future Directions
  - Provenance standards convergence
  - Tool certification
  - Teaching materials
  - Existing adoption (BIDS, fMRIPrep, OpenNeuroDerivatives, BABS, CRCNS)

## Methods
- TODO: VIOLATION — must be titled "Online Methods" with subheadings
- TODO: how principles were derived, validation approach, community input

## Data Availability
- Version-controlled manuscript repo: https://github.com/myyoda/principles-paper/
- TODO: Zenodo DOI https://github.com/myyoda/principles-paper/issues/19
- TODO: Examples repo https://github.com/myyoda/principles-paper/issues/20


## Code Availability

## References

## Author Contributions

## Competing Interests

## Acknowledgments
