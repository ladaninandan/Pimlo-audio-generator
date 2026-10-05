import asyncio
import os
import edge_tts

VOICE = "en-US-AnaNeural"  # Gentle, clear storytelling voice
RATE = "-10%"             # Slightly slower for young learners to follow along easily
OUTPUT_DIR = "/home/nandan/Disk_D/Pimlo_app/src/assets/audio"
ANDROID_RAW_DIR = "/home/nandan/Disk_D/Pimlo_app/android/app/src/main/res/raw"

STORY_AUDIO_ITEMS = [
    # Leo and the Red Ball
    ("story_leo_1", "Leo the little lion had a bright red ball. He loved to bounce it high into the blue sky."),
    ("story_leo_2", "Bounce, bounce, bounce! The red ball rolled behind a big green tree."),
    ("story_leo_3", "Milo the friendly monkey looked down from the tree and smiled. Here is your ball, Leo!"),
    ("story_leo_4", "Leo and Milo played together all afternoon. They became the best of jungle friends!"),
    ("story_leo_quiz", "Who helped Leo find his red ball?"),

    # Pip's Rocket Adventure
    ("story_pip_1", "Pip built a shiny silver rocket in his backyard. Today, I will touch a star! he said."),
    ("story_pip_2", "Three, two, one... Blast off! The rocket zoomed through fluffy white clouds into outer space."),
    ("story_pip_3", "He saw the glowing moon and a friendly panda waving from a shiny spaceship."),
    ("story_pip_4", "Pip caught a golden star in his pocket and flew safely home before bedtime."),
    ("story_pip_quiz", "What did Pip catch in his pocket?"),

    # Barnaby Bunny's Big Crunch
    ("story_bunny_1", "Barnaby the fluffy bunny woke up with a very hungry tummy."),
    ("story_bunny_2", "He hopped into the sunny garden and saw three juicy orange carrots."),
    ("story_bunny_3", "Crunch, crunch, crunch! Carrots make bunnies jump super high into the air."),
    ("story_bunny_4", "Barnaby shared his last carrot with his sister Bella. Sharing makes everyone happy!"),
    ("story_bunny_quiz", "What color were Barnaby's favorite carrots?"),
]

async def generate_sentence(audio_id: str, sentence_text: str):
    filename = f"{audio_id}.mp3"
    raw_path = os.path.join(ANDROID_RAW_DIR, filename)
    asset_path = os.path.join(OUTPUT_DIR, filename)

    print(f"Generating full sentence audio: {filename}...")
    communicate = edge_tts.Communicate(sentence_text, VOICE, rate=RATE)
    await communicate.save(raw_path)

    # Also copy to asset folder
    if os.path.exists(raw_path):
        import shutil
        shutil.copy2(raw_path, asset_path)
        print(f" Saved to {raw_path}")

async def main():
    os.makedirs(ANDROID_RAW_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Starting generation of {len(STORY_AUDIO_ITEMS)} full-sentence story audio files...")
    for audio_id, text in STORY_AUDIO_ITEMS:
        await generate_sentence(audio_id, text)
    print("All story audio generation completed successfully!")

if __name__ == "__main__":
    asyncio.run(main())
