# Source: https://docs.edenai.co/v3/features/ocr/ocr-tables-async.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Table Extraction

> OCR Table (Optical Character Recognition for tabular documents)  allows users to analyze documents containing tables and returns a structured representation of the detected tables in the form of a...

## Endpoint

`POST /v3/universal-ai/async` (async)

Model string pattern: `ocr/ocr_tables_async/{provider}[/{model}]`

## Input

| Field | Type        | Required | Description                                             |
| ----- | ----------- | -------- | ------------------------------------------------------- |
| file  | file\_input | Yes      | PDF or image file ID from /v3/upload or direct file URL |

## Output

| Field                             | Type           | Required | Description |
| --------------------------------- | -------------- | -------- | ----------- |
| **pages**                         | array\[object] | No       |             |
|     **tables**                    | array\[object] | No       |             |
|         **rows**                  | array\[object] | No       |             |
|             **cells**             | array\[object] | No       |             |
|                 text              | string         | Yes      |             |
|                 row\_index        | int            | Yes      |             |
|                 col\_index        | int            | Yes      |             |
|                 row\_span         | int            | Yes      |             |
|                 col\_span         | int            | Yes      |             |
|                 confidence        | float          | Yes      |             |
|                 **bounding\_box** | object         | Yes      |             |
|                     left          | float          | Yes      |             |
|                     top           | float          | Yes      |             |
|                     width         | float          | Yes      |             |
|                     height        | float          | Yes      |             |
|                 is\_header        | bool           | No       |             |
|         num\_rows                 | int            | Yes      |             |
|         num\_cols                 | int            | Yes      |             |
| num\_pages                        | int            | Yes      |             |

## Available Providers

| Provider  | Model String                     | Price                |
| --------- | -------------------------------- | -------------------- |
| amazon    | `ocr/ocr_tables_async/amazon`    | \$15 per 1,000 pages |
| google    | `ocr/ocr_tables_async/google`    | \$65 per 1,000 pages |
| microsoft | `ocr/ocr_tables_async/microsoft` | \$10 per 1,000 pages |

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
      "model": "ocr/ocr_tables_async/amazon",
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
      "model": "ocr/ocr_tables_async/amazon",
      "input": {"file": "YOUR_FILE_UUID_OR_URL"}
    }'
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).