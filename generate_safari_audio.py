import asyncio
import os
import edge_tts

VOICE = "en-US-AnaNeural"
OUTPUT_DIR = "/home/nandan/Disk_D/Pimlo_app/src/assets/audio"
ANDROID_RAW_DIR = "/home/nandan/Disk_D/Pimlo_app/android/app/src/main/res/raw"

WORDS = [
    # 3 Letters
    ("cat", "Cat"),
    ("dog", "Dog"),
    ("fox", "Fox"),
    ("pig", "Pig"),
    ("cow", "Cow"),
    ("sun", "Sun"),
    ("owl", "Owl"),
    ("bee", "Bee"),
    ("bat", "Bat"),
    ("car", "Car"),

    # 4 Letters
    ("lion", "Lion"),
    ("duck", "Duck"),
    ("frog", "Frog"),
    ("bear", "Bear"),
    ("fish", "Fish"),
    ("bird", "Bird"),
    ("deer", "Deer"),
    ("star", "Star"),
    ("moon", "Moon"),
    ("boat", "Boat"),

    # 5 Letters
    ("tiger", "Tiger"),
    ("panda", "Panda"),
    ("zebra", "Zebra"),
    ("horse", "Horse"),
    ("sheep", "Sheep"),
    ("whale", "Whale"),
    ("shark", "Shark"),
    ("apple", "Apple"),
    ("pizza", "Pizza"),
    ("train", "Train"),

    # 6 Letters
    ("monkey", "Monkey"),
    ("rabbit", "Rabbit"),
    ("turtle", "Turtle"),
    ("banana", "Banana"),
    ("orange", "Orange"),
    ("carrot", "Carrot"),
    ("parrot", "Parrot"),
    ("dolphin", "Dolphin"),
    ("kitten", "Kitten"),
    ("rocket", "Rocket"),
]

async def generate_word(word_id: str, spoken_word: str):
    filename = f"word_{word_id}.mp3"
    filepath = os.path.join(OUTPUT_DIR, filename)
    android_filepath = os.path.join(ANDROID_RAW_DIR, filename)
    
    communicate = edge_tts.Communicate(spoken_word, VOICE, rate="-10%", pitch="+2Hz")
    await communicate.save(filepath)
    
    with open(filepath, 'rb') as src_file, open(android_filepath, 'wb') as dst_file:
        dst_file.write(src_file.read())
    print(f"🎵 Generated: {filename} -> '{spoken_word}'")

async def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(ANDROID_RAW_DIR, exist_ok=True)
    print(f"🚀 Generating {len(WORDS)} Word Safari audio files...")
    tasks = [generate_word(word_id, spoken) for word_id, spoken in WORDS]
    await asyncio.gather(*tasks)
    print("✨ All Safari word audio files generated successfully!")

if __name__ == "__main__":
    asyncio.run(main())
