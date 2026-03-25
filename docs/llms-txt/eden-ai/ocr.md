# Source: https://docs.edenai.co/v3/features/ocr/ocr.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Text Detection (OCR)

> Optical Character Recognition or Reader (OCR) is the electronic or mechanical conversion of images of typed, handwritten or printed text into machine-encoded text. The image can be a scanned document...

## Endpoint

`POST /v3/universal-ai` (sync)

Model string pattern: `ocr/ocr/{provider}[/{model}]`

## Input

| Field    | Type        | Required | Description                                             |
| -------- | ----------- | -------- | ------------------------------------------------------- |
| file     | file\_input | Yes      | PDF or image file ID from /v3/upload or direct file URL |
| language | string      | Yes      | Document language code                                  |

## Output

| Field               | Type           | Required | Description |
| ------------------- | -------------- | -------- | ----------- |
| text                | string         | Yes      |             |
| **bounding\_boxes** | array\[object] | No       |             |
|     text            | string         | Yes      |             |
|     left            | float          | Yes      |             |
|     top             | float          | Yes      |             |
|     width           | float          | Yes      |             |
|     height          | float          | Yes      |             |

## Available Providers

| Provider   | Model String         | Price                  |
| ---------- | -------------------- | ---------------------- |
| amazon     | `ocr/ocr/amazon`     | \$1.5 per 1,000 pages  |
| api4ai     | `ocr/ocr/api4ai`     | \$3 per 1,000 requests |
| google     | `ocr/ocr/google`     | \$1.5 per 1,000 pages  |
| microsoft  | `ocr/ocr/microsoft`  | \$1 per 1,000 pages    |
| mistral    | `ocr/ocr/mistral`    | \$1 per 1,000 pages    |
| sentisight | `ocr/ocr/sentisight` | \$0.75 per 1,000 files |

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
      "model": "ocr/ocr/amazon",
      "input": {
          "file": "YOUR_FILE_UUID_OR_URL",
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
      "model": "ocr/ocr/amazon",
      "input": {"file": "YOUR_FILE_UUID_OR_URL", "language": "en"}
    }'
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).