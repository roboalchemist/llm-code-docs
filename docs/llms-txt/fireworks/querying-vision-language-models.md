# Source: https://docs.fireworks.ai/guides/querying-vision-language-models.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Vision Models

> Query vision-language models to analyze images and visual content

Vision-language models (VLMs) process both text and images in a single request, enabling image captioning, visual question answering, document analysis, chart interpretation, OCR, and content moderation. Use VLMs via serverless inference or [dedicated deployments](/getting-started/ondemand-quickstart).

[Browse available vision models →](https://app.fireworks.ai/models?filter=Vision)

## Chat Completions API

Provide images via URL or base64 encoding. The request structure is identical to OpenAI's vision API.

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    from fireworks import Fireworks

    client = Fireworks()

    response = client.chat.completions.create(
        model="accounts/fireworks/models/qwen2p5-vl-32b-instruct",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Can you describe this image?"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "https://images.unsplash.com/photo-1582538885592-e70a5d7ab3d3?w=800"
                        }
                    }
                ]
            }
        ]
    )

    print(response.choices[0].message.content)
    ```

    <Tip>
      You can also use the [OpenAI SDK](/tools-sdks/openai-compatibility) with Fireworks by changing the base URL and API key.
    </Tip>
  </Tab>

  <Tab title="JavaScript">
    ```javascript  theme={null}
    import OpenAI from "openai";

    const client = new OpenAI({
      apiKey: process.env.FIREWORKS_API_KEY,
      baseURL: "https://api.fireworks.ai/inference/v1",
    });

    const response = await client.chat.completions.create({
      model: "accounts/fireworks/models/qwen2p5-vl-32b-instruct",
      messages: [
        {
          role: "user",
          content: [
            { type: "text", text: "Can you describe this image?" },
            {
              type: "image_url",
              image_url: {
                url: "https://images.unsplash.com/photo-1582538885592-e70a5d7ab3d3?w=800"
              }
            }
          ]
        }
      ]
    });

    console.log(response.choices[0].message.content);
    ```
  </Tab>

  <Tab title="curl">
    ```bash  theme={null}
    curl https://api.fireworks.ai/inference/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $FIREWORKS_API_KEY" \
      -d '{
        "model": "accounts/fireworks/models/qwen2p5-vl-32b-instruct",
        "messages": [
          {
            "role": "user",
            "content": [
              {"type": "text", "text": "Can you describe this image?"},
              {
                "type": "image_url",
                "image_url": {
                  "url": "https://images.unsplash.com/photo-1582538885592-e70a5d7ab3d3?w=800"
                }
              }
            ]
          }
        ]
      }'
    ```
  </Tab>
</Tabs>

### Using base64-encoded images

For local files, encode them as base64 with the appropriate MIME type prefix:

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    import base64
    from fireworks import Fireworks

    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")

    image_base64 = encode_image("your_image.jpg")

    client = Fireworks()

    response = client.chat.completions.create(
        model="accounts/fireworks/models/qwen2p5-vl-32b-instruct",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Can you describe this image?"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_base64}"
                        }
                    }
                ]
            }
        ]
    )

    print(response.choices[0].message.content)
    ```
  </Tab>

  <Tab title="JavaScript">
    ```javascript  theme={null}
    import OpenAI from "openai";
    import fs from "fs";

    const client = new OpenAI({
      apiKey: process.env.FIREWORKS_API_KEY,
      baseURL: "https://api.fireworks.ai/inference/v1",
    });

    const imageBase64 = fs.readFileSync("your_image.jpg").toString("base64");

    const response = await client.chat.completions.create({
      model: "accounts/fireworks/models/qwen2p5-vl-32b-instruct",
      messages: [
        {
          role: "user",
          content: [
            { type: "text", text: "Can you describe this image?" },
            {
              type: "image_url",
              image_url: {
                url: `data:image/jpeg;base64,${imageBase64}`
              }
            }
          ]
        }
      ]
    });

    console.log(response.choices[0].message.content);
    ```
  </Tab>
</Tabs>

## Working with images

Vision-language models support [prompt caching](/guides/prompt-caching) to improve performance for requests with repeated content. Both text and image portions can benefit from caching to reduce time to first token by up to 80%.

**Tips for optimal performance:**

* **Use URLs for long conversations** – Reduces latency compared to base64 encoding
* **Downsize images** – Smaller images use fewer tokens and process faster
* **Structure prompts for caching** – Place static instructions at the beginning, variable content at the end
* **Include metadata in prompts** – Add context about the image directly in your text prompt

## Advanced capabilities

<CardGroup cols={2}>
  <Card title="Vision fine-tuning" href="/fine-tuning/fine-tuning-vlm" icon="sliders">
    Fine-tune VLMs for specialized visual tasks
  </Card>

  <Card title="LoRA adapters" href="/models/uploading-custom-models" icon="layer-group">
    Deploy custom LoRA adapters for vision models
  </Card>

  <Card title="Dedicated deployments" href="/getting-started/ondemand-quickstart" icon="server">
    Deploy VLMs on dedicated GPUs for better performance
  </Card>

  <Card title="Video & audio inputs" href="/guides/video-audio-inputs" icon="video">
    Process video and audio content with multimodal models
  </Card>
</CardGroup>

## Alternative query methods

For the Completions API, manually insert the image token `<image>` in your prompt and supply images as an ordered list:

```python  theme={null}
response = client.completions.create(
    model="accounts/fireworks/models/qwen2p5-vl-32b-instruct",
    prompt="SYSTEM: Hello\n\nUSER:<image>\ntell me about the image\n\nASSISTANT:",
    extra_body={
        "images": ["https://images.unsplash.com/photo-1582538885592-e70a5d7ab3d3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80"]
    }
)

print(response.choices[0].text)
```

## Known limitations

1. **Maximum images per request**: 30 images maximum, regardless of format (base64 or URL)
2. **Base64 size limit**: Total base64-encoded images must be less than 10MB
3. **URL size and timeout**: Each image URL must be smaller than 5MB and download within 1.5 seconds
4. **Supported formats**: `.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`, `.tiff`, `.ppm`
5. **Llama 3.2 Vision models**: Pass images before text in the content field to avoid refusals (temporary limitation)
