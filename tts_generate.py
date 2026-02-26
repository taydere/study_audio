import subprocess
from pathlib import Path

VOICE = "piper/models/en_US-lessac-medium.onnx"
CONFIG = "piper/models/en_US-lessac-medium.onnx.json"

text_files = sorted(Path("data/lessons_text").glob("lesson_01_chunk_*.txt"))

for txt in text_files:
    wav_out = f"data/audio/{txt.stem}.wav"
    with open(txt, "r", encoding="utf-8") as f:
        subprocess.run(
            [
                "piper/piper",
                "--model", VOICE,
                "--config", CONFIG,
                "--output_file", wav_out
            ],
            input=f.read(),
            text=True
        )
    print(f"Generated {wav_out}")
