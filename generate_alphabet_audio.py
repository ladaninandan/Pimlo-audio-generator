import asyncio
import os
import edge_tts

# Voice: en-US-AnaNeural is a warm, gentle voice designed specifically for kids and storytelling
VOICE = "en-US-AnaNeural"
OUTPUT_DIR = "/home/nandan/Disk_D/Pimlo_app/src/assets/audio"

ALPHABET_DATA = [
    ("A", "Apple", "ah"),
    ("B", "Ball", "buh"),
    ("C", "Cat", "kuh"),
    ("D", "Dog", "duh"),
    ("E", "Elephant", "eh"),
    ("F", "Fish", "ff"),
    ("G", "Grapes", "guh"),
    ("H", "Hat", "huh"),
    ("I", "Igloo", "ih"),
    ("J", "Juice", "juh"),
    ("K", "Kite", "kuh"),
    ("L", "Lion", "ll"),
    ("M", "Monkey", "mm"),
    ("N", "Nest", "nn"),
    ("O", "Orange", "awe"),
    ("P", "Penguin", "puh"),
    ("Q", "Queen", "kwuh"),
    ("R", "Rabbit", "err"),
    ("S", "Star", "sss"),
    ("T", "Tiger", "tuh"),
    ("U", "Umbrella", "uh"),
    ("V", "Violin", "vv"),
    ("W", "Watch", "wuh"),
    ("X", "Xylophone", "ks"),
    ("Y", "Yo-yo", "yuh"),
    ("Z", "Zebra", "zzz"),
]

FEEDBACK_CLIPS = [
    ("encourage_awesome", "Awesome job! You earned stars!"),
    ("encourage_great", "Great job! Let's keep going!"),
    ("encourage_you_did_it", "Woohoo! You did it!"),
    ("encourage_super", "Super star! That was amazing!"),
    ("gentle_try_again", "Almost! Let's give it another try!"),
    ("gentle_oops", "Oops! Let's try that stroke again!"),
    ("session_break", "Great job learning today! Time for a little stretch and water break!"),
]

async def generate_file(text: str, filename: str):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filepath = os.path.join(OUTPUT_DIR, filename)
    # Slow down speed by 10% for child clarity and early sight-hearing
    communicate = edge_tts.Communicate(text, VOICE, rate="-10%", pitch="+2Hz")
    await communicate.save(filepath)
    print(f"🎵 Generated: {filename} -> '{text}'")

async def main():
    print("🚀 Starting Audio Asset Generation for ABC Adventure...")
    
    # 1. Generate Letter Lesson Prompts (FR-3: Letter Shape + Name + Sound)
    for letter, word, phonetic in ALPHABET_DATA:
        # Simple letter name
        await generate_file(f"Letter {letter}", f"letter_{letter.lower()}.mp3")
        
        # Teaching sentence (Connecting Name + Phonic Sound + Word)
        lesson_text = f"{letter}. {letter} says {phonetic}. {letter} is for {word}!"
        await generate_file(lesson_text, f"{letter.lower()}_phonics.mp3")

    # 2. Generate Gentle Multi-Sensory Feedback Audio
    for clip_name, speech_text in FEEDBACK_CLIPS:
        await generate_file(speech_text, f"{clip_name}.mp3")

    print("\n✅ All audio assets successfully generated and saved to:")
    print(f"👉 {OUTPUT_DIR}")

if __name__ == "__main__":
    asyncio.run(main())
