# Research Materials for YODA Formalization Manuscript

This directory contains supporting research and analysis for the YODA formalization manuscript.

## Contents

### `related-organizational-principles.md`

Comprehensive survey of 19 organizational frameworks and principles for research data management (2003-2025), including:

- **Data versioning platforms**: Pachyderm, Quilt, Git LFS
- **Research packaging**: RO-Crate, OSF, Research Compendium
- **Environment management**: Nix/Guix
- **Domain platforms**: Galaxy, Code Ocean, brainlife.io, Flywheel, nipoppy
- **Data engineering**: Kedro
- **Foundational principles**: FAIR, Noble 2009, Cookiecutter Data Science, DVC

**Key findings**:
- Convergent evolution: Multiple independent initiatives arrived at similar patterns
- "Git for data" convergence (git-annex, Pachyderm, DVC, Git LFS, Quilt)
- Code/Environment/Data trinity pattern (Code Ocean, platforms, BIDS+YODA)
- Hierarchical composition (OSF, Kedro, YODA)
- YODA's unique contributions: federated, interface-agnostic, "do not look up"

**Use in manuscript**:
- Related Work section showing YODA in context
- Discussion section comparisons
- Validation that YODA principles solve universal problems

## Additional Research Needed

- Formal compliance checking methodology
- User studies on principle adoption
- Quantitative comparison of approaches
- Migration paths from other frameworks to YODA

## Contributing

Research materials should be added here with:
1. Clear documentation of sources
2. Organized by topic
3. Linked from manuscript where relevant
