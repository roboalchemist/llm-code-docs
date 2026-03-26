# Source: https://docs.api7.ai/apisix/how-to-guide/ai-gateway/proxy-gemini-requests.md

# Proxy Gemini Requests

[Google Gemini](https://ai.google.dev/) provides an OpenAI-compatible API that allows you to access Gemini models using the familiar OpenAI API format.

This guide shows how to integrate APISIX with Google Gemini using the [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugin. With provider set to `gemini`, you do not need to set a custom endpoint.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker/).
* Install [cURL](https://curl.se/) to send requests to the services for validation.
* Follow the [Getting Started Tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker or on Kubernetes.

## Obtain a Google API Key[â](#obtain-a-google-api-key "Direct link to Obtain a Google API Key")

Create an account and API key by following the [Google AI Studio](https://aistudio.google.com/apikey). Optionally save the key to an environment variable:

```
export GEMINI_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  # replace with your API key
```

## Create a Route to Gemini[â](#create-a-route-to-gemini "Direct link to Create a Route to Gemini")

Create a route with the [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugin as such:

* Admin API
* ADC

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '{
  "id": "gemini-chat",
  "uri": "/anything",
  "plugins": {
    "ai-proxy": {
      "provider": "gemini",
      "auth": {
        "header": {
          "Authorization": "Bearer '"$GEMINI_API_KEY"'"
        }
      },
      "options": {
        "model": "gemini-2.5-flash"
      }
    }
  }
}'
```

â¶ Set the provider to `gemini`.

â· Attach the Google API key using the `Authorization` header.

â¸ Set a model supported by Gemini, for example `gemini-2.5-flash`.

adc.yaml

```
services:
  - name: Gemini Service
    routes:
      - uris:
          - /anything
        name: gemini-chat
        plugins:
          ai-proxy:
            provider: gemini
            auth:
              header:
                Authorization: "Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            options:
              model: gemini-2.5-flash
```

â¶ Set the provider to `gemini`.

â· Attach the Google API key using the `Authorization` header.

â¸ Set a model supported by Gemini, for example `gemini-2.5-flash`.

Synchronize the configuration to APISIX:

```
adc sync -f adc.yaml
```

## Verify[â](#verify "Direct link to Verify")

Send a request with the following prompts to the route:

```
curl "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      { "role": "system", "content": "You are a helpful AI assistant" },
      { "role": "user", "content": "What is the capital of France?" }
    ]
  }'
```

You should receive a response similar to the following:

```
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "The capital of France is **Paris**.",
        "role": "assistant"
      }
    }
  ],
  "model": "gemini-2.5-flash",
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 8,
    "prompt_tokens": 15,
    "total_tokens": 41
  },
  ...
}
```

## Next Steps[â](#next-steps "Direct link to Next Steps")

You have learned how to integrate APISIX with Google Gemini. See the [Google AI for Developers](https://ai.google.dev/gemini-api/docs) and [Models](https://ai.google.dev/gemini-api/docs/models/gemini) pages for more details.

If you would like to stream responses, enable streaming in your request and use the [`proxy-buffering`](https://docs.api7.ai/hub/proxy-buffering.md) plugin to disable NGINX `proxy_buffering` to avoid server-sent events (SSE) being buffered.
