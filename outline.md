# SPAM: The Four Pillars of Idiomatic Dataset Version Control

## Abstract


## Introduction

What is Version Control  (Super brief, one sentence maybe 2 if critical)

How can VCS Datasets be useful?
- increased rigor: through transparency and reproducibility

Why it isnt done 
 - additional layer of complexity
 - difficulty prevents use
 - ad hoc solutions are expensive to create difficult to re-use

The importance of developing idioms
- increased readability
- increased reuse through interoperability
- common patterns simplify collaboration (between partners, reviewers, future work)
- common implementation enables automation

Pedagogy
- idioms should be easy to teach
- idioms should be easy to discuss
- developing idioms requires adoption
- scale from  "No VCS" -> "perfect", the goal is to progress (

## Results


### S → Self-contained: All Required Artifacts Are Versioned and Sourced

- Every dataset component MUST be versioned
- Every required artifact MUST be bundled or explicitly linked.

### P → Preserve: Software Environments Are Versioned and Managed

- Software environments SHOULD also be put under version control, just like datasets.

Benefits:
- promotes for portability
- helpful in limiting "dependency entropy"
- its all "there" for inspection

### A → Action Provenance is Recorded as Metadata

- All changes MUST be explicitly recorded.
- Data changes made by software should SHOULD complete execution instructions

Benefits:
- Results can be verified via re-execution
- Helpful for development
- Helpful for branching workflows (future related work)

### M → Modular: Compose discrete complentents

- Components that can be used individually SHOULD be versioned independently

Benefits: 
- keeps components decoupled.
- Encourages reuse, flexibility, and reparability
- each component should be tracked to earliest provenance, ie specific source.


## Discussion

Connection to FAIR
Other tools

## Methods

- Use cases
- Example implementation with git
- Example implementation with git-annex
- Example implementation in datalad
