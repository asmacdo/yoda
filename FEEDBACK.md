# Feedback and Guidance on YODA Formalization Manuscript

**Date**: 2026-02-06
**Authors**: Yaroslav Halchenko, Claude (assistant)
**Status**: Co-author guidance for manuscript development

---

## Overall Assessment

**Excellent work!** This formalization effort is critical for moving YODA from "best practices" to "operational specification." The RFC-style approach (MUST/SHOULD/MAY) is exactly right for:
- Standards body adoption
- Tool implementation specifications
- Compliance checking
- Clear teaching/documentation

The manuscript does important work positioning YODA within broader reproducibility landscape (FAIR, FAIR4RS, WCI-FW) while maintaining pragmatic focus.

---

## References to Add

**Foundational**:
- Noble, W. S. (2009). PLOS Computational Biology - Quick guide
- Wilkinson et al. (2016). Nature Scientific Data - FAIR Principles
- Wilson et al. (2017). PLOS Computational Biology - Good Enough Practices

**Git for Data**:
- Pachyderm: https://github.com/pachyderm/pachyderm
- DVC: https://dvc.org/
- Git LFS vs git-annex comparison: https://lwn.net/Articles/774125/

**Platforms**:
- Code Ocean: https://pmc.ncbi.nlm.nih.gov/articles/PMC7893895/
- brainlife.io: https://www.nature.com/articles/s41592-024-02237-2
- Galaxy: https://academic.oup.com/nar/article/52/W1/W83/7676834

**Frameworks**:
- Kedro: https://kedro.org/
- nipoppy: https://github.com/nipoppy/nipoppy
- Cookiecutter Data Science: https://cookiecutter-data-science.drivendata.org/

**Standards**:
- RO-Crate: https://www.researchobject.org/ro-crate/
- BEP028: https://github.com/bids-standard/BEP028_BIDSprov
- BioComputeObject: IEEE 2791-2020

**Package Management**:
- Nix for reproducibility: https://onlinelibrary.wiley.com/doi/full/10.1002/qua.26872
- Guix-HPC: https://arxiv.org/abs/1506.02822

**YODA Implementations & Adoption**:
- Wagner et al. (2023). "A DataLad extension for semantic metadata handling" - Scientific Data: https://doi.org/10.1038/s41597-023-02242-8
- DataLad MetaLad provenance extractor: https://github.com/datalad/datalad-metalad/blob/master/datalad_metalad/extractors/runprov.py

**BIDS & Neuroimaging Adoption**:
- BIDS specification: https://bids-specification.readthedocs.io/
- fMRIPrep: https://fmriprep.org/ and https://github.com/nipreps/fmriprep
  - TODO: Add specific GitHub issue reference for "yoda" layout proposal
- OpenNeuroDerivatives: https://github.com/OpenNeuroDerivatives
- BABS (BIDS App Bootstrap): https://github.com/PennLINC/babs
- Hanke et al. "FAIRly big workflow": https://doi.org/10.1016/j.patter.2021.100322 (Patterns, 2021)

---

## Final Note

This manuscript fills a critical gap: moving YODA from "tribal knowledge" to "operational specification." The RFC-style formalization enables:
- Tool builders to create YODA-compliant implementations
- Standards bodies to adopt/reference principles
- Educators to teach systematically
- Researchers to self-assess compliance

The convergent evolution we documented (19 frameworks, 2003-2025) **validates** that YODA principles solve real, universal problems. This manuscript can position YODA as a synthesis of best practices emerging across domains.

Strong foundation—with additions outlined above, this will be a significant contribution to reproducible research methodology!
