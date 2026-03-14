# Source: https://docs.edenai.co/v3/features/translation/document-translation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Document Translation

> Document Translation API translates whole documents in supported languages and various file formats (like pdf or doc) while keeping their structure intact.

## Endpoint

`POST /v3/universal-ai` (sync)

Model string pattern: `translation/document_translation/{provider}[/{model}]`

## Input

| Field            | Type        | Required | Description                                                           |
| ---------------- | ----------- | -------- | --------------------------------------------------------------------- |
| file             | file\_input | Yes      | Document file ID from /v3/upload or direct file URL (PDF, DOCX, PPTX) |
| target\_language | string      | Yes      | Target language code                                                  |
| source\_language | string      | No       | Source language code                                                  |

## Output

| Field                   | Type   | Required | Description |
| ----------------------- | ------ | -------- | ----------- |
| file                    | string | Yes      |             |
| document\_resource\_url | string | Yes      |             |

## Available Providers

| Provider | Model String                              | Price            |
| -------- | ----------------------------------------- | ---------------- |
| deepl    | `translation/document_translation/deepl`  | \$2 per 20 pages |
| google   | `translation/document_translation/google` | \$0.08 per page  |

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
      "model": "translation/document_translation/deepl",
      "input": {
          "file": "YOUR_FILE_UUID_OR_URL",
          "target_language": "fr",
          "source_language": "en"
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
      "model": "translation/document_translation/deepl",
      "input": {"file": "YOUR_FILE_UUID_OR_URL", "target_language": "fr", "source_language": "en"}
    }'
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).