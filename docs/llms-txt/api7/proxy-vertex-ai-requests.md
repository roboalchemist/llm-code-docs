# Source: https://docs.api7.ai/apisix/how-to-guide/ai-gateway/proxy-vertex-ai-requests.md

# Proxy Vertex AI Requests

[Vertex AI](https://cloud.google.com/vertex-ai) provides access to Google's Gemini models through an OpenAI-compatible API.

This guide shows how to integrate APISIX with Vertex AI using the [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugin. With provider set to `vertex-ai`, you can configure your project and region through `provider_conf` without specifying a custom endpoint.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker/).
* Install [cURL](https://curl.se/) to send requests to the services for validation.
* Follow the [Getting Started Tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker or on Kubernetes.
* Have a Google Cloud project with [Vertex AI API enabled](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com).

## Obtain a Vertex AI Service Account Key[â](#obtain-a-vertex-ai-service-account-key "Direct link to Obtain a Vertex AI Service Account Key")

Create a service account and JSON key by following the [Google Cloud service account documentation](https://cloud.google.com/iam/docs/service-accounts-create). Ensure the service account has permissions to call Vertex AI (for example, `Vertex AI User`).

Optionally save the service account JSON to an environment variable:

```
export GCP_SERVICE_ACCOUNT_JSON="$(cat /path/to/service-account.json)"
```

## Create a Route to Vertex AI[â](#create-a-route-to-vertex-ai "Direct link to Create a Route to Vertex AI")

Create a route with the [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugin as such:

* Admin API
* ADC

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '{
  "id": "vertex-ai-chat",
  "uri": "/anything",
  "plugins": {
    "ai-proxy": {
      "provider": "vertex-ai",
      "provider_conf": {
        "project_id": "evident-xxx",
        "region": "us-central1"
      },
      "auth": {
        "gcp": {
          "service_account_json": "'"$GCP_SERVICE_ACCOUNT_JSON"'"
        }
      },
      "options": {
        "model": "google/gemini-2.5-flash"
      }
    }
  }
}'
```

â¶ Set the provider to `vertex-ai` and configure `project_id` and `region`.

â· Replace with your service account JSON.

â¸ Set a model supported by Vertex AI, for example `google/gemini-2.5-flash`.

adc.yaml

```
services:
  - name: Vertex AI Service
    routes:
      - uris:
          - /anything
        name: vertex-ai-chat
        plugins:
          ai-proxy:
            provider: vertex-ai
            provider_conf:
              project_id: evident-xxx
              region: us-central1
            auth:
              gcp:
                service_account_json: |
                  {
                    ...
                  }
            options:
              model: google/gemini-2.5-flash
```

â¶ Set the provider to `vertex-ai` and configure `project_id` and `region`.

â· Replace with your service account JSON.

â¸ Set a model supported by Vertex AI, for example `google/gemini-2.5-flash`.

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
      { "role": "system", "content": "You are a mathematician" },
      { "role": "user", "content": "What is 1+1?" }
    ]
  }'
```

You should receive a response similar to the following:

```
{
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "1 + 1 = 2\n"
      },
      "index": 0,
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "completion_tokens": 8,
    "extra_properties": {
      "google": {
        "traffic_type": "ON_DEMAND"
      }
    },
    "total_tokens": 19,
    "prompt_tokens": 11
  },
  "object": "chat.completion",
  "model": "google/gemini-2.5-flash",
  ...
}
```

## Next Steps[â](#next-steps "Direct link to Next Steps")

You have learned how to integrate APISIX with Vertex AI. See the [Vertex AI documentation](https://cloud.google.com/vertex-ai/docs) and [Gemini models](https://cloud.google.com/vertex-ai/generative-ai/docs/models) pages for more details.

If you would like to stream responses, enable streaming in your request and use the [`proxy-buffering`](https://docs.api7.ai/hub/proxy-buffering.md) plugin to disable NGINX `proxy_buffering` to avoid server-sent events (SSE) being buffered.
