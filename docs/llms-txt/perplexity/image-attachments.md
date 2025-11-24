# Source: https://docs.perplexity.ai/guides/image-attachments.md

# Image Attachments with Sonar

> Learn how to upload and analyze images using Sonar models

## Overview

Sonar models support image analysis through direct image uploads. You can include images in your API requests to support multi-modal conversations alongside text. Images can be provided either as base64 encoded strings within a data URI or as standard HTTPS URLs.

<Note>
  **SDK Installation Required**: Install the official SDK first - `pip install perplexityai` for Python or `npm install @perplexity-ai/perplexity_ai` for TypeScript/JavaScript.
</Note>

<Warning>
  * When using base64 encoding, the API currently only supports images up to 50 MB per image.
  * Supported formats for base64 encoded images: PNG (image/png), JPEG (image/jpeg), WEBP (image/webp), and GIF (image/gif).
  * When using an HTTPS URL, the model will attempt to fetch the image from the provided URL. Ensure the URL is publicly accessible.
</Warning>

## Supported Features

Image uploads can be useful for:

* **Visual Question Answering**: Ask questions about visual content (e.g., text in a screenshot, diagram interpretation)
* **Context Analysis**: Providing context for follow-up queries
* **Multi-modal Conversations**: Analyzing visual media as part of a multi-turn conversation
* **Content Description**: Get detailed descriptions of images
* **Text Extraction**: Extract text from images and documents

## Upload Methods

You can include images in your requests using two methods:

### 1. Base64 Data URI

Encode the image as a base64 string and embed it in a data URI:

```
data:image/png;base64,<BASE64_ENCODED_IMAGE>
```

Replace `image/png` with the correct MIME type if you're using JPEG or GIF (`image/jpeg` or `image/gif`).

### 2. HTTPS URL

Provide a standard HTTPS URL pointing directly to the image file:

```
https://example.com/path/to/your/image.png
```

## Request Format

Images must be embedded in the `messages` array, alongside any text input. Each image should be provided using the following structure:

**Using Base64 Data URI:**

```json  theme={null}
{
  "type": "image_url",
  "image_url": {
    "url": "data:image/png;base64,<BASE64_ENCODED_IMAGE>"
  }
}
```

**Using HTTPS URL:**

```json  theme={null}
{
  "type": "image_url",
  "image_url": {
    "url": "https://example.com/path/to/your/image.png"
  }
}
```

## Basic Usage

