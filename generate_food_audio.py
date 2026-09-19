import asyncio
import os
import edge_tts

VOICE = "en-US-AnaNeural"
OUTPUT_DIR = "/home/nandan/Disk_D/Pimlo_app/src/assets/audio"
ANDROID_RAW_DIR = "/home/nandan/Disk_D/Pimlo_app/android/app/src/main/res/raw"

FOOD_ITEMS = [
    ("food_apple", "Apple"),
    ("food_banana", "Banana"),
    ("food_orange", "Orange"),
    ("food_strawberry", "Strawberry"),
    ("food_grapes", "Grapes"),
    ("food_watermelon", "Watermelon"),
    ("food_mango", "Mango"),
    ("food_carrot", "Carrot"),
    ("food_broccoli", "Broccoli"),
    ("food_tomato", "Tomato"),
    ("food_corn", "Corn"),
    ("food_cucumber", "Cucumber"),
    ("food_potato", "Potato"),
    ("food_pumpkin", "Pumpkin"),
]

PROMPTS = [
    ("prompt_find_apple", "Can you find the Apple?"),
    ("prompt_find_banana", "Can you find the Banana?"),
    ("prompt_find_orange", "Can you find the Orange?"),
    ("prompt_find_strawberry", "Can you find the Strawberry?"),
    ("prompt_find_grapes", "Can you find the Grapes?"),
    ("prompt_find_watermelon", "Can you find the Watermelon?"),
    ("prompt_find_mango", "Can you find the Mango?"),
    ("prompt_find_carrot", "Can you find the Carrot?"),
    ("prompt_find_broccoli", "Can you find the Broccoli?"),
    ("prompt_find_tomato", "Can you find the Tomato?"),
    ("prompt_find_corn", "Can you find the Corn?"),
    ("prompt_find_cucumber", "Can you find the Cucumber?"),
    ("prompt_find_potato", "Can you find the Potato?"),
    ("prompt_find_pumpkin", "Can you find the Pumpkin?"),
    ("prompt_find_fruit", "Which one is a Fruit?"),
    ("prompt_find_veggie", "Which one is a Vegetable?"),
    ("encourage_yummy_fruit", "Yummy! That is a delicious sweet fruit!"),
    ("encourage_healthy_veggie", "Super! That is a crunchy, healthy vegetable!"),
    ("prompt_sort_fruit", "Put it in the Fruit Basket!"),
    ("prompt_sort_veggie", "Put it in the Veggie Basket!"),
]

async def generate_file(filename_base: str, text: str):
    filename = f"{filename_base}.mp3"
    filepath = os.path.join(OUTPUT_DIR, filename)
    android_filepath = os.path.join(ANDROID_RAW_DIR, filename)

    communicate = edge_tts.Communicate(text, VOICE, rate="-8%", pitch="+2Hz")
    await communicate.save(filepath)

    with open(filepath, 'rb') as src_file, open(android_filepath, 'wb') as dst_file:
        dst_file.write(src_file.read())
    print(f"🎵 Generated: {filename} -> '{text}'")

async def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(ANDROID_RAW_DIR, exist_ok=True)
    all_items = FOOD_ITEMS + PROMPTS
    print(f"🚀 Generating {len(all_items)} Food audio files...")
    tasks = [generate_file(fid, text) for fid, text in all_items]
    await asyncio.gather(*tasks)
    print("✨ All Food audio files generated successfully!")

if __name__ == "__main__":
    asyncio.run(main())
