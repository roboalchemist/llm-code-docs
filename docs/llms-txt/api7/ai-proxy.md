# Source: https://docs.api7.ai/hub/ai-proxy.md

# ai-proxy

The `ai-proxy` plugin simplifies access to LLM and embedding models by transforming plugin configurations into the designated request format. It supports the integration with OpenAI, DeepSeek, Anthropic, Gemini, Vertex AI, and other OpenAI-compatible APIs.

In addition, the plugin also supports logging LLM request information in the access log, such as token usage, model, time to the first response, and more.

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can configure `ai-proxy` for different scenarios.

### Proxy to OpenAI[â](#proxy-to-openai "Direct link to Proxy to OpenAI")

The following example demonstrates how you can configure the API key, model, and other parameters in the `ai-proxy` plugin and configure the plugin on a route to proxy user prompts to OpenAI.

Obtain the OpenAI [API key](https://openai.com/blog/openai-api) and optionally save it to an environment variable:

```
export OPENAI_API_KEY=sk-REDACTED-EXAMPLE-KEY   # replace with your API key
```

* Admin API
* ADC
* Ingress Controller

Create a route and configure the `ai-proxy` plugin as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-proxy-route",
    "uri": "/anything",
    "methods": ["POST"],
    "plugins": {
      "ai-proxy": {
        "provider": "openai",
        "auth": {
          "header": {
            "Authorization": "Bearer '"$OPENAI_API_KEY"'"
          }
        },
        "options":{
          "model": "gpt-4"
        }
      }
    }
  }'
```

â¶ Specify the provider to be `openai`.

â· Attach OpenAI API key in the `Authorization` header.

â¸ Specify the name of the model.

Create a route with the `ai-proxy` plugin configured as such:

adc.yaml

```
services:
  - name: openai-service
    routes:
      - name: openai-route
        uris:
          - /anything
        methods:
          - POST
        plugins:
          ai-proxy:
            provider: openai
            auth:
              header:
                Authorization: "Bearer ${OPENAI_API_KEY}"
            options:
              model: gpt-4
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

â¶ Specify the provider to be `openai`.

â· Attach OpenAI API key in the `Authorization` header.

â¸ Specify the name of the model.

* Gateway API
* APISIX CRD

ai-proxy-ic.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: ai-proxy-plugin-config
spec:
  plugins:
    - name: ai-proxy
      config:
        provider: openai
        auth:
          header:
            Authorization: "Bearer sk-REDACTED-EXAMPLE-KEY"
        options:
          model: gpt-4
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: openai-route
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
            name: ai-proxy-plugin-config
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-proxy-ic.yaml
```

â¶ Specify the provider to be `openai`.

â· Attach OpenAI API key in the `Authorization` header.

â¸ Specify the name of the model.

ai-proxy-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: openai-route
spec:
  ingressClassName: apisix
  http:
    - name: openai-route
      match:
        paths:
          - /anything
        methods:
          - POST
      plugins:
      - name: ai-proxy
        enable: true
        config:
          provider: openai
          auth:
            header:
              Authorization: "Bearer sk-REDACTED-EXAMPLE-KEY"
          options:
            model: gpt-4
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-proxy-ic.yaml
```

â¶ Specify the provider to be `openai`.

â· Attach OpenAI API key in the `Authorization` header.

â¸ Specify the name of the model.

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
  ...
}
```

### Proxy to DeepSeek[â](#proxy-to-deepseek "Direct link to Proxy to DeepSeek")

The following example demonstrates how you can configure the `ai-proxy` plugin to proxy requests to DeepSeek.

Obtain the DeepSeek API key and optionally save it to an environment variable:

```
export DEEPSEEK_API_KEY=sk-5e99f3e26abc40e75d80009a90e66   # replace with your API key
```

* Admin API
* ADC
* Ingress Controller

Create a route and configure the `ai-proxy` plugin as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-proxy-route",
    "uri": "/anything",
    "methods": ["POST"],
    "plugins": {
      "ai-proxy": {
        "provider": "deepseek",
        "auth": {
          "header": {
            "Authorization": "Bearer '"$DEEPSEEK_API_KEY"'"
          }
        },
        "options": {
          "model": "deepseek-chat"
        }
      }
    }
  }'
```

â¶ Specify the provider to be `deepseek`, so that the plugin will proxy requests to `https://api.deepseek.com/chat/completions`.

â· Attach DeepSeek API key in the `Authorization` header.

â¸ Specify the name of the model.

Create a route with the `ai-proxy` plugin configured as such:

adc.yaml

```
services:
  - name: deepseek-service
    routes:
      - name: deepseek-route
        uris:
          - /anything
        methods:
          - POST
        plugins:
          ai-proxy:
            provider: deepseek
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

â¶ Specify the provider to be `deepseek`, so that the plugin will proxy requests to `https://api.deepseek.com/chat/completions`.

â· Attach DeepSeek API key in the `Authorization` header.

â¸ Specify the name of the model.

* Gateway API
* APISIX CRD

deepseek-ic.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: ai-proxy-plugin-config
spec:
  plugins:
    - name: ai-proxy
      config:
        provider: deepseek
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
  name: deepseek-route
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
            name: ai-proxy-plugin-config
```

Apply the configuration to your cluster:

```
kubectl apply -f deepseek-ic.yaml
```

â¶ Specify the provider to be `deepseek`, so that the plugin will proxy requests to `https://api.deepseek.com/chat/completions`.

