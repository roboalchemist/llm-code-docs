# Source: https://developers.cloudflare.com/ai-gateway/usage/providers/openai/index.md

---

title: OpenAI · Cloudflare AI Gateway docs
description: OpenAI helps you build with GPT models.
lastUpdated: 2025-11-25T12:59:29.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/ai-gateway/usage/providers/openai/
  md: https://developers.cloudflare.com/ai-gateway/usage/providers/openai/index.md
---

[OpenAI](https://openai.com/about/) helps you build with GPT models.

## Endpoint

**Base URL**

```plaintext
https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai
```

When making requests to OpenAI, replace `https://api.openai.com/v1` in the URL you are currently using with `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai`.

**Chat completions endpoint**

`https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/chat/completions`

**Responses endpoint**

`https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/responses`

## Examples

### OpenAI SDK

With Key in Request

* With Authenticated Gateway

  ```js
  import OpenAI from "openai";


  const client = new OpenAI({
    apiKey: "YOUR_OPENAI_API_KEY",
    defaultHeaders: {
      "cf-aig-authorization": `Bearer {cf_api_token}`,
    },
    baseURL:
      "https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai",
  });


  const response = await client.chat.completions.create({
    model: "gpt-4o-mini",
    messages: [{ role: "user", content: "Hello, world!" }],
  });
  ```

* Unauthenticated Gateway

  ```js
  import OpenAI from "openai";


  const client = new OpenAI({
    apiKey: "YOUR_OPENAI_API_KEY",
    baseURL:
      "https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai",
  });


  const response = await client.chat.completions.create({
    model: "gpt-4o-mini",
    messages: [{ role: "user", content: "Hello, world!" }],
  });
  ```

With Stored Keys (BYOK) / Unified Billing

```js
import OpenAI from "openai";


const client = new OpenAI({
  apiKey: "{cf_api_token}",
  baseURL:
    "https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai",
});


// Ensure your OpenAI API key is stored with BYOK
// or Unified Billing has credits
const response = await client.chat.completions.create({
  model: "gpt-4o-mini",
  messages: [{ role: "user", content: "Hello, world!" }],
});
```

### cURL

Responses API with API Key in Request

* With Authenticated Gateway

  ```bash
  curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/responses \
    --header 'Authorization: Bearer {OPENAI_API_KEY}' \
    --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
    --header 'Content-Type: application/json' \
    --data '{
      "model": "gpt-5.1",
      "input": [
        {
          "role": "user",
          "content": "Write a one-sentence bedtime story about a unicorn."
        }
      ]
    }'
  ```

* Unauthenticated Gateway

  ```bash
  curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/responses \
    --header 'Authorization: Bearer {OPENAI_API_KEY}' \
    --header 'Content-Type: application/json' \
    --data '{
      "model": "gpt-5.1",
      "input": [
        {
          "role": "user",
          "content": "Write a one-sentence bedtime story about a unicorn."
        }
      ]
    }'
  ```

Chat Completions with API Key in Request

* With Authenticated Gateway

  ```bash
  curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/chat/completions \
    --header 'Authorization: Bearer {OPENAI_API_KEY}' \
    --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
    --header 'Content-Type: application/json' \
    --data '{
      "model": "gpt-4o-mini",
      "messages": [
        {
          "role": "user",
          "content": "What is Cloudflare?"
        }
      ]
    }'
  ```

* Unauthenticated Gateway

  ```bash
  curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/chat/completions \
    --header 'Authorization: Bearer {OPENAI_API_KEY}' \
    --header 'Content-Type: application/json' \
    --data '{
      "model": "gpt-4o-mini",
      "messages": [
        {
          "role": "user",
          "content": "What is Cloudflare?"
        }
      ]
    }'
  ```

Responses API with Stored Keys (BYOK) / Unified Billing

```bash
curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/responses \
  --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "gpt-5.1",
    "input": [
      {
        "role": "user",
        "content": "Write a one-sentence bedtime story about a unicorn."
      }
    ]
  }'
```

Chat Completions with Stored Keys (BYOK) / Unified Billing

```bash
curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/chat/completions \
  --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "gpt-4o-mini",
    "messages": [
      {
        "role": "user",
        "content": "What is Cloudflare?"
      }
    ]
  }'
```
