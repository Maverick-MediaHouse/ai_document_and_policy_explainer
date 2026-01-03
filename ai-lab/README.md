# Day 1 – Prompt vs Pipeline Behavior (01-01-2026)

Goal:
Understand how LLM behavior is driven more by instructions and constraints than by pipeline labels.

Key Observation:
Using the same model (FLAN-T5), different instructions produce different behaviors even across similar pipelines.

Current Status:
Foundational learning. Not production-ready.

# Day 2 - File Summarizer (02-01-2026)

Learned that chunking is required due to context limits, but naive chunking causes loss of global coherence, repetition, and structural confusion unless document sections are explicitly preserved.
Goal: Understand:
1. How NLP systems handle file inputs, not just raw strings
2. How document length forces chunking (a real-world constraint)
3. How summaries degrade if structure is ignored
4. Why “works on a paragraph” ≠ “works in production”

Key observation:
LLMs have Context limits, Attention decay, Compression bias, Real documents (policies, reports, research notes) break naive summarization.

Current status:
Building internal capability.

# Day 3 - Structured file summarization (03-01-2026)

Goal: To stabilize long-document summarization by introducing explicit structure, role-based prompting, and output constraints, and to analyze failure modes (repetition, ambiguity) as diagnostic signals rather than model errors.

Key Observations:
Structure functions as an external control mechanism: LLMs do not infer document structure; they strictly follow the structure imposed through headers, roles, and formatting constraints.
Prompting cannot compensate for weak source material: Repetitive or vague outputs often indicate low information density in the input text, not a failure of the model.
Repetition is a diagnostic signal: Repeated ideas reveal sections lacking distinct semantic units and can be used to flag poorly written or low-quality documents.
Constraints outweigh creativity in production systems: Explicit rules such as non-redundancy, allowance for uncertainty, and requirement for new information significantly improve output stability and reliability.

Current Status:
Transitioned from ad-hoc prompting to constraint-driven, structure-aware summarization

Developing intuition for LLM failure analysis based on input quality and control design

Positioned to move from exploratory learning to comparative and evaluative outputs (Day 4 focus)

### This stage marks a shift from learning how to use LLMs to understanding how LLM behavior is operationally controlled in real systems.
1: Structure is an external control mechanism. LLMs do not discover structure — they obey structure.

2: Prompting cannot compensate for weak source material. Repetition is often a signal of low information density, not model failure.
