from google import genai

print("=" * 50)
print("   ShortsForge 🎬 - AI Script Generator")
print("   Made by cr1ms0ncode 🚀")
print("=" * 50)
print()
print("SETUP: aistudio.google.com se API key lo")
print()

api_key = input("Enter your Gemini API Key: ")
client = genai.Client(api_key=api_key)

print()
print("Platforms: YouTube Shorts, Instagram Reels, TikTok")
platform = input("Platform choose karo: ")
topic = input("Video topic kya hai: ")
tone = input("Tone (funny/motivational/educational): ")

print()
print("Generating viral script... 🎬")
print()

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

print("=" * 50)
print(response.text)
print("=" * 50)