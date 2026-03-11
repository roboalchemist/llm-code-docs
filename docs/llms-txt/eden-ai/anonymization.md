# Source: https://docs.edenai.co/v3/features/image/anonymization.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Image Anonymization

> Image Anonymization API, also known as image de-identification or image de-personalization, refers to the process of automatically removing personal or sensitive information from images. The main...

## Endpoint

`POST /v3/universal-ai` (sync)

Model string pattern: `image/anonymization/{provider}[/{model}]`

## Input

| Field | Type        | Required | Description                                      |
| ----- | ----------- | -------- | ------------------------------------------------ |
| file  | file\_input | Yes      | Image file ID from /v3/upload or direct file URL |

## Output

| Field                   | Type           | Required | Description |
| ----------------------- | -------------- | -------- | ----------- |
| image                   | string         | Yes      |             |
| image\_resource\_url    | string         | Yes      |             |
| **items**               | array\[object] | No       |             |
|     kind                | string         | Yes      |             |
|     confidence          | float          | Yes      |             |
|     **bounding\_boxes** | object         | Yes      |             |
|         x\_min          | float          | Yes      |             |
|         x\_max          | float          | Yes      |             |
|         y\_min          | float          | Yes      |             |
|         y\_max          | float          | Yes      |             |

## Available Providers

| Provider | Model String                 | Price                |
| -------- | ---------------------------- | -------------------- |
| api4ai   | `image/anonymization/api4ai` | \$25 per 1,000 files |

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
      "model": "image/anonymization/api4ai",
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
      "model": "image/anonymization/api4ai",
      "input": {"file": "YOUR_FILE_UUID_OR_URL"}
    }'
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).