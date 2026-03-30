# Source: https://docs.api7.ai/hub/ai-proxy-multi.md

# ai-proxy-multi

The `ai-proxy-multi` plugin simplifies access to LLM and embedding models by transforming plugin configurations into the designated request format for OpenAI, DeepSeek, Gemini, Vertex AI, and other OpenAI-compatible APIs. It extends the capabilities of [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) with load balancing, retries, fallbacks, and health checks.

In addition, the plugin also supports logging LLM request information in the access log, such as token usage, model, time to the first response, and more.

<!-- -->

## Demo[â](#demo "Direct link to Demo")

The following demo demonstrates the [configure instance priority and rate limiting example](#configure-instance-priority-and-rate-limiting). It shows how you can configure two models with different priorities and apply rate limiting on the instance with a higher priority in API7 Enterprise using the Dashboard. In the case where `fallback_strategy` is set to `["rate_limiting"]`, the plugin should continue to forward requests to the low priority instance once the high priority instance's rate limiting quota is fully consumed.

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can configure `ai-proxy-multi` for different scenarios.

### Load Balance between Instances[â](#load-balance-between-instances "Direct link to Load Balance between Instances")

The following example demonstrates how you can configure two models for load balancing, forwarding 80% of the traffic to one instance and 20% to the other.

For demonstration and easier differentiation, you will be configuring one OpenAI instance and one DeepSeek instance as the upstream LLM services.

Create a route as such and update with your LLM providers, models, API keys, and endpoints if applicable:

* Admin API
* ADC
* Ingress Controller

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-proxy-multi-route",
    "uri": "/anything",
    "methods": ["POST"],
    "plugins": {
      "ai-proxy-multi": {
        "instances": [
          {
            "name": "openai-instance",
            "provider": "openai",
            "weight": 8,
            "auth": {
              "header": {
                "Authorization": "Bearer '"$OPENAI_API_KEY"'"
              }
            },
            "options": {
              "model": "gpt-4"
            }
          },
          {
            "name": "deepseek-instance",
            "provider": "deepseek",
            "weight": 2,
            "auth": {
              "header": {
                "Authorization": "Bearer '"$DEEPSEEK_API_KEY"'"
              }
            },
            "options": {
              "model": "deepseek-chat"
            }
          }
        ]
      }
    }
  }'
```

â¶ Configure the weight for `openai-instance` to be `8`.

â· Configure the weight for `deepseek-instance` to be `2`.

adc.yaml

```
services:
  - name: ai-proxy-multi-service
    routes:
      - name: ai-proxy-multi-route
        uris:
          - /anything
        methods:
          - POST
        plugins:
          ai-proxy-multi:
            instances:
              - name: openai-instance
                provider: openai
                weight: 8
                auth:
                  header:
                    Authorization: "Bearer ${OPENAI_API_KEY}"
                options:
                  model: gpt-4
              - name: deepseek-instance
                provider: deepseek
                weight: 2
                auth:
                  header:
                    Authorization: "Bearer ${DEEPSEEK_API_KEY}"
                options:
                  model: deepseek-chat
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

â¶ Configure the weight for `openai-instance` to be `8`.

â· Configure the weight for `deepseek-instance` to be `2`.

* Gateway API
* APISIX CRD

ai-proxy-multi-ic.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: ai-proxy-multi-plugin-config
spec:
  plugins:
    - name: ai-proxy-multi
      config:
        instances:
          - name: openai-instance
            provider: openai
            weight: 8
            auth:
              header:
                Authorization: "Bearer sk-REDACTED-EXAMPLE-KEY"
            options:
              model: gpt-4
          - name: deepseek-instance
            provider: deepseek
            weight: 2
            auth:
              header:
                Authorization: "Bearer sk-5e99f3e26abc40e75d80009a90e66"
            options:
              model: deepseek-chat
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: ai-proxy-multi-route
spec:
  parentRefs:
    - name: apisix
  rules:
    - matches:
        - path:
            type: Exact
            value: /anything
          method: POST
      filters:
        - type: ExtensionRef
          extensionRef:
            group: apisix.apache.org
            kind: PluginConfig
            name: ai-proxy-multi-plugin-config
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-proxy-multi-ic.yaml
```

â¶ Configure the weight for `openai-instance` to be `8`.

â· Configure the weight for `deepseek-instance` to be `2`.

ai-proxy-multi-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: ai-proxy-multi-route
spec:
  ingressClassName: apisix
  http:
    - name: ai-proxy-multi-route
      match:
        paths:
          - /anything
        methods:
          - POST
      plugins:
        - name: ai-proxy-multi
          enable: true
          config:
            instances:
              - name: openai-instance
                provider: openai
                weight: 8
                auth:
                  header:
                    Authorization: "Bearer sk-REDACTED-EXAMPLE-KEY"
                options:
                  model: gpt-4
              - name: deepseek-instance
                provider: deepseek
                weight: 2
                auth:
                  header:
                    Authorization: "Bearer sk-5e99f3e26abc40e75d80009a90e66"
                options:
                  model: deepseek-chat
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-proxy-multi-ic.yaml
```

â¶ Configure the weight for `openai-instance` to be `8`.

â· Configure the weight for `deepseek-instance` to be `2`.

Send 10 POST requests to the route with a system prompt and a sample user question in the request body, to see the number of requests forwarded to OpenAI and DeepSeek:

```
openai_count=0
deepseek_count=0

for i in {1..10}; do 
  model=$(curl -s "http://127.0.0.1:9080/anything" -X POST \
    -H "Content-Type: application/json" \
    -d '{
      "messages": [
        { "role": "system", "content": "You are a mathematician" },
        { "role": "user", "content": "What is 1+1?" }
      ]
    }' | jq -r '.model')

  if [[ "$model" == *"gpt-4"* ]]; then
    ((openai_count++))
  elif [[ "$model" == "deepseek-chat" ]]; then
    ((deepseek_count++))
  fi
done

echo "OpenAI responses: $openai_count"
echo "DeepSeek responses: $deepseek_count"
```

You should see a response similar to the following:

```
OpenAI responses: 8
DeepSeek responses: 2
```

### Load Balance between Gemini and Vertex AI[â](#load-balance-between-gemini-and-vertex-ai "Direct link to Load Balance between Gemini and Vertex AI")

The following example demonstrates how you can configure load balancing between Google AI Studio Gemini and Vertex AI Gemini, forwarding 70% of traffic to Gemini and 30% to Vertex AI. This example applies only to API7 Enterprise from version 3.9.2 and is not applicable in APISIX.

Before proceeding:

