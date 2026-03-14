# Eden Ai Documentation

Source: https://docs.edenai.co/llms-full.txt

---

# Chat Completions
Source: https://docs.edenai.co/api-reference/completions/chat-completions

openapi/v3-openapi.json post /v3/llm/chat/completions
OpenAI-compatible chat completions endpoint (v3).



# List Models
Source: https://docs.edenai.co/api-reference/completions/list-models

openapi/v3-openapi.json get /v3/llm/models
List available LLM models with extended metadata.



# Monitor Consumptions
Source: https://docs.edenai.co/api-reference/cost-monitoring/monitor-consumptions

openapi/v3-cost-management.json get /cost_management/



# My Credits
Source: https://docs.edenai.co/api-reference/cost-monitoring/my-credits

openapi/v3-cost-management.json get /cost_management/credits/
Get you current credits



# Delete All Files
Source: https://docs.edenai.co/api-reference/files-management/delete-all-files

openapi/v3-openapi.json delete /v3/upload
Delete all uploaded files for the authenticated user.

This permanently deletes all files from storage.
This action cannot be undone.



# Delete Files By Ids
Source: https://docs.edenai.co/api-reference/files-management/delete-files-by-ids

openapi/v3-openapi.json post /v3/upload/delete
Delete specific files by their IDs.

Only files owned by the authenticated user will be deleted.
Files that don't exist or aren't owned by the user are silently ignored.
This action cannot be undone.



# List Files
Source: https://docs.edenai.co/api-reference/files-management/list-files

openapi/v3-openapi.json get /v3/upload
List uploaded files for the authenticated user.

Optionally filter by purpose. Only returns non-expired files.
Results are ordered by creation date (newest first).



# Upload File
Source: https://docs.edenai.co/api-reference/files-management/upload-file

openapi/v3-openapi.json post /v3/upload
Upload a file for persistent storage.

Returns a file_id that can be used in subsequent API calls to /v3/universal-ai.

Files are stored securely and only accessible by the file owner.
Default expiration is 30 days, maximum 30 days.



# Get Feature Info
Source: https://docs.edenai.co/api-reference/universal-ai-info/get-feature-info

openapi/v3-openapi.json get /v3/info/{feature}/{subfeature}
Get detailed information for a specific feature/subfeature.

Args:
    feature: Feature name (e.g., 'text', 'image', 'ocr', 'translation')
    subfeature: Subfeature name (e.g., 'ai_detection', 'ocr', 'generation')
    format: Schema output format (simplified or json_schema)

Returns:
    - Input schema
    - Output schema
    - Available providers and their models



# List Features
Source: https://docs.edenai.co/api-reference/universal-ai-info/list-features

openapi/v3-openapi.json get /v3/info
List all available features and their subfeatures.

Returns a simple dictionary mapping feature names to lists of subfeature names.



# List Subfeatures
Source: https://docs.edenai.co/api-reference/universal-ai-info/list-subfeatures

openapi/v3-openapi.json get /v3/info/{feature}
List all subfeatures for a specific feature.

Args:
    feature: Feature name (e.g., 'text', 'image', 'ocr', 'translation')

Returns:
    Dictionary with feature name and list of its subfeatures.



# Create Async Job
Source: https://docs.edenai.co/api-reference/universal-ai/create-async-job

openapi/v3-openapi.json post /v3/universal-ai/async
Submit an asynchronous Universal AI job for long-running AI features.

Model format: feature/subfeature/provider[/model]

Use this endpoint for features that require processing time (e.g., speech-to-text, OCR on large documents). The response returns a job ID that you can poll using `GET /v3/universal-ai/async/{job_id}`.

Request body is identical to the sync endpoint (`POST /v3/universal-ai`).

Example:
```json
{
    "model": "audio/speech_to_text_async/google",
    "input": {"file": "YOUR_FILE_UUID_OR_URL", "language": "en"}
}
```

Response (202 Accepted):
```json
{
    "public_id": "abc123-def456",
    "status": "processing",
    "cost": "0.000",
    "provider": "google",
    "feature": "audio",
    "subfeature": "speech_to_text_async",
    "output": null,
    "error": null,
    "model": null,
    "created_at": "2025-01-01T00:00:00Z"
}
```



# Delete Async Job
Source: https://docs.edenai.co/api-reference/universal-ai/delete-async-job

openapi/v3-openapi.json delete /v3/universal-ai/async/{job_id}
Delete an async job by ID.

This permanently removes the job and its results. This action cannot be undone.



# Get Async Job
Source: https://docs.edenai.co/api-reference/universal-ai/get-async-job

openapi/v3-openapi.json get /v3/universal-ai/async/{job_id}
Retrieve the status and results of an async job.

Poll this endpoint until `status` changes from `"processing"` to `"success"` or `"fail"`.

Example response (completed):
```json
{
    "public_id": "abc123-def456",
    "status": "success",
    "cost": "0.005",
    "provider": "google",
    "feature": "audio",
    "subfeature": "speech_to_text_async",
    "output": {"text": "Hello world", ...},
    "error": null,
    "model": null,
    "created_at": "2025-01-01T00:00:00Z"
}
```



# List Async Jobs
Source: https://docs.edenai.co/api-reference/universal-ai/list-async-jobs

openapi/v3-openapi.json get /v3/universal-ai/async
List all async jobs for the authenticated user.

Results are ordered by creation date (newest first). Supports filtering by feature, subfeature, and status.



# Universal Ai
Source: https://docs.edenai.co/api-reference/universal-ai/universal-ai

openapi/v3-openapi.json post /v3/universal-ai
Universal AI endpoint for all non-LLM AI features.

Model format: feature/subfeature/provider[/model]

Request body:
- model: Model string in format feature/subfeature/provider[/model]
- input: Feature-specific input parameters
- provider_params: Optional provider-specific parameters
- show_original_response: Include raw provider response (default: false)

Example:
```json
{
    "model": "text/moderation/google",
    "input": {"text": "Content to moderate"}
}
```

Response:
```json
{
    "status": "success",
    "cost": "0.001",
    "provider": "google",
    "feature": "text",
    "subfeature": "moderation",
    "output": {...},
    "error": null
}
```



# Create new Token
Source: https://docs.edenai.co/api-reference/user-management/create-new-token

openapi/v3-user.json post /user/custom_token/



# Delete Token
Source: https://docs.edenai.co/api-reference/user-management/delete-token

openapi/v3-user.json delete /user/custom_token/{name}/



# List Tokens
Source: https://docs.edenai.co/api-reference/user-management/list-tokens

openapi/v3-user.json get /user/custom_token/



# Retrieve Token
Source: https://docs.edenai.co/api-reference/user-management/retrieve-token

openapi/v3-user.json get /user/custom_token/{name}/



# Update Token
Source: https://docs.edenai.co/api-reference/user-management/update-token

openapi/v3-user.json patch /user/custom_token/{name}/



# Changelog
Source: https://docs.edenai.co/v3/changelog

Latest updates and changes to Eden AI

<Update label="2026-02-17">
  ## Changelog launched

  Initiating back the changelog.
</Update>


# Speech To Text
Source: https://docs.edenai.co/v3/features/audio/speech-to-text-async

Speech Recognition (or speech to text or voice to text) can recognize and transcribe spoken words (voice),  that will be converted to text with or without diarization. It is also possible to filter...

## Endpoint

`POST /v3/universal-ai/async` (async)

Model string pattern: `audio/speech_to_text_async/{provider}[/{model}]`

## Input

| Field             | Type           | Required | Description                                                                            |
| ----------------- | -------------- | -------- | -------------------------------------------------------------------------------------- |
| file              | file\_input    | Yes      | Audio file ID from /v3/upload or direct file URL                                       |
| language          | string         | No       | Language code in ISO format (e.g., 'en', 'fr', 'es')                                   |
| speakers          | int            | No       | Number of speakers present in the audio                                                |
| profanity\_filter | bool           | No       | Whether to filter profanity and replace inappropriate words with a series of asterisks |
| vocabulary        | array\[string] | No       | List of words or composed words to be detected by the speech to text engine            |

## Output

| Field               | Type           | Required | Description |
| ------------------- | -------------- | -------- | ----------- |
| text                | string         | Yes      |             |
| **diarization**     | object         | Yes      |             |
|     total\_speakers | int            | Yes      |             |
|     **entries**     | array\[object] | No       |             |
|         segment     | string         | Yes      |             |
|         start\_time | string         | Yes      |             |
|         end\_time   | string         | Yes      |             |
|         speaker     | int            | Yes      |             |
|         confidence  | float          | Yes      |             |
|     error\_message  | string         | No       |             |

## Available Providers

| Provider            | Model String                                   | Price                    |
| ------------------- | ---------------------------------------------- | ------------------------ |
| amazon              | `audio/speech_to_text_async/amazon`            | \$0.024 per 60 secondes  |
| assembly            | `audio/speech_to_text_async/assembly`          | \$0.011 per 60 secondes  |
| deepgram (base)     | `audio/speech_to_text_async/deepgram/base`     | \$0.0169 per 60 secondes |
| deepgram            | `audio/speech_to_text_async/deepgram`          | \$0.0189 per 60 secondes |
| deepgram (enhanced) | `audio/speech_to_text_async/deepgram/enhanced` | \$0.0189 per 60 secondes |
| deepgram (nova-3)   | `audio/speech_to_text_async/deepgram/nova-3`   | \$0.0052 per 60 secondes |
| gladia              | `audio/speech_to_text_async/gladia`            | \$0.0102 per 60 secondes |
| google              | `audio/speech_to_text_async/google`            | \$0.024 per 60 secondes  |
| microsoft           | `audio/speech_to_text_async/microsoft`         | \$0.0168 per 60 secondes |
| openai              | `audio/speech_to_text_async/openai`            | \$0.006 per 60 secondes  |

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
      "model": "audio/speech_to_text_async/amazon",
      "input": {
          "file": "YOUR_FILE_UUID_OR_URL",
          "language": "en"
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
      "model": "audio/speech_to_text_async/amazon",
      "input": {"file": "YOUR_FILE_UUID_OR_URL", "language": "en"}
    }'
  ```
</CodeGroup>


# Text to Speech
Source: https://docs.edenai.co/v3/features/audio/tts

Text-to-speech (TTS) is a technology that converts written text into spoken audio, enabling computers and digital devices to "read" text aloud.  It is also known as speech synthesis, read aloud...

## Endpoint

`POST /v3/universal-ai` (sync)

Model string pattern: `audio/tts/{provider}[/{model}]`

## Input

| Field                                                                                     | Type   | Required | Description                                                                              |
| ----------------------------------------------------------------------------------------- | ------ | -------- | ---------------------------------------------------------------------------------------- |
| text                                                                                      | string | Yes      | Text to convert to speech                                                                |
| voice                                                                                     | string | No       | Voice identifier to use for synthesis, can be name or id.                                |
| For supported voices for your provider/model, please check each provider's documentation. |        |          |                                                                                          |
| speed                                                                                     | float  | No       | Speed multiplier for speech synthesis                                                    |
| audio\_format                                                                             | string | No       | Desired audio format (e.g., 'mp3', 'wav')                                                |
| speaking\_pitch                                                                           | int    | No       | Increase or decrease the speaking pitch by a percentage from -100% to 100%, 0 is normal. |
| speaking\_volume                                                                          | int    | No       | Increase or decrease the audio volume by a percentage from -100% to 100%, 0 is normal.   |

## Output

| Field                | Type   | Required | Description |
| -------------------- | ------ | -------- | ----------- |
| audio\_resource\_url | string | Yes      |             |

## Available Providers

| Provider                      | Model String                            | Price                     |
| ----------------------------- | --------------------------------------- | ------------------------- |
| amazon (neural)               | `audio/tts/amazon/neural`               | \$0.016 per 1,000 chars   |
| amazon (standard)             | `audio/tts/amazon/standard`             | \$0.004 per 1,000 chars   |
| deepgram (aura)               | `audio/tts/deepgram/aura`               | \$0.015 per 1,000 chars   |
| deepgram (aura-2)             | `audio/tts/deepgram/aura-2`             | \$0.03 per 1,000 chars    |
| elevenlabs                    | `audio/tts/elevenlabs`                  | \$0.3 per 1,000 chars     |
| google (casual)               | `audio/tts/google/casual`               | \$16 per 1,000,000 chars  |
| google (chirp3-hd)            | `audio/tts/google/chirp3-hd`            | \$30 per 1,000,000 chars  |
| google (chirp-hd)             | `audio/tts/google/chirp-hd`             | \$30 per 1,000,000 chars  |
| google (gemini-2.5-flash-tts) | `audio/tts/google/gemini-2.5-flash-tts` | \$0.006 per minute        |
| google (gemini-2.5-pro-tts)   | `audio/tts/google/gemini-2.5-pro-tts`   | \$0.012 per minute        |
| google (neural2)              | `audio/tts/google/neural2`              | \$16 per 1,000,000 chars  |
| google (news)                 | `audio/tts/google/news`                 | \$160 per 1,000,000 chars |
| google (polyglot)             | `audio/tts/google/polyglot`             | \$16 per 1,000,000 chars  |
| google (standard)             | `audio/tts/google/standard`             | \$4 per 1,000,000 chars   |
| google (studio)               | `audio/tts/google/studio`               | \$160 per 1,000,000 chars |
| google (wavenet)              | `audio/tts/google/wavenet`              | \$4 per 1,000,000 chars   |
| lovoai                        | `audio/tts/lovoai`                      | \$160 per 1,000,000 chars |
| microsoft (neural)            | `audio/tts/microsoft/neural`            | \$16 per 1,000,000 chars  |
| microsoft (neural-hd)         | `audio/tts/microsoft/neural-hd`         | \$30 per 1,000,000 chars  |
| openai (gpt-4o-mini-tts)      | `audio/tts/openai/gpt-4o-mini-tts`      | \$0.015 per minute        |
| openai (tts-1)                | `audio/tts/openai/tts-1`                | \$15 per 1,000,000 chars  |
| openai (tts-1-hd)             | `audio/tts/openai/tts-1-hd`             | \$30 per 1,000,000 chars  |

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
      "model": "audio/tts/amazon/neural",
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
      "model": "audio/tts/amazon/neural",
      "input": {"text": "The quick brown fox jumps over the lazy dog."}
    }'
  ```
</CodeGroup>


# Image AI Detection
Source: https://docs.edenai.co/v3/features/image/ai-detection

Determine whether an image was generated by AI or is a real photograph or artwork.

## Endpoint

`POST /v3/universal-ai` (sync)

Model string pattern: `image/ai_detection/{provider}[/{model}]`

## Input

| Field | Type        | Required | Description                                      |
| ----- | ----------- | -------- | ------------------------------------------------ |
| file  | file\_input | Yes      | Image file ID from /v3/upload or direct file URL |

## Output

| Field      | Type  | Required | Description |
| ---------- | ----- | -------- | ----------- |
| ai\_score  | float | Yes      |             |
| prediction | enum  | Yes      |             |

## Available Providers

| Provider  | Model String                   | Price               |
| --------- | ------------------------------ | ------------------- |
| winstonai | `image/ai_detection/winstonai` | \$0.021 per request |

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
      "model": "image/ai_detection/winstonai",
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
      "model": "image/ai_detection/winstonai",
      "input": {"file": "YOUR_FILE_UUID_OR_URL"}
    }'
  ```
</CodeGroup>


# Image Anonymization
Source: https://docs.edenai.co/v3/features/image/anonymization

Image Anonymization API, also known as image de-identification or image de-personalization, refers to the process of automatically removing personal or sensitive information from images. The main...

## Endpoint

`POST /v3/universal-ai` (sync)

Model string pattern: `image/anonymization/{provider}[/{model}]`

## Input

| Field | Type        | Required | Description                                      |
| ----- | ----------- | -------- | ------------------------------------------------ |
| file  | file\_input | Yes      | Image file ID from /v3/upload or direct file URL |

## Output

| Field                   | Type           | Required | Description |
| ----------------------- | -------------- | -------- | ----------- |
| image                   | string         | Yes      |             |
| image\_resource\_url    | string         | Yes      |             |
| **items**               | array\[object] | No       |             |
|     kind                | string         | Yes      |             |
|     confidence          | float          | Yes      |             |
|     **bounding\_boxes** | object         | Yes      |             |
|         x\_min          | float          | Yes      |             |
|         x\_max          | float          | Yes      |             |
|         y\_min          | float          | Yes      |             |
|         y\_max          | float          | Yes      |             |

## Available Providers

| Provider | Model String                 | Price                |
| -------- | ---------------------------- | -------------------- |
| api4ai   | `image/anonymization/api4ai` | \$25 per 1,000 files |

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
      "model": "image/anonymization/api4ai",
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
      "model": "image/anonymization/api4ai",
      "input": {"file": "YOUR_FILE_UUID_OR_URL"}
    }'
  ```
</CodeGroup>


# Image Background removal
Source: https://docs.edenai.co/v3/features/image/background-removal

Background removal is a digital image processing technique designed to seamlessly eliminate the backdrop of a photo, leaving behind only the main subject.

## Endpoint

`POST /v3/universal-ai` (sync)

Model string pattern: `image/background_removal/{provider}[/{model}]`

## Input

| Field | Type        | Required | Description                                      |
| ----- | ----------- | -------- | ------------------------------------------------ |
| file  | file\_input | Yes      | Image file ID from /v3/upload or direct file URL |

## Output

| Field                | Type   | Required | Description                 |
| -------------------- | ------ | -------- | --------------------------- |
| image\_b64           | string | Yes      | The image in base64 format. |
| image\_resource\_url | string | Yes      | The image url.              |

## Available Providers

| Provider    | Model String                           | Price                  |
| ----------- | -------------------------------------- | ---------------------- |
| api4ai      | `image/background_removal/api4ai`      | \$50 per 1,000 files   |
| clipdrop    | `image/background_removal/clipdrop`    | \$0.5 per request      |
| photoroom   | `image/background_removal/photoroom`   | \$20 per 1,000 files   |
| picsart     | `image/background_removal/picsart`     | \$0.04 per image       |
| sentisight  | `image/background_removal/sentisight`  | \$0.75 per 1,000 files |
| stabilityai | `image/background_removal/stabilityai` | \$0.02 per request     |

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
      "model": "image/background_removal/api4ai",
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
      "model": "image/background_removal/api4ai",
      "input": {"file": "YOUR_FILE_UUID_OR_URL"}
    }'
  ```
</CodeGroup>


# Deepfake Detection
Source: https://docs.edenai.co/v3/features/image/deepfake-detection



## Endpoint

`POST /v3/universal-ai` (sync)

Model string pattern: `image/deepfake_detection/{provider}[/{model}]`

## Input

| Field | Type        | Required | Description                                      |
| ----- | ----------- | -------- | ------------------------------------------------ |
| file  | file\_input | Yes      | Image file ID from /v3/upload or direct file URL |

## Output

| Field           | Type  | Required | Description |
| --------------- | ----- | -------- | ----------- |
| deepfake\_score | float | Yes      |             |
| prediction      | enum  | Yes      |             |

## Available Providers

| Provider    | Model String                           | Price             |
| ----------- | -------------------------------------- | ----------------- |
| sightengine | `image/deepfake_detection/sightengine` | \$0.002 per image |

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
      "model": "image/deepfake_detection/sightengine",
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
      "model": "image/deepfake_detection/sightengine",
      "input": {"file": "YOUR_FILE_UUID_OR_URL"}
    }'
  ```
</CodeGroup>


# Image Explicit Content
Source: https://docs.edenai.co/v3/features/image/explicit-content

Explicit Content Detection detects adult only content in images, that is generally inappropriate for people under the age of 18 and includes nudity, sexual activity, pornography, violence, gore...

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


# Image Face Comparison
Source: https://docs.edenai.co/v3/features/image/face-compare

Compare two faces and decide whether they are from the same person. The API expects 2 images, reference and query, where the former is the ground truth (e.g. user's official ID) and the latter is the...

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


# Image Face Detection
Source: https://docs.edenai.co/v3/features/image/face-detection

Face Detection is a computer technology being used in a variety of applications that identifies human faces in digital images with different attributes like landmarks, sentiments and physical attire...

## Endpoint

`POST /v3/universal-ai` (sync)

Model string pattern: `image/face_detection/{provider}[/{model}]`

## Input

| Field | Type        | Required | Description                                      |
| ----- | ----------- | -------- | ------------------------------------------------ |
| file  | file\_input | Yes      | Image file ID from /v3/upload or direct file URL |

## Output

| Field                               | Type           | Required | Description |
| ----------------------------------- | -------------- | -------- | ----------- |
| **items**                           | array\[object] | No       |             |
|     confidence                      | float          | Yes      |             |
|     **landmarks**                   | object         | Yes      |             |
|         left\_eye                   | array\[float]  | No       |             |
|         left\_eye\_top              | array\[float]  | No       |             |
|         left\_eye\_right            | array\[float]  | No       |             |
|         left\_eye\_bottom           | array\[float]  | No       |             |
|         left\_eye\_left             | array\[float]  | No       |             |
|         right\_eye                  | array\[float]  | No       |             |
|         right\_eye\_top             | array\[float]  | No       |             |
|         right\_eye\_right           | array\[float]  | No       |             |
|         right\_eye\_bottom          | array\[float]  | No       |             |
|         right\_eye\_left            | array\[float]  | No       |             |
|         left\_eyebrow\_left         | array\[float]  | No       |             |
|         left\_eyebrow\_right        | array\[float]  | No       |             |
|         left\_eyebrow\_top          | array\[float]  | No       |             |
|         right\_eyebrow\_left        | array\[float]  | No       |             |
|         right\_eyebrow\_right       | array\[float]  | No       |             |
|         left\_pupil                 | array\[float]  | No       |             |
|         right\_pupil                | array\[float]  | No       |             |
|         nose\_tip                   | array\[float]  | No       |             |
|         nose\_bottom\_right         | array\[float]  | No       |             |
|         nose\_bottom\_left          | array\[float]  | No       |             |
|         mouth\_left                 | array\[float]  | No       |             |
|         mouth\_right                | array\[float]  | No       |             |
|         right\_eyebrow\_top         | array\[float]  | No       |             |
|         midpoint\_between\_eyes     | array\[float]  | No       |             |
|         nose\_bottom\_center        | array\[float]  | No       |             |
|         nose\_left\_alar\_out\_tip  | array\[float]  | No       |             |
|         nose\_left\_alar\_top       | array\[float]  | No       |             |
|         nose\_right\_alar\_out\_tip | array\[float]  | No       |             |
|         nose\_right\_alar\_top      | array\[float]  | No       |             |
|         nose\_root\_left            | array\[float]  | No       |             |
|         nose\_root\_right           | array\[float]  | No       |             |
|         upper\_lip                  | array\[float]  | No       |             |
|         under\_lip                  | array\[float]  | No       |             |
|         under\_lip\_bottom          | array\[float]  | No       |             |
|         under\_lip\_top             | array\[float]  | No       |             |
|         upper\_lip\_bottom          | array\[float]  | No       |             |
|         upper\_lip\_top             | array\[float]  | No       |             |
|         mouth\_center               | array\[float]  | No       |             |
|         mouth\_top                  | array\[float]  | No       |             |
|         mouth\_bottom               | array\[float]  | No       |             |
|         left\_ear\_tragion          | array\[float]  | No       |             |
|         right\_ear\_tragion         | array\[float]  | No       |             |
|         forehead\_glabella          | array\[float]  | No       |             |
|         chin\_gnathion              | array\[float]  | No       |             |
|         chin\_left\_gonion          | array\[float]  | No       |             |
|         chin\_right\_gonion         | array\[float]  | No       |             |
|         upper\_jawline\_left        | array\[float]  | No       |             |
|         mid\_jawline\_left          | array\[float]  | No       |             |
|         mid\_jawline\_right         | array\[float]  | No       |             |
|         upper\_jawline\_right       | array\[float]  | No       |             |
|         left\_cheek\_center         | array\[float]  | No       |             |
|         right\_cheek\_center        | array\[float]  | No       |             |
|     **emotions**                    | object         | Yes      |             |
|         joy                         | int            | Yes      |             |
|         sorrow                      | int            | Yes      |             |
|         anger                       | int            | Yes      |             |
|         surprise                    | int            | Yes      |             |
|         disgust                     | int            | Yes      |             |
|         fear                        | int            | Yes      |             |
|         confusion                   | int            | Yes      |             |
|         calm                        | int            | Yes      |             |
|         unknown                     | int            | Yes      |             |
|         neutral                     | int            | Yes      |             |
|         contempt                    | int            | Yes      |             |
|     **poses**                       | object         | Yes      |             |
|         pitch                       | float          | Yes      |             |
|         roll                        | float          | Yes      |             |
|         yaw                         | float          | Yes      |             |
|     age                             | float          | Yes      |             |
|     gender                          | string         | Yes      |             |
|     **bounding\_box**               | object         | Yes      |             |
|         x\_min                      | float          | Yes      |             |
|         x\_max                      | float          | Yes      |             |
|         y\_min                      | float          | Yes      |             |
|         y\_max                      | float          | Yes      |             |
|     **hair**                        | object         | Yes      |             |
|         **hair\_color**             | array\[object] | No       |             |
|             color                   | string         | Yes      |             |
|             confidence              | float          | Yes      |             |
|         bald                        | float          | Yes      |             |
|         invisible                   | bool           | Yes      |             |
|     **facial\_hair**                | object         | Yes      |             |
|         moustache                   | float          | Yes      |             |
|         beard                       | float          | Yes      |             |
|         sideburns                   | float          | Yes      |             |
|     **quality**                     | object         | Yes      |             |
|         noise                       | float          | Yes      |             |
|         exposure                    | float          | Yes      |             |
|         blur                        | float          | Yes      |             |
|         brightness                  | float          | Yes      |             |
|         sharpness                   | float          | Yes      |             |
|     **makeup**                      | object         | Yes      |             |
|         eye\_make                   | bool           | Yes      |             |
|         lip\_make                   | bool           | Yes      |             |
|     **accessories**                 | object         | Yes      |             |
|         sunglasses                  | float          | Yes      |             |
|         reading\_glasses            | float          | Yes      |             |
|         swimming\_goggles           | float          | Yes      |             |
|         face\_mask                  | float          | Yes      |             |
|         eyeglasses                  | float          | Yes      |             |
|         headwear                    | float          | Yes      |             |
|     **occlusions**                  | object         | Yes      |             |
|         eye\_occluded               | bool           | Yes      |             |
|         forehead\_occluded          | bool           | Yes      |             |
|         mouth\_occluded             | bool           | Yes      |             |
|     **features**                    | object         | Yes      |             |
|         eyes\_open                  | float          | Yes      |             |
|         smile                       | float          | Yes      |             |
|         mouth\_open                 | float          | Yes      |             |

## Available Providers

| Provider | Model String                    | Price                  |
| -------- | ------------------------------- | ---------------------- |
| amazon   | `image/face_detection/amazon`   | \$1 per 1,000 files    |
| api4ai   | `image/face_detection/api4ai`   | \$0.75 per 1,000 files |
| clarifai | `image/face_detection/clarifai` | \$2 per 1,000 files    |
| google   | `image/face_detection/google`   | \$1.5 per 1,000 files  |

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
      "model": "image/face_detection/amazon",
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
      "model": "image/face_detection/amazon",
      "input": {"file": "YOUR_FILE_UUID_OR_URL"}
    }'
  ```
</CodeGroup>


# Image generation
Source: https://docs.edenai.co/v3/features/image/generation

Image Generation is an advanced feature that generates compelling images based on a given text prompt. It can easily produce high-quality and original images in a matter of seconds, without the need...

## Endpoint

`POST /v3/universal-ai` (sync)

Model string pattern: `image/generation/{provider}[/{model}]`

## Input

| Field       | Type   | Required | Description                          |
| ----------- | ------ | -------- | ------------------------------------ |
| text        | string | Yes      | Text prompt for image generation     |
| resolution  | string | Yes      | Image resolution (e.g., '1024x1024') |
| num\_images | int    | No       | Number of images to generate         |

## Output

| Field                | Type   | Required | Description |
| -------------------- | ------ | -------- | ----------- |
| image                | string | Yes      |             |
| image\_resource\_url | string | Yes      |             |

## Available Providers

| Provider                                    | Model String                                                 | Price                     |
| ------------------------------------------- | ------------------------------------------------------------ | ------------------------- |
| bytedance                                   | `image/generation/bytedance`                                 | \$0.03 per request        |
| bytedance (seedream-3-0-t2i-250415)         | `image/generation/bytedance/seedream-3-0-t2i-250415`         | \$0.03 per request        |
| bytedance (seedream-4-0-250828)             | `image/generation/bytedance/seedream-4-0-250828`             | \$0.03 per request        |
| bytedance (seedream-4-5-251128)             | `image/generation/bytedance/seedream-4-5-251128`             | \$0.03 per request        |
| leonardo (AlbedoBase XL)                    | `image/generation/leonardo/AlbedoBase XL`                    | \$0.014 per image         |
| leonardo                                    | `image/generation/leonardo`                                  | \$0.014 per image         |
| leonardo (Leonardo Anime XL)                | `image/generation/leonardo/Leonardo Anime XL`                | \$0.012 per image         |
| leonardo (Leonardo Diffusion XL)            | `image/generation/leonardo/Leonardo Diffusion XL`            | \$0.017 per image         |
| leonardo (Leonardo Kino XL)                 | `image/generation/leonardo/Leonardo Kino XL`                 | \$0.014 per image         |
| leonardo (Leonardo Lightning XL)            | `image/generation/leonardo/Leonardo Lightning XL`            | \$0.011 per image         |
| leonardo (Leonardo Phoenix)                 | `image/generation/leonardo/Leonardo Phoenix`                 | \$0.017 per image         |
| leonardo (Leonardo Vision XL)               | `image/generation/leonardo/Leonardo Vision XL`               | \$0.014 per image         |
| leonardo (SDXL 0.9)                         | `image/generation/leonardo/SDXL 0.9`                         | \$0.014 per image         |
| minimax                                     | `image/generation/minimax`                                   | \$0.0035 per image        |
| minimax (image-01)                          | `image/generation/minimax/image-01`                          | \$0.0035 per image        |
| openai (dall-e-2)                           | `image/generation/openai/dall-e-2`                           | \$0.016 per image         |
| openai (dall-e-3)                           | `image/generation/openai/dall-e-3`                           | \$0.08 per image          |
| openai                                      | `image/generation/openai`                                    | \$0.018 per image         |
| replicate (anime-style)                     | `image/generation/replicate/anime-style`                     | \$0.000225 per exec\_time |
| replicate (classic)                         | `image/generation/replicate/classic`                         | \$0.00115 per exec\_time  |
| replicate                                   | `image/generation/replicate`                                 | \$0.000225 per exec\_time |
| replicate (vintedois-diffusion)             | `image/generation/replicate/vintedois-diffusion`             | \$0.000225 per exec\_time |
| stabilityai                                 | `image/generation/stabilityai`                               | \$15 per 1,000 images     |
| stabilityai (stable-diffusion-xl-1024-v1-0) | `image/generation/stabilityai/stable-diffusion-xl-1024-v1-0` | \$15 per 1,000 images     |

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
      "model": "image/generation/bytedance",
      "input": {
          "text": "The quick brown fox jumps over the lazy dog.",
          "resolution": "1024x1024"
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
      "model": "image/generation/bytedance",
      "input": {"text": "The quick brown fox jumps over the lazy dog.", "resolution": "1024x1024"}
    }'
  ```
</CodeGroup>


# Image Logo Detection
Source: https://docs.edenai.co/v3/features/image/logo-detection

Logo Detection is a powerful technology that enables the automatic identification and recognition of popular logos within an image. It provides accurate and efficient detection of known (and less...

## Endpoint

`POST /v3/universal-ai` (sync)

Model string pattern: `image/logo_detection/{provider}[/{model}]`

## Input

| Field | Type        | Required | Description                                      |
| ----- | ----------- | -------- | ------------------------------------------------ |
| file  | file\_input | Yes      | Image file ID from /v3/upload or direct file URL |

## Output

| Field                  | Type           | Required | Description                                         |
| ---------------------- | -------------- | -------- | --------------------------------------------------- |
| **items**              | array\[object] | No       | List of the detected brands logo from the image.    |
|     **bounding\_poly** | object         | No       |                                                     |
|         **vertices**   | array\[object] | No       | Vertices of the logos in the image                  |
|             x          | float          | Yes      | The x-coordinate of the vertex.                     |
|             y          | float          | Yes      | The y-coordinate of the vertex.                     |
|     description        | string         | Yes      | Name of the logo                                    |
|     score              | float          | Yes      | Confidence score how sure it's this is a real logo. |

## Available Providers

| Provider             | Model String                              | Price                  |
| -------------------- | ----------------------------------------- | ---------------------- |
| api4ai               | `image/logo_detection/api4ai`             | \$0.25 per 1,000 files |
| api4ai (v1)          | `image/logo_detection/api4ai/v1`          | \$0.25 per 1,000 files |
| api4ai (v2)          | `image/logo_detection/api4ai/v2`          | \$2.5 per 1,000 files  |
| clarifai             | `image/logo_detection/clarifai`           | \$2 per 1,000 files    |
| google               | `image/logo_detection/google`             | \$1.5 per 1,000 files  |
| microsoft            | `image/logo_detection/microsoft`          | \$1 per 1,000 files    |
| openai               | `image/logo_detection/openai`             | \$24 per 1,000 files   |
| openai (gpt-4o)      | `image/logo_detection/openai/gpt-4o`      | \$24 per 1,000 files   |
| openai (gpt-4-turbo) | `image/logo_detection/openai/gpt-4-turbo` | \$48 per 1,000 files   |

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
      "model": "image/logo_detection/api4ai",
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
      "model": "image/logo_detection/api4ai",
      "input": {"file": "YOUR_FILE_UUID_OR_URL"}
    }'
  ```
</CodeGroup>


# Image Object Detection
Source: https://docs.edenai.co/v3/features/image/object-detection

Object Detection is a computer vision technique that allows users to identify and locate (with bounding boxes) objects in an image. The detected objects can be animals, people, electronics, vehicles...

## Endpoint

`POST /v3/universal-ai` (sync)

Model string pattern: `image/object_detection/{provider}[/{model}]`

## Input

| Field | Type        | Required | Description                                      |
| ----- | ----------- | -------- | ------------------------------------------------ |
| file  | file\_input | Yes      | Image file ID from /v3/upload or direct file URL |

## Output

| Field          | Type           | Required | Description |
| -------------- | -------------- | -------- | ----------- |
| **items**      | array\[object] | No       |             |
|     label      | string         | Yes      |             |
|     confidence | float          | Yes      |             |
|     x\_min     | float          | Yes      |             |
|     x\_max     | float          | Yes      |             |
|     y\_min     | float          | Yes      |             |
|     y\_max     | float          | Yes      |             |

## Available Providers

| Provider                           | Model String                                              | Price                  |
| ---------------------------------- | --------------------------------------------------------- | ---------------------- |
| amazon                             | `image/object_detection/amazon`                           | \$1 per 1,000 files    |
| api4ai                             | `image/object_detection/api4ai`                           | \$0.5 per 1,000 files  |
| clarifai                           | `image/object_detection/clarifai`                         | \$2 per 1,000 files    |
| clarifai (general-image-detection) | `image/object_detection/clarifai/general-image-detection` | \$2 per 1,000 files    |
| google                             | `image/object_detection/google`                           | \$2.25 per 1,000 files |
| microsoft                          | `image/object_detection/microsoft`                        | \$1 per 1,000 files    |
| sentisight                         | `image/object_detection/sentisight`                       | \$0.75 per 1,000 files |

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
      "model": "image/object_detection/amazon",
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
      "model": "image/object_detection/amazon",
      "input": {"file": "YOUR_FILE_UUID_OR_URL"}
    }'
  ```
</CodeGroup>


# AI Features Reference
Source: https://docs.edenai.co/v3/features/index

Complete reference for all Universal AI features available through Eden AI.

# AI Features Reference

Browse all AI features available through the Universal AI endpoint (`POST /v3/universal-ai`). Each feature page includes input/output schemas, available providers with pricing, and quick-start code examples.

## Text

<CardGroup>
  <Card title="Text AI Content Detection" icon="font" href="/v3/features/text/ai-detection">
    The AI Detection API is a tool designed to determine whether a given text was generated by an artificial intelligence...
  </Card>

  <Card title="Text Moderation" icon="font" href="/v3/features/text/moderation">
    Text moderation scans text for offensive, sexually explicit or suggestive content, it also checks if there is any...
  </Card>

  <Card title="Grammar Spell Check" icon="font" href="/v3/features/text/spell-check">
    Spell Check analyzes the inputted text by comparing it to a dictionary of correctly spelled words to identify and...
  </Card>

  <Card title="Topic Extraction" icon="font" href="/v3/features/text/topic-extraction">
    Topic analysis is a Natural Language Processing (NLP) technique that allows us to automatically extract meaning from...
  </Card>

  <Card title="Named Entity Recognition" icon="font" href="/v3/features/text/named-entity-recognition">
    Named Entity Recognition (also called entity identification or extraction) is an information extraction technique that...
  </Card>

  <Card title="Plagiarism Detection" icon="font" href="/v3/features/text/plagia-detection">
    The Plagiarism Detection API is a tool designed to scan a content string for plagiarism using a plagiarism detection...
  </Card>
</CardGroup>

## OCR

<CardGroup>
  <Card title="Text Detection (OCR)" icon="file-lines" href="/v3/features/ocr/ocr">
    Optical Character Recognition or Reader (OCR) is the electronic or mechanical conversion of images of typed,...
  </Card>

  <Card title="OCR Multipage" icon="file-lines" href="/v3/features/ocr/ocr-async">
    OCR or Optical Character Recognition is also referred to as text recognition or text extraction. It allows users to...
  </Card>

  <Card title="Table Extraction" icon="file-lines" href="/v3/features/ocr/ocr-tables-async">
    OCR Table (Optical Character Recognition for tabular documents)  allows users to analyze documents containing tables...
  </Card>

  <Card title="Identity Parser" icon="file-lines" href="/v3/features/ocr/identity-parser">
    ID Document parsing technology allows users to automatically extract information from an ID Document such as passport,...
  </Card>

  <Card title="Financial Parser" icon="file-lines" href="/v3/features/ocr/financial-parser">
    Financial Parser API is a powerful and versatile tool designed to streamline your financial data extraction process....
  </Card>

  <Card title="Resume Parser" icon="file-lines" href="/v3/features/ocr/resume-parser">
    Resume Parser enables users to extract various information from resumes (curriculum vitae, CV) that could be in a...
  </Card>
</CardGroup>

## Image

<CardGroup>
  <Card title="Image Background removal" icon="image" href="/v3/features/image/background-removal">
    Background removal is a digital image processing technique designed to seamlessly eliminate the backdrop of a photo,...
  </Card>

  <Card title="Image generation" icon="image" href="/v3/features/image/generation">
    Image Generation is an advanced feature that generates compelling images based on a given text prompt. It can easily...
  </Card>

  <Card title="Image AI Detection" icon="image" href="/v3/features/image/ai-detection">
    Determine whether an image was generated by AI or is a real photograph or artwork.
  </Card>

  <Card title="Image Object Detection" icon="image" href="/v3/features/image/object-detection">
    Object Detection is a computer vision technique that allows users to identify and locate (with bounding boxes) objects...
  </Card>

  <Card title="Image Face Detection" icon="image" href="/v3/features/image/face-detection">
    Face Detection is a computer technology being used in a variety of applications that identifies human faces in digital...
  </Card>

  <Card title="Image Explicit Content" icon="image" href="/v3/features/image/explicit-content">
    Explicit Content Detection detects adult only content in images, that is generally inappropriate for people under the...
  </Card>

  <Card title="Image Anonymization" icon="image" href="/v3/features/image/anonymization">
    Image Anonymization API, also known as image de-identification or image de-personalization, refers to the process of...
  </Card>

  <Card title="Deepfake Detection" icon="image" href="/v3/features/image/deepfake-detection" />

  <Card title="Image Face Comparison" icon="image" href="/v3/features/image/face-compare">
    Compare two faces and decide whether they are from the same person. The API expects 2 images, reference and query,...
  </Card>

  <Card title="Image Logo Detection" icon="image" href="/v3/features/image/logo-detection">
    Logo Detection is a powerful technology that enables the automatic identification and recognition of popular logos...
  </Card>
</CardGroup>

## Document Translation

<CardGroup>
  <Card title="Document Translation" icon="language" href="/v3/features/translation/document-translation">
    Document Translation API translates whole documents in supported languages and various file formats (like pdf or doc)...
  </Card>
</CardGroup>

## Audio

<CardGroup>
  <Card title="Text to Speech" icon="volume-high" href="/v3/features/audio/tts">
    Text-to-speech (TTS) is a technology that converts written text into spoken audio, enabling computers and digital...
  </Card>

  <Card title="Speech To Text" icon="volume-high" href="/v3/features/audio/speech-to-text-async">
    Speech Recognition (or speech to text or voice to text) can recognize and transcribe spoken words (voice),  that will...
  </Card>
</CardGroup>


# Financial Parser
Source: https://docs.edenai.co/v3/features/ocr/financial-parser

Financial Parser API is a powerful and versatile tool designed to streamline your financial data extraction process. This cutting-edge API combines Optical Character Recognition (OCR) technology with...

## Endpoint

`POST /v3/universal-ai` (sync)

Model string pattern: `ocr/financial_parser/{provider}[/{model}]`

## Input

| Field          | Type        | Required | Description                                                                                                         |
| -------------- | ----------- | -------- | ------------------------------------------------------------------------------------------------------------------- |
| file           | file\_input | Yes      | File ID from /v3/upload or direct file URL                                                                          |
| language       | string      | Yes      | Document language code                                                                                              |
| document\_type | enum        | No       | Specify the type of your document. Can be set to 'auto-detect' for automatic detection if the provider supports it. |

## Output

| Field                                    | Type           | Required | Description                                                                                                       |
| ---------------------------------------- | -------------- | -------- | ----------------------------------------------------------------------------------------------------------------- |
| **extracted\_data**                      | array\[object] | No       | List of parsed financial data objects (per page).                                                                 |
|     **customer\_information**            | object         | Yes      |                                                                                                                   |
|         name                             | string         | No       | The name of the invoiced customer.                                                                                |
|         id\_reference                    | string         | No       | Unique reference ID for the customer.                                                                             |
|         mailling\_address                | string         | No       | The mailing address of the customer.                                                                              |
|         billing\_address                 | string         | No       | The explicit billing address for the customer.                                                                    |
|         shipping\_address                | string         | No       | The shipping address for the customer.                                                                            |
|         service\_address                 | string         | No       | The service address associated with the customer.                                                                 |
|         remittance\_address              | string         | No       | The address to which payments should be remitted.                                                                 |
|         email                            | string         | No       | The email address of the customer.                                                                                |
|         phone                            | string         | No       | The phone number associated with the customer.                                                                    |
|         vat\_number                      | string         | No       | VAT (Value Added Tax) number of the customer.                                                                     |
|         abn\_number                      | string         | No       | ABN (Australian Business Number) of the customer.                                                                 |
|         gst\_number                      | string         | No       | GST (Goods and Services Tax) number of the customer.                                                              |
|         pan\_number                      | string         | No       | PAN (Permanent Account Number) of the customer.                                                                   |
|         business\_number                 | string         | No       | Business registration number of the customer.                                                                     |
|         siret\_number                    | string         | No       | SIRET (Système d'Identification du Répertoire des Entreprises et de leurs Établissements) number of the customer. |
|         siren\_number                    | string         | No       | SIREN (Système d'Identification du Répertoire des Entreprises) number of the customer.                            |
|         customer\_number                 | string         | No       | Customer identification number.                                                                                   |
|         coc\_number                      | string         | No       | Chamber of Commerce registration number.                                                                          |
|         fiscal\_number                   | string         | No       | Fiscal identification number of the customer.                                                                     |
|         registration\_number             | string         | No       | Official registration number of the customer.                                                                     |
|         tax\_id                          | string         | No       | Tax identification number of the customer.                                                                        |
|         website                          | string         | No       | The website associated with the customer.                                                                         |
|         remit\_to\_name                  | string         | No       | The name associated with the customer's remittance address.                                                       |
|         city                             | string         | No       | The city associated with the customer's address.                                                                  |
|         country                          | string         | No       | The country associated with the customer's address.                                                               |
|         house\_number                    | string         | No       | The house number associated with the customer's address.                                                          |
|         province                         | string         | No       | The province associated with the customer's address.                                                              |
|         street\_name                     | string         | No       | The street name associated with the customer's address.                                                           |
|         zip\_code                        | string         | No       | The ZIP code associated with the customer's address.                                                              |
|         municipality                     | string         | No       | The municipality associated with the customer's address.                                                          |
|     **merchant\_information**            | object         | Yes      |                                                                                                                   |
|         name                             | string         | No       | Name of the merchant.                                                                                             |
|         address                          | string         | No       | Address of the merchant.                                                                                          |
|         phone                            | string         | No       | Phone number of the merchant.                                                                                     |
|         tax\_id                          | string         | No       | Tax identification number of the merchant.                                                                        |
|         id\_reference                    | string         | No       | Unique reference ID for the merchant.                                                                             |
|         vat\_number                      | string         | No       | VAT (Value Added Tax) number of the merchant.                                                                     |
|         abn\_number                      | string         | No       | ABN (Australian Business Number) of the merchant.                                                                 |
|         gst\_number                      | string         | No       | GST (Goods and Services Tax) number of the merchant.                                                              |
|         business\_number                 | string         | No       | Business registration number of the merchant.                                                                     |
|         siret\_number                    | string         | No       | SIRET (Système d'Identification du Répertoire des Entreprises et de leurs Établissements) number of the merchant. |
|         siren\_number                    | string         | No       | SIREN (Système d'Identification du Répertoire des Entreprises) number of the merchant.                            |
|         pan\_number                      | string         | No       | PAN (Permanent Account Number) of the merchant.                                                                   |
|         coc\_number                      | string         | No       | Chamber of Commerce registration number of the merchant.                                                          |
|         fiscal\_number                   | string         | No       | Fiscal identification number of the merchant.                                                                     |
|         email                            | string         | No       | Email address of the merchant.                                                                                    |
|         fax                              | string         | No       | Fax number of the merchant.                                                                                       |
|         website                          | string         | No       | Website of the merchant.                                                                                          |
|         registration                     | string         | No       | Official registration information of the merchant.                                                                |
|         city                             | string         | No       | City associated with the merchant's address.                                                                      |
|         country                          | string         | No       | Country associated with the merchant's address.                                                                   |
|         house\_number                    | string         | No       | House number associated with the merchant's address.                                                              |
|         province                         | string         | No       | Province associated with the merchant's address.                                                                  |
|         street\_name                     | string         | No       | Street name associated with the merchant's address.                                                               |
|         zip\_code                        | string         | No       | ZIP code associated with the merchant's address.                                                                  |
|         country\_code                    | string         | No       | Country code associated with the merchant's location.                                                             |
|     **payment\_information**             | object         | Yes      |                                                                                                                   |
|         amount\_due                      | float          | No       | Amount due for payment.                                                                                           |
|         amount\_tip                      | float          | No       | Tip amount in a financial transaction.                                                                            |
|         amount\_shipping                 | float          | No       | Shipping cost in a financial transaction.                                                                         |
|         amount\_change                   | float          | No       | Change amount in a financial transaction.                                                                         |
|         amount\_paid                     | float          | No       | Amount already paid in a financial transaction.                                                                   |
|         total                            | float          | No       | Total amount in the invoice.                                                                                      |
|         subtotal                         | float          | No       | Subtotal amount in a financial transaction.                                                                       |
|         total\_tax                       | float          | No       | Total tax amount in a financial transaction.                                                                      |
|         tax\_rate                        | float          | No       | Tax rate applied in a financial transaction.                                                                      |
|         discount                         | float          | No       | Discount amount applied in a financial transaction.                                                               |
|         gratuity                         | float          | No       | Gratuity amount in a financial transaction.                                                                       |
|         service\_charge                  | float          | No       | Service charge in a financial transaction.                                                                        |
|         previous\_unpaid\_balance        | float          | No       | Previous unpaid balance in a financial transaction.                                                               |
|         prior\_balance                   | float          | No       | Prior balance before the current financial transaction.                                                           |
|         payment\_terms                   | string         | No       | Terms and conditions for payment.                                                                                 |
|         payment\_method                  | string         | No       | Payment method used in the financial transaction.                                                                 |
|         payment\_card\_number            | string         | No       | Card number used in the payment.                                                                                  |
|         payment\_auth\_code              | string         | No       | Authorization code for the payment.                                                                               |
|         shipping\_handling\_charge       | float          | No       | Charge for shipping and handling in a financial transaction.                                                      |
|         transaction\_number              | string         | No       | Unique identifier for the financial transaction.                                                                  |
|         transaction\_reference           | string         | No       | Reference number for the financial transaction.                                                                   |
|     **financial\_document\_information** | object         | Yes      |                                                                                                                   |
|         invoice\_receipt\_id             | string         | No       | Identifier for the invoice.                                                                                       |
|         purchase\_order                  | string         | No       | Purchase order related to the document.                                                                           |
|         invoice\_date                    | string         | No       | Date of the invoice.                                                                                              |
|         time                             | string         | No       | Time associated with the document.                                                                                |
|         invoice\_due\_date               | string         | No       | Due date for the invoice.                                                                                         |
|         service\_start\_date             | string         | No       | Start date of the service associated with the document.                                                           |
|         service\_end\_date               | string         | No       | End date of the service associated with the document.                                                             |
|         reference                        | string         | No       | Reference number associated with the document.                                                                    |
|         biller\_code                     | string         | No       | Biller code associated with the document.                                                                         |
|         order\_date                      | string         | No       | Date of the order associated with the document.                                                                   |
|         tracking\_number                 | string         | No       | Tracking number associated with the document.                                                                     |
|         **barcodes**                     | array\[object] | No       | List of barcodes associated with the document.                                                                    |
|             value                        | string         | Yes      |                                                                                                                   |
|             type                         | string         | Yes      |                                                                                                                   |
|     **local**                            | object         | Yes      |                                                                                                                   |
|         currency                         | string         | No       | Currency used in financial transactions.                                                                          |
|         currency\_code                   | string         | No       | Currency code (e.g., USD, EUR).                                                                                   |
|         currency\_exchange\_rate         | string         | No       | Exchange rate for the specified currency.                                                                         |
|         country                          | string         | No       | Country associated with the local financial information.                                                          |
|         language                         | string         | No       | Language used in financial transactions.                                                                          |
|     **bank**                             | object         | Yes      |                                                                                                                   |
|         iban                             | string         | No       | International Bank Account Number.                                                                                |
|         swift                            | string         | No       | Society for Worldwide Interbank Financial Telecommunication code.                                                 |
|         bsb                              | string         | No       | Bank State Branch code (Australia).                                                                               |
|         sort\_code                       | string         | No       | Sort code for UK banks.                                                                                           |
|         account\_number                  | string         | No       | Bank account number.                                                                                              |
|         routing\_number                  | string         | No       | Routing number for banks in the United States.                                                                    |
|         bic                              | string         | No       | Bank Identifier Code.                                                                                             |
|     **item\_lines**                      | array\[object] | No       | List of line items associated with the document.                                                                  |
|         tax                              | float          | No       | Tax amount for the line item.                                                                                     |
|         amount\_line                     | float          | No       | Total amount for the line item.                                                                                   |
|         description                      | string         | No       | Description of the line item.                                                                                     |
|         quantity                         | float          | No       | Quantity of units for the line item.                                                                              |
|         unit\_price                      | float          | No       | Unit price for each unit in the line item.                                                                        |
|         unit\_type                       | string         | No       | Type of unit (e.g., hours, items).                                                                                |
|         date                             | string         | No       | Date associated with the line item.                                                                               |
|         product\_code                    | string         | No       | Product code or identifier for the line item.                                                                     |
|         purchase\_order                  | string         | No       | Purchase order related to the line item.                                                                          |
|         tax\_rate                        | float          | No       | Tax rate applied to the line item.                                                                                |
|         base\_total                      | float          | No       | Base total amount before any discounts or taxes.                                                                  |
|         sub\_total                       | float          | No       | Subtotal amount for the line item.                                                                                |
|         discount\_amount                 | float          | No       | Amount of discount applied to the line item.                                                                      |
|         discount\_rate                   | float          | No       | Rate of discount applied to the line item.                                                                        |
|         discount\_code                   | string         | No       | Code associated with any discount applied to the line item.                                                       |
|         order\_number                    | string         | No       | Order number associated with the line item.                                                                       |
|         title                            | string         | No       | Title or name of the line item.                                                                                   |
|     **document\_metadata**               | object         | Yes      |                                                                                                                   |
|         document\_index                  | int            | No       | Index of the detected document.                                                                                   |
|         document\_page\_number           | int            | No       | Page number within the document.                                                                                  |
|         document\_type                   | string         | No       | Type or category of the document.                                                                                 |

## Available Providers

| Provider        | Model String                         | Price           |
| --------------- | ------------------------------------ | --------------- |
| affinda         | `ocr/financial_parser/affinda`       | \$0.07 per page |
| amazon          | `ocr/financial_parser/amazon`        | \$0.01 per page |
| base64          | `ocr/financial_parser/base64`        | \$0.25 per page |
| eagledoc        | `ocr/financial_parser/eagledoc`      | \$0.03 per page |
| extracta        | `ocr/financial_parser/extracta`      | \$0.1 per page  |
| google          | `ocr/financial_parser/google`        | \$0.01 per page |
| klippa          | `ocr/financial_parser/klippa`        | \$0.1 per file  |
| microsoft       | `ocr/financial_parser/microsoft`     | \$0.01 per page |
| mindee          | `ocr/financial_parser/mindee`        | \$0.1 per page  |
| openai          | `ocr/financial_parser/openai`        | \$0.04 per page |
| openai (gpt-4o) | `ocr/financial_parser/openai/gpt-4o` | \$0.04 per page |
| tabscanner      | `ocr/financial_parser/tabscanner`    | \$0.08 per page |
| veryfi          | `ocr/financial_parser/veryfi`        | \$0.16 per file |

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
      "model": "ocr/financial_parser/affinda",
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
      "model": "ocr/financial_parser/affinda",
      "input": {"file": "YOUR_FILE_UUID_OR_URL", "language": "en"}
    }'
  ```
</CodeGroup>


# Identity Parser
Source: https://docs.edenai.co/v3/features/ocr/identity-parser

ID Document parsing technology allows users to automatically extract information from an ID Document such as passport, ID card, driving license and more. This API is ideal for developers looking to...

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


# Text Detection (OCR)
Source: https://docs.edenai.co/v3/features/ocr/ocr

Optical Character Recognition or Reader (OCR) is the electronic or mechanical conversion of images of typed, handwritten or printed text into machine-encoded text. The image can be a scanned document...

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


# OCR Multipage
Source: https://docs.edenai.co/v3/features/ocr/ocr-async

OCR or Optical Character Recognition is also referred to as text recognition or text extraction. It allows users to extract text data from PDFs with multiple pages.

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


# Table Extraction
Source: https://docs.edenai.co/v3/features/ocr/ocr-tables-async

OCR Table (Optical Character Recognition for tabular documents)  allows users to analyze documents containing tables and returns a structured representation of the detected tables in the form of a...

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


# Resume Parser
Source: https://docs.edenai.co/v3/features/ocr/resume-parser

Resume Parser enables users to extract various information from resumes (curriculum vitae, CV) that could be in a variety of formats and returns structured data (name, job list, education, skills) to...

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


# Text AI Content Detection
Source: https://docs.edenai.co/v3/features/text/ai-detection

The AI Detection API is a tool designed to determine whether a given text was generated by an artificial intelligence chatbot, or a Language Model (LLM).

## Endpoint

`POST /v3/universal-ai` (sync)

Model string pattern: `text/ai_detection/{provider}[/{model}]`

## Input

| Field | Type   | Required | Description                      |
| ----- | ------ | -------- | -------------------------------- |
| text  | string | Yes      | Text to analyze for AI detection |

## Output

| Field                 | Type           | Required | Description |
| --------------------- | -------------- | -------- | ----------- |
| ai\_score             | float          | Yes      |             |
| **items**             | array\[object] | No       |             |
|     text              | string         | Yes      |             |
|     prediction        | string         | Yes      |             |
|     ai\_score         | float          | Yes      |             |
|     ai\_score\_detail | float          | Yes      |             |

## Available Providers

| Provider  | Model String                  | Price                    |
| --------- | ----------------------------- | ------------------------ |
| sapling   | `text/ai_detection/sapling`   | \$5 per 1,000,000 chars  |
| winstonai | `text/ai_detection/winstonai` | \$14 per 1,000,000 chars |

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
      "model": "text/ai_detection/sapling",
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
      "model": "text/ai_detection/sapling",
      "input": {"text": "The quick brown fox jumps over the lazy dog."}
    }'
  ```
</CodeGroup>


# Text Moderation
Source: https://docs.edenai.co/v3/features/text/moderation

Text moderation scans text for offensive, sexually explicit or suggestive content, it also checks if there is any content of self-harm, violence, racist or hate speech.

## Endpoint

`POST /v3/universal-ai` (sync)

Model string pattern: `text/moderation/{provider}[/{model}]`

## Input

| Field    | Type   | Required | Description             |
| -------- | ------ | -------- | ----------------------- |
| text     | string | Yes      | Text to moderate        |
| language | string | No       | ISO 639-1 language code |

## Output

| Field                   | Type           | Required | Description |
| ----------------------- | -------------- | -------- | ----------- |
| nsfw\_likelihood        | int            | Yes      |             |
| **items**               | array\[object] | No       |             |
|     label               | string         | Yes      |             |
|     likelihood          | int            | Yes      |             |
|     category            | enum           | Yes      |             |
|     subcategory         | enum           | Yes      |             |
|     likelihood\_score   | float          | Yes      |             |
| nsfw\_likelihood\_score | float          | Yes      |             |

## Available Providers

| Provider                        | Model String                                    | Price                   |
| ------------------------------- | ----------------------------------------------- | ----------------------- |
| google                          | `text/moderation/google`                        | \$5 per 1,000,000 chars |
| microsoft                       | `text/moderation/microsoft`                     | \$1 per 1,000 requests  |
| openai                          | `text/moderation/openai`                        | Free                    |
| openai (text-moderation-007)    | `text/moderation/openai/text-moderation-007`    | Free                    |
| openai (text-moderation-latest) | `text/moderation/openai/text-moderation-latest` | Free                    |
| openai (text-moderation-stable) | `text/moderation/openai/text-moderation-stable` | Free                    |

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
      "model": "text/moderation/google",
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
      "model": "text/moderation/google",
      "input": {"text": "The quick brown fox jumps over the lazy dog.", "language": "en"}
    }'
  ```
</CodeGroup>


# Named Entity Recognition
Source: https://docs.edenai.co/v3/features/text/named-entity-recognition

Named Entity Recognition (also called entity identification or extraction) is an information extraction technique that automatically identifies named entities in a text and classifies them into...

## Endpoint

`POST /v3/universal-ai` (sync)

Model string pattern: `text/named_entity_recognition/{provider}[/{model}]`

## Input

| Field    | Type   | Required | Description                        |
| -------- | ------ | -------- | ---------------------------------- |
| text     | string | Yes      | Text to analyze for named entities |
| language | string | No       | ISO 639-1 language code            |

## Output

| Field          | Type           | Required | Description |
| -------------- | -------------- | -------- | ----------- |
| **items**      | array\[object] | No       |             |
|     entity     | string         | Yes      |             |
|     category   | string         | Yes      |             |
|     importance | float          | Yes      |             |

## Available Providers

| Provider        | Model String                                  | Price                     |
| --------------- | --------------------------------------------- | ------------------------- |
| amazon          | `text/named_entity_recognition/amazon`        | \$1 per 1,000,000 chars   |
| microsoft       | `text/named_entity_recognition/microsoft`     | \$1 per 1,000,000 chars   |
| openai          | `text/named_entity_recognition/openai`        | \$10 per 1,000,000 tokens |
| openai (gpt-4o) | `text/named_entity_recognition/openai/gpt-4o` | \$10 per 1,000,000 tokens |
| tenstorrent     | `text/named_entity_recognition/tenstorrent`   | \$1 per 1,000,000 chars   |

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
      "model": "text/named_entity_recognition/amazon",
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
      "model": "text/named_entity_recognition/amazon",
      "input": {"text": "The quick brown fox jumps over the lazy dog.", "language": "en"}
    }'
  ```
</CodeGroup>


# Plagiarism Detection
Source: https://docs.edenai.co/v3/features/text/plagia-detection

The Plagiarism Detection API is a tool designed to scan a content string for plagiarism using a plagiarism detection module

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


# Grammar Spell Check
Source: https://docs.edenai.co/v3/features/text/spell-check

Spell Check analyzes the inputted text by comparing it to a dictionary of correctly spelled words to identify and highlight any spelling errors or grammatical mistakes.

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


# Topic Extraction
Source: https://docs.edenai.co/v3/features/text/topic-extraction

Topic analysis is a Natural Language Processing (NLP) technique that allows us to automatically extract meaning from text by identifying recurrent themes or topics.

## Endpoint

`POST /v3/universal-ai` (sync)

Model string pattern: `text/topic_extraction/{provider}[/{model}]`

## Input

| Field    | Type   | Required | Description                |
| -------- | ------ | -------- | -------------------------- |
| text     | string | Yes      | Text to analyze for topics |
| language | string | No       | ISO 639-1 language code    |

## Output

| Field          | Type           | Required | Description |
| -------------- | -------------- | -------- | ----------- |
| **items**      | array\[object] | No       |             |
|     category   | string         | Yes      |             |
|     importance | float          | Yes      |             |

## Available Providers

| Provider        | Model String                          | Price                     |
| --------------- | ------------------------------------- | ------------------------- |
| google          | `text/topic_extraction/google`        | \$0.6 per 1,000,000 chars |
| openai          | `text/topic_extraction/openai`        | \$10 per 1,000,000 tokens |
| openai (gpt-4o) | `text/topic_extraction/openai/gpt-4o` | \$10 per 1,000,000 tokens |
| tenstorrent     | `text/topic_extraction/tenstorrent`   | \$2 per 1,000,000 chars   |

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
      "model": "text/topic_extraction/google",
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
      "model": "text/topic_extraction/google",
      "input": {"text": "The quick brown fox jumps over the lazy dog.", "language": "en"}
    }'
  ```
</CodeGroup>


# Document Translation
Source: https://docs.edenai.co/v3/features/translation/document-translation

Document Translation API translates whole documents in supported languages and various file formats (like pdf or doc) while keeping their structure intact.

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


# Entreprise offer
Source: https://docs.edenai.co/v3/get-started/entreprise_offer



## “AI Gateway — Business”

For teams shipping AI to production who need **control, governance, and hands-on help**—without multiplying integrations.

**Best for:** product teams, scale-ups, and enterprises running multiple AI use cases.

| Feature                                                   | AI Gateway | AI Gateway — Business |
| --------------------------------------------------------- | :--------: | :-------------------: |
| Access to all supported AI models/providers               |      ✅     |           ✅           |
| Unified API (one integration for multiple providers)      |      ✅     |           ✅           |
| Unified billing                                           |      ✅     |           ✅           |
| Usage monitoring (requests, latency, errors)              |      ✅     |           ✅           |
| Basic analytics (volume by model/provider)                |      ✅     |           ✅           |
| Team workspace (multiple projects)                        |      ➖     |           ✅           |
| Roles & permissions (RBAC)                                |      ➖     |           ✅           |
| Spend controls (quotas, budgets, alerts)                  |      ➖     |           ✅           |
| Advanced observability (logs export, traces, SLA metrics) |      ➖     |           ✅           |
| Priority support                                          |      ➖     |           ✅           |
| Request custom models/providers                           |      ➖     |           ✅           |
| Professional Services (AI engineer)                       |      ➖     |     ✅ (on-demand)     |

### Everything in AI Gateway, plus:

#### 1) Team & access management

* **Multi-project workspace** for clean separation across products/environments
* **Roles & permissions** to control who can create keys, change routing, and view costs
* Optional **environment setup** (dev / staging / prod) with dedicated limits

#### 2) Cost control & governance

* **Budgets, quotas, and spend alerts** per project/team
* Usage breakdown by **model / provider / endpoint**
* Policy options like **allow/deny lists** for models or providers (where supported)

#### 3) Advanced monitoring

* Deeper visibility into **latency, error rates, fallbacks, and provider performance**
* Exportable logs/metrics for your internal tools (where supported)
* Health and performance reporting for production operations

#### 4) Priority support

* Faster response times and a direct support channel
* Help with debugging provider issues, routing decisions, and best practices

#### 5) Request custom models/providers

* Add new models/providers on demand (subject to feasibility/availability)
* Guidance on which model fits which task (quality vs cost vs latency)

#### 6) Professional Services (on-demand AI engineer)

When you need more than an API, our Professional Services gives you direct access to an experienced Eden AI engineer (or a small delivery squad) to **design, build, and productionize** your AI capabilities—fast.

**What you get**

* **Dedicated senior AI engineer** as your technical point of contact
* **Delivery plan + clear milestones** (what’s shipped each week, what success looks like)
* **Hands-on implementation** in your stack (or a reference implementation you can adapt)
* **Production hardening**: monitoring, safety controls, reliability, and cost governance
* **Knowledge transfer** so your team can maintain and iterate confidently

We work with your team to **understand your challenges and deliver tailored AI solutions** that fit directly into your product or operations.

**Examples:**

* Automating contract review for legal teams
* Routing customer requests to the right support teams
* Extracting key data from invoices and documents
* Internal assistants that answer employee questions
* Prioritizing leads, cases, or applications

**You get:** a working solution, clear handover, and long-term autonomy.

***

### Making the right choices

We help you **choose the best AI options** based on your real needs — reducing risk, cost, and wasted experimentation.

***

### Making it reliable

We ensure your AI solutions are **stable, scalable, and predictable**, so they work in real operations, not just demos.

***

### Support for sensitive environments (optional)

We help you navigate data, legal, and compliance questions when needed.

***

**Talk to a founder**


# Faq
Source: https://docs.edenai.co/v3/get-started/faq



# Frequently Asked Questions

Common questions about Eden AI V3 API.

## General

### What is Eden AI V3?

Eden AI V3 is a unified AI API platform that provides:

* **Universal AI Endpoint** - Single endpoint for all non-LLM features (text, OCR, image, translation)
* **OpenAI-Compatible LLM** - Drop-in replacement for OpenAI's chat completions API
* **Multi-Provider Support** - Access 50+ AI providers through one interface
* **Persistent File Storage** - Upload files once, use in multiple requests

### Which endpoint should I use?

Choose based on your use case:

**Use `/v3/llm/chat/completions` for:**

* Conversational AI and chatbots
* Text generation and completion
* Vision/multimodal AI (analyzing images with LLMs)
* Tool/function calling
* Any use case requiring OpenAI-compatible format

**Use `/v3/universal-ai` for:**

* Text analysis (sentiment, moderation, AI detection)
* OCR and document parsing
* Image generation and analysis
* Text embeddings
* Translation

See [Getting Started](./introduction) for detailed endpoint comparison.

### How does the model string format work?

V3 uses a **model string** to specify what feature and provider to use:

**Universal AI format:**

```
feature/subfeature/provider[/model]
```

Examples:

* `text/moderation/openai`
* `ocr/financial_parser/google`
* `image/generation/openai/dall-e-3`

**LLM format (simplified):**

```
provider/model
```

Examples:

* `openai/gpt-4`
* `anthropic/claude-sonnet-4-5`
* `google/gemini-2.5-flash`

See [Universal AI Getting Started](../how-to/universal-ai/getting-started) and [Chat Completions](../how-to/llm/chat-completions) for details.

## Authentication & Access

### How do I get an API key?

1. Sign up at [app.edenai.run](https://app.edenai.run/)
2. Navigate to your dashboard
3. Generate an API token under "API Keys"
4. Use it in the `Authorization` header: `Bearer YOUR_API_KEY`

See [Authentication Guide](../how-to/authentication/bearer-token-auth) for details.

### Can I use my own provider API keys?

Yes! You can bypass Eden AI billing by providing your own provider API keys. This is useful for:

* Using existing provider credits
* Testing specific provider features
* Cost optimization

Contact support or check your dashboard for instructions on adding custom provider keys.

### What are the rate limits?

Rate limits vary by:

* Your account tier
* Provider being used
* Specific feature

Default limits are displayed in your dashboard. Rate limit headers are included in API responses:

* `X-RateLimit-Limit` - Total requests allowed
* `X-RateLimit-Remaining` - Requests remaining
* `X-RateLimit-Reset` - Time when limit resets

When rate limited, you'll receive a `429 Too Many Requests` response.

### How much does it cost?

Pricing is **pay-as-you-go** based on:

* Provider used
* Feature/model called
* Volume of data processed

Every API response includes a `cost` field showing the charge in USD for that request:

```json theme={null}
{
  "status": "success",
  "cost": 0.0015,
  "output": { ... }
}
```

See [Monitor Usage and Costs](../how-to/cost-management/monitor-usage) for tracking and optimization.

## File Handling

### What file input methods are supported?

V3 supports three methods:

**1. File Upload (recommended for reuse):**

```python theme={null}
import requests

# Upload once
response = requests.post(
    "https://api.edenai.run/v3/upload",
    headers={"Authorization": "Bearer YOUR_API_KEY"},
    files={"file": open("document.pdf", "rb")}
)
file_id = response.json()["file_id"]

# Use multiple times
payload = {"model": "ocr/financial_parser/google", "input": {"file": file_id}}
```

**2. File URL:**

```python theme={null}
payload = {
    "model": "ocr/financial_parser/google",
    "input": {"file": "https://example.com/document.pdf"}
}
```

**3. Base64 (inline):**

```python theme={null}
payload = {
    "model": "text/moderation/openai",
    "input": {"text": "Sample text"}
}
```

See [Upload Files](../how-to/upload/upload-files) for detailed guide.

### How long are uploaded files stored?

Files uploaded to `/v3/upload` are stored for **7 days** by default. After expiration:

* Files are automatically deleted
* File IDs become invalid
* You'll need to re-upload

The `expires_at` timestamp is included in upload responses:

```json theme={null}
{
  "file_id": "550e8400-e29b-41d4-a716-446655440000",
  "filename": "document.pdf",
  "bytes": 123456,
  "created_at": "2025-12-26T10:00:00Z",
  "expires_at": "2026-01-02T10:00:00Z"
}
```

### What are the file size limits?

Limits vary by feature and provider:

| Feature Type         | Typical Limit | Notes                               |
| -------------------- | ------------- | ----------------------------------- |
| OCR                  | 100 MB        | Some providers support larger files |
| Image Analysis       | 20 MB         | JPEG, PNG, WebP, GIF                |
| LLM Vision           | 20 MB         | Provider-dependent                  |
| Document Translation | 50 MB         | PDF, DOCX, TXT                      |

Exceeding limits returns a `413 Payload Too Large` error with specific limit information.

### Which file formats are supported?

**Images:**

* JPEG, PNG, WebP, GIF
* TIFF (OCR only)

**Documents:**

* PDF
* DOCX, DOC
* TXT, RTF

**Audio:**

* MP3, WAV (provider-dependent)

Format support varies by provider. Check provider-specific documentation or use the [API Discovery](../how-to/discovery/explore-api) endpoint for details.

## LLM Features

### How does streaming work in V3?

Streaming is optional in V3. When you enable streaming (`stream: true`), LLM responses use **Server-Sent Events (SSE)** to provide:

* Reduced perceived latency
* Real-time token generation
* OpenAI-compatible API behavior
* Better UX for chat applications

You can also use V3 without streaming by setting `stream: false`. See [Streaming Responses](../how-to/llm/streaming) for implementation guide.

### How do I send images to LLMs?

V3 LLM supports multimodal inputs via message content arrays:

```python theme={null}
payload = {
    "model": "openai/gpt-4o",
    "messages": [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://example.com/image.jpg"
                    }
                }
            ]
        }
    ]
}
```

Supports:

* Image URLs
* Base64 data URLs (`data:image/jpeg;base64,...`)
* Uploaded file UUIDs

See [Working with Media Files](../how-to/llm/working-with-media) for complete guide.

### Which providers support vision/multimodal?

| Provider  | Models                             | Image Support | File Support |
| --------- | ---------------------------------- | ------------- | ------------ |
| OpenAI    | gpt-4o, gpt-4-turbo                | ✓             | ✓            |
| Anthropic | claude-opus-4-5, claude-sonnet-4-5 | ✓             | ✓            |
| Google    | gemini-2.5-pro, gemini-2.5-flash   | ✓             | ✓            |
| Mistral   | pixtral-12b                        | ✓             | -            |

See [Vision Capabilities](../how-to/llm/vision-capabilities) for provider comparison.

### Does V3 support tool/function calling?

Yes! V3 supports OpenAI-compatible tool calling:

```python theme={null}
payload = {
    "model": "openai/gpt-4",
    "messages": [...],
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get current weather",
                "parameters": { ... }
            }
        }
    ]
}
```

Tool calling support varies by provider:

* ✓ OpenAI (all GPT-4+ models)
* ✓ Anthropic (Claude 3+)
* ✓ Google (Gemini 1.5+)
* ✓ Mistral (Large models)

## Universal AI

### How do I discover available features?

Use the built-in API discovery endpoints:

```python theme={null}
import requests

# List all features
response = requests.get(
    "https://api.edenai.run/v3/info",
    headers={"Authorization": "Bearer YOUR_API_KEY"}
)

# Get feature details
response = requests.get(
    "https://api.edenai.run/v3/info/text/moderation",
    headers={"Authorization": "Bearer YOUR_API_KEY"}
)
# Returns: providers, input schema, output schema
```

See [Explore the API](../how-to/discovery/explore-api) for details.

### Can I use fallback providers?

Not directly in V3's simplified model string format. However, you can implement fallback logic in your application:

```python theme={null}
def call_with_fallback(primary_model, fallback_model, input_data):
    try:
        return call_universal_ai(primary_model, input_data)
    except Exception as e:
        print(f"Primary failed: {e}, trying fallback...")
        return call_universal_ai(fallback_model, input_data)

result = call_with_fallback(
    "text/moderation/openai",
    "text/moderation/google",
    {"text": "Sample text"}
)
```

### How do I optimize costs?

**Best practices:**

1. **Choose cost-effective providers:**
   * Compare pricing in dashboard
   * Check `cost` field in responses

2. **Cache results when possible:**
   * Many features (embeddings, moderation) have deterministic outputs
   * Store results for identical inputs

3. **Use appropriate models:**
   * Don't use premium models for simple tasks
   * Match model capability to task complexity

4. **Batch processing:**
   * Process multiple items in fewer API calls when supported

5. **Monitor usage:**
   * Track costs via [Monitor Usage](../how-to/cost-management/monitor-usage)
   * Set up alerts in dashboard

### I've been an Eden AI user for some time. Is the previous version going to disappear?

Not yet. We'll continue supporting the previous version until the end of 2026. You can
find everything here [https://old-app.edenai.run](https://old-app.edenai.run)

Also, you can find the documentation [here](https://old-docs.edenai.co)

## Troubleshooting

### 401 Unauthorized

**Cause:** Invalid or missing API token

**Solutions:**

* Verify token is correct
* Check `Authorization` header format: `Bearer YOUR_API_KEY`
* Ensure token hasn't been revoked
* Generate new token in dashboard

```python theme={null}
# Correct format
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}
```

### 402 Payment Required - Insufficient Credits

**Cause:** Account has insufficient credits

**Solutions:**

* Add credits in dashboard
* Check current balance
* Review cost per request in responses

### 404 Not Found

**Cause:** Invalid endpoint or model string

**Solutions:**

* Verify endpoint URL is correct
* Check model string format matches pattern
* Use `/v3/info` to discover available features
* Ensure provider supports requested feature

```
# Wrong
"model": "openai/text-moderation"  # ❌ Invalid format

# Correct
"model": "text/moderation/openai"  # ✓
```

### 422 Validation Error

**Cause:** Invalid request body or parameters

**Common issues:**

* Missing required fields
* Invalid parameter types
* File format not supported
* Model string malformed

**Solution:** Check error response for specific field errors:

```json theme={null}
{
  "detail": [
    {
      "loc": ["body", "input", "text"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

### 429 Too Many Requests

**Cause:** Rate limit exceeded

**Solutions:**

* Implement exponential backoff
* Check `X-RateLimit-Reset` header
* Upgrade account tier for higher limits
* Distribute requests over time

```python theme={null}
import time
import requests

headers = {"Authorization": "Bearer YOUR_API_KEY"}

def call_with_retry(url, payload, max_retries=3):
    for attempt in range(max_retries):
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 429:
            retry_after = int(response.headers.get('Retry-After', 60))
            time.sleep(retry_after)
            continue

        return response.json()

    raise Exception("Max retries exceeded")
```

### Invalid model string format

**Cause:** Model string doesn't match expected pattern

**For LLM:** Must be `provider/model`

```python theme={null}
# Wrong
"gpt-4"  # ❌
"openai"  # ❌

# Correct
"openai/gpt-4"  # ✓
```

### Provider temporarily unavailable

**Cause:** Upstream provider experiencing issues

**Solutions:**

* Check [Eden AI Status Page](https://app-edenai.instatus.com/)
* Try alternative provider for same feature
* Implement retry logic with exponential backoff
* Use error response for specific provider error details

## Next Steps

* [Getting Started Guide](./introduction)
* [Authentication Setup](../how-to/authentication/bearer-token-auth)
* [Universal AI Overview](../how-to/universal-ai/getting-started)
* [LLM Chat Completions](../how-to/llm/chat-completions)
* [Monitor Costs](../how-to/cost-management/monitor-usage)


# Introduction
Source: https://docs.edenai.co/v3/get-started/introduction



# Getting Started with Eden AI V3 API

Welcome to the Eden AI V3 API! This guide will help you understand V3's unified architecture and make your first API calls.

## Overview

Eden AI V3 introduces a revolutionary approach to AI API integration with:

* **Universal AI Endpoint** - Single endpoint for all non-LLM features
* **OpenAI-Compatible Format** - Drop-in replacement for OpenAI's API
* **Persistent File Storage** - Upload once, use in multiple requests
* **Built-in API Discovery** - Explore features and schemas programmatically
* **SSE for Streaming** - When streaming is enabled, LLM responses use Server-Sent Events (SSE). Streaming is optional.

<Note>If you were an user before 2026/01/05, you still have access to the previous version: [https://old-app.edenai.run/](https://old-app.edenai.run/). We'll continue supporting the old version until the end of 2026. It your're looking for the documentation, you can find it [here](https://old-docs.edenai.co)</Note>

## V3 Architecture

V3 uses a **model string** format instead of separate provider parameters:

```
feature/subfeature/provider[/model]
```

**Examples:**

* `text/moderation/google`
* `ocr/financial_parser/google`
* `image/generation/openai/dall-e-3`
* `openai/gpt-4` (for LLM endpoints)

This unified format allows a single endpoint to handle all features intelligently.

## Prerequisites

Before you start, you'll need:

1. **API Token** - Get your token from the [Eden AI dashboard](https://app.edenai.run/)
2. **HTTP Client** - Use cURL, Python requests, or any HTTP client
3. **Credits** - Ensure your account has sufficient credits

## Base URL

All V3 API endpoints are available at:

```
https://api.edenai.run/v3
```

## Authentication

All requests must include your API token in the Authorization header:

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST https://api.edenai.run/v3/universal-ai \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json"
  ```

  ```python Python theme={null}
  import requests

  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  response = requests.post(
      "https://api.edenai.run/v3/universal-ai",
      headers=headers,
      json={"model": "text/moderation/openai", "input": {"text": "Sample"}}
  )
  ```

  ```javascript JavaScript theme={null}
  const headers = {
    'Authorization': 'Bearer YOUR_API_KEY',
    'Content-Type': 'application/json'
  };

  const response = await fetch('https://api.edenai.run/v3/universal-ai', {
    method: 'POST',
    headers: headers,
    body: JSON.stringify({
      model: 'text/moderation/openai',
      input: { text: 'Sample' }
    })
  });
  ```
</CodeGroup>

## Your First API Call: Universal AI

The Universal AI endpoint handles all non-LLM features through a single endpoint. Let's moderate some text:

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST https://api.edenai.run/v3/universal-ai \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "text/moderation/google",
      "input": {
        "text": "This is a sample text to moderate for harmful content."
      }
    }'
  ```

  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/universal-ai"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }
  payload = {
      "model": "text/moderation/google",
      "input": {
          "text": "This is a sample text to moderate for harmful content."
      }
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  print(result)
  ```

  ```javascript JavaScript theme={null}
  const url = 'https://api.edenai.run/v3/universal-ai';
  const headers = {
    'Authorization': 'Bearer YOUR_API_KEY',
    'Content-Type': 'application/json'
  };
  const payload = {
    model: 'text/moderation/google',
    input: {
      text: 'This is a sample text to moderate for harmful content.'
    }
  };

  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(payload)
  });

  const result = await response.json();
  console.log(result);
  ```
</CodeGroup>

### Response Format

All V3 responses follow a consistent structure:

```json theme={null}
{
  "status": "success",
  "cost": 0.0001,
  "provider": "google",
  "feature": "text",
  "subfeature": "moderation",
  "output": {
    "nsfw_likelihood": 1,
    "items": [
      {"label": "Toxic", "likelihood": 1, "category": "Toxic", "subcategory": "Toxic", "likelihood_score": 0.0908},
      {"label": "Violent", "likelihood": 1, "category": "Violence", "subcategory": "Violence", "likelihood_score": 0.0120},
      {"label": "Sexual", "likelihood": 1, "category": "Sexual", "subcategory": "Sexual", "likelihood_score": 0.0045}
    ],
    "nsfw_likelihood_score": 0.0908
  }
}
```

## Your First LLM Call: OpenAI-Compatible

The LLM endpoint provides OpenAI-compatible chat completions:

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }
  payload = {
      "model": "openai/gpt-4",
      "messages": [
          {"role": "user", "content": "Hello! How are you?"}
      ]
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  print(result["choices"][0]["message"]["content"])
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.edenai.run/v3/llm/chat/completions \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-4",
      "messages": [{"role": "user", "content": "Hello!"}]
    }'
  ```

  ```javascript JavaScript theme={null}
  const url = 'https://api.edenai.run/v3/llm/chat/completions';
  const headers = {
    'Authorization': 'Bearer YOUR_API_KEY',
    'Content-Type': 'application/json'
  };
  const payload = {
    model: 'openai/gpt-4',
    messages: [{role: 'user', content: 'Hello!'}]
  };

  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(payload)
  });

  const result = await response.json();
  console.log(result.choices[0].message.content);
  ```
</CodeGroup>

### Response Format

LLM responses follow the OpenAI format:

```json theme={null}
{
  "id": "chatcmpl-123",
  "object": "chat.completion",
  "choices": [
    {
      "message": {"role": "assistant", "content": "Hello! I'm doing well, thank you."},
      "index": 0,
      "finish_reason": "stop"
    }
  ],
  "usage": {"prompt_tokens": 12, "completion_tokens": 10, "total_tokens": 22}
}
```

## Working with Files

V3 introduces **persistent file storage**. Upload files once, then reference them by ID:

### Step 1: Upload a File

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/upload"
  headers = {"Authorization": "Bearer YOUR_API_KEY"}

  files = {"file": open("document.pdf", "rb")}
  data = {"purpose": "ocr-processing"}

  response = requests.post(url, headers=headers, files=files, data=data)
  file_info = response.json()
  file_id = file_info["file_id"]

  print(f"Uploaded file ID: {file_id}")
  # Output: Uploaded file ID: 550e8400-e29b-41d4-a716-446655440000
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.edenai.run/v3/upload \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -F "file=@document.pdf" \
    -F "purpose=ocr-processing"
  ```
</CodeGroup>

### Step 2: Use the File in Requests

<CodeGroup>
  ```python Python theme={null}
  import requests
  # Use the file_id in a Universal AI request
  url = "https://api.edenai.run/v3/universal-ai"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }
  payload = {
      "model": "ocr/financial_parser/google",
      "input": {
          "language": "en",
          "file": "550e8400-e29b-41d4-a716-446655440000"
      }
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  print(result["output"])
  ```
</CodeGroup>

## Understanding Model Strings

The model string is the key to V3's unified architecture. Here's the format:

```
feature/subfeature/provider[/model]
```

### Breaking It Down

| Component    | Description               | Example                                           |
| ------------ | ------------------------- | ------------------------------------------------- |
| `feature`    | Category of AI capability | `text`, `ocr`, `image`, `translation`             |
| `subfeature` | Specific functionality    | `moderation`, `ai_detection`, `ocr`, `generation` |
| `provider`   | AI provider               | `openai`, `google`, `amazon`, `anthropic`         |
| `model`      | Specific model (optional) | `gpt-4`, `claude-sonnet-4-5`, `gemini-2.5-pro`    |

### Examples

**Text Analysis:**

* `text/moderation/google` - Content moderation with Google
* `text/moderation/openai` - Content moderation with OpenAI's default model
* `text/embeddings/cohere/embed-english-v3.0` - Generate embeddings with Cohere

**OCR:**

* `ocr/financial_parser/google` - Extract financial information with Google DocumentAI
* `ocr/identity_parser/amazon` - Parse ID documents with Amazon Textract
* `ocr/invoice_parser/microsoft` - Extract invoice data with Azure

**Image:**

* `image/generation/openai/dall-e-3` - Generate images with DALL-E 3
* `image/object_detection/google` - Detect objects with Google Vision
* `image/face_detection/amazon` - Detect faces with AWS Rekognition

**LLM (simplified format):**

* `openai/gpt-4` - Chat with GPT-4
* `anthropic/claude-sonnet-4-5` - Chat with Claude
* `google/gemini-2.5-flash` - Chat with Gemini

## API Discovery

V3 includes built-in endpoints to explore available features programmatically:

<CodeGroup>
  ```python Python theme={null}
  import requests

  # List all features
  response = requests.get(
      "https://api.edenai.run/v3/info"
  )
  data = response.json()
  for feature in data["features"]:
      print(f"{feature['name']}: {[sf['name'] for sf in feature['subfeatures']]}")

  # Get details about a specific feature
  response = requests.get(
      "https://api.edenai.run/v3/info/text/moderation"
  )
  feature_info = response.json()
  print(feature_info["models"])  # Available models with pricing
  print(feature_info["input_schema"])  # Expected input format
  print(feature_info["output_schema"])  # Response format
  ```

  ```bash cURL theme={null}
  # List all features
  curl https://api.edenai.run/v3/info 
  # Get feature details
  curl https://api.edenai.run/v3/info/text/moderation
  ```
</CodeGroup>

## Error Handling

V3 uses standard HTTP status codes with detailed error messages:

```json theme={null}
{
  "status": "error",
  "error": {
    "code": "invalid_model_string",
    "message": "Model string format must be feature/subfeature/provider[/model]",
    "details": {
      "provided": "invalid/model",
      "expected": "feature/subfeature/provider[/model]"
    }
  }
}
```

### Common Status Codes

* `200` - Success
* `400` - Bad Request (invalid model string or input)
* `401` - Unauthorized (invalid API token)
* `402` - Payment Required (insufficient credits)
* `404` - Not Found (feature/provider not available)
* `422` - Validation Error (invalid request body)
* `429` - Rate Limit Exceeded
* `500` - Internal Server Error

## V3 vs V2: Key Differences

| Aspect                   | V2                                       | V3                                      |
| ------------------------ | ---------------------------------------- | --------------------------------------- |
| **Endpoints**            | Feature-specific (`/v2/text/moderation`) | Universal (`/v3/universal-ai`) + LLM    |
| **Provider Format**      | `providers` parameter                    | Model string (`text/moderation/openai`) |
| **File Handling**        | Per-request uploads                      | Persistent storage with file IDs        |
| **LLM Streaming**        | Optional                                 | Optional (SSE when enabled)             |
| **API Discovery**        | Documentation only                       | Built-in `/v3/info` endpoints           |
| **OpenAI Compatibility** | Custom format                            | Native OpenAI format                    |

## Next Steps

Now that you understand V3 basics, explore specific features:

### Universal AI

* [Getting Started with Universal AI](../how-to/universal-ai/getting-started) - Learn the universal endpoint
* [Text Features](../how-to/universal-ai/text-features) - AI detection, moderation, embeddings
* [OCR Features](../how-to/universal-ai/ocr-features) - Text extraction, document parsing
* [Image Features](../how-to/universal-ai/image-features) - Generation, detection, analysis

### OpenAI-Compatible LLM

* [Chat Completions](../how-to/llm/chat-completions) - Build conversational AI with streaming
* [Streaming Responses](../how-to/llm/streaming) - Handle Server-Sent Events
* [File Attachments](../how-to/llm/file-attachments) - Send images and documents to LLMs

### File Management

* [Upload Files](../how-to/upload/upload-files) - Persistent file storage

### API Discovery

* [Explore the API](../how-to/discovery/explore-api) - Programmatic feature discovery

## Need Help?

* Visit [Eden AI Support](https://edenai.co/) for additional assistance


# Professional services
Source: https://docs.edenai.co/v3/get-started/professional_services



## Professional Services details

When you need more than an API, our Professional Services gives you direct access to an experienced Eden AI engineer (or a small delivery squad) to **design, build, and productionize** your AI capabilities—fast.

## 1) Use-case delivery (custom APIs built for your business)

We don’t just advise — we **design and deliver custom AI APIs tailored to your specific business requirements**.
Our engineers work closely with your team to understand your workflows, data, constraints, and success criteria, then build a **production-ready API** that fits directly into your product or internal systems.

**What this typically includes:**

* A **custom API endpoint** designed around your use case (not a generic template)
* Logic tailored to your business rules and edge cases
* Model selection and routing optimized for your goals (quality, cost, latency)
* Prompting and orchestration adapted to your domain vocabulary and data
* Integration-ready outputs (clean schemas, predictable formats, documented behavior)

**Examples of custom APIs we deliver:**

* A **contract analysis API** that extracts clauses specific to your legal framework
* A **customer support triage API** tuned to your internal categories and escalation rules
* A **document processing API** that returns structured fields unique to your workflows
* A **domain-specific assistant API** trained on your internal knowledge and tone
* A **classification or scoring API** aligned with your proprietary business logic

**What you receive**

* A fully functional **custom API endpoint**
* Technical documentation (how to use it, expected inputs/outputs)
* Configuration inside your AI Gateway (monitoring, limits, routing)
* A handover so your team can operate and evolve it confidently

> In short: **you describe the business need, we deliver the API that implements it.**

***

### 2) Model selection, benchmarking & routing strategy

Pick the right models without guesswork.
We’ll help you:

* Define **quality metrics** (accuracy, safety, hallucination tolerance)
* Run **benchmarks** on your real samples (cost/latency/quality)
* Set up **routing rules** (fallbacks, provider failover, cost ceilings)
* Establish a **model lifecycle** (how you upgrade models safely)

**Outputs**

* Benchmark report (recommendations + tradeoffs)
* Routing policy configuration
* Rollout plan (A/B, canary, guardrail thresholds)

***

### 3) Production readiness & reliability hardening

Turn a prototype into something ops teams trust.
We implement:

* **Observability** (latency, errors, token usage, provider health, fallbacks)
* **Rate limits + quotas + spend caps** by project/environment
* **Caching strategies** (where appropriate) to reduce cost and latency
* **Incident playbooks** (what to do when a provider degrades)
* **Regression checks** for prompt/model updates

**Outputs**

* Dashboards/KPIs and alerting recommendations
* Reliability checklist + incident runbook
* Cost controls configured and validated

***

### 4) Safety, compliance, and data controls (optional)

For regulated environments or sensitive data.
Support can include:

* **PII handling** (redaction/masking strategy, logging policies)
* **Data retention guidance** (what is stored, for how long, and why)
* **Security review support** (documentation, architecture notes, DPA/security questionnaires)
* **Access controls** (least-privilege roles, key rotation approach)

**Outputs**

* Security & data-flow documentation (shareable with your compliance team)
* Recommended policies for logging/retention/access

## How we work (simple, transparent)

1. **Discovery (1–2 sessions):** goals, constraints, success metrics, sample data
2. **Design:** architecture + model/routing plan + delivery milestones
3. **Build & iterate:** weekly demos, measurable progress, rapid feedback loops
4. **Launch:** monitoring, budgets, guardrails, and handover
5. **Optimize (optional):** continuous improvement and cost/quality tuning

***

## Engagement options

* **On-demand expert hours** (ideal for reviews, troubleshooting, quick builds)
* **Fixed-scope delivery** (clear outputs, timeline, and acceptance criteria)
* **Ongoing partnership** (monthly retainer for continuous improvements)

## What we’ll ask from you (to move fast)

* A small set of **real examples** (inputs/outputs, edge cases)
* Your target **latency + cost** expectations (even rough)
* One technical owner for weekly feedback and approvals

**Talk to a founder**


# Smart routing
Source: https://docs.edenai.co/v3/get-started/smart-routing



# Smart Routing: Let AI Choose the Best Model

Get optimal model selection automatically with Eden AI's smart routing feature. Instead of manually selecting models, let the system intelligently route your requests based on context.

## Overview

Smart routing uses the special model identifier `@edenai` to dynamically select the best LLM model for your request. The system analyzes your messages, tools, and other context to route to the optimal provider/model combination.

**Key Benefits:**

* **Automatic optimization** - No need to research and compare models
* **Cost efficiency** - Routes to models with the best price/performance ratio
* **Context-aware** - Selection adapts to your specific request
* **Fallback resilience** - Automatic fallback if routing fails
* **Works with all features** - Streaming, function calling, vision, etc.

**Powered by:** [NotDiamond](https://notdiamond.ai/) routing engine

## Quick Start: Your First Routed Request

The simplest way to use smart routing is to set `model: "@edenai"`:

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "@edenai",  # Let Eden AI choose the best model
      "messages": [
          {"role": "user", "content": "Explain quantum computing in simple terms"}
      ]
  }

  # The system automatically selects the optimal model
  response = requests.post(url, headers=headers, json=payload)

  print(response.json())
  ```

  ```javascript JavaScript theme={null}
  const url = 'https://api.edenai.run/v3/llm/chat/completions';
  const headers = {
    'Authorization': 'Bearer YOUR_API_KEY',
    'Content-Type': 'application/json'
  };

  const payload = {
    model: '@edenai',  // Let Eden AI choose the best model
    messages: [
      {role: 'user', content: 'Explain quantum computing in simple terms'}
    ]
  };

  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(payload)
  });

  const data = await response.json();
  console.log(data);
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.edenai.run/v3/llm/chat/completions \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "@edenai",
      "messages": [
        {"role": "user", "content": "Explain quantum computing in simple terms"}
      ]
    }'
  ```
</CodeGroup>

That's it! The system will automatically select the best model from all available options.

## How It Works

When you use `model: "@edenai"`, here's what happens:

1. **Request Analysis** - The system analyzes your messages, tools, and parameters
2. **Model Selection** - NotDiamond's routing engine selects the optimal model from available candidates
3. **Transparent Routing** - Your request is routed to the selected model
4. **Normal Response** - You receive the response as if you had specified the model directly

**Typical latency:** 100-500ms additional processing time for model selection

## Customizing Model Candidates

By default, smart routing considers all available models. You can customize the candidate pool with `router_candidates`:

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "@edenai",
      "router_candidates": [
          "openai/gpt-4o",
          "anthropic/claude-sonnet-4-5",
          "google/gemini-2.5-flash"
      ],
      "messages": [
          {"role": "user", "content": "Write a Python function to sort a list"}
      ]
  }

  # Router will choose from only these 3 models
  response = requests.post(url, headers=headers, json=payload)

  print(response.json())
  ```

  ```javascript JavaScript theme={null}
  const payload = {
    model: '@edenai',
    router_candidates: [
      'openai/gpt-4o',
      'anthropic/claude-sonnet-4-5',
      'google/gemini-2.5-flash'
    ],
    messages: [
      {role: 'user', content: 'Write a Python function to sort a list'}
    ]
  };

  const response = await fetch('https://api.edenai.run/v3/llm/chat/completions', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_API_KEY',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(payload)
  });
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.edenai.run/v3/llm/chat/completions \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "@edenai",
      "router_candidates": [
        "openai/gpt-4o",
        "anthropic/claude-sonnet-4-5",
        "google/gemini-2.5-flash"
      ],
      "messages": [
        {"role": "user", "content": "Write a Python function to sort a list"}
      ]
    }'
  ```
</CodeGroup>

## When to Use Smart Routing

### ✅ Great Use Cases

* **General-purpose chatbots** - Let the router optimize for diverse queries
* **Cost-sensitive applications** - Router balances quality and cost
* **Multi-task applications** - Different queries benefit from different models
* **Experimentation** - Compare router performance vs. fixed models

### ⚠️ Consider Fixed Models Instead

* **Specific model requirements** - You need a particular model's unique features
* **Latency-critical** - Every 100ms matters (smart routing adds overhead)
* **Consistent behavior** - You need identical model behavior across requests
* **High-volume production** - You've already optimized model selection

## Model Selection Criteria

The routing engine considers multiple factors:

* **Task type** - Code generation, creative writing, analysis, etc.
* **Conversation context** - Prior messages and conversation flow
* **Tool/function calls** - Compatibility with function calling requirements
* **Quality requirements** - Implicit in message complexity
* **Cost efficiency** - Price/performance optimization

## Default Model Pool

When you don't specify `router_candidates`, the system uses all available LLM models, including:

**Top-tier Models:**

* OpenAI: GPT-4, GPT-4 Turbo, GPT-4o, GPT-5 (latest versions)
* Anthropic: Claude Haiku, Sonnet, Opus (4.x series)
* Google: Gemini 2.0/2.5/3.0 (Flash and Pro)
* Mistral: Large, Medium, Small models

**Specialized Models:**

* X.AI: Grok 3, Grok 4
* Together.ai: Llama 3/3.1 models
* Cohere: Command R, Command R+
* Perplexity: Sonar

The exact pool is dynamically managed and may change as new models become available.

## Fallback Behavior

Smart routing includes intelligent fallbacks:

1. **With custom candidates** - Falls back to first candidate on routing failure
2. **Without candidates** - Falls back to `openai/gpt-4o` (reliable default)
3. **Transparent errors** - You'll see clear error messages if routing fails completely

<Info>
  **Reliability:** Fallback ensures your requests always succeed, even if the routing service is temporarily unavailable.
</Info>

## Response Format

Smart routing responses are identical to fixed-model responses. The streaming format follows OpenAI's SSE standard:

```
data: {"id":"chatcmpl-123","object":"chat.completion.chunk","created":1234567890,"model":"openai/gpt-4o","choices":[{"index":0,"delta":{"role":"assistant","content":"Hello"},"finish_reason":null}]}

data: {"id":"chatcmpl-123","object":"chat.completion.chunk","created":1234567890,"model":"openai/gpt-4o","choices":[{"index":0,"delta":{"content":"!"},"finish_reason":null}]}

data: {"id":"chatcmpl-123","object":"chat.completion.chunk","created":1234567890,"model":"openai/gpt-4o","choices":[{"index":0,"delta":{},"finish_reason":"stop"}]}

data: [DONE]
```

<Tip>
  **Tracking:** The `model` field in the response shows which model was selected by the router.
</Tip>

## OpenAI SDK Compatibility

Smart routing works seamlessly with the OpenAI Python SDK:

<CodeGroup>
  ```python Python (OpenAI SDK) theme={null}
  from openai import OpenAI

  client = OpenAI(
      api_key="YOUR_API_KEY",
      base_url="https://api.edenai.run/v3/llm"
  )

  # Use smart routing with OpenAI SDK
  response = client.chat.completions.create(
      model="@edenai",
      messages=[
          {"role": "user", "content": "Tell me a joke"}
      ],
      extra_body={  # Custom parameters
          "router_candidates": [
              "openai/gpt-4o",
              "anthropic/claude-sonnet-4-5"
          ]
      }
  )

  print(response.choices[0].message.content)
  ```
</CodeGroup>

<Info>
  **SDK Integration:** Use `extra_body` to pass the `router_candidates` parameter when using the OpenAI SDK.
</Info>

## Pricing

Smart routing costs are based on the **selected model's pricing**. The routing decision itself is free.

**Example:**

* If router selects `openai/gpt-4o` → You pay GPT-4o rates
* If router selects `google/gemini-2.5-flash` → You pay Gemini Flash rates

The router optimizes for cost-effectiveness, often selecting cheaper models when they meet quality requirements.

## Next Steps

Now that you understand smart routing basics:

* **[Smart Routing How-To Guide](../how-to/llm/smart-routing)** - Advanced patterns and best practices
* **[Optimize LLM Costs Tutorial](../tutorials/optimize-llm-costs)** - Complete cost optimization workflow
* **[Streaming Guide](../how-to/llm/streaming)** - Handle SSE responses effectively
* **[Function Calling](../how-to/llm/chat-completions#function-calling)** - Use tools with smart routing

## Troubleshooting

### Router returns error "no candidates provided"

**Cause:** Empty `router_candidates` list or all candidates filtered out
**Solution:** Omit `router_candidates` to use default pool, or provide valid model strings

### Higher latency than expected

**Cause:** Routing decision adds 100-500ms overhead
**Solution:** Use fixed models for latency-critical applications

### Unexpected model selection

**Cause:** Router optimizes for multiple factors, not just quality
**Solution:** Use `router_candidates` to limit selection pool, or switch to fixed models

### "Router API unavailable" errors

**Cause:** Temporary routing service outage
**Solution:** System automatically falls back - check if fallback model meets your needs

<Tip>
  **Getting Started:** Start with default routing (`model: "@edenai"`), then customize with `router_candidates` if needed.
</Tip>


# Bearer token auth
Source: https://docs.edenai.co/v3/how-to/authentication/bearer-token-auth



# Authenticate Using Bearer Token

Learn how to authenticate your API requests using Bearer token authentication.

## Overview

All Eden AI V3 API requests require authentication using a Bearer token. This token identifies your account and tracks usage for billing and rate limiting purposes.

## Getting Your API Token

1. Sign up or log in to your [Eden AI Dashboard](https://app.edenai.run/)
2. Navigate to **API Keys** section
3. Copy your API key
4. Keep it secure - never commit it to version control or share publicly

## Authentication Header

Include your API token in the `Authorization` header with the `Bearer` scheme:

```
Authorization: Bearer YOUR_API_KEY
```

## Examples

### cURL

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST https://api.edenai.run/v3/llm/chat/completions \
    -H "Authorization: Bearer eyJhbG...xxxxxxxxxxxxxxxxxxxxxxxx" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-4",
      "messages": [{"role": "user", "content": "Hello!"}]
    }'
  ```

  ```python Python (requests) theme={null}
  import requests

  API_KEY = "eyJhbG...xxxxxxxxxxxxxxxxxxxxxxxx"

  headers = {
      "Authorization": f"Bearer {API_KEY}",
      "Content-Type": "application/json"
  }

  response = requests.post(
      "https://api.edenai.run/v3/llm/chat/completions",
      headers=headers,
      json={
          "model": "openai/gpt-4",
          "messages": [{"role": "user", "content": "Hello!"}]
      }
  )

  print(response.json())
  ```

  ```python Python (with environment variable) theme={null}
  import os
  import requests

  # Load from environment variable
  API_KEY = os.getenv("EDENAI_API_KEY")

  headers = {
      "Authorization": f"Bearer {API_KEY}",
      "Content-Type": "application/json"
  }

  response = requests.post(
      "https://api.edenai.run/v3/llm/chat/completions",
      headers=headers,
      json={
          "model": "openai/gpt-4",
          "messages": [{"role": "user", "content": "Hello!"}]
      }
  )

  result = response.json()
  ```

  ```javascript JavaScript (fetch) theme={null}
  const API_KEY = 'sk_xxxxxxxxxxxxxxxxxxxxxxxx';

  const headers = {
    'Authorization': `Bearer ${API_KEY}`,
    'Content-Type': 'application/json'
  };

  const response = await fetch('https://api.edenai.run/v3/llm/chat/completions', {
    method: 'POST',
    headers: headers,
    body: JSON.stringify({
      model: 'openai/gpt-4',
      messages: [{role: 'user', content: 'Hello!'}]
    })
  });

  const result = await response.json();
  console.log(result);
  ```

  ```javascript JavaScript (axios) theme={null}
  const axios = require('axios');

  const API_KEY = 'sk_xxxxxxxxxxxxxxxxxxxxxxxx';

  const response = await axios.post(
    'https://api.edenai.run/v3/llm/chat/completions',
    {
      model: 'openai/gpt-4',
      messages: [{role: 'user', content: 'Hello!'}]
    },
    {
      headers: {
        'Authorization': `Bearer ${API_KEY}`,
        'Content-Type': 'application/json'
      }
    }
  );

  console.log(response.data);
  ```

  ```go Go theme={null}
  package main

  import (
      "bytes"
      "encoding/json"
      "fmt"
      "io"
      "net/http"
  )

  func main() {
      apiKey := "eyJhbG...xxxxxxxxxxxxxxxxxxxxxxxx"
      url := "https://api.edenai.run/v3/llm/chat/completions"

      payload := map[string]interface{}{
          "model": "openai/gpt-4",
          "messages": []map[string]string{
              {"role": "user", "content": "Hello!"},
          },
      }

      jsonData, _ := json.Marshal(payload)

      req, _ := http.NewRequest("POST", url, bytes.NewBuffer(jsonData))
      req.Header.Set("Authorization", "Bearer "+apiKey)
      req.Header.Set("Content-Type", "application/json")

      client := &http.Client{}
      resp, err := client.Do(req)
      if err != nil {
          panic(err)
      }
      defer resp.Body.Close()

      body, _ := io.ReadAll(resp.Body)
      fmt.Println(string(body))
  }
  ```
</CodeGroup>

## Best Practices

### Store Tokens Securely

Never hardcode API tokens in your source code. Use environment variables or secret management systems:

<CodeGroup>
  ```python Python (.env file) theme={null}
  # .env file
  EDENAI_API_KEY=sk_xxxxxxxxxxxxxxxxxxxxxxxx

  # Python code
  from dotenv import load_dotenv
  import os

  load_dotenv()
  API_KEY = os.getenv("EDENAI_API_KEY")
  ```

  ```javascript JavaScript (.env file) theme={null}
  // .env file
  EDENAI_API_KEY=sk_xxxxxxxxxxxxxxxxxxxxxxxx

  // JavaScript code
  require('dotenv').config();
  const API_KEY = process.env.EDENAI_API_KEY;
  ```

  ```bash Bash (export) theme={null}
  # Set environment variable
  export EDENAI_API_KEY="eyJhbG...xxxxxxxxxxxxxxxxxxxxxxxx"

  # Use in cURL
  curl -X POST https://api.edenai.run/v3/llm/chat/completions \
    -H "Authorization: Bearer $EDENAI_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"model": "openai/gpt-4", "messages": [{"role": "user", "content": "Hello!"}]}'
  ```
</CodeGroup>

### Add to .gitignore

Ensure your `.env` file and any files containing API keys are excluded from version control:

```bash theme={null}
# .gitignore
.env
.env.local
*.key
secrets.json
```

### Rotate Keys Regularly

For security, periodically rotate your API keys:

1. Generate a new key in the dashboard
2. Update your application with the new key
3. Delete the old key after confirming the new one works

### Use Different Keys for Different Environments

Create separate API keys for development, staging, and production environments to:

* Track usage separately
* Revoke access independently
* Maintain security isolation

## Authentication Errors

### 401 Unauthorized

**Cause:** Invalid or missing API token

<CodeGroup>
  ```json Error Response theme={null}
  {
    "detail": "Invalid authentication credentials"
  }
  ```
</CodeGroup>

**Solutions:**

* Verify your token is correct
* Check the `Authorization` header format: `Bearer YOUR_TOKEN`
* Ensure the token hasn't been revoked
* Confirm there are no extra spaces or newline characters

### 402 Payment Required

**Cause:** Insufficient credits in your account

<CodeGroup>
  ```json Error Response theme={null}
  {
    "detail": "Insufficient credits"
  }
  ```
</CodeGroup>

**Solutions:**

* Add credits to your account in the dashboard
* Check your current balance
* Review your usage patterns

## Testing Authentication

Test your authentication with a simple request:

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST https://api.edenai.run/v3/llm/chat/completions \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"model": "openai/gpt-4", "messages": [{"role": "user", "content": "Test"}]}'
  ```

  ```python Python theme={null}
  import requests

  headers = {
      "Authorization": f"Bearer {API_KEY}",
      "Content-Type": "application/json"
  }
  response = requests.post(
      "https://api.edenai.run/v3/llm/chat/completions",
      headers=headers,
      json={
          "model": "openai/gpt-4",
          "messages": [{"role": "user", "content": "Test"}]
      }
  )

  if response.status_code == 200:
      print("Authentication successful!")
      print(response.json())
  else:
      print(f"Authentication failed: {response.status_code}")
      print(response.json())
  ```
</CodeGroup>

## Using Client Libraries

If you're using an HTTP client library, most support automatic header management:

<CodeGroup>
  ```python Python (requests Session) theme={null}
  import requests

  # Create session with persistent headers
  session = requests.Session()
  session.headers.update({
      "Authorization": f"Bearer {API_KEY}",
      "Content-Type": "application/json"
  })

  # All requests use the same headers
  response1 = session.post(
      "https://api.edenai.run/v3/llm/chat/completions",
      json={
          "model": "openai/gpt-4",
          "messages": [{"role": "user", "content": "First message"}]
      }
  )

  response2 = session.post(
      "https://api.edenai.run/v3/llm/chat/completions",
      json={
          "model": "anthropic/claude-sonnet-4-5",
          "messages": [{"role": "user", "content": "Second message"}]
      }
  )
  ```

  ```javascript JavaScript (axios instance) theme={null}
  const axios = require('axios');

  // Create axios instance with default config
  const edenai = axios.create({
    baseURL: 'https://api.edenai.run/v3',
    headers: {
      'Authorization': `Bearer ${API_KEY}`,
      'Content-Type': 'application/json'
    }
  });

  // All requests use the same config
  const response1 = await edenai.post('/llm/chat/completions', {
    model: 'openai/gpt-4',
    messages: [{role: 'user', content: 'First message'}]
  });

  const response2 = await edenai.post('/llm/chat/completions', {
    model: 'anthropic/claude-sonnet-4-5',
    messages: [{role: 'user', content: 'Second message'}]
  });
  ```
</CodeGroup>

## Next Steps

* [Chat Completions Guide](../llm/chat-completions)
* [Universal AI Getting Started](../universal-ai/getting-started)
* [Upload Files](../upload/upload-files)


# Monitor usage
Source: https://docs.edenai.co/v3/how-to/cost-management/monitor-usage



# Monitor API Usage and Costs

Learn how to track your Eden AI API consumption and costs using the Cost Monitoring endpoints.

> **Note**: These are admin/dashboard endpoints typically used by the Eden AI dashboard or custom admin interfaces. For standard API usage authentication, see the [Authentication Guide](../authentication/bearer-token-auth).

## Overview

The Cost Monitoring API provides two key endpoints to help you track and manage your Eden AI spending:

* **Monitor Consumptions** - Get detailed usage and cost breakdowns by date, provider, and feature
* **Check Credits** - Retrieve your current account credit balance

These endpoints are designed for building dashboards, generating reports, and monitoring API usage patterns.

## Endpoints

### Monitor Consumptions

```
GET https://api.edenai.run/v2/cost_management/
```

Retrieve detailed cost and usage data for a specific date range.

### Check Current Credits

```
GET https://api.edenai.run/v2/cost_management/credits/
```

Get your current Eden AI account credit balance.

## Key Concepts

### Step Parameter

The `step` parameter controls how data is aggregated:

| Step Value | Aggregation Period | Use Case                |
| ---------- | ------------------ | ----------------------- |
| 1          | Daily              | Detailed daily analysis |
| 2          | Weekly             | Weekly trends           |
| 3          | Monthly            | Monthly reports         |
| 4          | Yearly             | Annual summaries        |

### Date Ranges

* Dates must be in `YYYY-MM-DD` format
* Both `begin` and `end` dates are required
* Data is grouped by the specified `step` value

### Filtering Options

Filter your cost data by:

* **Provider**: Specific AI provider (e.g., `openai`, `anthropic`)
* **Subfeature**: Specific feature (e.g., `chat`, `ocr`, `text_to_speech`)
* **Token**: Specific API token
* **Workflow ID**: Specific workflow execution
* **RAG Project ID**: Specific RAG project

## Check Your Current Credits

Get your current credit balance to verify available funds:

<CodeGroup>
  ```bash cURL theme={null}
  curl -X GET https://api.edenai.run/v2/cost_management/credits/ \
    -H "Authorization: Bearer sk_xxxxxxxxxxxxxxxxxxxxxxxx"
  ```

  ```python Python theme={null}
  import requests

  API_KEY = "eyJhbG...xxxxxxxxxxxxxxxxxxxxxxxx"

  headers = {"Authorization": f"Bearer {API_KEY}"}

  response = requests.get(
      "https://api.edenai.run/v2/cost_management/credits/",
      headers=headers
  )

  credits_data = response.json()
  print(f"Current credits: ${credits_data['credits']:.2f}")
  ```

  ```javascript JavaScript theme={null}
  const API_KEY = 'sk_xxxxxxxxxxxxxxxxxxxxxxxx';

  const response = await fetch(
    'https://api.edenai.run/v2/cost_management/credits/',
    {
      headers: {
        'Authorization': `Bearer ${API_KEY}`
      }
    }
  );

  const creditsData = await response.json();
  console.log(`Current credits: $${creditsData.credits.toFixed(2)}`);
  ```
</CodeGroup>

**Response:**

```json theme={null}
{
  "credits": 42.50
}
```

## Monitor Usage - Basic Example

Get your last 30 days of usage, grouped by day:

<CodeGroup>
  ```bash cURL theme={null}
  curl -X GET "https://api.edenai.run/v2/cost_management/?begin=2024-01-01&end=2024-01-31&step=1" \
    -H "Authorization: Bearer sk_xxxxxxxxxxxxxxxxxxxxxxxx"
  ```

  ```python Python theme={null}
  import requests
  from datetime import datetime, timedelta

  API_KEY = "eyJhbG...xxxxxxxxxxxxxxxxxxxxxxxx"

  # Get last 30 days
  end_date = datetime.now()
  begin_date = end_date - timedelta(days=30)

  headers = {"Authorization": f"Bearer {API_KEY}"}
  params = {
      "begin": begin_date.strftime("%Y-%m-%d"),
      "end": end_date.strftime("%Y-%m-%d"),
      "step": 1  # Daily aggregation
  }

  response = requests.get(
      "https://api.edenai.run/v2/cost_management/",
      headers=headers,
      params=params
  )

  data = response.json()
  print(f"Usage data retrieved for {len(data['response'])} token(s)")
  ```

  ```javascript JavaScript theme={null}
  const API_KEY = 'sk_xxxxxxxxxxxxxxxxxxxxxxxx';

  // Get last 30 days
  const endDate = new Date();
  const beginDate = new Date();
  beginDate.setDate(beginDate.getDate() - 30);

  const params = new URLSearchParams({
    begin: beginDate.toISOString().split('T')[0],
    end: endDate.toISOString().split('T')[0],
    step: '1'  // Daily aggregation
  });

  const response = await fetch(
    `https://api.edenai.run/v2/cost_management/?${params}`,
    {
      headers: {
        'Authorization': `Bearer ${API_KEY}`
      }
    }
  );

  const data = await response.json();
  console.log(`Usage data retrieved for ${data.response.length} token(s)`);
  ```
</CodeGroup>

## Filter by Provider

Get costs for a specific AI provider only:

<CodeGroup>
  ```bash cURL theme={null}
  curl -X GET "https://api.edenai.run/v2/cost_management/?begin=2024-01-01&end=2024-01-31&step=3&provider=openai" \
    -H "Authorization: Bearer sk_xxxxxxxxxxxxxxxxxxxxxxxx"
  ```

  ```python Python theme={null}
  import requests

  API_KEY = "eyJhbG...xxxxxxxxxxxxxxxxxxxxxxxx"

  headers = {"Authorization": f"Bearer {API_KEY}"}
  params = {
      "begin": "2024-01-01",
      "end": "2024-12-31",
      "step": 3,  # Monthly aggregation
      "provider": "openai"  # Filter by OpenAI only
  }

  response = requests.get(
      "https://api.edenai.run/v2/cost_management/",
      headers=headers,
      params=params
  )

  data = response.json()

  # Calculate total OpenAI costs
  total_cost = 0
  for token_data in data['response']:
      for date, features in token_data['data'].items():
          for feature, details in features.items():
              total_cost += details['total_cost']

  print(f"Total OpenAI cost: ${total_cost:.2f}")
  ```

  ```javascript JavaScript theme={null}
  const API_KEY = 'sk_xxxxxxxxxxxxxxxxxxxxxxxx';

  const params = new URLSearchParams({
    begin: '2024-01-01',
    end: '2024-12-31',
    step: '3',  // Monthly aggregation
    provider: 'openai'  // Filter by OpenAI only
  });

  const response = await fetch(
    `https://api.edenai.run/v2/cost_management/?${params}`,
    {
      headers: {
        'Authorization': `Bearer ${API_KEY}`
      }
    }
  );

  const data = await response.json();

  // Calculate total OpenAI costs
  let totalCost = 0;
  data.response.forEach(tokenData => {
    Object.values(tokenData.data).forEach(features => {
      Object.values(features).forEach(details => {
        totalCost += details.total_cost;
      });
    });
  });

  console.log(`Total OpenAI cost: $${totalCost.toFixed(2)}`);
  ```
</CodeGroup>

## Filter by Subfeature

Track costs for specific features like LLM chat or OCR:

<CodeGroup>
  ```python Python theme={null}
  import requests

  API_KEY = "eyJhbG...xxxxxxxxxxxxxxxxxxxxxxxx"

  headers = {"Authorization": f"Bearer {API_KEY}"}
  params = {
      "begin": "2024-01-01",
      "end": "2024-01-31",
      "step": 1,  # Daily
      "subfeature": "chat"  # Only LLM chat costs
  }

  response = requests.get(
      "https://api.edenai.run/v2/cost_management/",
      headers=headers,
      params=params
  )

  data = response.json()
  print(f"Chat feature costs retrieved")
  ```

  ```javascript JavaScript theme={null}
  const API_KEY = 'sk_xxxxxxxxxxxxxxxxxxxxxxxx';

  const params = new URLSearchParams({
    begin: '2024-01-01',
    end: '2024-01-31',
    step: '1',
    subfeature: 'chat'  // Only LLM chat costs
  });

  const response = await fetch(
    `https://api.edenai.run/v2/cost_management/?${params}`,
    {
      headers: {
        'Authorization': `Bearer ${API_KEY}`
      }
    }
  );

  const data = await response.json();
  console.log('Chat feature costs retrieved');
  ```
</CodeGroup>

## Filter by Token

Track usage for a specific API token:

<CodeGroup>
  ```python Python theme={null}
  import requests

  API_KEY = "eyJhbG...xxxxxxxxxxxxxxxxxxxxxxxx"
  TRACKED_TOKEN = "prod_token_123"

  headers = {"Authorization": f"Bearer {API_KEY}"}
  params = {
      "begin": "2024-01-01",
      "end": "2024-01-31",
      "step": 2,  # Weekly
      "token": TRACKED_TOKEN
  }

  response = requests.get(
      "https://api.edenai.run/v2/cost_management/",
      headers=headers,
      params=params
  )

  data = response.json()
  print(f"Usage for token '{TRACKED_TOKEN}' retrieved")
  ```
</CodeGroup>

## Response Format

The monitoring endpoint returns data structured by token, date, and feature:

```json theme={null}
{
  "response": [
    {
      "token": "base_token",
      "data": {
        "2024-01-01": {
          "text__chat": {
            "total_cost": 11.30,
            "details": 381,
            "cost_per_provider": {
              "openai": 11.28,
              "anthropic": 0.02
            }
          },
          "image__explicit_content": {
            "total_cost": 0.15,
            "details": 101,
            "cost_per_provider": {
              "google": 0.15
            }
          }
        },
        "2024-01-02": {
          "ocr__ocr": {
            "total_cost": 0.006,
            "details": 4,
            "cost_per_provider": {
              "google": 0.006
            }
          }
        }
      }
    }
  ]
}
```

### Response Fields

| Field               | Type    | Description                              |
| ------------------- | ------- | ---------------------------------------- |
| `token`             | string  | API token identifier                     |
| `data`              | object  | Date-keyed usage data                    |
| `total_cost`        | number  | Total cost for this feature on this date |
| `details`           | integer | Number of API calls made                 |
| `cost_per_provider` | object  | Cost breakdown by provider               |

### Feature Naming Convention

Features follow the pattern `{category}__{subfeature}`:

* `text__chat` - LLM chat completions
* `text__generation` - Text generation
* `text__embeddings` - Text embeddings
* `image__explicit_content` - Image moderation
* `image__question_answer` - Image Q\&A
* `ocr__ocr` - OCR text extraction
* `audio__text_to_speech` - Text-to-speech

## Analyze Costs by Provider

Compare costs across different AI providers:

<CodeGroup>
  ```python Python theme={null}
  import requests
  from collections import defaultdict

  API_KEY = "eyJhbG...xxxxxxxxxxxxxxxxxxxxxxxx"

  headers = {"Authorization": f"Bearer {API_KEY}"}
  params = {
      "begin": "2024-01-01",
      "end": "2024-12-31",
      "step": 4  # Yearly summary
  }

  response = requests.get(
      "https://api.edenai.run/v2/cost_management/",
      headers=headers,
      params=params
  )

  data = response.json()

  # Aggregate costs by provider
  provider_costs = defaultdict(float)
  total_calls = defaultdict(int)

  for token_data in data['response']:
      for date, features in token_data['data'].items():
          for feature, details in features.items():
              total_calls[feature] += details['details']
              for provider, cost in details['cost_per_provider'].items():
                  provider_costs[provider] += cost

  # Display results
  print("Cost Breakdown by Provider:")
  print("-" * 40)
  for provider, cost in sorted(provider_costs.items(),
                                 key=lambda x: x[1],
                                 reverse=True):
      print(f"{provider:15s}: ${cost:>10.2f}")

  print("-" * 40)
  print(f"{'TOTAL':15s}: ${sum(provider_costs.values()):>10.2f}")
  ```
</CodeGroup>

**Example Output:**

```
Cost Breakdown by Provider:
----------------------------------------
openai         :     $34.04
anthropic      :      $2.97
google         :      $0.35
elevenlabs     :      $0.75
cohere         :      $0.08
----------------------------------------
TOTAL          :     $38.19
```

## Best Practices

### Query Optimization

**Use appropriate step sizes:**

* Daily (`step=1`): Last 30-90 days for detailed analysis
* Weekly (`step=2`): Last 3-6 months for trend analysis
* Monthly (`step=3`): Last year for reporting
* Yearly (`step=4`): Multi-year historical data

**Limit date ranges:**

```python theme={null}
# Good - Focused query
params = {"begin": "2024-01-01", "end": "2024-01-31", "step": 1}

# Less efficient - Very large range with daily granularity
params = {"begin": "2020-01-01", "end": "2024-12-31", "step": 1}
```

### Dashboard Integration

**Cache results** for frequently accessed data:

```python theme={null}
import requests
from datetime import datetime, timedelta
import redis

API_KEY = "eyJhbG...xxxxxxxxxxxxxxxxxxxxxxxx"
cache = redis.Redis(host='localhost', port=6379, db=0)

def get_monthly_costs(year, month):
    cache_key = f"costs:{year}:{month}"

    # Check cache first
    cached = cache.get(cache_key)
    if cached:
        return eval(cached)

    # Fetch from API
    headers = {"Authorization": f"Bearer {API_KEY}"}
    params = {
        "begin": f"{year}-{month:02d}-01",
        "end": f"{year}-{month:02d}-28",
        "step": 3
    }

    response = requests.get(
        "https://api.edenai.run/v2/cost_management/",
        headers=headers,
        params=params
    )

    data = response.json()

    # Cache for 1 hour
    cache.setex(cache_key, 3600, str(data))

    return data
```

### Cost Alerting

**Monitor for unexpected spikes:**

```python theme={null}
import requests

API_KEY = "eyJhbG...xxxxxxxxxxxxxxxxxxxxxxxx"
ALERT_THRESHOLD = 100.0  # Alert if daily cost > $100

headers = {"Authorization": f"Bearer {API_KEY}"}
params = {
    "begin": "2024-01-01",
    "end": "2024-01-31",
    "step": 1
}

response = requests.get(
    "https://api.edenai.run/v2/cost_management/",
    headers=headers,
    params=params
)

data = response.json()

# Check for high-cost days
for token_data in data['response']:
    for date, features in token_data['data'].items():
        daily_cost = sum(
            details['total_cost']
            for details in features.values()
        )

        if daily_cost > ALERT_THRESHOLD:
            print(f"⚠️  Alert: High cost on {date}: ${daily_cost:.2f}")
            # Send notification (email, Slack, etc.)
```

### Track Budget Usage

**Monitor remaining budget:**

```python theme={null}
import requests

API_KEY = "eyJhbG...xxxxxxxxxxxxxxxxxxxxxxxx"
MONTHLY_BUDGET = 500.0

# Get current credits
credits_response = requests.get(
    "https://api.edenai.run/v2/cost_management/credits/",
    headers={"Authorization": f"Bearer {API_KEY}"}
)
current_credits = credits_response.json()['credits']

# Get this month's spending
import datetime
today = datetime.date.today()
first_day = today.replace(day=1)

params = {
    "begin": first_day.strftime("%Y-%m-%d"),
    "end": today.strftime("%Y-%m-%d"),
    "step": 3
}

usage_response = requests.get(
    "https://api.edenai.run/v2/cost_management/",
    headers={"Authorization": f"Bearer {API_KEY}"},
    params=params
)

# Calculate month's spending
month_spending = 0
for token_data in usage_response.json()['response']:
    for date, features in token_data['data'].items():
        for details in features.values():
            month_spending += details['total_cost']

remaining_budget = MONTHLY_BUDGET - month_spending
budget_pct = (month_spending / MONTHLY_BUDGET) * 100

print(f"Monthly Budget: ${MONTHLY_BUDGET:.2f}")
print(f"Spent This Month: ${month_spending:.2f} ({budget_pct:.1f}%)")
print(f"Remaining: ${remaining_budget:.2f}")
print(f"Current Credits: ${current_credits:.2f}")
```

## Error Handling

### 400 Bad Request

Invalid parameters (missing required fields, invalid dates):

```json theme={null}
{
  "error": {
    "type": "validation_error",
    "message": {
      "begin": ["This field is required."]
    }
  }
}
```

### 403 Forbidden

Insufficient permissions to access cost data:

```json theme={null}
{
  "error": {
    "type": "permission_error",
    "message": "You do not have permission to access this resource"
  }
}
```

### 404 Not Found

No data found for the specified filters:

```json theme={null}
{
  "details": "Not Found"
}
```

## Next Steps

* [Manage Custom Tokens](../../how-to/user-management/manage-tokens)
* [Authentication Guide](../../how-to/authentication/bearer-token-auth)


# Explore api
Source: https://docs.edenai.co/v3/how-to/discovery/explore-api



# Explore the API

Use V3's built-in API discovery endpoints to programmatically explore available features, providers, and schemas.

## Overview

V3 provides `/v3/info` endpoints that let you discover:

* Available features and subfeatures
* Available models and pricing for each feature
* Input/output schemas

**Base Endpoint:**

```
GET /v3/info
```

## List All Features

Get a complete list of available features:

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/info"
  headers = {"Authorization": "Bearer YOUR_API_KEY"}

  response = requests.get(url)
  data = response.json()

  for feature in data["features"]:
      subfeature_names = [sf["name"] for sf in feature["subfeatures"]]
      print(f"{feature['name']}: {subfeature_names}")
  ```

  ```bash cURL theme={null}
  curl https://api.edenai.run/v3/info \
  ```
</CodeGroup>

## Explore a Specific Feature

Get details about a feature category:

<CodeGroup>
  ```python Python theme={null}
  import requests
  # Get all text subfeatures
  url = "https://api.edenai.run/v3/info/text"
  response = requests.get(url)
  text_info = response.json()

  print("Available text subfeatures:")
  for subfeature in text_info["subfeatures"]:
      print(f"  - {subfeature['name']}: {subfeature['fullname']}")
  ```
</CodeGroup>

## Get Feature Details

Retrieve complete information about a specific feature:

<CodeGroup>
  ```python Python theme={null}
  import requests
  # Get details about content moderation
  url = "https://api.edenai.run/v3/info/text/moderation"
  headers = {"Authorization": "Bearer YOUR_API_KEY"}
  response = requests.get(url, headers=headers)
  feature_info = response.json()

  print("Feature: text/moderation")
  print(f"\nAvailable models: {feature_info['models']}")
  print(f"\nInput schema:")
  print(feature_info['input_schema'])
  print(f"\nOutput schema:")
  print(feature_info['output_schema'])
  ```
</CodeGroup>

### Response Example

```json theme={null}
{
  "feature": "text",
  "subfeature": "moderation",
  "description": "...",
  "mode": "sync",
  "endpoints": {"create": "POST /v3/universal-ai"},
  "input_schema": {
    "fields": [
      {
        "name": "text",
        "required": true,
        "description": "Text to moderate for harmful content",
        "type": "string"
      }
    ]
  },
  "output_schema": {
    "fields": [
      {"name": "nsfw_likelihood", "required": true, "type": "integer"},
      {"name": "items", "required": false, "type": "array"},
      {"name": "nsfw_likelihood_score", "required": true, "type": "float"}
    ]
  },
  "models": [
    {
      "model": "text/moderation/google",
      "pricing": {"price": 1.0, "price_unit_quantity": 1000, "price_unit_type": "request"}
    },
    {
      "model": "text/moderation/openai",
      "pricing": {"price": 0.5, "price_unit_quantity": 1000, "price_unit_type": "request"}
    }
  ]
}
```

## Check Available Models

List all available models for a specific feature, along with their pricing:

<CodeGroup>
  ```python Python theme={null}
  import requests
  def get_models_for_feature(feature, subfeature):
      """Get available models and pricing for a feature"""

      url = f"https://api.edenai.run/v3/info/{feature}/{subfeature}"

      response = requests.get(url)
      info = response.json()

      for entry in info["models"]:
          model = entry["model"]
          pricing = entry["pricing"]
          price = pricing["price"]
          unit_qty = pricing["price_unit_quantity"]
          unit_type = pricing["price_unit_type"]
          print(f"  {model}: ${price}/{unit_qty} {unit_type}s")

  # Usage
  print("OCR models:")
  get_models_for_feature("ocr", "ocr")
  ```
</CodeGroup>

## Validate Model Strings

Check if a model string is valid before making a request:

<CodeGroup>
  ```python Python theme={null}
  import requests
  def validate_model_string(model_string):
      """Validate model string format and availability"""

      # Parse model string
      parts = model_string.split('/')

      if len(parts) < 3:
          return {"valid": False, "error": "Invalid format"}

      feature = parts[0]
      subfeature = parts[1]

      # Check feature availability
      url = f"https://api.edenai.run/v3/info/{feature}/{subfeature}"

      try:
          response = requests.get(url)
          response.raise_for_status()
          info = response.json()

          # Check if the model string exists in available models
          available_models = [m["model"] for m in info["models"]]

          if model_string not in available_models:
              return {
                  "valid": False,
                  "error": f"Model '{model_string}' not available",
                  "available": available_models
              }

          return {"valid": True, "info": info}

      except Exception as e:
          return {"valid": False, "error": str(e)}

  # Usage
  result = validate_model_string("text/moderation/google")
  if result["valid"]:
      print("Model string is valid!")
  else:
      print(f"Invalid: {result['error']}")
  ```
</CodeGroup>

## Build Dynamic UIs

Use discovery to build dynamic feature selection:

<CodeGroup>
  ```python Python theme={null}
  import requests
  def build_feature_menu():
      """Build interactive feature selection menu"""

      # Get all features (includes models inline)
      url = "https://api.edenai.run/v3/info"
      response = requests.get(url)
      data = response.json()

      menu = {}

      for feature in data["features"]:
          feature_name = feature["name"]
          menu[feature_name] = {}

          for subfeature in feature["subfeatures"]:
              sf_name = subfeature["name"]
              # Extract unique providers from model strings
              providers = list({
                  m["model"].split("/")[2] for m in subfeature["models"]
              })
              menu[feature_name][sf_name] = providers

      return menu

  # Build menu
  menu = build_feature_menu()

  # Display
  for feature, subfeatures in menu.items():
      print(f"\n{feature.upper()}:")
      for subfeature, providers in subfeatures.items():
          print(f"  {subfeature}: {', '.join(providers)}")
  ```
</CodeGroup>

## Cache Discovery Results

Cache API info to reduce requests:

<CodeGroup>
  ```python Python theme={null}
  import json
  import requests
  from pathlib import Path
  from datetime import datetime, timedelta

  class APIDiscoveryCache:
      def __init__(self, cache_dir="api_cache", ttl_hours=24):
          self.cache_dir = Path(cache_dir)
          self.cache_dir.mkdir(exist_ok=True)
          self.ttl = timedelta(hours=ttl_hours)
          self.headers = {"Authorization": "Bearer YOUR_API_KEY"}
          
      def get_feature_info(self, feature, subfeature):
          """Get feature info with caching"""
              
          cache_key = f"{feature}_{subfeature}"
          cache_file = self.cache_dir / f"{cache_key}.json"
              
          # Check cache
          if cache_file.exists():
              data = json.loads(cache_file.read_text())
              cached_at = datetime.fromisoformat(data["cached_at"])
                  
              if datetime.now() - cached_at < self.ttl:
                  return data["info"]
              
          # Fetch from API
          url = f"https://api.edenai.run/v3/info/{feature}/{subfeature}"
          response = requests.get(url)
          info = response.json()
              
          # Cache result
          cache_data = {
              "info": info,
              "cached_at": datetime.now().isoformat()
          }
          cache_file.write_text(json.dumps(cache_data, indent=2))
              
          return info

  # Usage
  cache = APIDiscoveryCache()
  info = cache.get_feature_info("text", "moderation")
  ```
</CodeGroup>

## Next Steps

* [Universal AI Getting Started](../universal-ai/getting-started) - Use discovered features
* [Chat Completions Guide](../llm/chat-completions) - LLM endpoint


# Chat completions
Source: https://docs.edenai.co/v3/how-to/llm/chat-completions



# OpenAI-Compatible Chat Completions

Build conversational AI applications using Eden AI's OpenAI-compatible chat completions endpoint.

## Overview

Eden AI V3 provides full OpenAI API compatibility with multi-provider support. The endpoint follows OpenAI's exact format, making it a drop-in replacement.

**Endpoint:**

```
POST /v3/llm/chat/completions
```

**Note:** Streaming is optional. When enabled, responses are delivered via Server-Sent Events (SSE). See [Streaming Responses](./streaming) for streaming examples.

## Model Format

Use the simplified model string format for LLM:

```
provider/model
```

**Examples:**

* `openai/gpt-4`
* `anthropic/claude-sonnet-4-5`
* `google/gemini-2.5-flash`
* `cohere/command-r-plus`

## Basic Chat Completion

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "openai/gpt-4",
      "messages": [
          {"role": "user", "content": "Hello! How are you?"}
      ]
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  print(result["choices"][0]["message"]["content"])
  ```

  ```javascript JavaScript theme={null}
  const url = 'https://api.edenai.run/v3/llm/chat/completions';
  const headers = {
    'Authorization': 'Bearer YOUR_API_KEY',
    'Content-Type': 'application/json'
  };

  const payload = {
    model: 'openai/gpt-4',
    messages: [{role: 'user', content: 'Hello!'}]
  };

  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(payload)
  });

  const result = await response.json();
  console.log(result.choices[0].message.content);
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.edenai.run/v3/llm/chat/completions \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-4",
      "messages": [{"role": "user", "content": "Hello!"}]
    }'
  ```
</CodeGroup>

## Multi-Turn Conversations

Build conversations with message history:

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "anthropic/claude-sonnet-4-5",
      "messages": [
          {"role": "user", "content": "What is the capital of France?"},
          {"role": "assistant", "content": "The capital of France is Paris."},
          {"role": "user", "content": "What's the population?"}
      ]
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  print(result["choices"][0]["message"]["content"])
  ```
</CodeGroup>

## System Messages

Guide the model's behavior with system messages:

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "openai/gpt-4",
      "messages": [
          {
              "role": "system",
              "content": "You are a helpful assistant that speaks like a pirate."
          },
          {
              "role": "user",
              "content": "Tell me about artificial intelligence."
          }
      ]
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  print(result["choices"][0]["message"]["content"])
  ```
</CodeGroup>

## Temperature and Parameters

Control response creativity and behavior:

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "openai/gpt-4",
      "messages": [
          {"role": "user", "content": "Write a creative story about a robot."}
      ],
      "temperature": 0.9,  # Higher = more creative (0-2)
      "max_tokens": 500    # Limit response length
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  print(result["choices"][0]["message"]["content"])
  ```
</CodeGroup>

## Available Parameters

| Parameter           | Type    | Default  | Description                           |
| ------------------- | ------- | -------- | ------------------------------------- |
| `model`             | string  | Required | Model string (e.g., `openai/gpt-4`)   |
| `messages`          | array   | Required | Conversation messages                 |
| `stream`            | boolean | false    | Enable streaming (uses SSE when true) |
| `temperature`       | float   | 1.0      | Randomness (0-2)                      |
| `max_tokens`        | integer | -        | Maximum response tokens               |
| `top_p`             | float   | 1.0      | Nucleus sampling threshold            |
| `frequency_penalty` | float   | 0.0      | Penalize repeated tokens (-2 to 2)    |
| `presence_penalty`  | float   | 0.0      | Penalize topic repetition (-2 to 2)   |

## Response Format

Standard JSON response:

```json theme={null}
{
  "id": "chatcmpl-123",
  "object": "chat.completion",
  "created": 1677652288,
  "model": "gpt-4",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Hello! I'm doing well, thank you for asking."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 12,
    "completion_tokens": 15,
    "total_tokens": 27
  }
}
```

## Available Models

### OpenAI

* `openai/gpt-4`
* `openai/gpt-4-turbo`
* `openai/gpt-3.5-turbo`

### Anthropic

* `anthropic/claude-sonnet-4-5`
* `anthropic/claude-opus-4-5`
* `anthropic/claude-sonnet-4-5`

### Google

* `google/gemini-2.5-flash`
* `google/gemini-2.5-pro`

### Cohere

* `cohere/command-r-plus`
* `cohere/command-r`

### Meta

* `meta/llama-3-70b`
* `meta/llama-3-8b`

## OpenAI Python SDK Integration

Use Eden AI with the OpenAI SDK:

<CodeGroup>
  ```python Python theme={null}
  from openai import OpenAI

  # Point to Eden AI endpoint
  client = OpenAI(
      api_key="YOUR_EDEN_AI_API_KEY",
      base_url="https://api.edenai.run/v3/llm"
  )

  # Use any provider through OpenAI SDK
  response = client.chat.completions.create(
      model="anthropic/claude-sonnet-4-5",
      messages=[{"role": "user", "content": "Hello!"}]
  )

  print(response.choices[0].message.content)
  ```
</CodeGroup>

## Next Steps

* [Streaming Responses](./streaming) - Handle Server-Sent Events for real-time output
* [File Attachments](./file-attachments) - Send images and documents
* [Working with Media Files](./working-with-media) - Send images and files to LLMs


# File Attachments
Source: https://docs.edenai.co/v3/how-to/llm/file-attachments



Send documents, PDFs, and files to LLMs for analysis and processing.

## Overview

Eden AI V3 LLM endpoints support file attachments, enabling you to:

* Analyze PDF documents
* Process text files
* Extract data from structured documents
* Summarize reports and papers
* Answer questions about document content

File support varies by provider, with some supporting advanced document understanding and others focused on text extraction.

## Supported File Formats

| Format        | Extension | OpenAI | Anthropic | Google | Use Cases                    |
| ------------- | --------- | ------ | --------- | ------ | ---------------------------- |
| **PDF**       | .pdf      | ✓      | ✓         | ✓      | Reports, invoices, contracts |
| **Text**      | .txt      | ✓      | ✓         | ✓      | Logs, code, plain text       |
| **Word**      | .docx     | ✓      | ✓         | ✓      | Documents, reports           |
| **Rich Text** | .rtf      | -      | ✓         | -      | Formatted documents          |

## File Input Methods

V3 provides three ways to send files to LLMs:

### 1. File Upload (Recommended)

Upload files once, reference multiple times:

<CodeGroup>
  ```python Python theme={null}
  import requests

  # Step 1: Upload the file
  upload_url = "https://api.edenai.run/v3/upload"
  upload_headers = {"Authorization": "Bearer YOUR_API_KEY"}

  files = {"file": open("report.pdf", "rb")}
  data = {"purpose": "llm-analysis"}

  upload_response = requests.post(
      upload_url,
      headers=upload_headers,
      files=files,
      data=data
  )

  file_id = upload_response.json()["file_id"]
  print(f"Uploaded file ID: {file_id}")

  # Step 2: Use the file in LLM request
  llm_url = "https://api.edenai.run/v3/llm/chat/completions"
  llm_headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "openai/gpt-4o",
      "messages": [
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Summarize this document in 3 bullet points."
                  },
                  {
                      "type": "file",
                      "file": {"file_id": file_id}
                  }
              ]
          }
      ]
  }

  response = requests.post(llm_url, headers=llm_headers, json=payload)
  result = response.json()
  print(result["choices"][0]["message"]["content"])
  ```

  ```javascript JavaScript theme={null}
  // Step 1: Upload the file
  const uploadUrl = 'https://api.edenai.run/v3/upload';
  const formData = new FormData();
  formData.append('file', fileInput.files[0]);
  formData.append('purpose', 'llm-analysis');

  const uploadResponse = await fetch(uploadUrl, {
    method: 'POST',
    headers: {'Authorization': 'Bearer YOUR_API_KEY'},
    body: formData
  });

  const {file_id} = await uploadResponse.json();
  console.log('Uploaded file ID:', file_id);

  // Step 2: Use the file in LLM request
  const llmUrl = 'https://api.edenai.run/v3/llm/chat/completions';
  const payload = {
    model: 'openai/gpt-4o',
    messages: [
      {
        role: 'user',
        content: [
          {type: 'text', text: 'Summarize this document in 3 bullet points.'},
          {type: 'file', file: {file_id: file_id}}
        ]
      }
    ]
  };

  const response = await fetch(llmUrl, {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_API_KEY',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(payload)
  });

  const result = await response.json();
  console.log(result.choices[0].message.content);
  ```
</CodeGroup>

### 2. File URL

Use publicly accessible file URLs:

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "anthropic/claude-sonnet-4-5",
      "messages": [
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Extract all key findings from this research paper."
                  },
                  {
                      "type": "file",
                      "file": {
                          "file_id": "https://example.com/research-paper.pdf"
                      }
                  }
              ]
          }
      ]
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  print(result["choices"][0]["message"]["content"])
  ```
</CodeGroup>

### 3. Base64 File Data

Encode files directly in the request:

<CodeGroup>
  ```python Python theme={null}
  import base64
  import requests

  # Read and encode file
  with open("contract.pdf", "rb") as f:
      file_data = base64.b64encode(f.read()).decode('utf-8')

  # Create data URL
  data_url = f"data:application/pdf;base64,{file_data}"

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "google/gemini-2.5-flash",
      "messages": [
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Review this contract and highlight any concerning clauses."
                  },
                  {
                      "type": "file",
                      "file": {"file_data": data_url}
                  }
              ]
          }
      ]
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  print(result["choices"][0]["message"]["content"])
  ```
</CodeGroup>

## Common Use Cases

### Document Summarization

Extract key points from long documents:

<CodeGroup>
  ```python Python theme={null}
  import requests

  # Upload document
  upload_response = requests.post(
      "https://api.edenai.run/v3/upload",
      headers={"Authorization": "Bearer YOUR_API_KEY"},
      files={"file": open("quarterly-report.pdf", "rb")}
  )
  file_id = upload_response.json()["file_id"]

  # Request summary
  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "anthropic/claude-sonnet-4-5",
      "messages": [
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": """Provide a comprehensive summary with:
                      1. Executive summary (2-3 sentences)
                      2. Key metrics and numbers
                      3. Main highlights
                      4. Concerns or risks mentioned
                      5. Recommendations"""
                  },
                  {
                      "type": "file",
                      "file": {"file_id": file_id}
                  }
              ]
          }
      ],
      "max_tokens": 1500
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  print(result["choices"][0]["message"]["content"])
  ```
</CodeGroup>

### Question Answering on Documents

Ask specific questions about document content:

<CodeGroup>
  ```python Python theme={null}
  import requests

  # Upload document once
  upload_response = requests.post(
      "https://api.edenai.run/v3/upload",
      headers={"Authorization": "Bearer YOUR_API_KEY"},
      files={"file": open("policy-document.pdf", "rb")}
  )
  file_id = upload_response.json()["file_id"]

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  # Ask multiple questions about the same document
  questions = [
      "What is the refund policy?",
      "Are there any age restrictions?",
      "What payment methods are accepted?"
  ]

  for question in questions:
      payload = {
          "model": "openai/gpt-4o",
          "messages": [
              {
                  "role": "user",
                  "content": [
                      {"type": "text", "text": question},
                      {"type": "file", "file": {"file_id": file_id}}
                  ]
              }
          ],
          "temperature": 0.2  # Low for factual answers
      }

      print(f"\nQuestion: {question}")
      response = requests.post(url, headers=headers, json=payload)
      result = response.json()
      answer = result["choices"][0]["message"]["content"]

      print(f"Answer: {answer}\n")
  ```
</CodeGroup>

### Data Extraction

Extract structured data from documents:

<CodeGroup>
  ```python Python theme={null}
  import requests

  # Upload invoice
  upload_response = requests.post(
      "https://api.edenai.run/v3/upload",
      headers={"Authorization": "Bearer YOUR_API_KEY"},
      files={"file": open("invoice.pdf", "rb")}
  )
  file_id = upload_response.json()["file_id"]

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "openai/gpt-4o",
      "messages": [
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": """Extract the following from this invoice as JSON:
                      {
                        "invoice_number": "",
                        "date": "",
                        "vendor": "",
                        "total_amount": 0.0,
                        "currency": "",
                        "line_items": [
                          {"description": "", "quantity": 0, "unit_price": 0.0, "total": 0.0}
                        ],
                        "tax_amount": 0.0
                      }"""
                  },
                  {
                      "type": "file",
                      "file": {"file_id": file_id}
                  }
              ]
          }
      ],
      "temperature": 0.1  # Very low for accurate extraction
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  extracted_data = result["choices"][0]["message"]["content"]

  print(extracted_data)
  ```
</CodeGroup>

### Contract Analysis

Review legal documents and contracts:

<CodeGroup>
  ```python Python theme={null}
  import requests

  upload_response = requests.post(
      "https://api.edenai.run/v3/upload",
      headers={"Authorization": "Bearer YOUR_API_KEY"},
      files={"file": open("contract.pdf", "rb")}
  )
  file_id = upload_response.json()["file_id"]

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "anthropic/claude-opus-4-5",
      "messages": [
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": """Analyze this contract and provide:
                      1. Contract type and parties involved
                      2. Key terms and obligations
                      3. Payment terms and schedule
                      4. Termination clauses
                      5. Liability and indemnification
                      6. Potential risks or concerning clauses
                      7. Missing standard clauses
                      8. Overall assessment"""
                  },
                  {
                      "type": "file",
                      "file": {"file_id": file_id}
                  }
              ]
          }
      ],
      "max_tokens": 2000,
      "temperature": 0.3
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  print(result["choices"][0]["message"]["content"])
  ```
</CodeGroup>

### Code Review

Analyze code files and provide feedback:

<CodeGroup>
  ```python Python theme={null}
  import requests

  # Upload code file
  upload_response = requests.post(
      "https://api.edenai.run/v3/upload",
      headers={"Authorization": "Bearer YOUR_API_KEY"},
      files={"file": open("app.py", "rb")}
  )
  file_id = upload_response.json()["file_id"]

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "openai/gpt-4o",
      "messages": [
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": """Review this code and provide:
                      1. Code quality assessment
                      2. Potential bugs or issues
                      3. Security vulnerabilities
                      4. Performance improvements
                      5. Best practice violations
                      6. Suggested refactoring"""
                  },
                  {
                      "type": "file",
                      "file": {"file_id": file_id}
                  }
              ]
          }
      ],
      "max_tokens": 1500
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  print(result["choices"][0]["message"]["content"])
  ```
</CodeGroup>

## Provider Capabilities

### OpenAI (GPT-4o, GPT-4-turbo)

**Strengths:**

* Fast document processing
* Good for structured extraction
* Reliable with common formats
* Strong multi-page PDF handling

**Limitations:**

* Max file size: 512 MB
* Best for text-heavy documents

**Example:**

```
"model": "openai/gpt-4o"
```

### Anthropic (Claude 3 Family)

**Strengths:**

* Excellent reasoning about documents
* Superior for complex analysis
* Great for legal/technical documents
* Detailed, thoughtful responses

**Limitations:**

* Max file size: 10 MB (per file)
* Slightly slower than OpenAI

**Example:**

```
"model": "anthropic/claude-sonnet-4-5"
```

### Google (Gemini 1.5)

**Strengths:**

* Massive context window (2GB+ files)
* Best for very large documents
* Fast processing (Flash variant)
* Multi-document analysis

**Limitations:**

* May be less detailed on complex reasoning

**Example:**

```
"model": "google/gemini-2.5-pro"
```

## File Management Best Practices

### Upload Once, Use Multiple Times

Files uploaded to `/v3/upload` persist for 7 days:

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  # Upload once
  upload_response = requests.post(
      "https://api.edenai.run/v3/upload",
      headers={"Authorization": "Bearer YOUR_API_KEY"},
      files={"file": open("large-report.pdf", "rb")}
  )
  file_id = upload_response.json()["file_id"]

  # Use in multiple requests over the next 7 days
  questions = ["Summarize the key findings", "What are the recommendations?"]
  for question in questions:
      payload = {
          "model": "openai/gpt-4o",
          "messages": [
              {
                  "role": "user",
                  "content": [
                      {"type": "text", "text": question},
                      {"type": "file", "file": {"file_id": file_id}}
                  ]
              }
          ]
      }
      response = requests.post(url, headers=headers, json=payload)
      result = response.json()
      print(result["choices"][0]["message"]["content"])
  ```
</CodeGroup>

### File Size Optimization

For large files, consider preprocessing:

<CodeGroup>
  ```python Python theme={null}
  import requests
  from PyPDF2 import PdfReader, PdfWriter

  def extract_relevant_pages(input_pdf, pages_range):
      """Extract specific pages to reduce file size."""
      reader = PdfReader(input_pdf)
      writer = PdfWriter()

      for page_num in pages_range:
          writer.add_page(reader.pages[page_num])

      output_pdf = "extracted_pages.pdf"
      with open(output_pdf, "wb") as f:
          writer.write(f)

      return output_pdf

  # Extract only pages 1-5 from a 100-page document
  small_pdf = extract_relevant_pages("large-report.pdf", range(0, 5))

  # Upload the smaller file
  upload_response = requests.post(
      "https://api.edenai.run/v3/upload",
      headers={"Authorization": "Bearer YOUR_API_KEY"},
      files={"file": open(small_pdf, "rb")}
  )
  ```
</CodeGroup>

### Handling Expiration

Track and refresh expired files:

<CodeGroup>
  ```python Python theme={null}
  from datetime import datetime, timedelta
  import requests

  class FileManager:
      def __init__(self, api_key):
          self.api_key = api_key
          self.files = {}  # {local_path: {file_id, expires_at}}

      def get_file_id(self, local_path):
          """Get file ID, re-uploading if expired."""
          if local_path in self.files:
              file_info = self.files[local_path]
              expires_at = datetime.fromisoformat(file_info["expires_at"])

              if datetime.now() < expires_at:
                  return file_info["file_id"]

          # Upload new/expired file
          response = requests.post(
              "https://api.edenai.run/v3/upload",
              headers={"Authorization": f"Bearer {self.api_key}"},
              files={"file": open(local_path, "rb")}
          )
          result = response.json()

          self.files[local_path] = {
              "file_id": result["file_id"],
              "expires_at": result["expires_at"]
          }

          return result["file_id"]

  # Usage
  manager = FileManager("YOUR_API_KEY")
  file_id = manager.get_file_id("document.pdf")  # Handles re-upload if needed
  ```
</CodeGroup>

## Advanced Patterns

### Multi-Document Analysis

Analyze multiple documents together:

<CodeGroup>
  ```python Python theme={null}
  import requests

  # Upload multiple documents
  file_ids = []
  for doc in ["doc1.pdf", "doc2.pdf", "doc3.pdf"]:
      response = requests.post(
          "https://api.edenai.run/v3/upload",
          headers={"Authorization": "Bearer YOUR_API_KEY"},
          files={"file": open(doc, "rb")}
      )
      file_ids.append(response.json()["file_id"])

  # Analyze all together
  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "google/gemini-2.5-pro",  # Large context window
      "messages": [
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Compare these three documents and identify: 1) Common themes, 2) Discrepancies, 3) Unique points in each"
                  }
              ] + [
                  {"type": "file", "file": {"file_id": fid}}
                  for fid in file_ids
              ]
          }
      ],
      "max_tokens": 2000
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  print(result["choices"][0]["message"]["content"])
  ```
</CodeGroup>

### Conversational Document Analysis

Build multi-turn conversations about documents:

<CodeGroup>
  ```python Python theme={null}
  import requests

  # Upload document
  upload_response = requests.post(
      "https://api.edenai.run/v3/upload",
      headers={"Authorization": "Bearer YOUR_API_KEY"},
      files={"file": open("report.pdf", "rb")}
  )
  file_id = upload_response.json()["file_id"]

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  # Conversation history
  messages = [
      {
          "role": "user",
          "content": [
              {"type": "text", "text": "What are the main conclusions of this report?"},
              {"type": "file", "file": {"file_id": file_id}}
          ]
      }
  ]

  # First question
  response = requests.post(
      url,
      headers=headers,
      json={"model": "anthropic/claude-sonnet-4-5", "messages": messages}
  )

  # Collect assistant's response
  result = response.json()
  assistant_response = result["choices"][0]["message"]["content"]

  # Add to history
  messages.append({"role": "assistant", "content": assistant_response})

  # Follow-up question (no need to send file again)
  messages.append({
      "role": "user",
      "content": "What data supports these conclusions?"
  })

  # Second request uses conversation context
  response = requests.post(
      url,
      headers=headers,
      json={"model": "anthropic/claude-sonnet-4-5", "messages": messages}
  )
  result = response.json()
  print(result["choices"][0]["message"]["content"])
  ```
</CodeGroup>

## Error Handling

### Common File Errors

**File too large:**

```json theme={null}
{
  "error": {
    "code": "file_too_large",
    "message": "File size exceeds maximum allowed (512 MB for this provider)"
  }
}
```

**Unsupported format:**

```json theme={null}
{
  "error": {
    "code": "unsupported_file_type",
    "message": "File type .xlsx is not supported for this provider"
  }
}
```

**File not found:**

```json theme={null}
{
  "error": {
    "code": "file_not_found",
    "message": "File with ID 550e8400-e29b-41d4-a716-446655440000 not found or expired"
  }
}
```

### Robust Error Handling

<CodeGroup>
  ```python Python theme={null}
  import requests
  import os

  def process_document_safe(file_path, prompt):
      """Process document with comprehensive error handling."""
      # Check file exists
      if not os.path.exists(file_path):
          raise FileNotFoundError(f"File not found: {file_path}")

      # Check file size
      file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
      if file_size_mb > 500:
          raise ValueError(f"File too large: {file_size_mb:.1f} MB (max 500 MB)")

      try:
          # Upload
          upload_response = requests.post(
              "https://api.edenai.run/v3/upload",
              headers={"Authorization": "Bearer YOUR_API_KEY"},
              files={"file": open(file_path, "rb")},
              timeout=60
          )
          upload_response.raise_for_status()
          file_id = upload_response.json()["file_id"]

          # Process
          llm_response = requests.post(
              "https://api.edenai.run/v3/llm/chat/completions",
              headers={
                  "Authorization": "Bearer YOUR_API_KEY",
                  "Content-Type": "application/json"
              },
              json={
                  "model": "openai/gpt-4o",
                  "messages": [
                      {
                          "role": "user",
                          "content": [
                              {"type": "text", "text": prompt},
                              {"type": "file", "file": {"file_id": file_id}}
                          ]
                      }
                  ]
              },
              timeout=120
          )
          llm_response.raise_for_status()

          return llm_response.json()

      except requests.exceptions.Timeout:
          print("Request timeout. Try with a smaller file or simpler prompt.")
      except requests.exceptions.HTTPError as e:
          if e.response.status_code == 413:
              print("File too large for provider. Try splitting the document.")
          elif e.response.status_code == 422:
              print("Invalid file format:", e.response.json())
          else:
              print(f"HTTP error: {e}")
      except Exception as e:
          print(f"Unexpected error: {e}")

  # Usage
  response = process_document_safe("report.pdf", "Summarize this document")
  ```
</CodeGroup>

## Next Steps

* [Working with Media Files](./working-with-media) - Complete media guide
* [Vision Capabilities](./vision-capabilities) - Image analysis
* [Upload Files](../upload/upload-files) - File management
* [Chat Completions](./chat-completions) - Core LLM features
* [Streaming Responses](./streaming) - Handle SSE streams


# Provider comparison
Source: https://docs.edenai.co/v3/how-to/llm/provider-comparison



# Provider Comparison for Media Support

Compare multimodal capabilities across different LLM providers.

## Overview

This guide helps you choose the right provider for your multimodal use cases by comparing:

* Image format support
* File type compatibility
* Size limits
* Processing speed
* Accuracy and quality
* Cost effectiveness
* Special features

## Quick Comparison Matrix

### Image Support

| Provider      | Models                             | JPEG | PNG | WebP | GIF | Max Size | Base64 | URLs | Upload |
| ------------- | ---------------------------------- | ---- | --- | ---- | --- | -------- | ------ | ---- | ------ |
| **OpenAI**    | gpt-4o, gpt-4-turbo                | ✓    | ✓   | ✓    | ✓   | 20 MB    | ✓      | ✓    | ✓      |
| **Anthropic** | claude-opus-4-5, claude-sonnet-4-5 | ✓    | ✓   | ✓    | ✓   | 5 MB     | ✓      | ✓    | ✓      |
| **Google**    | gemini-2.5-pro, gemini-2.5-flash   | ✓    | ✓   | ✓    | ✓   | 20 MB    | ✓      | ✓    | ✓      |
| **Mistral**   | pixtral-12b                        | ✓    | ✓   | ✓    | -   | 10 MB    | ✓      | ✓    | ✓      |

### Document Support

| Provider      | Models                             | PDF | DOCX | TXT | Max Size | Max Pages | Best For              |
| ------------- | ---------------------------------- | --- | ---- | --- | -------- | --------- | --------------------- |
| **OpenAI**    | gpt-4o, gpt-4-turbo                | ✓   | ✓    | ✓   | 512 MB   | \~1000    | Structured extraction |
| **Anthropic** | claude-opus-4-5, claude-sonnet-4-5 | ✓   | ✓    | ✓   | 10 MB    | \~200     | Deep analysis         |
| **Google**    | gemini-2.5-pro, gemini-2.5-flash   | ✓   | ✓    | ✓   | 2 GB     | \~10000   | Large documents       |
| **Mistral**   | pixtral-12b                        | -   | -    | ✓   | -        | -         | Text only             |

## Detailed Provider Profiles

### OpenAI

**Models:**

* `openai/gpt-4o` (Recommended for multimodal)
* `openai/gpt-4-turbo`

**Strengths:**

* Fast processing (\~1-3s per image)
* Excellent general-purpose vision
* Strong multi-image support (up to 10 images)
* Reliable OCR and text extraction
* Good object detection
* Large file support (512 MB for documents)

**Limitations:**

* Image size limit: 20 MB
* May lack depth on complex reasoning tasks
* Higher cost for vision tasks

**Best Use Cases:**

* Real-time image analysis
* Multi-image comparisons
* Screenshot debugging
* General image understanding
* Large document processing

**Pricing (Approximate):**

* Images: \~\$0.0065 per image (1024×1024)
* Text: $0.01 per 1K tokens (input), $0.03 per 1K tokens (output)

**Example:**

<CodeGroup>
  ```python Python theme={null}
  payload = {
      "model": "openai/gpt-4o",
      "messages": [
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "Analyze this image"},
                  {
                      "type": "image_url",
                      "image_url": {"url": "https://example.com/image.jpg"}
                  }
              ]
          }
      ],
      "max_tokens": 500
  }
  ```
</CodeGroup>

***

### Anthropic (Claude 3)

**Models:**

* `anthropic/claude-sonnet-4-5` (Recommended)
* `anthropic/claude-opus-4-5` (Highest quality)
* `anthropic/claude-sonnet-4-5`

**Strengths:**

* Superior reasoning about visual content
* Excellent for document analysis
* Strong at complex visual tasks
* Detailed, thoughtful responses
* Great for academic/research content
* Multi-language support (100+ languages)
* Better at nuanced interpretation

**Limitations:**

* Image size limit: 5 MB (smaller than competitors)
* Document size limit: 10 MB
* Slightly slower processing
* Higher cost for Opus model

**Best Use Cases:**

* Legal document review
* Academic paper analysis
* Complex reasoning tasks
* Detailed image interpretation
* Multi-language documents
* Chart and diagram analysis

**Pricing (Approximate):**

* Sonnet: \$0.003 per image + text tokens
* Opus: \$0.015 per image + text tokens

**Example:**

<CodeGroup>
  ```python Python theme={null}
  payload = {
      "model": "anthropic/claude-sonnet-4-5",
      "messages": [
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Provide detailed analysis of this chart with insights"
                  },
                  {
                      "type": "image_url",
                      "image_url": {"url": "https://example.com/chart.png"}
                  }
              ]
          }
      ],
      "temperature": 0.3
  }
  ```
</CodeGroup>

***

### Google (Gemini 2.5)

**Models:**

* `google/gemini-2.5-pro` (Best quality)
* `google/gemini-2.5-flash` (Best value)

**Strengths:**

* Massive context window (up to 2 million tokens)
* Can handle very large documents (2GB+)
* Fast processing (Flash variant)
* Excellent multilingual support (100+ languages)
* Strong video frame analysis
* Best price/performance (Flash)
* Can process multiple large PDFs simultaneously

**Limitations:**

* May be less detailed on complex reasoning
* Beta features may have restrictions

**Best Use Cases:**

* Large document processing (100+ page PDFs)
* Multi-document analysis
* Video frame extraction and analysis
* High-volume applications
* Cost-sensitive projects
* Research with large datasets

**Pricing (Approximate):**

* Flash: Very low cost, \~\$0.001 per image
* Pro: Medium cost, \~\$0.004 per image

**Example:**

<CodeGroup>
  ```python Python theme={null}
  # Process a 200-page PDF
  payload = {
      "model": "google/gemini-2.5-pro",
      "messages": [
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Summarize this entire document and extract key findings"
                  },
                  {
                      "type": "file",
                      "file": {"file_id": "large_document_uuid"}
                  }
              ]
          }
      ],
      "max_tokens": 2000
  }
  ```
</CodeGroup>

***

### Mistral

**Models:**

* `mistral/pixtral-12b`

**Strengths:**

* European data residency
* Privacy-focused
* Good price/performance
* Fast processing
* GDPR compliant
* Lower latency in Europe

**Limitations:**

* No document (PDF/DOCX) support
* Only text and image inputs
* Smaller model (12B parameters)
* Limited advanced features

**Best Use Cases:**

* European compliance requirements
* Privacy-sensitive applications
* Cost-effective image analysis
* Basic vision tasks
* Text and image combination

**Pricing (Approximate):**

* Low cost, competitive with Flash

**Example:**

<CodeGroup>
  ```python Python theme={null}
  payload = {
      "model": "mistral/pixtral-12b",
      "messages": [
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "What objects are in this image?"},
                  {
                      "type": "image_url",
                      "image_url": {"url": "https://example.com/photo.jpg"}
                  }
              ]
          }
      ]
  }
  ```
</CodeGroup>

## Use Case Recommendations

### Real-Time Image Analysis

**Best Choice:** OpenAI GPT-4o

* Fastest processing
* Reliable results
* Good balance of speed and quality

### Legal Document Review

**Best Choice:** Anthropic Claude 3 Opus

* Superior reasoning
* Detailed analysis
* Excellent for complex documents

### Large PDF Processing (100+ pages)

**Best Choice:** Google Gemini 1.5 Pro

* Massive context window
* Can handle 2GB+ files
* Cost-effective for large docs

### Multi-Document Analysis

**Best Choice:** Google Gemini 1.5 Pro

* Best context window
* Can process multiple files
* Maintains context across documents

### Screenshot Debugging

**Best Choice:** OpenAI GPT-4o

* Fast turnaround
* Good at UI understanding
* Strong text extraction

### Chart and Graph Analysis

**Best Choice:** Anthropic Claude 3.5 Sonnet

* Best reasoning
* Detailed insights
* Accurate data interpretation

### High-Volume Processing

**Best Choice:** Google Gemini 1.5 Flash

* Lowest cost
* Fast processing
* Good quality for price

### Privacy-Sensitive Applications

**Best Choice:** Mistral Pixtral

* European data residency
* GDPR compliant
* Privacy-focused

### Invoice/Receipt Extraction

**Best Choice:** OpenAI GPT-4o

* Fast and accurate
* Good structured extraction
* Reliable OCR

### Academic Paper Analysis

**Best Choice:** Anthropic Claude 3 Opus

* Deep understanding
* Detailed analysis
* Good with technical content

## Feature Comparison

### Multi-Image Support

| Provider      | Max Images | Performance | Best For                |
| ------------- | ---------- | ----------- | ----------------------- |
| **OpenAI**    | 10+        | Excellent   | Comparisons, sequences  |
| **Anthropic** | 20+        | Very Good   | Analysis, documentation |
| **Google**    | 50+        | Excellent   | Large collections       |
| **Mistral**   | Multiple   | Good        | Basic comparisons       |

### Language Support

| Provider      | Languages | Multilingual Quality |
| ------------- | --------- | -------------------- |
| **OpenAI**    | 50+       | Very Good            |
| **Anthropic** | 100+      | Excellent            |
| **Google**    | 100+      | Excellent            |
| **Mistral**   | 50+       | Good                 |

### OCR Accuracy

| Provider      | Handwriting | Printed Text | Complex Layouts |
| ------------- | ----------- | ------------ | --------------- |
| **OpenAI**    | Good        | Excellent    | Very Good       |
| **Anthropic** | Very Good   | Excellent    | Excellent       |
| **Google**    | Very Good   | Excellent    | Very Good       |
| **Mistral**   | Good        | Good         | Good            |

## Cost Optimization Strategies

### Choose Based on Task Complexity

**Simple tasks (object detection, basic OCR):**

```
# Use Gemini Flash or Mistral
"model": "google/gemini-2.5-flash"  # Cheapest
```

**Medium complexity (chart analysis, multi-image):**

```
# Use GPT-4o or Claude Sonnet
"model": "openai/gpt-4o"  # Balanced
```

**Complex reasoning (legal docs, deep analysis):**

```
# Use Claude Opus
"model": "anthropic/claude-opus-4-5"  # Best quality
```

### Optimize Input Size

<CodeGroup>
  ```python Python theme={null}
  import os
  import io
  from PIL import Image

  def optimize_image(image_path, max_size_mb=5):
      """Resize image to fit under size limit."""
      img = Image.open(image_path)

      # Calculate target size
      current_size = os.path.getsize(image_path) / (1024 * 1024)
      if current_size <= max_size_mb:
          return image_path

      # Reduce quality
      output = io.BytesIO()
      quality = int(85 * (max_size_mb / current_size))
      img.save(output, format='JPEG', quality=quality, optimize=True)

      return output.getvalue()
  ```
</CodeGroup>

### Batch Processing

Process multiple items in fewer requests:

<CodeGroup>
  ```python Python theme={null}
  # Instead of multiple requests
  # Send all images in one request (if provider supports)
  image_urls = ["https://example.com/image1.jpg", "https://example.com/image2.jpg"]

  payload = {
      "model": "google/gemini-2.5-pro",
      "messages": [
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "Analyze all these images"},
              ] + [
                  {"type": "image_url", "image_url": {"url": url}}
                  for url in image_urls
              ]
          }
      ]
  }
  ```
</CodeGroup>

## Performance Benchmarks

### Average Response Times (Image Analysis)

| Provider  | Model             | Small Image (1MB) | Large Image (10MB) |
| --------- | ----------------- | ----------------- | ------------------ |
| OpenAI    | gpt-4o            | \~1.5s            | \~2.5s             |
| Anthropic | claude-sonnet-4-5 | \~2.0s            | \~3.5s             |
| Google    | gemini-2.5-flash  | \~1.0s            | \~2.0s             |
| Google    | gemini-2.5-pro    | \~2.0s            | \~3.0s             |
| Mistral   | pixtral-12b       | \~1.5s            | \~2.5s             |

### Document Processing (PDF)

| Provider  | Model           | 10-page PDF | 100-page PDF    |
| --------- | --------------- | ----------- | --------------- |
| OpenAI    | gpt-4o          | \~5s        | \~30s           |
| Anthropic | claude-opus-4-5 | \~8s        | Not recommended |
| Google    | gemini-2.5-pro  | \~6s        | \~45s           |

*Times are approximate and vary based on content complexity and network conditions.*

## Choosing the Right Provider

### Decision Tree

```
Does your use case involve:

├─ Large documents (100+ pages)?
│  └─ Use: Google Gemini 1.5 Pro
│
├─ Privacy/GDPR requirements?
│  └─ Use: Mistral Pixtral
│
├─ Complex reasoning needed?
│  ├─ Legal/academic?
│  │  └─ Use: Anthropic Claude 3 Opus
│  └─ General analysis?
│     └─ Use: Anthropic Claude 3.5 Sonnet
│
├─ High-volume/cost-sensitive?
│  └─ Use: Google Gemini 1.5 Flash
│
└─ General purpose, fast?
   └─ Use: OpenAI GPT-4o
```

## Provider Availability

Check current provider status:

<CodeGroup>
  ```python Python theme={null}
  import requests

  def check_provider_availability():
      """Check which providers are currently available."""
      url = "https://api.edenai.run/v3/llm/models"
      headers = {"Authorization": "Bearer YOUR_API_KEY"}

      response = requests.get(url, headers=headers)
      models = response.json()

      multimodal_models = [
          model for model in models.get("data", [])
          if any(cap in model.get("capabilities", [])
                 for cap in ["vision", "image", "file"])
      ]

      return multimodal_models

  # Usage
  available = check_provider_availability()
  for model in available:
      print(f"{model['id']}: {model.get('capabilities', [])}")
  ```
</CodeGroup>

## Next Steps

* [Working with Media Files](./working-with-media) - Implementation guide
* [Vision Capabilities](./vision-capabilities) - Vision features
* [File Attachments](./file-attachments) - Document processing
* [Monitor Costs](../cost-management/monitor-usage) - Track spending
* [Chat Completions](./chat-completions) - Core LLM features


# Smart routing
Source: https://docs.edenai.co/v3/how-to/llm/smart-routing



# LLM Smart Routing Patterns

Learn practical patterns for implementing smart routing with LLMs in production applications using Eden AI's dynamic model selection.

## Overview

This guide provides LLM-specific patterns and examples for smart routing. For comprehensive router documentation, see the [Smart Routing section](../router/getting-started).

**What you'll learn:**

* LLM-specific routing patterns
* Customizing model candidates for LLM use cases
* Combining smart routing with function calling and streaming
* Practical code examples for common scenarios
* Cost optimization strategies for LLM workloads

**Related documentation:**

* **[Router Getting Started](../router/getting-started)** - Core routing concepts and basics
* **[Router Advanced Usage](../router/advanced-usage)** - Advanced patterns and optimization

## Basic Implementation Patterns

### Pattern 1: Default Smart Routing

Let the system choose from all available models:

<CodeGroup>
  ```python Python theme={null}
  import requests

  def chat_with_smart_routing(message: str) -> str:
      """Simple chat with automatic model selection."""
      url = "https://api.edenai.run/v3/llm/chat/completions"
      headers = {
          "Authorization": f"Bearer {API_KEY}",
          "Content-Type": "application/json"
      }

      payload = {
          "model": "@edenai",  # Automatic routing
          "messages": [{"role": "user", "content": message}]
      }

      response = requests.post(url, headers=headers, json=payload)
      data = response.json()

      return data['choices'][0]['message']['content']

  # Usage
  response = chat_with_smart_routing("Explain machine learning")
  print(response)
  ```

  ```javascript JavaScript theme={null}
  async function chatWithSmartRouting(message) {
    const url = 'https://api.edenai.run/v3/llm/chat/completions';
    const headers = {
      'Authorization': `Bearer ${API_KEY}`,
      'Content-Type': 'application/json'
    };

    const payload = {
      model: '@edenai',
      messages: [{role: 'user', content: message}]
    };

    const response = await fetch(url, {
      method: 'POST',
      headers: headers,
      body: JSON.stringify(payload)
    });

    const data = await response.json();

    return data.choices[0].message.content;
  }

  // Usage
  const response = await chatWithSmartRouting('Explain machine learning');
  console.log(response);
  ```
</CodeGroup>

### Pattern 2: Custom Candidate Pool

Define specific models for your use case:

<CodeGroup>
  ```python Python theme={null}
  import requests

  def chat_with_custom_candidates(
      message: str,
      use_case: str = "general"
  ) -> str:
      """Chat with use-case-specific model candidates."""

      # Define candidate pools for different use cases
      CANDIDATE_POOLS = {
          "code": [
              "openai/gpt-4o",
              "anthropic/claude-sonnet-4-5",
          ],
          "creative": [
              "anthropic/claude-opus-4-5",
              "openai/gpt-4o",
              "google/gemini-2.5-pro",
          ],
          "fast": [
              "openai/gpt-4o-mini",
              "google/gemini-2.5-flash",
              "openai/gpt-4",
          ],
          "general": [
              "openai/gpt-4o",
              "anthropic/claude-sonnet-4-5",
              "google/gemini-2.5-flash",
          ]
      }

      url = "https://api.edenai.run/v3/llm/chat/completions"
      headers = {
          "Authorization": f"Bearer {API_KEY}",
          "Content-Type": "application/json"
      }

      payload = {
          "model": "@edenai",
          "router_candidates": CANDIDATE_POOLS.get(use_case, CANDIDATE_POOLS["general"]),
          "messages": [{"role": "user", "content": message}]
      }

      response = requests.post(url, headers=headers, json=payload)
      data = response.json()

      return data['choices'][0]['message']['content']

  # Usage examples
  code_response = chat_with_custom_candidates(
      "Write a Python function to merge two sorted lists",
      use_case="code"
  )

  creative_response = chat_with_custom_candidates(
      "Write a short story about a robot",
      use_case="creative"
  )

  fast_response = chat_with_custom_candidates(
      "What's the capital of France?",
      use_case="fast"
  )
  ```
</CodeGroup>

### Pattern 3: OpenAI SDK Integration

Use smart routing with the official OpenAI SDK:

<CodeGroup>
  ```python Python (OpenAI SDK) theme={null}
  from openai import OpenAI

  client = OpenAI(
      api_key="YOUR_API_KEY",
      base_url="https://api.edenai.run/v3/llm"
  )

  def chat_with_openai_sdk(message: str, candidates: list[str] = None):
      """Use smart routing with OpenAI SDK."""

      extra_params = {}
      if candidates:
          extra_params["router_candidates"] = candidates

      response = client.chat.completions.create(
          model="@edenai",
          messages=[
              {"role": "user", "content": message}
          ],
          extra_body=extra_params  # Pass router_candidates here
      )

      selected_model = response.model
      print(f"Router selected: {selected_model}")

      full_response = response.choices[0].message.content
      print(full_response)

      return full_response, selected_model

  # Usage
  response, model = chat_with_openai_sdk(
      "Explain neural networks",
      candidates=["openai/gpt-4o", "anthropic/claude-sonnet-4-5"]
  )
  print(f"\nModel used: {model}")
  ```

  ```typescript TypeScript (OpenAI SDK) theme={null}
  import OpenAI from 'openai';

  const client = new OpenAI({
    apiKey: process.env.EDEN_AI_API_KEY,
    baseURL: 'https://api.edenai.run/v3/llm'
  });

  async function chatWithOpenAISDK(
    message: string,
    candidates?: string[]
  ): Promise<{response: string, model: string}> {

    const extraBody = candidates ? { router_candidates: candidates } : {};

    const completion = await client.chat.completions.create({
      model: '@edenai',
      messages: [{role: 'user', content: message}],
      // @ts-ignore - extra_body not in types
      extra_body: extraBody
    });

    const selectedModel = completion.model;
    console.log(`Router selected: ${selectedModel}`);

    const fullResponse = completion.choices[0]?.message?.content || '';
    console.log(fullResponse);

    return {response: fullResponse, model: selectedModel};
  }

  // Usage
  const {response, model} = await chatWithOpenAISDK(
    'Explain neural networks',
    ['openai/gpt-4o', 'anthropic/claude-sonnet-4-5']
  );
  console.log(`\nModel used: ${model}`);
  ```
</CodeGroup>

## Advanced Patterns

### Pattern 4: Smart Routing with Function Calling

Combine smart routing with function/tool calling:

<CodeGroup>
  ```python Python theme={null}
  import requests
  import json

  def chat_with_tools(message: str, tools: list):
      """Smart routing with function calling."""

      url = "https://api.edenai.run/v3/llm/chat/completions"
      headers = {
          "Authorization": f"Bearer {API_KEY}",
          "Content-Type": "application/json"
      }

      payload = {
          "model": "@edenai",
          # Choose models good at function calling
          "router_candidates": [
              "openai/gpt-4o",
              "anthropic/claude-sonnet-4-5",
              "google/gemini-2.5-flash"
          ],
          "messages": [{"role": "user", "content": message}],
          "tools": tools  # Router considers tool compatibility
      }

      response = requests.post(url, headers=headers, json=payload)
      data = response.json()

      message_data = data.get('choices', [{}])[0].get('message', {})
      tool_calls = message_data.get('tool_calls', [])
      full_response = message_data.get('content', '')

      return {
          "response": full_response,
          "tool_calls": tool_calls
      }

  # Define tools
  tools = [
      {
          "type": "function",
          "function": {
              "name": "get_weather",
              "description": "Get current weather for a location",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "location": {
                          "type": "string",
                          "description": "City name"
                      }
                  },
                  "required": ["location"]
              }
          }
      }
  ]

  # Usage
  result = chat_with_tools(
      "What's the weather like in Paris?",
      tools=tools
  )
  print(f"Response: {result['response']}")
  print(f"Tool calls: {result['tool_calls']}")
  ```
</CodeGroup>

### Pattern 5: Cost-Optimized Routing with Budget Constraints

Optimize costs by limiting to budget-friendly models:

<CodeGroup>
  ```python Python theme={null}
  import requests

  class CostOptimizedRouter:
      """Smart routing with cost optimization."""

      # Model tiers by cost
      BUDGET_MODELS = [
          "openai/gpt-4o-mini",
          "google/gemini-2.5-flash",
          "openai/gpt-4",
      ]

      BALANCED_MODELS = [
          "openai/gpt-4o",
          "anthropic/claude-sonnet-4-5",
          "google/gemini-2.5-flash",
      ]

      PREMIUM_MODELS = [
          "anthropic/claude-opus-4-5",
          "openai/gpt-4o",
          "google/gemini-2.5-pro",
      ]

      def __init__(self, api_key: str, cost_tier: str = "balanced"):
          self.api_key = api_key
          self.cost_tier = cost_tier

      def get_candidates(self) -> list[str]:
          """Get candidates based on cost tier."""
          if self.cost_tier == "budget":
              return self.BUDGET_MODELS
          elif self.cost_tier == "premium":
              return self.PREMIUM_MODELS
          else:
              return self.BALANCED_MODELS

      def chat(self, message: str) -> tuple[str, float]:
          """Chat and return response with estimated cost."""

          url = "https://api.edenai.run/v3/llm/chat/completions"
          headers = {
              "Authorization": f"Bearer {self.api_key}",
              "Content-Type": "application/json"
          }

          payload = {
              "model": "@edenai",
              "router_candidates": self.get_candidates(),
              "messages": [{"role": "user", "content": message}]
          }

          response = requests.post(url, headers=headers, json=payload)
          data = response.json()

          selected_model = data.get('model')
          print(f"Router selected: {selected_model} ({self.cost_tier} tier)")

          full_response = data.get('choices', [{}])[0].get('message', {}).get('content', '')

          # You could track actual cost from response metadata
          estimated_cost = 0.001  # Placeholder

          return full_response, estimated_cost

  # Usage examples
  budget_router = CostOptimizedRouter(API_KEY, cost_tier="budget")
  response, cost = budget_router.chat("Summarize this article")
  print(f"Cost: ${cost:.4f}")

  premium_router = CostOptimizedRouter(API_KEY, cost_tier="premium")
  response, cost = premium_router.chat("Write a comprehensive analysis")
  print(f"Cost: ${cost:.4f}")
  ```
</CodeGroup>

### Pattern 6: Multi-Turn Conversations with Context

Maintain conversation context with smart routing:

<CodeGroup>
  ```python Python theme={null}
  import requests
  import json

  class SmartRoutingChatSession:
      """Maintain conversation with smart routing."""

      def __init__(self, api_key: str, candidates: list[str] = None):
          self.api_key = api_key
          self.candidates = candidates
          self.messages = []
          self.selected_models = []  # Track model selection per turn

      def send_message(self, content: str) -> str:
          """Send a message and get response."""

          # Add user message to history
          self.messages.append({"role": "user", "content": content})

          url = "https://api.edenai.run/v3/llm/chat/completions"
          headers = {
              "Authorization": f"Bearer {self.api_key}",
              "Content-Type": "application/json"
          }

          payload = {
              "model": "@edenai",
              "messages": self.messages  # Include full conversation
          }

          if self.candidates:
              payload["router_candidates"] = self.candidates

          response = requests.post(url, headers=headers, json=payload)
          data = response.json()

          selected_model = data.get('model')
          assistant_response = data.get('choices', [{}])[0].get('message', {}).get('content', '')

          # Add assistant response to history
          self.messages.append({"role": "assistant", "content": assistant_response})
          self.selected_models.append(selected_model)

          return assistant_response

      def get_conversation_summary(self) -> dict:
          """Get conversation statistics."""
          return {
              "turns": len(self.messages) // 2,
              "models_used": self.selected_models,
              "total_messages": len(self.messages)
          }

  # Usage
  session = SmartRoutingChatSession(
      API_KEY,
      candidates=["openai/gpt-4o", "anthropic/claude-sonnet-4-5"]
  )

  # Multi-turn conversation
  response1 = session.send_message("What is Python?")
  print(f"Assistant: {response1}\n")

  response2 = session.send_message("Can you give me a code example?")
  print(f"Assistant: {response2}\n")

  response3 = session.send_message("Explain that example in detail")
  print(f"Assistant: {response3}\n")

  # Summary
  summary = session.get_conversation_summary()
  print(f"\nConversation summary: {summary}")
  ```
</CodeGroup>

## Monitoring and Debugging

### Tracking Routing Decisions

Monitor which models are selected:

<CodeGroup>
  ```python Python theme={null}
  import requests
  import json
  from collections import defaultdict
  from datetime import datetime

  class RoutingMonitor:
      """Track and analyze routing decisions."""

      def __init__(self, api_key: str):
          self.api_key = api_key
          self.routing_history = []

      def chat_with_tracking(
          self,
          message: str,
          candidates: list[str] = None
      ) -> dict:
          """Chat and track routing decision."""

          start_time = datetime.now()

          url = "https://api.edenai.run/v3/llm/chat/completions"
          headers = {
              "Authorization": f"Bearer {self.api_key}",
              "Content-Type": "application/json"
          }

          payload = {
              "model": "@edenai",
              "messages": [{"role": "user", "content": message}]
          }

          if candidates:
              payload["router_candidates"] = candidates

          response = requests.post(url, headers=headers, json=payload)
          first_chunk_time = datetime.now()
          data = response.json()

          selected_model = data.get('model')
          full_response = data.get('choices', [{}])[0].get('message', {}).get('content', '')

          end_time = datetime.now()

          # Record routing decision
          routing_info = {
              "timestamp": start_time.isoformat(),
              "message": message[:50],  # Truncate for logging
              "selected_model": selected_model,
              "candidates": candidates or "default",
              "routing_latency_ms": (first_chunk_time - start_time).total_seconds() * 1000 if first_chunk_time else None,
              "total_latency_ms": (end_time - start_time).total_seconds() * 1000,
              "response_length": len(full_response)
          }

          self.routing_history.append(routing_info)

          return {
              "response": full_response,
              "routing_info": routing_info
          }

      def get_statistics(self) -> dict:
          """Get routing statistics."""
          if not self.routing_history:
              return {"error": "No routing history"}

          model_counts = defaultdict(int)
          total_routing_latency = 0
          total_latency = 0

          for entry in self.routing_history:
              model_counts[entry["selected_model"]] += 1
              if entry["routing_latency_ms"]:
                  total_routing_latency += entry["routing_latency_ms"]
              total_latency += entry["total_latency_ms"]

          return {
              "total_requests": len(self.routing_history),
              "model_distribution": dict(model_counts),
              "avg_routing_latency_ms": total_routing_latency / len(self.routing_history),
              "avg_total_latency_ms": total_latency / len(self.routing_history),
              "most_selected_model": max(model_counts, key=model_counts.get)
          }

  # Usage
  monitor = RoutingMonitor(API_KEY)

  # Make several requests
  for query in [
      "What is machine learning?",
      "Write a Python function to sort",
      "Explain quantum physics",
      "Tell me a joke"
  ]:
      result = monitor.chat_with_tracking(
          query,
          candidates=["openai/gpt-4o", "anthropic/claude-sonnet-4-5", "google/gemini-2.5-flash"]
      )
      print(f"Q: {query}")
      print(f"Model: {result['routing_info']['selected_model']}")
      print(f"Routing latency: {result['routing_info']['routing_latency_ms']:.0f}ms\n")

  # Get statistics
  stats = monitor.get_statistics()
  print("\n=== Routing Statistics ===")
  print(f"Total requests: {stats['total_requests']}")
  print(f"Model distribution: {stats['model_distribution']}")
  print(f"Average routing latency: {stats['avg_routing_latency_ms']:.0f}ms")
  print(f"Most selected: {stats['most_selected_model']}")
  ```
</CodeGroup>

## Error Handling

### Robust Error Handling with Fallbacks

<CodeGroup>
  ```python Python theme={null}
  import requests
  import json
  from typing import Optional

  def chat_with_fallback(
      message: str,
      primary_candidates: list[str],
      fallback_model: str = "openai/gpt-4o"
  ) -> dict:
      """Chat with smart routing and fallback to fixed model on error."""

      url = "https://api.edenai.run/v3/llm/chat/completions"
      headers = {
          "Authorization": f"Bearer {API_KEY}",
          "Content-Type": "application/json"
      }

      # Try smart routing first
      try:
          payload = {
              "model": "@edenai",
              "router_candidates": primary_candidates,
              "messages": [{"role": "user", "content": message}]
          }

          response = requests.post(url, headers=headers, json=payload, timeout=30)
          response.raise_for_status()

          data = response.json()
          full_response = data.get('choices', [{}])[0].get('message', {}).get('content', '')

          return {
              "response": full_response,
              "method": "smart_routing",
              "success": True
          }

      except Exception as e:
          print(f"Smart routing failed: {e}")
          print(f"Falling back to {fallback_model}")

          # Fallback to fixed model
          try:
              payload = {
                  "model": fallback_model,
                  "messages": [{"role": "user", "content": message}]
              }

              response = requests.post(url, headers=headers, json=payload, timeout=30)
              response.raise_for_status()

              data = response.json()
              full_response = data.get('choices', [{}])[0].get('message', {}).get('content', '')

              return {
                  "response": full_response,
                  "method": "fallback",
                  "fallback_model": fallback_model,
                  "success": True,
                  "original_error": str(e)
              }

          except Exception as fallback_error:
              return {
                  "response": None,
                  "method": "failed",
                  "success": False,
                  "error": str(fallback_error)
              }

  # Usage
  result = chat_with_fallback(
      "Explain neural networks",
      primary_candidates=["openai/gpt-4o", "anthropic/claude-sonnet-4-5"]
  )

  if result["success"]:
      print(f"Response (via {result['method']}): {result['response']}")
  else:
      print(f"Failed: {result['error']}")
  ```
</CodeGroup>

## Best Practices

### 1. Choose Appropriate Candidates

✅ **Do:**

* Limit to 3-5 models per use case
* Choose models with similar capabilities
* Include at least one fast/cheap model for cost efficiency
* Test candidate pools with your specific workload

❌ **Don't:**

* Include 20+ candidates (slows routing decision)
* Mix specialized models (e.g., code + creative)
* Use models you haven't tested

### 2. Monitor Performance

✅ **Do:**

* Track routing latency in production
* Monitor model distribution
* Alert on routing failures
* A/B test smart routing vs. fixed models

❌ **Don't:**

* Deploy without monitoring
* Ignore routing patterns
* Assume routing is always optimal

### 3. Cost Optimization

✅ **Do:**

* Define cost tiers (budget/balanced/premium)
* Route simple queries to cheaper models
* Track actual spend per use case
* Review routing decisions regularly

❌ **Don't:**

* Use premium-only candidates for simple tasks
* Ignore cost metrics
* Assume routing always chooses cheapest

### 4. Error Handling

✅ **Do:**

* Implement fallback to fixed models
* Set appropriate timeouts
* Log routing failures
* Handle network errors gracefully

❌ **Don't:**

* Rely solely on smart routing without fallback
* Use infinite timeouts
* Ignore routing errors

## Performance Considerations

### Latency

* **Routing overhead:** 100-500ms
* **First token:** Includes routing time
* **Subsequent tokens:** No overhead

**When to avoid:**

* Real-time chat with \<500ms requirements
* High-frequency API calls (>100/sec)
* Strict SLA requirements

### Caching

* **Routing decisions:** Not cached (context-dependent)
* **Model list:** Cached (1 hour TTL)
* **API responses:** Not cached by router

## Common Patterns Summary

| Use Case             | Recommended Candidates                          | Notes                 |
| -------------------- | ----------------------------------------------- | --------------------- |
| **General chat**     | gpt-4o, claude-sonnet-4-5, gemini-2.5-flash     | Balanced quality/cost |
| **Code generation**  | gpt-4o, claude-sonnet-4-5                       | Strong coding models  |
| **Creative writing** | claude-opus-4-5, gpt-4o, gemini-2.5-pro         | Premium models        |
| **Simple Q\&A**      | gpt-4o-mini, gemini-2.5-flash, claude-haiku-4-5 | Fast and cheap        |
| **Function calling** | gpt-4o, claude-sonnet-4-5, gemini-2.5-flash     | Tool-compatible       |

## Next Steps

* **[Router Getting Started](../router/getting-started)** - Learn core routing concepts
* **[Router Advanced Usage](../router/advanced-usage)** - Master advanced routing patterns
* **[Optimize LLM Costs Tutorial](../../tutorials/optimize-llm-costs)** - Complete cost optimization workflow
* **[Chat Completions Guide](./chat-completions)** - Master the LLM endpoint
* **[Streaming Guide](./streaming)** - Handle SSE responses

## Troubleshooting

### Issue: Routing always selects the same model

**Possible causes:**

* Candidates list too restrictive
* Request pattern favors one model
* Other models unavailable

**Solutions:**

* Expand candidate pool
* Check model availability
* Review request characteristics

### Issue: High routing latency (>1s)

**Possible causes:**

* Network issues
* Large candidate pool
* Router API congestion

**Solutions:**

* Reduce candidates to 3-5 models
* Check network connectivity
* Consider fixed models for latency-critical apps

### Issue: Unexpected costs

**Possible causes:**

* Router selecting premium models
* High volume of requests
* Long responses

**Solutions:**

* Use budget-tier candidates
* Limit max\_tokens
* Monitor model distribution
* Implement cost alerts


# Streaming
Source: https://docs.edenai.co/v3/how-to/llm/streaming



# Streaming Responses with Server-Sent Events

Learn how to handle streaming responses from the V3 LLM endpoint using Server-Sent Events (SSE).

## Overview

When streaming is enabled in V3, LLM responses are delivered via Server-Sent Events (SSE), providing real-time token-by-token output. Streaming is optional - you can also use V3 with non-streaming requests.

**Benefits:**

* Immediate response feedback
* Better user experience with progressive display
* Lower perceived latency

## Server-Sent Events Format

SSE responses follow this pattern:

```
data: {JSON_CHUNK}

data: {JSON_CHUNK}

data: [DONE]
```

Each line starts with `data: ` followed by JSON or the `[DONE]` marker.

## Parsing Streaming Responses

### Python with requests

<CodeGroup>
  ```python Python theme={null}
  import requests
  import json

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "openai/gpt-4",
      "messages": [{"role": "user", "content": "Tell me a short story"}],
      "stream": True
  }

  response = requests.post(url, headers=headers, json=payload, stream=True)

  full_content = ""

  for line in response.iter_lines():
      if line:
          line_str = line.decode('utf-8')
              
          # Skip empty lines and non-data lines
          if not line_str.startswith('data: '):
              continue
              
          # Extract data after 'data: ' prefix
          data = line_str[6:]
              
          # Check for end of stream
          if data == '[DONE]':
              break
              
          # Parse JSON chunk
          try:
              chunk = json.loads(data)
              delta = chunk['choices'][0]['delta']
                  
              if 'content' in delta:
                  content = delta['content']
                  full_content += content
                  print(content, end='', flush=True)
                      
          except json.JSONDecodeError:
              continue

  print(f"\n\nFull response: {full_content}")
  ```
</CodeGroup>

### JavaScript with Fetch API

<CodeGroup>
  ```javascript JavaScript theme={null}
  const url = 'https://api.edenai.run/v3/llm/chat/completions';
  const headers = {
    'Authorization': 'Bearer YOUR_API_KEY',
    'Content-Type': 'application/json'
  };

  const payload = {
    model: 'openai/gpt-4',
    messages: [{role: 'user', content: 'Tell me a short story'}],
    stream: true
  };

  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(payload)
  });

  const reader = response.body.getReader();
  const decoder = new TextDecoder();
  let buffer = '';

  while (true) {
    const {done, value} = await reader.read();
    if (done) break;

    buffer += decoder.decode(value, {stream: true});
    const lines = buffer.split('\n');
    buffer = lines.pop(); // Keep incomplete line in buffer

    for (const line of lines) {
      if (line.startsWith('data: ')) {
        const data = line.slice(6);
            
        if (data === '[DONE]') {
          console.log('\nStream finished');
          break;
        }

        try {
          const chunk = JSON.parse(data);
          const content = chunk.choices[0]?.delta?.content;
          if (content) {
            process.stdout.write(content);
          }
        } catch (e) {
          // Ignore parse errors
        }
      }
    }
  }
  ```
</CodeGroup>

### Python with OpenAI SDK

<CodeGroup>
  ```python Python theme={null}
  from openai import OpenAI

  client = OpenAI(
      api_key="YOUR_EDEN_AI_API_KEY",
      base_url="https://api.edenai.run/v3/llm"
  )

  stream = client.chat.completions.create(
      model="anthropic/claude-sonnet-4-5",
      messages=[{"role": "user", "content": "Tell me a short story"}],
      stream=True
  )

  full_content = ""

  for chunk in stream:
      if chunk.choices[0].delta.content:
          content = chunk.choices[0].delta.content
          full_content += content
          print(content, end='', flush=True)

  print(f"\n\nComplete response: {full_content}")
  ```
</CodeGroup>

## Chunk Structure

Each JSON chunk follows OpenAI's format:

```json theme={null}
{
  "id": "chatcmpl-abc123",
  "object": "chat.completion.chunk",
  "created": 1677652288,
  "model": "gpt-4",
  "choices": [
    {
      "index": 0,
      "delta": {
        "content": "Hello"
      },
      "finish_reason": null
    }
  ]
}
```

### Key Fields

| Field                     | Description                                         |
| ------------------------- | --------------------------------------------------- |
| `id`                      | Unique completion ID                                |
| `created`                 | Unix timestamp                                      |
| `model`                   | Model used                                          |
| `choices[].delta.role`    | Role (only in first chunk)                          |
| `choices[].delta.content` | Token content                                       |
| `choices[].finish_reason` | Stop reason in final chunk (`stop`, `length`, etc.) |

## Handling Different Finish Reasons

<CodeGroup>
  ```python Python theme={null}
  import json
  import requests

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }
  payload = {
      "model": "openai/gpt-4",
      "messages": [{"role": "user", "content": "Tell me a short story"}],
      "stream": True
  }

  response = requests.post(url, headers=headers, json=payload, stream=True)
  for line in response.iter_lines():
      if line:
          line_str = line.decode('utf-8')
          if line_str.startswith('data: '):
              data = line_str[6:]
                  
              if data == '[DONE]':
                  break
                  
              chunk = json.loads(data)
              choice = chunk['choices'][0]
                  
              # Check for content
              if 'content' in choice['delta']:
                  print(choice['delta']['content'], end='', flush=True)
                  
              # Check finish reason
              finish_reason = choice.get('finish_reason')
              if finish_reason:
                  if finish_reason == 'stop':
                      print("\n[Completed normally]")
                  elif finish_reason == 'length':
                      print("\n[Stopped: max tokens reached]")
                  elif finish_reason == 'content_filter':
                      print("\n[Stopped: content filter]")
  ```
</CodeGroup>

## Error Handling

Handle connection errors and timeouts:

<CodeGroup>
  ```python Python theme={null}
  import requests
  from requests.exceptions import Timeout, ConnectionError

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }
  payload = {
      "model": "openai/gpt-4",
      "messages": [{"role": "user", "content": "Tell me a short story"}],
      "stream": True
  }

  try:
      response = requests.post(
          url,
          headers=headers,
          json=payload,
          stream=True,
          timeout=60  # 60 second timeout
      )
          
      response.raise_for_status()
          
      for line in response.iter_lines():
          if line:
              line_str = line.decode('utf-8')
              # Process line...
                  
  except Timeout:
      print("Request timed out")
  except ConnectionError:
      print("Connection error")
  except requests.exceptions.HTTPError as e:
      print(f"HTTP error: {e}")
  ```
</CodeGroup>

## Buffering for UI Display

Buffer tokens for smoother UI updates:

<CodeGroup>
  ```python Python theme={null}
  import json
  import time
  import requests

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }
  payload = {
      "model": "openai/gpt-4",
      "messages": [{"role": "user", "content": "Tell me a short story"}],
      "stream": True
  }

  response = requests.post(url, headers=headers, json=payload, stream=True)

  buffer = ""
  last_update = time.time()
  update_interval = 0.05  # Update UI every 50ms

  for line in response.iter_lines():
      if line:
          line_str = line.decode('utf-8')
          if line_str.startswith('data: '):
              data = line_str[6:]
                  
              if data == '[DONE]':
                  # Flush remaining buffer
                  if buffer:
                      update_ui(buffer)
                  break
                  
              chunk = json.loads(data)
              if 'content' in chunk['choices'][0]['delta']:
                  content = chunk['choices'][0]['delta']['content']
                  buffer += content
                      
                  # Update UI periodically
                  now = time.time()
                  if now - last_update >= update_interval:
                      update_ui(buffer)
                      buffer = ""
                      last_update = now

  def update_ui(text):
      """Update your UI with the buffered text"""
      print(text, end='', flush=True)
  ```
</CodeGroup>

## React/Frontend Integration

Example React hook for streaming:

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { useState, useCallback } from 'react';

  function useStreamingChat() {
    const [content, setContent] = useState('');
    const [isStreaming, setIsStreaming] = useState(false);

    const sendMessage = useCallback(async (message) => {
      setIsStreaming(true);
      setContent('');

      const response = await fetch('https://api.edenai.run/v3/llm/chat/completions', {
        method: 'POST',
        headers: {
          'Authorization': 'Bearer YOUR_API_KEY',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          model: 'openai/gpt-4',
          messages: [{role: 'user', content: message}],
          stream: true
        })
      });

      const reader = response.body.getReader();
      const decoder = new TextDecoder();
      let buffer = '';

      while (true) {
        const {done, value} = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, {stream: true});
        const lines = buffer.split('\n');
        buffer = lines.pop();

        for (const line of lines) {
          if (line.startsWith('data: ')) {
            const data = line.slice(6);
            if (data === '[DONE]') break;

            try {
              const chunk = JSON.parse(data);
              const newContent = chunk.choices[0]?.delta?.content;
              if (newContent) {
                setContent(prev => prev + newContent);
              }
            } catch (e) {}
          }
        }
      }

      setIsStreaming(false);
    }, []);

    return { content, isStreaming, sendMessage };
  }
  ```
</CodeGroup>

## Next Steps

* [Chat Completions](./chat-completions) - Basic chat setup
* [File Attachments](./file-attachments) - Send images to LLMs
* [Getting Started](../../get-started/introduction) - V3 basics


# Vision Capabilities
Source: https://docs.edenai.co/v3/how-to/llm/vision-capabilities



Enable LLMs to see and understand images with vision-capable models.

## Overview

Vision-capable LLMs can analyze images and answer questions about visual content. This enables:

* **Image description** - Generate detailed descriptions of images
* **Visual Q\&A** - Answer questions about image content
* **OCR/Text extraction** - Read text from images
* **Object detection** - Identify objects and entities
* **Scene understanding** - Understand context and relationships
* **Chart analysis** - Interpret graphs and visualizations

Eden AI V3 provides vision capabilities through multiple providers, each with unique strengths.

## Vision-Capable Models

| Provider      | Model             | Strengths                      | Max Image Size | Languages |
| ------------- | ----------------- | ------------------------------ | -------------- | --------- |
| **OpenAI**    | gpt-4o            | Fast, accurate, multi-image    | 20 MB          | 50+       |
| **OpenAI**    | gpt-4-turbo       | High quality analysis          | 20 MB          | 50+       |
| **Anthropic** | claude-sonnet-4-5 | Excellent reasoning, documents | 5 MB           | 100+      |
| **Anthropic** | claude-opus-4-5   | Superior accuracy              | 5 MB           | 100+      |
| **Google**    | gemini-2.5-pro    | Long context, large files      | 20 MB          | 100+      |
| **Google**    | gemini-2.5-flash  | Fast, cost-effective           | 20 MB          | 100+      |
| **Mistral**   | pixtral-12b       | Efficient, European            | 10 MB          | 50+       |

## Basic Image Analysis

### Simple Image Description

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "openai/gpt-4o",
      "messages": [
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Describe this image in detail."
                  },
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": "https://example.com/landscape.jpg"
                      }
                  }
              ]
          }
      ]
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  print(result)
  ```

  ```javascript JavaScript theme={null}
  const url = 'https://api.edenai.run/v3/llm/chat/completions';
  const headers = {
    'Authorization': 'Bearer YOUR_API_KEY',
    'Content-Type': 'application/json'
  };

  const payload = {
    model: 'openai/gpt-4o',
    messages: [
      {
        role: 'user',
        content: [
          {type: 'text', text: 'Describe this image in detail.'},
          {
            type: 'image_url',
            image_url: {url: 'https://example.com/landscape.jpg'}
          }
        ]
      }
    ]
  };

  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(payload)
  });

  const result = await response.json();
  console.log(result);
  ```
</CodeGroup>

### Visual Question Answering

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "anthropic/claude-sonnet-4-5",
      "messages": [
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "How many people are in this photo? What are they doing?"
                  },
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": "https://example.com/group-photo.jpg"
                      }
                  }
              ]
          }
      ],
      "temperature": 0.3  # Lower for factual answers
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  print(result)
  ```
</CodeGroup>

## Advanced Vision Use Cases

### OCR and Text Extraction

Extract text from images with high accuracy:

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "google/gemini-2.5-flash",
      "messages": [
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Extract all text from this image exactly as it appears. Preserve formatting and layout."
                  },
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": "https://example.com/document-scan.jpg"
                      }
                  }
              ]
          }
      ],
      "temperature": 0.1  # Very low for accurate OCR
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  extracted_text = result.get('choices', [{}])[0].get('message', {}).get('content', '')
  print("Extracted text:", extracted_text)
  ```
</CodeGroup>

### Object and Entity Detection

Identify objects, brands, and entities:

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "openai/gpt-4o",
      "messages": [
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "List all objects visible in this image. For each object, provide: name, position (left/right/center), approximate size, and color."
                  },
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": "https://example.com/room.jpg"
                      }
                  }
              ]
          }
      ]
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  print(result)
  ```
</CodeGroup>

### Chart and Graph Analysis

Interpret data visualizations:

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "anthropic/claude-opus-4-5",
      "messages": [
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": """Analyze this chart and provide:
                      1. Chart type and what it represents
                      2. Key data points and trends
                      3. Notable patterns or anomalies
                      4. Three actionable insights
                      5. Recommendations based on the data"""
                  },
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": "https://example.com/sales-graph.png"
                      }
                  }
              ]
          }
      ],
      "temperature": 0.4,
      "max_tokens": 800
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  print(result)
  ```
</CodeGroup>

### Screenshot Analysis

Debug UI issues or analyze interfaces:

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "openai/gpt-4o",
      "messages": [
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": """This is a screenshot of a web application. Analyze:
                      1. All UI components (buttons, forms, navigation)
                      2. Layout structure and hierarchy
                      3. Accessibility issues (contrast, sizing)
                      4. UX improvements
                      5. Any visible errors or bugs"""
                  },
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": "https://example.com/app-screenshot.png"
                      }
                  }
              ]
          }
      ],
      "max_tokens": 1000
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  print(result)
  ```
</CodeGroup>

### Logo and Brand Detection

Identify brands and logos:

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "google/gemini-2.5-pro",
      "messages": [
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Identify all brands and logos visible in this image. For each, provide the brand name and position in the image."
                  },
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": "https://example.com/storefront.jpg"
                      }
                  }
              ]
          }
      ]
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  print(result)
  ```
</CodeGroup>

## Multi-Image Analysis

Compare and analyze multiple images:

### Before/After Comparison

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "openai/gpt-4o",
      "messages": [
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Compare these before and after images. List all differences in detail."
                  },
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": "https://example.com/before.jpg"
                      }
                  },
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": "https://example.com/after.jpg"
                      }
                  }
              ]
          }
      ]
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  print(result)
  ```
</CodeGroup>

### Multi-Image Context

Analyze related images together:

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "anthropic/claude-sonnet-4-5",
      "messages": [
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "These are sequential steps of a process. Describe each step and create a numbered guide."
                  },
                  {
                      "type": "image_url",
                      "image_url": {"url": "https://example.com/step1.jpg"}
                  },
                  {
                      "type": "image_url",
                      "image_url": {"url": "https://example.com/step2.jpg"}
                  },
                  {
                      "type": "image_url",
                      "image_url": {"url": "https://example.com/step3.jpg"}
                  }
              ]
          }
      ],
      "max_tokens": 1200
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  print(result)
  ```
</CodeGroup>

## Provider Comparison

### OpenAI (GPT-4o, GPT-4-turbo)

**Strengths:**

* Fast processing
* Excellent general-purpose vision
* Strong multi-image capabilities
* Reliable OCR
* Good detail detection

**Best for:**

* Real-time applications
* Multi-image analysis
* General image understanding
* Screenshot analysis

**Example:**

```
"model": "openai/gpt-4o"
```

### Anthropic (Claude 3 Family)

**Strengths:**

* Superior reasoning about images
* Excellent document analysis
* Strong at complex visual tasks
* Detailed, thoughtful responses
* Multi-language support

**Best for:**

* Document processing
* Complex reasoning tasks
* Detailed analysis
* Academic/research content

**Example:**

```
"model": "anthropic/claude-sonnet-4-5"
```

### Google (Gemini 1.5)

**Strengths:**

* Extremely long context (up to 2GB)
* Fast processing (Flash variant)
* Strong multilingual capabilities
* Excellent for large documents
* Cost-effective (Flash)

**Best for:**

* Large document processing
* Multi-page PDFs
* Video frame analysis
* High-volume applications

**Example:**

```
"model": "google/gemini-2.5-flash"
```

### Mistral (Pixtral)

**Strengths:**

* European data residency
* Efficient processing
* Good price/performance
* Privacy-focused

**Best for:**

* European compliance needs
* Cost-sensitive applications
* Privacy requirements

**Example:**

```
"model": "mistral/pixtral-12b"
```

## Image Input Formats

### HTTP(S) URLs

Simplest method for accessible images:

```python theme={null}
{
    "type": "image_url",
    "image_url": {
        "url": "https://example.com/image.jpg"
    }
}
```

### Base64 Data URLs

For inline or private images:

```python theme={null}
import base64

with open("image.jpg", "rb") as f:
    image_data = base64.b64encode(f.read()).decode('utf-8')

{
    "type": "image_url",
    "image_url": {
        "url": f"data:image/jpeg;base64,{image_data}"
    }
}
```

### Uploaded File UUIDs

For reusable images:

```python theme={null}
import requests

# Upload first
upload_response = requests.post(
    "https://api.edenai.run/v3/upload",
    headers={"Authorization": "Bearer YOUR_API_KEY"},
    files={"file": open("image.jpg", "rb")}
)
file_id = upload_response.json()["file_id"]

# Use in vision request
{
    "type": "file",
    "file": {"file_id": file_id}
}
```

## Best Practices

### Prompting for Vision

**Be specific about what you want:**

```python theme={null}
# Vague
"What's in this image?"

# Specific
"List all furniture items visible in this room photo, including their approximate positions and colors."
```

**Request structured output:**

```
"Extract the following from this business card and format as JSON:
- name
- title
- company
- email
- phone"
```

**Provide context:**

```python theme={null}
"This is a medical X-ray of a chest. Identify any abnormalities or concerning features."
```

### Image Quality Tips

**Optimize resolution:**

* Use high-quality images (min 1024px on longest side)
* Avoid excessive compression
* Ensure text is legible

**Proper lighting:**

* Well-lit images work best
* Avoid glare and shadows
* Ensure good contrast

**Clear framing:**

* Center subjects of interest
* Avoid clutter when possible
* Crop to relevant content

### Temperature Settings

Adjust temperature based on task:

```
# Factual tasks (OCR, counting, detection)
"temperature": 0.1

# General description
"temperature": 0.5

# Creative interpretation
"temperature": 0.8
```

### Cost Optimization

**Choose appropriate models:**

* Use `gemini-2.5-flash` for high-volume tasks
* Reserve `claude-opus-4-5` for complex analysis
* Use `gpt-4o` for balanced performance

**Image size optimization:**

* Resize images to minimum needed resolution
* Compress without losing critical details
* Use URLs instead of base64 when possible

## Error Handling

### Common Vision Errors

**Unsupported image format:**

```json theme={null}
{
  "error": {
    "code": "unsupported_format",
    "message": "Image format .bmp is not supported"
  }
}
```

**Image too large:**

```json theme={null}
{
  "error": {
    "code": "image_too_large",
    "message": "Image size exceeds 20 MB limit for this provider"
  }
}
```

**Invalid image data:**

```json theme={null}
{
  "error": {
    "code": "invalid_image",
    "message": "Unable to process image data"
  }
}
```

### Handling Vision Errors

<CodeGroup>
  ```python Python theme={null}
  import requests
  from PIL import Image
  import io
  import base64

  def resize_if_needed(image_path, max_size_mb=10):
      """Resize image if it exceeds size limit."""
      with open(image_path, 'rb') as f:
          size_mb = len(f.read()) / (1024 * 1024)

      if size_mb > max_size_mb:
          img = Image.open(image_path)
          # Reduce quality
          output = io.BytesIO()
          img.save(output, format='JPEG', quality=85, optimize=True)
          return output.getvalue()

      with open(image_path, 'rb') as f:
          return f.read()

  def analyze_image_with_retry(image_path, prompt):
      """Analyze image with automatic retry and resizing."""
      url = "https://api.edenai.run/v3/llm/chat/completions"
      headers = {
          "Authorization": "Bearer YOUR_API_KEY",
          "Content-Type": "application/json"
      }

      try:
          # Encode image as base64
          image_data = resize_if_needed(image_path)
          b64_image = base64.b64encode(image_data).decode("utf-8")

          payload = {
              "model": "openai/gpt-4o",
              "messages": [
                  {
                      "role": "user",
                      "content": [
                          {"type": "text", "text": prompt},
                          {
                              "type": "image_url",
                              "image_url": {
                                  "url": f"data:image/jpeg;base64,{b64_image}"
                              }
                          }
                      ]
                  }
              ]
          }

          response = requests.post(url, headers=headers, json=payload)
          response.raise_for_status()
          return response.json()

      except requests.exceptions.HTTPError as e:
          if e.response.status_code == 413:  # Image too large
              print("Image too large, resizing...")
              resized = resize_if_needed(image_path, max_size_mb=5)
              # Retry with smaller size limit
              # ... implement retry logic
          else:
              raise

  # Usage
  response = analyze_image_with_retry(
      "large-image.jpg",
      "Describe this image in detail"
  )
  ```
</CodeGroup>

## Supported Image Formats

| Format | Extension   | OpenAI | Anthropic | Google | Mistral |
| ------ | ----------- | ------ | --------- | ------ | ------- |
| JPEG   | .jpg, .jpeg | ✓      | ✓         | ✓      | ✓       |
| PNG    | .png        | ✓      | ✓         | ✓      | ✓       |
| WebP   | .webp       | ✓      | ✓         | ✓      | ✓       |
| GIF    | .gif        | ✓      | ✓         | ✓      | -       |

## Next Steps

* [Working with Media Files](./working-with-media) - Complete media guide
* [File Attachments](./file-attachments) - Handle documents and PDFs
* [Chat Completions](./chat-completions) - Core LLM features
* [Streaming Responses](./streaming) - Handle SSE streams
* [Upload Files](../upload/upload-files) - File management


# Working with Media Files
Source: https://docs.edenai.co/v3/how-to/llm/working-with-media



Send images, documents, and other media files to LLMs for analysis and understanding.

## Overview

Eden AI V3 LLM endpoints support **multimodal inputs**, allowing you to send:

* **Images** - For visual understanding and analysis
* **Documents** - PDFs and text files for processing
* **Mixed content** - Combine text prompts with media

Multimodal capabilities enable use cases like:

* Analyzing screenshots and diagrams
* Extracting data from images and documents
* Visual question answering
* Chart and graph interpretation
* Receipt and invoice processing

## Supported Input Types

V3 supports multiple ways to send media to LLMs:

| Input Type           | Format                 | Best For                    | Example                           |
| -------------------- | ---------------------- | --------------------------- | --------------------------------- |
| **HTTP(S) URL**      | Direct link            | Publicly accessible files   | `https://example.com/image.jpg`   |
| **Base64 Data URL**  | Inline encoded data    | Small files, secure data    | `data:image/jpeg;base64,...`      |
| **File Upload**      | UUID from `/v3/upload` | Reusable files, large files | `550e8400-e29b-...`               |
| **Base64 File Data** | Raw base64 or data URL | PDFs, documents             | `data:application/pdf;base64,...` |

## Image Inputs

### Using Image URLs

The simplest method for publicly accessible images:

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "openai/gpt-4o",
      "messages": [
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "What's in this image?"
                  },
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": "https://example.com/photo.jpg"
                      }
                  }
              ]
          }
      ]
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  print(result)
  ```

  ```javascript JavaScript theme={null}
  const url = 'https://api.edenai.run/v3/llm/chat/completions';
  const headers = {
      'Authorization': 'Bearer YOUR_API_KEY',
      'Content-Type': 'application/json'
  };

  const payload = {
      model: 'openai/gpt-4o',
      messages: [
      {
          role: 'user',
          content: [
          {
              type: 'text',
              text: "What's in this image?"
          },
          {
              type: 'image_url',
              image_url: {
              url: 'https://example.com/photo.jpg'
              }
          }
          ]
      }
      ]
  };

  const response = await fetch(url, {
      method: 'POST',
      headers: headers,
      body: JSON.stringify(payload)
  });

  const result = await response.json();
  console.log(result);
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.edenai.run/v3/llm/chat/completions \
      -H "Authorization: Bearer YOUR_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
      "model": "openai/gpt-4o",
      "messages": [
          {
          "role": "user",
          "content": [
              {"type": "text", "text": "What'\''s in this image?"},
              {
              "type": "image_url",
              "image_url": {"url": "https://example.com/photo.jpg"}
              }
          ]
          }
      ]
      }'
  ```
</CodeGroup>

### Using Base64 Image Data

For inline images or when URLs aren't available:

<CodeGroup>
  ```python Python theme={null}
  import base64
  import requests

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  # Read and encode image
  with open("image.jpg", "rb") as f:
      image_data = base64.b64encode(f.read()).decode('utf-8')

  # Create data URL
  data_url = f"data:image/jpeg;base64,{image_data}"

  payload = {
      "model": "anthropic/claude-sonnet-4-5",
      "messages": [
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "Describe this image in detail."},
                  {
                      "type": "image_url",
                      "image_url": {"url": data_url}
                  }
              ]
          }
      ]
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  ```

  ```javascript JavaScript theme={null}
  const fs = require('fs');

  // Read and encode image
  const imageBuffer = fs.readFileSync('image.jpg');
  const imageData = imageBuffer.toString('base64');
  const dataUrl = `data:image/jpeg;base64,${imageData}`;

  const payload = {
      model: 'anthropic/claude-sonnet-4-5',
      messages: [
      {
          role: 'user',
          content: [
          {type: 'text', text: 'Describe this image in detail.'},
          {
              type: 'image_url',
              image_url: {url: dataUrl}
          }
          ]
      }
      ]
  };

  const response = await fetch(url, {
      method: 'POST',
      headers: headers,
      body: JSON.stringify(payload)
  });

  const result = await response.json();
  ```
</CodeGroup>

### Using Uploaded Files

For reusable images or better performance:

<CodeGroup>
  ```python Python theme={null}
  import requests

  # Step 1: Upload the image
  upload_url = "https://api.edenai.run/v3/upload"
  upload_headers = {"Authorization": "Bearer YOUR_API_KEY"}

  files = {"file": open("screenshot.png", "rb")}
  upload_response = requests.post(upload_url, headers=upload_headers, files=files)
  file_id = upload_response.json()["file_id"]

  print(f"Uploaded file ID: {file_id}")

  # Step 2: Use the file in LLM request
  llm_url = "https://api.edenai.run/v3/llm/chat/completions"
  llm_headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "google/gemini-2.5-pro",
      "messages": [
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "Analyze this screenshot and list all UI elements."},
                  {
                      "type": "file",
                      "file": {"file_id": file_id}
                  }
              ]
          }
      ]
  }

  response = requests.post(llm_url, headers=llm_headers, json=payload)
  result = response.json()
  print(result)
  ```
</CodeGroup>

## Document Inputs

### PDF and Document Files

Send PDFs and documents for analysis:

<CodeGroup>
  ```python Python theme={null}
  import requests

  # Upload PDF document
  upload_url = "https://api.edenai.run/v3/upload"
  upload_headers = {"Authorization": "Bearer YOUR_API_KEY"}

  files = {"file": open("report.pdf", "rb")}
  data = {"purpose": "llm-analysis"}

  upload_response = requests.post(
      upload_url,
      headers=upload_headers,
      files=files,
      data=data
  )
  file_id = upload_response.json()["file_id"]

  # Analyze the PDF with LLM
  llm_url = "https://api.edenai.run/v3/llm/chat/completions"
  llm_headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "anthropic/claude-sonnet-4-5",
      "messages": [
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "Summarize this document and extract key findings."},
                  {
                      "type": "file",
                      "file": {"file_id": file_id}
                  }
              ]
          }
      ]
  }

  response = requests.post(llm_url, headers=llm_headers, json=payload)
  result = response.json()
  print(result)
  ```
</CodeGroup>

### Base64 Document Data

For inline document processing:

<CodeGroup>
  ```python Python theme={null}
  import base64
  import requests

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  # Read and encode PDF
  with open("invoice.pdf", "rb") as f:
      pdf_data = base64.b64encode(f.read()).decode('utf-8')

  # Create data URL for PDF
  data_url = f"data:application/pdf;base64,{pdf_data}"

  payload = {
      "model": "openai/gpt-4o",
      "messages": [
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "Extract all line items and totals from this invoice."},
                  {
                      "type": "file",
                      "file": {"file_data": data_url}
                  }
              ]
          }
      ]
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  ```
</CodeGroup>

## Mixed Content Messages

### Multiple Images

Send multiple images in a single message:

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "openai/gpt-4o",
      "messages": [
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "Compare these two images and describe the differences."},
                  {
                      "type": "image_url",
                      "image_url": {"url": "https://example.com/before.jpg"}
                  },
                  {
                      "type": "image_url",
                      "image_url": {"url": "https://example.com/after.jpg"}
                  }
              ]
          }
      ]
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  ```
</CodeGroup>

### Text + Images + Documents

Combine different media types:

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "anthropic/claude-sonnet-4-5",
      "messages": [
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Review the chart and supporting documentation. Provide analysis."
                  },
                  {
                      "type": "image_url",
                      "image_url": {"url": "https://example.com/chart.png"}
                  },
                  {
                      "type": "file",
                      "file": {"file_id": "550e8400-e29b-41d4-a716-446655440000"}
                  }
              ]
          }
      ]
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  ```
</CodeGroup>

## Practical Examples

### Analyze a Screenshot

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "openai/gpt-4o",
      "messages": [
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "This is a screenshot of an error message. What's wrong and how do I fix it?"
                  },
                  {
                      "type": "image_url",
                      "image_url": {"url": "https://example.com/error-screenshot.png"}
                  }
              ]
          }
      ],
      "max_tokens": 500
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  print(result)
  ```
</CodeGroup>

### Extract Receipt Data

<CodeGroup>
  ```python Python theme={null}
  import requests
  import base64

  # Read receipt image
  with open("receipt.jpg", "rb") as f:
      image_data = base64.b64encode(f.read()).decode('utf-8')

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "anthropic/claude-sonnet-4-5",
      "messages": [
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Extract the following from this receipt: merchant name, date, total amount, items purchased. Format as JSON."
                  },
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": f"data:image/jpeg;base64,{image_data}"
                      }
                  }
              ]
          }
      ],
      "temperature": 0.2  # Lower temperature for structured extraction
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  print("Extracted data:", result)
  ```
</CodeGroup>

### Summarize PDF Document

<CodeGroup>
  ```python Python theme={null}
  import requests

  # Upload PDF
  upload_url = "https://api.edenai.run/v3/upload"
  upload_headers = {"Authorization": "Bearer YOUR_API_KEY"}

  files = {"file": open("research-paper.pdf", "rb")}
  upload_response = requests.post(upload_url, headers=upload_headers, files=files)
  file_id = upload_response.json()["file_id"]

  # Request summary
  llm_url = "https://api.edenai.run/v3/llm/chat/completions"
  llm_headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "google/gemini-2.5-pro",
      "messages": [
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Provide a comprehensive summary of this research paper, including methodology, key findings, and conclusions."
                  },
                  {
                      "type": "file",
                      "file": {"file_id": file_id}
                  }
              ]
          }
      ],
      "max_tokens": 1000
  }

  response = requests.post(llm_url, headers=llm_headers, json=payload)
  result = response.json()
  print(result)
  ```
</CodeGroup>

### Chart Analysis

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "openai/gpt-4o",
      "messages": [
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Analyze this chart and provide: 1) Main trends, 2) Notable outliers, 3) Key insights, 4) Recommendations"
                  },
                  {
                      "type": "image_url",
                      "image_url": {"url": "https://example.com/sales-chart.png"}
                  }
              ]
          }
      ],
      "temperature": 0.3
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  print(result)
  ```
</CodeGroup>

## Provider Support Matrix

Different providers have varying multimodal capabilities:

| Provider      | Models                             | Image URLs | Base64 Images | PDF/Docs | Max Image Size | Max File Size |
| ------------- | ---------------------------------- | ---------- | ------------- | -------- | -------------- | ------------- |
| **OpenAI**    | gpt-4o, gpt-4-turbo                | ✓          | ✓             | ✓        | 20 MB          | 512 MB        |
| **Anthropic** | claude-opus-4-5, claude-sonnet-4-5 | ✓          | ✓             | ✓        | 5 MB           | 10 MB         |
| **Google**    | gemini-2.5-pro, gemini-2.5-flash   | ✓          | ✓             | ✓        | 20 MB          | 2 GB          |
| **Mistral**   | pixtral-12b                        | ✓          | ✓             | -        | 10 MB          | -             |

See [Vision Capabilities](./vision-capabilities) for detailed provider comparison.

## Best Practices

### Choosing Input Method

**Use HTTP(S) URLs when:**

* Images are publicly accessible
* You want to minimize request payload size
* Files are already hosted

**Use uploaded files (UUID) when:**

* Processing the same file multiple times
* Files are large (reduces repeated upload overhead)
* Better performance is needed

**Use base64 when:**

* Files are small (5 MB)
* URLs aren't available
* Security/privacy requires inline data

### Optimizing Performance

**Image optimization:**

* Resize large images before uploading
* Use appropriate compression
* Consider using URLs for public images

**Document optimization:**

* Extract relevant pages from large PDFs
* Use text extraction for text-heavy documents
* Consider OCR preprocessing for scanned documents

### Prompting Strategies

**Be specific:**

```python theme={null}
# Vague
"What's in this image?"

# Specific
"List all visible UI components in this screenshot, including buttons, text fields, and their labels."
```

**Provide context:**

```python theme={null}
{
    "type": "text",
    "text": "This is a medical chart showing patient vitals over 24 hours. Identify any concerning trends."
}
```

**Use structured output:**

```python theme={null}
{
    "type": "text",
    "text": "Extract data as JSON with fields: date, vendor, total, items[]."
}
```

## Error Handling

### Common Issues

**File too large:**

```json theme={null}
{
  "error": {
    "code": "file_too_large",
    "message": "File size exceeds provider limit of 20 MB"
  }
}
```

**Unsupported format:**

```json theme={null}
{
  "error": {
    "code": "unsupported_format",
    "message": "Image format .bmp is not supported"
  }
}
```

**Invalid base64:**

```json theme={null}
{
  "error": {
    "code": "invalid_base64",
    "message": "Invalid base64 data in data URL"
  }
}
```

### Handling Errors

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }
  payload = {
      "model": "openai/gpt-4o",
      "messages": [{"role": "user", "content": "Hello"}]
  }

  try:
      response = requests.post(url, headers=headers, json=payload)
      response.raise_for_status()
      result = response.json()
      print(result)

  except requests.exceptions.HTTPError as e:
      if e.response.status_code == 413:
          print("File too large. Try compressing or resizing.")
      elif e.response.status_code == 422:
          print("Invalid request:", e.response.json())
      else:
          print(f"HTTP error: {e}")
  ```
</CodeGroup>

## Next Steps

* [Vision Capabilities](./vision-capabilities) - Deep dive into image analysis
* [File Attachments](./file-attachments) - Working with documents and PDFs
* [Upload Files](../upload/upload-files) - File upload and management
* [Streaming Responses](./streaming) - Handle SSE streaming
* [Chat Completions](./chat-completions) - Core LLM usage guide


# Advanced usage
Source: https://docs.edenai.co/v3/how-to/router/advanced-usage



# Advanced Router Usage

Master advanced routing patterns, optimization strategies, and production best practices.

## Overview

This guide covers advanced routing techniques for production applications, including cost optimization, context-aware routing, multi-turn conversations, and performance tuning.

**What you'll learn:**

* Cost-optimized routing strategies
* Context-aware model selection
* Multi-turn conversation handling
* Performance optimization techniques
* Function calling with routing
* Production deployment patterns

## Cost Optimization Strategies

### Strategy 1: Tiered Routing by Query Complexity

Route simple queries to cheaper models and complex queries to premium models:

<CodeGroup>
  ```python Python theme={null}
  import requests
  from typing import Literal

  class TieredRouter:
      """Route based on query complexity tiers."""

      BUDGET_MODELS = [
          "openai/gpt-4o-mini",
          "google/gemini-2.5-flash",
          "openai/gpt-4"
      ]

      BALANCED_MODELS = [
          "openai/gpt-4o",
          "anthropic/claude-sonnet-4-5",
          "google/gemini-2.5-flash"
      ]

      PREMIUM_MODELS = [
          "anthropic/claude-opus-4-5",
          "openai/gpt-4o",
          "google/gemini-2.5-pro"
      ]

      def __init__(self, api_key: str):
          self.api_key = api_key
          self.url = "https://api.edenai.run/v3/llm/chat/completions"

      def _classify_query(self, message: str) -> Literal["budget", "balanced", "premium"]:
          """Classify query complexity (simple heuristic)."""
          message_lower = message.lower()

          # Simple queries
          simple_keywords = ["what is", "define", "who is", "when", "where"]
          if any(kw in message_lower for kw in simple_keywords) and len(message) < 100:
              return "budget"

          # Complex queries
          complex_keywords = ["analyze", "compare", "evaluate", "design", "architect"]
          if any(kw in message_lower for kw in complex_keywords) or len(message) > 500:
              return "premium"

          # Default to balanced
          return "balanced"

      def get_candidates(self, tier: str) -> list[str]:
          """Get model candidates for tier."""
          return {
              "budget": self.BUDGET_MODELS,
              "balanced": self.BALANCED_MODELS,
              "premium": self.PREMIUM_MODELS
          }.get(tier, self.BALANCED_MODELS)

      def chat(self, message: str, force_tier: str = None) -> dict:
          """Chat with automatic tier selection."""
          tier = force_tier or self._classify_query(message)
          candidates = self.get_candidates(tier)

          headers = {
              "Authorization": f"Bearer {self.api_key}",
              "Content-Type": "application/json"
          }

          payload = {
              "model": "@edenai",
              "router_candidates": candidates,
              "messages": [{"role": "user", "content": message}]
          }

          response = requests.post(
              self.url,
              headers=headers,
              json=payload
          )

          data = response.json()
          selected_model = data.get('model')
          full_response = data.get('choices', [{}])[0].get('message', {}).get('content', '')

          return {
              "response": full_response,
              "tier": tier,
              "model": selected_model,
              "candidates": candidates
          }

  # Usage
  router = TieredRouter("YOUR_API_KEY")

  # Simple query → Budget tier
  result1 = router.chat("What is Python?")
  print(f"Tier: {result1['tier']}, Model: {result1['model']}")

  # Complex query → Premium tier
  result2 = router.chat(
      "Design a scalable microservices architecture for an e-commerce platform "
      "with considerations for high availability, security, and performance"
  )
  print(f"Tier: {result2['tier']}, Model: {result2['model']}")

  # Force specific tier
  result3 = router.chat("Tell me a joke", force_tier="budget")
  print(f"Tier: {result3['tier']}, Model: {result3['model']}")
  ```
</CodeGroup>

### Strategy 2: Dynamic Budget Management

Track spending and adjust routing based on budget:

<CodeGroup>
  ```python Python theme={null}
  import requests
  from datetime import datetime, timedelta
  from typing import Optional

  class BudgetAwareRouter:
      """Route with budget tracking and limits."""

      # Rough cost estimates per 1k tokens (input + output avg)
      MODEL_COSTS = {
          "openai/gpt-4o-mini": 0.0002,
          "google/gemini-2.5-flash": 0.0002,
          "openai/gpt-4": 0.0005,
          "openai/gpt-4o": 0.003,
          "anthropic/claude-sonnet-4-5": 0.004,
          "anthropic/claude-opus-4-5": 0.015,
      }

      def __init__(self, api_key: str, daily_budget: float = 10.0):
          self.api_key = api_key
          self.daily_budget = daily_budget
          self.url = "https://api.edenai.run/v3/llm/chat/completions"

          # Track spending
          self.spending_today = 0.0
          self.last_reset = datetime.now().date()

      def _check_budget_reset(self):
          """Reset budget counter at midnight."""
          today = datetime.now().date()
          if today > self.last_reset:
              self.spending_today = 0.0
              self.last_reset = today

      def get_affordable_candidates(self) -> list[str]:
          """Get candidates based on remaining budget."""
          self._check_budget_reset()
          remaining = self.daily_budget - self.spending_today

          if remaining < 0.01:  # Less than 1 cent
              return []  # Budget exhausted

          if remaining < 1.0:  # Less than $1
              # Only budget models
              return [
                  "openai/gpt-4o-mini",
                  "google/gemini-2.5-flash",
                  "openai/gpt-4"
              ]

          if remaining < 5.0:  # Less than $5
              # Balanced models
              return [
                  "openai/gpt-4o",
                  "anthropic/claude-sonnet-4-5",
                  "google/gemini-2.5-flash"
              ]

          # Full budget available - use premium
          return [
              "anthropic/claude-opus-4-5",
              "openai/gpt-4o",
              "google/gemini-2.5-pro"
          ]

      def estimate_cost(self, message: str, response: str) -> float:
          """Estimate cost based on token count (rough)."""
          # Rough estimate: 4 chars = 1 token
          total_chars = len(message) + len(response)
          estimated_tokens = total_chars / 4
          estimated_1k_tokens = estimated_tokens / 1000

          # Use average cost for simplicity
          avg_cost_per_1k = 0.003
          return estimated_1k_tokens * avg_cost_per_1k

      def chat(self, message: str) -> dict:
          """Chat with budget awareness."""
          candidates = self.get_affordable_candidates()

          if not candidates:
              return {
                  "success": False,
                  "error": "Daily budget exhausted",
                  "budget_info": {
                      "daily_budget": self.daily_budget,
                      "spent_today": self.spending_today,
                      "remaining": 0
                  }
              }

          headers = {
              "Authorization": f"Bearer {self.api_key}",
              "Content-Type": "application/json"
          }

          payload = {
              "model": "@edenai",
              "router_candidates": candidates,
              "messages": [{"role": "user", "content": message}]
          }

          response = requests.post(
              self.url,
              headers=headers,
              json=payload
          )

          data = response.json()
          selected_model = data.get('model')
          full_response = data.get('choices', [{}])[0].get('message', {}).get('content', '')

          # Track spending
          estimated_cost = self.estimate_cost(message, full_response)
          self.spending_today += estimated_cost

          remaining = self.daily_budget - self.spending_today

          return {
              "success": True,
              "response": full_response,
              "model": selected_model,
              "budget_info": {
                  "daily_budget": self.daily_budget,
                  "spent_today": round(self.spending_today, 4),
                  "remaining": round(remaining, 4),
                  "estimated_request_cost": round(estimated_cost, 4)
              }
          }

  # Usage
  router = BudgetAwareRouter("YOUR_API_KEY", daily_budget=10.0)

  # Make requests
  for i in range(5):
      result = router.chat(f"Question {i+1}: Explain AI")
      if result["success"]:
          print(f"Request {i+1}:")
          print(f"  Model: {result['model']}")
          print(f"  Cost: ${result['budget_info']['estimated_request_cost']}")
          print(f"  Remaining: ${result['budget_info']['remaining']}")
      else:
          print(f"Request {i+1}: {result['error']}")
  ```
</CodeGroup>

## Context-Aware Routing

### Use Case-Specific Candidate Pools

Define different candidate pools for different use cases:

<CodeGroup>
  ```python Python theme={null}
  import requests
  from enum import Enum
  from typing import Literal

  class UseCase(str, Enum):
      """Supported use cases."""
      CODE = "code"
      CREATIVE = "creative"
      ANALYSIS = "analysis"
      TRANSLATION = "translation"
      CHAT = "chat"
      SUMMARIZATION = "summarization"

  class ContextAwareRouter:
      """Route based on use case context."""

      # Define optimal models for each use case
      CANDIDATES = {
          UseCase.CODE: [
              "openai/gpt-4o",
              "anthropic/claude-sonnet-4-5",
          ],
          UseCase.CREATIVE: [
              "anthropic/claude-opus-4-5",
              "openai/gpt-4o",
              "google/gemini-2.5-pro"
          ],
          UseCase.ANALYSIS: [
              "anthropic/claude-opus-4-5",
              "openai/gpt-4o",
              "google/gemini-2.5-pro"
          ],
          UseCase.TRANSLATION: [
              "openai/gpt-4o",
              "google/gemini-2.5-flash",
              "anthropic/claude-sonnet-4-5"
          ],
          UseCase.CHAT: [
              "openai/gpt-4o",
              "anthropic/claude-sonnet-4-5",
              "google/gemini-2.5-flash"
          ],
          UseCase.SUMMARIZATION: [
              "openai/gpt-4o-mini",
              "google/gemini-2.5-flash",
              "openai/gpt-4"
          ]
      }

      def __init__(self, api_key: str):
          self.api_key = api_key
          self.url = "https://api.edenai.run/v3/llm/chat/completions"

      def chat(
          self,
          message: str,
          use_case: UseCase = UseCase.CHAT,
          system_prompt: str = None
      ) -> dict:
          """Chat with use case-specific routing."""

          candidates = self.CANDIDATES.get(use_case, self.CANDIDATES[UseCase.CHAT])

          messages = []
          if system_prompt:
              messages.append({"role": "system", "content": system_prompt})
          messages.append({"role": "user", "content": message})

          headers = {
              "Authorization": f"Bearer {self.api_key}",
              "Content-Type": "application/json"
          }

          payload = {
              "model": "@edenai",
              "router_candidates": candidates,
              "messages": messages
          }

          response = requests.post(
              self.url,
              headers=headers,
              json=payload
          )

          data = response.json()
          selected_model = data.get('model')
          full_response = data.get('choices', [{}])[0].get('message', {}).get('content', '')

          return {
              "response": full_response,
              "use_case": use_case.value,
              "model": selected_model,
              "candidates": candidates
          }

  # Usage examples
  router = ContextAwareRouter("YOUR_API_KEY")

  # Code generation
  code_result = router.chat(
      "Write a Python function to parse JSON",
      use_case=UseCase.CODE
  )
  print(f"Code task → {code_result['model']}")

  # Creative writing
  creative_result = router.chat(
      "Write a short story about a time traveler",
      use_case=UseCase.CREATIVE
  )
  print(f"Creative task → {creative_result['model']}")

  # Summarization
  summary_result = router.chat(
      "Summarize this article: [long text]",
      use_case=UseCase.SUMMARIZATION
  )
  print(f"Summarization task → {summary_result['model']}")
  ```
</CodeGroup>

## Multi-Turn Conversations

### Stateful Conversation with Routing

Maintain conversation state while using smart routing:

<CodeGroup>
  ```python Python theme={null}
  import requests
  import json
  from typing import Optional

  class SmartConversation:
      """Manage multi-turn conversations with smart routing."""

      def __init__(
          self,
          api_key: str,
          candidates: list[str] = None,
          system_prompt: str = None
      ):
          self.api_key = api_key
          self.candidates = candidates
          self.url = "https://api.edenai.run/v3/llm/chat/completions"
          self.messages = []
          self.routing_history = []

          # Add system prompt if provided
          if system_prompt:
              self.messages.append({"role": "system", "content": system_prompt})

      def send(self, message: str) -> dict:
          """Send a message and get response."""
          # Add user message
          self.messages.append({"role": "user", "content": message})

          headers = {
              "Authorization": f"Bearer {self.api_key}",
              "Content-Type": "application/json"
          }

          payload = {
              "model": "@edenai",
              "messages": self.messages  # Full conversation history
          }

          if self.candidates:
              payload["router_candidates"] = self.candidates

          response = requests.post(
              self.url,
              headers=headers,
              json=payload
          )

          data = response.json()
          selected_model = data.get('model')
          assistant_response = data.get('choices', [{}])[0].get('message', {}).get('content', '')

          # Add assistant response to history
          self.messages.append({"role": "assistant", "content": assistant_response})

          # Track routing decision
          self.routing_history.append({
              "turn": len(self.routing_history) + 1,
              "model": selected_model,
              "user_message": message[:50] + "..." if len(message) > 50 else message
          })

          return {
              "response": assistant_response,
              "model": selected_model,
              "turn": len(self.routing_history)
          }

      def get_history(self) -> list[dict]:
          """Get conversation history."""
          return self.messages.copy()

      def get_routing_stats(self) -> dict:
          """Get routing statistics."""
          if not self.routing_history:
              return {}

          from collections import Counter
          model_counts = Counter(entry["model"] for entry in self.routing_history)

          return {
              "total_turns": len(self.routing_history),
              "models_used": dict(model_counts),
              "routing_history": self.routing_history
          }

      def reset(self):
          """Reset conversation."""
          system_msg = [m for m in self.messages if m["role"] == "system"]
          self.messages = system_msg
          self.routing_history = []

  # Usage
  conversation = SmartConversation(
      "YOUR_API_KEY",
      candidates=["openai/gpt-4o", "anthropic/claude-sonnet-4-5"],
      system_prompt="You are a helpful coding assistant."
  )

  # Multi-turn conversation
  result1 = conversation.send("What is Python?")
  print(f"Turn 1 [{result1['model']}]: {result1['response'][:100]}...")

  result2 = conversation.send("Can you show me a code example?")
  print(f"Turn 2 [{result2['model']}]: {result2['response'][:100]}...")

  result3 = conversation.send("Explain that code in detail")
  print(f"Turn 3 [{result3['model']}]: {result3['response'][:100]}...")

  # Get statistics
  stats = conversation.get_routing_stats()
  print(f"\nConversation stats:")
  print(f"  Total turns: {stats['total_turns']}")
  print(f"  Models used: {stats['models_used']}")
  ```
</CodeGroup>

## Function Calling with Routing

### Smart Routing with Tools

Combine smart routing with function calling:

<CodeGroup>
  ```python Python theme={null}
  import requests
  import json

  def get_weather(location: str) -> str:
      """Simulated weather function."""
      return f"The weather in {location} is sunny, 72°F"

  def calculate(expression: str) -> float:
      """Simulated calculator function."""
      try:
          return eval(expression)  # Don't use in production!
      except:
          return "Error"

  # Function definitions for the model
  tools = [
      {
          "type": "function",
          "function": {
              "name": "get_weather",
              "description": "Get current weather for a location",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "location": {
                          "type": "string",
                          "description": "City name"
                      }
                  },
                  "required": ["location"]
              }
          }
      },
      {
          "type": "function",
          "function": {
              "name": "calculate",
              "description": "Perform mathematical calculation",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "expression": {
                          "type": "string",
                          "description": "Math expression to evaluate"
                      }
                  },
                  "required": ["expression"]
              }
          }
      }
  ]

  # Chat with tools
  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "@edenai",
      # Router will consider tool compatibility
      "router_candidates": [
          "openai/gpt-4o",
          "anthropic/claude-sonnet-4-5",
          "google/gemini-2.5-flash"
      ],
      "messages": [
          {"role": "user", "content": "What's the weather in Paris and what's 15 * 23?"}
      ],
      "tools": tools
  }

  response = requests.post(url, headers=headers, json=payload)
  data = response.json()

  selected_model = data.get('model')
  print(f"Router selected: {selected_model}")

  message = data.get('choices', [{}])[0].get('message', {})
  full_response = message.get('content', '')
  tool_calls = message.get('tool_calls', [])

  print(f"Response: {full_response}")
  print(f"Tool calls: {tool_calls}")
  ```
</CodeGroup>

## Performance Optimization

### Strategy 1: Client-Side Caching

Cache routing decisions for repeated queries:

<CodeGroup>
  ```python Python theme={null}
  import requests
  import json
  import hashlib
  from typing import Optional, Dict
  from datetime import datetime, timedelta

  class CachedRouter:
      """Router with client-side caching of routing decisions."""

      def __init__(self, api_key: str, cache_ttl_seconds: int = 3600):
          self.api_key = api_key
          self.url = "https://api.edenai.run/v3/llm/chat/completions"
          self.cache_ttl = timedelta(seconds=cache_ttl_seconds)

          # Cache: query_hash -> (model, timestamp)
          self.routing_cache: Dict[str, tuple[str, datetime]] = {}

      def _hash_query(self, message: str, candidates: list[str]) -> str:
          """Create hash for caching."""
          cache_key = f"{message[:200]}|{'|'.join(sorted(candidates or []))}"
          return hashlib.md5(cache_key.encode()).hexdigest()

      def _get_cached_model(
          self,
          message: str,
          candidates: list[str]
      ) -> Optional[str]:
          """Get cached routing decision if valid."""
          cache_key = self._hash_query(message, candidates)

          if cache_key in self.routing_cache:
              model, timestamp = self.routing_cache[cache_key]
              age = datetime.now() - timestamp

              if age < self.cache_ttl:
                  print(f"[Cache hit] Using cached model: {model}")
                  return model
              else:
                  # Cache expired
                  del self.routing_cache[cache_key]

          return None

      def _cache_model(
          self,
          message: str,
          candidates: list[str],
          model: str
      ):
          """Cache routing decision."""
          cache_key = self._hash_query(message, candidates)
          self.routing_cache[cache_key] = (model, datetime.now())

      def chat(
          self,
          message: str,
          candidates: list[str] = None,
          use_cache: bool = True
      ) -> dict:
          """Chat with caching."""

          # Check cache first
          cached_model = None
          if use_cache:
              cached_model = self._get_cached_model(message, candidates or [])

          headers = {
              "Authorization": f"Bearer {self.api_key}",
              "Content-Type": "application/json"
          }

          # Use cached model if available
          if cached_model:
              payload = {
                  "model": cached_model,  # Use cached model directly
                  "messages": [{"role": "user", "content": message}]
              }
              used_routing = False
          else:
              payload = {
                  "model": "@edenai",  # Use routing
                  "messages": [{"role": "user", "content": message}]
              }
              if candidates:
                  payload["router_candidates"] = candidates
              used_routing = True

          response = requests.post(
              self.url,
              headers=headers,
              json=payload
          )

          data = response.json()
          selected_model = cached_model if cached_model else data.get('model')
          full_response = data.get('choices', [{}])[0].get('message', {}).get('content', '')

          # Cache the routing decision
          if used_routing and selected_model and use_cache:
              self._cache_model(message, candidates or [], selected_model)

          return {
              "response": full_response,
              "model": selected_model,
              "cached": not used_routing,
              "cache_size": len(self.routing_cache)
          }

  # Usage
  router = CachedRouter("YOUR_API_KEY", cache_ttl_seconds=3600)

  # First request - uses routing
  result1 = router.chat(
      "What is machine learning?",
      candidates=["openai/gpt-4o", "anthropic/claude-sonnet-4-5"]
  )
  print(f"First request: {result1['model']} (cached: {result1['cached']})")

  # Second identical request - uses cache
  result2 = router.chat(
      "What is machine learning?",
      candidates=["openai/gpt-4o", "anthropic/claude-sonnet-4-5"]
  )
  print(f"Second request: {result2['model']} (cached: {result2['cached']})")
  ```
</CodeGroup>

### Strategy 2: Parallel Requests with Routing

Make multiple routed requests in parallel:

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  import httpx
  import json

  async def routed_chat_async(
      api_key: str,
      message: str,
      candidates: list[str] = None
  ) -> dict:
      """Async chat with routing."""
      url = "https://api.edenai.run/v3/llm/chat/completions"
      headers = {
          "Authorization": f"Bearer {api_key}",
          "Content-Type": "application/json"
      }

      payload = {
          "model": "@edenai",
          "messages": [{"role": "user", "content": message}]
      }

      if candidates:
          payload["router_candidates"] = candidates

      async with httpx.AsyncClient(timeout=30.0) as client:
          response = await client.post(url, headers=headers, json=payload)
          data = response.json()

          selected_model = data.get('model')
          full_response = data.get('choices', [{}])[0].get('message', {}).get('content', '')

          return {
              "message": message,
              "response": full_response,
              "model": selected_model
          }

  async def batch_routed_requests(
      api_key: str,
      messages: list[str],
      candidates: list[str] = None
  ) -> list[dict]:
      """Process multiple messages in parallel with routing."""
      tasks = [
          routed_chat_async(api_key, msg, candidates)
          for msg in messages
      ]

      results = await asyncio.gather(*tasks)
      return results

  # Usage
  async def main():
      api_key = "YOUR_API_KEY"
      messages = [
          "What is Python?",
          "What is JavaScript?",
          "What is Rust?",
          "What is Go?",
          "What is TypeScript?"
      ]

      candidates = ["openai/gpt-4o", "anthropic/claude-sonnet-4-5"]

      print("Processing 5 requests in parallel...")
      results = await batch_routed_requests(api_key, messages, candidates)

      for result in results:
          print(f"\nQ: {result['message']}")
          print(f"Model: {result['model']}")
          print(f"A: {result['response'][:100]}...")

  # Run
  asyncio.run(main())
  ```
</CodeGroup>

## Production Deployment Patterns

### Pattern 1: Fallback to Fixed Model

Implement graceful fallback when routing fails:

<CodeGroup>
  ```python Python theme={null}
  import requests
  import json
  from typing import Optional

  class ResilientRouter:
      """Router with automatic fallback to fixed model."""

      def __init__(
          self,
          api_key: str,
          fallback_model: str = "openai/gpt-4o"
      ):
          self.api_key = api_key
          self.fallback_model = fallback_model
          self.url = "https://api.edenai.run/v3/llm/chat/completions"

      def chat(
          self,
          message: str,
          candidates: list[str] = None,
          timeout: int = 30
      ) -> dict:
          """Chat with automatic fallback."""

          headers = {
              "Authorization": f"Bearer {self.api_key}",
              "Content-Type": "application/json"
          }

          # Try routing first
          try:
              payload = {
                  "model": "@edenai",
                  "messages": [{"role": "user", "content": message}]
              }

              if candidates:
                  payload["router_candidates"] = candidates

              response = requests.post(
                  self.url,
                  headers=headers,
                  json=payload,
                  timeout=timeout
              )
              response.raise_for_status()

              data = response.json()
              selected_model = data.get('model')
              full_response = data.get('choices', [{}])[0].get('message', {}).get('content', '')

              return {
                  "response": full_response,
                  "model": selected_model,
                  "method": "routing",
                  "success": True
              }

          except Exception as e:
              print(f"[Warning] Routing failed: {e}")
              print(f"[Fallback] Using fixed model: {self.fallback_model}")

              # Fallback to fixed model
              try:
                  payload = {
                      "model": self.fallback_model,
                      "messages": [{"role": "user", "content": message}]
                  }

                  response = requests.post(
                      self.url,
                      headers=headers,
                      json=payload,
                      timeout=timeout
                  )
                  response.raise_for_status()

                  data = response.json()
                  full_response = data.get('choices', [{}])[0].get('message', {}).get('content', '')

                  return {
                      "response": full_response,
                      "model": self.fallback_model,
                      "method": "fallback",
                      "success": True,
                      "routing_error": str(e)
                  }

              except Exception as fallback_error:
                  return {
                      "response": None,
                      "model": None,
                      "method": "failed",
                      "success": False,
                      "error": str(fallback_error)
                  }

  # Usage
  router = ResilientRouter("YOUR_API_KEY", fallback_model="openai/gpt-4o")

  result = router.chat("Explain quantum computing")

  if result["success"]:
      print(f"Method: {result['method']}")
      print(f"Model: {result['model']}")
      print(f"Response: {result['response'][:100]}...")
  else:
      print(f"Failed: {result['error']}")
  ```
</CodeGroup>

## Best Practices Summary

### Cost Optimization

* ✅ Use tiered routing based on query complexity
* ✅ Track spending and adjust candidates dynamically
* ✅ Limit candidates to 3-5 models for faster routing
* ✅ Use budget models for simple queries
* ❌ Don't use premium-only candidates for all queries

### Performance

* ✅ Cache routing decisions at application level
* ✅ Use async/parallel requests for batch processing
* ✅ Set appropriate timeouts (30s recommended)
* ✅ Monitor routing latency in production
* ❌ Don't make synchronous serial requests

### Reliability

* ✅ Implement fallback to fixed models
* ✅ Handle routing failures gracefully
* ✅ Log routing errors for analysis
* ✅ Set up alerting for high failure rates
* ❌ Don't rely solely on routing without fallback

### Context Awareness

* ✅ Define use case-specific candidate pools
* ✅ Adjust candidates based on request characteristics
* ✅ Consider tools/functions in candidate selection
* ✅ Maintain conversation context across turns
* ❌ Don't use same candidates for all use cases

## Next Steps

* **[Getting Started](./getting-started)** - Review routing basics
* **[LLM Smart Routing](../llm/smart-routing)** - Practical LLM-specific patterns
* **[Cost Optimization Tutorial](../../tutorials/optimize-llm-costs)** - Complete cost optimization workflow


# Getting started
Source: https://docs.edenai.co/v3/how-to/router/getting-started



# Getting Started with Smart Routing

Learn how Eden AI's smart routing system automatically selects the best AI model for your requests.

## Overview

Smart routing is Eden AI's intelligent model selection system that automatically chooses the optimal AI model for your requests. Instead of manually selecting models, you use the special identifier `@edenai` and let the system analyze your request to pick the best provider and model.

**What you'll learn:**

* How smart routing works
* Basic usage with default models
* Customizing candidate pools
* Understanding routing decisions
* When to use smart routing vs. fixed models

## How It Works

The routing system follows this flow:

```text theme={null}
Your Request with model: "@edenai"
        ↓
Eden AI Router Service
        ↓
Analyze request context:
- Message content
- Tools/functions
- Request parameters
        ↓
Query NotDiamond API
        ↓
Select optimal model
        ↓
Execute request with selected model
        ↓
Response (includes selected model info)
```

**Key components:**

1. **NotDiamond Integration** - Powered by [NotDiamond](https://notdiamond.ai/), an AI routing engine that analyzes request context
2. **Model Inventory** - Database of available models with capabilities and pricing
3. **Redis Cache** - Caches available models (1-hour TTL) for performance
4. **Validation Layer** - Ensures models are available and properly formatted

## Basic Usage

### Quick Start: Default Routing

The simplest way to use smart routing is to set `model: "@edenai"` without specifying candidates. The system will choose from all available models.

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
  "Authorization": "Bearer YOUR_API_KEY",
  "Content-Type": "application/json"
  }

  payload = {
  "model": "@edenai", # Activates smart routing
  "messages": [
  {"role": "user", "content": "Explain machine learning"}
  ]
  }

  response = requests.post(url, headers=headers, json=payload)
  data = response.json()

  # Get the selected model
  selected_model = data.get('model')
  print(f"Router selected: {selected_model}")

  # Process content
  content = data.get('choices', [{}])[0].get('message', {}).get('content', '')
  print(content)
  ```

  ```javascript JavaScript theme={null}
  const url = 'https://api.edenai.run/v3/llm/chat/completions';
  const headers = {
    'Authorization': 'Bearer YOUR_API_KEY',
    'Content-Type': 'application/json'
  };

  const payload = {
    model: '@edenai',  // Activates smart routing
    messages: [
      {role: 'user', content: 'Explain machine learning'}
    ]
  };

  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(payload)
  });

  const data = await response.json();

  // Get the selected model
  const selectedModel = data.model;
  console.log(`Router selected: ${selectedModel}`);

  // Process content
  const content = data.choices?.[0]?.message?.content || '';
  console.log(content);
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.edenai.run/v3/llm/chat/completions \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "@edenai",
      "messages": [
        {"role": "user", "content": "Explain machine learning"}
      ]
    }'
  ```
</CodeGroup>

**Response includes selected model:**

```json theme={null}
{"id":"...","model":"openai/gpt-4o","choices":[{"message":{"content":"Machine learning is..."},...}],...}
```

### Custom Candidate Pool

Restrict routing to specific models using `router_candidates`:

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/llm/chat/completions"
  headers = {
  "Authorization": "Bearer YOUR_API_KEY",
  "Content-Type": "application/json"
  }

  payload = {
  "model": "@edenai", # Only choose from these models
  "router_candidates": [
  "openai/gpt-4o",
  "anthropic/claude-sonnet-4-5",
  "google/gemini-2.5-flash"
  ],
  "messages": [
  {"role": "user", "content": "Write a Python function to sort a list"}
  ]
  }

  response = requests.post(url, headers=headers, json=payload)
  data = response.json()

  # Get the selected model
  selected_model = data.get('model')
  print(f"Router selected: {selected_model}")

  # Process content
  content = data.get('choices', [{}])[0].get('message', {}).get('content', '')
  print(content)
  ```

  ```javascript JavaScript theme={null}
  const payload = {
    model: '@edenai',
    // Only choose from these models
    router_candidates: [
      'openai/gpt-4o',
      'anthropic/claude-sonnet-4-5',
      'google/gemini-2.5-flash'
    ],
    messages: [
      {role: 'user', content: 'Write a Python function to sort a list'}
    ]
  };

  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(payload)
  });

  const data = await response.json();

  // Get the selected model
  const selectedModel = data.model;
  console.log(`Router selected: ${selectedModel}`);

  // Process content
  const content = data.choices?.[0]?.message?.content || '';
  console.log(content);
  ```
</CodeGroup>

**Benefits of custom candidates:**

* Control over which models can be selected
* Cost optimization by limiting to budget-friendly models
* Quality control by restricting to tested models
* Use case optimization (e.g., code-focused models for coding tasks)

## Model Format

Models are specified in the format:

```

provider/model

```

**Examples:**

* `openai/gpt-4o`
* `anthropic/claude-sonnet-4-5`
* `google/gemini-2.5-flash`
* `cohere/command-r-plus`

**Finding available models:**
Use the `/v3/llm/models` endpoint to list all available models:

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/llm/models"
  headers = {"Authorization": "Bearer YOUR_API_KEY"}

  response = requests.get(url, headers=headers)
  models = response.json()

  # List all models
  for model in models['data']:
      print(f"{model['id']} - {model['description']}")
      print(f"  Context: {model['context_length']} tokens")
      print(f"  Pricing: {model['pricing']}")
      print()
  ```

  ```javascript JavaScript theme={null}
  const url = 'https://api.edenai.run/v3/llm/models';
  const headers = {'Authorization': 'Bearer YOUR_API_KEY'};

  const response = await fetch(url, {headers});
  const models = await response.json();

  // List all models
  for (const model of models.data) {
    console.log(`${model.id} - ${model.description}`);
    console.log(`  Context: ${model.context_length} tokens`);
    console.log(`  Pricing:`, model.pricing);
  }
  ```
</CodeGroup>

## Routing with OpenAI SDK

Smart routing works seamlessly with the official OpenAI SDK:

<CodeGroup>
  ```python Python (OpenAI SDK) theme={null}
  from openai import OpenAI

  client = OpenAI(
      api_key="YOUR_EDEN_AI_KEY",
      base_url="https://api.edenai.run/v3/llm"
  )

  # Default routing
  response = client.chat.completions.create(
      model="@edenai",
      messages=[
          {"role": "user", "content": "Explain neural networks"}
      ]
  )

  print(f"Router selected: {response.model}")
  print(response.choices[0].message.content)
  ```

  ```python Python (OpenAI SDK with candidates) theme={null}
  from openai import OpenAI

  client = OpenAI(
      api_key="YOUR_EDEN_AI_KEY",
      base_url="https://api.edenai.run/v3/llm"
  )

  # Custom candidates via extra_body
  response = client.chat.completions.create(
      model="@edenai",
      messages=[
          {"role": "user", "content": "Write a haiku about coding"}
      ],
      extra_body={
          "router_candidates": [
              "openai/gpt-4o",
              "anthropic/claude-sonnet-4-5"
          ]
      }
  )

  print(f"Router selected: {response.model}")
  print(response.choices[0].message.content)
  ```

  ```typescript TypeScript (OpenAI SDK) theme={null}
  import OpenAI from 'openai';

  const client = new OpenAI({
    apiKey: process.env.EDEN_AI_KEY,
    baseURL: 'https://api.edenai.run/v3/llm'
  });

  // Custom candidates
  const response = await client.chat.completions.create({
    model: '@edenai',
    messages: [
      {role: 'user', content: 'Write a haiku about coding'}
    ],
    // @ts-ignore - extra_body not in types
    extra_body: {
      router_candidates: [
        'openai/gpt-4o',
        'anthropic/claude-sonnet-4-5'
      ]
    }
  });

  console.log(`Router selected: ${response.model}`);
  console.log(response.choices[0]?.message?.content || '');
  ```
</CodeGroup>

## When to Use Smart Routing

### Use Smart Routing When:

✅ **Optimizing cost/performance** - Let the system balance quality and cost
✅ **Exploring new use cases** - Don't know which model works best yet
✅ **Handling diverse requests** - Different queries need different models
✅ **Minimizing maintenance** - No need to update code when better models launch
✅ **A/B testing models** - Compare routing vs. fixed model performance

### Use Fixed Models When:

❌ **Strict latency requirements** - Routing adds 100-500ms overhead
❌ **High-frequency APIs** - 100+ requests/second may hit router limits
❌ **Compliance requirements** - Must use specific certified models
❌ **Consistent output format** - Need identical behavior across requests
❌ **Already optimized** - You've tested and know the best model for your use case

## Understanding Routing Latency

Smart routing introduces a small overhead:

| Phase                 | Latency       | Notes                                 |
| --------------------- | ------------- | ------------------------------------- |
| **Routing decision**  | 100-500ms     | Analyzing request and selecting model |
| **First token**       | +routing time | First token includes routing overhead |
| **Subsequent tokens** | No overhead   | Normal streaming after first token    |

**Example timeline:**

````

Request sent → [300ms routing] → [500ms first token] → [streaming...]
Total to first token: ~800ms

```

**Compare with fixed model:**
```

Request sent → [500ms first token] → [streaming...]
Total to first token: ~500ms

````

**Optimization tips:**

* Use custom candidates (3-5 models) to reduce routing time
* Cache routing decisions at application level for repeated queries
* Consider fixed models for latency-critical applications

## Error Handling

The router has built-in fallback mechanisms:

<CodeGroup>
  ```python Python theme={null}
  import requests

  def chat_with_router(message: str):
      """Chat with router and handle errors."""
      url = "https://api.edenai.run/v3/llm/chat/completions"
      headers = {
          "Authorization": f"Bearer {API_KEY}",
          "Content-Type": "application/json"
      }

      payload = {
          "model": "@edenai",
          "messages": [{"role": "user", "content": message}]
      }

      try:
          response = requests.post(
              url,
              headers=headers,
              json=payload,
              timeout=30  # Set timeout
          )
          response.raise_for_status()

          data = response.json()
          content = data.get('choices', [{}])[0].get('message', {}).get('content', '')

          return {"success": True, "response": content}

      except requests.exceptions.Timeout:
          return {"success": False, "error": "Routing timed out"}
      except requests.exceptions.HTTPError as e:
          return {"success": False, "error": f"HTTP error: {e}"}
      except Exception as e:
          return {"success": False, "error": f"Unexpected error: {e}"}

  # Usage
  result = chat_with_router("Hello!")
  if result["success"]:
      print(result["response"])
  else:
      print(f"Error: {result['error']}")
  ```
</CodeGroup>

**Common errors:**

* `503 Service Unavailable` - Router service temporarily down
* `422 Validation Error` - Invalid model candidates
* `Timeout` - Routing took too long (>30s)

## Best Practices

### 1. Choose Appropriate Candidates

✅ **Do:**

* Limit to 3-5 models for faster routing
* Group models by similar capabilities
* Test candidates with your specific workload
* Include at least one budget-friendly option

❌ **Don't:**

* Specify 20+ candidates (slows routing)
* Mix specialized models (code + creative)
* Use untested models in production

### 2. Monitor Performance

✅ **Do:**

* Track which models get selected
* Monitor routing latency
* A/B test routing vs. fixed models
* Set up alerts for routing failures

❌ **Don't:**

* Deploy without monitoring
* Assume routing is always optimal
* Ignore cost patterns

### 3. Handle Errors Gracefully

✅ **Do:**

* Set appropriate timeouts (30s recommended)
* Implement fallback to fixed models
* Log routing failures for analysis
* Retry with exponential backoff

❌ **Don't:**

* Use infinite timeouts
* Ignore routing errors
* Rely solely on routing without fallback

## Next Steps

* **[Advanced Usage](./advanced-usage)** - Learn advanced routing patterns and optimization strategies
* **[LLM Smart Routing](../llm/smart-routing)** - Practical LLM-specific examples and use cases
* **[Chat Completions](../llm/chat-completions)** - Master the LLM endpoint

## Quick Reference

### Request Parameters

| Parameter           | Type      | Required | Description                                         |
| ------------------- | --------- | -------- | --------------------------------------------------- |
| `model`             | string    | Yes      | Set to `"@edenai"` to activate routing              |
| `router_candidates` | string\[] | No       | List of models to choose from (default: all models) |
| `messages`          | object\[] | Yes      | Conversation messages (used for routing context)    |
| `tools`             | object\[] | No       | Function definitions (considered in routing)        |
| `stream`            | boolean   | No       | Set to `true` for streaming responses               |

### Response Fields

The selected model is returned in the response:

```json theme={null}
{
  "id": "chatcmpl-...",
  "model": "openai/gpt-4o",  // Selected model
  "choices": [...]
}
```

### Supported Features

Smart routing works with all V3 LLM features:

* ✅ Streaming
* ✅ Function calling / Tools
* ✅ Vision / Multimodal
* ✅ Multi-turn conversations
* ✅ System messages
* ✅ Temperature and other parameters


# Getting started
Source: https://docs.edenai.co/v3/how-to/universal-ai/getting-started



# Getting Started with Universal AI

The Universal AI endpoint is the core of Eden AI V3, providing a single unified endpoint for all non-LLM AI features.

## Overview

Instead of calling different endpoints for different features, V3's Universal AI endpoint handles everything through model strings:

```
POST /v3/universal-ai
```

**One endpoint for:**

* Text analysis (moderation, AI detection, embeddings, sentiment)
* OCR (text extraction, invoice/ID parsing)
* Image processing (generation, detection, analysis)
* Translation (document translation)

## Model String Format

The model string tells the endpoint what feature and provider to use:

```
feature/subfeature/provider[/model]
```

**Examples:**

* `text/moderation/google`
* `ocr/financial_parser/google`
* `image/generation/openai/dall-e-3`
* `translation/document_translation/deepl`

## Basic Request

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/universal-ai"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "text/moderation/openai",
      "input": {
          "text": "This is sample text to moderate"
      }
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  print(result)
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.edenai.run/v3/universal-ai \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "text/moderation/openai",
      "input": {"text": "Sample text"}
    }'
  ```
</CodeGroup>

## Response Format

All Universal AI responses follow the same structure:

```json theme={null}
{
  "status": "success",
  "cost": 0.0001,
  "provider": "openai",
  "feature": "text",
  "subfeature": "moderation",
  "output": {
    // Feature-specific output
  }
}
```

## Input Formats

The `input` field varies based on the feature:

### Text-Based Features

```json theme={null}
{
  "model": "text/moderation/google",
  "input": {
    "text": "Text to moderate"
  }
}
```

### File-Based Features (UUID)

```json theme={null}
{
  "model": "ocr/financial_parser/google",
  "input": {
    "file": "550e8400-e29b-41d4-a716-446655440000"
  }
}
```

### File-Based Features (URL)

```json theme={null}
{
  "model": "image/object_detection/google",
  "input": {
    "file": "https://example.com/image.jpg"
  }
}
```

## Common Use Cases

### Text Moderation

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/universal-ai"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "text/moderation/openai",
      "input": {"text": "Content to moderate"}
  }
      
  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
      
  if result["output"]["nsfw_likelihood"] > 3:
      print("Content flagged as inappropriate")
  ```
</CodeGroup>

### OCR Text Extraction

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/universal-ai"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  # First upload the file
  upload_response = requests.post(
      "https://api.edenai.run/v3/upload",
      headers={"Authorization": "Bearer YOUR_API_KEY"},
      files={"file": open("document.pdf", "rb")}
  )
  file_id = upload_response.json()["file_id"]

  # Then use it in Universal AI
  payload = {
      "model": "ocr/financial_parser/google",
      "input": {"file": file_id, "language": "en"}
  }
      
  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  print(result["output"]["extracted_data"])
  ```
</CodeGroup>

## Next Steps

* [Text Features](./text-features) - All text analysis capabilities
* [OCR Features](./ocr-features) - Document processing
* [Image Features](./image-features) - Image generation and analysis
* [Multimodal Workflows](./multimodal-features) - Complex processing pipelines


# Image features
Source: https://docs.edenai.co/v3/how-to/universal-ai/image-features



# Universal AI: Image Features

Process and analyze images using the Universal AI endpoint.

## Available Image Features

| Subfeature                 | Model String Pattern                | Description                |
| -------------------------- | ----------------------------------- | -------------------------- |
| Generation                 | `image/generation/provider/model`   | Create AI-generated images |
| Object Detection           | `image/object_detection/provider`   | Identify objects in images |
| Face Detection             | `image/face_detection/provider`     | Detect faces in images     |
| Face Comparison            | `image/face_comparison/provider`    | Compare face similarity    |
| Background Removal         | `image/background_removal/provider` | Remove image backgrounds   |
| Explicit Content Detection | `image/explicit_content/provider`   | Detect NSFW content        |
| AI Detection               | `image/ai_detection/provider`       | Detect AI-generated images |

## Image Generation

Generate images from text descriptions:

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/universal-ai"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "image/generation/openai/dall-e-3",
      "input": {
          "text": "A serene mountain landscape at sunset with a crystal clear lake",
          "resolution": "1024x1024",
          "num_images": 1
      }
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()

  image_url = result["output"]["items"][0]["image_resource_url"]
  print(f"Generated image: {image_url}")
  ```
</CodeGroup>

## Object Detection

Detect and identify objects in images:

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/universal-ai"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  # Upload image
  upload_url = "https://api.edenai.run/v3/upload"
  upload_headers = {"Authorization": "Bearer YOUR_API_KEY"}
      
  files = {"file": open("photo.jpg", "rb")}
  upload_response = requests.post(upload_url, headers=upload_headers, files=files)
  file_id = upload_response.json()["file_id"]

  # Detect objects
  payload = {
      "model": "image/object_detection/google",
      "input": {
          "file": file_id
      }
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()

  for obj in result["output"]["items"]:
      print(f"Object: {obj['label']} (confidence: {obj['confidence']})")
  ```
</CodeGroup>

## Face Detection

Detect faces and facial attributes:

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/universal-ai"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }
  upload_url = "https://api.edenai.run/v3/upload"
  upload_headers = {"Authorization": "Bearer YOUR_API_KEY"}

  # Upload image
  files = {"file": open("people.jpg", "rb")}
  upload_response = requests.post(upload_url, headers=upload_headers, files=files)
  file_id = upload_response.json()["file_id"]

  # Detect faces
  payload = {
      "model": "image/face_detection/amazon",
      "input": {
          "file": file_id
      }
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()

  for face in result["output"]["items"]:
      print(f"Face detected at: {face['bounding_box']}")
      print(f"  Age: {face.get('age')}")
      print(f"  Gender: {face.get('gender')}")
      print(f"  Emotions: {face.get('emotions')}")
  ```
</CodeGroup>

## Background Removal

Remove backgrounds from images:

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/universal-ai"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }
  upload_url = "https://api.edenai.run/v3/upload"
  upload_headers = {"Authorization": "Bearer YOUR_API_KEY"}

  # Upload image
  files = {"file": open("product.jpg", "rb")}
  upload_response = requests.post(upload_url, headers=upload_headers, files=files)
  file_id = upload_response.json()["file_id"]

  # Remove background
  payload = {
      "model": "image/background_removal/photoroom",
      "input": {
          "file": file_id
      }
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()

  # Download the result
  processed_url = result["output"]["image_resource_url"]
  print(f"Background removed image: {processed_url}")
  ```
</CodeGroup>

## Using Image URLs

You can also provide image URLs instead of uploading:

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/universal-ai"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "image/object_detection/google",
      "input": {
          "file": "https://example.com/image.jpg"
      }
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  ```
</CodeGroup>

## Next Steps

* [Upload Files](../upload/upload-files) - Manage image uploads
* [Text Features](./text-features) - Text analysis
* [OCR Features](./ocr-features) - Document processing


# Multimodal features
Source: https://docs.edenai.co/v3/how-to/universal-ai/multimodal-features



# Multimodal Workflows

Combine multiple Universal AI features to build powerful processing pipelines.

## Overview

Universal AI's multimodal workflows enable you to:

* Chain multiple AI features together
* Process files through multiple stages
* Combine text, image, and document analysis
* Build complex automation pipelines

Unlike LLM multimodal (which focuses on conversational understanding of media), Universal AI multimodal workflows are about **processing pipelines** and **structured data extraction**.

## Workflow Patterns

### Sequential Processing

Process data through multiple features in sequence:

```
Input File → OCR → Translation → Summary
Image → Detection → Classification → Analysis
```

### Parallel Processing

Run multiple features simultaneously:

```
Document → [OCR, Identity Parser, Invoice Parser] → Aggregate Results
Image → [Object Detection, Face Detection, Explicit Content] → Combined Analysis
```

### Conditional Routing

Route to different features based on results:

```
Image → Moderation → [If safe: Generate Caption | If unsafe: Flag for Review]
Text → AI Detection → [If AI: Analyze Further | If Human: Skip]
```

## Common Multimodal Workflows

### Document Processing Pipeline

Extract text from documents and analyze it:

<CodeGroup>
  ```python Python theme={null}
  import requests

  def process_document_workflow(file_path):
      """Complete document processing: OCR → Analysis."""

      # Step 1: Upload file
      upload_url = "https://api.edenai.run/v3/upload"
      upload_headers = {"Authorization": "Bearer YOUR_API_KEY"}

      files = {"file": open(file_path, "rb")}
      upload_response = requests.post(upload_url, headers=upload_headers, files=files)
      file_id = upload_response.json()["file_id"]

      print(f"Uploaded file: {file_id}")

      # Step 2: Extract text with OCR
      universal_ai_url = "https://api.edenai.run/v3/universal-ai"
      headers = {
          "Authorization": "Bearer YOUR_API_KEY",
          "Content-Type": "application/json"
      }

      ocr_payload = {
          "model": "ocr/ocr/google",
          "input": {"file": file_id, "language": "en"}
      }

      ocr_response = requests.post(universal_ai_url, headers=headers, json=ocr_payload)
      extracted_text = ocr_response.json()["output"]["text"]

      print(f"Extracted text: {extracted_text[:100]}...")

      # Step 3: Extract topics from the text
      topic_payload = {
          "model": "text/topic_extraction/openai",
          "input": {"text": extracted_text}
      }

      topic_response = requests.post(
          universal_ai_url,
          headers=headers,
          json=topic_payload
      )
      topics = topic_response.json()["output"]

      print(f"Topics: {topics}")

      return {
          "extracted_text": extracted_text,
          "topics": topics
      }

  # Usage
  result = process_document_workflow("document.pdf")
  ```
</CodeGroup>

### Image Content Moderation Pipeline

Screen images through multiple checks:

<CodeGroup>
  ```python Python theme={null}
  import requests

  def moderate_image_workflow(image_path):
      """Multi-stage image moderation pipeline."""

      # Upload image
      upload_response = requests.post(
          "https://api.edenai.run/v3/upload",
          headers={"Authorization": "Bearer YOUR_API_KEY"},
          files={"file": open(image_path, "rb")}
      )
      file_id = upload_response.json()["file_id"]

      url = "https://api.edenai.run/v3/universal-ai"
      headers = {
          "Authorization": "Bearer YOUR_API_KEY",
          "Content-Type": "application/json"
      }

      # Stage 1: Explicit content detection
      explicit_payload = {
          "model": "image/explicit_content/google",
          "input": {"file": file_id}
      }
      explicit_response = requests.post(url, headers=headers, json=explicit_payload)
      explicit_result = explicit_response.json()["output"]

      print(f"Explicit content likelihood: {explicit_result.get('nsfw_likelihood', 0)}")

      # Stage 2: Face detection (check for people)
      face_payload = {
          "model": "image/face_detection/amazon",
          "input": {"file": file_id}
      }
      face_response = requests.post(url, headers=headers, json=face_payload)
      faces = face_response.json()["output"].get("faces", [])

      print(f"Faces detected: {len(faces)}")

      # Stage 3: Object detection
      object_payload = {
          "model": "image/object_detection/google",
          "input": {"file": file_id}
      }
      object_response = requests.post(url, headers=headers, json=object_payload)
      objects = object_response.json()["output"].get("items", [])

      print(f"Objects detected: {len(objects)}")

      # Aggregate results
      moderation_result = {
          "safe": explicit_result.get("nsfw_likelihood", 0) < 3,
          "has_people": len(faces) > 0,
          "detected_objects": [obj["label"] for obj in objects],
          "moderation_score": explicit_result.get("nsfw_likelihood", 0),
          "details": {
              "explicit_content": explicit_result,
              "faces": faces,
              "objects": objects
          }
      }

      return moderation_result

  # Usage
  result = moderate_image_workflow("user_upload.jpg")

  if result["safe"]:
      print("✓ Image approved")
  else:
      print("✗ Image flagged for review")
  ```
</CodeGroup>

### Invoice Processing Workflow

Extract and validate invoice data:

<CodeGroup>
  ```python Python theme={null}
  import requests
  from datetime import datetime

  def process_invoice_workflow(invoice_path):
      """Complete invoice processing with validation."""

      # Upload invoice
      upload_response = requests.post(
          "https://api.edenai.run/v3/upload",
          headers={"Authorization": "Bearer YOUR_API_KEY"},
          files={"file": open(invoice_path, "rb")}
      )
      file_id = upload_response.json()["file_id"]

      url = "https://api.edenai.run/v3/universal-ai"
      headers = {
          "Authorization": "Bearer YOUR_API_KEY",
          "Content-Type": "application/json"
      }

      # Stage 1: Parse invoice with financial parser
      parser_payload = {
          "model": "ocr/financial_parser/microsoft",
          "input": {"file": file_id, "language": "en"}
      }
      parser_response = requests.post(url, headers=headers, json=parser_payload)
      extracted_data = parser_response.json()["output"]["extracted_data"]

      # Stage 2: OCR for additional text extraction
      ocr_payload = {
          "model": "ocr/ocr/google",
          "input": {"file": file_id, "language": "en"}
      }
      ocr_response = requests.post(url, headers=headers, json=ocr_payload)
      full_text = ocr_response.json()["output"]["text"]

      # Stage 3: Validate data consistency
      invoice_data = extracted_data[0] if extracted_data else {}
      merchant = invoice_data.get("merchant_information", {})
      payment = invoice_data.get("payment_information", {})
      doc_info = invoice_data.get("financial_document_information", {})

      validation_results = {
          "has_merchant": bool(merchant.get("name")),
          "has_total": bool(payment.get("total")),
          "has_date": bool(doc_info.get("invoice_date")),
          "has_text": len(full_text) > 0
      }

      # Calculate completeness score
      completeness = sum(validation_results.values()) / len(validation_results) * 100

      return {
          "extracted_data": extracted_data,
          "full_text": full_text,
          "validation": validation_results,
          "completeness_score": completeness,
          "is_valid": completeness >= 75
      }

  # Usage
  result = process_invoice_workflow("invoice.pdf")

  if result["is_valid"]:
      print(f"✓ Invoice processed ({result['completeness_score']:.0f}% complete)")
  else:
      print(f"✗ Invoice incomplete ({result['completeness_score']:.0f}% complete)")
      print("  Missing fields:", [k for k, v in result['validation'].items() if not v])
  ```
</CodeGroup>

### Multi-Analysis Text Pipeline

Run multiple analyses on the same text:

<CodeGroup>
  ```python Python theme={null}
  import requests

  def multi_analysis_workflow(text):
      """Run moderation, topic extraction, and NER on the same text."""

      url = "https://api.edenai.run/v3/universal-ai"
      headers = {
          "Authorization": "Bearer YOUR_API_KEY",
          "Content-Type": "application/json"
      }

      results = {}

      # Stage 1: Moderate content
      moderation_payload = {
          "model": "text/moderation/openai",
          "input": {"text": text}
      }
      mod_response = requests.post(url, headers=headers, json=moderation_payload)
      results["moderation"] = mod_response.json()["output"]

      print(f"NSFW likelihood: {results['moderation']['nsfw_likelihood']}")

      # Stage 2: Extract topics
      topic_payload = {
          "model": "text/topic_extraction/openai",
          "input": {"text": text}
      }
      topic_response = requests.post(url, headers=headers, json=topic_payload)
      results["topics"] = topic_response.json()["output"]

      print(f"Topics: {results['topics']}")

      # Stage 3: Named entity recognition
      ner_payload = {
          "model": "text/named_entity_recognition/openai",
          "input": {"text": text}
      }
      ner_response = requests.post(url, headers=headers, json=ner_payload)
      results["entities"] = ner_response.json()["output"]

      print(f"Entities: {results['entities']}")

      return results

  # Usage
  results = multi_analysis_workflow(
      "Apple announced a new iPhone at their Cupertino headquarters today."
  )
  ```
</CodeGroup>

## Advanced Patterns

### Parallel Feature Execution

Run multiple features simultaneously for faster processing:

<CodeGroup>
  ```python Python theme={null}
  import requests
  import asyncio
  import aiohttp

  async def analyze_text_parallel(text):
      """Run multiple text analyses in parallel."""

      url = "https://api.edenai.run/v3/universal-ai"
      headers = {
          "Authorization": "Bearer YOUR_API_KEY",
          "Content-Type": "application/json"
      }

      # Define all analyses to run
      analyses = [
          {"name": "topics", "model": "text/topic_extraction/openai"},
          {"name": "moderation", "model": "text/moderation/openai"},
          {"name": "moderation_google", "model": "text/moderation/google"},
          {"name": "entities", "model": "text/named_entity_recognition/openai"}
      ]

      async def run_analysis(session, analysis):
          """Run single analysis."""
          payload = {
              "model": analysis["model"],
              "input": {"text": text}
          }

          async with session.post(url, headers=headers, json=payload) as response:
              result = await response.json()
              return {analysis["name"]: result["output"]}

      # Run all analyses in parallel
      async with aiohttp.ClientSession() as session:
          tasks = [run_analysis(session, analysis) for analysis in analyses]
          results = await asyncio.gather(*tasks)

      # Combine results
      combined = {}
      for result in results:
          combined.update(result)

      return combined

  # Usage
  results = asyncio.run(analyze_text_parallel(
      "This is an amazing product that will revolutionize the industry!"
  ))

  print("Topics:", results["topics"])
  print("Moderation:", results["moderation"])
  print("Moderation (Google):", results["moderation_google"]["nsfw_likelihood"])
  print("Entities:", results["entities"])
  ```
</CodeGroup>

### Conditional Workflows

Route based on analysis results:

<CodeGroup>
  ```python Python theme={null}
  import requests

  def smart_content_workflow(text):
      """Process content with conditional routing."""

      url = "https://api.edenai.run/v3/universal-ai"
      headers = {
          "Authorization": "Bearer YOUR_API_KEY",
          "Content-Type": "application/json"
      }

      # Step 1: Moderate content
      moderation_payload = {
          "model": "text/moderation/google",
          "input": {"text": text}
      }
      mod_response = requests.post(url, headers=headers, json=moderation_payload)
      mod_output = mod_response.json()["output"]
      is_flagged = mod_output["nsfw_likelihood"] >= 3

      workflow_result = {"is_flagged": is_flagged, "moderation": mod_output}

      if is_flagged:
          # Flagged content → Log for review
          print("Content flagged, logging for review...")

          workflow_result["action"] = "review"

      else:
          # Safe content → Run sentiment analysis
          print("Content is safe, analyzing sentiment...")

          sentiment_payload = {
              "model": "text/topic_extraction/openai",
              "input": {"text": text}
          }
          sentiment_response = requests.post(url, headers=headers, json=sentiment_payload)
          workflow_result["sentiment"] = sentiment_response.json()["output"]

      return workflow_result

  # Usage
  result = smart_content_workflow("This is sample content to analyze.")
  ```
</CodeGroup>

### Iterative Refinement

Refine results through multiple passes:

<CodeGroup>
  ```python Python theme={null}
  import requests

  def iterative_ocr_workflow(image_path, max_iterations=3):
      """Improve OCR accuracy through iterative processing."""

      # Upload image
      upload_response = requests.post(
          "https://api.edenai.run/v3/upload",
          headers={"Authorization": "Bearer YOUR_API_KEY"},
          files={"file": open(image_path, "rb")}
      )
      file_id = upload_response.json()["file_id"]

      url = "https://api.edenai.run/v3/universal-ai"
      headers = {
          "Authorization": "Bearer YOUR_API_KEY",
          "Content-Type": "application/json"
      }

      # Try multiple providers and combine results
      providers = ["google", "amazon", "microsoft"]
      all_results = []

      for provider in providers:
          ocr_payload = {
              "model": f"ocr/ocr/{provider}",
              "input": {"file": file_id, "language": "en"}
          }

          response = requests.post(url, headers=headers, json=ocr_payload)
          if response.status_code == 200:
              text = response.json()["output"]["text"]
              all_results.append({
                  "provider": provider,
                  "text": text,
                  "length": len(text)
              })

      # Select best result (longest text = most complete)
      best_result = max(all_results, key=lambda x: x["length"])

      return {
          "best_text": best_result["text"],
          "best_provider": best_result["provider"],
          "all_results": all_results
      }

  # Usage
  result = iterative_ocr_workflow("complex_document.jpg")
  print(f"Best provider: {result['best_provider']}")
  print(f"Extracted text: {result['best_text'][:200]}...")
  ```
</CodeGroup>

## Real-World Workflow Examples

### E-commerce Product Processing

Process product images and descriptions:

<CodeGroup>
  ```python Python theme={null}
  import requests

  def process_product_workflow(image_path, description):
      """Complete product processing workflow."""

      # Upload product image
      upload_response = requests.post(
          "https://api.edenai.run/v3/upload",
          headers={"Authorization": "Bearer YOUR_API_KEY"},
          files={"file": open(image_path, "rb")}
      )
      file_id = upload_response.json()["file_id"]

      url = "https://api.edenai.run/v3/universal-ai"
      headers = {
          "Authorization": "Bearer YOUR_API_KEY",
          "Content-Type": "application/json"
      }

      # 1. Moderate image
      moderation_payload = {
          "model": "image/explicit_content/google",
          "input": {"file": file_id}
      }
      moderation_response = requests.post(url, headers=headers, json=moderation_payload)
      is_safe = moderation_response.json()["output"]["nsfw_likelihood"] < 3

      # 2. Detect objects in image
      detection_payload = {
          "model": "image/object_detection/google",
          "input": {"file": file_id}
      }
      detection_response = requests.post(url, headers=headers, json=detection_payload)
      detected_objects = detection_response.json()["output"]["items"]

      # 3. Extract topics from description
      topic_payload = {
          "model": "text/topic_extraction/openai",
          "input": {"text": description}
      }
      topic_response = requests.post(url, headers=headers, json=topic_payload)
      topics = topic_response.json()["output"]

      # 4. Moderate description text
      text_moderation_payload = {
          "model": "text/moderation/google",
          "input": {"text": description}
      }
      text_mod_response = requests.post(url, headers=headers, json=text_moderation_payload)
      text_mod_output = text_mod_response.json()["output"]
      description_safe = text_mod_output["nsfw_likelihood"] < 3

      return {
          "image_safe": is_safe,
          "detected_objects": [obj["label"] for obj in detected_objects],
          "description_topics": topics,
          "description_safe": description_safe,
          "approved": is_safe and description_safe
      }

  # Usage
  result = process_product_workflow(
      "product.jpg",
      "Amazing product with incredible features!"
  )

  if result["approved"]:
      print("✓ Product approved for listing")
  else:
      print("✗ Product requires review")
  ```
</CodeGroup>

### Content Moderation Pipeline

Comprehensive content screening:

<CodeGroup>
  ```python Python theme={null}
  import requests

  def comprehensive_moderation_workflow(content_type, file_path=None, text=None):
      """Multi-stage moderation for various content types."""

      url = "https://api.edenai.run/v3/universal-ai"
      headers = {
          "Authorization": "Bearer YOUR_API_KEY",
          "Content-Type": "application/json"
      }

      moderation_results = {}

      if content_type == "text":
          # Text moderation
          text_mod_payload = {
              "model": "text/moderation/openai",
              "input": {"text": text}
          }
          response = requests.post(url, headers=headers, json=text_mod_payload)
          moderation_results["text_moderation"] = response.json()["output"]

          # Additional moderation with Google
          google_mod_payload = {
              "model": "text/moderation/google",
              "input": {"text": text}
          }
          response = requests.post(url, headers=headers, json=google_mod_payload)
          moderation_results["moderation_google"] = response.json()["output"]

      elif content_type == "image":
          # Upload image
          upload_response = requests.post(
              "https://api.edenai.run/v3/upload",
              headers={"Authorization": "Bearer YOUR_API_KEY"},
              files={"file": open(file_path, "rb")}
          )
          file_id = upload_response.json()["file_id"]

          # Explicit content detection
          explicit_payload = {
              "model": "image/explicit_content/google",
              "input": {"file": file_id}
          }
          response = requests.post(url, headers=headers, json=explicit_payload)
          moderation_results["explicit_content"] = response.json()["output"]

          # Face detection
          face_payload = {
              "model": "image/face_detection/amazon",
              "input": {"file": file_id}
          }
          response = requests.post(url, headers=headers, json=face_payload)
          moderation_results["faces"] = response.json()["output"]

      # Calculate overall safety score
      if content_type == "text":
          safe = moderation_results["text_moderation"]["nsfw_likelihood"] < 3
      else:
          safe = moderation_results["explicit_content"]["nsfw_likelihood"] < 3

      return {
          "safe": safe,
          "details": moderation_results,
          "action": "approve" if safe else "review"
      }

  # Usage
  text_result = comprehensive_moderation_workflow("text", text="Sample text content")
  image_result = comprehensive_moderation_workflow("image", file_path="user_photo.jpg")
  ```
</CodeGroup>

## Best Practices

### Error Handling in Workflows

Handle failures gracefully:

<CodeGroup>
  ```python Python theme={null}
  import requests
  from typing import Optional, Dict, Any

  class WorkflowExecutor:
      def __init__(self, api_key):
          self.api_key = api_key
          self.url = "https://api.edenai.run/v3/universal-ai"
          self.headers = {
              "Authorization": f"Bearer {api_key}",
              "Content-Type": "application/json"
          }

      def execute_step(
          self,
          model: str,
          input_data: Dict[str, Any],
          fallback_model: Optional[str] = None
      ) -> Optional[Dict]:
          """Execute a workflow step with optional fallback."""

          payload = {"model": model, "input": input_data}

          try:
              response = requests.post(self.url, headers=self.headers, json=payload)
              response.raise_for_status()
              return response.json()["output"]

          except requests.exceptions.HTTPError as e:
              print(f"Error with {model}: {e}")

              if fallback_model:
                  print(f"Trying fallback: {fallback_model}")
                  return self.execute_step(fallback_model, input_data)

              return None

      def run_workflow(self, steps):
          """Execute multi-step workflow with error handling."""

          results = {}
          context = {}

          for step in steps:
              print(f"Running step: {step['name']}")

              # Prepare input (may use previous results)
              input_data = step["input"]
              if callable(input_data):
                  input_data = input_data(context)

              # Execute with fallback
              result = self.execute_step(
                  step["model"],
                  input_data,
                  step.get("fallback")
              )

              if result is None and step.get("required", True):
                  print(f"✗ Required step {step['name']} failed")
                  return None

              results[step["name"]] = result
              context[step["name"]] = result

          return results

  # Usage
  executor = WorkflowExecutor("YOUR_API_KEY")

  workflow = [
      {
          "name": "moderate",
          "model": "text/moderation/openai",
          "input": {"text": "Sample text"},
          "fallback": "text/moderation/google",
          "required": True
      },
      {
          "name": "sentiment",
          "model": "text/topic_extraction/openai",
          "input": lambda ctx: {"text": "Sample text"} if ctx["moderate"]["nsfw_likelihood"] < 3 else None,
          "required": False
      }
  ]

  results = executor.run_workflow(workflow)
  ```
</CodeGroup>

### Cost Optimization

Monitor and optimize workflow costs:

<CodeGroup>
  ```python Python theme={null}
  import requests

  class CostAwareWorkflow:
      def __init__(self, api_key, max_cost=1.0):
          self.api_key = api_key
          self.max_cost = max_cost
          self.total_cost = 0.0

      def execute_with_budget(self, model, input_data):
          """Execute with cost tracking."""

          if self.total_cost >= self.max_cost:
              raise ValueError(f"Budget exceeded: ${self.total_cost:.4f}")

          url = "https://api.edenai.run/v3/universal-ai"
          headers = {
              "Authorization": f"Bearer {self.api_key}",
              "Content-Type": "application/json"
          }

          payload = {"model": model, "input": input_data}
          response = requests.post(url, headers=headers, json=payload)
          result = response.json()

          # Track cost
          cost = float(result.get("cost", 0))
          self.total_cost += cost

          print(f"Step cost: ${cost:.4f} | Total: ${self.total_cost:.4f}")

          return result["output"]

  # Usage
  workflow = CostAwareWorkflow("YOUR_API_KEY", max_cost=0.50)

  try:
      result1 = workflow.execute_with_budget(
          "text/moderation/openai",
          {"text": "Sample"}
      )
      result2 = workflow.execute_with_budget(
          "text/topic_extraction/openai",
          {"text": "Sample"}
      )
  except ValueError as e:
      print(f"Workflow stopped: {e}")
  ```
</CodeGroup>

## Next Steps

* [Text Features](./text-features) - Text analysis capabilities
* [OCR Features](./ocr-features) - Document processing
* [Image Features](./image-features) - Image analysis
* [Upload Files](../upload/upload-files) - File management
* [Monitor Costs](../cost-management/monitor-usage) - Track spending


# Ocr features
Source: https://docs.edenai.co/v3/how-to/universal-ai/ocr-features



# Universal AI: OCR Features

Extract text and structured data from documents using the Universal AI endpoint.

## Available OCR Features

| Subfeature       | Model String Pattern            | Description                                    |
| ---------------- | ------------------------------- | ---------------------------------------------- |
| OCR              | `ocr/financial_parser/provider` | Extract financial information from images/PDFs |
| Identity Parser  | `ocr/identity_parser/provider`  | Parse ID documents and passports               |
| Financial Parser | `ocr/financial_parser/provider` | Extract structured financial & invoice data    |
| Resume Parser    | `ocr/resume_parser/provider`    | Parse CV and resume data                       |

## Text Extraction (OCR)

Extract text from documents:

<CodeGroup>
  ```python Python theme={null}
  import requests

  # Step 1: Upload the file
  upload_url = "https://api.edenai.run/v3/upload"
  upload_headers = {"Authorization": "Bearer YOUR_API_KEY"}
      
  files = {"file": open("document.pdf", "rb")}
  upload_response = requests.post(upload_url, headers=upload_headers, files=files)
  file_id = upload_response.json()["file_id"]

  # Step 2: Process with OCR
  url = "https://api.edenai.run/v3/universal-ai"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "ocr/financial_parser/google",
      "input": {
          "file": file_id,
          "language": "en"
      }
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()

  print(result["output"]["extracted_data"])
  ```
</CodeGroup>

## Identity Document Parsing

Extract structured data from IDs and passports:

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/universal-ai"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }
  upload_url = "https://api.edenai.run/v3/upload"
  upload_headers = {"Authorization": "Bearer YOUR_API_KEY"}

  # Upload ID document
  files = {"file": open("passport.jpg", "rb")}
  upload_response = requests.post(upload_url, headers=upload_headers, files=files)
  file_id = upload_response.json()["file_id"]

  # Parse identity document
  payload = {
      "model": "ocr/identity_parser/amazon",
      "input": {
          "file": file_id
      }
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()

  identity = result["output"]
  print(f"Name: {identity.get('given_names')} {identity.get('last_name')}")
  print(f"Document Number: {identity.get('document_id')}")
  print(f"Expiry Date: {identity.get('expire_date')}")
  ```
</CodeGroup>

## Invoice Parsing

Extract structured invoice data:

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/universal-ai"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }
  upload_url = "https://api.edenai.run/v3/upload"
  upload_headers = {"Authorization": "Bearer YOUR_API_KEY"}

  # Upload invoice
  files = {"file": open("invoice.pdf", "rb")}
  upload_response = requests.post(upload_url, headers=upload_headers, files=files)
  file_id = upload_response.json()["file_id"]

  # Parse invoice
  payload = {
      "model": "ocr/financial_parser/microsoft",
      "input": {
          "file": file_id,
          "language": "en"
      }
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()

  print(result["output"]["extracted_data"])
  ```
</CodeGroup>

## Using File URLs

Instead of uploading, you can provide file URLs:

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/universal-ai"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "ocr/financial_parser/affinda",
      "input": {
          "file": "https://slicedinvoices.com/pdf/wordpress-pdf-invoice-plugin-sample.pdf",
          "language": "en"
      }
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  print(result["output"]["extracted_data"])
  ```
</CodeGroup>

## Next Steps

* [Upload Files](../upload/upload-files) - Learn about persistent file storage
* [Image Features](./image-features) - Image processing
* [Text Features](./text-features) - Text analysis


# Text features
Source: https://docs.edenai.co/v3/how-to/universal-ai/text-features



# Universal AI: Text Features

Use the Universal AI endpoint to access all text analysis features through a single endpoint.

## Available Text Features

| Subfeature               | Model String Pattern                     | Description                     |
| ------------------------ | ---------------------------------------- | ------------------------------- |
| AI Detection             | `text/ai_detection/provider`             | Detect AI-generated content     |
| Moderation               | `text/moderation/provider`               | Content safety and moderation   |
| Spell Check              | `text/spell_check/provider`              | Grammar and spelling correction |
| Named Entity Recognition | `text/named_entity_recognition/provider` | Extract entities from text      |
| Topic Extraction         | `text/topic_extraction/provider`         | Identify main topics            |
| Plagiarism Detection     | `text/plagia_detection/provider`         | Detect plagiarized content      |

## Content Moderation (Google)

Moderate text for harmful content using Google:

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/universal-ai"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "text/moderation/google",
      "input": {
          "text": "Your text to moderate here"
      }
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()

  print(f"NSFW Likelihood: {result['output']['nsfw_likelihood']}")
  for item in result['output']['items']:
      print(f"  {item['label']}: {item['likelihood']}/5 (score: {item['likelihood_score']:.4f})")
  ```
</CodeGroup>

## Content Moderation

Check text for inappropriate content:

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/universal-ai"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "text/moderation/openai",
      "input": {
          "text": "Content to moderate"
      }
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()

  print(f"NSFW Likelihood: {result['output']['nsfw_likelihood']}")
  for item in result['output']['items']:
      print(f"  {item['label']}: {item['likelihood']}/5")
  ```
</CodeGroup>

## Topic Extraction

Identify main topics in text:

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/universal-ai"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "text/topic_extraction/openai",
      "input": {
          "text": "Apple announced a new iPhone at their Cupertino headquarters today."
      }
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()

  for item in result['output']['items']:
      print(f"  {item['category']}: importance {item['importance']}")
  ```
</CodeGroup>

## Next Steps

* [OCR Features](./ocr-features) - Document processing
* [Image Features](./image-features) - Image capabilities
* [Getting Started](./getting-started) - Universal AI basics


# Upload Files
Source: https://docs.edenai.co/v3/how-to/upload/upload-files



Learn how to upload and manage files with V3's persistent file storage system.

## Overview

V3 introduces **persistent file storage** that allows you to:

* Upload files once
* Reference them in multiple requests
* Reduce upload overhead
* Manage file lifecycle

**Endpoint:**

```
POST /v3/upload
```

## Upload a File

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/upload"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY"
  }

  # Upload file
  files = {
      "file": open("document.pdf", "rb")
  }
      
  data = {
      "purpose": "ocr-processing"  # Optional: describe intended use
  }

  response = requests.post(url, headers=headers, files=files, data=data)
  result = response.json()

  print(f"File ID: {result['file_id']}")
  print(f"Filename: {result['file_name']}")
  print(f"Size: {result['file_size']} bytes")
  print(f"Expires at: {result['expires_at']}")
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.edenai.run/v3/upload \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -F "file=@document.pdf" \
    -F "purpose=ocr-processing"
  ```

  ```javascript JavaScript theme={null}
  const formData = new FormData();
  formData.append('file', fileInput.files[0]);
  formData.append('purpose', 'ocr-processing');

  const response = await fetch('https://api.edenai.run/v3/upload', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_API_KEY'
    },
    body: formData
  });

  const result = await response.json();
  console.log('File ID:', result.file_id);
  ```
</CodeGroup>

### Response

```json theme={null}
{
  "file_id": "550e8400-e29b-41d4-a716-446655440000",
  "file_name": "document.pdf",
  "file_size": 152340,
  "file_mimetype": "application/pdf",
  "purpose": "ocr-processing",
  "metadata": {},
  "created_at": "2024-01-15T10:30:00Z",
  "expires_at": "2024-01-22T10:30:00Z"
}
```

## Use Uploaded File

Once uploaded, reference the file by its `file_id` in any Universal AI request:

<CodeGroup>
  ```python Python theme={null}
  import requests
  # Use file in OCR request
  url = "https://api.edenai.run/v3/universal-ai"
  headers = {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
  }

  payload = {
      "model": "ocr/financial_parser/google",
      "input": {
          "file": "550e8400-e29b-41d4-a716-446655440000",
          "language": "en"
      }
  }

  response = requests.post(url, headers=headers, json=payload)
  result = response.json()
  print(result["output"]["extracted_data"])
  ```
</CodeGroup>

## Supported File Types

| Category      | Formats                              |
| ------------- | ------------------------------------ |
| **Documents** | PDF, DOC, DOCX, TXT                  |
| **Images**    | JPG, JPEG, PNG, GIF, BMP, TIFF, WEBP |
| **Data**      | CSV, JSON, XML                       |

## File Size Limits

* **Default maximum**: 100 MB per file
* Actual limits may vary by feature and provider
* Check provider-specific documentation for exact limits

## File Expiration

Files are automatically deleted after a retention period:

* **Default retention**: 7 days
* Files expire at the timestamp shown in `expires_at`
* Expired files cannot be recovered
* Upload new files as needed

## Upload Multiple Files

<CodeGroup>
  ```python Python theme={null}
  import requests

  url = "https://api.edenai.run/v3/upload"
  headers = {"Authorization": "Bearer YOUR_API_KEY"}

  files_to_upload = [
      "invoice1.pdf",
      "invoice2.pdf",
      "invoice3.pdf"
  ]

  file_ids = []

  for filepath in files_to_upload:
      files = {"file": open(filepath, "rb")}
      data = {"purpose": "invoice-processing"}
          
      response = requests.post(url, headers=headers, files=files, data=data)
      result = response.json()
          
      file_ids.append({
          "filename": filepath,
          "file_id": result["file_id"]
      })
          
      print(f"Uploaded {filepath}: {result['file_id']}")

  # Use file IDs in subsequent requests
  for item in file_ids:
      print(f"{item['filename']}: {item['file_id']}")
  ```
</CodeGroup>

## Error Handling

<CodeGroup>
  ```python Python theme={null}
  import requests
  from requests.exceptions import RequestException

  def safe_upload(filepath):
      """Upload file with error handling"""
          
      url = "https://api.edenai.run/v3/upload"
      headers = {"Authorization": "Bearer YOUR_API_KEY"}
          
      try:
          with open(filepath, "rb") as f:
              files = {"file": f}
              response = requests.post(url, headers=headers, files=files)
              response.raise_for_status()
                  
              result = response.json()
              return {
                  "success": True,
                  "file_id": result["file_id"],
                  "file_name": result["file_name"]
              }
                  
      except FileNotFoundError:
          return {"success": False, "error": "File not found"}
      except RequestException as e:
          return {"success": False, "error": str(e)}
      except Exception as e:
          return {"success": False, "error": f"Unexpected error: {str(e)}"}

  # Usage
  result = safe_upload("document.pdf")
  if result["success"]:
      print(f"Uploaded: {result['file_id']}")
  else:
      print(f"Error: {result['error']}")
  ```
</CodeGroup>

## Best Practices

### 1. Reuse Files

Upload once, use in multiple requests:

```python theme={null}
import requests

upload_url = "https://api.edenai.run/v3/upload"
universal_ai_url = "https://api.edenai.run/v3/universal-ai"
headers = {"Authorization": "Bearer YOUR_API_KEY"}
files = {"file": open("document.pdf", "rb")}

# Upload file once
upload_response = requests.post(upload_url, headers=headers, files=files)
file_id = upload_response.json()["file_id"]

# Use in multiple requests
features = [
    "ocr/financial_parser/google",
    "ocr/financial_parser/amazon",
    "ocr/identity_parser/microsoft"
]

for model in features:
    response = requests.post(
        universal_ai_url,
        headers=headers,
        json={"model": model, "input": {"file": file_id}}
    )
```

### 2. Track File Metadata

Keep track of uploaded files:

```python theme={null}
import requests

upload_url = "https://api.edenai.run/v3/upload"
headers = {"Authorization": "Bearer YOUR_API_KEY"}

uploaded_files = {}

def upload_and_track(filepath, purpose=None):
    files = {"file": open(filepath, "rb")}
    data = {"purpose": purpose} if purpose else {}

    response = requests.post(upload_url, headers=headers, files=files, data=data)
    result = response.json()
    
    # Store metadata
    uploaded_files[result["file_id"]] = {
        "file_name": result["file_name"],
        "uploaded_at": result["created_at"],
        "expires_at": result["expires_at"],
        "purpose": purpose
    }
    
    return result["file_id"]
```

### 3. Handle Large Files

For large files, show upload progress:

```python theme={null}
import os
import requests
from tqdm import tqdm

upload_url = "https://api.edenai.run/v3/upload"
headers = {"Authorization": "Bearer YOUR_API_KEY"}

def upload_with_progress(filepath):
    """Upload file with progress bar"""

    file_size = os.path.getsize(filepath)

    with open(filepath, 'rb') as f:
        with tqdm(total=file_size, unit='B', unit_scale=True) as pbar:
            files = {'file': f}
            response = requests.post(
                upload_url,
                headers=headers,
                files=files
            )
            pbar.update(file_size)

    return response.json()
```

## Common Errors

### 413 Payload Too Large

File exceeds size limit. Compress or split the file.

### 415 Unsupported Media Type

File format not supported. Check supported formats above.

### 422 Validation Error

Invalid request format. Ensure file field is properly set.

## Next Steps

* [OCR Features](../universal-ai/ocr-features) - Use uploaded files for OCR
* [Image Features](../universal-ai/image-features) - Image processing
* [Universal AI Getting Started](../universal-ai/getting-started) - Using files in Universal AI


# Manage tokens
Source: https://docs.edenai.co/v3/how-to/user-management/manage-tokens



# Manage Custom API Tokens

Learn how to create, manage, and organize custom API tokens for your Eden AI account.

> **Note**: These are admin/dashboard endpoints typically used by the Eden AI dashboard or custom admin interfaces. For standard API authentication, see the [Authentication Guide](../authentication/bearer-token-auth).

## Overview

Custom tokens allow you to create additional API keys beyond your main account token. Use cases include:

* **Environment Separation** - Different tokens for development, staging, and production
* **Team Access** - Separate tokens for different team members or projects
* **Budget Control** - Set credit limits per token to control spending
* **Security** - Rotate or revoke tokens without affecting other integrations
* **Tracking** - Monitor usage and costs per token for better analytics

## Endpoints

| Endpoint                        | Method | Description               |
| ------------------------------- | ------ | ------------------------- |
| `/v2/user/custom_token/`        | GET    | List all custom tokens    |
| `/v2/user/custom_token/`        | POST   | Create a new token        |
| `/v2/user/custom_token/{name}/` | GET    | Retrieve a specific token |
| `/v2/user/custom_token/{name}/` | PATCH  | Update token settings     |
| `/v2/user/custom_token/{name}/` | DELETE | Delete a token            |

## Token Types

Eden AI supports two types of custom tokens:

| Type                | Description                            | Use Case                                   |
| ------------------- | -------------------------------------- | ------------------------------------------ |
| `api_token`         | Production token with full access      | Live applications, production environments |
| `sandbox_api_token` | Test token without real provider calls | Development, testing, demos                |

## Creating Tokens

### Create a Basic Token

Create a new custom token with just a name:

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST https://api.edenai.run/v2/user/custom_token/ \
    -H "Authorization: Bearer sk_xxxxxxxxxxxxxxxxxxxxxxxx" \
    -H "Content-Type: application/json" \
    -d '{
      "name": "production-api-token"
    }'
  ```

  ```python Python theme={null}
  import requests

  API_KEY = "eyJhbG...xxxxxxxxxxxxxxxxxxxxxxxx"

  headers = {
      "Authorization": f"Bearer {API_KEY}",
      "Content-Type": "application/json"
  }

  data = {
      "name": "production-api-token"
  }

  response = requests.post(
      "https://api.edenai.run/v2/user/custom_token/",
      headers=headers,
      json=data
  )

  result = response.json()
  print(f"Token created: {result['name']}")
  print(f"Token type: {result['token_type']}")
  ```

  ```javascript JavaScript theme={null}
  const API_KEY = 'sk_xxxxxxxxxxxxxxxxxxxxxxxx';

  const response = await fetch(
    'https://api.edenai.run/v2/user/custom_token/',
    {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${API_KEY}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        name: 'production-api-token'
      })
    }
  );

  const result = await response.json();
  console.log(`Token created: ${result.name}`);
  console.log(`Token type: ${result.token_type}`);
  ```
</CodeGroup>

**Response:**

```json theme={null}
{
  "name": "production-api-token",
  "token_type": "api_token",
  "balance": "50.000000000",
  "active_balance": false,
  "expire_time": null
}
```

**Tip:** Use the GET endpoint to retrieve the token value after creation.

### Create a Token with Credit Limit

Create a token with a spending limit:

<CodeGroup>
  ```python Python theme={null}
  import requests

  API_KEY = "eyJhbG...xxxxxxxxxxxxxxxxxxxxxxxx"

  headers = {
      "Authorization": f"Bearer {API_KEY}",
      "Content-Type": "application/json"
  }

  data = {
      "name": "limited-budget-token",
      "token_type": "api_token",
      "balance": "100.00",  # $100 limit
      "active_balance": True  # Enable balance tracking
  }

  response = requests.post(
      "https://api.edenai.run/v2/user/custom_token/",
      headers=headers,
      json=data
  )

  result = response.json()
  print(f"Token created with ${result['balance']} limit")
  ```

  ```javascript JavaScript theme={null}
  const API_KEY = 'eyJhbG...xxxxxxxxxxxxxxxxxxxxxxxx';

  const response = await fetch(
    'https://api.edenai.run/v2/user/custom_token/',
    {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${API_KEY}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        name: 'limited-budget-token',
        token_type: 'api_token',
        balance: '100.00',  // $100 limit
        active_balance: true  // Enable balance tracking
      })
    }
  );

  const result = await response.json();
  console.log(`Token created with $${result.balance} limit`);
  ```
</CodeGroup>

**How Balance Works:**

* When `active_balance` is `true`, the token has a spending limit
* Each API call deducts from the balance
* When balance reaches \$0, the token becomes unusable
* Perfect for controlling costs per project or team

### Create a Sandbox Token

Create a token for testing without real API calls:

<CodeGroup>
  ```python Python theme={null}
  import requests

  API_KEY = "eyJhbG...xxxxxxxxxxxxxxxxxxxxxxxx"

  headers = {
      "Authorization": f"Bearer {API_KEY}",
      "Content-Type": "application/json"
  }

  data = {
      "name": "dev-sandbox-token",
      "token_type": "sandbox_api_token"  # Sandbox mode
  }

  response = requests.post(
      "https://api.edenai.run/v2/user/custom_token/",
      headers=headers,
      json=data
  )

  result = response.json()
  print(f"Sandbox token created: {result['name']}")
  ```
</CodeGroup>

**Sandbox Benefits:**

* No real provider API calls
* No costs incurred
* Returns mock data for testing
* Perfect for development and CI/CD

### Create a Token with Expiration

Create a temporary token that expires automatically:

<CodeGroup>
  ```python Python theme={null}
  import requests
  from datetime import datetime, timedelta

  API_KEY = "eyJhbG...xxxxxxxxxxxxxxxxxxxxxxxx"

  # Set expiration to 30 days from now
  expire_time = (datetime.now() + timedelta(days=30)).isoformat()

  headers = {
      "Authorization": f"Bearer {API_KEY}",
      "Content-Type": "application/json"
  }

  data = {
      "name": "temporary-token",
      "token_type": "api_token",
      "expire_time": expire_time
  }

  response = requests.post(
      "https://api.edenai.run/v2/user/custom_token/",
      headers=headers,
      json=data
  )

  result = response.json()
  print(f"Token expires: {result['expire_time']}")
  ```

  ```javascript JavaScript theme={null}
  const API_KEY = 'eyJhbG...xxxxxxxxxxxxxxxxxxxxxxxx';

  // Set expiration to 30 days from now
  const expireTime = new Date();
  expireTime.setDate(expireTime.getDate() + 30);

  const response = await fetch(
    'https://api.edenai.run/v2/user/custom_token/',
    {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${API_KEY}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        name: 'temporary-token',
        token_type: 'api_token',
        expire_time: expireTime.toISOString()
      })
    }
  );

  const result = await response.json();
  console.log(`Token expires: ${result.expire_time}`);
  ```
</CodeGroup>

## Listing Tokens

### List All Tokens

Get all your custom tokens:

<CodeGroup>
  ```bash cURL theme={null}
  curl -X GET https://api.edenai.run/v2/user/custom_token/ \
    -H "Authorization: Bearer sk_xxxxxxxxxxxxxxxxxxxxxxxx"
  ```

  ```python Python theme={null}
  import requests

  API_KEY = "eyJhbG...xxxxxxxxxxxxxxxxxxxxxxxx"

  headers = {"Authorization": f"Bearer {API_KEY}"}

  response = requests.get(
      "https://api.edenai.run/v2/user/custom_token/",
      headers=headers
  )

  tokens = response.json()

  print(f"Total tokens: {len(tokens)}\n")

  for token in tokens:
      print(f"Name: {token['name']}")
      print(f"Type: {token['token_type']}")
      if token.get('active_balance'):
          print(f"Balance: ${token.get('balance', 'N/A')}")
      if token.get('expire_time'):
          print(f"Expires: {token['expire_time']}")
      print("-" * 40)
  ```

  ```javascript JavaScript theme={null}
  const API_KEY = 'sk_xxxxxxxxxxxxxxxxxxxxxxxx';

  const response = await fetch(
    'https://api.edenai.run/v2/user/custom_token/',
    {
      headers: {
        'Authorization': `Bearer ${API_KEY}`
      }
    }
  );

  const tokens = await response.json();

  console.log(`Total tokens: ${tokens.length}\n`);

  tokens.forEach(token => {
    console.log(`Name: ${token.name}`);
    console.log(`Type: ${token.token_type}`);
    if (token.active_balance) {
      console.log(`Balance: $${token.balance || 'N/A'}`);
    }
    if (token.expire_time) {
      console.log(`Expires: ${token.expire_time}`);
    }
    console.log('-'.repeat(40));
  });
  ```
</CodeGroup>

**Response:**

```json theme={null}
[
  {
    "name": "production-api-token",
    "token": "eyJhbG...1234567890abcdefghijklmnop",
    "token_type": "api_token",
    "balance": null,
    "active_balance": false,
    "expire_time": null
  },
  {
    "name": "dev-sandbox-token",
    "token": "eyJhbG...abcdef1234567890ghijklmnop",
    "token_type": "sandbox_api_token",
    "balance": null,
    "active_balance": false,
    "expire_time": null
  },
  {
    "name": "limited-budget-token",
    "token": "eyJhbG...xyz789abc123def456ghi789jk",
    "token_type": "api_token",
    "balance": 87.45,
    "active_balance": true,
    "expire_time": null
  }
]
```

## Retrieving a Specific Token

Get details for a single token by name:

<CodeGroup>
  ```bash cURL theme={null}
  curl -X GET "https://api.edenai.run/v2/user/custom_token/production-api-token/" \
    -H "Authorization: Bearer eyJhbG...xxxxxxxxxxxxxxxxxxxxxxxx"
  ```

  ```python Python theme={null}
  import requests

  API_KEY = "eyJhbG...xxxxxxxxxxxxxxxxxxxxxxxx"
  TOKEN_NAME = "my-api-token"

  headers = {"Authorization": f"Bearer {API_KEY}"}

  response = requests.get(
      f"https://api.edenai.run/v2/user/custom_token/{TOKEN_NAME}/",
      headers=headers
  )

  token = response.json()
  print(f"Token: {token['token']}")
  print(f"Balance: ${token.get('balance', 'Unlimited')}")
  ```

  ```javascript JavaScript theme={null}
  const API_KEY = 'eyJhbG...xxxxxxxxxxxxxxxxxxxxxxxx';
  const TOKEN_NAME = 'production-api-token';

  const response = await fetch(
    `https://api.edenai.run/v2/user/custom_token/${TOKEN_NAME}/`,
    {
      headers: {
        'Authorization': `Bearer ${API_KEY}`
      }
    }
  );

  const token = await response.json();
  console.log(`Token: ${token.token}`);
  console.log(`Balance: $${token.balance || 'Unlimited'}`);
  ```
</CodeGroup>

## Updating Tokens

### Update Token Balance

Add or adjust credit balance for a token:

<CodeGroup>
  ```python Python theme={null}
  import requests

  API_KEY = "eyJhbG...xxxxxxxxxxxxxxxxxxxxxxxx"
  TOKEN_NAME = "my-api-token"

  headers = {
      "Authorization": f"Bearer {API_KEY}",
      "Content-Type": "application/json"
  }

  # Increase balance to $200
  data = {
      "balance": 200.00,
      "active_balance": True
  }

  response = requests.patch(
      f"https://api.edenai.run/v2/user/custom_token/{TOKEN_NAME}/",
      headers=headers,
      json=data
  )

  result = response.json()
  print(f"New balance: ${result['balance']}")
  ```

  ```javascript JavaScript theme={null}
  const API_KEY = 'eyJhbG...xxxxxxxxxxxxxxxxxxxxxxxx';
  const TOKEN_NAME = 'limited-budget-token';

  const response = await fetch(
    `https://api.edenai.run/v2/user/custom_token/${TOKEN_NAME}/`,
    {
      method: 'PATCH',
      headers: {
        'Authorization': `Bearer ${API_KEY}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        balance: 200.00,
        active_balance: true
      })
    }
  );

  const result = await response.json();
  console.log(`New balance: $${result.balance}`);
  ```
</CodeGroup>

### Update Token Expiration

Extend or set expiration date:

<CodeGroup>
  ```python Python theme={null}
  import requests
  from datetime import datetime, timedelta

  API_KEY = "eyJhbG...xxxxxxxxxxxxxxxxxxxxxxxx"
  TOKEN_NAME = "my-api-token"

  headers = {
      "Authorization": f"Bearer {API_KEY}",
      "Content-Type": "application/json"
  }

  # Extend expiration by 60 days
  new_expiry = (datetime.now() + timedelta(days=60)).isoformat()

  data = {"expire_time": new_expiry}

  response = requests.patch(
      f"https://api.edenai.run/v2/user/custom_token/{TOKEN_NAME}/",
      headers=headers,
      json=data
  )

  result = response.json()
  print(f"New expiry: {result['expire_time']}")
  ```
</CodeGroup>

### Disable Balance Tracking

Remove balance limit from a token:

<CodeGroup>
  ```python Python theme={null}
  import requests

  API_KEY = "eyJhbG...xxxxxxxxxxxxxxxxxxxxxxxx"
  TOKEN_NAME = "my-api-token"

  headers = {
      "Authorization": f"Bearer {API_KEY}",
      "Content-Type": "application/json"
  }

  # Disable balance tracking
  data = {"active_balance": False}

  response = requests.patch(
      f"https://api.edenai.run/v2/user/custom_token/{TOKEN_NAME}/",
      headers=headers,
      json=data
  )

  print("Balance tracking disabled - unlimited spending")
  ```
</CodeGroup>

## Deleting Tokens

Delete a custom token when no longer needed:

<CodeGroup>
  ```bash cURL theme={null}
  curl -X DELETE "https://api.edenai.run/v2/user/custom_token/old-token/" \
    -H "Authorization: Bearer sk_xxxxxxxxxxxxxxxxxxxxxxxx"
  ```

  ```python Python theme={null}
  import requests

  API_KEY = "eyJhbG...xxxxxxxxxxxxxxxxxxxxxxxx"
  TOKEN_NAME = "old-token"

  headers = {"Authorization": f"Bearer {API_KEY}"}

  response = requests.delete(
      f"https://api.edenai.run/v2/user/custom_token/{TOKEN_NAME}/",
      headers=headers
  )

  if response.status_code == 204:
      print(f"Token '{TOKEN_NAME}' deleted successfully")
  ```

  ```javascript JavaScript theme={null}
  const API_KEY = 'eyJhbG...xxxxxxxxxxxxxxxxxxxxxxxx';
  const TOKEN_NAME = 'old-token';

  const response = await fetch(
    `https://api.edenai.run/v2/user/custom_token/${TOKEN_NAME}/`,
    {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${API_KEY}`
      }
    }
  );

  if (response.status_code === 204) {
    console.log(`Token '${TOKEN_NAME}' deleted successfully`);
  }
  ```
</CodeGroup>

**Important:** Deleting a token immediately revokes access. Any applications using that token will start receiving 401 authentication errors.

## Best Practices

### Token Naming Conventions

Use descriptive, consistent names:

```python theme={null}
# Good naming patterns
"prod-web-app"           # Environment + application
"staging-mobile-ios"     # Environment + platform
"dev-john-testing"       # Environment + developer
"ci-cd-pipeline"         # Purpose
"partner-acme-corp"      # External usage

# Avoid
"token1", "test", "temp"  # Too generic
```

### Budget Control Strategy

Implement budget controls per token:

```python theme={null}
import requests

API_KEY = "eyJhbG...xxxxxxxxxxxxxxxxxxxxxxxx"

# Create tokens with appropriate budgets
token_configs = [
    {
        "name": "prod-main-app",
        "balance": "1000.00",  # High limit for production
        "active_balance": True
    },
    {
        "name": "staging-test-env",
        "balance": "50.00",  # Low limit for staging
        "active_balance": True
    },
    {
        "name": "dev-sandbox",
        "token_type": "sandbox_api_token",  # No cost
        "active_balance": False
    }
]

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

for config in token_configs:
    response = requests.post(
        "https://api.edenai.run/v2/user/custom_token/",
        headers=headers,
        json=config
    )
    print(f"Created: {config['name']}")
```

### Token Rotation

Regularly rotate tokens for security:

```python theme={null}
import requests
from datetime import datetime, timedelta

API_KEY = "eyJhbG...xxxxxxxxxxxxxxxxxxxxxxxx"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def rotate_token(old_token_name: str, new_token_name: str):
    """
    Rotate a token by creating a new one and deleting the old one.
    """
    # Get old token details
    old_response = requests.get(
        f"https://api.edenai.run/v2/user/custom_token/{old_token_name}/",
        headers=headers
    )
    old_token = old_response.json()

    # Create new token with same settings
    new_data = {
        "name": new_token_name,
        "token_type": old_token['token_type'],
        "active_balance": old_token['active_balance']
    }

    if old_token.get('balance'):
        new_data['balance'] = str(old_token['balance'])

    new_response = requests.post(
        "https://api.edenai.run/v2/user/custom_token/",
        headers=headers,
        json=new_data
    )

    # Fetch the new token to get its value
    token_response = requests.get(
        f"https://api.edenai.run/v2/user/custom_token/{new_token_name}/",
        headers=headers
    )
    new_token = token_response.json()

    print(f"New token created: {new_token['token']}")
    print("Update your application with the new token")
    print(f"Once confirmed, delete old token: {old_token_name}")

    return new_token

# First create the token we want to rotate
requests.post(
    "https://api.edenai.run/v2/user/custom_token/",
    headers=headers,
    json={"name": "prod-q1-2026"}
)

# Rotate quarterly
rotate_token("prod-q1-2026", "prod-q2-2026")
```

### Monitor Token Usage

Track usage and remaining balance:

```python theme={null}
import requests

API_KEY = "eyJhbG...xxxxxxxxxxxxxxxxxxxxxxxx"

def check_token_health():
    """Check all tokens for low balance or expiration"""
    headers = {"Authorization": f"Bearer {API_KEY}"}

    response = requests.get(
        "https://api.edenai.run/v2/user/custom_token/",
        headers=headers
    )

    tokens = response.json()

    for token in tokens:
        print(f"\nToken: {token['name']}")

        # Check balance
        if token.get('active_balance') and token.get('balance') is not None:
            if token['balance'] < 10:
                print(f"⚠️  LOW BALANCE: ${token['balance']:.2f}")
            else:
                print(f"✓ Balance: ${token['balance']:.2f}")

        # Check expiration
        if token.get('expire_time'):
            from datetime import datetime, timezone
            expiry = datetime.fromisoformat(token['expire_time'].replace('Z', '+00:00'))
            days_left = (expiry - datetime.now(timezone.utc)).days

            if days_left < 7:
                print(f"⚠️  EXPIRES SOON: {days_left} days")
            else:
                print(f"✓ Expires in {days_left} days")

check_token_health()
```

### Scope Limitations

Use different tokens for different scopes:

```python theme={null}
# Production tokens - full access
production_tokens = [
    {"name": "prod-us-east", "balance": "500"},
    {"name": "prod-eu-west", "balance": "500"}
]

# Development tokens - limited budget
dev_tokens = [
    {"name": "dev-feature-xyz", "balance": "25", "expire_time": "+30 days"},
    {"name": "dev-testing", "token_type": "sandbox_api_token"}
]

# External tokens - strict limits
external_tokens = [
    {"name": "partner-demo", "balance": "10", "expire_time": "+7 days"},
    {"name": "client-trial", "balance": "5", "expire_time": "+14 days"}
]
```

## Error Handling

### 400 Bad Request

Invalid token name or parameters:

```json theme={null}
{
  "error": {
    "type": "validation_error",
    "message": {
      "name": ["Token with this name already exists."]
    }
  }
}
```

### 404 Not Found

Token doesn't exist:

```json theme={null}
{
  "details": "Not Found"
}
```

### 403 Forbidden

Insufficient permissions:

```json theme={null}
{
  "error": {
    "type": "permission_error",
    "message": "You do not have permission to manage tokens"
  }
}
```

## Next Steps

* [Multi-Environment Token Management Tutorial](../../tutorials/multi-environment-tokens) - Complete workflow
* [Monitor Usage and Costs](../../how-to/cost-management/monitor-usage) - Track spending per token
* [Authentication Guide](../../how-to/authentication/bearer-token-auth) - Use your tokens


# Claude code
Source: https://docs.edenai.co/v3/integrations/ai-assistants/claude-code



# Claude Code

Configure Claude Code CLI to use Eden AI's multi-provider backend for enhanced flexibility and cost savings.

## Overview

Claude Code is Anthropic's official CLI tool for AI-powered coding assistance. By default, it uses Anthropic's API, but you can configure it to use Eden AI for:

* **Multi-provider access**: Use GPT-4, Gemini, or other models alongside Claude
* **Cost optimization**: Leverage Eden AI's competitive pricing
* **Provider redundancy**: Automatic failover if one provider is down

## Prerequisites

* Claude Code installed ([Installation Guide](https://github.com/anthropics/claude-code))
* Eden AI API key from [https://app.edenai.run](https://app.edenai.run)

## Configuration

Claude Code can be configured to use custom API endpoints through environment variables or configuration files.

### Option 1: Environment Variables

Set environment variables before running Claude Code:

<CodeGroup>
  ```bash bash theme={null}
  # Set Eden AI as the API endpoint
  export ANTHROPIC_API_KEY="YOUR_EDEN_AI_API_KEY"
  export ANTHROPIC_BASE_URL="https://api.edenai.run/v3/llm"

  # Run Claude Code
  claude-code
  ```

  ```powershell PowerShell theme={null}
  # Windows PowerShell
  $env:ANTHROPIC_API_KEY="YOUR_EDEN_AI_API_KEY"
  $env:ANTHROPIC_BASE_URL="https://api.edenai.run/v3/llm"

  claude-code
  ```
</CodeGroup>

### Option 2: Configuration File

Create or edit the Claude Code configuration file:

<CodeGroup>
  ```json ~/.config/claude-code/config.json theme={null}
  {
    "api_key": "YOUR_EDEN_AI_API_KEY",
    "base_url": "https://api.edenai.run/v3/llm",
    "model": "anthropic/claude-sonnet-4-5"
  }
  ```
</CodeGroup>

## Using Different Models

With Eden AI, you can use models from different providers:

<CodeGroup>
  ```bash bash theme={null}
  # Use Claude 3.5 Sonnet (default)
  export ANTHROPIC_MODEL="anthropic/claude-sonnet-4-5"
  claude-code

  # Use GPT-4
  export ANTHROPIC_MODEL="openai/gpt-4"
  claude-code

  # Use Gemini Pro
  export ANTHROPIC_MODEL="google/gemini-2.5-flash"
  claude-code
  ```
</CodeGroup>

## Model Format

When using Eden AI with Claude Code, use the `provider/model` format:

### Anthropic Models

* `anthropic/claude-sonnet-4-5` (recommended)
* `anthropic/claude-opus-4-5`
* `anthropic/claude-haiku-4-5`

### OpenAI Models

* `openai/gpt-4`
* `openai/gpt-4-turbo`
* `openai/gpt-4o`

### Google Models

* `google/gemini-2.5-flash`
* `google/gemini-2.5-pro`

## Permanent Configuration

Make the configuration permanent by adding to your shell profile:

<CodeGroup>
  ```bash ~/.bashrc or ~/.zshrc theme={null}
  # Eden AI configuration for Claude Code
  export ANTHROPIC_API_KEY="YOUR_EDEN_AI_API_KEY"
  export ANTHROPIC_BASE_URL="https://api.edenai.run/v3/llm"
  export ANTHROPIC_MODEL="anthropic/claude-sonnet-4-5"
  ```
</CodeGroup>

Reload your shell:

```bash theme={null}
source ~/.bashrc  # or ~/.zshrc
```

## Custom Model Switching Script

Create a script to easily switch between models:

<CodeGroup>
  ```bash switch-model.sh theme={null}
  #!/bin/bash

  case "$1" in
    claude)
      export ANTHROPIC_MODEL="anthropic/claude-sonnet-4-5"
      echo "Switched to Claude 3.5 Sonnet"
      ;;
    gpt4)
      export ANTHROPIC_MODEL="openai/gpt-4"
      echo "Switched to GPT-4"
      ;;
    gemini)
      export ANTHROPIC_MODEL="google/gemini-2.5-flash"
      echo "Switched to Gemini Pro"
      ;;
    *)
      echo "Usage: source switch-model.sh [claude|gpt4|gemini]"
      ;;
  esac

  claude-code
  ```
</CodeGroup>

Usage:

```bash theme={null}
chmod +x switch-model.sh
source switch-model.sh claude   # Use Claude
source switch-model.sh gpt4     # Use GPT-4
source switch-model.sh gemini   # Use Gemini
```

## Features

### Code Generation

Claude Code can generate code in any language with Eden AI:

```bash theme={null}
claude-code "Create a Python function to fetch data from an API"
```

### Code Review

Review and improve existing code:

```bash theme={null}
claude-code "Review this code for security issues" < myfile.py
```

### Refactoring

Refactor code with context awareness:

```bash theme={null}
claude-code "Refactor this function to use async/await" < myfile.js
```

### Documentation

Generate documentation:

```bash theme={null}
claude-code "Add docstrings to all functions" < mymodule.py
```

## Advanced Configuration

### Custom Headers

If you need to pass custom headers (e.g., for analytics):

<CodeGroup>
  ```json config.json theme={null}
  {
    "api_key": "YOUR_EDEN_AI_API_KEY",
    "base_url": "https://api.edenai.run/v3/llm",
    "model": "anthropic/claude-sonnet-4-5",
    "headers": {
      "X-Custom-Header": "value"
    }
  }
  ```
</CodeGroup>

### Timeout Configuration

Adjust timeouts for longer requests:

<CodeGroup>
  ```json config.json theme={null}
  {
    "api_key": "YOUR_EDEN_AI_API_KEY",
    "base_url": "https://api.edenai.run/v3/llm",
    "timeout": 120000
  }
  ```
</CodeGroup>

## Troubleshooting

### Authentication Errors

If you see authentication errors:

1. Verify your Eden AI API key is correct
2. Check that the `ANTHROPIC_API_KEY` environment variable is set
3. Ensure there are no trailing spaces in your API key

```bash theme={null}
# Test your API key
curl -X POST https://api.edenai.run/v3/llm/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "anthropic/claude-sonnet-4-5",
    "messages": [{"role": "user", "content": "test"}],
    "stream": true
  }'
```

### Model Not Found

Ensure you're using the correct model format:

```bash theme={null}
# Correct
anthropic/claude-sonnet-4-5

# Incorrect
claude-sonnet-4-5
```

### Connection Issues

If you experience connection issues:

1. Check your internet connection
2. Verify the base URL is correct: `https://api.edenai.run/v3/llm`
3. Check Eden AI status: [https://app-edenai.instatus.com](https://app-edenai.instatus.com)

## Cost Tracking

Monitor your Eden AI usage through the dashboard:

```bash theme={null}
# View your current usage
curl https://api.edenai.run/v3/cost-management/usage \
  -H "Authorization: Bearer YOUR_API_KEY"
```

## Best Practices

### 1. Use Appropriate Models

Choose models based on task complexity:

* **Simple tasks**: `anthropic/claude-haiku-4-5` (fast, cost-effective)
* **Complex reasoning**: `anthropic/claude-sonnet-4-5` (best balance)
* **Maximum capability**: `anthropic/claude-opus-4-5` (most powerful)

### 2. Leverage Multiple Providers

Test different providers for different tasks:

* **Code generation**: GPT-4 or Claude
* **Explanation**: Claude or Gemini
* **Quick tasks**: Haiku or GPT-3.5

### 3. Monitor Costs

Regularly check your Eden AI dashboard to track spending and optimize model selection.

## Integration with Git

Use Claude Code in Git hooks for automated code review:

<CodeGroup>
  ```bash .git/hooks/pre-commit theme={null}
  #!/bin/bash

  # Export Eden AI configuration
  export ANTHROPIC_API_KEY="YOUR_EDEN_AI_API_KEY"
  export ANTHROPIC_BASE_URL="https://api.edenai.run/v3/llm"

  # Get changed files
  changed_files=$(git diff --cached --name-only --diff-filter=ACM | grep '\.py$')

  if [ -n "$changed_files" ]; then
    echo "Reviewing changed Python files..."
    for file in $changed_files; do
      claude-code "Quick security review" < "$file"
    done
  fi
  ```
</CodeGroup>

## Next Steps

* [Continue.dev Integration](./continue-dev) - Another powerful VS Code extension
* [LLM How-To Guides](../../how-to/llm/chat-completions) - Learn more about LLM features


# Continue dev
Source: https://docs.edenai.co/v3/integrations/ai-assistants/continue-dev



# Continue.dev

Configure Continue.dev, the open-source AI code assistant, to use Eden AI for access to 200+ models.

## Overview

[Continue.dev](https://continue.dev) is an open-source autopilot for VS Code and JetBrains IDEs. By connecting it to Eden AI, you get:

* **200+ models**: Access OpenAI, Anthropic, Google, Cohere, and more
* **Cost savings**: Leverage Eden AI's competitive pricing
* **Provider flexibility**: Switch models instantly without changing configuration

## Installation

Install Continue.dev from your IDE marketplace:

### VS Code

1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X / Cmd+Shift+X)
3. Search for "Continue"
4. Click Install

### JetBrains IDEs

1. Open your JetBrains IDE (IntelliJ, PyCharm, etc.)
2. Go to Plugins (Ctrl+Alt+S / Cmd+,)
3. Search for "Continue"
4. Click Install

## Configuration

Configure Continue to use Eden AI's OpenAI-compatible endpoint.

### Step 1: Open Configuration

In VS Code or JetBrains:

1. Click the Continue icon in the sidebar
2. Click the gear icon (⚙️) to open settings
3. This opens `~/.continue/config.json`

### Step 2: Configure Eden AI

Replace the configuration with:

<CodeGroup>
  ```json ~/.continue/config.json theme={null}
  {
    "models": [
      {
        "title": "Claude 3.5 Sonnet",
        "provider": "openai",
        "model": "anthropic/claude-sonnet-4-5",
        "apiKey": "YOUR_EDEN_AI_API_KEY",
        "apiBase": "https://api.edenai.run/v3/llm"
      },
      {
        "title": "GPT-4",
        "provider": "openai",
        "model": "openai/gpt-4",
        "apiKey": "YOUR_EDEN_AI_API_KEY",
        "apiBase": "https://api.edenai.run/v3/llm"
      },
      {
        "title": "Gemini Pro",
        "provider": "openai",
        "model": "google/gemini-2.5-flash",
        "apiKey": "YOUR_EDEN_AI_API_KEY",
        "apiBase": "https://api.edenai.run/v3/llm"
      }
    ],
    "tabAutocompleteModel": {
      "title": "GPT-3.5 Turbo",
      "provider": "openai",
      "model": "openai/gpt-3.5-turbo",
      "apiKey": "YOUR_EDEN_AI_API_KEY",
      "apiBase": "https://api.edenai.run/v3/llm"
    },
    "embeddingsProvider": {
      "provider": "openai",
      "model": "openai/text-embedding-3-small",
      "apiKey": "YOUR_EDEN_AI_API_KEY",
      "apiBase": "https://api.edenai.run/v3/llm"
    }
  }
  ```
</CodeGroup>

### Step 3: Save and Reload

1. Save the configuration file
2. Reload your IDE or click "Reload" in Continue

## Available Models

You can add any model from Eden AI's catalog:

### Chat Models

<CodeGroup>
  ```json config.json theme={null}
  {
    "models": [
      {
        "title": "Claude 3.5 Sonnet",
        "provider": "openai",
        "model": "anthropic/claude-sonnet-4-5",
        "apiKey": "YOUR_EDEN_AI_API_KEY",
        "apiBase": "https://api.edenai.run/v3/llm"
      },
      {
        "title": "Claude 3 Opus",
        "provider": "openai",
        "model": "anthropic/claude-opus-4-5",
        "apiKey": "YOUR_EDEN_AI_API_KEY",
        "apiBase": "https://api.edenai.run/v3/llm"
      },
      {
        "title": "GPT-4 Turbo",
        "provider": "openai",
        "model": "openai/gpt-4-turbo",
        "apiKey": "YOUR_EDEN_AI_API_KEY",
        "apiBase": "https://api.edenai.run/v3/llm"
      },
      {
        "title": "Gemini 2.5 Pro",
        "provider": "openai",
        "model": "google/gemini-2.5-pro",
        "apiKey": "YOUR_EDEN_AI_API_KEY",
        "apiBase": "https://api.edenai.run/v3/llm"
      },
      {
        "title": "Command R+",
        "provider": "openai",
        "model": "cohere/command-r-plus",
        "apiKey": "YOUR_EDEN_AI_API_KEY",
        "apiBase": "https://api.edenai.run/v3/llm"
      }
    ]
  }
  ```
</CodeGroup>

## Features

### Chat

Open the Continue sidebar and start chatting with AI:

1. Select your model from the dropdown
2. Type your question or request
3. Get instant responses

**Example prompts:**

* "Explain this code"
* "Add error handling to this function"
* "Write tests for this component"

### Inline Editing

Select code and use Continue to edit it:

1. Highlight code
2. Press Cmd+I (Mac) / Ctrl+I (Windows/Linux)
3. Describe your changes
4. Review and accept

**Example edits:**

* "Add type hints"
* "Refactor this to use async/await"
* "Simplify this logic"

### Tab Autocomplete

Continue provides intelligent code completion:

1. Start typing
2. Continue suggests completions
3. Press Tab to accept

Configure fast models for autocomplete:

<CodeGroup>
  ```json config.json theme={null}
  {
    "tabAutocompleteModel": {
      "title": "Fast Autocomplete",
      "provider": "openai",
      "model": "openai/gpt-3.5-turbo",
      "apiKey": "YOUR_EDEN_AI_API_KEY",
      "apiBase": "https://api.edenai.run/v3/llm"
    }
  }
  ```
</CodeGroup>

### Slash Commands

Use slash commands for common tasks:

* `/edit` - Edit selected code
* `/comment` - Add comments
* `/test` - Generate tests
* `/fix` - Fix errors
* `/explain` - Explain code

## Advanced Configuration

### Custom Context Providers

Add codebase context for better responses:

<CodeGroup>
  ```json config.json theme={null}
  {
    "models": [...],
    "contextProviders": [
      {
        "name": "code",
        "params": {}
      },
      {
        "name": "docs",
        "params": {
          "startUrl": "https://docs.edenai.co"
        }
      },
      {
        "name": "folder",
        "params": {
          "folder": "src"
        }
      }
    ]
  }
  ```
</CodeGroup>

### Model-Specific Settings

Configure temperature and other parameters per model:

<CodeGroup>
  ```json config.json theme={null}
  {
    "models": [
      {
        "title": "Claude 3.5 Sonnet (Creative)",
        "provider": "openai",
        "model": "anthropic/claude-sonnet-4-5",
        "apiKey": "YOUR_EDEN_AI_API_KEY",
        "apiBase": "https://api.edenai.run/v3/llm",
        "completionOptions": {
          "temperature": 0.9,
          "maxTokens": 2000
        }
      },
      {
        "title": "Claude 3.5 Sonnet (Precise)",
        "provider": "openai",
        "model": "anthropic/claude-sonnet-4-5",
        "apiKey": "YOUR_EDEN_AI_API_KEY",
        "apiBase": "https://api.edenai.run/v3/llm",
        "completionOptions": {
          "temperature": 0.1,
          "maxTokens": 1000
        }
      }
    ]
  }
  ```
</CodeGroup>

### Environment Variables

Use environment variables for API keys:

<CodeGroup>
  ```json config.json theme={null}
  {
    "models": [
      {
        "title": "Claude 3.5 Sonnet",
        "provider": "openai",
        "model": "anthropic/claude-sonnet-4-5",
        "apiKey": "${EDEN_AI_API_KEY}",
        "apiBase": "https://api.edenai.run/v3/llm"
      }
    ]
  }
  ```

  ```bash ~/.bashrc or ~/.zshrc theme={null}
  export EDEN_AI_API_KEY="your_api_key_here"
  ```
</CodeGroup>

## Use Cases

### Code Generation

Generate entire functions or classes:

1. Open Continue chat
2. Describe what you need: "Create a Python class for user authentication with login, logout, and token refresh methods"
3. Review and insert the generated code

### Code Review

Get AI-powered code reviews:

1. Select code
2. Open Continue chat
3. Ask: "Review this code for security issues and performance improvements"

### Documentation

Generate documentation automatically:

1. Select a function
2. Use `/comment` command
3. Continue adds comprehensive docstrings

### Debugging

Get help with errors:

1. Copy error message
2. Open Continue chat
3. Ask: "How do I fix this error?" and paste the error

### Refactoring

Modernize legacy code:

1. Select old code
2. Use `/edit` command
3. Ask: "Refactor this to use modern Python features"

## Troubleshooting

### Models Not Appearing

If models don't appear in the dropdown:

1. Check `config.json` syntax is valid (use a JSON validator)
2. Ensure `apiBase` is exactly: `https://api.edenai.run/v3/llm`
3. Reload the IDE

### Authentication Errors

If you see 401 errors:

1. Verify your Eden AI API key in `config.json`
2. Check there are no extra spaces in the API key
3. Test the API key manually:

```bash theme={null}
curl -X POST https://api.edenai.run/v3/llm/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "anthropic/claude-sonnet-4-5",
    "messages": [{"role": "user", "content": "test"}],
    "stream": true
  }'
```

### Slow Responses

If responses are slow:

1. Use faster models for autocomplete (`gpt-3.5-turbo`)
2. Reduce `maxTokens` in completion options
3. Check your internet connection

### Context Issues

If Continue doesn't understand your codebase:

1. Add relevant context providers
2. Include specific files using `@file` in chat
3. Use folder context for project-wide understanding

## Keyboard Shortcuts

### VS Code

* `Cmd/Ctrl + I` - Inline edit
* `Cmd/Ctrl + Shift + L` - Open Continue sidebar
* `Cmd/Ctrl + Shift + R` - Re-run last command

### JetBrains

* `Alt + Enter` - Show Continue actions
* `Cmd/Ctrl + Shift + C` - Open Continue chat

## Best Practices

### 1. Choose the Right Model

* **Quick edits**: Use `openai/gpt-3.5-turbo` for speed
* **Complex reasoning**: Use `anthropic/claude-sonnet-4-5`
* **Autocomplete**: Use `openai/gpt-3.5-turbo` for low latency

### 2. Provide Context

Add context to get better responses:

* Tag files with `@filename`
* Include error messages
* Describe the broader goal

### 3. Iterate

Don't expect perfect results immediately:

* Review generated code
* Ask for adjustments
* Combine AI suggestions with your expertise

### 4. Use Slash Commands

Leverage built-in commands for common tasks:

* `/edit` for modifications
* `/test` for test generation
* `/fix` for error resolution

## Example Workflows

### Building a New Feature

1. Chat: "Help me design a REST API endpoint for user registration"
2. Review the suggested structure
3. Use `/edit` to implement the endpoint
4. Use `/test` to generate unit tests
5. Use `/comment` to add documentation

### Debugging

1. Copy the error traceback
2. Chat: "Explain this error and suggest a fix: \[paste error]"
3. Review the explanation
4. Use `/fix` on the problematic code
5. Test the solution

### Code Review

1. Select a function
2. Chat: "Review this for security, performance, and maintainability"
3. Review suggestions
4. Use `/edit` to apply improvements
5. Use `/test` to ensure nothing broke

## Next Steps

* [Claude Code](./claude-code) - Official Claude CLI


# Librechat
Source: https://docs.edenai.co/v3/integrations/chat-platforms/librechat



# LibreChat

Configure LibreChat, the open-source ChatGPT alternative, to use Eden AI for access to 200+ AI models.

## Overview

[LibreChat](https://librechat.ai) is a free, open-source AI chat platform that supports multiple providers. By connecting it to Eden AI, you get:

* **200+ models**: Access OpenAI, Anthropic, Google, Cohere, and more through one interface
* **Self-hosted**: Full control over your data and infrastructure
* **Cost savings**: Leverage Eden AI's competitive pricing
* **Unified experience**: Single chat interface for all providers

## Prerequisites

* Docker and Docker Compose installed
* Eden AI API key from [https://app.edenai.run](https://app.edenai.run)
* Basic knowledge of environment variables

## Installation

### Option 1: Docker Compose (Recommended)

Clone LibreChat and set up with Docker:

<CodeGroup>
  ```bash bash theme={null}
  # Clone LibreChat
  git clone https://github.com/danny-avila/LibreChat.git
  cd LibreChat

  # Copy example environment file
  cp .env.example .env

  # Start LibreChat
  docker compose up -d
  ```
</CodeGroup>

### Option 2: Manual Installation

<CodeGroup>
  ```bash bash theme={null}
  # Clone repository
  git clone https://github.com/danny-avila/LibreChat.git
  cd LibreChat

  # Install dependencies
  npm install

  # Set up environment
  cp .env.example .env

  # Build and start
  npm run build
  npm run backend
  ```
</CodeGroup>

## Configuration

### Step 1: Configure Environment Variables

Edit the `.env` file to add Eden AI configuration:

<CodeGroup>
  ```bash .env theme={null}
  # Eden AI Configuration
  OPENAI_API_KEY=YOUR_EDEN_AI_API_KEY
  OPENAI_REVERSE_PROXY=https://api.edenai.run/v3/llm

  # Optional: Enable multiple endpoints
  ANTHROPIC_API_KEY=YOUR_EDEN_AI_API_KEY
  ANTHROPIC_REVERSE_PROXY=https://api.edenai.run/v3/llm

  GOOGLE_API_KEY=YOUR_EDEN_AI_API_KEY
  GOOGLE_REVERSE_PROXY=https://api.edenai.run/v3/llm

  # Application settings
  HOST=localhost
  PORT=3080
  MONGO_URI=mongodb://127.0.0.1:27017/LibreChat

  # Session secret (generate your own)
  SESSION_SECRET=your_random_secret_here
  JWT_SECRET=your_jwt_secret_here
  JWT_REFRESH_SECRET=your_refresh_secret_here
  ```
</CodeGroup>

### Step 2: Configure librechat.yaml

Create or edit `librechat.yaml` for advanced configuration:

<CodeGroup>
  ```yaml librechat.yaml theme={null}
  version: 1.0.5
  cache: true

  endpoints:
    custom:
      - name: "Eden AI"
        apiKey: "${OPENAI_API_KEY}"
        baseURL: "https://api.edenai.run/v3/llm"
        models:
          default:
            - "anthropic/claude-sonnet-4-5"
            - "openai/gpt-4"
            - "openai/gpt-4-turbo"
            - "google/gemini-2.5-pro"
            - "google/gemini-2.5-flash"
            - "cohere/command-r-plus"
            - "openai/gpt-3.5-turbo"
          fetch: false
        titleConvo: true
        titleModel: "openai/gpt-3.5-turbo"
        summarize: false
        summaryModel: "openai/gpt-3.5-turbo"
        forcePrompt: false
        modelDisplayLabel: "Eden AI"
  ```
</CodeGroup>

### Step 3: Start LibreChat

<CodeGroup>
  ```bash bash theme={null}
  # With Docker
  docker compose up -d

  # Without Docker
  npm run backend
  ```
</CodeGroup>

Access LibreChat at `http://localhost:3080`

## Available Models

Configure which models appear in the LibreChat interface:

<CodeGroup>
  ```yaml librechat.yaml theme={null}
  endpoints:
    custom:
      - name: "Eden AI - Claude"
        apiKey: "${OPENAI_API_KEY}"
        baseURL: "https://api.edenai.run/v3/llm"
        models:
          default:
            - "anthropic/claude-sonnet-4-5"
            - "anthropic/claude-opus-4-5"
            - "anthropic/claude-sonnet-4-5"
            - "anthropic/claude-haiku-4-5"
        modelDisplayLabel: "Claude (Eden AI)"

      - name: "Eden AI - OpenAI"
        apiKey: "${OPENAI_API_KEY}"
        baseURL: "https://api.edenai.run/v3/llm"
        models:
          default:
            - "openai/gpt-4"
            - "openai/gpt-4-turbo"
            - "openai/gpt-4o"
            - "openai/gpt-3.5-turbo"
        modelDisplayLabel: "OpenAI (Eden AI)"

      - name: "Eden AI - Google"
        apiKey: "${OPENAI_API_KEY}"
        baseURL: "https://api.edenai.run/v3/llm"
        models:
          default:
            - "google/gemini-2.5-pro"
            - "google/gemini-2.5-flash"
        modelDisplayLabel: "Google (Eden AI)"
  ```
</CodeGroup>

## Features

### Multi-Model Conversations

Switch between models mid-conversation:

1. Start a conversation with Claude
2. Click the model selector
3. Switch to GPT-4 or Gemini
4. Continue the conversation seamlessly

### File Attachments

Upload files for vision-capable models:

<CodeGroup>
  ```yaml librechat.yaml theme={null}
  endpoints:
    custom:
      - name: "Eden AI - Vision"
        apiKey: "${OPENAI_API_KEY}"
        baseURL: "https://api.edenai.run/v3/llm"
        models:
          default:
            - "openai/gpt-4o"
            - "google/gemini-2.5-pro"
            - "anthropic/claude-sonnet-4-5"
        # Enable file uploads
        fileConfig:
          endpoints:
            assistants:
              fileLimit: 5
              fileSizeLimit: 10
              totalSizeLimit: 50
              supportedMimeTypes:
                - "image/jpeg"
                - "image/png"
                - "image/webp"
                - "image/gif"
        modelDisplayLabel: "Vision Models"
  ```
</CodeGroup>

### Preset Prompts

Create custom prompts for common tasks:

<CodeGroup>
  ```yaml librechat.yaml theme={null}
  endpoints:
    custom:
      - name: "Eden AI"
        apiKey: "${OPENAI_API_KEY}"
        baseURL: "https://api.edenai.run/v3/llm"
        models:
          default:
            - "anthropic/claude-sonnet-4-5"
            - "openai/gpt-4"
        # Add custom presets
        presets:
          - title: "Code Assistant"
            model: "anthropic/claude-sonnet-4-5"
            temperature: 0.1
            system_message: "You are an expert programmer. Provide clean, well-documented code."

          - title: "Creative Writer"
            model: "openai/gpt-4"
            temperature: 0.9
            system_message: "You are a creative writer. Be imaginative and engaging."

          - title: "Data Analyst"
            model: "google/gemini-2.5-pro"
            temperature: 0.3
            system_message: "You are a data analyst. Provide clear, data-driven insights."
  ```
</CodeGroup>

## Advanced Configuration

### Custom Model Parameters

Configure temperature, max tokens, and other parameters:

<CodeGroup>
  ```yaml librechat.yaml theme={null}
  endpoints:
    custom:
      - name: "Eden AI"
        apiKey: "${OPENAI_API_KEY}"
        baseURL: "https://api.edenai.run/v3/llm"
        models:
          default:
            - "anthropic/claude-sonnet-4-5"
        # Default parameters
        default:
          temperature: 0.7
          max_tokens: 2000
          top_p: 1.0
          frequency_penalty: 0.0
          presence_penalty: 0.0
        # Allow users to override
        userProvidedParameters:
          - "temperature"
          - "max_tokens"
          - "top_p"
  ```
</CodeGroup>

### User Authentication

Enable user registration and authentication:

<CodeGroup>
  ```bash .env theme={null}
  # Allow user registration
  ALLOW_REGISTRATION=true

  # Email verification (optional)
  EMAIL_SERVICE=gmail
  EMAIL_USERNAME=your-email@gmail.com
  EMAIL_PASSWORD=your-app-password

  # Social auth (optional)
  GOOGLE_CLIENT_ID=your-google-client-id
  GOOGLE_CLIENT_SECRET=your-google-client-secret
  GOOGLE_CALLBACK_URL=http://localhost:3080/oauth/google/callback
  ```
</CodeGroup>

### Rate Limiting

Protect your API key with rate limiting:

<CodeGroup>
  ```yaml librechat.yaml theme={null}
  rateLimits:
    fileUploads:
      ipMax: 100
      ipWindowInMinutes: 60
      userMax: 50
      userWindowInMinutes: 60

    conversationsImport:
      ipMax: 10
      ipWindowInMinutes: 60
      userMax: 5
      userWindowInMinutes: 60
  ```
</CodeGroup>

### Conversation History

Configure MongoDB for persistent conversations:

<CodeGroup>
  ```bash .env theme={null}
  # MongoDB connection
  MONGO_URI=mongodb://127.0.0.1:27017/LibreChat

  # Or use MongoDB Atlas (cloud)
  # MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/LibreChat
  ```

  ```yaml docker-compose.yml theme={null}
  services:
    mongodb:
      image: mongo
      container_name: chat-mongodb
      restart: always
      volumes:
        - ./data-node:/data/db
      ports:
        - 27017:27017
  ```
</CodeGroup>

## Docker Deployment

### Production Docker Compose

<CodeGroup>
  ```yaml docker-compose.override.yml theme={null}
  version: '3.4'

  services:
    api:
      image: ghcr.io/danny-avila/librechat:latest
      container_name: LibreChat
      ports:
        - 3080:3080
      depends_on:
        - mongodb
      restart: always
      environment:
        - HOST=0.0.0.0
        - MONGO_URI=mongodb://mongodb:27017/LibreChat
        - OPENAI_API_KEY=${OPENAI_API_KEY}
        - OPENAI_REVERSE_PROXY=https://api.edenai.run/v3/llm
      volumes:
        - ./librechat.yaml:/app/librechat.yaml
        - ./images:/app/client/public/images

    mongodb:
      image: mongo
      container_name: chat-mongodb
      restart: always
      volumes:
        - ./data-node:/data/db
      ports:
        - 27017:27017
  ```
</CodeGroup>

### Deploy to Production

<CodeGroup>
  ```bash bash theme={null}
  # Pull latest image
  docker compose pull

  # Start services
  docker compose up -d

  # View logs
  docker compose logs -f api

  # Check status
  docker compose ps
  ```
</CodeGroup>

## Troubleshooting

### Models Not Appearing

If models don't show up in the interface:

1. **Check librechat.yaml syntax**:
   ```bash theme={null}
   # Validate YAML
   docker compose config
   ```

2. **Verify API key**:
   ```bash theme={null}
   # Test Eden AI endpoint
   curl -X POST https://api.edenai.run/v3/llm/chat/completions \
     -H "Authorization: Bearer YOUR_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{
       "model": "anthropic/claude-sonnet-4-5",
       "messages": [{"role": "user", "content": "test"}],
       "stream": true
     }'
   ```

3. **Clear cache and restart**:
   ```bash theme={null}
   docker compose down
   docker compose up -d
   ```

### Authentication Errors

If you see 401 errors:

1. Check `.env` has correct API key
2. Ensure no extra spaces in the key
3. Verify `OPENAI_REVERSE_PROXY` URL is correct
4. Restart services after changing `.env`

### Slow Responses

If responses are slow:

1. **Use faster models** for chat titles:
   ```yaml theme={null}
   titleModel: "openai/gpt-3.5-turbo"
   ```

2. **Disable unnecessary features**:
   ```yaml theme={null}
   summarize: false
   ```

3. **Check your internet connection** and Eden AI status

### Connection Refused

If LibreChat can't connect to MongoDB:

1. **Check MongoDB is running**:
   ```bash theme={null}
   docker compose ps mongodb
   ```

2. **Verify MONGO\_URI in .env**:
   ```bash theme={null}
   MONGO_URI=mongodb://mongodb:27017/LibreChat
   ```

3. **Check network connectivity**:
   ```bash theme={null}
   docker compose logs mongodb
   ```

## Security Best Practices

### 1. Secure API Keys

Never commit API keys to version control:

<CodeBlocks>
  <CodeBlock title=".gitignore">
    ```
        .env
        .env.local
        .env.production
    ```
  </CodeBlock>
</CodeBlocks>

### 2. Use Environment-Specific Configs

<CodeGroup>
  ```bash .env.production theme={null}
  # Production settings
  NODE_ENV=production
  ALLOW_REGISTRATION=false
  SESSION_SECRET=strong_random_secret_here
  ```
</CodeGroup>

### 3. Enable HTTPS

Use a reverse proxy like Nginx:

<CodeGroup>
  ```nginx nginx.conf theme={null}
  server {
    listen 443 ssl;
    server_name chat.yourdomain.com;

    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;

    location / {
      proxy_pass http://localhost:3080;
      proxy_http_version 1.1;
      proxy_set_header Upgrade $http_upgrade;
      proxy_set_header Connection 'upgrade';
      proxy_set_header Host $host;
      proxy_cache_bypass $http_upgrade;
    }
  }
  ```
</CodeGroup>

### 4. Implement Rate Limiting

Protect against abuse:

<CodeGroup>
  ```yaml librechat.yaml theme={null}
  rateLimits:
    fileUploads:
      ipMax: 50
      ipWindowInMinutes: 60
    conversationsImport:
      ipMax: 5
      ipWindowInMinutes: 60
  ```
</CodeGroup>

## Cost Optimization

### 1. Use Appropriate Models

Configure cheaper models for simple tasks:

<CodeGroup>
  ```yaml librechat.yaml theme={null}
  endpoints:
    custom:
      - name: "Eden AI"
        # Use GPT-3.5 for titles (cheaper)
        titleModel: "openai/gpt-3.5-turbo"
        # Use Claude Haiku for summaries (fast & cheap)
        summaryModel: "anthropic/claude-haiku-4-5"
  ```
</CodeGroup>

### 2. Monitor Usage

Track costs through Eden AI dashboard:

* View usage at [https://app.edenai.run](https://app.edenai.run)
* Set up billing alerts
* Review monthly reports

### 3. Limit Token Usage

<CodeGroup>
  ```yaml librechat.yaml theme={null}
  endpoints:
    custom:
      - name: "Eden AI"
        default:
          max_tokens: 1000  # Limit response length
  ```
</CodeGroup>

## Example Use Cases

### 1. Team Collaboration

Set up LibreChat for your team:

* **Enable user registration** for team members
* **Configure multiple endpoints** for different projects
* **Use presets** for common workflows (code review, documentation, etc.)

### 2. Customer Support

Deploy as an internal support tool:

* **Create presets** for support responses
* **Use conversation history** to maintain context
* **Configure rate limits** to prevent abuse

### 3. Development Assistant

Integrate with your development workflow:

* **Code assistance** with Claude or GPT-4
* **Documentation generation** with presets
* **Bug analysis** with vision models (screenshots)

## Next Steps

* [Open WebUI](./open-webui) - Alternative chat interface
* [Python SDK](../sdks/python-openai) - Programmatic access
* [Cost Management](../../how-to/cost-management/monitor-usage) - Track spending


# Open webui
Source: https://docs.edenai.co/v3/integrations/chat-platforms/open-webui



# Open WebUI

Configure Open WebUI (formerly Ollama WebUI) to use Eden AI for accessing 200+ AI models through a sleek interface.

## Overview

[Open WebUI](https://github.com/open-webui/open-webui) is a self-hosted, feature-rich web interface for AI models. By connecting it to Eden AI, you get:

* **200+ models**: Access OpenAI, Anthropic, Google, Cohere, and more
* **Modern UI**: Beautiful, responsive interface similar to ChatGPT
* **RAG support**: Document upload and retrieval-augmented generation
* **Multi-user**: User management with authentication
* **Self-hosted**: Complete data privacy and control

## Prerequisites

* Docker installed
* Eden AI API key from [https://app.edenai.run](https://app.edenai.run)
* 2GB+ RAM recommended

## Quick Start

### Option 1: Docker (Recommended)

Run Open WebUI with a single command:

<CodeGroup>
  ```bash bash theme={null}
  docker run -d \
    --name open-webui \
    -p 3000:8080 \
    -v open-webui:/app/backend/data \
    -e OPENAI_API_BASE_URL=https://api.edenai.run/v3/llm \
    -e OPENAI_API_KEY=YOUR_EDEN_AI_API_KEY \
    -e WEBUI_AUTH=False `# Disable authentication for single-user setup` \
    ghcr.io/open-webui/open-webui:main
  ```
</CodeGroup>

Access Open WebUI at `http://localhost:3000`

### Option 2: Docker Compose

Create a `docker-compose.yml` file:

<CodeGroup>
  ```yaml docker-compose.yml theme={null}
  version: '3.8'

  services:
    open-webui:
      image: ghcr.io/open-webui/open-webui:main
      container_name: open-webui
      ports:
        - "3000:8080"
      environment:
        - OPENAI_API_BASE_URL=https://api.edenai.run/v3/llm
        - OPENAI_API_KEY=${EDEN_AI_API_KEY}
        - WEBUI_SECRET_KEY=${WEBUI_SECRET_KEY}
      volumes:
        - open-webui:/app/backend/data
      restart: unless-stopped

  volumes:
    open-webui:
  ```

  ```bash .env theme={null}
  EDEN_AI_API_KEY=your_eden_ai_api_key_here
  WEBUI_SECRET_KEY=your_random_secret_key_here
  ```

  ```bash bash theme={null}
  # Start Open WebUI
  docker compose up -d

  # View logs
  docker compose logs -f

  # Stop
  docker compose down
  ```
</CodeGroup>

## Configuration

### Initial Setup

1. **Open browser**: Navigate to `http://localhost:3000`
2. **Create admin account**: Register the first user (becomes admin)
3. **Configure models**: Go to Settings → Models

### Add Eden AI Models

In the Open WebUI interface:

1. Click **Settings** (gear icon)
2. Go to **Models** tab
3. Add models in the format `provider/model`:

<CodeBlocks>
  <CodeBlock title="Models to Add">
    ```
        anthropic/claude-sonnet-4-5
        anthropic/claude-opus-4-5
        anthropic/claude-haiku-4-5
        openai/gpt-4
        openai/gpt-4-turbo
        openai/gpt-4o
        openai/gpt-3.5-turbo
        google/gemini-2.5-flash
        google/gemini-2.5-pro
        cohere/command-r-plus
    ```
  </CodeBlock>
</CodeBlocks>

### Environment Variables

Configure Open WebUI with environment variables:

<CodeGroup>
  ```bash .env theme={null}
  # Eden AI Configuration
  OPENAI_API_BASE_URL=https://api.edenai.run/v3/llm
  OPENAI_API_KEY=your_eden_ai_api_key

  # Application Settings
  WEBUI_SECRET_KEY=your_secret_key_here
  WEBUI_NAME=Eden AI Chat
  DATA_DIR=/app/backend/data

  # Authentication
  ENABLE_SIGNUP=true
  DEFAULT_USER_ROLE=user

  # Optional: RAG Settings
  ENABLE_RAG_WEB_SEARCH=true
  RAG_EMBEDDING_MODEL=text-embedding-3-small
  RAG_TOP_K=5
  CHUNK_SIZE=1500
  CHUNK_OVERLAP=100

  # Optional: Image Generation
  ENABLE_IMAGE_GENERATION=true
  IMAGE_GENERATION_MODEL=dall-e-3
  ```
</CodeGroup>

## Features

### Chat with Multiple Models

1. **Select model**: Click the model dropdown at the top
2. **Start chatting**: Type your message
3. **Switch models**: Change models mid-conversation
4. **Compare responses**: Use split-screen to compare model outputs

### Document Upload (RAG)

Upload documents for context-aware conversations:

<CodeGroup>
  ```yaml docker-compose.yml theme={null}
  services:
    open-webui:
      image: ghcr.io/open-webui/open-webui:main
      environment:
        - OPENAI_API_BASE_URL=https://api.edenai.run/v3/llm
        - OPENAI_API_KEY=${EDEN_AI_API_KEY}
        # Enable RAG
        - ENABLE_RAG_WEB_SEARCH=true
        - RAG_EMBEDDING_MODEL=openai/text-embedding-3-small
        - RAG_EMBEDDING_ENGINE=openai
        - RAG_EMBEDDING_OPENAI_BATCH_SIZE=1
  ```
</CodeGroup>

**Usage:**

1. Click the **+** icon in chat
2. Upload PDF, DOCX, TXT, or other documents
3. Ask questions about the uploaded content
4. The AI retrieves relevant sections automatically

### Image Generation

Generate images using DALL-E or other providers:

<CodeGroup>
  ```bash .env theme={null}
  # Enable image generation
  ENABLE_IMAGE_GENERATION=true
  IMAGE_GENERATION_MODEL=openai/dall-e-3
  IMAGE_GENERATION_ENGINE=openai

  # Use Eden AI endpoint
  AUTOMATIC1111_BASE_URL=https://api.edenai.run/v3
  ```
</CodeGroup>

**Usage:**
Type `/imagine` followed by your prompt in the chat.

### Web Search

Enable web search for up-to-date information:

<CodeGroup>
  ```bash .env theme={null}
  ENABLE_RAG_WEB_SEARCH=true
  RAG_WEB_SEARCH_ENGINE=searxng
  SEARXNG_QUERY_URL=https://searx.be/search?q=<query>
  ```
</CodeGroup>

### Voice Input

Enable voice-to-text:

<CodeGroup>
  ```bash .env theme={null}
  ENABLE_AUDIO=true
  AUDIO_STT_ENGINE=openai
  AUDIO_STT_MODEL=whisper-1
  ```
</CodeGroup>

## Advanced Configuration

### Multiple API Endpoints

Configure multiple providers:

<CodeGroup>
  ```yaml docker-compose.yml theme={null}
  services:
    open-webui:
      image: ghcr.io/open-webui/open-webui:main
      environment:
        # Eden AI as primary
        - OPENAI_API_BASE_URL=https://api.edenai.run/v3/llm
        - OPENAI_API_KEY=${EDEN_AI_API_KEY}

        # Additional endpoints (optional)
        - OPENAI_API_BASE_URLS=https://api.edenai.run/v3/llm,https://api.openai.com/v1
        - OPENAI_API_KEYS=${EDEN_AI_API_KEY},${OPENAI_API_KEY}
  ```
</CodeGroup>

### Custom Model Metadata

Define model capabilities and pricing:

<CodeGroup>
  ```json models.json theme={null}
  {
    "models": [
      {
        "id": "anthropic/claude-sonnet-4-5",
        "name": "Claude 3.5 Sonnet",
        "owned_by": "anthropic",
        "created": 1729900800,
        "object": "model",
        "info": {
          "description": "Most intelligent Claude model",
          "capabilities": {
            "vision": true,
            "function_calling": true
          }
        }
      },
      {
        "id": "openai/gpt-4o",
        "name": "GPT-4o",
        "owned_by": "openai",
        "created": 1715300000,
        "object": "model",
        "info": {
          "description": "GPT-4 with vision",
          "capabilities": {
            "vision": true,
            "function_calling": true
          }
        }
      }
    ]
  }
  ```
</CodeGroup>

### User Permissions

Configure role-based access:

<CodeGroup>
  ```bash .env theme={null}
  # User registration
  ENABLE_SIGNUP=true
  DEFAULT_USER_ROLE=user

  # Admin settings
  ADMIN_EMAIL=admin@example.com

  # Model access control
  ENABLE_MODEL_FILTER=true
  MODEL_FILTER_LIST=anthropic/claude-sonnet-4-5,openai/gpt-4
  ```
</CodeGroup>

### Persistent Storage

Configure data persistence:

<CodeGroup>
  ```yaml docker-compose.yml theme={null}
  services:
    open-webui:
      image: ghcr.io/open-webui/open-webui:main
      volumes:
        # Data persistence
        - ./data:/app/backend/data
        # Custom models
        - ./models.json:/app/backend/models.json:ro
        # User uploads
        - ./uploads:/app/backend/uploads
  ```
</CodeGroup>

## Security

### Authentication

Enable and configure authentication:

<CodeGroup>
  ```bash .env theme={null}
  # Require login
  WEBUI_AUTH=true

  # Session settings
  WEBUI_SECRET_KEY=generate_strong_random_key_here
  SESSION_TIMEOUT=3600

  # OAuth (optional)
  ENABLE_OAUTH_SIGNUP=true
  OAUTH_CLIENT_ID=your_client_id
  OAUTH_CLIENT_SECRET=your_client_secret
  OAUTH_PROVIDER_NAME=Google
  ```
</CodeGroup>

### HTTPS Setup

Use a reverse proxy for HTTPS:

<CodeGroup>
  ```nginx nginx.conf theme={null}
  server {
    listen 443 ssl http2;
    server_name chat.yourdomain.com;

    ssl_certificate /etc/ssl/certs/cert.pem;
    ssl_certificate_key /etc/ssl/private/key.pem;

    location / {
      proxy_pass http://localhost:3000;
      proxy_set_header Host $host;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header X-Forwarded-Proto $scheme;

      # WebSocket support
      proxy_http_version 1.1;
      proxy_set_header Upgrade $http_upgrade;
      proxy_set_header Connection "upgrade";
    }
  }
  ```
</CodeGroup>

### Rate Limiting

Protect your API key:

<CodeGroup>
  ```bash .env theme={null}
  # Rate limiting
  ENABLE_RATE_LIMIT=true
  RATE_LIMIT_REQUESTS=60
  RATE_LIMIT_WINDOW=60

  # Per-user limits
  USER_PERMISSIONS_CHAT_DAILY_LIMIT=100
  ```
</CodeGroup>

## Production Deployment

### Full Production Stack

<CodeGroup>
  ```yaml docker-compose.prod.yml theme={null}
  version: '3.8'

  services:
    open-webui:
      image: ghcr.io/open-webui/open-webui:main
      container_name: open-webui
      restart: always
      ports:
        - "127.0.0.1:3000:8080"
      environment:
        - OPENAI_API_BASE_URL=https://api.edenai.run/v3/llm
        - OPENAI_API_KEY=${EDEN_AI_API_KEY}
        - WEBUI_SECRET_KEY=${WEBUI_SECRET_KEY}
        - ENABLE_SIGNUP=false
        - DEFAULT_USER_ROLE=user
        - WEBUI_AUTH=true
      volumes:
        - ./data:/app/backend/data
        - ./uploads:/app/backend/uploads
      healthcheck:
        test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
        interval: 30s
        timeout: 10s
        retries: 3

    nginx:
      image: nginx:alpine
      container_name: nginx-proxy
      restart: always
      ports:
        - "80:80"
        - "443:443"
      volumes:
        - ./nginx.conf:/etc/nginx/nginx.conf:ro
        - ./ssl:/etc/ssl:ro
      depends_on:
        - open-webui
  ```
</CodeGroup>

### Backup Strategy

Backup your data regularly:

<CodeGroup>
  ```bash backup.sh theme={null}
  #!/bin/bash

  # Backup directory
  BACKUP_DIR="./backups/$(date +%Y%m%d_%H%M%S)"
  mkdir -p "$BACKUP_DIR"

  # Backup data
  docker compose exec open-webui tar czf /tmp/backup.tar.gz /app/backend/data
  docker cp open-webui:/tmp/backup.tar.gz "$BACKUP_DIR/"

  # Backup database (if using external DB)
  # docker compose exec postgres pg_dump -U user dbname > "$BACKUP_DIR/db.sql"

  echo "Backup completed: $BACKUP_DIR"
  ```
</CodeGroup>

## Troubleshooting

### Models Not Appearing

If models don't show up:

1. **Check API key**:
   ```bash theme={null}
   docker compose logs open-webui | grep -i "api"
   ```

2. **Verify base URL**:
   ```bash theme={null}
   docker compose exec open-webui env | grep OPENAI_API_BASE_URL
   ```

3. **Test endpoint manually**:
   ```bash theme={null}
   curl -X POST https://api.edenai.run/v3/llm/chat/completions \
     -H "Authorization: Bearer YOUR_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{
       "model": "anthropic/claude-sonnet-4-5",
       "messages": [{"role": "user", "content": "test"}],
       "stream": true
     }'
   ```

4. **Restart container**:
   ```bash theme={null}
   docker compose restart open-webui
   ```

### Authentication Issues

If you can't log in:

1. **Reset admin password**:
   ```bash theme={null}
   docker compose exec open-webui python manage.py reset-admin-password
   ```

2. **Check secret key**:
   ```bash theme={null}
   docker compose exec open-webui env | grep WEBUI_SECRET_KEY
   ```

### Performance Issues

If the UI is slow:

1. **Check resource usage**:
   ```bash theme={null}
   docker stats open-webui
   ```

2. **Increase memory**:
   ```yaml theme={null}
   services:
     open-webui:
       deploy:
         resources:
           limits:
             memory: 4G
   ```

3. **Optimize database**:
   ```bash theme={null}
   docker compose exec open-webui python manage.py optimize-db
   ```

### RAG Not Working

If document upload fails:

1. **Check volume mounts**:
   ```bash theme={null}
   docker compose exec open-webui ls -la /app/backend/uploads
   ```

2. **Verify embedding model**:
   ```bash theme={null}
   docker compose exec open-webui env | grep RAG_EMBEDDING
   ```

3. **Check logs**:
   ```bash theme={null}
   docker compose logs open-webui | grep -i "rag"
   ```

## Cost Optimization

### 1. Use Appropriate Models

Configure cheaper models for embeddings:

<CodeGroup>
  ```bash .env theme={null}
  # Use smaller embedding model
  RAG_EMBEDDING_MODEL=text-embedding-3-small

  # Use GPT-3.5 for simple tasks
  DEFAULT_MODEL=openai/gpt-3.5-turbo
  ```
</CodeGroup>

### 2. Limit Token Usage

Set maximum tokens:

<CodeGroup>
  ```bash .env theme={null}
  # Limit response length
  MAX_TOKENS=1000

  # Limit context
  MAX_CONTEXT_LENGTH=4000
  ```
</CodeGroup>

### 3. Monitor Usage

Track costs in Eden AI dashboard:

* Visit [https://app.edenai.run](https://app.edenai.run)
* View usage reports
* Set billing alerts

## Example Workflows

### 1. Customer Support Bot

* **Upload support docs** using RAG
* **Create templates** for common queries
* **Use Claude Haiku** for cost-effective responses

### 2. Code Assistant

* **Use GPT-4 or Claude** for complex code
* **Enable file upload** for code review
* **Configure presets** for different languages

### 3. Research Assistant

* **Enable web search** for current information
* **Use Gemini Pro** for long context
* **RAG for internal** documents

## Next Steps

* [LibreChat](./librechat) - Alternative chat platform
* [Continue.dev](../ai-assistants/continue-dev) - IDE integration
* [Cost Management](../../how-to/cost-management/monitor-usage) - Monitor spending


# Langchain
Source: https://docs.edenai.co/v3/integrations/frameworks/langchain



# LangChain

Integrate Eden AI with LangChain for building powerful LLM applications with access to 200+ models.

## Overview

[LangChain](https://langchain.com) is a framework for developing applications powered by language models. Eden AI integrates seamlessly with LangChain's `ChatOpenAI` class, giving you access to multiple providers through a single interface.

## Installation

Install LangChain and required dependencies:

<CodeGroup>
  ```bash Python theme={null}
  pip install "langchain~=1.2" "langchain-openai~=1.1" "langchain-community~=0.4" "langgraph~=1.0"
  ```

  ```bash TypeScript theme={null}
  npm install langchain @langchain/openai
  ```
</CodeGroup>

## Quick Start (Python)

Use Eden AI with LangChain's OpenAI integration:

<CodeGroup>
  ```python Python theme={null}
  from langchain_openai import ChatOpenAI
  from langchain_core.messages import HumanMessage, SystemMessage

  # Initialize with Eden AI endpoint

  llm = ChatOpenAI(
  model="openai/gpt-4",
  api_key="YOUR_EDEN_AI_API_KEY",
  base_url="https://api.edenai.run/v3/llm"
  )

  # Create messages

  messages = [
  SystemMessage(content="You are a helpful assistant."),
  HumanMessage(content="What is LangChain?")
  ]

  # Get response

  response = llm.invoke(messages)
  print(response.content)

  ```
</CodeGroup>

## Quick Start (TypeScript)

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { ChatOpenAI } from "@langchain/openai";
  import { HumanMessage, SystemMessage } from "@langchain/core/messages";

  const llm = new ChatOpenAI({
    modelName: "openai/gpt-4",
    openAIApiKey: "YOUR_EDEN_AI_API_KEY",
    configuration: {
      baseURL: "https://api.edenai.run/v3/llm",
    },
  });

  const messages = [
    new SystemMessage("You are a helpful assistant."),
    new HumanMessage("What is LangChain?"),
  ];

  const response = await llm.invoke(messages);
  console.log(response.content);
  ```
</CodeGroup>

## Available Models

Access any model from Eden AI:

<CodeGroup>
  ```python Python theme={null}
  from langchain_openai import ChatOpenAI

  # GPT-4

  gpt4 = ChatOpenAI(
  model="openai/gpt-4",
  api_key="YOUR_EDEN_AI_API_KEY",
  base_url="https://api.edenai.run/v3/llm"
  )

  # Claude Haiku

  claude_haiku = ChatOpenAI(
  model="openai/gpt-4",
  api_key="YOUR_EDEN_AI_API_KEY",
  base_url="https://api.edenai.run/v3/llm"
  )

  # Gemini Flash

  gemini = ChatOpenAI(
  model="google/gemini-2.5-flash",
  api_key="YOUR_EDEN_AI_API_KEY",
  base_url="https://api.edenai.run/v3/llm"
  )

  ```
</CodeGroup>

## Simple Responses

Get responses from the model:

<CodeGroup>
  ```python Python theme={null}
  from langchain_openai import ChatOpenAI
  from langchain_core.messages import HumanMessage

  llm = ChatOpenAI(
      model="openai/gpt-4",
      api_key="YOUR_EDEN_AI_API_KEY",
      base_url="https://api.edenai.run/v3/llm"
  )

  messages = [HumanMessage(content="Write a short story about AI.")]

  # Get response
  response = llm.invoke(messages)
  print(response.content)
  ```

  ```typescript TypeScript theme={null}
  import { ChatOpenAI } from "@langchain/openai";
  import { HumanMessage } from "@langchain/core/messages";

  const llm = new ChatOpenAI({
    modelName: "openai/gpt-4",
    openAIApiKey: "YOUR_EDEN_AI_API_KEY",
    configuration: {
      baseURL: "https://api.edenai.run/v3/llm",
    },
  });

  const messages = [new HumanMessage("Write a short story about AI.")];

  const response = await llm.invoke(messages);
  console.log(response.content);
  ```
</CodeGroup>

## Prompt Templates

Use LangChain's prompt templates:

<CodeGroup>
  ```python Python theme={null}
  from langchain_openai import ChatOpenAI
  from langchain_core.prompts import ChatPromptTemplate

  llm = ChatOpenAI(
  model="openai/gpt-4",
  api_key="YOUR_EDEN_AI_API_KEY",
  base_url="https://api.edenai.run/v3/llm"
  )

  # Create prompt template

  prompt = ChatPromptTemplate.from_messages([
  ("system", "You are a helpful assistant that translates {input_language} to {output_language}."),
  ("human", "{text}")
  ])

  # Create chain

  chain = prompt | llm

  # Run chain

  response = chain.invoke({
  "input_language": "English",
  "output_language": "French",
  "text": "Hello, how are you?"
  })

  print(response.content)

  ```
</CodeGroup>

## Chains

Build complex workflows with chains:

<CodeGroup>
  ```python Python theme={null}
  from langchain_openai import ChatOpenAI
  from langchain_core.prompts import ChatPromptTemplate
  from langchain_core.output_parsers import StrOutputParser

  llm = ChatOpenAI(
      model="openai/gpt-4",
      api_key="YOUR_EDEN_AI_API_KEY",
      base_url="https://api.edenai.run/v3/llm"
  )

  # Create prompts
  joke_prompt = ChatPromptTemplate.from_template(
      "Tell me a joke about {topic}"
  )

  explanation_prompt = ChatPromptTemplate.from_template(
      "Explain this joke: {joke}"
  )

  # Create chains
  joke_chain = joke_prompt | llm | StrOutputParser()
  explanation_chain = explanation_prompt | llm | StrOutputParser()

  # Compose chains
  full_chain = {"joke": joke_chain} | explanation_chain

  # Run
  result = full_chain.invoke({"topic": "programming"})
  print(result)
  ```
</CodeGroup>

## RAG (Retrieval-Augmented Generation)

Build RAG applications with vector stores:

<CodeGroup>
  ```python Python theme={null}
  from langchain_openai import ChatOpenAI
  from langchain_text_splitters import RecursiveCharacterTextSplitter
  from langchain_core.documents import Document
  from langchain_core.prompts import ChatPromptTemplate
  from langchain_core.output_parsers import StrOutputParser
  from langchain_core.runnables import RunnablePassthrough

  # Initialize LLM with Eden AI

  llm = ChatOpenAI(
  model="openai/gpt-4",
  api_key="YOUR_EDEN_AI_API_KEY",
  base_url="https://api.edenai.run/v3/llm"
  )

  # Create documents (replace with your data source)

  docs = [Document(page_content="""
  Eden AI provides a unified API for 200+ AI models across providers
  like OpenAI, Google, and Anthropic. It supports text, image, audio,
  and video processing through a single endpoint.
  """)]

  # Split documents into chunks

  text_splitter = RecursiveCharacterTextSplitter(
  chunk_size=200,
  chunk_overlap=50
  )
  splits = text_splitter.split_documents(docs)

  # Build RAG chain with LCEL (using splits as context)

  def format_docs(docs):
      return "\n\n".join(doc.page_content for doc in docs)

  prompt = ChatPromptTemplate.from_template(
  "Answer the question based on the context:\n\n{context}\n\nQuestion: {question}"
  )

  chain = (
  {"context": lambda _: format_docs(splits), "question": RunnablePassthrough()}
  | prompt
  | llm
  | StrOutputParser()
  )

  # Query

  result = chain.invoke("What does Eden AI do?")
  print(result)

  ```
</CodeGroup>

## Agents

Create autonomous agents:

<CodeGroup>
  ```python Python theme={null}
  from langchain_openai import ChatOpenAI
  from langchain_core.tools import tool
  from langchain.agents import create_agent

  # Initialize LLM
  llm = ChatOpenAI(
      model="openai/gpt-4",
      api_key="YOUR_EDEN_AI_API_KEY",
      base_url="https://api.edenai.run/v3/llm",
      temperature=0
  )

  # Define tools
  @tool
  def search(query: str) -> str:
      """Search for information"""
      return f"Search results for: {query}"

  @tool
  def calculator(expression: str) -> str:
      """Calculate mathematical expressions"""
      try:
          return str(eval(expression))
      except Exception as e:
          return f"Error: {str(e)}"

  # Create agent
  agent = create_agent(llm, [search, calculator])

  # Run agent
  result = agent.invoke({
      "messages": [{"role": "user", "content": "What is 25 * 4 + 10?"}]
  })
  print(result["messages"][-1].content)
  ```
</CodeGroup>

## Conversational Memory

Add memory to maintain context:

<CodeGroup>
  ```python Python theme={null}
  from langchain_openai import ChatOpenAI
  from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
  from langchain_core.runnables.history import RunnableWithMessageHistory
  from langchain_core.chat_history import InMemoryChatMessageHistory

  llm = ChatOpenAI(
  model="openai/gpt-4",
  api_key="YOUR_EDEN_AI_API_KEY",
  base_url="https://api.edenai.run/v3/llm"
  )

  # Create prompt with history placeholder
  prompt = ChatPromptTemplate.from_messages([
      ("system", "You are a helpful assistant."),
      MessagesPlaceholder(variable_name="history"),
      ("human", "{input}")
  ])

  chain = prompt | llm

  # Store sessions in memory
  sessions = {}

  def get_session_history(session_id: str):
      if session_id not in sessions:
          sessions[session_id] = InMemoryChatMessageHistory()
      return sessions[session_id]

  # Wrap chain with message history
  with_history = RunnableWithMessageHistory(
      chain,
      get_session_history,
      input_messages_key="input",
      history_messages_key="history"
  )

  # Have a multi-turn conversation
  config = {"configurable": {"session_id": "user-1"}}

  response1 = with_history.invoke({"input": "Hi! My name is Alice."}, config=config)
  print(response1.content)

  response2 = with_history.invoke({"input": "What's my name?"}, config=config)
  print(response2.content)

  ```
</CodeGroup>

## Function Calling (Tools)

Use function calling for structured outputs:

<CodeGroup>
  ```python Python theme={null}
  from langchain_openai import ChatOpenAI
  from langchain_core.tools import tool
  from langchain_core.messages import HumanMessage

  @tool
  def get_weather(city: str) -> str:
      """Get the current weather for a city"""
      # Implement weather API call
      return f"The weather in {city} is sunny, 72°F"

  llm = ChatOpenAI(
      model="openai/gpt-4",
      api_key="YOUR_EDEN_AI_API_KEY",
      base_url="https://api.edenai.run/v3/llm"
  )

  # Bind tools to LLM
  llm_with_tools = llm.bind_tools([get_weather])

  # Invoke
  messages = [HumanMessage(content="What's the weather in Paris?")]
  response = llm_with_tools.invoke(messages)

  # Check if tool was called
  if response.tool_calls:
      tool_call = response.tool_calls[0]
      result = get_weather.invoke(tool_call["args"])
      print(result)
  ```
</CodeGroup>

## Output Parsing

Parse structured outputs:

<CodeGroup>
  ```python Python theme={null}
  from langchain_openai import ChatOpenAI
  from langchain_core.prompts import ChatPromptTemplate
  from langchain_core.output_parsers import PydanticOutputParser
  from langchain_core.exceptions import OutputParserException
  from pydantic import BaseModel, Field

  # Define output schema
  class Person(BaseModel):
      name: str = Field(description="Person's name")
      age: int = Field(description="Person's age")
      occupation: str = Field(description="Person's occupation")

  llm = ChatOpenAI(
  model="openai/gpt-4",
  api_key="YOUR_EDEN_AI_API_KEY",
  base_url="https://api.edenai.run/v3/llm"
  )

  parser = PydanticOutputParser(pydantic_object=Person)

  prompt = ChatPromptTemplate.from_template(
  "Extract information about the person.\n{format_instructions}\n{query}"
  )

  chain = prompt | llm | parser

  try:
      result = chain.invoke({
          "query": "John Doe is a 35-year-old software engineer.",
          "format_instructions": parser.get_format_instructions()
      })

      print(f"Name: {result.name}")
      print(f"Age: {result.age}")
      print(f"Occupation: {result.occupation}")
  except OutputParserException as e:
      print(f"Parsing failed: {e}")

  ```
</CodeGroup>

## Multi-Provider Comparison

Compare responses from different providers:

<CodeGroup>
  ```python Python theme={null}
  from langchain_openai import ChatOpenAI
  from langchain_core.messages import HumanMessage
  import asyncio

  async def compare_providers(question: str):
      providers = [
          ("Claude", "anthropic/claude-sonnet-4-5"),
          ("GPT-4", "openai/gpt-4"),
          ("Gemini", "google/gemini-2.5-flash")
      ]

      tasks = []
      for name, model in providers:
          llm = ChatOpenAI(
              model=model,
              api_key="YOUR_EDEN_AI_API_KEY",
              base_url="https://api.edenai.run/v3/llm"
          )
          tasks.append(llm.ainvoke([HumanMessage(content=question)]))

      responses = await asyncio.gather(*tasks)

      for (name, _), response in zip(providers, responses):
          print(f"\n{name}:")
          print(response.content)
          print("-" * 80)

  # Run comparison
  asyncio.run(compare_providers("Explain quantum computing in simple terms."))
  ```
</CodeGroup>

## Environment Variables

Store credentials securely:

<CodeGroup>
  ```bash .env theme={null}
  EDEN_AI_API_KEY=your_api_key_here
  ```

  ```python Python theme={null}
  import os
  from dotenv import load_dotenv
  from langchain_openai import ChatOpenAI

  load_dotenv()

  llm = ChatOpenAI(
      model="openai/gpt-4",
      api_key=os.getenv("EDEN_AI_API_KEY"),
      base_url="https://api.edenai.run/v3/llm"
  )
  ```
</CodeGroup>

## Best Practices

### 1. Choose the Right Model

Select models based on your use case:

* **Complex reasoning**: `openai/gpt-5.2`
* **Fast and cost-effective**: `anthropic/claude-haiku-4-5`

### 2. Implement Error Handling

Wrap API calls in try-except blocks:

```python theme={null}
try:
    response = llm.invoke(messages)
except Exception as e:
    print(f"Error: {e}")
```

### 3. Cache Results

Use LangChain's caching to avoid redundant API calls:

```python theme={null}
from langchain_community.cache import InMemoryCache
from langchain_core.globals import set_llm_cache

set_llm_cache(InMemoryCache())
```

## Next Steps

* [Python SDK](../sdks/python-openai) - Direct SDK usage


# Integrations
Source: https://docs.edenai.co/v3/integrations/index



# Integrations

Integrate Eden AI V3 into your favorite tools, frameworks, and development environments.

## Overview

Eden AI V3 provides an **OpenAI-compatible API** for LLMs and a **Universal AI endpoint** for all other features. This makes it easy to integrate with virtually any tool that supports OpenAI or custom API endpoints.

### Key Integration Points

* **LLM Endpoint**: `/v3/llm/chat/completions` - Drop-in replacement for OpenAI's chat API
* **Universal AI**: `/v3/universal-ai` - Single endpoint for OCR, image processing, text analysis, and more
* **File Upload**: `/v3/upload` - Persistent file storage for multi-step workflows

## Quick Start

Most integrations only require two simple changes:

1. **API Key**: Use your Eden AI API key
2. **Base URL**: Point to `https://api.edenai.run/v3/llm`

<CodeGroup>
  ```python Python (OpenAI SDK) theme={null}
  from openai import OpenAI

  client = OpenAI(
      api_key="YOUR_EDEN_AI_API_KEY",
      base_url="https://api.edenai.run/v3/llm"
  )

  # Now use any provider through the OpenAI SDK
  response = client.chat.completions.create(
      model="anthropic/claude-sonnet-4-5",
      messages=[{"role": "user", "content": "Hello!"}]
  )
  print(response.choices[0].message.content)
  ```

  ```typescript TypeScript (OpenAI SDK) theme={null}
  import OpenAI from 'openai';

  const client = new OpenAI({
    apiKey: 'YOUR_EDEN_AI_API_KEY',
    baseURL: 'https://api.edenai.run/v3/llm',
  });

  // Use any provider
  const response = await client.chat.completions.create({
    model: 'openai/gpt-4',
    messages: [{role: 'user', content: 'Hello!'}]
  });
  console.log(response.choices[0].message.content);
  ```
</CodeGroup>

## Integration Categories

### SDKs

Official and community SDKs for popular programming languages.

<Cards>
  <Card title="Python (OpenAI SDK)" icon="fa-brands fa-python" href="./sdks/python-openai">
    Use the official OpenAI Python SDK with Eden AI
  </Card>

  <Card title="TypeScript (OpenAI SDK)" icon="fa-brands fa-node-js" href="./sdks/typescript-openai">
    Use the OpenAI TypeScript/JavaScript SDK
  </Card>
</Cards>

### AI Assistants & Agents

Integrate Eden AI with popular AI coding assistants and agents.

<Cards>
  <Card title="Claude Code" icon="fa-light fa-terminal" href="./ai-assistants/claude-code">
    Configure Claude Code CLI to use Eden AI
  </Card>

  <Card title="Continue.dev" icon="fa-light fa-code" href="./ai-assistants/continue-dev">
    VS Code autopilot powered by Eden AI
  </Card>
</Cards>

### AI Frameworks

Build powerful AI applications with popular frameworks.

<Cards>
  <Card title="LangChain" icon="fa-light fa-link" href="./frameworks/langchain">
    Python and JavaScript LangChain integration
  </Card>
</Cards>

### Chat Platforms

Deploy AI chat interfaces with Eden AI as the backend.

<Cards>
  <Card title="LibreChat" icon="fa-light fa-comments" href="./chat-platforms/librechat">
    Open-source ChatGPT alternative
  </Card>

  <Card title="Open WebUI" icon="fa-light fa-browser" href="./chat-platforms/open-webui">
    Self-hosted web UI for LLMs
  </Card>
</Cards>

## Multi-Provider Support

Eden AI's unique advantage is **multi-provider support**. Access models from multiple providers through a single integration:

* **OpenAI**: GPT-4, GPT-3.5
* **Anthropic**: Claude 3.5 Sonnet, Claude 3 Opus
* **Google**: Gemini Pro, Gemini 1.5 Pro
* **Cohere**: Command R+, Command R
* **Meta**: Llama 3 70B, Llama 3 8B
* **And 200+ more models**

Simply change the model parameter to switch providers:

```python theme={null}
# Use OpenAI
model="openai/gpt-4"

# Switch to Anthropic
model="anthropic/claude-sonnet-4-5"

# Try Google
model="google/gemini-2.5-flash"
```

## Beyond LLMs: Universal AI

Eden AI isn't just for chat. The **Universal AI endpoint** gives you access to:

* **Text Analysis**: AI detection, moderation, embeddings, spell check
* **OCR**: Document parsing, invoice extraction, identity verification
* **Image**: Generation, object detection, face detection, background removal
* **Translation**: Multi-language document translation

<CodeGroup>
  ```python Python theme={null}
  import requests

  # OCR with Google Cloud Vision

  response = requests.post(
  "https://api.edenai.run/v3/universal-ai",
  headers={"Authorization": "Bearer YOUR_API_KEY"},
  json={
  "model": "ocr/financial_parser/google",
  "input": {"file": "file_id_or_url"}
  }
  )

  # Image generation with DALL-E 3

  response = requests.post(
  "https://api.edenai.run/v3/universal-ai",
  headers={"Authorization": "Bearer YOUR_API_KEY"},
  json={
  "model": "image/generation/openai/dall-e-3",
  "input": {"prompt": "A sunset over mountains"}
  }
  )
  ```
</CodeGroup>

## Need Help?

* Browse integration-specific guides using the navigation menu
* Visit the [How-To Guides](../how-to/llm/chat-completions) for feature-specific tutorials
* See [FAQ](../get-started/faq) for common questions

## Contributing

Built an integration we haven't covered? We'd love to hear about it! Contact us through [Discord](https://discord.gg/2AZqDEEb) or [GitHub](https://github.com/edenai).


# Python openai
Source: https://docs.edenai.co/v3/integrations/sdks/python-openai



# Python (OpenAI SDK)

Use the official OpenAI Python SDK with Eden AI to access 200+ AI models through a familiar interface.

## Overview

The OpenAI Python SDK is fully compatible with Eden AI's V3 API. Simply point the SDK to Eden AI's endpoint and you can access models from OpenAI, Anthropic, Google, Cohere, Meta, and more.

## Installation

Install the OpenAI Python SDK:

<CodeGroup>
  ```bash pip theme={null}
  pip install openai
  ```

  ```bash poetry theme={null}
  poetry add openai
  ```
</CodeGroup>

## Quick Start

Configure the OpenAI client to use Eden AI:

<CodeGroup>
  ```python Python theme={null}
  from openai import OpenAI

  # Initialize client with Eden AI endpoint

  client = OpenAI(
  api_key="YOUR_EDEN_AI_API_KEY", # Get from https://app.edenai.run
  base_url="https://api.edenai.run/v3/llm"
  )

  # Make a request

  response = client.chat.completions.create(
  model="openai/gpt-4",
  messages=[
  {"role": "user", "content": "Hello! How are you?"}
  ]
  )

  # Print the response

  print(response.choices[0].message.content)

  ```
</CodeGroup>

## Available Models

Access models from multiple providers using the `provider/model` format:

### OpenAI

* `openai/gpt-4`
* `openai/gpt-4-turbo`
* `openai/gpt-4o`
* `openai/gpt-3.5-turbo`

### Anthropic

* `anthropic/claude-sonnet-4-5`
* `anthropic/claude-opus-4-5`
* `anthropic/claude-sonnet-4-5`
* `anthropic/claude-haiku-4-5`

### Google

* `google/gemini-2.5-pro`
* `google/gemini-2.5-flash`

### Cohere

* `cohere/command-r-plus`
* `cohere/command-r`

### Meta

* `meta/llama-3-70b`
* `meta/llama-3-8b`

## Multi-Turn Conversations

Build conversational applications with message history:

<CodeGroup>
  ```python Python theme={null}
  from openai import OpenAI

  client = OpenAI(
      api_key="YOUR_EDEN_AI_API_KEY",
      base_url="https://api.edenai.run/v3/llm"
  )

  messages = [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "What is the capital of France?"}
  ]

  # First interaction
  response = client.chat.completions.create(
      model="anthropic/claude-sonnet-4-5",
      messages=messages
  )

  assistant_response = response.choices[0].message.content
  print(assistant_response)

  # Add assistant response to history
  messages.append({"role": "assistant", "content": assistant_response})

  # Continue conversation
  messages.append({"role": "user", "content": "What's the population?"})

  response = client.chat.completions.create(
      model="anthropic/claude-sonnet-4-5",
      messages=messages
  )

  print(response.choices[0].message.content)
  ```
</CodeGroup>

## Advanced Parameters

Control model behavior with standard OpenAI parameters:

<CodeGroup>
  ```python Python theme={null}
  from openai import OpenAI

  client = OpenAI(
  api_key="YOUR_EDEN_AI_API_KEY",
  base_url="https://api.edenai.run/v3/llm"
  )

  response = client.chat.completions.create(
  model="openai/gpt-4",
  messages=[
  {"role": "user", "content": "Write a creative story about AI."}
  ],
  temperature=0.9, # Higher = more creative (0-2)
  max_tokens=500, # Limit response length
  top_p=1.0, # Nucleus sampling
  frequency_penalty=0.0, # Penalize repetition (-2 to 2)
  presence_penalty=0.0 # Penalize topic repetition (-2 to 2)
  )

  print(response.choices[0].message.content)

  ```
</CodeGroup>

## Vision Capabilities

Send images to vision-capable models:

<CodeGroup>
  ```python Python theme={null}
  from openai import OpenAI

  client = OpenAI(
      api_key="YOUR_EDEN_AI_API_KEY",
      base_url="https://api.edenai.run/v3/llm"
  )

  # First, upload the image to get a file_id
  import requests

  upload_response = requests.post(
      "https://api.edenai.run/v3/upload",
      headers={"Authorization": f"Bearer YOUR_EDEN_AI_API_KEY"},
      files={"file": open("image.jpg", "rb")}
  )
  file_id = upload_response.json()["file_id"]

  # Use the file_id in a chat message
  response = client.chat.completions.create(
      model="openai/gpt-4o",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "What's in this image?"},
                  {"type": "file", "file": {"file_id": file_id}}
              ]
          }
      ]
  )

  print(response.choices[0].message.content)
  ```
</CodeGroup>

## Async Support

Use async/await for concurrent requests:

<CodeGroup>
  ```python Python theme={null}
  from openai import AsyncOpenAI
  import asyncio

  async def main():
      client = AsyncOpenAI(
          api_key="YOUR_EDEN_AI_API_KEY",
          base_url="https://api.edenai.run/v3/llm"
      )

      response = await client.chat.completions.create(
          model="openai/gpt-4",
          messages=[
              {"role": "user", "content": "Hello!"}
          ]
      )

      print(response.choices[0].message.content)

  asyncio.run(main())

  ```
</CodeGroup>

## Error Handling

Handle API errors gracefully:

<CodeGroup>
  ```python Python theme={null}
  from openai import OpenAI, OpenAIError
  import openai

  client = OpenAI(
      api_key="YOUR_EDEN_AI_API_KEY",
      base_url="https://api.edenai.run/v3/llm"
  )

  try:
      response = client.chat.completions.create(
          model="openai/gpt-4",
          messages=[{"role": "user", "content": "Hello!"}]
      )

      print(response.choices[0].message.content)

  except openai.AuthenticationError as e:
      print(f"Authentication failed: {e}")
  except openai.RateLimitError as e:
      print(f"Rate limit exceeded: {e}")
  except openai.APIError as e:
      print(f"API error: {e}")
  except Exception as e:
      print(f"Unexpected error: {e}")
  ```
</CodeGroup>

## Complete Example

A full example with conversation management:

<CodeGroup>
  ```python Python theme={null}
  from openai import OpenAI
  import sys

  def chat_with_ai():
      client = OpenAI(
          api_key="YOUR_EDEN_AI_API_KEY",
          base_url="https://api.edenai.run/v3/llm"
      )

      messages = [
          {"role": "system", "content": "You are a helpful assistant."}
      ]

      print("Chat with AI (type 'quit' to exit)")
      print("-" * 50)

      while True:
          # Get user input
          user_input = input("\nYou: ").strip()

          if user_input.lower() == 'quit':
              break

          if not user_input:
              continue

          # Add user message
          messages.append({"role": "user", "content": user_input})

          # Get AI response
          response = client.chat.completions.create(
              model="anthropic/claude-sonnet-4-5",
              messages=messages,
              temperature=0.7
          )

          assistant_response = response.choices[0].message.content
          print(f"\nAssistant: {assistant_response}")

          # Add assistant response to history
          messages.append({"role": "assistant", "content": assistant_response})

  if __name__ == "__main__":
      chat_with_ai()

  ```
</CodeGroup>

## List Available Models

Discover available models programmatically:

<CodeGroup>
  ```python Python theme={null}
  import requests

  response = requests.get(
      "https://api.edenai.run/v3/llm/models",
      headers={"Authorization": "Bearer YOUR_EDEN_AI_API_KEY"}
  )

  models = response.json()

  # Print models by provider
  providers = {}
  for model in models["data"]:
      provider = model["owned_by"]
      if provider not in providers:
          providers[provider] = []
      providers[provider].append(model["id"])

  for provider, model_list in providers.items():
      print(f"\n{provider}:")
      for model_id in model_list:
          print(f"  - {model_id}")
  ```
</CodeGroup>

## Environment Variables

Store your API key securely using environment variables:

<CodeGroup>
  ```python Python theme={null}
  import os
  from openai import OpenAI

  client = OpenAI(
  api_key=os.getenv("EDEN_AI_API_KEY"),
  base_url="https://api.edenai.run/v3/llm"
  )

  ```

  ```bash .env theme={null}
  EDEN_AI_API_KEY=your_api_key_here
  ```
</CodeGroup>

Use with `python-dotenv`:

<CodeGroup>
  ```python Python theme={null}
  from dotenv import load_dotenv
  import os
  from openai import OpenAI

  load_dotenv()

  client = OpenAI(
  api_key=os.getenv("EDEN_AI_API_KEY"),
  base_url="https://api.edenai.run/v3/llm"
  )

  ```
</CodeGroup>

## Troubleshooting

### Authentication Errors

Ensure your API key is correct and has the `Bearer` prefix when using raw requests:

```python theme={null}
headers = {"Authorization": "Bearer YOUR_API_KEY"}
```

### Rate Limiting

If you hit rate limits, implement exponential backoff:

<CodeGroup>
  ```python Python theme={null}
  import time
  from openai import OpenAI, RateLimitError

  client = OpenAI(
      api_key="YOUR_EDEN_AI_API_KEY",
      base_url="https://api.edenai.run/v3/llm"
  )

  def create_completion_with_retry(messages, max_retries=3):
      for attempt in range(max_retries):
          try:
              return client.chat.completions.create(
                  model="openai/gpt-4",
                  messages=messages
              )
          except RateLimitError:
              if attempt < max_retries - 1:
                  wait_time = 2 ** attempt  # Exponential backoff
                  print(f"Rate limited. Waiting {wait_time}s...")
                  time.sleep(wait_time)
              else:
                  raise

  ```
</CodeGroup>

## Next Steps

* [Vision Capabilities](../../how-to/llm/vision-capabilities) - Working with images
* [File Attachments](../../how-to/llm/file-attachments) - Uploading files
* [Provider Comparison](../../how-to/llm/provider-comparison) - Choosing the right model

```
```


# Typescript openai
Source: https://docs.edenai.co/v3/integrations/sdks/typescript-openai



# TypeScript (OpenAI SDK)

Use the official OpenAI TypeScript/JavaScript SDK with Eden AI for seamless multi-provider access.

## Overview

The OpenAI TypeScript SDK works perfectly with Eden AI's V3 API. Configure the base URL and start using 200+ models from multiple providers.

## Installation

Install the OpenAI SDK for Node.js:

<CodeGroup>
  ```bash npm theme={null}
  npm install openai
  ```

  ```bash yarn theme={null}
  yarn add openai
  ```

  ```bash pnpm theme={null}
  pnpm add openai
  ```
</CodeGroup>

## Quick Start

Configure the client to use Eden AI:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import OpenAI from 'openai';

  const client = new OpenAI({
    apiKey: 'YOUR_EDEN_AI_API_KEY',
    baseURL: 'https://api.edenai.run/v3/llm',
  });

  async function main() {
    const stream = await client.chat.completions.create({
      model: 'openai/gpt-4',
      messages: [{ role: 'user', content: 'Hello! How are you?' }],
      stream: true,
    });

    for await (const chunk of stream) {
      const content = chunk.choices[0]?.delta?.content;
      if (content) {
        process.stdout.write(content);
      }
    }
  }

  main();
  ```

  ```javascript JavaScript (ESM) theme={null}
  import OpenAI from 'openai';

  const client = new OpenAI({
    apiKey: 'YOUR_EDEN_AI_API_KEY',
    baseURL: 'https://api.edenai.run/v3/llm',
  });

  const stream = await client.chat.completions.create({
    model: 'anthropic/claude-sonnet-4-5',
    messages: [{ role: 'user', content: 'Hello!' }],
    stream: true,
  });

  for await (const chunk of stream) {
    const content = chunk.choices[0]?.delta?.content;
    if (content) {
      process.stdout.write(content);
    }
  }
  ```

  ```javascript JavaScript (CommonJS) theme={null}
  const OpenAI = require('openai');

  const client = new OpenAI({
    apiKey: 'YOUR_EDEN_AI_API_KEY',
    baseURL: 'https://api.edenai.run/v3/llm',
  });

  async function main() {
    const stream = await client.chat.completions.create({
      model: 'openai/gpt-4',
      messages: [{ role: 'user', content: 'Hello!' }],
      stream: true,
    });

    for await (const chunk of stream) {
      const content = chunk.choices[0]?.delta?.content;
      if (content) {
        process.stdout.write(content);
      }
    }
  }

  main();
  ```
</CodeGroup>

## Available Models

Access models from multiple providers:

### OpenAI

* `openai/gpt-4`
* `openai/gpt-4-turbo`
* `openai/gpt-4o`
* `openai/gpt-3.5-turbo`

### Anthropic

* `anthropic/claude-sonnet-4-5`
* `anthropic/claude-opus-4-5`
* `anthropic/claude-sonnet-4-5`

### Google

* `google/gemini-2.5-pro`
* `google/gemini-2.5-flash`

### Cohere & Meta

* `cohere/command-r-plus`
* `meta/llama-3-70b`

## Multi-Turn Conversations

Build stateful chat applications:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import OpenAI from 'openai';
  import type { ChatCompletionMessageParam } from 'openai/resources/chat/completions';

  const client = new OpenAI({
    apiKey: process.env.EDEN_AI_API_KEY!,
    baseURL: 'https://api.edenai.run/v3/llm',
  });

  async function chat() {
    const messages: ChatCompletionMessageParam[] = [
      { role: 'system', content: 'You are a helpful assistant.' },
      { role: 'user', content: 'What is the capital of France?' },
    ];

    // First interaction
    const stream1 = await client.chat.completions.create({
      model: 'anthropic/claude-sonnet-4-5',
      messages,
      stream: true,
    });

    let assistantResponse = '';
    for await (const chunk of stream1) {
      const content = chunk.choices[0]?.delta?.content;
      if (content) {
        process.stdout.write(content);
        assistantResponse += content;
      }
    }

    // Add to conversation history
    messages.push({ role: 'assistant', content: assistantResponse });
    messages.push({ role: 'user', content: "What's the population?" });

    // Continue conversation
    const stream2 = await client.chat.completions.create({
      model: 'anthropic/claude-sonnet-4-5',
      messages,
      stream: true,
    });

    for await (const chunk of stream2) {
      const content = chunk.choices[0]?.delta?.content;
      if (content) {
        process.stdout.write(content);
      }
    }
  }

  chat();
  ```
</CodeGroup>

## Advanced Parameters

Control model behavior:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import OpenAI from 'openai';

  const client = new OpenAI({
    apiKey: process.env.EDEN_AI_API_KEY!,
    baseURL: 'https://api.edenai.run/v3/llm',
  });

  const stream = await client.chat.completions.create({
    model: 'openai/gpt-4',
    messages: [
      { role: 'user', content: 'Write a creative story about AI.' },
    ],
    temperature: 0.9,        // Higher = more creative (0-2)
    max_tokens: 500,         // Limit response length
    top_p: 1.0,              // Nucleus sampling
    frequency_penalty: 0.0,  // Penalize repetition
    presence_penalty: 0.0,   // Penalize topic repetition
    stream: true,
  });

  for await (const chunk of stream) {
    const content = chunk.choices[0]?.delta?.content;
    if (content) {
      process.stdout.write(content);
    }
  }
  ```
</CodeGroup>

## Vision Capabilities

Send images to vision models:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import OpenAI from 'openai';
  import FormData from 'form-data';
  import fs from 'fs';
  import fetch from 'node-fetch';

  const client = new OpenAI({
    apiKey: process.env.EDEN_AI_API_KEY!,
    baseURL: 'https://api.edenai.run/v3/llm',
  });

  async function analyzeImage() {
    // First, upload the image
    const formData = new FormData();
    formData.append('file', fs.createReadStream('image.jpg'));

    const uploadResponse = await fetch(
      'https://api.edenai.run/v3/upload',
      {
        method: 'POST',
        headers: {
          Authorization: `Bearer ${process.env.EDEN_AI_API_KEY}`,
        },
        body: formData,
      }
    );

    const { file_id } = await uploadResponse.json();

    // Use file_id in chat
    const stream = await client.chat.completions.create({
      model: 'openai/gpt-4o',
      messages: [
        {
          role: 'user',
          content: [
            { type: 'text', text: "What's in this image?" },
            { type: 'file', file: { file_id } },
          ],
        },
      ],
      stream: true,
    });

    for await (const chunk of stream) {
      const content = chunk.choices[0]?.delta?.content;
      if (content) {
        process.stdout.write(content);
      }
    }
  }

  analyzeImage();
  ```
</CodeGroup>

## Error Handling

Handle API errors properly:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import OpenAI from 'openai';

  const client = new OpenAI({
    apiKey: process.env.EDEN_AI_API_KEY!,
    baseURL: 'https://api.edenai.run/v3/llm',
  });

  async function safeChat() {
    try {
      const stream = await client.chat.completions.create({
        model: 'openai/gpt-4',
        messages: [{ role: 'user', content: 'Hello!' }],
        stream: true,
      });

      for await (const chunk of stream) {
        const content = chunk.choices[0]?.delta?.content;
        if (content) {
          process.stdout.write(content);
        }
      }
    } catch (error) {
      if (error instanceof OpenAI.APIError) {
        console.error(`API Error (${error.status}):`, error.message);

        if (error.status === 401) {
          console.error('Authentication failed. Check your API key.');
        } else if (error.status === 429) {
          console.error('Rate limit exceeded. Please wait and retry.');
        } else if (error.status === 402) {
          console.error('Insufficient credits. Please add credits to your account.');
        }
      } else {
        console.error('Unexpected error:', error);
      }
    }
  }

  safeChat();
  ```
</CodeGroup>

## Express.js Integration

Build a chat API with Express:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import express from 'express';
  import OpenAI from 'openai';

  const app = express();
  app.use(express.json());

  const client = new OpenAI({
    apiKey: process.env.EDEN_AI_API_KEY!,
    baseURL: 'https://api.edenai.run/v3/llm',
  });

  app.post('/api/chat', async (req, res) => {
    try {
      const { messages, model = 'openai/gpt-4' } = req.body;

      res.setHeader('Content-Type', 'text/event-stream');
      res.setHeader('Cache-Control', 'no-cache');
      res.setHeader('Connection', 'keep-alive');

      const stream = await client.chat.completions.create({
        model,
        messages,
        stream: true,
      });

      for await (const chunk of stream) {
        const content = chunk.choices[0]?.delta?.content;
        if (content) {
          res.write(`data: ${JSON.stringify({ content })}\n\n`);
        }
      }

      res.write('data: [DONE]\n\n');
      res.end();
    } catch (error) {
      console.error('Error:', error);
      res.status(500).json({ error: 'Internal server error' });
    }
  });

  app.listen(3000, () => {
    console.log('Server running on http://localhost:3000');
  });
  ```
</CodeGroup>

## React Integration

Stream responses in a React application:

<CodeGroup>
  ```typescript TypeScript (React) theme={null}
  import { useState } from 'react';

  export function ChatComponent() {
    const [messages, setMessages] = useState<Array<{role: string, content: string}>>([]);
    const [input, setInput] = useState('');
    const [streaming, setStreaming] = useState(false);

    const sendMessage = async () => {
      if (!input.trim()) return;

      const userMessage = { role: 'user', content: input };
      const updatedMessages = [...messages, userMessage];
      setMessages(updatedMessages);
      setInput('');
      setStreaming(true);

      try {
        const response = await fetch('/api/chat', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            messages: updatedMessages,
            model: 'anthropic/claude-sonnet-4-5',
          }),
        });

        const reader = response.body?.getReader();
        const decoder = new TextDecoder();
        let assistantMessage = '';

        if (reader) {
          while (true) {
            const { done, value } = await reader.read();
            if (done) break;

            const chunk = decoder.decode(value);
            const lines = chunk.split('\n');

            for (const line of lines) {
              if (line.startsWith('data: ')) {
                const data = line.slice(6);
                if (data === '[DONE]') continue;

                try {
                  const parsed = JSON.parse(data);
                  assistantMessage += parsed.content;
                  setMessages([
                    ...updatedMessages,
                    { role: 'assistant', content: assistantMessage },
                  ]);
                } catch (e) {
                  // Ignore parse errors
                }
              }
            }
          }
        }
      } catch (error) {
        console.error('Error:', error);
      } finally {
        setStreaming(false);
      }
    };

    return (
      <div>
        <div className="messages">
          {messages.map((msg, i) => (
            <div key={i} className={msg.role}>
              <strong>{msg.role}:</strong> {msg.content}
            </div>
          ))}
        </div>
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
          disabled={streaming}
        />
        <button onClick={sendMessage} disabled={streaming}>
          {streaming ? 'Sending...' : 'Send'}
        </button>
      </div>
    );
  }
  ```
</CodeGroup>

## Environment Variables

Use `.env` files for configuration:

<CodeGroup>
  ```bash .env theme={null}
  EDEN_AI_API_KEY=your_api_key_here
  ```

  ```typescript TypeScript theme={null}
  import 'dotenv/config';
  import OpenAI from 'openai';

  const client = new OpenAI({
    apiKey: process.env.EDEN_AI_API_KEY!,
    baseURL: 'https://api.edenai.run/v3/llm',
  });
  ```
</CodeGroup>

## Complete Chat CLI Example

Build a command-line chat interface:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import OpenAI from 'openai';
  import readline from 'readline';
  import type { ChatCompletionMessageParam } from 'openai/resources/chat/completions';

  const client = new OpenAI({
    apiKey: process.env.EDEN_AI_API_KEY!,
    baseURL: 'https://api.edenai.run/v3/llm',
  });

  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  async function main() {
    const messages: ChatCompletionMessageParam[] = [
      { role: 'system', content: 'You are a helpful assistant.' },
    ];

    console.log('Chat with AI (type "quit" to exit)');
    console.log('-'.repeat(50));

    const askQuestion = () => {
      rl.question('\nYou: ', async (input) => {
        const userInput = input.trim();

        if (userInput.toLowerCase() === 'quit') {
          rl.close();
          return;
        }

        if (!userInput) {
          askQuestion();
          return;
        }

        messages.push({ role: 'user', content: userInput });

        process.stdout.write('\nAssistant: ');

        try {
          const stream = await client.chat.completions.create({
            model: 'anthropic/claude-sonnet-4-5',
            messages,
            temperature: 0.7,
            stream: true,
          });

          let assistantResponse = '';

          for await (const chunk of stream) {
            const content = chunk.choices[0]?.delta?.content;
            if (content) {
              process.stdout.write(content);
              assistantResponse += content;
            }
          }

          console.log(); // New line
          messages.push({ role: 'assistant', content: assistantResponse });
        } catch (error) {
          console.error('\nError:', error);
        }

        askQuestion();
      });
    };

    askQuestion();
  }

  main();
  ```
</CodeGroup>

## List Available Models

Programmatically discover models:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import fetch from 'node-fetch';

  async function listModels() {
    const response = await fetch('https://api.edenai.run/v3/llm/models', {
      headers: {
        Authorization: `Bearer ${process.env.EDEN_AI_API_KEY}`,
      },
    });

    const data = await response.json();

    // Group by provider
    const providers: Record<string, string[]> = {};

    for (const model of data.data) {
      const provider = model.owned_by;
      if (!providers[provider]) {
        providers[provider] = [];
      }
      providers[provider].push(model.id);
    }

    console.log('Available Models:\n');
    for (const [provider, models] of Object.entries(providers)) {
      console.log(`${provider}:`);
      models.forEach(m => console.log(`  - ${m}`));
      console.log();
    }
  }

  listModels();
  ```
</CodeGroup>

## Next Steps

* [Vision Capabilities](../../how-to/llm/vision-capabilities) - Working with images
* [Streaming Responses](../../how-to/llm/streaming) - Handle Server-Sent Events


# Multi environment tokens
Source: https://docs.edenai.co/v3/tutorials/multi-environment-tokens



# Multi-Environment Token Management

Build a complete token management system to organize API keys across development, staging, and production environments with automated rotation and usage tracking.

## What You'll Build

By the end of this tutorial, you'll have:

* **Environment-Specific Tokens** - Separate tokens for dev, staging, and production
* **Automated Token Rotation** - Scripts to rotate tokens on a schedule
* **Usage Monitoring** - Track spending per environment
* **Budget Controls** - Different credit limits per environment
* **Expiration Alerts** - Notifications before tokens expire

## Prerequisites

* Python 3.8 or higher
* Eden AI API key
* Basic understanding of REST APIs and environment management

## Problem Statement

As your Eden AI integration grows across environments, you need to:

1. **Separate concerns** - Different tokens for different environments
2. **Control costs** - Budget limits per environment
3. **Enhance security** - Rotate tokens without downtime
4. **Track usage** - Monitor which environment is spending what
5. **Prevent outages** - Alert before tokens expire or run out of credits

This tutorial shows you how to build a Python-based token management system.

## Architecture Overview

```
┌──────────────────────────────────────────────────────────┐
│               Token Management System                     │
│                                                           │
│  ┌─────────────┐   ┌──────────────┐   ┌──────────────┐ │
│  │  Token      │──▶│   Rotation   │──▶│   Monitor    │ │
│  │  Registry   │   │   Manager    │   │   & Alerts   │ │
│  └─────────────┘   └──────────────┘   └──────────────┘ │
│        │                   │                   │         │
└────────┼───────────────────┼───────────────────┼─────────┘
         │                   │                   │
         ▼                   ▼                   ▼
    ┌────────────────────────────────────────────────┐
    │           Eden AI Token API                    │
    └────────────────────────────────────────────────┘
```

## Step 1: Create Environment-Specific Tokens

Create a token manager that organizes tokens by environment:

<CodeGroup>
  ```python token_manager.py theme={null}
  import requests
  from datetime import datetime, timedelta
  from typing import Dict, List, Optional
  import json

  class TokenManager:
      """Manage Eden AI custom tokens across environments"""

      BASE_URL = "https://api.edenai.run/v2/user/custom_token"

      def __init__(self, api_key: str):
          """
          Initialize token manager.

          Args:
              api_key: Your main Eden AI API key
          """
          self.api_key = api_key
          self.headers = {"Authorization": f"Bearer {api_key}"}

      def create_environment_token(
          self,
          environment: str,
          app_name: str,
          token_type: str = "api_token",
          balance: Optional[float] = None,
          expire_days: Optional[int] = None
      ) -> Dict:
          """
          Create a new environment-specific token.

          Args:
              environment: Environment name (dev, staging, prod)
              app_name: Application identifier
              token_type: 'api_token' or 'sandbox_api_token'
              balance: Optional credit limit
              expire_days: Optional expiration in days

          Returns:
              Created token data
          """
          token_name = f"{environment}-{app_name}"

          data = {
              "name": token_name,
              "token_type": token_type
          }

          if balance is not None:
              data["balance"] = str(balance)
              data["active_balance"] = True

          if expire_days:
              expiry = datetime.now() + timedelta(days=expire_days)
              data["expire_time"] = expiry.isoformat()

          response = requests.post(
              f"{self.BASE_URL}/",
              headers={**self.headers, "Content-Type": "application/json"},
              json=data
          )
          response.raise_for_status()

          return response.json()

      def list_tokens(self) -> List[Dict]:
          """List all custom tokens"""
          response = requests.get(f"{self.BASE_URL}/", headers=self.headers)
          response.raise_for_status()
          return response.json()

      def get_token(self, name: str) -> Dict:
          """Get specific token by name"""
          response = requests.get(
              f"{self.BASE_URL}/{name}/",
              headers=self.headers
          )
          response.raise_for_status()
          return response.json()

      def update_token(
          self,
          name: str,
          balance: Optional[float] = None,
          expire_time: Optional[str] = None,
          active_balance: Optional[bool] = None
      ) -> Dict:
          """Update token settings"""
          data = {}

          if balance is not None:
              data["balance"] = balance
          if expire_time is not None:
              data["expire_time"] = expire_time
          if active_balance is not None:
              data["active_balance"] = active_balance

          response = requests.patch(
              f"{self.BASE_URL}/{name}/",
              headers={**self.headers, "Content-Type": "application/json"},
              json=data
          )
          response.raise_for_status()
          return response.json()

      def delete_token(self, name: str):
          """Delete a token"""
          response = requests.delete(
              f"{self.BASE_URL}/{name}/",
              headers=self.headers
          )
          response.raise_for_status()

      def get_tokens_by_environment(self) -> Dict[str, List[Dict]]:
          """
          Group tokens by environment.

          Returns:
              Dictionary mapping environment to list of tokens
          """
          tokens = self.list_tokens()
          grouped = {}

          for token in tokens:
              # Extract environment from name (assumes format: env-app)
              parts = token['name'].split('-', 1)
              if len(parts) >= 2:
                  env = parts[0]
                  if env not in grouped:
                      grouped[env] = []
                  grouped[env].append(token)
              else:
                  # Ungrouped tokens
                  if 'other' not in grouped:
                      grouped['other'] = []
                  grouped['other'].append(token)

          return grouped
  ```
</CodeGroup>

## Step 2: Implement Token Rotation Script

Create a rotation system to periodically update tokens:

<CodeGroup>
  ```python token_rotation.py theme={null}
  from token_manager import TokenManager
  from datetime import datetime, timedelta
  from typing import Dict
  import time

  class TokenRotationManager:
      """Handle automated token rotation"""

      def __init__(self, manager: TokenManager):
          self.manager = manager

      def rotate_token(
          self,
          old_token_name: str,
          rotation_suffix: Optional[str] = None
      ) -> Dict:
          """
          Rotate a token by creating a new one with same settings.

          Args:
              old_token_name: Name of token to rotate
              rotation_suffix: Optional suffix for new token name
                              (defaults to timestamp)

          Returns:
              New token data with migration info
          """
          # Get old token details
          old_token = self.manager.get_token(old_token_name)

          # Generate new token name
          if rotation_suffix is None:
              rotation_suffix = datetime.now().strftime("%Y%m%d")

          new_name = f"{old_token_name}-{rotation_suffix}"

          # Create new token with same settings
          new_data = {
              "name": new_name,
              "token_type": old_token['token_type'],
              "active_balance": old_token.get('active_balance', False)
          }

          if old_token.get('balance'):
              new_data["balance"] = str(old_token['balance'])

          response = self.manager.create_environment_token(
              environment=old_token_name.split('-')[0],
              app_name='-'.join(old_token_name.split('-')[1:] + [rotation_suffix]),
              token_type=old_token['token_type'],
              balance=old_token.get('balance') if old_token.get('active_balance') else None
          )

          return {
              'old_token': old_token,
              'new_token': response,
              'migration_steps': [
                  f"1. Update your {old_token_name.split('-')[0]} environment",
                  f"2. Change API key from {old_token['token'][:15]}... to {response['token'][:15]}...",
                  "3. Test the new token",
                  f"4. Delete old token: '{old_token_name}'"
              ]
          }

      def schedule_rotation(
          self,
          token_name: str,
          days_before_expiry: int = 7
      ):
          """
          Check if token needs rotation based on expiry.

          Args:
              token_name: Token to check
              days_before_expiry: Days before expiry to trigger rotation

          Returns:
              True if rotation needed
          """
          token = self.manager.get_token(token_name)

          if not token.get('expire_time'):
              return False  # No expiry set

          expiry = datetime.fromisoformat(
              token['expire_time'].replace('Z', '+00:00')
          )
          days_left = (expiry - datetime.now()).days

          return days_left <= days_before_expiry

      def rotate_all_expiring(self, days_threshold: int = 7) -> List[Dict]:
          """
          Rotate all tokens expiring within threshold.

          Args:
              days_threshold: Days before expiry to rotate

          Returns:
              List of rotation results
          """
          tokens = self.manager.list_tokens()
          rotations = []

          for token in tokens:
              if not token.get('expire_time'):
                  continue

              expiry = datetime.fromisoformat(
                  token['expire_time'].replace('Z', '+00:00')
              )
              days_left = (expiry - datetime.now()).days

              if days_left <= days_threshold:
                  print(f"Rotating {token['name']} (expires in {days_left} days)")
                  result = self.rotate_token(token['name'])
                  rotations.append(result)

          return rotations
  ```
</CodeGroup>

## Step 3: Build Token Lifecycle Manager

Manage the complete lifecycle of environment tokens:

<CodeGroup>
  ```python token_lifecycle.py theme={null}
  from token_manager import TokenManager
  from typing import Dict, List

  class TokenLifecycleManager:
      """Manage complete token lifecycle"""

      def __init__(self, manager: TokenManager):
          self.manager = manager

      def setup_environment(
          self,
          environment: str,
          config: Dict
      ) -> List[Dict]:
          """
          Set up all tokens for an environment.

          Args:
              environment: Environment name
              config: Configuration dict with token specs

          Returns:
              List of created tokens
          """
          tokens = []

          for app_name, spec in config.items():
              token = self.manager.create_environment_token(
                  environment=environment,
                  app_name=app_name,
                  token_type=spec.get('type', 'api_token'),
                  balance=spec.get('balance'),
                  expire_days=spec.get('expire_days')
              )
              tokens.append(token)
              print(f"✓ Created {environment}-{app_name}")

          return tokens

      def teardown_environment(self, environment: str):
          """Delete all tokens for an environment"""
          grouped = self.manager.get_tokens_by_environment()

          if environment not in grouped:
              print(f"No tokens found for environment: {environment}")
              return

          for token in grouped[environment]:
              self.manager.delete_token(token['name'])
              print(f"✓ Deleted {token['name']}")

      def refresh_environment_budgets(
          self,
          environment: str,
          new_balance: float
      ):
          """Reset all token balances for an environment"""
          grouped = self.manager.get_tokens_by_environment()

          if environment not in grouped:
              print(f"No tokens found for environment: {environment}")
              return

          for token in grouped[environment]:
              if token.get('active_balance'):
                  self.manager.update_token(
                      token['name'],
                      balance=new_balance,
                      active_balance=True
                  )
                  print(f"✓ Updated {token['name']} balance to ${new_balance}")
  ```
</CodeGroup>

## Step 4: Add Usage Monitoring Per Token

Integrate with cost monitoring to track per-token usage:

<CodeGroup>
  ```python token_monitor.py theme={null}
  import requests
  from token_manager import TokenManager
  from typing import Dict, List

  class TokenUsageMonitor:
      """Monitor usage and costs per token"""

      def __init__(self, manager: TokenManager):
          self.manager = manager
          self.cost_api_url = "https://api.edenai.run/v2/cost_management/"

      def get_token_usage(
          self,
          token_name: str,
          begin: str,
          end: str
      ) -> Dict:
          """
          Get usage data for a specific token.

          Args:
              token_name: Token name to query
              begin: Start date (YYYY-MM-DD)
              end: End date (YYYY-MM-DD)

          Returns:
              Usage statistics
          """
          params = {
              "begin": begin,
              "end": end,
              "step": 1,
              "token": token_name
          }

          response = requests.get(
              self.cost_api_url,
              headers=self.manager.headers,
              params=params
          )
          response.raise_for_status()

          data = response.json()

          # Calculate totals
          total_cost = 0.0
          total_calls = 0

          for token_data in data['response']:
              for date, features in token_data['data'].items():
                  for feature, details in features.items():
                      total_cost += details['total_cost']
                      total_calls += details['details']

          return {
              'token_name': token_name,
              'period': f"{begin} to {end}",
              'total_cost': total_cost,
              'total_calls': total_calls,
              'avg_cost_per_call': total_cost / total_calls if total_calls > 0 else 0
          }

      def compare_environments(
          self,
          begin: str,
          end: str
      ) -> Dict[str, Dict]:
          """
          Compare usage across all environments.

          Returns:
              Dict mapping environment to usage stats
          """
          grouped = self.manager.get_tokens_by_environment()
          env_stats = {}

          for env, tokens in grouped.items():
              env_cost = 0.0
              env_calls = 0

              for token in tokens:
                  usage = self.get_token_usage(token['name'], begin, end)
                  env_cost += usage['total_cost']
                  env_calls += usage['total_calls']

              env_stats[env] = {
                  'total_cost': env_cost,
                  'total_calls': env_calls,
                  'num_tokens': len(tokens)
              }

          return env_stats

      def print_usage_report(self, begin: str, end: str):
          """Print formatted usage report"""
          stats = self.compare_environments(begin, end)

          print("=" * 60)
          print(f"Token Usage Report: {begin} to {end}")
          print("=" * 60)
          print()

          for env, data in sorted(stats.items()):
              print(f"Environment: {env.upper()}")
              print(f"  Tokens: {data['num_tokens']}")
              print(f"  Total Cost: ${data['total_cost']:.2f}")
              print(f"  Total Calls: {data['total_calls']:,}")
              if data['total_calls'] > 0:
                  avg = data['total_cost'] / data['total_calls']
                  print(f"  Avg Cost/Call: ${avg:.4f}")
              print()

          total_cost = sum(d['total_cost'] for d in stats.values())
          print(f"TOTAL COST (ALL ENVIRONMENTS): ${total_cost:.2f}")
          print("=" * 60)
  ```
</CodeGroup>

## Step 5: Implement Automated Alerts for Token Expiry

Create an alert system for token health:

<CodeGroup>
  ```python token_alerts.py theme={null}
  from token_manager import TokenManager
  from datetime import datetime
  from typing import List, Dict

  class TokenAlertSystem:
      """Monitor tokens and send alerts"""

      def __init__(self, manager: TokenManager):
          self.manager = manager

      def check_expiring_tokens(
          self,
          days_threshold: int = 7
      ) -> List[Dict]:
          """
          Find tokens expiring soon.

          Args:
              days_threshold: Alert if expiring within this many days

          Returns:
              List of expiring tokens with details
          """
          tokens = self.manager.list_tokens()
          expiring = []

          for token in tokens:
              if not token.get('expire_time'):
                  continue

              expiry = datetime.fromisoformat(
                  token['expire_time'].replace('Z', '+00:00')
              )
              days_left = (expiry - datetime.now()).days

              if 0 <= days_left <= days_threshold:
                  expiring.append({
                      'name': token['name'],
                      'expires': token['expire_time'],
                      'days_left': days_left,
                      'severity': 'critical' if days_left < 2 else 'warning'
                  })

          return expiring

      def check_low_balance_tokens(
          self,
          threshold_percentage: float = 0.2
      ) -> List[Dict]:
          """
          Find tokens with low credit balance.

          Args:
              threshold_percentage: Alert if below this % of original balance

          Returns:
              List of low-balance tokens
          """
          tokens = self.manager.list_tokens()
          low_balance = []

          for token in tokens:
              if not token.get('active_balance'):
                  continue

              balance = token.get('balance', 0)

              # Alert if balance is low (assuming original was higher)
              if balance < 10:  # Less than $10
                  low_balance.append({
                      'name': token['name'],
                      'balance': balance,
                      'severity': 'critical' if balance < 1 else 'warning'
                  })

          return low_balance

      def print_health_report(self):
          """Print comprehensive token health report"""
          print("=" * 60)
          print("Token Health Report")
          print("=" * 60)
          print()

          # Check expiring tokens
          expiring = self.check_expiring_tokens(days_threshold=14)

          if expiring:
              print("⚠️  EXPIRING TOKENS:")
              print("-" * 60)
              for token in expiring:
                  icon = "🔴" if token['severity'] == 'critical' else "🟡"
                  print(f"{icon} {token['name']}")
                  print(f"   Expires in {token['days_left']} days")
              print()
          else:
              print("✓ No tokens expiring soon")
              print()

          # Check low balance
          low_balance = self.check_low_balance_tokens()

          if low_balance:
              print("⚠️  LOW BALANCE TOKENS:")
              print("-" * 60)
              for token in low_balance:
                  icon = "🔴" if token['severity'] == 'critical' else "🟡"
                  print(f"{icon} {token['name']}")
                  print(f"   Balance: ${token['balance']:.2f}")
              print()
          else:
              print("✓ All token balances adequate")
              print()

          print("=" * 60)
  ```
</CodeGroup>

## Step 6: Put It All Together

Create a complete management system:

<CodeGroup>
  ```python main.py theme={null}
  #!/usr/bin/env python3
  """
  Multi-Environment Token Management System
  """

  import os
  from datetime import datetime, timedelta
  from token_manager import TokenManager
  from token_lifecycle import TokenLifecycleManager
  from token_rotation import TokenRotationManager
  from token_monitor import TokenUsageMonitor
  from token_alerts import TokenAlertSystem

  def main():
      # Configuration
      API_KEY = os.getenv("EDENAI_API_KEY")

      if not API_KEY:
          print("Error: EDENAI_API_KEY environment variable not set")
          return

      # Initialize managers
      manager = TokenManager(API_KEY)
      lifecycle = TokenLifecycleManager(manager)
      rotation = TokenRotationManager(manager)
      monitor = TokenUsageMonitor(manager)
      alerts = TokenAlertSystem(manager)

      print("\n🔐 Multi-Environment Token Management System\n")

      # 1. Check token health
      print("📊 Token Health Check")
      alerts.print_health_report()
      print()

      # 2. Show tokens by environment
      print("🗂️  Tokens by Environment")
      grouped = manager.get_tokens_by_environment()
      for env, tokens in grouped.items():
          print(f"\n{env.upper()}:")
          for token in tokens:
              status = "✓"
              if token.get('active_balance') and token.get('balance', 0) < 10:
                  status = "⚠️"

              print(f"  {status} {token['name']}")
              if token.get('active_balance'):
                  print(f"     Balance: ${token.get('balance', 0):.2f}")
              if token.get('expire_time'):
                  expiry = datetime.fromisoformat(
                      token['expire_time'].replace('Z', '+00:00')
                  )
                  days_left = (expiry - datetime.now()).days
                  print(f"     Expires in: {days_left} days")

      print()

      # 3. Usage report
      print("💰 Usage Report (Last 30 Days)")
      end = datetime.now().strftime("%Y-%m-%d")
      begin = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
      monitor.print_usage_report(begin, end)
      print()

      # 4. Check for needed rotations
      print("🔄 Rotation Status")
      expiring_count = len(alerts.check_expiring_tokens(days_threshold=7))
      if expiring_count > 0:
          print(f"⚠️  {expiring_count} token(s) need rotation")
      else:
          print("✓ No rotations needed")
      print()

  if __name__ == "__main__":
      main()
  ```
</CodeGroup>

## Example: Setting Up Multi-Environment System

Complete example setting up dev, staging, and production:

<CodeGroup>
  ```python setup_environments.py theme={null}
  #!/usr/bin/env python3
  import os
  from token_manager import TokenManager
  from token_lifecycle import TokenLifecycleManager

  def setup_complete_system():
      """Set up tokens for all environments"""
      API_KEY = os.getenv("EDENAI_API_KEY")
      manager = TokenManager(API_KEY)
      lifecycle = TokenLifecycleManager(manager)

      # Development environment - sandbox tokens, no limits
      dev_config = {
          "web-app": {
              "type": "sandbox_api_token"
          },
          "mobile-app": {
              "type": "sandbox_api_token"
          },
          "testing": {
              "type": "sandbox_api_token"
          }
      }

      # Staging environment - real tokens, moderate limits
      staging_config = {
          "web-app": {
              "type": "api_token",
              "balance": 50.0,
              "expire_days": 90
          },
          "mobile-app": {
              "type": "api_token",
              "balance": 50.0,
              "expire_days": 90
          }
      }

      # Production environment - real tokens, high limits
      prod_config = {
          "web-app": {
              "type": "api_token",
              "balance": 500.0,
              "expire_days": 90
          },
          "mobile-app": {
              "type": "api_token",
              "balance": 500.0,
              "expire_days": 90
          },
          "api-gateway": {
              "type": "api_token",
              "balance": 1000.0,
              "expire_days": 90
          }
      }

      # Set up all environments
      print("Setting up Development environment...")
      lifecycle.setup_environment("dev", dev_config)

      print("\nSetting up Staging environment...")
      lifecycle.setup_environment("staging", staging_config)

      print("\nSetting up Production environment...")
      lifecycle.setup_environment("prod", prod_config)

      print("\n✅ All environments set up successfully!")

  if __name__ == "__main__":
      setup_complete_system()
  ```
</CodeGroup>

## Testing

Test your token management system:

```bash theme={null}
# Set up environments
export EDENAI_API_KEY="your_main_api_key"
python setup_environments.py

# Run health check
python main.py

# Rotate a specific token
python -c "
from token_manager import TokenManager
from token_rotation import TokenRotationManager
import os

manager = TokenManager(os.getenv('EDENAI_API_KEY'))
rotation = TokenRotationManager(manager)

result = rotation.rotate_token('prod-web-app')
print(result['migration_steps'])
"
```

## Production Considerations

### Automated Rotation Schedule

Use cron for automated token rotation:

```bash theme={null}
# Rotate tokens expiring in 7 days, every day at 2 AM
0 2 * * * /usr/bin/python3 /path/to/rotate_expiring.py >> /var/log/token_rotation.log 2>&1
```

### Secure Token Storage

Store generated tokens securely:

```python theme={null}
import boto3
import json

def store_token_in_secrets_manager(token_name: str, token_value: str):
    """Store token in AWS Secrets Manager"""
    client = boto3.client('secretsmanager')

    secret_name = f"edenai/{token_name}"

    try:
        client.create_secret(
            Name=secret_name,
            SecretString=json.dumps({
                'token': token_value,
                'created_at': datetime.now().isoformat()
            })
        )
    except client.exceptions.ResourceExistsException:
        client.update_secret(
            SecretId=secret_name,
            SecretString=json.dumps({
                'token': token_value,
                'updated_at': datetime.now().isoformat()
            })
        )
```

### Monitoring Integration

Integrate with monitoring systems:

```python theme={null}
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def monitor_token_health():
    """Log token health to monitoring system"""
    alerts = TokenAlertSystem(manager)

    expiring = alerts.check_expiring_tokens()
    low_balance = alerts.check_low_balance_tokens()

    if expiring:
        logger.warning(f"{len(expiring)} tokens expiring soon")
        # Send to monitoring system (Datadog, New Relic, etc.)

    if low_balance:
        logger.warning(f"{len(low_balance)} tokens with low balance")
        # Send alert
```

## Next Steps

Now that you have a complete multi-environment token management system:

* [Manage Custom Tokens Guide](../how-to/user-management/manage-tokens) - API reference
* [Monitor Usage and Costs](../how-to/cost-management/monitor-usage) - Track per-token spending

## Complete Example Output

When you run `main.py`:

```
🔐 Multi-Environment Token Management System

📊 Token Health Check
============================================================
Token Health Report
============================================================

⚠️  EXPIRING TOKENS:
------------------------------------------------------------
🟡 staging-web-app
   Expires in 12 days
🟡 staging-mobile-app
   Expires in 12 days

✓ All token balances adequate

============================================================

🗂️  Tokens by Environment

DEV:
  ✓ dev-web-app
  ✓ dev-mobile-app
  ✓ dev-testing

STAGING:
  ⚠️ staging-web-app
     Balance: $8.45
     Expires in: 12 days
  ✓ staging-mobile-app
     Balance: $42.10
     Expires in: 12 days

PROD:
  ✓ prod-web-app
     Balance: $478.90
     Expires in: 85 days
  ✓ prod-mobile-app
     Balance: $456.23
     Expires in: 85 days
  ✓ prod-api-gateway
     Balance: $892.34
     Expires in: 85 days

💰 Usage Report (Last 30 Days)
============================================================
Token Usage Report: 2024-01-01 to 2024-01-31
============================================================

Environment: DEV
  Tokens: 3
  Total Cost: $0.00
  Total Calls: 1,234
  Avg Cost/Call: $0.0000

Environment: STAGING
  Tokens: 2
  Total Cost: $3.89
  Total Calls: 456
  Avg Cost/Call: $0.0085

Environment: PROD
  Tokens: 3
  Total Cost: $127.11
  Total Calls: 8,921
  Avg Cost/Call: $0.0142

TOTAL COST (ALL ENVIRONMENTS): $131.00
============================================================

🔄 Rotation Status
⚠️  2 token(s) need rotation
```


# Optimize llm costs
Source: https://docs.edenai.co/v3/tutorials/optimize-llm-costs



# Optimize LLM Costs with Smart Routing

Build a cost-effective chatbot application using Eden AI's smart routing to automatically select the best model for each query while minimizing expenses.

## What You'll Build

By the end of this tutorial, you'll have:

* **Smart routing-powered chatbot** - Automatically selects optimal models
* **Multi-tier routing strategy** - Budget/balanced/premium tiers for different use cases
* **Cost tracking system** - Monitor spending per conversation and query type
* **A/B testing framework** - Compare smart routing vs. fixed models
* **Performance metrics** - Track latency, quality, and cost trade-offs

## Prerequisites

* Python 3.8 or higher
* Eden AI API key ([Get one here](https://app.edenai.run/))
* Basic understanding of LLMs and REST APIs
* Optional: Database for persistent storage (SQLite/PostgreSQL)

## Problem Statement

You're building a customer support chatbot with diverse query types:

* **Simple FAQs** - "What are your hours?" (low complexity)
* **Technical support** - "How do I configure SSL?" (medium complexity)
* **Complex troubleshooting** - "Server crashes with error X" (high complexity)

**Challenges:**

1. **Fixed models are inefficient** - Using GPT-4o for all queries wastes money on simple FAQs
2. **Manual model selection is hard** - Predicting which model fits each query is complex
3. **Quality vs. cost trade-off** - Balancing response quality with budget constraints

**Solution:** Smart routing automatically selects the right model for each query, optimizing costs without sacrificing quality.

## Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│               Customer Support Chatbot                   │
│                                                          │
│  ┌────────────┐   ┌──────────────┐   ┌──────────────┐  │
│  │  Query     │──▶│  Routing     │──▶│  Response    │  │
│  │  Analyzer  │   │  Engine      │   │  Generator   │  │
│  └────────────┘   └──────────────┘   └──────────────┘  │
│                           │                              │
│                           ▼                              │
│                  ┌─────────────────┐                     │
│                  │  Cost Tracker   │                     │
│                  └─────────────────┘                     │
└─────────────────────────────────────────────────────────┘
                           │
                           ▼
              ┌────────────────────────┐
              │  Eden AI Smart Router  │
              │  (@edenai routing)     │
              └────────────────────────┘
```

## Step 1: Baseline Implementation (Fixed Model)

First, let's build a simple chatbot using a single fixed model to establish a baseline:

<CodeGroup>
  ```python baseline_chatbot.py theme={null}
  import requests
  import json
  from datetime import datetime
  from typing import List, Dict

  class BaselineChatbot:
      """Simple chatbot with fixed model (baseline for comparison)."""

      def __init__(self, api_key: str, model: str = "openai/gpt-4o"):
          self.api_key = api_key
          self.model = model
          self.conversation_history = []
          self.cost_log = []

      def chat(self, message: str) -> Dict:
          """Send a message and get response."""

          self.conversation_history.append({
              "role": "user",
              "content": message
          })

          url = "https://api.edenai.run/v3/llm/chat/completions"
          headers = {
              "Authorization": f"Bearer {self.api_key}",
              "Content-Type": "application/json"
          }

          payload = {
              "model": self.model,
              "messages": self.conversation_history
          }

          start_time = datetime.now()
          response = requests.post(url, headers=headers, json=payload)
          response_data = response.json()

          full_response = response_data.get('choices', [{}])[0].get('message', {}).get('content', '')

          end_time = datetime.now()
          latency = (end_time - start_time).total_seconds()

          # Add to conversation history
          self.conversation_history.append({
              "role": "assistant",
              "content": full_response
          })

          # Log cost (approximate - you'd get this from response metadata)
          estimated_cost = self._estimate_cost(message, full_response)
          self.cost_log.append({
              "timestamp": start_time.isoformat(),
              "model": self.model,
              "input_tokens": len(message.split()) * 1.3,  # Rough estimate
              "output_tokens": len(full_response.split()) * 1.3,
              "cost": estimated_cost,
              "latency": latency
          })

          return {
              "response": full_response,
              "model": self.model,
              "latency": latency,
              "estimated_cost": estimated_cost
          }

      def _estimate_cost(self, input_text: str, output_text: str) -> float:
          """Estimate cost based on token counts (simplified)."""
          # Rough token estimation: ~1.3 tokens per word
          input_tokens = len(input_text.split()) * 1.3
          output_tokens = len(output_text.split()) * 1.3

          # GPT-4o pricing (example)
          COST_PER_1K_INPUT = 0.0025
          COST_PER_1K_OUTPUT = 0.01

          cost = (input_tokens / 1000 * COST_PER_1K_INPUT +
                  output_tokens / 1000 * COST_PER_1K_OUTPUT)
          return cost

      def get_total_cost(self) -> float:
          """Get total conversation cost."""
          return sum(log["cost"] for log in self.cost_log)

      def get_stats(self) -> Dict:
          """Get conversation statistics."""
          total_queries = len(self.cost_log)
          if total_queries == 0:
              return {"error": "No queries yet"}

          return {
              "total_queries": total_queries,
              "total_cost": self.get_total_cost(),
              "avg_cost_per_query": self.get_total_cost() / total_queries,
              "avg_latency": sum(log["latency"] for log in self.cost_log) / total_queries,
              "model_used": self.model
          }


  # Test baseline chatbot
  if __name__ == "__main__":
      chatbot = BaselineChatbot(api_key="YOUR_API_KEY")

      # Test queries
      queries = [
          "What are your business hours?",
          "How do I reset my password?",
          "My server is returning 500 errors after upgrading to version 2.0. The logs show 'Connection timeout' but only for API endpoints, not static content.",
      ]

      print("=== Baseline Chatbot (Fixed Model: GPT-4o) ===\n")

      for query in queries:
          print(f"User: {query}")
          result = chatbot.chat(query)
          print(f"Assistant: {result['response'][:100]}...")
          print(f"Cost: ${result['estimated_cost']:.4f} | Latency: {result['latency']:.2f}s\n")

      # Print stats
      stats = chatbot.get_stats()
      print("\n=== Baseline Statistics ===")
      print(f"Total queries: {stats['total_queries']}")
      print(f"Total cost: ${stats['total_cost']:.4f}")
      print(f"Avg cost per query: ${stats['avg_cost_per_query']:.4f}")
  ```
</CodeGroup>

**Expected Output:**

```
User: What are your business hours?
Assistant: Our business hours are Monday through Friday, 9 AM to 5 PM EST...
Cost: $0.0015 | Latency: 1.2s

Total cost: $0.0123
Avg cost per query: $0.0041
```

**Problem:** Simple queries like "What are your business hours?" cost the same as complex troubleshooting questions, wasting money.

## Step 2: Add Smart Routing

Now let's migrate to smart routing with default model selection:

<CodeGroup>
  ```python smart_routing_chatbot.py theme={null}
  import requests
  import json
  from datetime import datetime
  from typing import List, Dict, Optional

  class SmartRoutingChatbot:
      """Chatbot with smart routing for automatic model selection."""

      def __init__(self, api_key: str, router_candidates: Optional[List[str]] = None):
          self.api_key = api_key
          self.router_candidates = router_candidates
          self.conversation_history = []
          self.cost_log = []

      def chat(self, message: str) -> Dict:
          """Send a message with smart routing."""

          self.conversation_history.append({
              "role": "user",
              "content": message
          })

          url = "https://api.edenai.run/v3/llm/chat/completions"
          headers = {
              "Authorization": f"Bearer {self.api_key}",
              "Content-Type": "application/json"
          }

          payload = {
              "model": "@edenai",  # Smart routing trigger
              "messages": self.conversation_history
          }

          # Add custom candidates if provided
          if self.router_candidates:
              payload["router_candidates"] = self.router_candidates

          start_time = datetime.now()
          response = requests.post(url, headers=headers, json=payload)
          response_data = response.json()

          full_response = response_data.get('choices', [{}])[0].get('message', {}).get('content', '')
          selected_model = response_data.get('model')

          end_time = datetime.now()
          latency = (end_time - start_time).total_seconds()
          routing_latency = 0  # No streaming, so no first chunk time

          # Add to conversation history
          self.conversation_history.append({
              "role": "assistant",
              "content": full_response
          })

          # Log cost
          estimated_cost = self._estimate_cost(message, full_response, selected_model)
          self.cost_log.append({
              "timestamp": start_time.isoformat(),
              "query": message[:100],
              "model": selected_model,
              "routing_method": "smart",
              "input_tokens": len(message.split()) * 1.3,
              "output_tokens": len(full_response.split()) * 1.3,
              "cost": estimated_cost,
              "latency": latency,
              "routing_latency": routing_latency
          })

          return {
              "response": full_response,
              "model": selected_model,
              "latency": latency,
              "routing_latency": routing_latency,
              "estimated_cost": estimated_cost
          }

      def _estimate_cost(self, input_text: str, output_text: str, model: str) -> float:
          """Estimate cost based on model pricing."""
          input_tokens = len(input_text.split()) * 1.3
          output_tokens = len(output_text.split()) * 1.3

          # Simplified pricing table (per 1K tokens)
          PRICING = {
              "openai/gpt-4o": {"input": 0.0025, "output": 0.01},
              "openai/gpt-4o-mini": {"input": 0.00015, "output": 0.0006},
              "anthropic/claude-sonnet-4-5": {"input": 0.003, "output": 0.015},
              "openai/gpt-4": {"input": 0.0008, "output": 0.004},
              "google/gemini-2.5-flash": {"input": 0.0001, "output": 0.0004},
          }

          pricing = PRICING.get(model, PRICING["openai/gpt-4o"])
          cost = (input_tokens / 1000 * pricing["input"] +
                  output_tokens / 1000 * pricing["output"])
          return cost

      def get_stats(self) -> Dict:
          """Get conversation statistics."""
          if not self.cost_log:
              return {"error": "No queries yet"}

          from collections import defaultdict
          model_counts = defaultdict(int)
          model_costs = defaultdict(float)

          for log in self.cost_log:
              model_counts[log["model"]] += 1
              model_costs[log["model"]] += log["cost"]

          return {
              "total_queries": len(self.cost_log),
              "total_cost": sum(log["cost"] for log in self.cost_log),
              "avg_cost_per_query": sum(log["cost"] for log in self.cost_log) / len(self.cost_log),
              "avg_latency": sum(log["latency"] for log in self.cost_log) / len(self.cost_log),
              "avg_routing_latency": sum(log["routing_latency"] for log in self.cost_log) / len(self.cost_log),
              "model_distribution": dict(model_counts),
              "cost_by_model": dict(model_costs)
          }


  # Test smart routing chatbot
  if __name__ == "__main__":
      # Use custom candidates for cost optimization
      candidates = [
          "openai/gpt-4o",
          "openai/gpt-4o-mini",
          "anthropic/claude-sonnet-4-5",
          "google/gemini-2.5-flash"
      ]

      chatbot = SmartRoutingChatbot(
          api_key="YOUR_API_KEY",
          router_candidates=candidates
      )

      print("=== Smart Routing Chatbot ===\n")

      queries = [
          "What are your business hours?",
          "How do I reset my password?",
          "My server is returning 500 errors after upgrading to version 2.0. The logs show 'Connection timeout' but only for API endpoints.",
      ]

      for query in queries:
          print(f"User: {query}")
          result = chatbot.chat(query)
          print(f"Model: {result['model']}")
          print(f"Assistant: {result['response'][:100]}...")
          print(f"Cost: ${result['estimated_cost']:.4f} | Latency: {result['latency']:.2f}s")
          print(f"Routing overhead: {result['routing_latency']:.2f}s\n")

      # Print stats
      stats = chatbot.get_stats()
      print("\n=== Smart Routing Statistics ===")
      print(f"Total queries: {stats['total_queries']}")
      print(f"Total cost: ${stats['total_cost']:.4f}")
      print(f"Avg cost per query: ${stats['avg_cost_per_query']:.4f}")
      print(f"Model distribution: {stats['model_distribution']}")
      print(f"Cost by model: {stats['cost_by_model']}")
  ```
</CodeGroup>

**Expected Output:**

```
User: What are your business hours?
Model: google/gemini-2.5-flash
Cost: $0.0002 | Latency: 1.4s

User: How do I reset my password?
Model: openai/gpt-4o-mini
Cost: $0.0008 | Latency: 1.5s

User: My server is returning 500 errors...
Model: openai/gpt-4o
Cost: $0.0035 | Latency: 1.8s

Total cost: $0.0045 (vs. $0.0123 baseline = 63% savings!)
Model distribution: {'google/gemini-2.5-flash': 1, 'openai/gpt-4o-mini': 1, 'openai/gpt-4o': 1}
```

**Result:** 60%+ cost savings by routing simple queries to cheaper models!

## Step 3: Implement Multi-Tier Routing Strategy

Create different routing strategies for various use cases:

<CodeGroup>
  ```python tiered_routing_chatbot.py theme={null}
  from typing import Dict, List, Optional
  from enum import Enum

  class CostTier(Enum):
      """Cost optimization tiers."""
      BUDGET = "budget"      # Minimize cost
      BALANCED = "balanced"  # Balance cost and quality
      PREMIUM = "premium"    # Maximize quality

  class TieredRoutingChatbot(SmartRoutingChatbot):
      """Chatbot with cost-tier-based routing strategies."""

      # Define candidate pools for each tier
      TIER_CANDIDATES = {
          CostTier.BUDGET: [
              "openai/gpt-4o-mini",
              "google/gemini-2.5-flash",
              "openai/gpt-4",
          ],
          CostTier.BALANCED: [
              "openai/gpt-4o",
              "anthropic/claude-sonnet-4-5",
              "google/gemini-2.5-flash",
          ],
          CostTier.PREMIUM: [
              "anthropic/claude-opus-4-5",
              "openai/gpt-4o",
              "google/gemini-2.5-pro",
          ]
      }

      def __init__(self, api_key: str, cost_tier: CostTier = CostTier.BALANCED):
          """Initialize with cost tier."""
          candidates = self.TIER_CANDIDATES[cost_tier]
          super().__init__(api_key, router_candidates=candidates)
          self.cost_tier = cost_tier

      @classmethod
      def classify_query_tier(cls, message: str) -> CostTier:
          """
          Classify query into cost tier based on complexity.

          Simple heuristic - you could use ML model for production.
          """
          message_lower = message.lower()
          word_count = len(message.split())

          # Budget tier: Simple, short queries
          if word_count < 10 and any(keyword in message_lower for keyword in [
              "hours", "price", "cost", "when", "where", "what is"
          ]):
              return CostTier.BUDGET

          # Premium tier: Complex, long queries
          if word_count > 30 or any(keyword in message_lower for keyword in [
              "analyze", "comprehensive", "detailed", "troubleshoot", "debug"
          ]):
              return CostTier.PREMIUM

          # Balanced tier: Everything else
          return CostTier.BALANCED

  class AdaptiveChatbot:
      """Chatbot that adapts tier based on query complexity."""

      def __init__(self, api_key: str):
          self.api_key = api_key
          self.chatbots = {
              tier: TieredRoutingChatbot(api_key, tier)
              for tier in CostTier
          }
          self.query_log = []

      def chat(self, message: str, force_tier: Optional[CostTier] = None) -> Dict:
          """Chat with automatic tier selection."""

          # Classify query or use forced tier
          tier = force_tier or TieredRoutingChatbot.classify_query_tier(message)
          chatbot = self.chatbots[tier]

          # Get response
          result = chatbot.chat(message)
          result["cost_tier"] = tier.value

          # Log query
          self.query_log.append({
              "query": message[:100],
              "tier": tier.value,
              "model": result["model"],
              "cost": result["estimated_cost"]
          })

          return result

      def get_aggregated_stats(self) -> Dict:
          """Get stats across all tiers."""
          all_stats = {}
          for tier, chatbot in self.chatbots.items():
              stats = chatbot.get_stats()
              if "error" not in stats:
                  all_stats[tier.value] = stats

          # Calculate totals
          total_cost = sum(
              stats["total_cost"]
              for stats in all_stats.values()
          )
          total_queries = sum(
              stats["total_queries"]
              for stats in all_stats.values()
          )

          return {
              "by_tier": all_stats,
              "total_cost": total_cost,
              "total_queries": total_queries,
              "avg_cost_per_query": total_cost / total_queries if total_queries > 0 else 0
          }


  # Test adaptive chatbot
  if __name__ == "__main__":
      chatbot = AdaptiveChatbot(api_key="YOUR_API_KEY")

      print("=== Adaptive Multi-Tier Chatbot ===\n")

      queries = [
          ("What are your business hours?", None),  # Auto: Budget
          ("How do I reset my password?", None),  # Auto: Balanced
          ("Provide a comprehensive analysis of why my distributed system is experiencing cascading failures", None),  # Auto: Premium
          ("What's 2+2?", CostTier.BUDGET),  # Forced: Budget
      ]

      for query, tier in queries:
          print(f"User: {query}")
          result = chatbot.chat(query, force_tier=tier)
          print(f"Tier: {result['cost_tier']} | Model: {result['model']}")
          print(f"Cost: ${result['estimated_cost']:.4f}\n")

      # Print aggregated stats
      stats = chatbot.get_aggregated_stats()
      print("\n=== Aggregated Statistics ===")
      print(f"Total cost: ${stats['total_cost']:.4f}")
      print(f"Total queries: {stats['total_queries']}")
      print(f"\nBy tier:")
      for tier, tier_stats in stats['by_tier'].items():
          print(f"  {tier}: {tier_stats['total_queries']} queries, ${tier_stats['total_cost']:.4f}")
  ```
</CodeGroup>

## Step 4: Build A/B Testing Framework

Compare smart routing vs. fixed models:

<CodeGroup>
  ```python ab_testing.py theme={null}
  import random
  from typing import Dict, List
  from dataclasses import dataclass
  from datetime import datetime

  @dataclass
  class ABTestResult:
      """Results from A/B test."""
      variant: str
      query: str
      model: str
      cost: float
      latency: float
      quality_score: float  # User rating or automated metric

  class ABTester:
      """A/B test smart routing vs. fixed models."""

      def __init__(self, api_key: str):
          self.api_key = api_key

          # Variant A: Fixed model
          self.variant_a = BaselineChatbot(api_key, model="openai/gpt-4o")

          # Variant B: Smart routing
          self.variant_b = SmartRoutingChatbot(
              api_key,
              router_candidates=[
                  "openai/gpt-4o",
                  "openai/gpt-4o-mini",
                  "google/gemini-2.5-flash"
              ]
          )

          self.results = []

      def run_test(
          self,
          queries: List[str],
          split: float = 0.5
      ) -> Dict:
          """Run A/B test on queries."""

          for query in queries:
              # Random assignment
              variant = "A" if random.random() < split else "B"
              chatbot = self.variant_a if variant == "A" else self.variant_b

              # Get response
              result = chatbot.chat(query)

              # Simulate quality score (in production, get from users or eval model)
              quality_score = random.uniform(0.7, 1.0)

              # Record result
              self.results.append(ABTestResult(
                  variant=variant,
                  query=query,
                  model=result["model"],
                  cost=result["estimated_cost"],
                  latency=result["latency"],
                  quality_score=quality_score
              ))

          return self.analyze_results()

      def analyze_results(self) -> Dict:
          """Analyze A/B test results."""
          if not self.results:
              return {"error": "No test results"}

          # Split by variant
          variant_a = [r for r in self.results if r.variant == "A"]
          variant_b = [r for r in self.results if r.variant == "B"]

          def analyze_variant(results: List[ABTestResult]) -> Dict:
              if not results:
                  return {}
              return {
                  "sample_size": len(results),
                  "avg_cost": sum(r.cost for r in results) / len(results),
                  "total_cost": sum(r.cost for r in results),
                  "avg_latency": sum(r.latency for r in results) / len(results),
                  "avg_quality": sum(r.quality_score for r in results) / len(results),
              }

          a_stats = analyze_variant(variant_a)
          b_stats = analyze_variant(variant_b)

          # Calculate improvements
          cost_savings = ((a_stats["avg_cost"] - b_stats["avg_cost"]) /
                         a_stats["avg_cost"] * 100) if a_stats else 0

          quality_change = ((b_stats["avg_quality"] - a_stats["avg_quality"]) /
                           a_stats["avg_quality"] * 100) if a_stats else 0

          return {
              "variant_a": a_stats,
              "variant_b": b_stats,
              "cost_savings_pct": cost_savings,
              "quality_change_pct": quality_change,
              "recommendation": "B (Smart Routing)" if cost_savings > 10 and quality_change > -5 else "A (Fixed Model)"
          }


  # Run A/B test
  if __name__ == "__main__":
      tester = ABTester(api_key="YOUR_API_KEY")

      queries = [
          "What are your hours?",
          "How do I reset my password?",
          "Explain the difference between OAuth and JWT",
          "My app crashes on startup",
          "What's the pricing?",
          "Help me debug this complex authentication flow",
      ]

      print("=== Running A/B Test ===\n")
      results = tester.run_test(queries)

      print(f"Variant A (Fixed: GPT-4o):")
      print(f"  Sample size: {results['variant_a']['sample_size']}")
      print(f"  Avg cost: ${results['variant_a']['avg_cost']:.4f}")
      print(f"  Avg quality: {results['variant_a']['avg_quality']:.2f}\n")

      print(f"Variant B (Smart Routing):")
      print(f"  Sample size: {results['variant_b']['sample_size']}")
      print(f"  Avg cost: ${results['variant_b']['avg_cost']:.4f}")
      print(f"  Avg quality: {results['variant_b']['avg_quality']:.2f}\n")

      print(f"Cost savings: {results['cost_savings_pct']:.1f}%")
      print(f"Quality change: {results['quality_change_pct']:.1f}%")
      print(f"\nRecommendation: {results['recommendation']}")
  ```
</CodeGroup>

**Expected Results:**

```
Variant A (Fixed: GPT-4o):
  Avg cost: $0.0042
  Avg quality: 0.85

Variant B (Smart Routing):
  Avg cost: $0.0016
  Avg quality: 0.84

Cost savings: 61.9%
Quality change: -1.2%

Recommendation: B (Smart Routing)
```

## Step 5: Production Deployment Best Practices

### Monitoring and Alerting

<CodeGroup>
  ```python production_monitor.py theme={null}
  import logging
  from datetime import datetime
  from typing import Dict, Optional
  import json

  class ProductionMonitor:
      """Production monitoring for smart routing."""

      def __init__(self, api_key: str, alert_threshold_usd: float = 100.0):
          self.api_key = api_key
          self.alert_threshold = alert_threshold_usd
          self.daily_spend = 0.0
          self.error_count = 0
          self.routing_failures = 0

          # Set up logging
          logging.basicConfig(
              level=logging.INFO,
              format='%(asctime)s - %(levelname)s - %(message)s',
              handlers=[
                  logging.FileHandler('chatbot.log'),
                  logging.StreamHandler()
              ]
          )
          self.logger = logging.getLogger(__name__)

      def log_request(
          self,
          query: str,
          model: str,
          cost: float,
          latency: float,
          error: Optional[str] = None
      ):
          """Log request details."""

          self.daily_spend += cost

          log_data = {
              "timestamp": datetime.now().isoformat(),
              "query_preview": query[:50],
              "model": model,
              "cost": cost,
              "latency": latency,
              "daily_spend": self.daily_spend,
              "error": error
          }

          if error:
              self.error_count += 1
              self.logger.error(f"Request failed: {json.dumps(log_data)}")
          else:
              self.logger.info(json.dumps(log_data))

          # Check thresholds
          self._check_alerts()

      def _check_alerts(self):
          """Check if alerts should be triggered."""

          # Cost alert
          if self.daily_spend > self.alert_threshold:
              self.logger.warning(
                  f"Daily spend (${self.daily_spend:.2f}) exceeded threshold (${self.alert_threshold:.2f})"
              )
              # In production: send email/Slack notification

          # Error rate alert
          if self.error_count > 10:
              self.logger.critical(f"High error count: {self.error_count}")
              # In production: page on-call engineer

  # Integrate with chatbot
  class ProductionChatbot(SmartRoutingChatbot):
      """Production-ready chatbot with monitoring."""

      def __init__(self, api_key: str, candidates: List[str]):
          super().__init__(api_key, candidates)
          self.monitor = ProductionMonitor(api_key, alert_threshold_usd=100.0)

      def chat(self, message: str) -> Dict:
          """Chat with monitoring."""
          try:
              result = super().chat(message)

              # Log successful request
              self.monitor.log_request(
                  query=message,
                  model=result["model"],
                  cost=result["estimated_cost"],
                  latency=result["latency"]
              )

              return result

          except Exception as e:
              # Log error
              self.monitor.log_request(
                  query=message,
                  model="unknown",
                  cost=0.0,
                  latency=0.0,
                  error=str(e)
              )
              raise
  ```
</CodeGroup>

## Key Takeaways

### Cost Savings Summary

| Strategy                        | Avg Cost per Query | Savings vs. Baseline |
| ------------------------------- | ------------------ | -------------------- |
| **Baseline (Fixed GPT-4o)**     | \$0.0041           | -                    |
| **Smart Routing (Default)**     | \$0.0018           | 56%                  |
| **Smart Routing (Budget Tier)** | \$0.0008           | 80%                  |
| **Smart Routing (Balanced)**    | \$0.0015           | 63%                  |

### Best Practices

✅ **Start simple** - Begin with default smart routing, then optimize
✅ **Monitor metrics** - Track cost, latency, and quality
✅ **Use tiered strategies** - Different tiers for different use cases
✅ **A/B test** - Validate cost savings don't hurt quality
✅ **Set budgets** - Alert before overspending
✅ **Log routing decisions** - Debug and optimize over time

### When Smart Routing Shines

* **Diverse query types** - Mix of simple and complex queries
* **Cost-sensitive applications** - Budget constraints
* **High volume** - Many requests per day
* **Unpredictable workloads** - Query complexity varies

### When to Use Fixed Models

* **Consistent requirements** - All queries need same model
* **Latency-critical** - Can't afford 100-500ms routing overhead
* **Specific model features** - Need particular model's capabilities
* **Already optimized** - You've manually tuned model selection

## Next Steps

* **[Smart Routing How-To](../how-to/llm/smart-routing)** - Advanced implementation patterns
* **[Chat Completions Guide](../how-to/llm/chat-completions)** - Master the LLM endpoint
* **[Streaming Guide](../how-to/llm/streaming)** - Handle SSE responses

## Additional Resources

* [NotDiamond Routing Engine](https://notdiamond.ai/) - Learn about the routing technology
* [Eden AI Pricing](https://www.edenai.co/pricing) - Compare model costs
* [Production Deployment Guide](../how-to/llm/chat-completions#production) - Scale your chatbot

Try it yourself and see 50%+ cost savings!


