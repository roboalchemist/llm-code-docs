# Source: https://docs.api7.ai/apisix/how-to-guide/ai-gateway/proxy-anthropic-requests.md

# Proxy Anthropic Requests

[Anthropic](https://www.anthropic.com/) provides an OpenAI-compatible API that allows you to access Claude models using the familiar OpenAI API format.

This guide shows how to integrate APISIX with Anthropic using the [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugin. With provider set to `anthropic`, you do not need to set a custom endpoint.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker/).
* Install [cURL](https://curl.se/) to send requests to the services for validation.
* Follow the [Getting Started Tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker or on Kubernetes.

## Obtain an Anthropic API Key[â](#obtain-an-anthropic-api-key "Direct link to Obtain an Anthropic API Key")

Create an account and API key by following the [Anthropic API Documentation](https://docs.anthropic.com/en/api/getting-started). Optionally save the key to an environment variable:

```
export ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  # replace with your API key
```

## Create a Route to Anthropic[â](#create-a-route-to-anthropic "Direct link to Create a Route to Anthropic")

Create a route with the [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugin as such:

* Admin API
* ADC

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '{
  "id": "anthropic-chat",
  "uri": "/anything",
  "plugins": {
    "ai-proxy": {
      "provider": "anthropic",
      "auth": {
        "header": {
          "Authorization": "Bearer '"$ANTHROPIC_API_KEY"'"
        }
      },
      "options": {
        "model": "claude-sonnet-4-5"
      }
    }
  }
}'
```

â¶ Set the provider to `anthropic`.

â· Attach the Anthropic API key using the `Authorization` header.

â¸ Set a model supported by Anthropic, for example `claude-sonnet-4-5`.

adc.yaml

```
services:
  - name: Anthropic Service
    routes:
      - uris:
          - /anything
        name: anthropic-chat
        plugins:
          ai-proxy:
            provider: anthropic
            auth:
              header:
                Authorization: "Bearer sk-ant-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            options:
              model: claude-sonnet-4-5
```

â¶ Set the provider to `anthropic`.

â· Attach the Anthropic API key using the `Authorization` header.

â¸ Set a model supported by Anthropic, for example `claude-sonnet-4-5`.

Synchronize the configuration to APISIX:

```
adc sync -f adc.yaml
```

## Verify[â](#verify "Direct link to Verify")

Send a request with the following prompts to the route:

```
curl "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "Hello"}]}'
```

You should receive a response similar to the following:

```
{
  "request": {
    "messages": [
      {
        "role": "user",
        "content": "Hello"
      }
    ]
  },
  "response": {
    "id": "msg_01HUQ8fAR1XvJ9PodefrZixW",
    "object": "chat.completion",
    "created": 1770029318,
    "model": "claude-sonnet-4-5-20250929",
    "choices": [
      {
        "index": 0,
        "finish_reason": "stop",
        "message": {
          "role": "assistant",
          "content": "Hello! How can I help you today?"
        }
      }
    ],
    "usage": {
      "prompt_tokens": 8,
      "completion_tokens": 12,
      "total_tokens": 20
    }
  }
}
```

## Next Steps[â](#next-steps "Direct link to Next Steps")

You have learned how to integrate APISIX with Anthropic. See the [Anthropic API Documentation](https://docs.anthropic.com/en/api/getting-started) and [Models](https://docs.anthropic.com/en/docs/about-claude/models) pages for more details.

If you would like to stream responses, enable streaming in your request and use the [`proxy-buffering`](https://docs.api7.ai/hub/proxy-buffering.md) plugin to disable NGINX `proxy_buffering` to avoid server-sent events (SSE) being buffered.