â· Attach DeepSeek API key in the `Authorization` header.

â¸ Specify the name of the model.

deepseek-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: deepseek-route
spec:
  ingressClassName: apisix
  http:
    - name: deepseek-route
      match:
        paths:
          - /anything
        methods:
          - POST
      plugins:
      - name: ai-proxy
        enable: true
        config:
          provider: deepseek
          auth:
            header:
              Authorization: "Bearer sk-5e99f3e26abc40e75d80009a90e66"
          options:
            model: deepseek-chat
```

Apply the configuration to your cluster:

```
kubectl apply -f deepseek-ic.yaml
```

â¶ Specify the provider to be `deepseek`, so that the plugin will proxy requests to `https://api.deepseek.com/chat/completions`.

â· Attach DeepSeek API key in the `Authorization` header.

â¸ Specify the name of the model.

Send a POST request to the route with a sample question in the request body:

```
curl "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {
        "role": "system",
        "content": "You are an AI assistant that helps people find information."
      },
      {
        "role": "user",
        "content": "Write me a 50-word introduction for Apache APISIX."
      }
    ]
  }'
```

You should receive a response similar to the following:

```
{
  ...
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Apache APISIX is a dynamic, real-time, high-performance API gateway and cloud-native platform. It provides rich traffic management features like load balancing, dynamic upstream, canary release, circuit breaking, authentication, observability, and more. Designed for microservices and serverless architectures, APISIX ensures scalability, security, and seamless integration with modern DevOps workflows."
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  ...
}
```

### Proxy to Azure OpenAI[â](#proxy-to-azure-openai "Direct link to Proxy to Azure OpenAI")

The following example demonstrates how you can configure the `ai-proxy` plugin to proxy requests to other LLM services, such as Azure OpenAI.

Obtain the Azure OpenAI API key and optionally save it to an environment variable:

```
export AZ_OPENAI_API_KEY=57cha9ee8e8a89a12c0aha174f180f4   # replace with your API key
```

* Admin API
* ADC
* Ingress Controller

Create a route and configure the `ai-proxy` plugin as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-proxy-route",
    "uri": "/anything",
    "methods": ["POST"],
    "plugins": {
      "ai-proxy": {
        "provider": "azure-openai",
        "auth": {
          "header": {
            "api-key": "'"$AZ_OPENAI_API_KEY"'"
          }
        },
        "options":{
          "model": "gpt-4"
        },
        "override": {
          "endpoint": "https://api7-azure-openai.openai.azure.com/openai/deployments/gpt-4/chat/completions?api-version=2024-02-15-preview"
        }
      }
    }
  }'
```

â¶ Set the provider to `azure-openai`.

â· Attach Azure OpenAI API key in the `api-key` header.

â¸ Specify the name of the model.

â¹ Specify the Azure OpenAI endpoint.

Create a route with the `ai-proxy` plugin configured as such:

adc.yaml

```
services:
  - name: azure-openai-service
    routes:
      - name: azure-openai-route
        uris:
          - /anything
        methods:
          - POST
        plugins:
          ai-proxy:
            provider: azure-openai
            auth:
              header:
                api-key: "${AZ_OPENAI_API_KEY}"
            options:
              model: gpt-4
            override:
              endpoint: "https://api7-azure-openai.openai.azure.com/openai/deployments/gpt-4/chat/completions?api-version=2024-02-15-preview"
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

â¶ Set the provider to `azure-openai`.

â· Attach Azure OpenAI API key in the `api-key` header.

â¸ Specify the name of the model.

â¹ Specify the Azure OpenAI endpoint.

* Gateway API
* APISIX CRD

azure-openai-ic.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: ai-proxy-plugin-config
spec:
  plugins:
    - name: ai-proxy
      config:
        provider: azure-openai
        auth:
          header:
            api-key: "57cha9ee8e8a89a12c0aha174f180f4"
        options:
          model: gpt-4
        override:
          endpoint: "https://api7-azure-openai.openai.azure.com/openai/deployments/gpt-4/chat/completions?api-version=2024-02-15-preview"
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: azure-openai-route
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
            name: ai-proxy-plugin-config
```

Apply the configuration to your cluster:

```
kubectl apply -f azure-openai-ic.yaml
```

â¶ Set the provider to `azure-openai`.

â· Attach Azure OpenAI API key in the `api-key` header.

â¸ Specify the name of the model.

â¹ Specify the Azure OpenAI endpoint.

azure-openai-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: azure-openai-route
spec:
  ingressClassName: apisix
  http:
    - name: azure-openai-route
      match:
        paths:
          - /anything
        methods:
          - POST
      plugins:
      - name: ai-proxy
        enable: true
        config:
          provider: azure-openai
          auth:
            header:
              api-key: "57cha9ee8e8a89a12c0aha174f180f4"
          options:
            model: gpt-4
          override:
            endpoint: "https://api7-azure-openai.openai.azure.com/openai/deployments/gpt-4/chat/completions?api-version=2024-02-15-preview"
```

Apply the configuration to your cluster:

```
kubectl apply -f azure-openai-ic.yaml
```

â¶ Set the provider to `azure-openai`.

â· Attach Azure OpenAI API key in the `api-key` header.

â¸ Specify the name of the model.

â¹ Specify the Azure OpenAI endpoint.

Send a POST request to the route with a sample question in the request body:

