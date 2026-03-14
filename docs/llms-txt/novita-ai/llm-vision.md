# Source: https://novita.ai/docs/guides/llm-vision.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Vision Language Models

export const VisionModels = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    let attempts = 0;
    const maxAttempts = 50;
    const INIT_DISPLAY_COUNT = 3;
    const interval = setInterval(() => {
      const clientComponent = document.getElementById("vision-models");
      if (clientComponent && window.novitaRemoteData.llmModels.status === 'loaded') {
        const modelList = window.novitaRemoteData.llmModels.data.filter(model => {
          return (model.features || []).includes('vision');
        });
        let displayModels = modelList.slice(0, INIT_DISPLAY_COUNT).map(model => {
          return `<li><span class="model-id-item">${model.id}</span></li>`;
        }).join('');
        let showMoreButton = '';
        if (modelList.length > INIT_DISPLAY_COUNT) {
          showMoreButton = `<button id="show-more-vision-model-btn" style="margin-left: 32px; color: rgb(40 116 255)">View More</button>`;
        }
        clientComponent.innerHTML = `
          <ul>${displayModels}</ul>
          ${showMoreButton}
        `;
        document.getElementById('show-more-vision-model-btn')?.addEventListener('click', () => {
          clientComponent.innerHTML = `
            <ul>${modelList.map(model => {
            return `<li><span class="model-id-item">${model.id}</span></li>`;
          }).join('')}</ul>
          `;
        });
        clearInterval(interval);
      }
      attempts++;
      if (attempts >= maxAttempts) {
        clearInterval(interval);
      }
    }, 200);
    return <div id="vision-models"></div>;
  }
};

## Overview

Vision-Language Models (VLMs) are a type of multimodal foundation model capable of processing both image and text inputs. These models understand visual content in conjunction with language instructions, and generate high-quality responses based on the combined context. They are widely used in scenarios involving image recognition, content interpretation, and intelligent visual Q\&A.

### Typical Use Cases

* **Image Recognition and Description**: Automatically identifies objects, colors, scenes, and spatial relationships in images, and generates natural language descriptions.
* **Multimodal Understanding**: Combines image input and contextual text for multi-turn dialogue and task completion.
* **Visual Question Answering**: Acts as an advanced OCR tool by recognizing and interpreting text embedded in images.
* **Emerging Applications**: Ideal for use in intelligent vision assistants, robot perception, AR interfaces, and more.

***

## API Usage Guide

To invoke a Vision-Language Model, use the `/chat/completions` endpoint with both image and text inputs.

### Image Detail Parameter

Use the `detail` field to control image resolution. The following modes are available:

* `high`: High resolution, preserves more detail—ideal for precision tasks.
* `low`: Low resolution, faster response—suitable for real-time usage.
* `auto`: Automatically selects the appropriate mode.

***

### Example Message Format

#### Image via URL

```json  theme={"system"}
{
  "role": "user",
  "content": [
    {
      "type": "image_url",
      "image_url": {
        "url": "https://example.com/image.png",
        "detail": "high"
      }
    },
    {
      "type": "text",
      "text": "Please describe the scene in the image."
    }
  ]
}
```

#### Image via Base64

```json  theme={"system"}
{
  "role": "user",
  "content": [
    {
      "type": "image_url",
      "image_url": {
        "url": "data:image/jpeg;base64,{base64_image}",
        "detail": "low"
      }
    },
    {
      "type": "text",
      "text": "What text is present in the image?"
    }
  ]
}
```

***

### Python Code: Encode Image to Base64

```python  theme={"system"}
import base64
from PIL import Image
import io

def image_to_base64(image_path):
    with Image.open(image_path) as img:
        buffered = io.BytesIO()
        img.save(buffered, format="JPEG")
        return base64.b64encode(buffered.getvalue()).decode('utf-8')

base64_image = image_to_base64("path/to/your/image.jpg")
```

***

## Multi-Image Input

The API supports sending multiple images alongside text input. For best results, we recommend sending no more than two images per request.

```json  theme={"system"}
{
  "role": "user",
  "content": [
    {
      "type": "image_url",
      "image_url": {
        "url": "https://example.com/image1.png"
      }
    },
    {
      "type": "image_url",
      "image_url": {
        "url": "data:image/jpeg;base64,{base64_image}"
      }
    },
    {
      "type": "text",
      "text": "Compare the common features of these two images."
    }
  ]
}
```

***

## Supported Models

The following Vision-Language Models are currently supported on the Novita platform:

<VisionModels />

Visit the [Model Hub](https://novita.ai/models-console/library) for a complete and up-to-date list of available models.

***

## Billing

Image input is tokenized and counted toward billing together with text.

* Each model uses a different image-to-token conversion method.
* Refer to each model’s pricing page for detailed billing and token policy.

***

## API Call Examples

### Single Image Description

```python  theme={"system"}
from openai import OpenAI

client = OpenAI(api_key="YOUR_KEY", base_url="https://api.novita.ai/openai")

response = client.chat.completions.create(
    model="qwen/qwen2.5-vl-72b-instruct",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://example.com/cityscape.jpg"
                    }
                },
                {
                    "type": "text",
                    "text": "Describe the main buildings in the image."
                }
            ]
        }
    ],
    stream=True
)

for chunk in response:
    print(chunk.choices[0].delta.content or "", end="", flush=True)
```

### Multi-Image Comparison

```python  theme={"system"}
response = client.chat.completions.create(
    model="qwen/qwen2.5-vl-72b-instruct",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://example.com/product1.jpg"
                    }
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://example.com/product2.jpg"
                    }
                },
                {
                    "type": "text",
                    "text": "Please compare the key differences between these two products."
                }
            ]
        }
    ],
    stream=True
)

for chunk in response:
    print(chunk.choices[0].delta.content or "", end="", flush=True)
```

***

## Notes & Troubleshooting

* Image resolution and clarity significantly affect model performance. Use high-quality sources where possible.
* Base64-encoded images should ideally be under 1MB to avoid timeouts or errors.
* For detailed usage, [book a call with our sales team](https://meet.brevo.com/novita-ai/contact-sales) or contact support if needed.


Built with [Mintlify](https://mintlify.com).