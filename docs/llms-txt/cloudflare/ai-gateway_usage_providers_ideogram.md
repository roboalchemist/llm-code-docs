# Source: https://developers.cloudflare.com/ai-gateway/usage/providers/ideogram/index.md

---

title: Ideogram · Cloudflare AI Gateway docs
description: Ideogram provides advanced text-to-image generation models with
  exceptional text rendering capabilities and visual quality.
lastUpdated: 2025-11-25T09:00:35.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/ai-gateway/usage/providers/ideogram/
  md: https://developers.cloudflare.com/ai-gateway/usage/providers/ideogram/index.md
---

[Ideogram](https://ideogram.ai/) provides advanced text-to-image generation models with exceptional text rendering capabilities and visual quality.

## Endpoint

```txt
https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/ideogram
```

## Prerequisites

When making requests to Ideogram, ensure you have the following:

* Your AI Gateway Account ID.
* Your AI Gateway gateway name.
* An active Ideogram API key.
* The name of the Ideogram model you want to use (e.g., `V_3`).

## Examples

### cURL

```bash
curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/ideogram/v1/ideogram-v3/generate \
  --header 'Api-Key: {ideogram_api_key}' \
  --header 'Content-Type: application/json' \
  --data '{
    "prompt": "A serene landscape with mountains and a lake at sunset",
    "model": "V_3"
  }'
```

### Use with JavaScript

```js
const accountId = "{account_id}";
const gatewayId = "{gateway_id}";
const ideogramApiKey = "{ideogram_api_key}";
const baseURL = `https://gateway.ai.cloudflare.com/v1/${accountId}/${gatewayId}/ideogram`;


const response = await fetch(`${baseURL}/v1/ideogram-v3/generate`, {
  method: "POST",
  headers: {
    "Api-Key": ideogramApiKey,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    prompt: "A serene landscape with mountains and a lake at sunset",
    model: "V_3",
  }),
});


const result = await response.json();
console.log(result);
```