1. For Google AI Studio Gemini, [obtain a Gemini API key](https://ai.google.dev/gemini-api/docs/api-key).
2. For Vertex AI Gemini, [enable Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/featurestore/setup) and billing for your GCP project. Then, follow the [service account credentials](https://developers.google.com/workspace/guides/create-credentials#service-account) instructions to create a service account in GCP, assign it the "Vertex AI User" role, and download the account credentials in JSON format.

Create a route as such and update with your project ID and region:

* Admin API
* ADC
* Ingress Controller

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-proxy-multi-google-ai-route",
    "uri": "/anything",
    "methods": ["POST"],
    "plugins": {
      "ai-proxy-multi": {
        "fallback_strategy": ["rate_limiting"],
        "instances": [
          {
            "name": "gemini-instance",
            "provider": "gemini",
            "weight": 7,
            "auth": {
              "header": {
                "Authorization": "Bearer '"$GEMINI_API_KEY"'"
              }
            },
            "options": {
              "model": "gemini-2.5-flash"
            }
          },
          {
            "name": "vertex-ai-instance",
            "provider": "vertex-ai",
            "weight": 3,
            "auth": {
              "gcp": {
                "service_account_json": "'"$GCP_SA_JSON"'"
              }
            },
            "provider_conf": {
              "project_id": "api7-vertex",
              "region": "us-central1"
            },
            "options": {
              "model": "google/gemini-2.5-flash"
            }
          }
        ]
      }
    }
  }'
```

â¶ Configure the provider to be `gemini` for Google AI Studio Gemini access.

â· Replace with your Gemini API key in the `Authorization` header.

â¸ Specify the name of the Gemini model through Google AI Studio in the `<model>` format.

â¹ Configure the provider to be `vertex-ai` for Vertex AI Gemini access.

âº Replace with your JSON credentials. Ensure that it is a JSON-escaped string.

â» Replace with your Vertex AI project ID and region.

â¼ Specify the name of the Gemini model through Vertex AI in the `<publisher>/<model>` format.

adc.yaml

```
services:
  - name: ai-proxy-multi-service
    routes:
      - name: ai-proxy-multi-route
        uris:
          - /anything
        methods:
          - POST
        plugins:
          ai-proxy-multi:
            fallback_strategy:
              - rate_limiting
            instances:
              - name: gemini-instance
                provider: gemini
                weight: 7
                auth:
                  header:
                    Authorization: "Bearer ${GEMINI_API_KEY}"
                options:
                  model: gemini-2.5-flash
              - name: vertex-ai-instance
                provider: vertex-ai
                weight: 3
                auth:
                  gcp:
                    service_account_json: "${GCP_SA_JSON}"
                provider_conf:
                  project_id: api7-vertex
                  region: us-central1
                options:
                  model: google/gemini-2.5-flash
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

â¶ Configure the provider to be `gemini` for Google AI Studio Gemini access.

â· Replace with your Gemini API key in the `Authorization` header.

â¸ Specify the name of the Gemini model through Google AI Studio in the `<model>` format.

â¹ Configure the provider to be `vertex-ai` for Vertex AI Gemini access.

âº Replace with your JSON credentials. Ensure that it is a JSON-escaped string.

â» Replace with your Vertex AI project ID and region.

â¼ Specify the name of the Gemini model through Vertex AI in the `<publisher>/<model>` format.

* Gateway API
* APISIX CRD

ai-proxy-multi-ic.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: ai-proxy-multi-plugin-config
spec:
  plugins:
    - name: ai-proxy-multi
      config:
        fallback_strategy:
          - rate_limiting
        instances:
          - name: gemini-instance
            provider: gemini
            weight: 7
            auth:
              header:
                Authorization: "Bearer AIzaSyDUMZbZmHCmJ5BNNLl0KfQk"
            options:
              model: gemini-2.5-flash
          - name: vertex-ai-instance
            provider: vertex-ai
            weight: 3
            auth:
              gcp:
                service_account_json: '{"type":"service_account","project_id":"api7-vertex","private_key_id":"...","private_key":"-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----","client_email":"api7-docs@api7-vertex.iam.gserviceaccount.com","client_id":"...","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_x509_cert_url":"https://www.googleapis.com/robot/v1/metadata/x509/api7-docs%40api7-vertex.iam.gserviceaccount.com","universe_domain":"googleapis.com"}'
            provider_conf:
              project_id: api7-vertex
              region: us-central1
            options:
              model: google/gemini-2.5-flash
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: ai-proxy-multi-route
spec:
  parentRefs:
    - name: apisix
  rules:
    - matches:
        - path:
            type: Exact
            value: /anything
          method: POST
      filters:
        - type: ExtensionRef
          extensionRef:
            group: apisix.apache.org
            kind: PluginConfig
            name: ai-proxy-multi-plugin-config
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-proxy-multi-ic.yaml
```

â¶ Configure the provider to be `gemini` for Google AI Studio Gemini access.

â· Replace with your Gemini API key in the `Authorization` header.

â¸ Specify the name of the Gemini model through Google AI Studio in the `<model>` format.

â¹ Configure the provider to be `vertex-ai` for Vertex AI Gemini access.

âº Replace with your JSON credentials. Ensure that it is a JSON-escaped string.

â» Replace with your Vertex AI project ID and region.

â¼ Specify the name of the Gemini model through Vertex AI in the `<publisher>/<model>` format.

ai-proxy-multi-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: ai-proxy-multi-route
spec:
  ingressClassName: apisix
  http:
    - name: ai-proxy-multi-route
      match:
        paths:
          - /anything
        methods:
          - POST
      plugins:
        - name: ai-proxy-multi
          enable: true
          config:
            fallback_strategy:
              - rate_limiting
            instances:
              - name: gemini-instance
                provider: gemini
                weight: 7
                auth:
                  header:
                    Authorization: "Bearer AIzaSyDUMZbZmHCmJ5BNNLl0KfQk"
                options:
                  model: gemini-2.5-flash
              - name: vertex-ai-instance
                provider: vertex-ai
                weight: 3
                auth:
                  gcp:
                    service_account_json: '{"type":"service_account","project_id":"api7-vertex","private_key_id":"...","private_key":"-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----","client_email":"api7-docs@api7-vertex.iam.gserviceaccount.com","client_id":"...","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_x509_cert_url":"https://www.googleapis.com/robot/v1/metadata/x509/api7-docs%40api7-vertex.iam.gserviceaccount.com","universe_domain":"googleapis.com"}'
                provider_conf:
                  project_id: api7-vertex
                  region: us-central1
                options:
                  model: google/gemini-2.5-flash
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-proxy-multi-ic.yaml
```

â¶ Configure the provider to be `gemini` for Google AI Studio Gemini access.

â· Replace with your Gemini API key in the `Authorization` header.

â¸ Specify the name of the Gemini model through Google AI Studio in the `<model>` format.

â¹ Configure the provider to be `vertex-ai` for Vertex AI Gemini access.

âº Replace with your JSON credentials. Ensure that it is a JSON-escaped string.

â» Replace with your Vertex AI project ID and region.

â¼ Specify the name of the Gemini model through Vertex AI in the `<publisher>/<model>` format.

Send 10 POST requests to the route to see the load balancing distribution:

```
studio_count=0
vertex_count=0

for i in {1..10}; do 
  model=$(curl -s "http://127.0.0.1:9080/anything" -X POST \
    -H "Content-Type: application/json" \
    -d '{
      "messages": [
        { "role": "system", "content": "You are a mathematician" },
        { "role": "user", "content": "What is 1+1?" }
      ]
    }' | jq -r '.model')

  if [[ "$model" == "gemini-2.5-flash" ]]; then
    ((studio_count++))
  elif [[ "$model" == "google/gemini-2.5-flash" ]]; then
    ((vertex_count++))
  fi
done

echo "Google AI Studio Gemini responses: $studio_count"
echo "Vertex AI Gemini responses: $vertex_count"
```

You should see a response similar to the following:

```
Google AI Studio Gemini responses: 7
Vertex AI Gemini responses: 3
```

### Configure Instance Priority and Rate Limiting[â](#configure-instance-priority-and-rate-limiting "Direct link to Configure Instance Priority and Rate Limiting")

The following example demonstrates how you can configure two models with different priorities and apply rate limiting on the instance with a higher priority. In the case where `fallback_strategy` is set to `["rate_limiting"]`, the plugin should continue to forward requests to the low priority instance once the high priority instance's rate limiting quota is fully consumed.

Create a route as such and update with your LLM providers, models, API keys, and endpoints if applicable:

* Admin API
* ADC
* Ingress Controller

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-proxy-multi-route",
    "uri": "/anything",
    "methods": ["POST"],
    "plugins": {
      "ai-proxy-multi": {
        "fallback_strategy": ["rate_limiting"],
        "instances": [
          {
            "name": "openai-instance",
            "provider": "openai",
            "priority": 1,
            "weight": 0,
            "auth": {
              "header": {
                "Authorization": "Bearer '"$OPENAI_API_KEY"'"
              }
            },
            "options": {
              "model": "gpt-4"
            }
          },
          {
            "name": "deepseek-instance",
            "provider": "deepseek",
            "priority": 0,
            "weight": 0,
            "auth": {
              "header": {
                "Authorization": "Bearer '"$DEEPSEEK_API_KEY"'"
              }
            },
            "options": {
              "model": "deepseek-chat"
            }
          }
        ]
      },
      "ai-rate-limiting": {
        "instances": [
          {
            "name": "openai-instance",
            "limit": 10,
            "time_window": 60
          }
        ],
        "limit_strategy": "total_tokens"
      }
    }
  }'
