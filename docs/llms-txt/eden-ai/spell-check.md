# Source: https://docs.edenai.co/v3/features/text/spell-check.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Grammar Spell Check

> Spell Check analyzes the inputted text by comparing it to a dictionary of correctly spelled words to identify and highlight any spelling errors or grammatical mistakes.

## Endpoint

`POST /v3/universal-ai` (sync)

Model string pattern: `text/spell_check/{provider}[/{model}]`

## Input

| Field    | Type   | Required | Description              |
| -------- | ------ | -------- | ------------------------ |
| text     | string | Yes      | Text to be spell-checked |
| language | string | No       | ISO 639-1 language code  |

## Output

| Field               | Type           | Required | Description |
| ------------------- | -------------- | -------- | ----------- |
| text                | string         | Yes      |             |
| **items**           | array\[object] | No       |             |
|     text            | string         | Yes      |             |
|     type            | string         | Yes      |             |
|     offset          | int            | Yes      |             |
|     length          | int            | Yes      |             |
|     **suggestions** | array\[object] | No       |             |
|         suggestion  | string         | Yes      |             |
|         score       | float          | Yes      |             |

## Available Providers

| Provider      | Model String                     | Price                   |
| ------------- | -------------------------------- | ----------------------- |
| prowritingaid | `text/spell_check/prowritingaid` | \$10 per 1,000 requests |
| sapling       | `text/spell_check/sapling`       | \$2 per 1,000,000 chars |

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
      "model": "text/spell_check/prowritingaid",
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
      "model": "text/spell_check/prowritingaid",
      "input": {"text": "The quick brown fox jumps over the lazy dog.", "language": "en"}
    }'
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).