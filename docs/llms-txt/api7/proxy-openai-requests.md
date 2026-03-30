# Source: https://docs.api7.ai/apisix/how-to-guide/ai-gateway/proxy-openai-requests.md

# Proxy OpenAI Requests

[OpenAI](https://openai.com/) provides access to state-of-the-art AI models, such as GPT-3, for various applications including natural language processing, text generation, and more. Integrating OpenAI's APIs into your applications can unlock powerful capabilities for text analysis, content generation, and other AI-driven tasks.

APISIX provides capabilities for secret management, response streaming, rate limiting, and more, making it an excellent choice for proxying requests from OpenAI's API endpoints.

This guide will show you how to configure APISIX to integrate with OpenAI APIs to proxy user requests and model responses, using the [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugin.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker/).
* Install [cURL](https://curl.se/) to send requests to the services for validation.
* Follow the [Getting Started Tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker or on Kubernetes.

## Obtain an OpenAI API Key[â](#obtain-an-openai-api-key "Direct link to Obtain an OpenAI API Key")

Create an [OpenAI account](https://openai.com) and an [API key](https://openai.com/blog/openai-api) before proceeding. You can optionally save the key to an environment variable as such:

```
export OPENAI_API_KEY=sk-REDACTED-EXAMPLE-KEY   # replace with your API key
```

## Create a Route to OpenAI API[â](#create-a-route-to-openai-api "Direct link to Create a Route to OpenAI API")

Create a route with the [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugin as such:

* Admin API
* ADC

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '{
  "id": "openai-chat",
  "uri": "/anything",
  "plugins": {
    "ai-proxy": {
      "provider": "openai",
      "auth": {
        "header": {
          "Authorization": "Bearer '"$OPENAI_API_KEY"'"
        }
      },
      "options": {
        "model": "gpt-3.5-turbo"
      }
    }
  }
}'
```

â¶ Set the provider to `openai`, which will proxy requests to the OpenAI endpoint.

â· Attach OpenAPI API key to `Authorization` request header.

â¸ Set the model to `gpt-3.5-turbo`.

adc.yaml

```
services:
  - name: OpenAI Service
    routes:
      - uris:
          - /anything
        name: openai-chat
        plugins:
          ai-proxy:
            provider: openai
            auth:
              header:
                Authorization: sk-REDACTED-EXAMPLE-KEY
            options:
              model: "gpt-3.5-turbo"
```

â¶ Set the provider to `openai`, which will proxy requests to the OpenAI endpoint.

â· Attach OpenAPI API key to `Authorization` request header.

â¸ Set the model to `gpt-3.5-turbo`.

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
  ...,
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "A Turing machine is an abstract mathematical model that manipulates symbols on an infinite tape according to a set of rules, representing the concept of a general-purpose computer."
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  ...
}
```

See [OpenAI's API specifications](https://platform.openai.com/docs/api-reference/chat/create) for more information about how to compose the request.

## Next Steps[â](#next-steps "Direct link to Next Steps")

You have now learned how to integrate APISIX with OpenAI. See [OpenAI's API reference](https://platform.openai.com/docs/api-reference) to learn more about OpenAI's capabilities.

If you would like to integrate with OpenAI's [streaming API](https://platform.openai.com/docs/api-reference/streaming), you can use the [`proxy-buffering`](https://docs.api7.ai/hub/proxy-buffering.md) plugin to disable NGINX's `proxy_buffering` directive to avoid server-sent events (SSE) being buffered.

In addition, you can integrate more capabilities that APISIX offers, such as [rate limiting](https://docs.api7.ai/apisix/how-to-guide/traffic-management/rate-limiting.md) and [caching](https://docs.api7.ai/hub/proxy-cache.md), to improve system availability and user experience.
