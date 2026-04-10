# Source: https://dev.writer.com/home/chat-with-images.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add images to chat completions

You can include images directly in your chat conversations with Palmyra X5 using mixed content support. This allows you to send both text and images in the same message, enabling rich visual conversations with Palmyra X5.

<Warning>
  Image analysis in chat completions is only supported with the **Palmyra X5** model. Other models don't support the `image_url` content type.
</Warning>

<Note>
  You need an API key to access the Writer API. Get an API key by following the steps in the [API quickstart](/home/quickstart).

  We recommend setting the API key as an environment variable in a `.env` file with the name `WRITER_API_KEY`.
</Note>

## Overview

Mixed content support allows you to send messages that contain both text and images in a chat with Palmyra X5. Instead of using the separate [Vision tool](/home/vision-tool), you can now include images directly in your chat messages, making conversations more natural and contextual.

## How it works

When sending a message to the chat completion endpoint, you can use the `content` field in two ways:

1. **Text-only message**:

```json  theme={null}
    "messages": [
        {
            "role": "user",
            "content": "Hello, how are you?"
        }
    ]
```

2. **Mixed content message**:

```json  theme={null}
    "messages": [
        {
            "role": "user",
            "content": [{"type": "text", "text": "What do you see in this image?"}, {"type": "image_url", "image_url": {"url": "<IMAGE_URL>"}}]
        }
    ]
```

## Endpoint

**URL:** `POST https://api.writer.com/v1/chat`

### Content fragment types

#### Text fragment

```json  theme={null}
{
  "type": "text",
  "text": "Your text content here"
}
```

#### Image fragment

```json  theme={null}
{
  "type": "image_url",
  "image_url": {
    "url": "<IMAGE_URL>"
  }
}
```

## Examples

### Single image analysis

This example shows how to send a message with a single image. The `content` field is an array of content fragments, where each fragment can be either text or image.

The text fragment includes the message for the model to analyze. The image fragment includes the image URL.

<CodeGroup>
  ```bash cURL theme={null}
  curl --location 'https://api.writer.com/v1/chat' \
  --header 'Content-Type: application/json' \
  --header "Authorization: Bearer $WRITER_API_KEY" \
  --data '{
    "model": "palmyra-x5",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "What do you see in this image?"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "<IMAGE_URL>"
            }
          }
        ]
      }
    ]
  }'
  ```

  ```python Python theme={null}
  from writerai import Writer

  # Initialize the client. If you don't pass the `apiKey` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  response = client.chat.chat(
    model="palmyra-x5",
    messages=[
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "What do you see in this image?"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "<IMAGE_URL>"
            }
          }
        ]
      }
    ]
  )

  print(response.choices[0].message.content)
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from "writer-sdk";

  // Initialize the client. If you don't pass the `apiKey` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  const response = await client.chat.chat({
    model: "palmyra-x5",
    messages: [
      {
        role: "user",
        content: [
          {
            type: "text",
            text: "What do you see in this image?"
          },
          {
            type: "image_url",
            image_url: {
              url: "<IMAGE_URL>"
            }
          }
        ]
      }
    ]
  });

  console.log(response.choices[0].message.content);
  ```
</CodeGroup>

### Using local images with data URLs

You can also use [data URLs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs) to send local images without uploading them to a remote server. This is useful for testing or when working with local files:

<CodeGroup>
  ```bash cURL theme={null}
  # Convert local image to base64 data URL
  base64_image=$(base64 -i "<IMAGE_PATH>")
  data_url="data:image/jpeg;base64,$base64_image"

  curl --location 'https://api.writer.com/v1/chat' \
  --header 'Content-Type: application/json' \
  --header "Authorization: Bearer $WRITER_API_KEY" \
  --data "{
    \"model\": \"palmyra-x5\",
    \"messages\": [
      {
        \"role\": \"user\",
        \"content\": [
          {
            \"type\": \"text\",
            \"text\": \"Analyze this local image:\"
          },
          {
            \"type\": \"image_url\",
            \"image_url\": {
              \"url\": \"$data_url\"
            }
          }
        ]
      }
    ]
  }"
  ```

  ```python Python theme={null}
  import base64
  from pathlib import Path
  from writerai import Writer

  # Initialize the client. If you don't pass the `apiKey` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  # Read local image and convert to base64 data URL
  def image_to_data_url(image_path):
      with open(image_path, "rb") as image_file:
          encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
          file_extension = Path(image_path).suffix.lstrip('.')
          mime_type = f"image/{file_extension}" if file_extension in ['jpg', 'jpeg', 'png', 'gif'] else "image/jpeg"
          return f"data:{mime_type};base64,{encoded_string}"

  # Convert local image to data URL
  data_url = image_to_data_url("<IMAGE_PATH>")

  response = client.chat.chat(
    model="palmyra-x5",
    messages=[
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Analyze this local image:"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": data_url
            }
          }
        ]
      }
    ]
  )

  print(response.choices[0].message.content)
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from "writer-sdk";
  import fs from 'fs';

  // Initialize the client. If you don't pass the `apiKey` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  // Convert local image to base64 data URL
  function imageToDataUrl(imagePath) {
    const imageBuffer = fs.readFileSync(imagePath);
    const base64String = imageBuffer.toString('base64');
    const fileExtension = imagePath.split('.').pop();
    const mimeType = ['jpg', 'jpeg', 'png', 'gif'].includes(fileExtension) 
      ? `image/${fileExtension}` 
      : 'image/jpeg';
    return `data:${mimeType};base64,${base64String}`;
  }

  // Convert local image to data URL
  const dataUrl = imageToDataUrl("<IMAGE_PATH>");

  const response = await client.chat.chat({
    model: "palmyra-x5",
    messages: [
      {
        role: "user",
        content: [
          {
            type: "text",
            text: "Analyze this local image:"
          },
          {
            type: "image_url",
            image_url: {
              url: dataUrl
            }
          }
        ]
      }
    ]
  });

  console.log(response.choices[0].message.content);
  ```
</CodeGroup>

### Multiple images with text

You can include multiple images in a single message:

<CodeGroup>
  ```bash cURL theme={null}
  curl --location 'https://api.writer.com/v1/chat' \
  --header 'Content-Type: application/json' \
  --header "Authorization: Bearer $WRITER_API_KEY" \
  --data '{
    "model": "palmyra-x5",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Compare these two images and tell me the differences:"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "<IMAGE_URL_1>"
            }
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "<IMAGE_URL_2>"
            }
          }
        ]
      }
    ]
  }'
  ```

  ```python Python theme={null}
  from writerai import Writer

  # Initialize the client. If you don't pass the `apiKey` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  response = client.chat.chat(
    model="palmyra-x5",
    messages=[
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Compare these two images and tell me the differences:"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "<IMAGE_URL_1>"
            }
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "<IMAGE_URL_2>"
            }
          }
        ]
      }
    ]
  )

  print(response.choices[0].message.content)
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from "writer-sdk";

  // Initialize the client. If you don't pass the `apiKey` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  const response = await client.chat.chat({
    model: "palmyra-x5",
    messages: [
      {
        role: "user",
        content: [
          {
            type: "text",
            text: "Compare these two images and tell me the differences:"
          },
          {
            type: "image_url",
            image_url: {
              url: "<IMAGE_URL_1>"
            }
          },
          {
            type: "image_url",
            image_url: {
              url: "<IMAGE_URL_2>"
            }
          }
        ]
      }
    ]
  });

  console.log(response.choices[0].message.content);
  ```
</CodeGroup>

## Next steps

* Learn about [chat completions](/home/chat-completion) for text-based conversations
* Explore the [Vision tool](/home/vision-tool) for dedicated image analysis
* Check out [Palmyra X5](/home/models#palmyra-x5) model capabilities
