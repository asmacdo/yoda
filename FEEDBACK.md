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

## Critical Gaps Requiring Attention

### 1. Missing 4th Pillar: Portable Environments ❌

**Issue**: Title claims "Four pillars" but only 3 sections exist:
1. ✓ Version Control Everything
2. ✓ Modularity
3. ✓ Provenance
4. ❌ **Portable Environments** (this is YODA Principle 2!)

**Action Required**: Add section after Modularity:

**Suggested structure**:

```latex
\subsection{Portable Computational Environments}

Research reproducibility fundamentally depends not only on preserving code and data,
but also on capturing the complete computational environment—the operating system,
libraries, dependencies, and tool versions—that produced the results.

Environmental drift, where software dependencies evolve or disappear over time,
is a primary cause of computational irreproducibility. Even with identical code and
data, differences in library versions, compiler settings, or system configurations
can produce divergent results or outright failures.

YODA addresses this through explicit environment specification and versioning.
Computational environments should be:
- Explicitly defined (not implicitly assumed)
- Machine-reproducible (via containers, Nix/Guix, or language-specific managers)
- Version controlled alongside code and data
- Self-contained within the project boundary

Two primary approaches exist for environment portability:
1. **Container-based**: Docker, Singularity/Apptainer provide OS-level isolation
2. **Package-based**: Nix, Guix provide declarative, reproducible package management

YODA principles are environment-mechanism-agnostic; what matters is that
environments are explicitly specified, versioned, and available within the project.

\textbf{Formal Principles:}

\begin{itemize}
    \item \textbf{P4.1} Computational environments \textbf{MUST} be explicitly specified
    \item \textbf{P4.2} Environment specifications \textbf{SHOULD} be machine-reproducible
    \item \textbf{P4.3} Environment definitions \textbf{MUST} be version controlled
    \item \textbf{P4.4} Environments \textbf{SHOULD} be self-contained within the dataset
\end{itemize}
```

### 2. "Do Not Look Up" Principle Missing ❌

**Issue**: Lines 125-127 have comments about this critical principle but no formal statement!

This is THE distinguishing YODA principle that enables:
- True portability (dataset moves anywhere)
- Federated composition (subdatasets from different origins)
- Independent reuse (no implicit dependencies)

**Action Required**: Add to Modularity section (P2.4):

```latex
A fundamental constraint for achieving true modularity is that modules must not
depend on assets outside their defined boundary. This "do not look up" principle
ensures that a dataset remains portable and self-contained.

Specifically:
- No references to parent directories (../)
- No implicit dependencies on user environment variables
- No unversioned references to external registries (docker pull without hash/tag)
- No absolute paths to user-specific locations

Violation of this principle breaks dataset portability and undermines reproducibility
guarantees. If external resources are required, they must be explicitly included
as versioned subdatasets or documented dependencies.

\textbf{Real-world validation}: The BIDS neuroimaging community experienced this issue
directly. Early BIDS specifications nested derivative data under \texttt{derivatives/}
within raw datasets, forcing derivative datasets to "look up" to their parent. This
violated portability—moving a derivative dataset broke its connection to raw data.
Following YODA principles, BIDS reversed the relationship: derivatives now exist
independently and reference raw data as subdatasets. This architectural change influenced
fMRIPrep (initially proposed as "yoda" layout), OpenNeuroDerivatives, and the BIDS
specification itself~\cite{bids-spec,fmriprep,openneuro-derivatives}.

\textbf{Formal Principles:}

\begin{itemize}
    \item \textbf{P2.4} Modules \textbf{MUST NOT} depend on assets outside their boundary
    \item \textbf{P2.5} External dependencies \textbf{MUST} be either:
        \begin{itemize}
            \item included as versioned git submodules (DataLad subdatasets), or
            \item instrumented with other known and/or well documented retrieval mechanisms
        \end{itemize}
\end{itemize}
```

