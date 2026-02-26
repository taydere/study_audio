import requests

url = "https://www.themathpage.com/Arith/intro.htm"
html = requests.get(url).text

with open("data/raw_html/lesson_01.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Downloaded lesson")
