import re

def spoken_math(text):
    replacements = {
        "+": " plus ",
        "-": " minus ",
        "×": " times ",
        "÷": " divided by ",
        "=": " equals "
    }
    for k, v in replacements.items():
        text = text.replace(k, v)

    text = re.sub(r"\b(\d+)\b", lambda m: m.group(1), text)
    return text
