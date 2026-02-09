# Source: https://docs.agent.ai/actions/generate_image.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Generate Image

## Overview

Create visually engaging images using AI models, with options for style, aspect ratio, and detailed prompts.

### Use Cases

* **Creative Design**: Generate digital art, illustrations, or concept visuals.
* **Marketing Campaigns**: Produce images for advertisements or social media posts.
* **Visualization**: Create representations of ideas or concepts.

## Configuration Fields

### Model

* **Description**: Select the AI model to generate images.
* **Options**: DALL-E 3, Playground v3, FLUX 1.1 Pro, Ideogram.
* **Example**: "DALL-E 3" for high-quality digital art.
* **Required**: Yes

### Style

* **Description**: Choose the style for the generated image.
* **Options**: Default, Photo, Digital Art, Illustration, Drawing.
* **Example**: "Digital Art" for a creative design.
* **Required**: Yes

### Aspect Ratio

* **Description**: Set the aspect ratio for the image.
* **Options**: 9:16, 1:1, 4:3, 16:9.
* **Example**: "16:9" for widescreen formats.
* **Required**: Yes

### Prompt

* **Description**: Enter a prompt to describe the image.
* **Example**: "A futuristic cityscape" or "A serene mountain lake at sunset."
* **Required**: Yes

### Output Variable Name

* **Description**: Provide a variable name to store the generated image.
* **Example**: "generated\_image" or "ai\_image."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes

***