```

â¶ Set the `fallback_strategy` to `["rate_limiting"]`.

â· Set a higher priority on `openai-instance` instance.

â¸ Set a lower priority on `deepseek-instance` instance.

â¹ Configure a quota of 10 tokens.

âº Configure the time window to be 60 seconds.

â» Configure the `limit_strategy` to `total_tokens`.

adc.yaml

```
services:
  - name: ai-proxy-multi-service
    routes:
      - name: ai-proxy-multi-route
        uris:
          - /anything
        methods:
          - POST
        plugins:
          ai-proxy-multi:
            fallback_strategy:
              - rate_limiting
            instances:
              - name: openai-instance
                provider: openai
                priority: 1
                weight: 0
                auth:
                  header:
                    Authorization: "Bearer ${OPENAI_API_KEY}"
                options:
                  model: gpt-4
              - name: deepseek-instance
                provider: deepseek
                priority: 0
                weight: 0
                auth:
                  header:
                    Authorization: "Bearer ${DEEPSEEK_API_KEY}"
                options:
                  model: deepseek-chat
          ai-rate-limiting:
            instances:
              - name: openai-instance
                limit: 10
                time_window: 60
            limit_strategy: total_tokens
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

â¶ Set the `fallback_strategy` to `["rate_limiting"]`.

â· Set a higher priority on `openai-instance` instance.

â¸ Set a lower priority on `deepseek-instance` instance.

â¹ Configure a quota of 10 tokens.

âº Configure the time window to be 60 seconds.

â» Configure the `limit_strategy` to `total_tokens`.

* Gateway API
* APISIX CRD

ai-proxy-multi-ic.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: ai-proxy-multi-plugin-config
spec:
  plugins:
    - name: ai-proxy-multi
      config:
        fallback_strategy:
          - rate_limiting
        instances:
          - name: openai-instance
            provider: openai
            priority: 1
            weight: 0
            auth:
              header:
                Authorization: "Bearer sk-REDACTED-EXAMPLE-KEY"
            options:
              model: gpt-4
          - name: deepseek-instance
            provider: deepseek
            priority: 0
            weight: 0
            auth:
              header:
                Authorization: "Bearer sk-5e99f3e26abc40e75d80009a90e66"
            options:
              model: deepseek-chat
    - name: ai-rate-limiting
      config:
        instances:
          - name: openai-instance
            limit: 10
            time_window: 60
        limit_strategy: total_tokens
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: ai-proxy-multi-route
spec:
  parentRefs:
    - name: apisix
  rules:
    - matches:
        - path:
            type: Exact
            value: /anything
          method: POST
      filters:
        - type: ExtensionRef
          extensionRef:
            group: apisix.apache.org
            kind: PluginConfig
            name: ai-proxy-multi-plugin-config
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-proxy-multi-ic.yaml
```

â¶ Set the `fallback_strategy` to `["rate_limiting"]`.

â· Set a higher priority on `openai-instance` instance.

â¸ Set a lower priority on `deepseek-instance` instance.

â¹ Configure a quota of 10 tokens.

âº Configure the time window to be 60 seconds.

â» Configure the `limit_strategy` to `total_tokens`.

ai-proxy-multi-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: ai-proxy-multi-route
spec:
  ingressClassName: apisix
  http:
    - name: ai-proxy-multi-route
      match:
        paths:
          - /anything
        methods:
          - POST
      plugins:
        - name: ai-proxy-multi
          enable: true
          config:
            fallback_strategy:
              - rate_limiting
            instances:
              - name: openai-instance
                provider: openai
                priority: 1
                weight: 0
                auth:
                  header:
                    Authorization: "Bearer sk-REDACTED-EXAMPLE-KEY"
                options:
                  model: gpt-4
              - name: deepseek-instance
                provider: deepseek
                priority: 0
                weight: 0
                auth:
                  header:
                    Authorization: "Bearer sk-5e99f3e26abc40e75d80009a90e66"
                options:
                  model: deepseek-chat
        - name: ai-rate-limiting
          enable: true
          config:
            instances:
              - name: openai-instance
                limit: 10
                time_window: 60
            limit_strategy: total_tokens
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-proxy-multi-ic.yaml
```

â¶ Set the `fallback_strategy` to `["rate_limiting"]`.

â· Set a higher priority on `openai-instance` instance.

â¸ Set a lower priority on `deepseek-instance` instance.

â¹ Configure a quota of 10 tokens.

âº Configure the time window to be 60 seconds.

â» Configure the `limit_strategy` to `total_tokens`.

Send a POST request to the route with a system prompt and a sample user question in the request body:

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
  ...,
  "model": "gpt-4-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "1+1 equals 2.",
        "refusal": null
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 23,
    "completion_tokens": 8,
    "total_tokens": 31,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "audio_tokens": 0
    },
    "completion_tokens_details": {
      "reasoning_tokens": 0,
      "audio_tokens": 0,
      "accepted_prediction_tokens": 0,
      "rejected_prediction_tokens": 0
    }
  },
  "service_tier": "default",
  "system_fingerprint": null
}
```

Since the `total_tokens` value exceeds the configured quota of `10`, the next request within the 60-second window is expected to be forwarded to the other instance.

Within the same 60-second window, send another POST request to the route:

```
curl "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      { "role": "system", "content": "You are a mathematician" },
      { "role": "user", "content": "Explain Newton law" }
    ]
  }'
```

You should see a response similar to the following:

```
{
  ...,
  "model": "deepseek-chat",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Certainly! Newton's laws of motion are three fundamental principles that describe the relationship between the motion of an object and the forces acting on it. They were formulated by Sir Isaac Newton in the late 17th century and are foundational to classical mechanics.\n\n---\n\n### **1. Newton's First Law (Law of Inertia):**\n- **Statement:** An object at rest will remain at rest, and an object in motion will continue moving at a constant velocity (in a straight line at a constant speed), unless acted upon by an external force.\n- **Key Idea:** This law introduces the concept of **inertia**, which is the tendency of an object to resist changes in its state of motion.\n- **Example:** If you slide a book across a table, it eventually stops because of the force of friction acting on it. Without friction, the book would keep moving indefinitely.\n\n---\n\n### **2. Newton's Second Law (Law of Acceleration):**\n- **Statement:** The acceleration of an object is directly proportional to the net force acting on it and inversely proportional to its mass. Mathematically, this is expressed as:\n  \\[\n  F = ma\n  \\]\n  where:\n  - \\( F \\) = net force applied (in Newtons),\n  -"
      },
      ...
    }
  ],
  ...
}
```

### Load Balance and Rate Limit by Consumers[â](#load-balance-and-rate-limit-by-consumers "Direct link to Load Balance and Rate Limit by Consumers")

The following example demonstrates how you can configure two models for load balancing and apply rate limiting by consumer.

Create a consumer `johndoe` and a rate limiting quota of 10 tokens in a 60-second window on `openai-instance` instance:

* Admin API
* ADC
* Ingress Controller

```
curl "http://127.0.0.1:9180/apisix/admin/consumers" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "username": "johndoe",
    "plugins": {
      "ai-rate-limiting": {
        "instances": [
          {
            "name": "openai-instance",
            "limit": 10,
            "time_window": 60
          }
        ],
        "rejected_code": 429,
        "policy": "local",
        "limit_strategy": "total_tokens"
      }
    }
  }'
```

Configure `key-auth` credential for `johndoe`:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers/johndoe/credentials" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "cred-john-key-auth",
    "plugins": {
      "key-auth": {
        "key": "john-key"
      }
    }
  }'
```

