# Source: https://docs.edenai.co/v3/features/image/explicit-content.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Image Explicit Content

> Explicit Content Detection detects adult only content in images, that is generally inappropriate for people under the age of 18 and includes nudity, sexual activity, pornography, violence, gore...

## Endpoint

`POST /v3/universal-ai` (sync)

Model string pattern: `image/explicit_content/{provider}[/{model}]`

## Input

| Field | Type        | Required | Description                                      |
| ----- | ----------- | -------- | ------------------------------------------------ |
| file  | file\_input | Yes      | Image file ID from /v3/upload or direct file URL |

## Output

| Field                   | Type           | Required | Description                                                                                                                                                                |
| ----------------------- | -------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| nsfw\_likelihood        | int            | Yes      | An integer representing the likelihood of NSFW content. Higher values indicate a higher likelihood.                                                                        |
| nsfw\_likelihood\_score | float          | Yes      | A floating-point score representing the confidence level of the NSFW likelihood assessment. This is typically a value between 0.0 and 1.0.                                 |
| **items**               | array\[object] | No       | A list of items identified as potentially explicit. Each item contains details of the explicit content detected.                                                           |
|     label               | string         | Yes      |                                                                                                                                                                            |
|     likelihood          | int            | Yes      |                                                                                                                                                                            |
|     likelihood\_score   | float          | Yes      |                                                                                                                                                                            |
|     category            | enum           | Yes      | The category of the detected content. Possible values include: 'Toxic', 'Content', 'Sexual', 'Violence', 'DrugAndAlcohol', 'Finance', 'HateAndExtremism', 'Safe', 'Other'. |
|     subcategory         | string         | Yes      | The subcategory of content. Possible values:                                                                                                                               |

Toxic Subcategories:

* Insult
* Obscene
* Derogatory
* Profanity
* Threat
* Toxic

Content Subcategories:

* MiddleFinger
* PublicSafety
* Health
* Explicit
* QRCode
* Medical
* Politics
* Legal

Sexual Subcategories:

* SexualActivity
* SexualSituations
* Nudity
* PartialNudity
* Suggestive
* AdultToys
* RevealingClothes
* Sexual

Violence Subcategories:

* GraphicViolenceOrGore
* PhysicalViolence
* WeaponViolence
* Violence

Drug and Alcohol Subcategories:

* DrugProducts
* DrugUse
* Tobacco
* Smoking
* Alcohol
* Drinking

Finance Subcategories:

* Gambling
* Finance
* MoneyContent

Hate and Extremism Subcategories:

* Hate
* Harassment
* Threatening
* Extremist
* Racy

Safe Subcategories:

* Safe
* NotSafe

Other Subcategories:

* Spoof
* Religion
* Offensive
* Other |

## Available Providers

| Provider        | Model String                           | Price                  |
| --------------- | -------------------------------------- | ---------------------- |
| amazon          | `image/explicit_content/amazon`        | \$1 per 1,000 files    |
| clarifai        | `image/explicit_content/clarifai`      | \$2 per 1,000 files    |
| google          | `image/explicit_content/google`        | \$1.5 per 1,000 files  |
| microsoft       | `image/explicit_content/microsoft`     | \$1 per 1,000 files    |
| openai          | `image/explicit_content/openai`        | \$24 per 1,000 files   |
| openai (gpt-4o) | `image/explicit_content/openai/gpt-4o` | \$24 per 1,000 files   |
| sentisight      | `image/explicit_content/sentisight`    | \$0.75 per 1,000 files |

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
      "model": "image/explicit_content/amazon",
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
      "model": "image/explicit_content/amazon",
      "input": {"file": "YOUR_FILE_UUID_OR_URL"}
    }'
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).