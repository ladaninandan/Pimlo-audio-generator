# Pimlo Audio Generator

Speech & audio asset generator for Pimlo / ABC Adventure using `edge-tts` with high-clarity neural child storytelling voices (`en-US-AnaNeural`).

## Features
- Generates phonics, letter sounds, and word associations (A-Z).
- Generates positive reinforcement audio feedback ("Awesome job!", "Super star!").
- Outputs audio directly to Pimlo mobile app asset folder.

## Setup & Usage

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python generate_alphabet_audio.py
```