Create another consumer `janedoe` and a rate limiting quota of 10 tokens in a 60-second window on `deepseek-instance` instance:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "username": "janedoe",
    "plugins": {
      "ai-rate-limiting": {
        "instances": [
          {
            "name": "deepseek-instance",
            "limit": 10,
            "time_window": 60
          }
        ],
        "rejected_code": 429,
        "policy": "local",
        "limit_strategy": "total_tokens"
      }
    }
  }'
```

Configure `key-auth` credential for `janedoe`:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers/janedoe/credentials" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "cred-jane-key-auth",
    "plugins": {
      "key-auth": {
        "key": "jane-key"
      }
    }
  }'
```

adc.yaml

```
consumers:
  - username: johndoe
    plugins:
      ai-rate-limiting:
        instances:
          - name: openai-instance
            limit: 10
            time_window: 60
        rejected_code: 429
        policy: local
        limit_strategy: total_tokens
    credentials:
      - name: key-auth
        type: key-auth
        config:
          key: john-key
  - username: janedoe
    plugins:
      ai-rate-limiting:
        instances:
          - name: deepseek-instance
            limit: 10
            time_window: 60
        rejected_code: 429
        policy: local
        limit_strategy: total_tokens
    credentials:
      - name: key-auth
        type: key-auth
        config:
          key: jane-key
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

* Gateway API
* APISIX CRD

ai-proxy-multi-consumer-ic.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: Consumer
metadata:
  namespace: aic
  name: johndoe
spec:
  gatewayRef:
    name: apisix
  plugins:
    - name: ai-rate-limiting
      config:
        instances:
          - name: openai-instance
            limit: 10
            time_window: 60
        rejected_code: 429
        policy: local
        limit_strategy: total_tokens
  credentials:
    - type: key-auth
      name: primary-key
      config:
        key: john-key
---
apiVersion: apisix.apache.org/v1alpha1
kind: Consumer
metadata:
  namespace: aic
  name: janedoe
spec:
  gatewayRef:
    name: apisix
  plugins:
    - name: ai-rate-limiting
      config:
        instances:
          - name: deepseek-instance
            limit: 10
            time_window: 60
        rejected_code: 429
        policy: local
        limit_strategy: total_tokens
  credentials:
    - type: key-auth
      name: primary-key
      config:
        key: jane-key
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-proxy-multi-consumer-ic.yaml
```

ai-proxy-multi-consumer-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixConsumer
metadata:
  namespace: aic
  name: johndoe
spec:
  ingressClassName: apisix
  authParameter:
    keyAuth:
      value:
        key: john-key
  plugins:
    ai-rate-limiting:
      instances:
        - name: openai-instance
          limit: 10
          time_window: 60
      rejected_code: 429
      policy: local
      limit_strategy: total_tokens
---
apiVersion: apisix.apache.org/v2
kind: ApisixConsumer
metadata:
  namespace: aic
  name: janedoe
spec:
  ingressClassName: apisix
  authParameter:
    keyAuth:
      value:
        key: jane-key
  plugins:
    ai-rate-limiting:
      instances:
        - name: deepseek-instance
          limit: 10
          time_window: 60
      rejected_code: 429
      policy: local
      limit_strategy: total_tokens
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-proxy-multi-consumer-ic.yaml
```

Create a route as such and update with your LLM providers, models, API keys, and endpoints if applicable:

* Admin API
* ADC
* Ingress Controller

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-proxy-multi-route",
    "uri": "/anything",
    "methods": ["POST"],
    "plugins": {
      "key-auth": {},
      "ai-proxy-multi": {
        "fallback_strategy": ["rate_limiting"],
        "instances": [
          {
            "name": "openai-instance",
            "provider": "openai",
            "weight": 0,
            "auth": {
              "header": {
                "Authorization": "Bearer '"$OPENAI_API_KEY"'"
              }
            },
            "options": {
              "model": "gpt-4"
            }
          },
          {
            "name": "deepseek-instance",
            "provider": "deepseek",
            "weight": 0,
            "auth": {
              "header": {
                "Authorization": "Bearer '"$DEEPSEEK_API_KEY"'"
              }
            },
            "options": {
              "model": "deepseek-chat"
            }
          }
        ]
      }
    }
  }'
```

â¶ Enable `key-auth` on the route.

â· Configure an `openai` instance.

â¸ Configure a `deepseek` instance.

adc.yaml

```
services:
  - name: ai-proxy-multi-service
    routes:
      - name: ai-proxy-multi-route
        uris:
          - /anything
        methods:
          - POST
        plugins:
          key-auth: {}
          ai-proxy-multi:
            fallback_strategy:
              - rate_limiting
            instances:
              - name: openai-instance
                provider: openai
                weight: 0
                auth:
                  header:
                    Authorization: "Bearer ${OPENAI_API_KEY}"
                options:
                  model: gpt-4
              - name: deepseek-instance
                provider: deepseek
                weight: 0
                auth:
                  header:
                    Authorization: "Bearer ${DEEPSEEK_API_KEY}"
                options:
                  model: deepseek-chat
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

â¶ Enable `key-auth` on the route.

â· Configure an `openai` instance.

â¸ Configure a `deepseek` instance.

* Gateway API
* APISIX CRD

ai-proxy-multi-ic.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: ai-proxy-multi-plugin-config
spec:
  plugins:
    - name: key-auth
      config:
        _meta:
          disable: false
    - name: ai-proxy-multi
      config:
        fallback_strategy:
          - rate_limiting
        instances:
          - name: openai-instance
            provider: openai
            weight: 0
            auth:
              header:
                Authorization: "Bearer sk-REDACTED-EXAMPLE-KEY"
            options:
              model: gpt-4
          - name: deepseek-instance
            provider: deepseek
            weight: 0
            auth:
              header:
                Authorization: "Bearer sk-5e99f3e26abc40e75d80009a90e66"
            options:
              model: deepseek-chat
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: ai-proxy-multi-route
spec:
  parentRefs:
    - name: apisix
  rules:
    - matches:
        - path:
            type: Exact
            value: /anything
          method: POST
      filters:
        - type: ExtensionRef
          extensionRef:
            group: apisix.apache.org
            kind: PluginConfig
            name: ai-proxy-multi-plugin-config
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-proxy-multi-ic.yaml
```

â¶ Enable `key-auth` on the route.

â· Configure an `openai` instance.

â¸ Configure a `deepseek` instance.

ai-proxy-multi-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: ai-proxy-multi-route
spec:
  ingressClassName: apisix
  http:
    - name: ai-proxy-multi-route
      match:
        paths:
          - /anything
        methods:
          - POST
      plugins:
        - name: key-auth
          enable: true
        - name: ai-proxy-multi
          enable: true
          config:
            fallback_strategy:
              - rate_limiting
            instances:
              - name: openai-instance
                provider: openai
                weight: 0
                auth:
                  header:
                    Authorization: "Bearer sk-REDACTED-EXAMPLE-KEY"
                options:
                  model: gpt-4
              - name: deepseek-instance
                provider: deepseek
                weight: 0
                auth:
                  header:
                    Authorization: "Bearer sk-5e99f3e26abc40e75d80009a90e66"
                options:
                  model: deepseek-chat
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-proxy-multi-ic.yaml
```

â¶ Enable `key-auth` on the route.

â· Configure an `openai` instance.

â¸ Configure a `deepseek` instance.

Send a POST request to the route without any consumer key:

```
curl -i "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      { "role": "system", "content": "You are a mathematician" },
      { "role": "user", "content": "What is 1+1?" }
    ]
  }'
