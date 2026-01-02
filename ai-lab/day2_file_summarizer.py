from transformers import pipeline

# Load summarizer
summarizer = pipeline(
    "summarization",
    model="google/flan-t5-small"
)

# Read file
with open("sample.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Simple chunking (important)
def chunk_text(text, max_words=200):
    words = text.split()
    chunks = []
    for i in range(0, len(words), max_words):
        chunk = " ".join(words[i:i + max_words])
        chunks.append(chunk)
    return chunks

chunks = chunk_text(text)

summaries = []

for i, chunk in enumerate(chunks):
    summary = summarizer(
        chunk,
        max_length=80,
        min_length=30,
        do_sample=False
    )[0]["summary_text"]
    
    summaries.append(summary)

final_summary = "\n".join(summaries)

print("=== FINAL SUMMARY ===")
print(final_summary)
