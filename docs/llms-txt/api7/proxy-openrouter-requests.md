# Source: https://docs.api7.ai/apisix/how-to-guide/ai-gateway/proxy-openrouter-requests.md

# Proxy OpenRouter Requests

[OpenRouter](https://openrouter.ai/) provides a unified, OpenAI-compatible API that aggregates models from multiple providers (OpenAI, Anthropic, Google, Mistral, and more).

This guide shows how to integrate APISIX with OpenRouter using the [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugin. With provider set to `openrouter`, you do not need to set a custom endpoint.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker/).
* Install [cURL](https://curl.se/) to send requests to the services for validation.
* Follow the [Getting Started Tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker or on Kubernetes.

## Obtain an OpenRouter API Key[â](#obtain-an-openrouter-api-key "Direct link to Obtain an OpenRouter API Key")

Create an account and API key by following the [OpenRouter Quickstart](https://openrouter.ai/docs/quickstart). Optionally save the key to an environment variable:

```
export OPENROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  # replace with your API key
```

## Create a Route to OpenRouter[â](#create-a-route-to-openrouter "Direct link to Create a Route to OpenRouter")

Create a route with the [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugin as such:

* Admin API
* ADC

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '{
  "id": "openrouter-chat",
  "uri": "/anything",
  "plugins": {
    "ai-proxy": {
      "provider": "openrouter",
      "auth": {
        "header": {
          "Authorization": "Bearer '"$OPENROUTER_API_KEY"'"
        }
      },
      "options": {
        "model": "deepseek/deepseek-chat"
      }
    }
  }
}'
```

â¶ Set the provider to `openrouter`.

â· Attach the OpenRouter API key using the `Authorization` header.

â¸ Set a model supported by OpenRouter, for example `deepseek/deepseek-chat`.

adc.yaml

```
services:
  - name: OpenRouter Service
    routes:
      - uris:
          - /anything
        name: openrouter-chat
        plugins:
          ai-proxy:
            provider: openrouter
            auth:
              header:
                Authorization: "Bearer sk-or-v1-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            options:
              model: deepseek/deepseek-chat
```

â¶ Set the provider to `openrouter`.

â· Attach the OpenRouter API key using the `Authorization` header.

â¸ Set a model supported by OpenRouter, for example `deepseek/deepseek-chat`.

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
      {
        "role": "system",
        "content": "You are a computer scientist."
      },
      {
        "role": "user",
        "content": "Explain in one sentence what a Turing machine is."
      }
    ]
  }'
```

You should receive a response similar to the following:

```
{
  "id": "gen-1770023173-XYUZ4kUwUAWHwDMPLN20",
  "provider": "Novita",
  "model": "deepseek/deepseek-chat",
  ...
  "choices": [
    {
      "logprobs": null,
      "finish_reason": "stop",
      "native_finish_reason": "stop",
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "A Turing machine is a theoretical computational model that manipulates symbols on an infinite tape according to a set of rules, simulating any algorithm's logic and serving as the foundation for modern computability theory.",
        "refusal": null,
        "reasoning": null
      }
    }
  ],
  ...
}
```

## Next Steps[â](#next-steps "Direct link to Next Steps")

You have learned how to integrate APISIX with OpenRouter. See the [OpenRouter Quickstart](https://openrouter.ai/docs/quickstart) and [Models](https://openrouter.ai/models) pages for more details.

If you would like to stream responses, enable streaming in your request and use the [`proxy-buffering`](https://docs.api7.ai/hub/proxy-buffering.md) plugin to disable NGINX `proxy_buffering` to avoid server-sent events (SSE) being buffered.
