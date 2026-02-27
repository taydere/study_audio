import requests

url = "https://themathpage.com/Arith/numeration.htm"
html = requests.get(url).text

with open("data/raw_html/lesson_01.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Downloaded lesson")
