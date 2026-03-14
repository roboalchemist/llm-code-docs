# Source: https://docs.edenai.co/v3/features/ocr/identity-parser.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Identity Parser

> ID Document parsing technology allows users to automatically extract information from an ID Document such as passport, ID card, driving license and more. This API is ideal for developers looking to...

## Endpoint

`POST /v3/universal-ai` (sync)

Model string pattern: `ocr/identity_parser/{provider}[/{model}]`

## Input

| Field | Type        | Required | Description                                             |
| ----- | ----------- | -------- | ------------------------------------------------------- |
| file  | file\_input | Yes      | PDF or image file ID from /v3/upload or direct file URL |

## Output

| Field                    | Type           | Required | Description |
| ------------------------ | -------------- | -------- | ----------- |
| **extracted\_data**      | array\[object] | No       |             |
|     **last\_name**       | object         | Yes      |             |
|         value            | string         | No       |             |
|         confidence       | float          | No       |             |
|     **given\_names**     | array\[object] | No       |             |
|         value            | string         | No       |             |
|         confidence       | float          | No       |             |
|     **birth\_place**     | object         | Yes      |             |
|         value            | string         | No       |             |
|         confidence       | float          | No       |             |
|     **birth\_date**      | object         | Yes      |             |
|         value            | string         | No       |             |
|         confidence       | float          | No       |             |
|     **issuance\_date**   | object         | Yes      |             |
|         value            | string         | No       |             |
|         confidence       | float          | No       |             |
|     **expire\_date**     | object         | Yes      |             |
|         value            | string         | No       |             |
|         confidence       | float          | No       |             |
|     **document\_id**     | object         | Yes      |             |
|         value            | string         | No       |             |
|         confidence       | float          | No       |             |
|     **issuing\_state**   | object         | Yes      |             |
|         value            | string         | No       |             |
|         confidence       | float          | No       |             |
|     **address**          | object         | Yes      |             |
|         value            | string         | No       |             |
|         confidence       | float          | No       |             |
|     **age**              | object         | Yes      |             |
|         value            | string         | No       |             |
|         confidence       | float          | No       |             |
|     **country**          | object         | Yes      |             |
|         name             | string         | Yes      |             |
|         alpha2           | string         | Yes      |             |
|         alpha3           | string         | Yes      |             |
|         confidence       | float          | No       |             |
|     **document\_type**   | object         | Yes      |             |
|         value            | string         | No       |             |
|         confidence       | float          | No       |             |
|     **gender**           | object         | Yes      |             |
|         value            | string         | No       |             |
|         confidence       | float          | No       |             |
|     **image\_id**        | array\[object] | No       |             |
|         value            | string         | No       |             |
|         confidence       | float          | No       |             |
|     **image\_signature** | array\[object] | No       |             |
|         value            | string         | No       |             |
|         confidence       | float          | No       |             |
|     **mrz**              | object         | Yes      |             |
|         value            | string         | No       |             |
|         confidence       | float          | No       |             |
|     **nationality**      | object         | Yes      |             |
|         value            | string         | No       |             |
|         confidence       | float          | No       |             |

## Available Providers

| Provider        | Model String                        | Price            |
| --------------- | ----------------------------------- | ---------------- |
| affinda         | `ocr/identity_parser/affinda`       | \$0.07 per file  |
| amazon          | `ocr/identity_parser/amazon`        | \$0.025 per page |
| base64          | `ocr/identity_parser/base64`        | \$0.2 per page   |
| klippa          | `ocr/identity_parser/klippa`        | \$0.1 per file   |
| microsoft       | `ocr/identity_parser/microsoft`     | \$0.01 per page  |
| mindee          | `ocr/identity_parser/mindee`        | \$0.1 per page   |
| openai          | `ocr/identity_parser/openai`        | \$0.02 per page  |
| openai (gpt-4o) | `ocr/identity_parser/openai/gpt-4o` | \$0.02 per page  |

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
      "model": "ocr/identity_parser/affinda",
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
      "model": "ocr/identity_parser/affinda",
      "input": {"file": "YOUR_FILE_UUID_OR_URL"}
    }'
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).