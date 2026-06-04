# ShortsForge 🎬
# Made by cr1ms0ncode 🚀
#
# Purpose:
# Generate viral short-form video scripts using Gemini AI.
# Supports YouTube Shorts, Instagram Reels and TikTok.

from google import genai


# -------------------------------
# Function 1: Show project banner
# -------------------------------
def banner():
    print("=" * 50)
    print("   ShortsForge 🎬 - AI Script Generator")
    print("   Made by cr1ms0ncode 🚀")
    print("=" * 50)
    print()


# ------------------------------------
# Function 2: Generate script using AI
# ------------------------------------
def generate_script(client, platform, topic, tone):

    prompt = f"""
Create a viral {platform} script about '{topic}'.

Tone: {tone}

Language: Hinglish (Hindi + English mix)

Format:

HOOK (first 3 seconds - attention grabbing)

MAIN CONTENT (key points)

CTA (call to action)

HASHTAGS (10 relevant hashtags)

Keep it under 60 seconds.
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text


# -----------------------
# Main Program Starts Here
# -----------------------

# Display project title
banner()

print("SETUP: aistudio.google.com se API key lo")
print()

# Take Gemini API key from user
api_key = input("Enter your Gemini API Key: ")

# Create Gemini client
client = genai.Client(api_key=api_key)

print()
print("Platforms: YouTube Shorts, Instagram Reels, TikTok")

# User inputs
platform = input("Platform choose karo: ")
topic = input("Video topic kya hai: ")
tone = input("Tone (funny/motivational/educational): ")

print()
print("Generating viral script... 🎬")
print()

# Generate script
script = generate_script(
    client,
    platform,
    topic,
    tone
)

# Display result
print("=" * 50)
print(script)
print("=" * 50)