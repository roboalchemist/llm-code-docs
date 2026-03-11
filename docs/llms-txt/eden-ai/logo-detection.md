# Source: https://docs.edenai.co/v3/features/image/logo-detection.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Image Logo Detection

> Logo Detection is a powerful technology that enables the automatic identification and recognition of popular logos within an image. It provides accurate and efficient detection of known (and less...

## Endpoint

`POST /v3/universal-ai` (sync)

Model string pattern: `image/logo_detection/{provider}[/{model}]`

## Input

| Field | Type        | Required | Description                                      |
| ----- | ----------- | -------- | ------------------------------------------------ |
| file  | file\_input | Yes      | Image file ID from /v3/upload or direct file URL |

## Output

| Field                  | Type           | Required | Description                                         |
| ---------------------- | -------------- | -------- | --------------------------------------------------- |
| **items**              | array\[object] | No       | List of the detected brands logo from the image.    |
|     **bounding\_poly** | object         | No       |                                                     |
|         **vertices**   | array\[object] | No       | Vertices of the logos in the image                  |
|             x          | float          | Yes      | The x-coordinate of the vertex.                     |
|             y          | float          | Yes      | The y-coordinate of the vertex.                     |
|     description        | string         | Yes      | Name of the logo                                    |
|     score              | float          | Yes      | Confidence score how sure it's this is a real logo. |

## Available Providers

| Provider             | Model String                              | Price                  |
| -------------------- | ----------------------------------------- | ---------------------- |
| api4ai               | `image/logo_detection/api4ai`             | \$0.25 per 1,000 files |
| api4ai (v1)          | `image/logo_detection/api4ai/v1`          | \$0.25 per 1,000 files |
| api4ai (v2)          | `image/logo_detection/api4ai/v2`          | \$2.5 per 1,000 files  |
| clarifai             | `image/logo_detection/clarifai`           | \$2 per 1,000 files    |
| google               | `image/logo_detection/google`             | \$1.5 per 1,000 files  |
| microsoft            | `image/logo_detection/microsoft`          | \$1 per 1,000 files    |
| openai               | `image/logo_detection/openai`             | \$24 per 1,000 files   |
| openai (gpt-4o)      | `image/logo_detection/openai/gpt-4o`      | \$24 per 1,000 files   |
| openai (gpt-4-turbo) | `image/logo_detection/openai/gpt-4-turbo` | \$48 per 1,000 files   |

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
      "model": "image/logo_detection/api4ai",
      "input": {
          "file": "YOUR_FILE_UUID_OR_URL"
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
      "model": "image/logo_detection/api4ai",
      "input": {"file": "YOUR_FILE_UUID_OR_URL"}
    }'
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).