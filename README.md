# ShortsForge

A command-line demo that drafts short-form video scripts in Hinglish with Google Gemini.

## Features

- YouTube Shorts, Instagram Reels, and TikTok formats
- Funny, motivational, and educational tones
- Hook, main content, call to action, and hashtag suggestions
- Saves the generated draft to `generated_script.txt`

Generated content may be inaccurate and does not guarantee reach or virality. Review factual claims and platform requirements before publishing.

## Setup

Requires Python 3.10 or newer.

```sh
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and set `GEMINI_API_KEY` using a key from [Google AI Studio](https://aistudio.google.com/). Keep `.env` private; Git ignores it.

Run:

```sh
python shorts_forge.py
```
