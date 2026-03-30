# Source: https://docs.api7.ai/apisix/how-to-guide/ai-gateway/configure-prompt-decorators.md

# Configure Prompt Decorators

When working with [large language models (LLMs)](https://en.wikipedia.org/wiki/Large_language_model) for specialized content generation, it is a common practice to pre-engineer and pre-configure prompts as the ârules of engagementâ to shape how the model should operate within desired guidelines and safety standards in the subsequent interactions.

In this document, you will learn how to configure prompt decorators in APISIX using the [`ai-prompt-decorator`](https://docs.api7.ai/hub/ai-prompt-decorator.md) plugin, to prepend and append additional messages to the user-defined message. While the document will be using [OpenAI](https://openai.com/) as the sample upstream service, the procedure can be easily adapted to work with other LLM service providers.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker/).
* Install [cURL](https://curl.se/) to send requests to the services for validation.
* Follow the [Getting Started Tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker or on Kubernetes.

## Obtain an OpenAI API Key[â](#obtain-an-openai-api-key "Direct link to Obtain an OpenAI API Key")

Create an [OpenAI account](https://openai.com) and an [API key](https://openai.com/blog/openai-api) before proceeding. You can optionally save the key to an environment variable as such:

```
export OPENAI_API_KEY=sk-REDACTED-EXAMPLE-KEY   # replace with your API key
```

## Create a Route[â](#create-a-route "Direct link to Create a Route")

In this example, you will prepend a system prompt to instruct the model to answer briefly and conceptually, and append a user prompt to instruct the model to end the answer with a simple analogy.

Create a route to the chat completion endpoint with pre-configured prompt templates:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-prompt-decorator-route",
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
          "model": "gpt-4"
        }
      },
      "ai-prompt-decorator": {
        "prepend":[
          {
            "role": "system",
            "content": "Answer briefly and conceptually."
          }
        ],
        "append":[
          {
            "role": "user",
            "content": "End the answer with a simple analogy."
          }
        ]
      }
    }
  }'
```

â¶ Prepend a system message to set the behavior of the assistant.

â· Append an additional user message to the user-defined prompt.

## Verify[â](#verify "Direct link to Verify")

Send a POST request to the route with a sample message in the request body:

```
curl "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [{ "role": "user", "content": "What is mTLS authentication?" }]
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
        "content": "Mutual TLS (mTLS) authentication is a security protocol that ensures both the client and server authenticate each other's identity before establishing a connection. This mutual authentication is achieved through the exchange and verification of digital certificates, which are cryptographically signed credentials proving each party's identity. In contrast to standard TLS, where only the server is authenticated, mTLS adds an additional layer of trust by verifying the client as well, providing enhanced security for sensitive communications.\n\nThink of mTLS as a secret handshake between two friends meeting at a club. Both must know the handshake to get in, ensuring they recognize and trust each other before entering.",
        "role": "assistant"
      }
    }
  ],
  "created": 1723193502,
  "id": "chatcmpl-9uFdWDlwKif6biCt9DpG0xgedEamg",
  "model": "gpt-4o-2024-05-13",
  "object": "chat.completion",
  "system_fingerprint": "fp_abc28019ad",
  "usage": {
    "completion_tokens": 124,
    "prompt_tokens": 31,
    "total_tokens": 155
  }
}
```

## Next Steps[â](#next-steps "Direct link to Next Steps")

You have now learned how to configure prompt decorators in APISIX when integrating with LLM service providers.

If you would like to integrate with OpenAI's [streaming API](https://platform.openai.com/docs/api-reference/streaming), you can use the [`proxy-buffering`](https://docs.api7.ai/hub/proxy-buffering.md) plugin to disable NGINX's `proxy_buffering` directive to avoid server-sent events (SSE) being buffered.

In addition, you can integrate more capabilities that APISIX offers, such as [rate limiting](https://docs.api7.ai/apisix/how-to-guide/traffic-management/rate-limiting.md) and [caching](https://docs.api7.ai/hub/proxy-cache.md), to improve system availability and user experience.
