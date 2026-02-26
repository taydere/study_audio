from spoken_math import spoken_math

MAX_WORDS = 400

with open("data/lessons_text/lesson_01.txt", encoding="utf-8") as f:
    text = spoken_math(f.read())

words = text.split()
chunks = []
current = []

for word in words:
    current.append(word)
    if len(current) >= MAX_WORDS:
        chunks.append(" ".join(current))
        current = []

if current:
    chunks.append(" ".join(current))

for i, chunk in enumerate(chunks, start=1):
    with open(f"data/lessons_text/lesson_01_chunk_{i}.txt", "w", encoding="utf-8") as f:
        f.write(chunk)

print(f"Created {len(chunks)} chunks")