```

You should receive an `HTTP/1.1 401 Unauthorized` response.

Send a POST request to the route with `johndoe`'s key:

```
curl "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -H 'apikey: john-key' \
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
  ...,
  "model": "gpt-4-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "1+1 equals 2.",
        "refusal": null
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 23,
    "completion_tokens": 8,
    "total_tokens": 31,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "audio_tokens": 0
    },
    "completion_tokens_details": {
      "reasoning_tokens": 0,
      "audio_tokens": 0,
      "accepted_prediction_tokens": 0,
      "rejected_prediction_tokens": 0
    }
  },
  "service_tier": "default",
  "system_fingerprint": null
}
```

Since the `total_tokens` value exceeds the configured quota of the `openai` instance for `johndoe`, the next request within the 60-second window from `johndoe` is expected to be forwarded to the `deepseek` instance.

Within the same 60-second window, send another POST request to the route with `johndoe`'s key:

```
curl "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -H 'apikey: john-key' \
  -d '{
    "messages": [
      { "role": "system", "content": "You are a mathematician" },
      { "role": "user", "content": "Explain Newtons laws to me" }
    ]
  }'
```

You should see a response similar to the following:

```
{
  ...,
  "model": "deepseek-chat",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Certainly! Newton's laws of motion are three fundamental principles that describe the relationship between the motion of an object and the forces acting on it. They were formulated by Sir Isaac Newton in the late 17th century and are foundational to classical mechanics.\n\n---\n\n### **1. Newton's First Law (Law of Inertia):**\n- **Statement:** An object at rest will remain at rest, and an object in motion will continue moving at a constant velocity (in a straight line at a constant speed), unless acted upon by an external force.\n- **Key Idea:** This law introduces the concept of **inertia**, which is the tendency of an object to resist changes in its state of motion.\n- **Example:** If you slide a book across a table, it eventually stops because of the force of friction acting on it. Without friction, the book would keep moving indefinitely.\n\n---\n\n### **2. Newton's Second Law (Law of Acceleration):**\n- **Statement:** The acceleration of an object is directly proportional to the net force acting on it and inversely proportional to its mass. Mathematically, this is expressed as:\n  \\[\n  F = ma\n  \\]\n  where:\n  - \\( F \\) = net force applied (in Newtons),\n  -"
      },
      ...
    }
  ],
  ...
}
```

Send a POST request to the route with `janedoe`'s key:

```
curl "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -H 'apikey: jane-key' \
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
  ...,
  "model": "deepseek-chat",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "The sum of 1 and 1 is 2. This is a basic arithmetic operation where you combine two units to get a total of two units."
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 14,
    "completion_tokens": 31,
    "total_tokens": 45,
    "prompt_tokens_details": {
      "cached_tokens": 0
    },
    "prompt_cache_hit_tokens": 0,
    "prompt_cache_miss_tokens": 14
  },
  "system_fingerprint": "fp_3a5770e1b4_prod0225"
}
```

Since the `total_tokens` value exceeds the configured quota of the `deepseek` instance for `janedoe`, the next request within the 60-second window from `janedoe` is expected to be forwarded to the `openai` instance.

Within the same 60-second window, send another POST request to the route with `janedoe`'s key:

```
curl "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -H 'apikey: jane-key' \
  -d '{
    "messages": [
      { "role": "system", "content": "You are a mathematician" },
      { "role": "user", "content": "Explain Newtons laws to me" }
    ]
  }'
```

You should see a response similar to the following:

```
{
  ...,
  "model": "gpt-4-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Sure, here are Newton's three laws of motion:\n\n1) Newton's First Law, also known as the Law of Inertia, states that an object at rest will stay at rest, and an object in motion will stay in motion, unless acted on by an external force. In simple words, this law suggests that an object will keep doing whatever it is doing until something causes it to do otherwise. \n\n2) Newton's Second Law states that the force acting on an object is equal to the mass of that object times its acceleration (F=ma). This means that force is directly proportional to mass and acceleration. The heavier the object and the faster it accelerates, the greater the force.\n\n3) Newton's Third Law, also known as the law of action and reaction, states that for every action, there is an equal and opposite reaction. Essentially, any force exerted onto a body will create a force of equal magnitude but in the opposite direction on the object that exerted the first force.\n\nRemember, these laws become less accurate when considering speeds near the speed of light (where Einstein's theory of relativity becomes more appropriate) or objects very small or very large. However, for everyday situations, they provide a good model of how things move.",
        "refusal": null
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  ...
}
```

This shows `ai-proxy-multi` load balance the traffic with respect to the rate limiting rules in `ai-rate-limiting` by consumers.

### Restrict Maximum Number of Completion Tokens[â](#restrict-maximum-number-of-completion-tokens "Direct link to Restrict Maximum Number of Completion Tokens")

The following example demonstrates how you can restrict the number of `completion_tokens` used when generating the chat completion.

For demonstration and easier differentiation, you will be configuring one OpenAI instance and one DeepSeek instance as the upstream LLM services.

Create a route as such and update with your LLM providers, models, API keys, and endpoints if applicable:

* Admin API
* ADC
* Ingress Controller

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-proxy-multi-route",
    "uri": "/anything",
    "methods": ["POST"],
    "plugins": {
      "ai-proxy-multi": {
        "instances": [
          {
            "name": "openai-instance",
            "provider": "openai",
            "weight": 0,
            "auth": {
              "header": {
                "Authorization": "Bearer '"$OPENAI_API_KEY"'"
              }
            },
            "options": {
              "model": "gpt-4",
              "max_tokens": 50
            }
          },
          {
            "name": "deepseek-instance",
            "provider": "deepseek",
            "weight": 0,
            "auth": {
              "header": {
                "Authorization": "Bearer '"$DEEPSEEK_API_KEY"'"
              }
            },
            "options": {
              "model": "deepseek-chat",
              "max_tokens": 100
            }
          }
        ]
      }
    }
  }'
```

â¶ Configure the `max_tokens` for the OpenAI instance to be `50`.

â· Configure the `max_tokens` for the DeepSeek instance to be `100`.

adc.yaml

```
services:
  - name: ai-proxy-multi-service
    routes:
      - name: ai-proxy-multi-route
        uris:
          - /anything
        methods:
          - POST
        plugins:
          ai-proxy-multi:
            instances:
              - name: openai-instance
                provider: openai
                weight: 0
                auth:
                  header:
                    Authorization: "Bearer ${OPENAI_API_KEY}"
                options:
                  model: gpt-4
                  max_tokens: 50
              - name: deepseek-instance
                provider: deepseek
                weight: 0
                auth:
                  header:
                    Authorization: "Bearer ${DEEPSEEK_API_KEY}"
                options:
                  model: deepseek-chat
                  max_tokens: 100
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

â¶ Configure the `max_tokens` for the OpenAI instance to be `50`.

â· Configure the `max_tokens` for the DeepSeek instance to be `100`.

* Gateway API
* APISIX CRD

ai-proxy-multi-ic.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: ai-proxy-multi-plugin-config
spec:
  plugins:
    - name: ai-proxy-multi
      config:
        instances:
          - name: openai-instance
            provider: openai
            weight: 0
            auth:
              header:
                Authorization: "Bearer sk-REDACTED-EXAMPLE-KEY"
            options:
              model: gpt-4
              max_tokens: 50
          - name: deepseek-instance
            provider: deepseek
            weight: 0
            auth:
              header:
                Authorization: "Bearer sk-5e99f3e26abc40e75d80009a90e66"
            options:
              model: deepseek-chat
              max_tokens: 100
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: ai-proxy-multi-route
spec:
  parentRefs:
    - name: apisix
  rules:
    - matches:
        - path:
            type: Exact
            value: /anything
          method: POST
      filters:
        - type: ExtensionRef
          extensionRef:
            group: apisix.apache.org
            kind: PluginConfig
            name: ai-proxy-multi-plugin-config
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-proxy-multi-ic.yaml
```

â¶ Configure the `max_tokens` for the OpenAI instance to be `50`.

â· Configure the `max_tokens` for the DeepSeek instance to be `100`.

