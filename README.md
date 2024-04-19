# AI Script Generator for YouTube Videos :movie_camera:

Welcome to the AI Script Generator repository! This innovative project leverages OpenAI's GPT models, Google's text-to-speech, and advanced image generation technologies to automate the creation of YouTube video scripts, complete with voiceovers and relevant images.

![AI Command Center](attachment://QV8WJkddCNuYVOk6)  
*Futuristic AI command center representing the high-tech environment of this project.*

## Features :sparkles:
- **Script Generation**: Automatically generate engaging scripts for YouTube videos on a variety of topics.
- **Image Insertion**: Embed dynamic images within scripts using sophisticated AI models.
- **Voiceover Creation**: Convert text scripts to audio using Google's text-to-speech service.
- **Video Assembly**: Compile images and voiceovers into a complete video.

## Installation :gear:

Before you start, make sure Python is installed on your system. You can then install the required libraries using pip:

```bash
pip install openai gtts moviepy requests
```

## Usage :computer:

Here’s a quick guide on how to use the script generator:

1. **Initialize the script**: Set up your OpenAI API key and other preferences.
2. **Generate a script**: Provide a topic to generate a script discussing your chosen subject.
3. **Extract image prompts**: Identify and prepare images based on the script's prompts.
4. **Create the video**: Compile the images and voiceover into a final video file.

### Example:

```python
topic = "Blackholes"
num_images = 3
script = generate_script_with_image_prompts(topic)
print(script)
```

## Contributing :handshake:

Interested in contributing? Great! Here are a few ways you can help:

- **Submit bugs**: Found something off? Submit an issue!
- **Propose improvements**: Have ideas on how to make this even better? We’d love to hear from you!
- **Pull requests**: Feel free to submit pull requests, but please ensure you've discussed the changes with us first.

---

We're excited to see what you create with our AI Script Generator! Dive in and start creating content that stands out!
