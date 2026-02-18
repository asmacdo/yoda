# Proposal: STAMPED as the encompassing acronym for all 7 dimensions

## Terms

**Research Object**: a collection of data, code, and metadata that together represent a complete unit of research output.
**Module**: a separately distributable collection of components.
- Examples: datasets, software packages, container images, analysis pipeline, submodule dependence...

**Component**: A trackable atomic object, part a module.
- Examples: raw data file, directory, Zarr, code, documentation, logs, records...
- Note that a module contains components, but not every component is a module.

**Workflow**: a sequence of computational steps that transform the data of the research object using code components to produce resultant output data.
- Examples: a Jupyter notebook that processes raw data to produce figures, a Nextflow pipeline that orchestrates multiple scripts to analyze data, a containerized application that acts as a block box for input and output.

**Provenance**: the detailed history of how a research object was created, modified, and executed over time.
It captures the lineage and transformations of data and code, providing a transparent record of the workflow's evolution.

Provenance can have many specific types:
- a history of modifications, which may include details of who made the change, when, and what was changed.
  - Examples: version control histories (`git log`), file metadata such as modification records (`stat`, EXIF, video/image headers).
- details about the computational environment, including software versions, dependencies, and configuration settings.
  - Examples: Container tags and digests, frozen environment records (`pip freeze`, `conda list`, `package-lock.json`), system information (OS version, hardware details).
- a record of the commands or scripts executed, along with their inputs, outputs, and logs.
  - Examples: W3C PROV records, `datalad rerun` logs.
- a trace of the workflow execution, showing how data and code were transformed over time.
  - Examples: CWLProv, Nextflow/Snakemake reports.



## STAMP(ED): Acronym Definition

A scientific Research Object follows **STAMP** guidelines when it adheres to the following principles:

- **S** — **S**elf-containment: a research object is a complete retrieval unit — it can be obtained and understood in its entirety without needing to reference external resources.
- **T** — **T**racking: the provenance of all components is recorded.
- **A** — **A**ctionability: Procedures within a research object can be carried out by following or executing its contents. This ranges from well-documented manual steps to fully automated workflows.
- **M** — **M**odularity: all modules are independent and composable.
- **P** — **P**ortability: Procedures can be executed on different host environments, given documented system requirements.

A scientific Research Object is fully **STAMPED** if it additionally meets the following ideal criteria:

- **E** — **E**phemerality: is able to perform all computation within a throwaway environment.
- **D** — **D**istributability: all modules and components are shareable in a persistent state.

These principles are ordered according to their importance:
- Self-Containment is the foundation upon which all others apply.
- Tracking applies to everything under Self-containment.
- Actionability is the cross-cutting quality that enables each dimension to have a practical method of enactment.
- Ephemerality and Distributability are the final aspirational goals.

Actionability is the most challenging definition to elucidate and so deserves a more detailed explanation:
  - It is the quality that elevates a research object from being a static collection of metadata to being an operational unit that can be executed or followed to achieve the same results.
  - Actionability can be thought of as the "doability" of a research object — it means that the procedures and instructions contained within are not just documented, but can actually be carried out by someone else (or by an automated system) to reproduce the results.
  - This could range from having clear, step-by-step instructions for manual execution to having fully automated scripts that can be run with a single command.

Note before we proceed there is a critical difference between simply sharing a Research Object and Distributing it in our sense:
- Sharing a Research Object might involve making it available on a platform like GitHub, but that may not be in a state that can be easily reproducible by others due to loose dependencies.
- Distributing a Research Object, on the other hand, implies that it is packaged in such a way that it can be retrieved in the same or similar state as intended, such as for a particular container digest or bundled executable (respecting the previous Portability principle, of course).



## Normative properties

To help understand each principle in practice, let us examine some of the qualifiers of each.

- To be **Self-contained**:
  - all modules and components needed to understand and execute the Research Object are retrievable as a single unit.
  - external dependencies are explicitly documented with retrieval instructions.
  - there are no implicit references to undocumented external resources.

- To be **Tracked**:
  - every component has version information (commit hash, tag, or identifier).
  - changes to components are recorded with timestamps and authorship.
  - provenance records capture the computational history, context, and transformations.

- To be **Actionable**:
  - instructions for executing procedures are present and unambiguous.
  - execution paths can be followed manually or automated programmatically.
  - the Research Object transitions from documentation to operational capability.

- To be **Modular**:
  - modules can be independently modified.
  - components are organized in logical, separable units.
  - modules can be composed together or used in isolation.

- To be **Portable**:
  - system requirements and dependencies are explicitly documented.
  - the Research Object is flexible enough to execute on different host environments without modification by the user.
  - environment specifications are machine-readable where possible.

- To be **Ephemeral**:
  - computation can occur in temporary, disposable environments.
  - results are reproducible without knowledge of previous runs.
  - no reliance on external configurations or host system states (such as OS registry modifications).

- To be **Distributable**:
  - all modules and components can be shared in a persistent, retrievable state.
  - dependencies are frozen or pinned to specific versions across systems.
  - the Research Object can be obtained by others in the same state as intended.



## Imperative requirements (RFC 2119)

The following statements express obligations and permissions of each principle.
The terms "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in the following text are to be interpreted as described in RFC 2119.

- **Self-containment**
  - S.1: All modules and components essential to replicate computational execution MUST be contained within a single top-level research object.
- **Tracking**
  - T.1: Version information MUST be tracked for all components.
  - T.2: All components SHOULD be tracked using the same content-addressed version control system.
- **Actionability**
  - A.1: Research object MUST contain sufficient instructions to reproduce all computational results.
- **Modularity**
  - M.1: Components SHOULD be organized in a modular structure.
  - M.2: Components MAY be included directly or linked as subdatasets.
- **Portability**
  - P.1: Procedures MUST NOT depend on undocumented host environment state (hardcoded paths, implicitly available tools, specific OS configurations)
  - P.2: Computational environments MUST be explicitly specified
  - P.3: Environment definitions MUST be version controlled.
- **Ephemerality**
  - E.1: Computational results SHOULD be computed in ephemeral environments.
- **Distributability**
  - D.1: Computational environments MUST be explicitly specified.
  - D.2: Environment specifications SHOULD support reproducible builds.
  - D.3: Environment definitions MUST be version controlled.
  - D.4: Environment components SHOULD be self-contained within the dataset.


  
## The Seven Dimensions

They are not all at the same level:

```
Foundation:     Self-Containment (boundary definition, P0)
Cross-cutting:  Actionability (operationally, not just declarative)
Core Pillars:   Tracking | Modularity | Portability
Ideals:         Ephemerality | Distributability
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
- Evokes a relation to **timestamping** — a core VCS concept
- Works as noun ("the STAMPED principles"), adjective ("a STAMPED dataset"), or verb ("we STAMPED this research")

**As an acronym:**
- 7 letters, 7 concepts, clean 1-to-1 mapping
- Each letter maps to a distinct, well-defined dimension

**Practically:**
- Sidesteps Star Wars trademark concerns raised in #7
- More descriptive than VAMP
- Enables natural compliance language: "Is your research object STAMPED?", "Let's STAMP your pipelines.", "Your research workflow has received the STAMP of approval!"



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