ai-proxy-multi-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: ai-proxy-multi-route
spec:
  ingressClassName: apisix
  http:
    - name: ai-proxy-multi-route
      match:
        paths:
          - /anything
        methods:
          - POST
      plugins:
        - name: ai-proxy-multi
          enable: true
          config:
            instances:
              - name: openai-instance
                provider: openai
                weight: 0
                auth:
                  header:
                    Authorization: "Bearer sk-REDACTED-EXAMPLE-KEY"
                options:
                  model: gpt-4
                  max_tokens: 50
              - name: deepseek-instance
                provider: deepseek
                weight: 0
                auth:
                  header:
                    Authorization: "Bearer sk-5e99f3e26abc40e75d80009a90e66"
                options:
                  model: deepseek-chat
                  max_tokens: 100
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-proxy-multi-ic.yaml
```

â¶ Configure the `max_tokens` for the OpenAI instance to be `50`.

â· Configure the `max_tokens` for the DeepSeek instance to be `100`.

Send a POST request to the route with a system prompt and a sample user question in the request body:

```
curl "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      { "role": "system", "content": "You are a mathematician" },
      { "role": "user", "content": "Explain Newtons law" }
    ]
  }'
```

If the request is proxied to OpenAI, you should see a response similar to the following, where the content is truncated per 50 `max_tokens` threshold:

```
{
  ...,
  "model": "gpt-4-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Newton's Laws of Motion are three physical laws that form the bedrock for classical mechanics. They describe the relationship between a body and the forces acting upon it, and the body's motion in response to those forces. \n\n1. Newton's First Law",
        "refusal": null
      },
      "logprobs": null,
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 20,
    "completion_tokens": 50,
    "total_tokens": 70,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "audio_tokens": 0
    },
    "completion_tokens_details": {
      "reasoning_tokens": 0,
      "audio_tokens": 0,
      "accepted_prediction_tokens": 0,
      "rejected_prediction_tokens": 0
    }
  },
  "service_tier": "default",
  "system_fingerprint": null
}
```

If the request is proxied to DeepSeek, you should see a response similar to the following, where the content is truncated per 100 `max_tokens` threshold:

```
{
  ...,
  "model": "deepseek-chat",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Newton's Laws of Motion are three fundamental principles that form the foundation of classical mechanics. They describe the relationship between a body and the forces acting upon it, and the body's motion in response to those forces. Here's a brief explanation of each law:\n\n1. **Newton's First Law (Law of Inertia):**\n   - **Statement:** An object will remain at rest or in uniform motion in a straight line unless acted upon by an external force.\n   - **Explanation:** This law"
      },
      "logprobs": null,
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 10,
    "completion_tokens": 100,
    "total_tokens": 110,
    "prompt_tokens_details": {
      "cached_tokens": 0
    },
    "prompt_cache_hit_tokens": 0,
    "prompt_cache_miss_tokens": 10
  },
  "system_fingerprint": "fp_3a5770e1b4_prod0225"
}
```

### Proxy to Embedding Models[â](#proxy-to-embedding-models "Direct link to Proxy to Embedding Models")

The following example demonstrates how you can configure the `ai-proxy-multi` plugin to proxy requests and load balance between embedding models.

Create a route as such and update with your LLM providers, embedding models, API keys, and endpoints:

* Admin API
* ADC
* Ingress Controller

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-proxy-multi-route",
    "uri": "/anything",
    "methods": ["POST"],
    "plugins": {
      "ai-proxy-multi": {
        "instances": [
          {
            "name": "openai-instance",
            "provider": "openai",
            "weight": 0,
            "auth": {
              "header": {
                "Authorization": "Bearer '"$OPENAI_API_KEY"'"
              }
            },
            "options": {
              "model": "text-embedding-3-small"
            },
            "override": {
              "endpoint": "https://api.openai.com/v1/embeddings"
            }
          },
          {
            "name": "az-openai-instance",
            "provider": "azure-openai",
            "weight": 0,
            "auth": {
              "header": {
                "Authorization": "Bearer '"$AZ_OPENAI_API_KEY"'"
              }
            },
            "options": {
              "model": "text-embedding-3-small"
            },
            "override": {
              "endpoint": "https://ai-plugin-developer.openai.azure.com/openai/deployments/text-embedding-3-small/embeddings?api-version=2023-05-15"
            }
          }
        ]
      }
    }
  }'
```

â¶ Specify the name of the embedding model.

â· Override the default OpenAI endpoint with the embedding API endpoint.

â¸ Specify the name of the embedding model.

â¹ Specify the Azure embedding API endpoint.

adc.yaml

```
services:
  - name: ai-proxy-multi-service
    routes:
      - name: ai-proxy-multi-route
        uris:
          - /anything
        methods:
          - POST
        plugins:
          ai-proxy-multi:
            instances:
              - name: openai-instance
                provider: openai
                weight: 0
                auth:
                  header:
                    Authorization: "Bearer ${OPENAI_API_KEY}"
                options:
                  model: text-embedding-3-small
                override:
                  endpoint: "https://api.openai.com/v1/embeddings"
              - name: az-openai-instance
                provider: azure-openai
                weight: 0
                auth:
                  header:
                    api-key: "${AZ_OPENAI_API_KEY}"
                options:
                  model: text-embedding-3-small
                override:
                  endpoint: "https://ai-plugin-developer.openai.azure.com/openai/deployments/text-embedding-3-small/embeddings?api-version=2023-05-15"
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

â¶ Specify the name of the embedding model.

â· Override the default OpenAI endpoint with the embedding API endpoint.

â¸ Specify the name of the embedding model.

â¹ Specify the Azure embedding API endpoint.

* Gateway API
* APISIX CRD

ai-proxy-multi-ic.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: ai-proxy-multi-plugin-config
spec:
  plugins:
    - name: ai-proxy-multi
      config:
        instances:
          - name: openai-instance
            provider: openai
            weight: 0
            auth:
              header:
                Authorization: "Bearer sk-xxxxxxxxxxxxxxxx"
            options:
              model: text-embedding-3-small
            override:
              endpoint: "https://api.openai.com/v1/embeddings"
          - name: az-openai-instance
            provider: azure-openai
            weight: 0
            auth:
              header:
                api-key: "xxxxxxxxxxxxxxxx"
            options:
              model: text-embedding-3-small
            override:
              endpoint: "https://ai-plugin-developer.openai.azure.com/openai/deployments/text-embedding-3-small/embeddings?api-version=2023-05-15"
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: ai-proxy-multi-route
spec:
  parentRefs:
    - name: apisix
  rules:
    - matches:
        - path:
            type: Exact
            value: /anything
          method: POST
      filters:
        - type: ExtensionRef
          extensionRef:
            group: apisix.apache.org
            kind: PluginConfig
            name: ai-proxy-multi-plugin-config
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-proxy-multi-ic.yaml
```

â¶ Specify the name of the embedding model.

â· Override the default OpenAI endpoint with the embedding API endpoint.

â¸ Specify the name of the embedding model.

â¹ Specify the Azure embedding API endpoint.

ai-proxy-multi-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: ai-proxy-multi-route
spec:
  ingressClassName: apisix
  http:
    - name: ai-proxy-multi-route
      match:
        paths:
          - /anything
        methods:
          - POST
      plugins:
        - name: ai-proxy-multi
          enable: true
          config:
            instances:
              - name: openai-instance
                provider: openai
                weight: 0
                auth:
                  header:
                    Authorization: "Bearer sk-xxxxxxxxxxxxxxxx"
                options:
                  model: text-embedding-3-small
                override:
                  endpoint: "https://api.openai.com/v1/embeddings"
              - name: az-openai-instance
                provider: azure-openai
                weight: 0
                auth:
                  header:
                    api-key: "xxxxxxxxxxxxxxxx"
                options:
                  model: text-embedding-3-small
                override:
                  endpoint: "https://ai-plugin-developer.openai.azure.com/openai/deployments/text-embedding-3-small/embeddings?api-version=2023-05-15"
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-proxy-multi-ic.yaml
```

â¶ Specify the name of the embedding model.

â· Override the default OpenAI endpoint with the embedding API endpoint.

â¸ Specify the name of the embedding model.

â¹ Specify the Azure embedding API endpoint.

Send a POST request to the route with an input string:

```
curl "http://127.0.0.1:9080/embeddings" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "input": "hello world"
  }'
