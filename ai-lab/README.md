# Day 1 – Prompt vs Pipeline Behavior

Goal:
Understand how LLM behavior is driven more by instructions and constraints than by pipeline labels.

Key Observation:
Using the same model (FLAN-T5), different instructions produce different behaviors even across similar pipelines.

Current Status:
Foundational learning. Not production-ready.

# Day 2 - File Summarizer

Goal:
Understand:
1. How NLP systems handle file inputs, not just raw strings
2. How document length forces chunking (a real-world constraint)
3. How summaries degrade if structure is ignored
4. Why “works on a paragraph” ≠ “works in production”

Key observation:
LLMs have Context limits, Attention decay, Compression bias, Real documents (policies, reports, research notes) break naive summarization.

Current status:
Building internal capability.
