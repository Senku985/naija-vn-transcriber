import subprocess
import sys
import time

import numpy as np
from faster_whisper import WhisperModel
import shutil

if shutil.which("ffmpeg") is None:
    sys.exit("ffmpeg not found on PATH. Restart your terminal/PyCharm after installing it.")

def load_audio(path, sample_rate=16000):
    """Decode any audio file to the format Whisper expects:
    mono, 16 kHz, float32 samples between -1.0 and 1.0."""
    cmd = [
        "ffmpeg", "-nostdin",
        "-i", path,          # input file (.opus, .mp3, anything)
        "-f", "s16le",       # output raw 16-bit integers, no file header
        "-ac", "1",          # 1 channel (mono)
        "-ar", str(sample_rate),  # resample to 16,000 samples per second
        "-",                 # write to stdout instead of a file
    ]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    # 16-bit ints range from -32768 to 32767; dividing scales them to -1..1
    return np.frombuffer(raw, np.int16).astype(np.float32) / 32768.0



audio_path = sys.argv[1]
audio = load_audio(audio_path)

model_size = sys.argv[2] if len(sys.argv) > 2 else "tiny"
model = WhisperModel(model_size, device="cpu", compute_type="int8")

language = sys.argv[3] if len(sys.argv) > 3 else None  # None = auto-detect

start = time.time()
segments, info = model.transcribe(audio, language=language)  # pass the array, not the path
text = " ".join(seg.text.strip() for seg in segments)
elapsed = time.time() - start


print(f"Detected language: {info.language} ({info.language_probability:.0%})")
print(f"Audio: {info.duration:.1f}s | Processing: {elapsed:.1f}s")
print(f"Transcript: {text}")
if info.all_language_probs:
    top3 = sorted(info.all_language_probs, key=lambda x: x[1], reverse=True)[:3]
    print("Top languages:", ", ".join(f"{lang} {p:.0%}" for lang, p in top3))

