# ShortsForge 🎬
# Made by cr1ms0ncode 🚀
#
# Project Purpose:
# Generate viral short-form video scripts using Gemini AI.
#
# Features:
# - Platform specific scripts
# - Multiple tones
# - Hook generation
# - CTA generation
# - Hashtag generation
# - Save generated script to file


from google import genai


# --------------------------------
# Function 1: Display Banner
# --------------------------------
def banner():

    print("=" * 50)
    print("   ShortsForge 🎬 - AI Script Generator")
    print("   Made by cr1ms0ncode 🚀")
    print("=" * 50)
    print()


# --------------------------------
# Function 2: Generate AI Script
# --------------------------------
def generate_script(
    client,
    platform,
    topic,
    tone
):

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


# --------------------------------
# Function 3: Save Script to File
# --------------------------------
def save_script(script):

    with open(
        "generated_script.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(script)

    print("✅ Script saved successfully!")
    print("📄 File Name: generated_script.txt")


# --------------------------------
# Main Program Starts Here
# --------------------------------

# Show project banner
banner()

print("SETUP: aistudio.google.com se API key lo")
print()

# User enters Gemini API key
api_key = input("Enter your Gemini API Key: ")

# Create Gemini Client
client = genai.Client(api_key=api_key)

print()
print("Platforms: YouTube Shorts, Instagram Reels, TikTok")

# User Inputs
platform = input("Platform choose karo: ")
topic = input("Video topic kya hai: ")
tone = input(
    "Tone (funny/motivational/educational): "
)

print()
print("Generating viral script... 🎬")
print()

# Generate Script
script = generate_script(
    client,
    platform,
    topic,
    tone
)

# Display Result
print("=" * 50)
print(script)
print("=" * 50)

# Save Script
save_script(script)