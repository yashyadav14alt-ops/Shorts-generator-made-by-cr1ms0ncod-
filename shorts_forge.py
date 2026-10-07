"""Generate a short-form video script with Google Gemini."""

import os
import sys

from dotenv import load_dotenv
from google import genai

PLATFORMS = {"youtube shorts", "instagram reels", "tiktok"}
TONES = {"funny", "motivational", "educational"}


def generate_script(client, platform: str, topic: str, tone: str) -> str:
    if platform.casefold() not in PLATFORMS:
        raise ValueError("Choose YouTube Shorts, Instagram Reels, or TikTok.")
    if tone.casefold() not in TONES:
        raise ValueError("Choose funny, motivational, or educational tone.")
    if not topic.strip():
        raise ValueError("Enter a video topic.")

    prompt = f"""Create a short-form video script about: {topic.strip()}
Platform: {platform.strip()}
Tone: {tone.strip()}
Language: Hinglish (Hindi + English mix)

Include a hook, concise main content, a natural call to action, and relevant hashtags.
Aim for a spoken script under 60 seconds. Do not promise virality or invent factual claims.
"""
    response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
    script = response.text
    if not script or not script.strip():
        raise RuntimeError("The model returned an empty script.")
    return script.strip()


def save_script(script: str, path: str = "generated_script.txt") -> None:
    with open(path, "w", encoding="utf-8") as script_file:
        script_file.write(script + "\n")


def main() -> int:
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key or api_key == "your_api_key_here":
        print("GEMINI_API_KEY is missing. Copy .env.example to .env and add your key.", file=sys.stderr)
        return 1

    print("ShortsForge · AI script generator")
    print("Platforms: YouTube Shorts, Instagram Reels, TikTok")
    platform = input("Platform: ").strip()
    topic = input("Video topic: ").strip()
    tone = input("Tone (funny/motivational/educational): ").strip()
    try:
        script = generate_script(genai.Client(api_key=api_key), platform, topic, tone)
    except Exception as error:
        print(f"Script generation failed: {error}", file=sys.stderr)
        return 1

    print("\n" + script)
    save_script(script)
    print("\nScript saved to generated_script.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
