# Source: https://docs.edenai.co/v3/features/ocr/resume-parser.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Resume Parser

> Resume Parser enables users to extract various information from resumes (curriculum vitae, CV) that could be in a variety of formats and returns structured data (name, job list, education, skills) to...

## Endpoint

`POST /v3/universal-ai` (sync)

Model string pattern: `ocr/resume_parser/{provider}[/{model}]`

## Input

| Field | Type        | Required | Description                                |
| ----- | ----------- | -------- | ------------------------------------------ |
| file  | file\_input | Yes      | File ID from /v3/upload or direct file URL |

## Output

| Field                                | Type           | Required | Description |
| ------------------------------------ | -------------- | -------- | ----------- |
| **extracted\_data**                  | object         | Yes      |             |
|     **personal\_infos**              | object         | Yes      |             |
|         **name**                     | object         | Yes      |             |
|             first\_name              | string         | Yes      |             |
|             last\_name               | string         | Yes      |             |
|             raw\_name                | string         | Yes      |             |
|             middle                   | string         | Yes      |             |
|             title                    | string         | Yes      |             |
|             prefix                   | string         | Yes      |             |
|             sufix                    | string         | Yes      |             |
|         **address**                  | object         | Yes      |             |
|             formatted\_location      | string         | Yes      |             |
|             postal\_code             | string         | Yes      |             |
|             region                   | string         | Yes      |             |
|             country                  | string         | Yes      |             |
|             country\_code            | string         | Yes      |             |
|             raw\_input\_location     | string         | Yes      |             |
|             street                   | string         | Yes      |             |
|             street\_number           | string         | Yes      |             |
|             appartment\_number       | string         | Yes      |             |
|             city                     | string         | Yes      |             |
|         self\_summary                | string         | Yes      |             |
|         objective                    | string         | Yes      |             |
|         date\_of\_birth              | string         | Yes      |             |
|         place\_of\_birth             | string         | Yes      |             |
|         phones                       | array\[string] | No       |             |
|         mails                        | array\[string] | No       |             |
|         urls                         | array\[string] | No       |             |
|         fax                          | array\[string] | No       |             |
|         current\_profession          | string         | Yes      |             |
|         gender                       | string         | Yes      |             |
|         nationality                  | string         | Yes      |             |
|         martial\_status              | string         | Yes      |             |
|         current\_salary              | string         | Yes      |             |
|         availability                 | string         | No       |             |
|     **education**                    | object         | Yes      |             |
|         total\_years\_education      | int            | Yes      |             |
|         **entries**                  | array\[object] | No       |             |
|             title                    | string         | Yes      |             |
|             start\_date              | string         | Yes      |             |
|             end\_date                | string         | Yes      |             |
|             **location**             | object         | Yes      |             |
|                 formatted\_location  | string         | Yes      |             |
|                 postal\_code         | string         | Yes      |             |
|                 region               | string         | Yes      |             |
|                 country              | string         | Yes      |             |
|                 country\_code        | string         | Yes      |             |
|                 raw\_input\_location | string         | Yes      |             |
|                 street               | string         | Yes      |             |
|                 street\_number       | string         | Yes      |             |
|                 appartment\_number   | string         | Yes      |             |
|                 city                 | string         | Yes      |             |
|             establishment            | string         | Yes      |             |
|             description              | string         | Yes      |             |
|             gpa                      | string         | Yes      |             |
|             accreditation            | string         | Yes      |             |
|     **work\_experience**             | object         | Yes      |             |
|         total\_years\_experience     | string         | Yes      |             |
|         **entries**                  | array\[object] | No       |             |
|             title                    | string         | Yes      |             |
|             start\_date              | string         | Yes      |             |
|             end\_date                | string         | Yes      |             |
|             company                  | string         | Yes      |             |
|             **location**             | object         | Yes      |             |
|                 formatted\_location  | string         | Yes      |             |
|                 postal\_code         | string         | Yes      |             |
|                 region               | string         | Yes      |             |
|                 country              | string         | Yes      |             |
|                 country\_code        | string         | Yes      |             |
|                 raw\_input\_location | string         | Yes      |             |
|                 street               | string         | Yes      |             |
|                 street\_number       | string         | Yes      |             |
|                 appartment\_number   | string         | Yes      |             |
|                 city                 | string         | Yes      |             |
|             description              | string         | Yes      |             |
|             type                     | string         | No       |             |
|             industry                 | string         | Yes      |             |
|     **languages**                    | array\[object] | No       |             |
|         name                         | string         | Yes      |             |
|         code                         | string         | Yes      |             |
|     **skills**                       | array\[object] | No       |             |
|         name                         | string         | Yes      |             |
|         type                         | string         | Yes      |             |
|     **certifications**               | array\[object] | No       |             |
|         name                         | string         | Yes      |             |
|         type                         | string         | Yes      |             |
|     **courses**                      | array\[object] | No       |             |
|         name                         | string         | Yes      |             |
|         type                         | string         | Yes      |             |
|     **publications**                 | array\[object] | No       |             |
|         name                         | string         | Yes      |             |
|         type                         | string         | Yes      |             |
|     **interests**                    | array\[object] | No       |             |
|         name                         | string         | Yes      |             |
|         type                         | string         | Yes      |             |

## Available Providers

| Provider        | Model String                      | Price            |
| --------------- | --------------------------------- | ---------------- |
| affinda         | `ocr/resume_parser/affinda`       | \$0.07 per file  |
| extracta        | `ocr/resume_parser/extracta`      | \$0.1 per page   |
| klippa          | `ocr/resume_parser/klippa`        | \$0.1 per file   |
| openai          | `ocr/resume_parser/openai`        | \$0.04 per page  |
| openai (gpt-4o) | `ocr/resume_parser/openai/gpt-4o` | \$0.04 per page  |
| senseloaf       | `ocr/resume_parser/senseloaf`     | \$0.045 per file |

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
      "model": "ocr/resume_parser/affinda",
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
      "model": "ocr/resume_parser/affinda",
      "input": {"file": "YOUR_FILE_UUID_OR_URL"}
    }'
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).