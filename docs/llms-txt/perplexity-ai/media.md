# Source: https://docs.perplexity.ai/docs/sonar/media.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Media & Attachments

> Send and receive images, videos, and files with the Sonar API

## Overview

The Sonar API supports comprehensive media handling: send images and files for analysis, and receive images and videos in responses. This guide covers all media functionality in one place.

## Sending Images

Send images to the API for analysis using either base64 encoding or HTTPS URLs. Images are embedded in the `messages` array alongside text content.

<Warning>
  * Base64 images: Maximum 50 MB per image. Supported formats: PNG, JPEG, WEBP, GIF
  * HTTPS URLs: Must be publicly accessible and point directly to the image file
</Warning>

### Base64 Encoded Images

Use base64 encoding when you have the image file locally:

```python Python SDK theme={null}
from perplexity import Perplexity
import base64

client = Perplexity()

# Read and encode image as base64
with open("path/to/your/image.png", "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode("utf-8")
    image_data_uri = f"data:image/png;base64,{base64_image}"

# Analyze the image
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
```

### HTTPS URL Images

Reference images hosted online:

```python Python SDK theme={null}
from perplexity import Perplexity

client = Perplexity()

image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"

completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Can you describe the image at this URL?"},
                {"type": "image_url", "image_url": {"url": image_url}}
            ]
        }
    ]
)
print(completion.choices[0].message.content)
```

### Key Parameters

* **Image format**: Use `data:image/{format};base64,{content}` for base64 (e.g., `data:image/png;base64,...`)
* **Token pricing**: Images are tokenized as `(width × height) / 750` tokens, priced at input token rates
* **Supported formats**: PNG (`image/png`), JPEG (`image/jpeg`), WEBP (`image/webp`), GIF (`image/gif`)

## Sending Files

Upload documents (PDF, DOC, DOCX, TXT, RTF) for analysis using URLs or base64 encoding. Files can be provided as publicly accessible URLs or base64 encoded bytes without any prefix.

<Warning>
  Maximum file size is 50MB per file. Files larger than this limit will not be processed.
</Warning>

### Using a Public URL

```python Python SDK theme={null}
from perplexity import Perplexity

client = Perplexity()

completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Summarize this document"},
                {
                    "type": "file_url",
                    "file_url": {"url": "https://example.com/document.pdf"}
                }
            ]
        }
    ]
)
print(completion.choices[0].message.content)
```

### Using Base64 Encoding

```python Python SDK theme={null}
from perplexity import Perplexity
import base64

client = Perplexity()

# Read and encode file (no prefix needed)
with open("document.pdf", "rb") as file:
    encoded_file = base64.b64encode(file.read()).decode('utf-8')

completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Summarize this document"},
                {
                    "type": "file_url",
                    "file_url": {"url": encoded_file}  # Just base64 string, no prefix
                }
            ]
        }
    ]
)
print(completion.choices[0].message.content)
```

### Key Parameters

* **Supported formats**: PDF, DOC, DOCX, TXT, RTF
* **Base64 encoding**: Provide only the base64 string without `data:` prefix
* **File size limit**: 50MB per file, maximum 30 files per request
* **URL requirements**: Must be publicly accessible and return the file directly

## Receiving Images

Control which images are returned in API responses using `return_images`, `image_domain_filter`, and `image_format_filter` parameters.

<Info>
  The `return_images` feature is currently only available in the Sonar API.
</Info>

### Basic Image Returns

Enable image returns by setting `return_images: true`:

```python Python SDK theme={null}
from perplexity import Perplexity

client = Perplexity()

completion = client.chat.completions.create(
    model="sonar",
    return_images=True,
    messages=[
        {"role": "user", "content": "Show me images of Mount Everest"}
    ]
)
print(completion.choices[0].message.content)
```

### Filtering Image Domains

Control which image sources are included or excluded:

```python Python SDK theme={null}
from perplexity import Perplexity

client = Perplexity()

# Exclude specific domains (prefix with -)
completion = client.chat.completions.create(
    model="sonar",
    return_images=True,
    image_domain_filter=["-gettyimages.com", "-shutterstock.com"],
    messages=[
        {"role": "user", "content": "Show me nature photography"}
    ]
)

# Include only specific domains
completion = client.chat.completions.create(
    model="sonar",
    return_images=True,
    image_domain_filter=["wikimedia.org", "nasa.gov"],
    messages=[
        {"role": "user", "content": "Show me historical images"}
    ]
)
```

### Filtering Image Formats

Restrict results to specific file formats:

```python Python SDK theme={null}
from perplexity import Perplexity

client = Perplexity()

# Only return GIF images
completion = client.chat.completions.create(
    model="sonar",
    return_images=True,
    image_format_filter=["gif"],
    messages=[
        {"role": "user", "content": "Show me a funny cat gif"}
    ]
)

# Allow multiple formats
completion = client.chat.completions.create(
    model="sonar",
    return_images=True,
    image_format_filter=["jpg", "png", "webp"],
    messages=[
        {"role": "user", "content": "Show me high-quality landscape images"}
    ]
)
```

### Key Parameters

* **`return_images`**: Set to `true` to enable image returns
* **`image_domain_filter`**: Array of domains (max 10 entries). Prefix with `-` to exclude (e.g., `-gettyimages.com`)
* **`image_format_filter`**: Array of lowercase file extensions (max 10 entries). Use `gif`, `jpg`, `png`, `webp` (no dot prefix)
* **Limitations**: Maximum 30 images per response, filters only apply when `return_images: true`

## Receiving Videos

Enable video returns in responses using the `media_response.overrides.return_videos` parameter.

<Info>
  The `return_videos` feature is currently only available in the Sonar API.
</Info>

<Warning>
  Video returns may increase response size and processing time. Use this feature selectively for queries where video content adds significant value.
</Warning>

### Basic Video Returns

```python Python SDK theme={null}
from perplexity import Perplexity

client = Perplexity()

completion = client.chat.completions.create(
    model="sonar-pro",
    media_response={
        "overrides": {
            "return_videos": True
        }
    },
    messages=[
        {"role": "user", "content": "2024 Olympics highlights"}
    ]
)
print(completion.choices[0].message.content)
```

### Combining Videos with Images

You can request both videos and images in the same response:

```python Python SDK theme={null}
from perplexity import Perplexity

client = Perplexity()

completion = client.chat.completions.create(
    model="sonar-pro",
    return_images=True,
    media_response={
        "overrides": {
            "return_videos": True
        }
    },
    messages=[
        {"role": "user", "content": "Mars rover discoveries 2024"}
    ]
)
```

### Key Parameters

* **`media_response.overrides.return_videos`**: Set to `true` to enable video returns
* **Response format**: Videos appear in the `videos` array with `url`, `thumbnail_url`, and metadata
* **Performance**: Video-enabled requests may take longer to process and produce larger responses

## Best Practices

<Tip>
  **Image optimization**: Compress images before encoding to reduce payload size and token costs. Resize very large images before sending.

  **File preparation**: Ensure documents are text-based (not scanned images). For URLs, verify they return the file directly, not a preview page.

  **Filter strategy**: Start with broad filters and gradually refine based on result quality. Keep filter lists concise (≤10 entries) for best performance.
</Tip>

## Next Steps

<Card title="Sonar Quickstart" icon="rocket" href="/docs/sonar/quickstart">
  Get started with the Sonar API and learn the fundamentals
</Card>


Built with [Mintlify](https://mintlify.com).