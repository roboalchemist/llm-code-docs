# Source: https://docs.aimlapi.com/integrations/manus.md

# Manus

[Manus](https://manus.im/docs/introduction/welcome) is a workflow and AI-agent orchestration platform that lets users integrate custom APIs, define automation logic, and run LLM-powered tools inside a unified interface. Manus supports custom model backends (such as AI/ML API), prompt templates, request routing, secure secret storage, and visual debugging.

## Installation / Setup

### 1. Prerequisites

* **AI/ML API account** – sign up and create an API key at:
  * Dashboard: <https://aimlapi.com/app/?utm_source=manus&utm_medium=github&utm_campaign=integration>
  * API Keys: <https://aimlapi.com/app/keys/?utm_source=manus&utm_medium=github&utm_campaign=integration>
* **Manus account** – with access to **Settings → Integrations → Add custom API**.

<div align="left" data-with-frame="true"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fsdv2OuIy53jTmpfivEdB%2Fstep0_prereq.png?alt=media&#x26;token=ee866763-bf92-4807-86ec-f20f7266f673" alt=""><figcaption></figcaption></figure></div>

***

### 2. Open the *Add custom API* Form

In Manus, go to:

> **Settings → Integrations → Add custom API**

This opens the configuration form.

<div align="left" data-with-frame="true"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2F9dlp1kLCWc9oMzF9hBwV%2Fstep0_overview.png?alt=media&#x26;token=885df743-5004-4af4-9803-6eddbc5bc00e" alt=""><figcaption></figcaption></figure></div>

***

### 3. Fill Out the Configuration

#### A) Name

Enter:

```c
AI/ML API
```

<div align="left" data-with-frame="true"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fbs09mGaMYnjNoCJ16T12%2Fstep1_name.png?alt=media&#x26;token=19903f04-366c-4158-a3c8-d6b7d6f552c1" alt=""><figcaption></figcaption></figure></div>

***

#### B) Icon (optional)

Paste this URL into the icon field:

{% code overflow="wrap" %}

```css
https://raw.githubusercontent.com/OctavianTheI/aimlapi-assets-devrel/main/aimlapi%20square%20Logo%20Icon.svg
```

{% endcode %}

<div align="left" data-with-frame="true"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2FzaBl4Q9iGzyi9kbpwfJg%2Fstep2_icon.png?alt=media&#x26;token=6d9002e4-b9e4-4ee0-849e-3e2362387605" alt=""><figcaption></figcaption></figure></div>

***

#### C) Base URL & Auth Header

* **Base URL:**

```html
https://api.aimlapi.com
```

* **Authorization header (Manus will use the secret defined below):**

```python
Authorization: Bearer ${AIMLAPI_KEY}
```

<div align="left" data-with-frame="true"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2FzXNUl2fPXNhwcmR0kvPe%2Fstep0_tldr.png?alt=media&#x26;token=eff15381-73aa-44d5-aae6-6ff77898d70f" alt=""><figcaption></figcaption></figure></div>

***

#### D) Secrets

Create a secret to store your AI/ML API key:

* **Secret name:** `AIMLAPI_KEY`
* **Value:** your personal AI/ML API key from the AI/ML API dashboard.

<div align="left" data-with-frame="true"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2F9eq5kqbbQtery4QS72l8%2Fstep4_secret.png?alt=media&#x26;token=20c09475-f557-4f46-89e8-7b365c1f91c3" alt=""><figcaption></figcaption></figure></div>

***

#### E) Note (Request Templates)

Paste the following template into the **Note** field — Manus will use it as a reference for how to call AI/ML API endpoints:

{% code overflow="wrap" %}

```json
This custom API connects to https://api.aimlapi.com to access a variety of AI models.
The API key is stored in the AIMLAPI_KEY secret and must be sent as:
Authorization: Bearer ${AIMLAPI_KEY}

Base URL: https://api.aimlapi.com

## 1. Chat / Text & Code

POST /chat/completions
{ "model": "MODEL_NAME_HERE", "messages": [{"role":"user","content":"..."}] }

## 2. Text → Image

POST /images/generations
{ "model": "MODEL_NAME_HERE", "prompt": "Describe the image" }

## 3. Audio → Text (STT)

POST /audio/transcriptions
[file upload: "file"]
{ "model": "openai/whisper-1" }

## 4. Text → Speech (TTS)

POST /audio/speech
{ "model": "MODEL_NAME_HERE", "input": "Text to speak", "voice": "alloy" }

## 5. Image → Text (Vision)

POST /chat/completions
{ "model": "MODEL_NAME_HERE", "messages":[{"role":"user","content":[
{"type":"text","text":"Question"}, {"type":"image_url","image_url":{"url":"https://..."}}]}] }

## 6. Embeddings

POST /embeddings
{ "model": "MODEL_NAME_HERE", "input": "The text to embed" }
```

{% endcode %}

<div align="left" data-with-frame="true"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2FlH0YeyjccSA9eP5gtcDG%2Fstep3_note.png?alt=media&#x26;token=f0127b62-368c-49e1-980f-49ee3c88ce68" alt=""><figcaption></figcaption></figure></div>

***

### 4. Finalise the Integration

Click **Add**. Manus will save the integration and show a confirmation message.

<div align="left" data-with-frame="true"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2F8Fqi06K014SpZK7mHOW6%2Fstep5_final.png?alt=media&#x26;token=ba25dc0e-5424-49eb-9eb8-d641353dc9e3" alt=""><figcaption></figcaption></figure></div>

<div align="left" data-with-frame="true"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2FFTwhrvpj52X2iDg1oEq6%2Fstep5_chat_select.png?alt=media&#x26;token=3fef7163-abc8-421e-8a37-b2dfcbb150bf" alt=""><figcaption></figcaption></figure></div>

***

## Usage Examples

Once the custom API is added, you can select **AI/ML API** as a backend in Manus and use prompts such as:

* **Chat / Text & Code**

  > “Write a poem about spring.”
* **Text → Image**

  > “Draw a lonely lighthouse on a stormy coast using `openai/dall-e-3`.”
* **Embeddings**

  > “Generate embeddings for this paragraph with `BAAI/bge-large-en-v1.5`.”

<div align="left" data-with-frame="true"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fp7tIrnnN9xk6CcNXNoon%2Fstep6_usage.png?alt=media&#x26;token=a5301717-184c-4b49-bf42-d9036f9c48ae" alt=""><figcaption></figcaption></figure></div>

***

## Tips

* You can use either `https://api.aimlapi.com` or `https://api.aimlapi.com/v1` as the base URL.
* All requests must include:

  ```python
  Authorization: Bearer ${AIMLAPI_KEY}
  ```
* AI/ML API supports a wide range of providers and models (chat, code, images, audio, vision, embeddings) with enterprise-grade rate limits and uptime.

***

## Helpful Links

* Dashboard: [https://aimlapi.com/app/](https://aimlapi.com/app/?utm_source=manus\&utm_medium=github\&utm_campaign=integration)
* API Keys: [https://aimlapi.com/app/keys/](https://aimlapi.com/app/keys/?utm_source=manus\&utm_medium=github\&utm_campaign=integration)
* Models browser: [https://aimlapi.com/models/](https://aimlapi.com/models/?utm_source=manus\&utm_medium=github\&utm_campaign=integration)
* Docs: [https://docs.aimlapi.com/](https://docs.aimlapi.com/?utm_source=manus\&utm_medium=github\&utm_campaign=integration)

Enjoy building with Manus + AI/ML API 🚀
