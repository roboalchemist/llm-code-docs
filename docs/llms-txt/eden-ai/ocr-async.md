# Source: https://docs.edenai.co/v3/features/ocr/ocr-async.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# OCR Multipage

> OCR or Optical Character Recognition is also referred to as text recognition or text extraction. It allows users to extract text data from PDFs with multiple pages.

## Endpoint

`POST /v3/universal-ai/async` (async)

Model string pattern: `ocr/ocr_async/{provider}[/{model}]`

## Input

| Field | Type        | Required | Description                                             |
| ----- | ----------- | -------- | ------------------------------------------------------- |
| file  | file\_input | Yes      | PDF or image file ID from /v3/upload or direct file URL |

## Output

| Field                         | Type           | Required | Description                             |
| ----------------------------- | -------------- | -------- | --------------------------------------- |
| raw\_text                     | string         | Yes      |                                         |
| **pages**                     | array\[object] | No       | List of pages                           |
|     **lines**                 | array\[object] | No       | List of lines                           |
|         text                  | string         | Yes      | Text detected in the line               |
|         **words**             | array\[object] | No       | List of words                           |
|             text              | string         | Yes      | Text detected in the word               |
|             **bounding\_box** | object         | Yes      | Bounding boxes of the words in the word |
|                 left          | float          | Yes      | Left coordinate of the bounding box     |
|                 top           | float          | Yes      | Top coordinate of the bounding box      |
|                 width         | float          | Yes      | Width of the bounding box               |
|                 height        | float          | Yes      | Height of the bounding box              |
|             confidence        | float          | Yes      | Confidence score of the word            |
|         **bounding\_box**     | object         | No       | Bounding box of the line, can be None   |
|             left              | float          | Yes      | Left coordinate of the bounding box     |
|             top               | float          | Yes      | Top coordinate of the bounding box      |
|             width             | float          | Yes      | Width of the bounding box               |
|             height            | float          | Yes      | Height of the bounding box              |
|         confidence            | float          | Yes      | Confidence of the line                  |
| number\_of\_pages             | int            | Yes      | Number of pages in the document         |

## Available Providers

| Provider  | Model String              | Price                 |
| --------- | ------------------------- | --------------------- |
| amazon    | `ocr/ocr_async/amazon`    | \$1.5 per 1,000 pages |
| microsoft | `ocr/ocr_async/microsoft` | \$10 per 1,000 pages  |
| mistral   | `ocr/ocr_async/mistral`   | \$1 per 1,000 pages   |

## Quick Start

> This is an **async** feature. The initial response returns a job ID. Poll `GET /v3/universal-ai/async/{job_id}` until the job completes.

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/universal-ai/async"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "ocr/ocr_async/amazon",
      "input": {
          "file": "YOUR_FILE_UUID_OR_URL"
      }
  }

  response = requests.post(url, headers=headers, json=payload)
  print(response.json())
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.edenai.run/v3/universal-ai/async \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "ocr/ocr_async/amazon",
      "input": {"file": "YOUR_FILE_UUID_OR_URL"}
    }'
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).