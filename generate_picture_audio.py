import asyncio
import os
import edge_tts

VOICE = "en-US-AnaNeural"
OUTPUT_DIR = "/home/nandan/Disk_D/Pimlo_app/src/assets/audio"
ANDROID_RAW_DIR = "/home/nandan/Disk_D/Pimlo_app/android/app/src/main/res/raw"

PUZZLE_AUDIO_CLIPS = [
    ("prompt_complete_picture", "Complete the picture! Pick the matching piece below!"),
    ("puzzle_completed_cheer", "Woohoo! You completed the picture!"),
    ("puzzle_snap", "Click! Perfect fit!"),
    ("puzzle_mode_half", "Half and half matching puzzle!"),
    ("puzzle_mode_shape", "Shape cut-out puzzle! Find the missing shape!"),
    ("puzzle_find_piece", "Which piece fits in the missing spot?"),
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
    print(f"🧩 Generated: {filename}.mp3 -> '{text}'")

async def main():
    print(f"🚀 Starting Picture Puzzle Audio Generation ({len(PUZZLE_AUDIO_CLIPS)} files)...")
    for filename, text in PUZZLE_AUDIO_CLIPS:
        await generate_file(text, filename)
    print("✅ All picture puzzle audio generated successfully!")

if __name__ == "__main__":
    asyncio.run(main())