```
curl "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {
        "role": "system",
        "content": "You are an AI assistant that helps people find information."
      },
      {
        "role": "user",
        "content": "Write me a 50-word introduction for Apache APISIX."
      }
    ],
    "max_tokens": 800,
    "temperature": 0.7,
    "frequency_penalty": 0,
    "presence_penalty": 0,
    "top_p": 0.95,
    "stop": null
  }'
```

You should receive a response similar to the following:

```
{
  "choices": [
    {
      ...,
      "message": {
        "content": "Apache APISIX is a modern, cloud-native API gateway built to handle high-performance and low-latency use cases. It offers a wide range of features, including load balancing, rate limiting, authentication, and dynamic routing, making it an ideal choice for microservices and cloud-native architectures.",
        "role": "assistant"
      }
    }
  ],
  ...
}
```

### Proxy to Gemini[â](#proxy-to-gemini "Direct link to Proxy to Gemini")

The following example demonstrates how you can configure the `ai-proxy` plugin to proxy requests to Google's Gemini API for chat completion. This example applies only to API7 Enterprise from version 3.9.2 and is not applicable in APISIX.

[Obtain a Gemini API key](https://ai.google.dev/gemini-api/docs/api-key) and optionally save it to an environment variable:

```
export GEMINI_API_KEY=AIzaSyDUMZbZmHCmJ5BNNLl0KfQk   # replace with your API key
```

* Admin API
* ADC
* Ingress Controller

Create a route and configure the `ai-proxy` plugin as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-proxy-gemini-route",
    "uri": "/anything",
    "methods": ["POST"],
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

â¶ Specify the provider to be `gemini`.

â· Replace with your Gemini API key in the `Authorization` header.

â¸ Specify the name of the Gemini model.

Create a route with the `ai-proxy` plugin configured as such:

adc.yaml

```
services:
  - name: gemini-service
    routes:
      - name: gemini-route
        uris:
          - /anything
        methods:
          - POST
        plugins:
          ai-proxy:
            provider: gemini
            auth:
              header:
                Authorization: "Bearer ${GEMINI_API_KEY}"
            options:
              model: gemini-2.5-flash
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

â¶ Specify the provider to be `gemini`.

â· Replace with your Gemini API key in the `Authorization` header.

â¸ Specify the name of the Gemini model.

* Gateway API
* APISIX CRD

gemini-ic.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: ai-proxy-plugin-config
spec:
  plugins:
    - name: ai-proxy
      config:
        provider: gemini
        auth:
          header:
            Authorization: "Bearer AIzaSyDUMZbZmHCmJ5BNNLl0KfQk"
        options:
          model: gemini-2.5-flash
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: gemini-route
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
            name: ai-proxy-plugin-config
```

Apply the configuration to your cluster:

```
kubectl apply -f gemini-ic.yaml
```

â¶ Specify the provider to be `gemini`.

â· Replace with your Gemini API key in the `Authorization` header.

â¸ Specify the name of the Gemini model.

gemini-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: gemini-route
spec:
  ingressClassName: apisix
  http:
    - name: gemini-route
      match:
        paths:
          - /anything
        methods:
          - POST
      plugins:
      - name: ai-proxy
        enable: true
        config:
          provider: gemini
          auth:
            header:
              Authorization: "Bearer AIzaSyDUMZbZmHCmJ5BNNLl0KfQk"
          options:
            model: gemini-2.5-flash
```

Apply the configuration to your cluster:

```
kubectl apply -f gemini-ic.yaml
```

â¶ Specify the provider to be `gemini`.

â· Replace with your Gemini API key in the `Authorization` header.

â¸ Specify the name of the Gemini model.

about model endpoint

The configuration above proxies requests to the chat completion endpoint at `https://generativelanguage.googleapis.com/v1beta/openai/chat/completions`. To proxy requests to an embeddings model, explicitly configure the embeddings model endpoint in the `override` field.

Send a POST request to the route with a system prompt and a sample user question in the request body:

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

### Proxy to Vertex AI Chat Completion[â](#proxy-to-vertex-ai-chat-completion "Direct link to Proxy to Vertex AI Chat Completion")

The following example demonstrates how you can configure the `ai-proxy` plugin to proxy requests to Google Cloud's Vertex AI platform using GCP service account authentication. This example applies only to API7 Enterprise from version 3.9.2 and is not applicable in APISIX.

Before proceeding:

* [Enable Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/featurestore/setup) and billing for your GCP project.
* Follow the [service account credentials](https://developers.google.com/workspace/guides/create-credentials#service-account) section to create a service account in GCP, assign the account with the "Vertex AI User" role, and obtain the account credentials in JSON.

Your credentials file should look similar to the following:

credentials.json

```
{
  "type": "service_account",
  "project_id": "api7-vertex",
  "private_key_id": "...",
  "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
  "client_email": "api7-docs@api7-vertex.iam.gserviceaccount.com",
  "client_id": "....",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/api7-docs%40api7-vertex.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
```

Optionally save the JSON to an environment variable:

```
export GCP_SA_JSON="$(cat credentials.json)"
```

* Admin API
* ADC
* Ingress Controller

Create a route and configure the `ai-proxy` plugin as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-proxy-vertex-ai-route",
    "uri": "/anything",
    "methods": ["POST"],
    "plugins": {
      "ai-proxy": {
        "provider": "vertex-ai",
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
    }
  }'
```

â¶ Specify the provider to be `vertex-ai`.

â· Replace with your JSON credentials. Ensure that it is a JSON-escaped string.

â¸ Replace with your Vertex AI project ID and region.

â¹ Specify the name of the Gemini model through Vertex AI in the `<publisher>/<model>` format.

Create a route with the `ai-proxy` plugin configured as such:

adc.yaml

```
services:
  - name: vertex-ai-service
    routes:
      - name: vertex-ai-route
        uris:
          - /anything
        methods:
          - POST
        plugins:
          ai-proxy:
            provider: vertex-ai
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

â¶ Specify the provider to be `vertex-ai`.

â· Replace with your JSON credentials. Ensure that it is a JSON-escaped string.

â¸ Replace with your Vertex AI project ID and region.

â¹ Specify the name of the Gemini model through Vertex AI in the `<publisher>/<model>` format.

* Gateway API
* APISIX CRD

vertex-ai-ic.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: ai-proxy-plugin-config
spec:
  plugins:
    - name: ai-proxy
      config:
        provider: vertex-ai
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
  name: vertex-ai-route
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
            name: ai-proxy-plugin-config
```

Apply the configuration to your cluster:

```
kubectl apply -f vertex-ai-ic.yaml
```

â¶ Specify the provider to be `vertex-ai`.

â· Replace with your JSON credentials. Ensure that it is a JSON-escaped string.

â¸ Replace with your Vertex AI project ID and region.

â¹ Specify the name of the Gemini model through Vertex AI in the `<publisher>/<model>` format.

vertex-ai-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: vertex-ai-route
spec:
  ingressClassName: apisix
  http:
    - name: vertex-ai-route
      match:
        paths:
          - /anything
        methods:
          - POST
      plugins:
      - name: ai-proxy
        enable: true
        config:
          provider: vertex-ai
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
kubectl apply -f vertex-ai-ic.yaml
```

â¶ Specify the provider to be `vertex-ai`.

â· Replace with your JSON credentials. Ensure that it is a JSON-escaped string.

â¸ Replace with your Vertex AI project ID and region.

â¹ Specify the name of the Gemini model through Vertex AI in the `<publisher>/<model>` format.

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

### Proxy to Vertex AI Embedding Models[â](#proxy-to-vertex-ai-embedding-models "Direct link to Proxy to Vertex AI Embedding Models")

The following example demonstrates how you can configure the `ai-proxy` plugin to proxy requests to Vertex AI embedding models using GCP service account authentication. This example applies only to API7 Enterprise from version 3.9.2 and is not applicable in APISIX.

Before proceeding:

* [Enable Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/featurestore/setup) and billing for your GCP project.
* Follow the [service account credentials](https://developers.google.com/workspace/guides/create-credentials#service-account) section to create a service account in GCP, assign the account with the "Vertex AI User" role, and obtain the account credentials in JSON.

Your credentials file should look similar to the following:

credentials.json

```
{
  "type": "service_account",
  "project_id": "api7-vertex",
  "private_key_id": "...",
  "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
  "client_email": "api7-docs@api7-vertex.iam.gserviceaccount.com",
  "client_id": "....",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/api7-docs%40api7-vertex.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
```

Optionally save the JSON to an environment variable:

```
export GCP_SA_JSON="$(cat credentials.json)"
```

* Admin API
* ADC
* Ingress Controller

Create a route and configure the `ai-proxy` plugin as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-proxy-vertex-ai-embeddings-route",
    "uri": "/embeddings",
    "methods": ["POST"],
    "plugins": {
      "ai-proxy": {
        "provider": "vertex-ai",
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
          "model": "gemini-embedding-001"
        }
      }
    }
  }'
```

â¶ Specify the provider to be `vertex-ai`.

â· Replace with your JSON credentials. Ensure that it is a JSON-escaped string.

â¸ Replace with your Vertex AI project ID and region.

â¹ Specify the name of the Vertex AI Gemini embedding model.

Create a route with the `ai-proxy` plugin configured as such:

adc.yaml

```
services:
  - name: vertex-ai-embeddings-service
    routes:
      - name: vertex-ai-embeddings-route
        uris:
          - /embeddings
        methods:
          - POST
        plugins:
          ai-proxy:
            provider: vertex-ai
            auth:
              gcp:
                service_account_json: "${GCP_SA_JSON}"
            provider_conf:
              project_id: api7-vertex
              region: us-central1
            options:
              model: gemini-embedding-001
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

â¶ Specify the provider to be `vertex-ai`.

â· Replace with your JSON credentials. Ensure that it is a JSON-escaped string.

â¸ Replace with your Vertex AI project ID and region.

â¹ Specify the name of the Vertex AI Gemini embedding model.

* Gateway API
* APISIX CRD

vertex-ai-embeddings-ic.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: ai-proxy-plugin-config
spec:
  plugins:
    - name: ai-proxy
      config:
        provider: vertex-ai
        auth:
          gcp:
            service_account_json: '{"type":"service_account","project_id":"api7-vertex","private_key_id":"...","private_key":"-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----","client_email":"api7-docs@api7-vertex.iam.gserviceaccount.com","client_id":"...","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_x509_cert_url":"https://www.googleapis.com/robot/v1/metadata/x509/api7-docs%40api7-vertex.iam.gserviceaccount.com","universe_domain":"googleapis.com"}'
        provider_conf:
          project_id: api7-vertex
          region: us-central1
        options:
          model: gemini-embedding-001
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: vertex-ai-embeddings-route
spec:
  parentRefs:
    - name: apisix
  rules:
    - matches:
        - path:
            type: Exact
            value: /embeddings
          method: POST
      filters:
        - type: ExtensionRef
          extensionRef:
            group: apisix.apache.org
            kind: PluginConfig
            name: ai-proxy-plugin-config
```

Apply the configuration to your cluster:

```
kubectl apply -f vertex-ai-embeddings-ic.yaml
```

â¶ Specify the provider to be `vertex-ai`.

â· Replace with your JSON credentials. Ensure that it is a JSON-escaped string.

â¸ Replace with your Vertex AI project ID and region.

â¹ Specify the name of the Vertex AI Gemini embedding model.

vertex-ai-embeddings-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: vertex-ai-embeddings-route
spec:
  ingressClassName: apisix
  http:
    - name: vertex-ai-embeddings-route
      match:
        paths:
          - /embeddings
        methods:
          - POST
      plugins:
      - name: ai-proxy
        enable: true
        config:
          provider: vertex-ai
          auth:
            gcp:
              service_account_json: '{"type":"service_account","project_id":"api7-vertex","private_key_id":"...","private_key":"-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----","client_email":"api7-docs@api7-vertex.iam.gserviceaccount.com","client_id":"...","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_x509_cert_url":"https://www.googleapis.com/robot/v1/metadata/x509/api7-docs%40api7-vertex.iam.gserviceaccount.com","universe_domain":"googleapis.com"}'
          provider_conf:
            project_id: api7-vertex
            region: us-central1
          options:
            model: gemini-embedding-001
```

Apply the configuration to your cluster:

```
kubectl apply -f vertex-ai-embeddings-ic.yaml
```

â¶ Specify the provider to be `vertex-ai`.

â· Replace with your JSON credentials. Ensure that it is a JSON-escaped string.

â¸ Replace with your Vertex AI project ID and region.

â¹ Specify the name of the Vertex AI Gemini embedding model.

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
  "model": "gemini-embedding-001",
  "usage": {
    "total_tokens": 2,
    "prompt_tokens": 2
  },
  "object": "list",
  "data": [
    {
      "index": 0,
      "object": "embedding",
      "embedding": [
        -0.0241838414222,
        0.0098769934847951,
        0.0074856607243419,
        -0.067302219569683,
        ...
      ]
    }
  ]
}
```

### Proxy to OpenAI Embedding Models[â](#proxy-to-openai-embedding-models "Direct link to Proxy to OpenAI Embedding Models")

The following example demonstrates how you can configure the `ai-proxy` plugin to proxy requests to embedding models. This example will use the OpenAI embedding model endpoint.

Obtain the OpenAI [API key](https://openai.com/blog/openai-api) and optionally save it to an environment variable:

```
export OPENAI_API_KEY=sk-REDACTED-EXAMPLE-KEY   # replace with your API key
```

* Admin API
* ADC
* Ingress Controller

Create a route and configure the `ai-proxy` plugin as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-proxy-route",
    "uri": "/embeddings",
    "methods": ["POST"],
    "plugins": {
      "ai-proxy": {
        "provider": "openai",
        "auth": {
          "header": {
            "Authorization": "Bearer '"$OPENAI_API_KEY"'"
          }
        },
        "options":{
          "model": "text-embedding-3-small",
          "encoding_format": "float"
        },
        "override": {
          "endpoint": "https://api.openai.com/v1/embeddings"
        }
      }
    }
  }'
```

