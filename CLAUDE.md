# Naija Voice Note Transcriber

Portfolio/learning project: an Android app that transcribes WhatsApp voice notes, built for Nigerian speech (Nigerian-accented English, Pidgin, Yoruba/Igbo/Hausa, code-switching, noisy audio).

## About the developer
200-level Computer Engineering student. Strongest in Python; somewhat familiar with PostgreSQL and React. New to: React Native, audio processing, ML evaluation.

## Stack
- Backend: Python, FastAPI, faster-whisper, ffmpeg
- Database: PostgreSQL
- App: React Native (Expo) + expo-share-intent, development build
- Evaluation: jiwer (WER), pandas

## Repo layout
```
benchmark/   scripts for running models and scoring (Phase 0)
backend/     FastAPI service (Phase 1)
app/         React Native app (Phase 2)
results/     score tables (CSV) and charts: committed
data/        audio + reference transcripts: NEVER committed
```

## Hard rules
- NEVER commit anything in `data/`, any audio file (.opus, .ogg, .wav, .mp3, .m4a), or any transcript text. Only aggregate scores go in `results/`. Keep `.gitignore` enforcing this.
- Keep everything free / free-tier. No paid APIs.

## How to work with me
- This is a learning project. Before editing, explain your plan and wait for my go-ahead on anything non-trivial.
- Explain the *why* behind code and design choices, especially in areas new to me.
- Prefer small, runnable steps I can test over large code dumps.
- I want to write the core logic myself (WER scoring, FastAPI endpoint, share-intent handling). For those, guide and review rather than write it for me unless I ask.
- Tell me plainly when my approach is wrong or there's a better way.
- Write clear commit messages.

## Current phase
Phase 0: Benchmark Whisper tiny/base/small on ~20 self-recorded voice notes + an AfriSpeech-200 slice. See the Phase 0 checklist in the claude.ai Project.
