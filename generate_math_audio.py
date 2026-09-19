import asyncio
import os
import edge_tts

VOICE = "en-US-AnaNeural"
OUTPUT_DIR = "/home/nandan/Disk_D/Pimlo_app/src/assets/audio"
ANDROID_RAW_DIR = "/home/nandan/Disk_D/Pimlo_app/android/app/src/main/res/raw"

MATH_AUDIO_CLIPS = [
    # Operators & Math Speech
    ("math_plus", "Plus!"),
    ("math_minus", "Minus!"),
    ("math_times", "Times!"),
    ("math_divided", "Divided by!"),
    ("math_equals", "Equals!"),
    ("math_solve", "Can you solve this math problem?"),
    
    # Operation-specific visual hint audio
    ("math_hint_add", "Count all the items together to find the sum!"),
    ("math_hint_sub", "Count the items that are left after taking some away!"),
    ("math_hint_mult", "Count how many items there are across all the groups!"),
    ("math_hint_div", "Share the items equally into groups and see how many each group gets!"),
    
    # Level & Mode Audio
    ("math_level_easy", "Level one! Easy explorer!"),
    ("math_level_medium", "Level two! Smart adventurer!"),
    ("math_level_hard", "Level three! Math master challenge!"),
    ("math_quest_title", "Welcome to Math Quest! Let's play with numbers!"),
    ("math_great_job", "Awesome math wizard! You got it right!"),
]

async def generate_file(text: str, filename: str):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(ANDROID_RAW_DIR, exist_ok=True)
    filepath = os.path.join(OUTPUT_DIR, f"{filename}.mp3")
    android_filepath = os.path.join(ANDROID_RAW_DIR, f"{filename}.mp3")
    
    communicate = edge_tts.Communicate(text, VOICE, rate="-10%", pitch="+2Hz")
    await communicate.save(filepath)
    
    with open(filepath, 'rb') as src_file, open(android_filepath, 'wb') as dst_file:
        dst_file.write(src_file.read())
    print(f"🎵 Generated: {filename}.mp3 -> '{text}'")

async def main():
    print(f"🚀 Starting Math Audio Generation ({len(MATH_AUDIO_CLIPS)} files)...")
    for filename, text in MATH_AUDIO_CLIPS:
        await generate_file(text, filename)
    print("✅ All math audio generated successfully!")

if __name__ == "__main__":
    asyncio.run(main())