â¶ Specify the provider to be `openai`, so that the plugin will proxy requests to `https://api.openai.com/chat/completions`.

â· Attach OpenAI API key in the `Authorization` header.

â¸ Specify the name of the embedding model.

â¹ Add an additional parameter `encoding_format` to configure returned embedding vector to be a list of floating point numbers.

âº Override the default endpoint with the [embedding API endpoint](https://platform.openai.com/docs/api-reference/embeddings).

Create a route with the `ai-proxy` plugin configured as such:

adc.yaml

```
services:
  - name: openai-embeddings-service
    routes:
      - name: openai-embeddings-route
        uris:
          - /embeddings
        methods:
          - POST
        plugins:
          ai-proxy:
            provider: openai
            auth:
              header:
                Authorization: "Bearer ${OPENAI_API_KEY}"
            options:
              model: text-embedding-3-small
              encoding_format: float
            override:
              endpoint: "https://api.openai.com/v1/embeddings"
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

â¶ Specify the provider to be `openai`, so that the plugin will proxy requests to `https://api.openai.com/chat/completions`.

â· Attach OpenAI API key in the `Authorization` header.

â¸ Specify the name of the embedding model.

â¹ Add an additional parameter `encoding_format` to configure returned embedding vector to be a list of floating point numbers.

âº Override the default endpoint with the [embedding API endpoint](https://platform.openai.com/docs/api-reference/embeddings).

* Gateway API
* APISIX CRD

openai-embeddings-ic.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: ai-proxy-plugin-config
spec:
  plugins:
    - name: ai-proxy
      config:
        provider: openai
        auth:
          header:
            Authorization: "Bearer sk-REDACTED-EXAMPLE-KEY"
        options:
          model: text-embedding-3-small
          encoding_format: float
        override:
          endpoint: "https://api.openai.com/v1/embeddings"
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: openai-embeddings-route
spec:
  parentRefs:
    - name: apisix
  rules:
    - matches:
        - path:
            type: Exact
            value: /embeddings
          method: POST
      filters:
        - type: ExtensionRef
          extensionRef:
            group: apisix.apache.org
            kind: PluginConfig
            name: ai-proxy-plugin-config
```

Apply the configuration to your cluster:

```
kubectl apply -f openai-embeddings-ic.yaml
```

â¶ Specify the provider to be `openai`, so that the plugin will proxy requests to `https://api.openai.com/chat/completions`.

â· Attach OpenAI API key in the `Authorization` header.

â¸ Specify the name of the embedding model.

â¹ Add an additional parameter `encoding_format` to configure returned embedding vector to be a list of floating point numbers.

âº Override the default endpoint with the [embedding API endpoint](https://platform.openai.com/docs/api-reference/embeddings).

openai-embeddings-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: openai-embeddings-route
spec:
  ingressClassName: apisix
  http:
    - name: openai-embeddings-route
      match:
        paths:
          - /embeddings
        methods:
          - POST
      plugins:
      - name: ai-proxy
        enable: true
        config:
          provider: openai
          auth:
            header:
              Authorization: "Bearer sk-REDACTED-EXAMPLE-KEY"
          options:
            model: text-embedding-3-small
            encoding_format: float
          override:
            endpoint: "https://api.openai.com/v1/embeddings"
```

Apply the configuration to your cluster:

```
kubectl apply -f openai-embeddings-ic.yaml
```

â¶ Specify the provider to be `openai`, so that the plugin will proxy requests to `https://api.openai.com/chat/completions`.

â· Attach OpenAI API key in the `Authorization` header.

â¸ Specify the name of the embedding model.

â¹ Add an additional parameter `encoding_format` to configure returned embedding vector to be a list of floating point numbers.

âº Override the default endpoint with the [embedding API endpoint](https://platform.openai.com/docs/api-reference/embeddings).

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

### Proxy to Anthropic[â](#proxy-to-anthropic "Direct link to Proxy to Anthropic")

The following example demonstrates how you can configure the `ai-proxy` plugin to proxy requests to Anthropic's Claude API for chat completion.

Obtain an Anthropic [API key](https://console.anthropic.com/settings/keys) and optionally save it to an environment variable:

```
export ANTHROPIC_API_KEY=sk-ant-api03-XXXXXXXXXXXXXXXX   # replace with your API key
```

* Admin API
* ADC
* Ingress Controller

Create a route and configure the `ai-proxy` plugin as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-proxy-anthropic-route",
    "uri": "/anything",
    "methods": ["POST"],
    "plugins": {
      "ai-proxy": {
        "provider": "anthropic",
        "auth": {
          "header": {
            "x-api-key": "'"$ANTHROPIC_API_KEY"'"
          }
        },
        "options": {
          "model": "claude-sonnet-4-20250514"
        }
      }
    }
  }'
```

â¶ Specify the provider to be `anthropic`.

â· Attach Anthropic API key in the `x-api-key` header.

â¸ Specify the name of the Anthropic model.

Create a route with the `ai-proxy` plugin configured as such:

adc.yaml

```
services:
  - name: anthropic-service
    routes:
      - name: anthropic-route
        uris:
          - /anything
        methods:
          - POST
        plugins:
          ai-proxy:
            provider: anthropic
            auth:
              header:
                x-api-key: "${ANTHROPIC_API_KEY}"
            options:
              model: claude-sonnet-4-20250514
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

â¶ Specify the provider to be `anthropic`.

â· Attach Anthropic API key in the `x-api-key` header.

â¸ Specify the name of the Anthropic model.

* Gateway API
* APISIX CRD

anthropic-ic.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: ai-proxy-plugin-config
spec:
  plugins:
    - name: ai-proxy
      config:
        provider: anthropic
        auth:
          header:
            x-api-key: "sk-ant-api03-XXXXXXXXXXXXXXXX"
        options:
          model: claude-sonnet-4-20250514
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: anthropic-route
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
            name: ai-proxy-plugin-config
```

Apply the configuration to your cluster:

```
kubectl apply -f anthropic-ic.yaml
```

â¶ Specify the provider to be `anthropic`.

â· Attach Anthropic API key in the `x-api-key` header.

â¸ Specify the name of the Anthropic model.

anthropic-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: anthropic-route
spec:
  ingressClassName: apisix
  http:
    - name: anthropic-route
      match:
        paths:
          - /anything
        methods:
          - POST
      plugins:
      - name: ai-proxy
        enable: true
        config:
          provider: anthropic
          auth:
            header:
              x-api-key: "sk-ant-api03-XXXXXXXXXXXXXXXX"
          options:
            model: claude-sonnet-4-20250514
```

Apply the configuration to your cluster:

```
kubectl apply -f anthropic-ic.yaml
```

â¶ Specify the provider to be `anthropic`.

â· Attach Anthropic API key in the `x-api-key` header.

â¸ Specify the name of the Anthropic model.

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
  "id": "msg_01XFDUDYJgAACzvnptvVoYEL",
  "type": "message",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "1+1 equals 2."
    }
  ],
  "model": "claude-sonnet-4-20250514",
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 19,
    "output_tokens": 11
  }
}
```

### Convert Anthropic Requests to OpenAI-Compatible Backend[â](#convert-anthropic-requests-to-openai-compatible-backend "Direct link to Convert Anthropic Requests to OpenAI-Compatible Backend")

The following example demonstrates how the `ai-proxy` plugin can accept requests in the Anthropic Messages API format and automatically convert them to the OpenAI-compatible format before forwarding to any OpenAI-compatible backend (such as OpenAI, DeepSeek, or other compatible services). This is useful when client applications send Anthropic-formatted requests but you want to use a different LLM backend.

The protocol conversion is triggered automatically when the route URI is set to `/v1/messages` (the Anthropic Messages API endpoint). The plugin will convert Anthropic-formatted requests to OpenAI-compatible format and transform the responses back to Anthropic format.

Obtain an API key for your chosen OpenAI-compatible backend service and save it to an environment variable. This example uses OpenAI:

```
export BACKEND_API_KEY=sk-xxx   # replace with your API key
```

* Admin API
* ADC
* Ingress Controller

Create a route and configure the `ai-proxy` plugin as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-proxy-anthropic-convert-route",
    "uri": "/v1/messages",
    "methods": ["POST"],
    "plugins": {
      "ai-proxy": {
        "provider": "openai",
        "auth": {
          "header": {
            "Authorization": "Bearer '"$BACKEND_API_KEY"'"
          }
        },
        "options": {
          "model": "gpt-4"
        }
      }
    }
  }'
```