<Tabs>
  <Tab title="Base64 Encoding">
    <Info>Use this method when you have the image file locally and want to embed it directly into the request payload. Remember the 50MB size limit and supported formats (PNG, JPEG, WEBP, GIF).</Info>

    <CodeGroup>
      ```bash cURL theme={null}
      curl --location 'https://api.perplexity.ai/chat/completions' \
        --header 'accept: application/json' \
        --header 'content-type: application/json' \
        --header "Authorization: Bearer $SONAR_API_KEY" \
        --data '{
          "model": "sonar-pro",
          "stream": false,
          "messages": [
            {
              "role": "user",
              "content": [
                {
                  "type": "text",
                  "text": "Can you describe this image?"
                },
                {
                  "type": "image_url",
                  "image_url": {
                    "url": "data:image/png;base64,$BASE64_ENCODED_IMAGE"
                  }
                }
              ]
            }
          ]
        }' | jq
      ```

      ```python Python theme={null}
      from perplexity import Perplexity
      import base64

      # Initialize the client
      client = Perplexity()

      # Read and encode image as base64
      try:
          with open("path/to/your/image.png", "rb") as image_file:
              base64_image = base64.b64encode(image_file.read()).decode("utf-8")
          image_data_uri = f"data:image/png;base64,{base64_image}"  # Ensure correct MIME type
      except FileNotFoundError:
          print("Error: Image file not found.")
          exit()

      # Analyze the image
      try:
          completion = client.chat.completions.create(
              model="sonar-pro",
              messages=[
                  {
                      "role": "user",
                      "content": [
                          {"type": "text", "text": "Can you describe this image?"},
                          {"type": "image_url", "image_url": {"url": image_data_uri}}
                      ]
                  }
              ]
          )
          print(completion.choices[0].message.content)
      except Exception as e:
          print(f"API Request failed: {e}")
      ```

      ```javascript JavaScript theme={null}
      const Perplexity = require('@perplexity-ai/perplexity_ai');
      const fs = require('fs');

      // Initialize the client
      const client = new Perplexity();

      // Read and encode image as base64
      try {
          const imageBuffer = fs.readFileSync('path/to/your/image.png');
          const base64Image = imageBuffer.toString('base64');
          const imageDataUri = `data:image/png;base64,${base64Image}`;
          
          // Analyze the image
          const completion = await client.chat.completions.create({
              model: 'sonar-pro',
              messages: [
                  {
                      role: 'user',
                      content: [
                          { type: 'text', text: 'Can you describe this image?' },
                          { type: 'image_url', image_url: { url: imageDataUri } }
                      ]
                  }
              ]
          });
          
          console.log(completion.choices[0].message.content);
      } catch (error) {
          console.error('Error:', error.message);
      }
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';
      import * as fs from 'fs';

      // Initialize the client
      const client = new Perplexity();

      // Read and encode image as base64
      try {
          const imageBuffer = fs.readFileSync('path/to/your/image.png');
          const base64Image = imageBuffer.toString('base64');
          const imageDataUri = `data:image/png;base64,${base64Image}`;
          
          // Analyze the image
          const completion = await client.chat.completions.create({
              model: 'sonar-pro',
              messages: [
                  {
                      role: 'user',
                      content: [
                          { type: 'text', text: 'Can you describe this image?' },
                          { type: 'image_url', image_url: { url: imageDataUri } }
                      ]
                  }
              ]
          });
          
          console.log(completion.choices[0].message.content);
      } catch (error) {
          console.error('Error:', error.message);
      }
      ```
    </CodeGroup>
  </Tab>

  <Tab title="HTTPS URL">
    <Info>Use this method to reference an image hosted online. Ensure the URL is publicly accessible and points directly to the image file.</Info>

    <CodeGroup>
      ```bash cURL theme={null}
      curl --location 'https://api.perplexity.ai/chat/completions' \
        --header "accept: application/json" \
        --header "content-type: application/json" \
        --header "Authorization: Bearer $SONAR_API_KEY" \
        --data '{
          "model": "sonar-pro",
          "stream": false,
          "messages": [
            {
              "role": "user",
              "content": [
                {
                  "type": "text",
                  "text": "Can you describe the image at this URL?"
                },
                {
                  "type": "image_url",
                  "image_url": {
                    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
                  }
                }
              ]
            }
          ]
        }' | jq
      ```

      ```python Python theme={null}
      from perplexity import Perplexity

      # Initialize the client
      client = Perplexity()

      # Example HTTPS URL
      image_https_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"

      # Analyze the image
      try:
          completion = client.chat.completions.create(
              model="sonar-pro",
              messages=[
                  {
                      "role": "user",
                      "content": [
                          {"type": "text", "text": "Can you describe the image at this URL?"},
                          {"type": "image_url", "image_url": {"url": image_https_url}}
                      ]
                  }
              ]
          )
          print(completion.choices[0].message.content)
      except Exception as e:
          print(f"API Request failed: {e}")
      ```

      ```javascript JavaScript theme={null}
      const Perplexity = require('@perplexity-ai/perplexity_ai');

      // Initialize the client
      const client = new Perplexity();

      // Example HTTPS URL
      const imageHttpsUrl = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg";

      // Analyze the image
      try {
          const completion = await client.chat.completions.create({
              model: 'sonar-pro',
              messages: [
                  {
                      role: 'user',
                      content: [
                          { type: 'text', text: 'Can you describe the image at this URL?' },
                          { type: 'image_url', image_url: { url: imageHttpsUrl } }
                      ]
                  }
              ]
          });
          
          console.log(completion.choices[0].message.content);
      } catch (error) {
          console.error('API Request failed:', error.message);
      }
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      // Initialize the client
      const client = new Perplexity();

      // Example HTTPS URL
      const imageHttpsUrl = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg";

      // Analyze the image
      const analyzeImage = async (): Promise<void> => {
          try {
              const completion = await client.chat.completions.create({
                  model: 'sonar-pro',
                  messages: [
                      {
                          role: 'user',
                          content: [
                              { type: 'text', text: 'Can you describe the image at this URL?' },
                              { type: 'image_url', image_url: { url: imageHttpsUrl } }
                          ]
                      }
                  ]
              });
              
              console.log(completion.choices[0].message.content);
          } catch (error) {
              console.error('API Request failed:', error.message);
          }
      };

      analyzeImage();
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Common Use Cases

### Screenshot Analysis

```python  theme={null}
question = "What text is visible in this screenshot?"
```

### Diagram Interpretation

```python  theme={null}
question = "Explain the workflow shown in this diagram"
```

### Product Analysis

```python  theme={null}
question = "Describe the features and specifications of this product"
```

### Document Processing

```python  theme={null}
question = "Extract all the key information from this document image"
```

## Best Practices

<AccordionGroup>
  <Accordion title="Image Quality Guidelines">
    * Use high-resolution images for better text extraction
    * Ensure good contrast for text recognition
    * Avoid heavily compressed images when detail is important
    * Use appropriate image formats (PNG for screenshots, JPEG for photos)
  </Accordion>

  <Accordion title="File Size Optimization">
    * Keep images under 50MB for base64 encoding
    * Compress images when possible without losing critical detail
    * Consider using HTTPS URLs for very large images
    * Use WebP format for balanced quality and size
  </Accordion>

  <Accordion title="URL Best Practices">
    * Ensure URLs are publicly accessible (no authentication required)
    * Use direct links to image files, not web pages
    * Test URLs in a browser before using in API calls
    * Consider using CDNs for reliable image hosting
  </Accordion>
</AccordionGroup>

## Pricing

Images are tokenized based on their pixel dimensions using the following formula:

```
tokens = (width px × height px) / 750
```

**Examples:**

* A 1024×768 image would consume: (1024 × 768) / 750 = 1,048 tokens
* A 512×512 image would consume: (512 × 512) / 750 = 349 tokens

These image tokens are then priced according to the input token pricing of the model you're using (e.g., `sonar-pro`, `sonar`, etc.). The image tokens are added to your total token count for the request alongside any text tokens.

<Tip>
  To optimize costs, resize images to the minimum resolution needed for your use case while maintaining adequate quality.
</Tip>

## Limitations

<Warning>
  * Image and regex cannot be used together in the same request
  * `sonar-deep-research` does not support image input
  * Ensure provided HTTPS URLs are publicly accessible
  * Base64 images have a 50MB size limit
  * Supported formats: PNG, JPEG, WEBP, and GIF
</Warning>
