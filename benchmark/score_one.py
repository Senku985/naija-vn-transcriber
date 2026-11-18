"""Score one transcript against its reference.

Usage:
    python benchmark/score_one.py "<reference text>" "<model output>"

The texts come from the command line, not from this file, so no
transcript text ever ends up in git.
"""
import sys

import jiwer
from scoring import normalize

if len(sys.argv) != 3:
    sys.exit(__doc__)

ref = normalize(sys.argv[1])
hyp = normalize(sys.argv[2])
print("REF:", ref)
print("HYP:", hyp)
print("WER:", jiwer.wer(ref, hyp))
print("CER:", jiwer.cer(ref, hyp))

out = jiwer.process_words(ref, hyp)
print(jiwer.visualize_alignment(out))