â¶ Set the URI to `/v1/messages` to trigger automatic Anthropic protocol conversion.

â· Specify the backend provider. This can be any OpenAI-compatible provider, such as `openai`, `deepseek`, or others.

â¸ Specify the model name of the backend provider.

Create a route with the `ai-proxy` plugin configured as such:

adc.yaml

```
services:
  - name: anthropic-convert-service
    routes:
      - name: anthropic-convert-route
        uris:
          - /v1/messages
        methods:
          - POST
        plugins:
          ai-proxy:
            provider: openai
            auth:
              header:
                Authorization: "Bearer ${BACKEND_API_KEY}"
            options:
              model: gpt-4
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

â¶ Set the URI to `/v1/messages` to trigger automatic Anthropic protocol conversion.

â· Specify the backend provider. This can be any OpenAI-compatible provider, such as `openai`, `deepseek`, or others.

â¸ Specify the model name of the backend provider.

* Gateway API
* APISIX CRD

anthropic-convert-ic.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: ai-proxy-plugin-config
spec:
  plugins:
    - name: ai-proxy
      config:
        provider: openai
        auth:
          header:
            Authorization: "Bearer sk-xxx"
        options:
          model: gpt-4
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: anthropic-convert-route
spec:
  parentRefs:
    - name: apisix
  rules:
    - matches:
        - path:
            type: Exact
            value: /v1/messages
          method: POST
      filters:
        - type: ExtensionRef
          extensionRef:
            group: apisix.apache.org
            kind: PluginConfig
            name: ai-proxy-plugin-config
```

