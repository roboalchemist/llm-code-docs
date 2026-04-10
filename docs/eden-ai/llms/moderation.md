# Source: https://docs.edenai.co/v3/features/text/moderation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Text Moderation

> Text moderation scans text for offensive, sexually explicit or suggestive content, it also checks if there is any content of self-harm, violence, racist or hate speech.

## Endpoint

`POST /v3/universal-ai` (sync)

Model string pattern: `text/moderation/{provider}[/{model}]`

## Input

| Field    | Type   | Required | Description             |
| -------- | ------ | -------- | ----------------------- |
| text     | string | Yes      | Text to moderate        |
| language | string | No       | ISO 639-1 language code |

## Output

| Field                   | Type           | Required | Description |
| ----------------------- | -------------- | -------- | ----------- |
| nsfw\_likelihood        | int            | Yes      |             |
| **items**               | array\[object] | No       |             |
|     label               | string         | Yes      |             |
|     likelihood          | int            | Yes      |             |
|     category            | enum           | Yes      |             |
|     subcategory         | enum           | Yes      |             |
|     likelihood\_score   | float          | Yes      |             |
| nsfw\_likelihood\_score | float          | Yes      |             |

## Available Providers

| Provider                        | Model String                                    | Price                   |
| ------------------------------- | ----------------------------------------------- | ----------------------- |
| google                          | `text/moderation/google`                        | \$5 per 1,000,000 chars |
| microsoft                       | `text/moderation/microsoft`                     | \$1 per 1,000 requests  |
| openai                          | `text/moderation/openai`                        | Free                    |
| openai (text-moderation-007)    | `text/moderation/openai/text-moderation-007`    | Free                    |
| openai (text-moderation-latest) | `text/moderation/openai/text-moderation-latest` | Free                    |
| openai (text-moderation-stable) | `text/moderation/openai/text-moderation-stable` | Free                    |

## Quick Start

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/universal-ai"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "text/moderation/google",
      "input": {
          "text": "The quick brown fox jumps over the lazy dog.",
          "language": "en"
      }
  }

  response = requests.post(url, headers=headers, json=payload)
  print(response.json())
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.edenai.run/v3/universal-ai \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "text/moderation/google",
      "input": {"text": "The quick brown fox jumps over the lazy dog.", "language": "en"}
    }'
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).