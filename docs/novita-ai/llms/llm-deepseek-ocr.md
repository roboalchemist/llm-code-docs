# Source: https://novita.ai/docs/guides/llm-deepseek-ocr.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# DeepSeek-OCR Usage

## Overview

DeepSeek-OCR is designed for document recognition and image-to-text scenarios, pushing the limits of visual and textual compression. The model can render long texts into highly compressed images, achieving an OCR accuracy of 97% at a lossless compression ratio of 10x and around 60% accuracy at 20x compression.

<Note>
  This model currently supports only single-turn, independent recognition tasks. It does not support multi-turn conversations. Only one image can be uploaded per request, and it is strongly recommended to use preset prompts for optimal performance.
</Note>

## Recommended Preset Prompts

```bash  theme={"system"}
# Convert the document contents to markdown format
<|grounding|>Convert the document to markdown.

# Perform text recognition on this image
<|grounding|>OCR this image.

# Extract all text without layout consideration
Free OCR.

# Parse any figures or tables in the document
Parse the figure.

# Provide a detailed description of the image content
Describe this image in detail.

# Locate the position of <|ref|>xxxx<|/ref|> in the image
Locate <|ref|>xxxx<|/ref|> in the image.
```

## Usage Example

This example uses the `<|grounding|>OCR this image.` preset prompt to perform image text recognition.

```python  theme={"system"}
from openai import OpenAI

client = OpenAI(
    base_url="https://api.novita.ai/openai",
    api_key="<Your API Key>",
)

response = client.chat.completions.create(
    model="deepseek/deepseek-ocr",
    messages=[
      {
        "role": "user",
        "content": [
          {
            "type": "image_url",
            "image_url": {
              "url": "https://example.com/image.png"
            }
          },
          {
            "type": "text",
            "text": "<|grounding|>OCR this image."
          }
        ]
      }
    ],
    stream=False,
    max_tokens=4096
)

content = response.choices[0].message.content

print(content)
```

Example input image:

<Frame>
    <img src="https://mintcdn.com/novitaai/WiqzsYZd3W7VMsVe/guides/images/ocr_input.jpg?fit=max&auto=format&n=WiqzsYZd3W7VMsVe&q=85&s=c9163932898598c1c9f346549fdd6076" alt="OCR Example Image" width="762" height="406" data-path="guides/images/ocr_input.jpg" />
</Frame>

Example output:

```
<|/ref|><|det|>[[37, 48, 279, 140]]<|/det|>
<|ref|>Deploy open-source and specialized models<|/ref|><|det|>[[42, 48, 857, 133]]<|/det|>
<|ref|>smarterandfasterwithsimpleApls.Accessthe<|/ref|><|det|>[[44, 185, 902, 246]]<|/det|>
<|ref|>latest chat, code, image, audio, video models and<|/ref|><|det|>[[41, 291, 945, 370]]<|/det|>
<|ref|>more,ready for production with built-in<|/ref|><|det|>[[40, 407, 756, 488]]<|/det|>
<|ref|>scalability.<|/ref|><|det|>[[39, 515, 232, 606]]<|/det|>
<|ref|>Explore<|/ref|><|det|>[[87, 813, 266, 879]]<|/det|>
<|ref|>Models<|/ref|><|det|>[[289, 816, 432, 878]]<|/det|>
```


Built with [Mintlify](https://mintlify.com).