Apply the configuration to your cluster:

```
kubectl apply -f anthropic-convert-ic.yaml
```

â¶ Set the URI to `/v1/messages` to trigger automatic Anthropic protocol conversion.

â· Specify the backend provider. This can be any OpenAI-compatible provider, such as `openai`, `deepseek`, or others.

â¸ Specify the model name of the backend provider.

anthropic-convert-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: anthropic-convert-route
spec:
  ingressClassName: apisix
  http:
    - name: anthropic-convert-route
      match:
        paths:
          - /v1/messages
        methods:
          - POST
      plugins:
      - name: ai-proxy
        enable: true
        config:
          provider: openai
          auth:
            header:
              Authorization: "Bearer sk-xxx"
          options:
            model: gpt-4
```

Apply the configuration to your cluster:

```
kubectl apply -f anthropic-convert-ic.yaml
```

â¶ Set the URI to `/v1/messages` to trigger automatic Anthropic protocol conversion.

â· Specify the backend provider. This can be any OpenAI-compatible provider, such as `openai`, `deepseek`, or others.

â¸ Specify the model name of the backend provider.

Send a POST request to the route in Anthropic Messages API format:

```
curl "http://127.0.0.1:9080/v1/messages" -X POST \
  -H "Content-Type: application/json" \
  -H "x-api-key: ${BACKEND_API_KEY}" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "gpt-4",
    "max_tokens": 1024,
    "messages": [
      { "role": "user", "content": "What is 1+1?" }
    ]
  }'
