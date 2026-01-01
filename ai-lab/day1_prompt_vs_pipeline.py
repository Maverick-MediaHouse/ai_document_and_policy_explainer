from transformers import pipeline

text = """
India is a land of great diversity, rich heritage, and remarkable unity. This paragraph on India highlights its natural beauty, cultural traditions, festivals, and achievements. From majestic mountains to vibrant cities, India inspires its people with the message of unity in diversity. Explore what makes India unique and why it is loved by millions across the world. India is a vast country, stretching from the snowy Himalayas in the north to the tropical coastlines in the south. It is the seventh-largest country in the world. India’s landscapes range from the Thar Desert and fertile plains to dense forests and mighty rivers. The country’s geography supports diverse communities and traditions, making India a fascinating place for all. India’s heritage reflects centuries of civilisation, with heritage sites like the Taj Mahal, Red Fort, and Qutub Minar attracting millions. Read more about India’s heritage and how it shapes the country’s pride and identity. India is well-known for its colorful culture, languages, and festivals. People celebrate traditional Indian festivals like Diwali, Holi, Eid, Christmas, and Onam with much excitement. Every festival shares a story or brings a valuable lesson of unity, love, and respect among people. Indian food, music, dance, and art forms like Bharatnatyam and Kathak add beauty to its cultural landscape. This paragraph on India inspires students to love their nation and contribute to its bright future. India is a beautiful country in South Asia. It is famous for its unity in diversity. The Himalayas guard India’s north. Many languages and festivals are found here. The national flag of India has three colors. Indian festivals like Diwali bring people together. Indian army guards the country with courage. Farming is an important occupation in villages. India believes in peace and respect for all. We are proud to be Indians. India teaches us the moral value of unity and respect. Different communities live together, share customs, and celebrate each other’s festivals. The country shows how to value every culture while living in harmony. The message is clear—unity in diversity is India’s strength and gives hope for a peaceful world.
"""

# Summarization pipeline
summarizer = pipeline(
    "summarization",
    model="google/flan-t5-small"
)

summary_output = summarizer(
    text,
    max_length=120,
    min_length=40,
    do_sample=False
)

# Text-to-text generation with explicit instruction
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-small"
)

prompt = f"Rewrite the following text as a policy warning:\n\n{text}"

generation_output = generator(
    prompt,
    max_length=150,
    do_sample=False
)

print("=== Summarization Output ===")
print(summary_output[0]["summary_text"])

print("\n=== Text2Text Output ===")
print(generation_output[0]["generated_text"])
