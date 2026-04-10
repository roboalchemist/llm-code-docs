# Source: https://docs.edenai.co/v3/features/image/face-compare.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Image Face Comparison

> Compare two faces and decide whether they are from the same person. The API expects 2 images, reference and query, where the former is the ground truth (e.g. user's official ID) and the latter is the...

## Endpoint

`POST /v3/universal-ai` (sync)

Model string pattern: `image/face_compare/{provider}[/{model}]`

## Input

| Field | Type        | Required | Description                                      |
| ----- | ----------- | -------- | ------------------------------------------------ |
| file1 | file\_input | Yes      | Image file ID from /v3/upload or direct file URL |
| file2 | file\_input | Yes      | Image file ID from /v3/upload or direct file URL |

## Output

| Field                 | Type           | Required | Description |
| --------------------- | -------------- | -------- | ----------- |
| **items**             | array\[object] | No       |             |
|     confidence        | float          | Yes      |             |
|     **bounding\_box** | object         | Yes      |             |
|         top           | float          | Yes      |             |
|         left          | float          | Yes      |             |
|         height        | float          | Yes      |             |
|         width         | float          | Yes      |             |

## Available Providers

| Provider | Model String                | Price                  |
| -------- | --------------------------- | ---------------------- |
| amazon   | `image/face_compare/amazon` | \$1 per 1,000 requests |
| base64   | `image/face_compare/base64` | \$0.25 per request     |
| facepp   | `image/face_compare/facepp` | \$2 per 1,000 requests |

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
      "model": "image/face_compare/amazon",
      "input": {
          "file1": "YOUR_FILE_UUID_OR_URL",
          "file2": "YOUR_FILE_UUID_OR_URL"
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
      "model": "image/face_compare/amazon",
      "input": {"file1": "YOUR_FILE_UUID_OR_URL", "file2": "YOUR_FILE_UUID_OR_URL"}
    }'
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).