**Connection to "working surface" concept**: This principle relates to the notion of
a "working surface" (or "frontier") for a research project—a collection of working items
that represent frozen or derived states from "deeper", original structures. The "do not
look up" principle ensures that the working surface remains self-contained while preserving
mechanisms to retrieve and reconnect to source materials when needed. This is why
"retrieval" (P2.5) is emphasized: external dependencies must have documented access paths,
not implicit assumptions about directory hierarchies.

### 3. VAMP Terminology Clarification

**Issue**: Title mentions "YODA, VAMP" but VAMP never defined.

**Resolution**: Add footnote on first mention:

```latex
\title{YODA (VAMP\footnote{VAMP: Versioned, Actionable, Modular, Portable—alternative
terminology proposed by colleagues to describe the same principles. For consistency
with existing literature and community usage, this manuscript uses YODA throughout.}):
Four pillars of idiomatic version control}
```

Or simpler approach: Remove VAMP from title entirely and add brief mention in Introduction that alternative terminology exists but we use established YODA name.

---

## Major Enhancements

### 4. Integrate Organizational Principles Landscape Research 🎯

**Perfect timing!** Line 14 TODO: "do research on related compositional patterns across standards and fields"

**We just completed this research!** Document: [Organizational Principles Landscape Survey](research/related-organizational-principles.md)

**Findings** (19 frameworks spanning 2003-2025):
- Galaxy (2005), git-annex (2010), Nix/Guix (2012), Pachyderm (2014), Git LFS (2015), FAIR (2016), Code Ocean (2017), DVC (2017), brainlife.io (2017), YODA (2018), Flywheel (2018), Kedro (2019), RO-Crate (2019), Quilt (2020s), nipoppy (2023)

**Key insights for manuscript**:

1. **Convergent Evolution**: Multiple independent initiatives arrived at similar patterns:
   - "Git for data" (Pachyderm, DVC, git-annex, Git LFS, Quilt)
   - Code/Environment/Data trinity (Code Ocean, brainlife, Flywheel, BIDS+YODA)
   - Hierarchical composition (OSF components, Kedro modular pipelines, YODA subdatasets)
   - Frozen frontiers (snapshot.debian.org, DOIs, Pachyderm commits, Galaxy history)

2. **YODA's Unique Position**:
   - Only framework combining: full version control + federated architecture + hierarchical composition + interface agnosticism + local-first design
   - git-annex flexibility (many remote types: SSH, S3, HTTP, local) vs single-server models (Git LFS, Pachyderm)
   - "Do not look up" principle (unique to YODA)

3. **Pragmatic Spectrum**:
   - Abstract guidelines (FAIR, Noble 2009) ← YODA (pragmatic tools) → Turnkey services (Code Ocean, OSF, Galaxy)
   - YODA sits in middle: opinionated tools with local control, no cloud lock-in

**Action Required**: Add section to Introduction:

```latex
\subsection{Related Work: Organizational Principles Across Domains}

The challenges YODA addresses are not unique to neuroscience or even scientific computing
broadly. Multiple communities independently developed organizational frameworks exhibiting
remarkable convergent evolution toward similar core patterns.

Between 2003 and 2025, at least 19 distinct initiatives emerged addressing research data
organization, version control, and reproducibility:

\textbf{Foundational principles}: Noble's 2009 guidelines for computational biology
organization, FAIR principles (2016) for data sharing, Software Carpentry's "Good Enough
Practices" (2017).

\textbf{Version control extensions}: git-annex (2010), Git LFS (2015), DVC (2017),
Pachyderm (2014), Quilt (2020s) all independently arrived at "Git for data" concepts,
applying proven version control semantics to large datasets.

\textbf{Cloud platforms}: Code Ocean (2017), brainlife.io (2017), Flywheel (2018),
Galaxy (2005) provide turnkey reproducibility services, all implementing code/environment/data
trinity separation.

\textbf{Framework tooling}: Kedro (2019), nipoppy (2023), Cookiecutter Data Science (2016)
provide opinionated structures for data engineering and neuroimaging workflows.

\textbf{Metadata standards}: RO-Crate (2019), BioComputeObject (IEEE 2791-2020), BEP028
(BIDS Provenance) address packaging and provenance standardization.

Despite independent origins, these frameworks converged on core patterns:
\begin{itemize}
    \item \textbf{Separation of concerns}: Data ≠ code ≠ environment ≠ results
    \item \textbf{Immutability}: Raw data never modified in-place
    \item \textbf{Hierarchical organization}: Nested, modular structures
    \item \textbf{Version control}: Applying Git concepts beyond just code
    \item \textbf{Provenance tracking}: Recording how outputs were generated
\end{itemize}

YODA's unique contributions within this landscape:
\begin{itemize}
    \item \textbf{Federated composition}: Subdatasets can live anywhere (not centralized)
    \item \textbf{Interface agnosticism}: Works with any container/pipeline system
          (not platform-specific like brainlife ABCD apps or Flywheel gears)
    \item \textbf{"Do not look up" principle}: Explicit no-dependency-on-parent rule
    \item \textbf{Local-first design}: Works offline, no cloud platform dependency
    \item \textbf{git-annex flexibility}: Many remote types vs single-server models
    \item \textbf{Scale via modularity}: Proven from single files to 8000+ subdatasets
          (datasets.datalad.org)
\end{itemize}

This convergent evolution validates that YODA principles are not arbitrary choices but
responses to fundamental challenges in computational research reproducibility. The
formalization presented here provides a foundation for interoperability and comparison
across this evolving ecosystem of tools and standards.
```