```

Although the request is sent in Anthropic format, it will be automatically converted to OpenAI format and forwarded to the backend. The response is converted back to Anthropic format:

```
{
  "id": "msg_01XFDUDYJgAACzvnptvVoYEL",
  "type": "message",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "1+1 equals 2."
    }
  ],
  "model": "gpt-4",
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 12,
    "output_tokens": 8
  }
}
```

The plugin supports all features of the Anthropic Messages API, including streaming (SSE), system prompts, and tool use (function calling). The protocol conversion handles the bidirectional mapping between Anthropic and OpenAI formats transparently.

### Proxy to Selected Model using Request Body Parameter[â](#proxy-to-selected-model-using-request-body-parameter "Direct link to Proxy to Selected Model using Request Body Parameter")

The following example demonstrates how you can proxy requests to different models on the same URI, based on the user-specified model in the user requests. You will being using the `post_arg.*` [variable](https://docs.api7.ai/enterprise/reference/built-in-variables.md) to fetch the value of the request body parameter.

The example will use OpenAI and DeepSeek as the example LLM services. Obtain the OpenAI and DeepSeek API keys and save them to environment variables:

```
# replace with your API key
export OPENAI_API_KEY=sk-REDACTED-EXAMPLE-KEY
export DEEPSEEK_API_KEY=sk-5e99f3e26abc40e75d80009a90e66
```

* Admin API
* ADC
* Ingress Controller

Create a route to the OpenAI API with the `ai-proxy` plugin:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-proxy-openai-route",
    "uri": "/anything",
    "methods": ["POST"],
    "vars": [[ "post_arg.model", "==", "openai" ]],
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
      }
    }
  }'
```

