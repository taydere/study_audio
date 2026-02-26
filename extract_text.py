from bs4 import BeautifulSoup
from readability import Document

with open("data/raw_html/lesson_01.html", encoding="utf-8") as f:
    html = f.read()

doc = Document(html)
clean_html = doc.summary()

soup = BeautifulSoup(clean_html, "lxml")

text_blocks = []
for p in soup.find_all(["p", "h1", "h2", "h3"]):
    text = p.get_text(strip=True)
    if len(text) > 30:
        text_blocks.append(text)

lesson_text = "\n\n".join(text_blocks)

with open("data/lessons_text/lesson_01.txt", "w", encoding="utf-8") as f:
    f.write(lesson_text)

print("Extracted lesson text")