**References to add**:
- [Noble 2009](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424)
- [FAIR 2016](https://www.nature.com/articles/sdata201618)
- [Pachyderm](https://github.com/pachyderm/pachyderm)
- [Kedro](https://kedro.org/)
- [Code Ocean - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7893895/)
- [brainlife.io - Nature Methods 2024](https://www.nature.com/articles/s41592-024-02237-2)
- [RO-Crate](https://www.researchobject.org/ro-crate/)
- [Git LFS vs git-annex](https://lwn.net/Articles/774125/)

---

## Content Enhancements

### 5. Add Concrete Examples for Each Principle

Each principle needs:
- ✓ **Compliant example** (with code/structure)
- ✗ **Non-compliant example** (showing what fails)
- **Why non-compliant fails reproducibility**

Depending on publication venue we might want that in supplements or Addendum to not distract readers.
But if we accompany this also online in some form -- it could be an expandable note like often done e.g. in DataLad Handbook.

**Example for P2.4 ("Do not look up")**:

```latex
\textbf{Example: Non-compliant vs Compliant Structure}

\textbf{Non-compliant} (violates P2.4):
\begin{verbatim}
my-analysis/
├── code/
│   └── analyze.py          # imports from ../../../lab-utils/
└── results/
    └── figure1.png

# analyze.py contains:
import sys
sys.path.append('../../../lab-utils')  # VIOLATION: looks up
from preprocessing import load_data

docker run lab/analysis:latest ...     # VIOLATION: unversioned external
\end{verbatim}

This fails because:
- Moving my-analysis/ to another machine breaks (no ../../../lab-utils)
- Docker image may change without warning (no version pin)
- No record of what lab-utils code was actually used

\textbf{Compliant} (follows P2.4):
\begin{verbatim}
my-analysis/
├── code/
│   └── analyze.py
├── inputs/
│   └── lab-utils/          # subdataset (git submodule)
│       └── preprocessing.py
├── envs/
│   └── analysis.sif        # versioned Singularity container
└── results/
    └── figure1.png

# analyze.py contains:
import sys
sys.path.append('./inputs/lab-utils')  # contained within dataset
from preprocessing import load_data

singularity exec envs/analysis.sif ... # versioned, included environment
\end{verbatim}

This succeeds because:
- All dependencies within my-analysis/ boundary
- lab-utils at specific git commit (subdataset)
- Container is versioned file within dataset
- Dataset portable: works anywhere
\end{verbatim}
```

### 6. Expand Provenance Section

**Current**: Good conceptual description
**Missing**: Target provenance formats and interoperability

**Add**:

```latex
\subsubsection{Provenance Format Targets}

While YODA advocates embedding provenance in version control histories, interoperability
with standardized provenance formats is essential for broader adoption and integration.

Key provenance standards YODA implementations should support:

\textbf{W3C PROV}: Foundation for many domain-specific formats, provides Activity/Entity/Agent model.

\textbf{BEP028 (BIDS Provenance)}: BIDS Extension Proposal using W3C PROV for neuroimaging
workflows. Captures Activities (what ran), Entities (inputs/outputs), Agents (tools), in
JSON-LD format.

\textbf{RO-Crate}: Lightweight packaging with Schema.org + JSON-LD metadata. Practical
implementation of FAIR Digital Object Framework. Used across domains (bioinformatics,
digital humanities, regulatory sciences).

\textbf{BioComputeObject}: IEEE 2791-2020 standard for bioinformatics provenance.
Emphasizes regulatory compliance and auditability.

Pragmatic migration paths exist: DataLad run records (internal format) can be exported
to any of these standards, enabling YODA-structured projects to integrate with diverse
tool ecosystems while maintaining internal consistency. Reference implementations for
provenance export are available in the datalad-metalad extension~\cite{datalad-metalad-runprov}.
```

**Note**: Reference implementation for provenance extraction from DataLad run records is available at:
https://github.com/datalad/datalad-metalad/blob/master/datalad_metalad/extractors/runprov.py

### 7. Complete Discussion Section

**Suggested structure**:

```latex
\section{Discussion}

\subsection{Comparison to Related Approaches}

\subsubsection{DVC (Data Version Control)}
Shares "Git for data" philosophy but differs in architecture:
- DVC: External .dvc files + remote storage config
- YODA/git-annex: Integrated into git repository structure
- DVC: Python-ML focus, single project
- YODA: Language-agnostic, federated multi-project composition

Both valid; choice depends on: team familiarity (DVC easier for ML engineers),
infrastructure (DVC integrates easily with cloud ML platforms), scale requirements
(git-annex more flexible for federated datasets).

\subsubsection{Pachyderm}
Enterprise "Git for data" with Kubernetes-native architecture:
- Pachyderm: Centralized cluster, cloud-required
- YODA: Local-first, works offline, federated
- Pachyderm: Automatic pipeline triggering
- YODA: Explicit execution (datalad run)

Pachyderm excels for: production ML pipelines, team collaboration with compute resources,
automatic scaling. YODA excels for: research workflows, offline work, heterogeneous
datasets across institutions.

\subsubsection{Kedro}
Python data engineering framework with modular pipelines:
- Kedro: Within-project modularity (Python pipeline components)
- YODA: Across-project modularity (subdatasets as git submodules)
- Kedro: Built-in visualization (Kedro-Viz)
- YODA: CLI-focused, integration with external tools

Complementary: Kedro pipeline inside YODA dataset combines both strengths.

\subsubsection{Cloud Platforms (Code Ocean, brainlife.io, Flywheel)}
Turnkey reproducibility services with proprietary interfaces:
- Platforms: Zero local setup, institutional partnerships
- YODA: Local control, no vendor lock-in
- Platforms: Web GUI, point-and-click
- YODA: CLI/API, scriptable automation
- Platforms: Centralized (single capsule/project)
- YODA: Federated (compose across repositories)

YODA principles could "wrap" platform outputs: download results → organize locally
with full versioning → compose across platforms via subdatasets.

\subsection{Trade-offs and Limitations}

\subsubsection{git-annex Complexity vs Git LFS Simplicity}
YODA uses git-annex for maximum flexibility (many remote types: SSH, S3, HTTP, local
drives, even offline USB drives). This comes at cost: steeper learning curve.

Git LFS offers simpler alternative: transparent to users, GitHub/GitLab native support,
1M+ repos adoption. Trade-off: centralized (requires LFS server), no offline capability,
less flexible remote configurations.

"YODA-lite" implementations using Git LFS feasible for easier onboarding, sacrificing
federation flexibility.

\subsubsection{When YODA Is vs Isn't Appropriate}

\textbf{YODA excels when}:
- Multi-institutional collaboration (federated datasets)
- Long-term reproducibility (decades, offline archives)
- Heterogeneous workflows (not platform-specific)
- Data sovereignty requirements (no cloud upload mandates)
- Complex dependency graphs (subdatasets from diverse sources)

\textbf{YODA may be overkill for}:
- Single-script analyses (version control sufficient without DataLad)
- Ephemeral exploratory work (Jupyter notebooks)
- Cloud-native ML production (Pachyderm/platform may be better fit)
- Small teams with simple workflows (DVC, Git LFS may suffice)

\subsection{Integration Opportunities}

YODA principles are complementary, not competitive, with existing standards:

- \textbf{YODA + BIDS}: Domain standard within YODA structure
- \textbf{YODA + RO-Crate}: Organization during research → packaging for publication
- \textbf{YODA + FAIR}: Structure projects → share via FAIR
- \textbf{YODA + workflow systems}: Organize → execute (Nextflow, Snakemake, CWL)
- \textbf{YODA + platforms}: Download → version → compose locally

\subsection{Future Directions}

\subsubsection{Provenance Standards Convergence}
Ongoing work toward unified provenance representation (BEP028, RO-Crate convergence)
will improve YODA interoperability with domain-specific tools.

\subsubsection{Tool Certification}
Formal YODA principles enable "YODA-compliant" tool certification, similar to
BIDS validation.

\subsubsection{Teaching Materials}
Operationalized principles provide foundation for structured curriculum development
beyond current tutorial-based approaches.

\subsubsection{Existing YODA Adoption}
Several research projects have already adopted and documented YODA principles,
demonstrating practical utility across domains.

\textbf{BIDS Standard Evolution}: A significant validation of the "do not look up"
principle (P2.4) occurred within the Brain Imaging Data Structure (BIDS) community.
Originally, the BIDS specification nested derived data under \texttt{derivatives/}
within the original raw dataset, creating upward dependencies that violated portability.
Following YODA principles, the BIDS community reversed this relationship: derivative
datasets now exist independently and reference raw data as subdatasets, not vice versa.

This architectural shift influenced major neuroimaging tools:
\begin{itemize}
    \item \textbf{fMRIPrep}~\cite{fmriprep}: Switched default output layout to follow
          YODA structure, initially proposing to name it "yoda" layout
          (TODO: add GitHub issue reference).
    \item \textbf{OpenNeuroDerivatives}~\cite{openneuro-derivatives}: Entire derivative
          dataset collection now follows YODA organization, separating processed outputs
          from raw data dependencies.
    \item \textbf{BIDS specification}~\cite{bids-spec}: Updated to accommodate and
          recommend YODA-compliant layouts for derivative datasets.
\end{itemize}

\textbf{Workflow Platforms}: Infrastructure projects implementing YODA at scale:
\begin{itemize}
    \item \textbf{BABS}~\cite{babs}: Platform implementing Hanke et al.'s "FAIRly big
          workflow"~\cite{fairly-big} approach, demonstrating YODA principles for
          large-scale neuroimaging analyses with containerized pipelines and modular
          dataset composition.
    \item \textbf{CRCNS.org}~\cite{crcns-yoda}: Neuroscience data sharing platform
          providing YODA-structured templates and validation tools.
\end{itemize}

These adoptions demonstrate that YODA principles solve practical organizational
challenges across scales, from individual studies to community-wide infrastructure.
```

**Note**: Key reference for existing YODA adoption:
- Wagner et al. (2023). "A DataLad extension for semantic metadata handling" - Scientific Data
  https://doi.org/10.1038/s41597-023-02242-8
  (Shows YODA principles in practice with metadata management)

---

## Minor Improvements

### 8. Add Principle Priority Guidance

Help readers understand what's essential vs optional:

```latex
\subsection{Principle Priorities}

\textbf{Essential (MUST for basic reproducibility)}:
- P1.1: All assets included
- P3.1: Provenance annotated
- P4.1: Environments specified

These are minimum requirements; omitting any fundamentally compromises reproducibility.

\textbf{Strong recommendations (SHOULD for reusability)}:
- P1.2: Same VCS for all assets
- P2.1: Modular structure
- P2.4: Do not look up
- P4.2: Machine-reproducible environments

Deviation possible but reduces portability and reuse potential.

\textbf{Optional (MAY for convenience)}:
- P2.2: Subdatasets vs direct inclusion (both valid)
- P2.3: Domain-specific standards (nice-to-have, not always applicable)
```

### 9. Clarify Version Control Terminology

Line 66-68 insight is excellent but could be stronger:

```latex
Although commonly called "version control systems," the primary value is not version
numbering ("v1" vs "v2") but \emph{content-addressed identification}. Git describes
itself as "the stupid content tracker" (from \texttt{man git}), using cryptographic
checksums as content identifiers. Explicit version tags (v1.0, v2.3) are convenience
labels atop this content-tracking foundation.

This distinction matters: reproducibility requires precise content identification, not
just semantic versioning. Two datasets labeled "version 1.0" by different labs are
ambiguous; two datasets with identical content hashes are provably identical.
```

---

## Structural Suggestions

### 10. Methods Section Content

Should describe:
- How formal principles were derived (systematic review? expert consensus? iterative refinement?)
- Validation approach (if any): compliance checks on existing datasets?
- Community input process (if applicable)

### 11. Data/Code Availability

As manuscript about data organization, should be exemplar:
- "This manuscript and all source materials are version controlled at [repository]"
- "Analysis of related organizational frameworks available at [link to research]"
- "Compliant/non-compliant examples available at [link]"

So let's plan to have it under https://github.com/myyoda/paper or alike.

---

## Action Plan for Co-Authors

### Immediate (next iteration):
1. ✅ Add 4th pillar: Portable Environments section
2. ✅ Formalize "Do not look up" as P2.4
3. ✅ Clarify VAMP terminology (footnote or remove from title)

### Short-term (before submission):
4. ✅ Integrate organizational principles landscape research (Related Work section)
5. ✅ Add concrete examples for each principle (compliant vs non-compliant)
6. ✅ Complete Discussion section (comparisons, trade-offs, integration)
7. ✅ Expand provenance section with target formats (BEP028, RO-Crate, etc.)

### Polish (final draft):
8. ✅ Add principle priority guidance
9. ✅ Complete Methods section
10. ✅ Ensure exemplary Data/Code Availability section
11. ✅ Copy-edit for consistency (terminology, formatting)

---

## Offers of Assistance

As co-authors, we can contribute:

1. **Related Work section**: Draft complete section integrating 19-framework landscape research
2. **Discussion section**: Draft comparison subsections (DVC, Pachyderm, Kedro, platforms)
3. **Concrete examples**: Create compliant/non-compliant code examples for each principle
4. **4th pillar section**: Draft Portable Environments section with formal principles
5. **Figure creation**: If useful, can generate diagrams (architecture, comparison tables, timeline)

Let us know which sections would be most helpful for us to draft!

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
