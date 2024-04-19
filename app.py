import datetime

from openai import OpenAI
from gtts import gTTS
from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip
import requests
import re
import os

# Initialize the OpenAI client
client = OpenAI(api_key="Your-Api-Key")

# Step 1: Generate script with embedded image prompts
def generate_script_with_image_prompts(topic):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system",
             "content": "You are proficient at crafting engaging YouTube content. You do not include anything but the direct script in your response"},
            {"role": "user",
             "content": f"Generate a 20-second YouTube script discussing {topic}. Include image markers: [image: description]. Limit to {num_images} images. Don't include who is saying the lines."}
        ],

        temperature=0.7,
        max_tokens=500,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    script_with_prompts = response.choices[0].message.content
    return script_with_prompts


# Step 2: Extract image prompts from the script
def extract_image_prompts(script):
    pattern = r"\[image: (.*?)\]"
    prompts = re.findall(pattern, script)
    return prompts

# Step 3: Generate images using the provided format for image generation
def generate_image(prompt):
    response = client.images.generate(
        model="dall-e-2",  # Use dall-e-3 for higher quality videos
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    # Accessing the image URL directly from the response object's attributes
    image_url = response.data[0].url

    # Downloading the image
    image_response = requests.get(image_url)
    filename = "image_" + str(datetime.datetime.now().second) + ".png"
    with open(filename, "wb") as f:
        f.write(image_response.content)
    return filename


# Example usage
topic = "Blackholes"
num_images = 3
script_with_prompts = generate_script_with_image_prompts(topic)
print(script_with_prompts)
print("----------------------------------")
image_prompts = extract_image_prompts(script_with_prompts)
print(image_prompts)
print("----------------------------------")

# Remove the image prompts from the script for TTS
cleaned_script = re.sub(r"\[image:.*?\]", "", script_with_prompts)
print(cleaned_script)
# Generate images
image_filenames = [generate_image(prompt) for prompt in image_prompts]

# Generate voiceover
tts = gTTS(cleaned_script, lang='en')
voiceover_filename = "voiceover.mp3"
tts.save(voiceover_filename)
voiceover = AudioFileClip(voiceover_filename)

# Create video clips for each image and set their duration to the voiceover length divided by the number of images
clips = [ImageClip(filename).set_duration(voiceover.duration / len(image_filenames)) for filename in image_filenames]
video = concatenate_videoclips(clips)

# Combine audio and video
final_clip = video.set_audio(voiceover)

# Output the final video file
final_clip.write_videofile("final_video.mp4", fps=24)

# Cleanup generated files
os.remove(voiceover_filename)
for filename in image_filenames:
    os.remove(filename)
