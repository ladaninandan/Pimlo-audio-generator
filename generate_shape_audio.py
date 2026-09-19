import asyncio
import os
import edge_tts

VOICE = "en-US-AnaNeural"
OUTPUT_DIR = "/home/nandan/Disk_D/Pimlo_app/src/assets/audio"
ANDROID_RAW_DIR = "/home/nandan/Disk_D/Pimlo_app/android/app/src/main/res/raw"

SHAPES = [
    ("circle", "Circle"),
    ("square", "Square"),
    ("triangle", "Triangle"),
    ("star", "Star"),
    ("heart", "Heart"),
    ("rectangle", "Rectangle"),
    ("diamond", "Diamond"),
    ("oval", "Oval"),
    ("crescent", "Crescent"),
    ("pentagon", "Pentagon"),
]

async def generate_shape(shape_id: str, spoken_name: str):
    filename = f"shape_{shape_id}.mp3"
    filepath = os.path.join(OUTPUT_DIR, filename)
    android_filepath = os.path.join(ANDROID_RAW_DIR, filename)
    
    communicate = edge_tts.Communicate(spoken_name, VOICE, rate="-10%", pitch="+2Hz")
    await communicate.save(filepath)
    
    with open(filepath, 'rb') as src_file, open(android_filepath, 'wb') as dst_file:
        dst_file.write(src_file.read())
    print(f"🎵 Generated: {filename} -> '{spoken_name}'")

async def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(ANDROID_RAW_DIR, exist_ok=True)
    print(f"🚀 Generating {len(SHAPES)} Shape audio files...")
    tasks = [generate_shape(shape_id, spoken) for shape_id, spoken in SHAPES]
    await asyncio.gather(*tasks)
    print("✨ All Shape audio files generated successfully!")

if __name__ == "__main__":
    asyncio.run(main())
