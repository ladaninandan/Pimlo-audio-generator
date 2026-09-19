import asyncio
import os
import edge_tts

VOICE = "en-US-AnaNeural"
OUTPUT_DIR = "/home/nandan/Disk_D/Pimlo_app/src/assets/audio"
ANDROID_RAW_DIR = "/home/nandan/Disk_D/Pimlo_app/android/app/src/main/res/raw"

COLOR_AUDIO_CLIPS = [
    # Color Names
    ("color_red", "Red!"),
    ("color_blue", "Blue!"),
    ("color_yellow", "Yellow!"),
    ("color_green", "Green!"),
    ("color_orange", "Orange!"),
    ("color_purple", "Purple!"),
    ("color_pink", "Pink!"),
    ("color_brown", "Brown!"),
    ("color_black", "Black!"),
    ("color_white", "White!"),
    ("color_cyan", "Cyan!"),
    ("color_gold", "Gold!"),
    
    # Prompts: Find the color
    ("prompt_find_red", "Can you find the Red color?"),
    ("prompt_find_blue", "Can you find the Blue color?"),
    ("prompt_find_yellow", "Can you find the Yellow color?"),
    ("prompt_find_green", "Can you find the Green color?"),
    ("prompt_find_orange_col", "Can you find the Orange color?"),
    ("prompt_find_purple", "Can you find the Purple color?"),
    ("prompt_find_pink", "Can you find the Pink color?"),
    ("prompt_find_brown", "Can you find the Brown color?"),
    ("prompt_find_black", "Can you find the Black color?"),
    ("prompt_find_white", "Can you find the White color?"),
    ("prompt_find_cyan", "Can you find the Cyan color?"),
    ("prompt_find_gold", "Can you find the Gold color?"),
    
    # Mode & Feedback
    ("prompt_color_quest", "Welcome to Color Splash! Let's explore and find bright colors!"),
    ("color_mix_magic", "Magic mix! Look what color we made!"),
    ("color_great_job", "Awesome! That is the right color!"),
    ("color_try_again", "Good try! Look for the matching color!"),
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
    print(f"🎨 Generated: {filename}.mp3 -> '{text}'")

async def main():
    print(f"🚀 Starting Color Audio Generation ({len(COLOR_AUDIO_CLIPS)} files)...")
    for filename, text in COLOR_AUDIO_CLIPS:
        await generate_file(text, filename)
    print("✅ All color audio generated successfully!")

if __name__ == "__main__":
    asyncio.run(main())