â¶ Set the route URI to be `/anything`.

â· Match the route to requests where the body parameter `model` is set to `openai`.

Create another route `/anything` to the DeepSeek API with the `ai-proxy` plugin:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-proxy-deepseek-route",
    "uri": "/anything",
    "methods": ["POST"],
    "vars": [[ "post_arg.model", "==", "deepseek" ]],
    "plugins": {
      "ai-proxy": {
        "provider": "deepseek",
        "auth": {
          "header": {
            "Authorization": "Bearer '"$DEEPSEEK_API_KEY"'"
          }
        },
        "options": {
          "model": "deepseek-chat"
        }
      }
    }
  }'
```

â¶ Set the route URI to be `/anything`, same as the previous route.

â· Match the route to requests where the body parameter `model` is set to `deepseek`.

Create two routes with the `ai-proxy` plugin configured for different providers:

adc.yaml

```
services:
  - name: multi-model-service
    routes:
      - name: openai-route
        uris:
          - /anything
        methods:
          - POST
        vars:
          - - post_arg.model
            - ==
            - openai
        plugins:
          ai-proxy:
            provider: openai
            auth:
              header:
                Authorization: "Bearer ${OPENAI_API_KEY}"
            options:
              model: gpt-4
      - name: deepseek-route
        uris:
          - /anything
        methods:
          - POST
        vars:
          - - post_arg.model
            - ==
            - deepseek
        plugins:
          ai-proxy:
            provider: deepseek
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

â¶ Set the route URI to be `/anything`.

â· Match the route to requests where the body parameter `model` is set to `openai`.

â¸ Set the route URI to be `/anything`, same as the previous route.

â¹ Match the route to requests where the body parameter `model` is set to `deepseek`.

* Gateway API
* APISIX CRD

info

Body parameter matching is not supported in HTTPRoute. The supported matching mechanisms are `path`, `method`, `headers`, and `queryParams`. This example cannot be completed with Gateway API.

info

Body parameter matching is currently not supported in ApisixRoute. The supported matching mechanisms are based on `Header`, `Query`, or `Path`. This example cannot be completed with APISIX CRDs.

Send a POST request to the route with `model` set to `openai`:

```
curl "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openai",
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
  ...
}
```

Send a POST request to the route with `model` set to `deepseek`:

```
curl "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek",
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
  ...
}
```

You can also configure `post_arg.*` to fetch nested request body parameter. For instance, if the request format is:

```
curl "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "model": {
      "name": "openai"
    },
    "messages": [
      { "role": "system", "content": "You are a mathematician" },
      { "role": "user", "content": "What is 1+1?" }
    ]
  }'
```

You can configure the `vars` on the route to be `[[ "post_arg.model.name", "==", "openai" ]]`.

For more information on the expressions, see [APISIX Expressions](https://docs.api7.ai/enterprise/reference/expressions.md).

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

Now if you create a route following the [Proxy to OpenAI example](#proxy-to-openai). Send a request like this:

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

Since the model in `ai-proxy` is `gpt-4`, the request will be forwarded to GPT-4 model and you will receive a response similar to the following:

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

* Admin API
* ADC
* Ingress Controller

Create a route to your LLM service and configure logging details as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-proxy-openai-route",
    "uri": "/anything",
    "methods": ["POST"],
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
        },
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

Create a route with both `ai-proxy` and `kafka-logger` plugins:

adc.yaml

```
services:
  - name: logging-service
    routes:
      - name: logging-route
        uris:
          - /anything
        methods:
          - POST
        plugins:
          ai-proxy:
            provider: openai
            auth:
              header:
                Authorization: "Bearer ${OPENAI_API_KEY}"
            options:
              model: gpt-4
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

logging-ic.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: ai-proxy-logging-plugin-config
spec:
  plugins:
    - name: ai-proxy
      config:
        provider: openai
        auth:
          header:
            Authorization: "Bearer sk-REDACTED-EXAMPLE-KEY"
        options:
          model: gpt-4
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
  name: logging-route
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
            name: ai-proxy-logging-plugin-config
```

Apply the configuration to your cluster:

```
kubectl apply -f logging-ic.yaml
```

â¶ Log request LLM model, duration, request and response tokens.

â· Log request and response payload.

â¸ Update with your Kafka address.

â¹ Update with your Kafka topic.

âº Update with your Kafka key.

â» Set to 1 to send the log entry immediately.

logging-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: logging-route
spec:
  ingressClassName: apisix
  http:
    - name: logging-route
      match:
        paths:
          - /anything
        methods:
          - POST
      plugins:
      - name: ai-proxy
        enable: true
        config:
          provider: openai
          auth:
            header:
              Authorization: "Bearer sk-REDACTED-EXAMPLE-KEY"
          options:
            model: gpt-4
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
kubectl apply -f logging-ic.yaml
```

â¶ Log request LLM model, duration, request and response tokens.

â· Log request and response payload.

â¸ Update with your Kafka address.

â¹ Update with your Kafka topic.

âº Update with your Kafka key.

â» Set to 1 to send the log entry immediately.

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
  ...
}
```

In the Kafka topic, you should also see a log entry corresponding to the request with the LLM summary and request/response payload.
