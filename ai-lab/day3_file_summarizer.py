from transformers import pipeline

summarizer = pipeline(
    "text2text-generation",
    model="google/flan-t5-small"
)

def read_sections(file_path):
    sections = {}
    current_section = None

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("##"):
                current_section = line.replace("##", "").strip()
                sections[current_section] = ""
            elif current_section:
                sections[current_section] += line + " "
    return sections

sections = read_sections("sample_text.txt")

structured_summary = {}

#output prompt 1:
# You are assisting a policymaker.
# Summarize the following section in 3–4 bullet points.
# Focus only on what is decision-relevant.

for section, content in sections.items():
    prompt = f"""

Extract 3–4 distinct, non-redundant bullet points.
Each bullet must introduce a new idea.
Do NOT repeat wording or concepts.
If the text lacks detail, state that explicitly.


Section: {section}
Text: {content}
"""
    output = summarizer(
        prompt,
        max_length=120,
        repetition_penalty=2.0,
        do_sample=False
    )[0]["generated_text"]

    structured_summary[section] = output

print("=== STRUCTURED POLICY BRIEF ===\n")
for section, summary in structured_summary.items():
    print(f"{section}:")
    print(summary)
    print("-" * 40)