```

You should receive a response similar to the following:

```
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "index": 0,
      "embedding": [
        -0.0067144386,
        -0.039197803,
        0.034177095,
        0.028763203,
        -0.024785956,
        -0.04201061,
        ...
      ],
    }
  ],
  "model": "text-embedding-3-small",
  "usage": {
    "prompt_tokens": 2,
    "total_tokens": 2
  }
}
```

### Enable Active Health Checks[â](#enable-active-health-checks "Direct link to Enable Active Health Checks")

The following example demonstrates how you can configure the `ai-proxy-multi` plugin to proxy requests and load balance between models, and enable active health check to improve service availability. You can enable health check on one or multiple instances.

Create a route as such and update the LLM providers, embedding models, API keys, and health check related configurations:

* Admin API
* ADC
* Ingress Controller

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-proxy-multi-route",
    "uri": "/anything",
    "methods": ["POST"],
    "plugins": {
      "ai-proxy-multi": {
        "instances": [
          {
            "name": "llm-instance-1",
            "provider": "openai-compatible",
            "weight": 0,
            "auth": {
              "header": {
                "Authorization": "Bearer '"$YOUR_LLM_API_KEY"'"
              }
            },
            "options": {
              "model": "'"$YOUR_LLM_MODEL"'"
            }
          },
          {
            "name": "llm-instance-2",
            "provider": "openai-compatible",
            "weight": 0,
            "auth": {
              "header": {
                "Authorization": "Bearer '"$YOUR_LLM_API_KEY"'"
              }
            },
            "options": {
              "model": "'"$YOUR_LLM_MODEL"'"
            },
            "checks": {
              "active": {
                "type": "https",
                "host": "yourhost.com",
                "http_path": "/your/probe/path",
                "healthy": {
                  "interval": 2,
                  "successes": 1
                },
                "unhealthy": {
                  "interval": 1,
                  "http_failures": 3
                }
              }
            }
          }
        ]
      }
    }
  }'
```

â¶ Update the type of active health checks.

â· Update the host, if available.

â¸ Update the probing path.

â¹ Configure the time interval in seconds for periodically checking healthy nodes.

âº Configure the success count threshold for ruling if an upstream node is healthy.

â» Configure the time interval in seconds for periodically checking unhealthy nodes.

â¼ Configure the timeout count threshold for ruling if an upstream node is unhealthy.

adc.yaml

```
services:
  - name: ai-proxy-multi-service
    routes:
      - name: ai-proxy-multi-route
        uris:
          - /anything
        methods:
          - POST
        plugins:
          ai-proxy-multi:
            instances:
              - name: llm-instance-1
                provider: openai-compatible
                weight: 0
                auth:
                  header:
                    Authorization: "Bearer ${YOUR_LLM_API_KEY}"
                options:
                  model: "${YOUR_LLM_MODEL}"
              - name: llm-instance-2
                provider: openai-compatible
                weight: 0
                auth:
                  header:
                    Authorization: "Bearer ${YOUR_LLM_API_KEY}"
                options:
                  model: "${YOUR_LLM_MODEL}"
                checks:
                  active:
                    type: https
                    host: yourhost.com
                    http_path: /your/probe/path
                    healthy:
                      interval: 2
                      successes: 1
                    unhealthy:
                      interval: 1
                      http_failures: 3
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

â¶ Update the type of active health checks.

â· Update the host, if available.

â¸ Update the probing path.

â¹ Configure the time interval in seconds for periodically checking healthy nodes.

âº Configure the success count threshold for ruling if an upstream node is healthy.

â» Configure the time interval in seconds for periodically checking unhealthy nodes.

â¼ Configure the timeout count threshold for ruling if an upstream node is unhealthy.

* Gateway API
* APISIX CRD

ai-proxy-multi-ic.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: ai-proxy-multi-plugin-config
spec:
  plugins:
    - name: ai-proxy-multi
      config:
        instances:
          - name: llm-instance-1
            provider: openai-compatible
            weight: 0
            auth:
              header:
                Authorization: "Bearer xxxxxxxxxxxxxxxxxxx"
            options:
              model: your-model
          - name: llm-instance-2
            provider: openai-compatible
            weight: 0
            auth:
              header:
                Authorization: "Bearer xxxxxxxxxxxxxxxxxxx"
            options:
              model: your-model
            checks:
              active:
                type: https
                host: yourhost.com
                http_path: /your/probe/path
                healthy:
                  interval: 2
                  successes: 1
                unhealthy:
                  interval: 1
                  http_failures: 3
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: ai-proxy-multi-route
spec:
  parentRefs:
    - name: apisix
  rules:
    - matches:
        - path:
            type: Exact
            value: /anything
          method: POST
      filters:
        - type: ExtensionRef
          extensionRef:
            group: apisix.apache.org
            kind: PluginConfig
            name: ai-proxy-multi-plugin-config
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-proxy-multi-ic.yaml
```

â¶ Update the type of active health checks.

â· Update the host, if available.

â¸ Update the probing path.

â¹ Configure the time interval in seconds for periodically checking healthy nodes.

âº Configure the success count threshold for ruling if an upstream node is healthy.

â» Configure the time interval in seconds for periodically checking unhealthy nodes.

â¼ Configure the timeout count threshold for ruling if an upstream node is unhealthy.

ai-proxy-multi-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: ai-proxy-multi-route
spec:
  ingressClassName: apisix
  http:
    - name: ai-proxy-multi-route
      match:
        paths:
          - /anything
        methods:
          - POST
      plugins:
        - name: ai-proxy-multi
          enable: true
          config:
            instances:
              - name: llm-instance-1
                provider: openai-compatible
                weight: 0
                auth:
                  header:
                    Authorization: "Bearer xxxxxxxxxxxxxxxxxxx"
                options:
                  model: your-model
              - name: llm-instance-2
                provider: openai-compatible
                weight: 0
                auth:
                  header:
                    Authorization: "Bearer xxxxxxxxxxxxxxxxxxx"
                options:
                  model: your-model
                checks:
                  active:
                    type: https
                    host: yourhost.com
                    http_path: /your/probe/path
                    healthy:
                      interval: 2
                      successes: 1
                    unhealthy:
                      interval: 1
                      http_failures: 3
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-proxy-multi-ic.yaml
```

â¶ Update the type of active health checks.

â· Update the host, if available.

â¸ Update the probing path.

â¹ Configure the time interval in seconds for periodically checking healthy nodes.

âº Configure the success count threshold for ruling if an upstream node is healthy.

â» Configure the time interval in seconds for periodically checking unhealthy nodes.

â¼ Configure the timeout count threshold for ruling if an upstream node is unhealthy.

For verification, the behaviours should be consistent with the verification in [Active Health Checks](https://docs.api7.ai/apisix/how-to-guide/traffic-management/health-check.md#configure-active-health-checks).

### Include LLM Information in Access Log[â](#include-llm-information-in-access-log "Direct link to Include LLM Information in Access Log")

The following example demonstrates how you can log LLM request related information in the gateway's access log to improve analytics and audit. In addition to NGINX variables, the following variables are also available:

* `apisix_upstream_response_time`: Time taken for APISIX to send the request to the upstream service and receive the full response. Available from API7 Enterprise 3.8.8.
* `request_type`: Type of request, where the value could be `traditional_http`, `ai_chat`, or `ai_stream`.
* `llm_time_to_first_token`: Duration from request sending to the first token received from the LLM service, in milliseconds.
* `llm_model`: LLM model name forwarded to the upstream LLM service.
* `request_llm_model`: LLM model name specified in the request.
* `llm_prompt_tokens`: Number of tokens in the prompt.
* `llm_completion_tokens`: Number of chat completion tokens in the prompt.

tip

These variables are demonstrated in the access log format but are also available for use in logging plugins.

Update the access log format in your [configuration file](https://docs.api7.ai/enterprise/reference/configuration.md) to include additional LLM related variables:

conf/config.yaml

```
nginx_config:
  http:
    access_log_format: "$remote_addr - $remote_user [$time_local] $http_host \"$request_line\" $status $body_bytes_sent $request_time \"$http_referer\" \"$http_user_agent\" $upstream_addr $upstream_status $apisix_upstream_response_time \"$upstream_scheme://$upstream_host$upstream_uri\" \"$apisix_request_id\" \"$request_type\" \"$llm_time_to_first_token\" \"$llm_model\" \"$request_llm_model\" \"$llm_prompt_tokens\" \"$llm_completion_tokens\""
