# ShortsForge

A small Python CLI that uses Google's Gemini API to draft short-form video scripts in Hinglish for YouTube Shorts, Instagram Reels, or TikTok.

## What it does

- Prompts for a platform, topic, and tone (funny, motivational, or educational).
- Generates a draft with a hook, main content, call to action, and hashtag suggestions.
- Saves the result as **generated_script.txt** in the current working directory. A new run overwrites that file.

Generated content is a draft. It is not checked for factual accuracy and is not guaranteed to perform well or go viral. Review it before publishing.

## Requirements

- Python
- A Gemini API key from [Google AI Studio](https://aistudio.google.com/)

## Setup

From the repository directory:

~~~bash
python -m pip install -r requirements.txt
python shorts_forge.py
~~~

On Windows, use **python** in PowerShell or Command Prompt. When prompted, enter the API key; terminal input is hidden while typing. The key is used to create the Gemini client and is not written to a file by this program.

## Limitations

This is a local CLI prototype. It does not publish videos, verify generated claims, or preserve previous output files. Keep API keys private and follow Google's API terms and data handling guidance.
