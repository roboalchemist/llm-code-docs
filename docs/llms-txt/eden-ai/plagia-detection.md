# Source: https://docs.edenai.co/v3/features/text/plagia-detection.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Plagiarism Detection

> The Plagiarism Detection API is a tool designed to scan a content string for plagiarism using a plagiarism detection module

## Endpoint

`POST /v3/universal-ai` (sync)

Model string pattern: `text/plagia_detection/{provider}[/{model}]`

## Input

| Field | Type   | Required | Description                                            |
| ----- | ------ | -------- | ------------------------------------------------------ |
| text  | string | Yes      | Text content on which plagiarism detection will be run |
| title | string | No       | Content title                                          |

## Output

| Field                     | Type           | Required | Description |
| ------------------------- | -------------- | -------- | ----------- |
| plagia\_score             | float          | Yes      |             |
| **items**                 | array\[object] | No       |             |
|     text                  | string         | Yes      |             |
|     **candidates**        | array\[object] | No       |             |
|         url               | string         | Yes      |             |
|         plagia\_score     | float          | Yes      |             |
|         prediction        | string         | Yes      |             |
|         plagiarized\_text | string         | Yes      |             |

## Available Providers

| Provider  | Model String                      | Price                    |
| --------- | --------------------------------- | ------------------------ |
| winstonai | `text/plagia_detection/winstonai` | \$14 per 1,000,000 chars |

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
      "model": "text/plagia_detection/winstonai",
      "input": {
          "text": "The quick brown fox jumps over the lazy dog."
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
      "model": "text/plagia_detection/winstonai",
      "input": {"text": "The quick brown fox jumps over the lazy dog."}
    }'
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).