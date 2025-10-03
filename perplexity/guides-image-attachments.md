# Source: https://docs.perplexity.ai/guides/image-attachments

## 
[​](https://docs.perplexity.ai/guides/image-attachments#overview)
Overview
Sonar models support image analysis through direct image uploads. You can include images in your API requests to support multi-modal conversations alongside text. Images can be provided either as base64 encoded strings within a data URI or as standard HTTPS URLs.
**SDK Installation Required** : Install the official SDK first - `pip install perplexityai` for Python or `npm install @perplexity-ai/perplexity_ai` for TypeScript/JavaScript.
  * When using base64 encoding, the API currently only supports images up to 50 MB per image.
  * Supported formats for base64 encoded images: PNG (image/png), JPEG (image/jpeg), WEBP (image/webp), and GIF (image/gif).
  * When using an HTTPS URL, the model will attempt to fetch the image from the provided URL. Ensure the URL is publicly accessible.


## 
[​](https://docs.perplexity.ai/guides/image-attachments#supported-features)
Supported Features
Image uploads can be useful for:
  * **Visual Question Answering** : Ask questions about visual content (e.g., text in a screenshot, diagram interpretation)
  * **Context Analysis** : Providing context for follow-up queries
  * **Multi-modal Conversations** : Analyzing visual media as part of a multi-turn conversation
  * **Content Description** : Get detailed descriptions of images
  * **Text Extraction** : Extract text from images and documents


## 
[​](https://docs.perplexity.ai/guides/image-attachments#upload-methods)
Upload Methods
You can include images in your requests using two methods:
### 
[​](https://docs.perplexity.ai/guides/image-attachments#1-base64-data-uri)
1. Base64 Data URI
Encode the image as a base64 string and embed it in a data URI:
Copy
Ask AI
```
data:image/png;base64,<BASE64_ENCODED_IMAGE>

```

Replace `image/png` with the correct MIME type if you’re using JPEG or GIF (`image/jpeg` or `image/gif`).
### 
[​](https://docs.perplexity.ai/guides/image-attachments#2-https-url)
2. HTTPS URL
Provide a standard HTTPS URL pointing directly to the image file:
Copy
Ask AI
```
https://example.com/path/to/your/image.png

```

## 
[​](https://docs.perplexity.ai/guides/image-attachments#request-format)
Request Format
Images must be embedded in the `messages` array, alongside any text input. Each image should be provided using the following structure: **Using Base64 Data URI:**
Copy
Ask AI
```
{
  "type": "image_url",
  "image_url": {
    "url": "data:image/png;base64,<BASE64_ENCODED_IMAGE>"
  }
}

```

**Using HTTPS URL:**
Copy
Ask AI
```
{
  "type": "image_url",
  "image_url": {
    "url": "https://example.com/path/to/your/image.png"
  }
}

```

## 
[​](https://docs.perplexity.ai/guides/image-attachments#basic-usage)
Basic Usage
  * Base64 Encoding
  * HTTPS URL


Use this method when you have the image file locally and want to embed it directly into the request payload. Remember the 50MB size limit and supported formats (PNG, JPEG, WEBP, GIF).
cURL
Python
JavaScript
TypeScript
Copy
Ask AI
```
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

## 
[​](https://docs.perplexity.ai/guides/image-attachments#common-use-cases)
Common Use Cases
### 
[​](https://docs.perplexity.ai/guides/image-attachments#screenshot-analysis)
Screenshot Analysis
Copy
Ask AI
```
question = "What text is visible in this screenshot?"

```

### 
[​](https://docs.perplexity.ai/guides/image-attachments#diagram-interpretation)
Diagram Interpretation
Copy
Ask AI
```
question = "Explain the workflow shown in this diagram"

```

### 
[​](https://docs.perplexity.ai/guides/image-attachments#product-analysis)
Product Analysis
Copy
Ask AI
```
question = "Describe the features and specifications of this product"

```

### 
[​](https://docs.perplexity.ai/guides/image-attachments#document-processing)
Document Processing
Copy
Ask AI
```
question = "Extract all the key information from this document image"

```

## 
[​](https://docs.perplexity.ai/guides/image-attachments#best-practices)
Best Practices
Image Quality Guidelines
  * Use high-resolution images for better text extraction
  * Ensure good contrast for text recognition
  * Avoid heavily compressed images when detail is important
  * Use appropriate image formats (PNG for screenshots, JPEG for photos)


File Size Optimization
  * Keep images under 50MB for base64 encoding
  * Compress images when possible without losing critical detail
  * Consider using HTTPS URLs for very large images
  * Use WebP format for balanced quality and size


URL Best Practices
  * Ensure URLs are publicly accessible (no authentication required)
  * Use direct links to image files, not web pages
  * Test URLs in a browser before using in API calls
  * Consider using CDNs for reliable image hosting


## 
[​](https://docs.perplexity.ai/guides/image-attachments#pricing)
Pricing
Images are tokenized based on their pixel dimensions using the following formula:
Copy
Ask AI
```
tokens = (width px × height px) / 750

```

**Examples:**
  * A 1024×768 image would consume: (1024 × 768) / 750 = 1,048 tokens
  * A 512×512 image would consume: (512 × 512) / 750 = 349 tokens

These image tokens are then priced according to the input token pricing of the model you’re using (e.g., `sonar-pro`, `sonar`, etc.). The image tokens are added to your total token count for the request alongside any text tokens.
To optimize costs, resize images to the minimum resolution needed for your use case while maintaining adequate quality.
## 
[​](https://docs.perplexity.ai/guides/image-attachments#limitations)
Limitations
  * Image and regex cannot be used together in the same request
  * `sonar-deep-research` does not support image input
  * Ensure provided HTTPS URLs are publicly accessible
  * Base64 images have a 50MB size limit
  * Supported formats: PNG, JPEG, WEBP, and GIF