```

[Reload the gateway](https://docs.api7.ai/apisix/reference/apisix-cli.md#apisix-reload) for configuration changes to take effect.

Next, create a route with the `ai-proxy-multi` plugin following the previous examples and send a request. For instance, if you send a request like this:

```
curl "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-3.5",
    "messages": [
      { "role": "system", "content": "You are a mathematician" },
      { "role": "user", "content": "What is 1+1?" }
    ]
  }'
```

If the LLM instance model in `ai-proxy-multi` is `gpt-4`, then the request will be forwarded to GPT-4 model and you will receive a response similar to the following:

```
{
  ...,
  "model": "gpt-4-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "1+1 equals 2.",
        "refusal": null,
        "annotations": []
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 23,
    "completion_tokens": 8,
    "total_tokens": 31,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "audio_tokens": 0
    },
    ...
  },
  "service_tier": "default",
  "system_fingerprint": null
}
```

In the gateway's access log, you should see a log entry similar to the following:

```
192.168.215.1 - - [29/Aug/2025:09:54:16 +0000] 127.0.0.1:9080 "POST /anything HTTP/1.1" 200 808 2.670 "-" "curl/8.6.0" - - 2670 "http://127.0.0.1:9080" "6526bf5c961b6e6bb8cfcb66486f02dc" "ai_chat" "2670" "gpt-4" "gpt-3.5" "23" "7"
```

The access log entry shows the APISIX upstream response time as `2.670` seconds, the request type as `ai_chat`, time to first token as `2670` milliseconds, the LLM model that the request was forwarded to as `gpt-4`, the request LLM model as `gpt-3.5`, with prompt token usage of `23` and completion token usage of `7`.

### Send Request Log to Logger[â](#send-request-log-to-logger "Direct link to Send Request Log to Logger")

The following example demonstrates how you can log request and request information, including LLM model, token, and payload, and push them to a logger. Before proceeding, you should first set up a logger, such as Kafka. See [`kafka-logger`](https://docs.api7.ai/hub/kafka-logger.md) for more information.

Create a route to your LLM services and configure logging details as such:

* Admin API
* ADC
* Ingress Controller

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-proxy-multi-route",
    "uri": "/anything",
    "methods": ["POST"],
    "plugins": {
      "ai-proxy-multi": {
        "instances": [
          {
            "name": "openai-instance",
            "provider": "openai",
            "weight": 8,
            "auth": {
              "header": {
                "Authorization": "Bearer '"$OPENAI_API_KEY"'"
              }
            },
            "options": {
              "model": "gpt-4"
            }
          },
          {
            "name": "deepseek-instance",
            "provider": "deepseek",
            "weight": 2,
            "auth": {
              "header": {
                "Authorization": "Bearer '"$DEEPSEEK_API_KEY"'"
              }
            },
            "options": {
              "model": "deepseek-chat"
            }
          }
        ],
        "logging": {
          "summaries": true,
          "payloads": true
        }
      },
      "kafka-logger": {
        "brokers": [
          {
            "host": "127.0.0.1",
            "port": 9092
          }
        ],
        "kafka_topic": "test2",
        "key": "key1",
        "batch_max_size": 1
        }
      }
    }
  }'
```

â¶ Log request LLM model, duration, request and response tokens.

â· Log request and response payload.

â¸ Update with your Kafka address.

â¹ Update with your Kafka topic.

âº Update with your Kafka key.

â» Set to 1 to send the log entry immediately.

adc.yaml

```
services:
  - name: ai-proxy-multi-service
    routes:
      - name: ai-proxy-multi-route
        uris:
          - /anything
        methods:
          - POST
        plugins:
          ai-proxy-multi:
            instances:
              - name: openai-instance
                provider: openai
                weight: 8
                auth:
                  header:
                    Authorization: "Bearer ${OPENAI_API_KEY}"
                options:
                  model: gpt-4
              - name: deepseek-instance
                provider: deepseek
                weight: 2
                auth:
                  header:
                    Authorization: "Bearer ${DEEPSEEK_API_KEY}"
                options:
                  model: deepseek-chat
            logging:
              summaries: true
              payloads: true
          kafka-logger:
            brokers:
              - host: 127.0.0.1
                port: 9092
            kafka_topic: test2
            key: key1
            batch_max_size: 1
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

â¶ Log request LLM model, duration, request and response tokens.

â· Log request and response payload.

â¸ Update with your Kafka address.

â¹ Update with your Kafka topic.

âº Update with your Kafka key.

â» Set to 1 to send the log entry immediately.

* Gateway API
* APISIX CRD

ai-proxy-multi-ic.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: ai-proxy-multi-plugin-config
spec:
  plugins:
    - name: ai-proxy-multi
      config:
        instances:
          - name: openai-instance
            provider: openai
            weight: 8
            auth:
              header:
                Authorization: "Bearer sk-REDACTED-EXAMPLE-KEY"
            options:
              model: gpt-4
          - name: deepseek-instance
            provider: deepseek
            weight: 2
            auth:
              header:
                Authorization: "Bearer sk-5e99f3e26abc40e75d80009a90e66"
            options:
              model: deepseek-chat
        logging:
          summaries: true
          payloads: true
    - name: kafka-logger
      config:
        brokers:
          - host: kafka.aic.svc.cluster.local
            port: 9092
        kafka_topic: test2
        key: key1
        batch_max_size: 1
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: ai-proxy-multi-route
spec:
  parentRefs:
    - name: apisix
  rules:
    - matches:
        - path:
            type: Exact
            value: /anything
          method: POST
      filters:
        - type: ExtensionRef
          extensionRef:
            group: apisix.apache.org
            kind: PluginConfig
            name: ai-proxy-multi-plugin-config
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-proxy-multi-ic.yaml
```

â¶ Log request LLM model, duration, request and response tokens.

â· Log request and response payload.

â¸ Update with your Kafka topic.

â¹ Update with your Kafka key.

âº Set `batch_max_size` to 1.

ai-proxy-multi-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: ai-proxy-multi-route
spec:
  ingressClassName: apisix
  http:
    - name: ai-proxy-multi-route
      match:
        paths:
          - /anything
        methods:
          - POST
      plugins:
        - name: ai-proxy-multi
          enable: true
          config:
            instances:
              - name: openai-instance
                provider: openai
                weight: 8
                auth:
                  header:
                    Authorization: "Bearer sk-REDACTED-EXAMPLE-KEY"
                options:
                  model: gpt-4
              - name: deepseek-instance
                provider: deepseek
                weight: 2
                auth:
                  header:
                    Authorization: "Bearer sk-5e99f3e26abc40e75d80009a90e66"
                options:
                  model: deepseek-chat
            logging:
              summaries: true
              payloads: true
        - name: kafka-logger
          enable: true
          config:
            brokers:
              - host: kafka.aic.svc.cluster.local
                port: 9092
            kafka_topic: test2
            key: key1
            batch_max_size: 1
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-proxy-multi-ic.yaml
```

â¶ Log request LLM model, duration, request and response tokens.

â· Log request and response payload.

â¸ Update with your Kafka topic.

â¹ Update with your Kafka key.

âº Set to 1 to send the log entry immediately.

Send a POST request to the route:

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

You should receive a response similar to the following if the request is forwarded to OpenAI:

```
{
  ...,
  "model": "gpt-4-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "1+1 equals 2.",
        "refusal": null
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  ...
}
```

In the Kafka topic, you should also see a log entry corresponding to the request with the LLM summary and request/response payload.
