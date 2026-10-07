# ShortsForge 🎬
# Made by cr1ms0ncode 🚀
#
# Generate short-form video script drafts with Gemini AI.

from getpass import getpass

from google import genai


PLATFORMS = ("YouTube Shorts", "Instagram Reels", "TikTok")
TONES = ("funny", "motivational", "educational")


def banner():
    print("=" * 50)
    print("   ShortsForge 🎬 - AI Script Generator")
    print("   Made by cr1ms0ncode 🚀")
    print("=" * 50)
    print()


def generate_script(client, platform, topic, tone):
    prompt = f"""
Create an engaging draft for a {platform} video about '{topic}'.

Tone: {tone}
Language: Hinglish (Hindi + English mix)

Format:
HOOK (first 3 seconds)
MAIN CONTENT (key points)
CTA (call to action)
HASHTAGS (10 relevant hashtags)

Aim for a script under 60 seconds. This is a draft and is not guaranteed to go viral.
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )
    script = response.text
    if not script or not script.strip():
        raise RuntimeError("Gemini returned an empty response.")
    return script


def save_script(script):
    with open("generated_script.txt", "w", encoding="utf-8") as file:
        file.write(script)

    print("✅ Script saved successfully!")
    print("📄 File Name: generated_script.txt")


def choose_option(prompt, options):
    choices = {str(index): option for index, option in enumerate(options, start=1)}
    while True:
        print(" / ".join(f"{key}. {value}" for key, value in choices.items()))
        choice = input(prompt).strip()
        if choice in choices:
            return choices[choice]
        print(f"Please choose a number from 1 to {len(choices)}.")


def main():
    banner()
    print("Get an API key from aistudio.google.com. The key is not displayed while typing.")
    api_key = getpass("Enter your Gemini API key: ").strip()
    if not api_key:
        print("❌ An API key is required.")
        return

    platform = choose_option("Choose platform: ", PLATFORMS)
    topic = input("Video topic: ").strip()
    while not topic:
        print("Topic cannot be empty.")
        topic = input("Video topic: ").strip()
    tone = choose_option("Choose tone: ", TONES)

    print()
    print("Generating script draft... 🎬")
    print()
    try:
        client = genai.Client(api_key=api_key)
        script = generate_script(client, platform, topic, tone)
    except Exception:
        print("❌ Script generation failed. Check your API key and network, then try again.")
        return

    print("=" * 50)
    print(script)
    print("=" * 50)
    save_script(script)


if __name__ == "__main__":
    main()
