# Source: https://docs.api7.ai/hub/ai-prompt-decorator.md

# ai-prompt-decorator

The `ai-prompt-decorator` plugin modifies user input prompts by prefixing and appending pre-engineered prompts to set contexts in content generation. This practice helps the model operate within desired guidelines during interactions.

## Example[â](#example "Direct link to Example")

The following example will be using OpenAI as the upstream service provider. Before proceeding, create an [OpenAI account](https://openai.com) and an [API key](https://openai.com/blog/openai-api). You can optionally save the key to an environment variable as such:

```
export OPENAI_API_KEY=sk-REDACTED-EXAMPLE-KEY   # replace with your API key
```

If you are working with other LLM providers, please refer to the provider's documentation to obtain an API key.

### Prepend and Append Messages[â](#prepend-and-append-messages "Direct link to Prepend and Append Messages")

The following example demonstrates how to configure the `ai-prompt-decorator` plugin to prepend a system message and append a user message to the user input message.

* Admin API
* ADC
* Ingress Controller

Create a route to the chat completion endpoint with pre-configured prompt templates as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-prompt-decorator-route",
    "uri": "/v1/chat/completions",
    "methods": ["POST"],
    "plugins": {
      "proxy-rewrite": {
        "headers": {
          "set": {
            "Authorization": "Bearer '"$OPENAI_API_KEY"'"
          }
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
    },
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "api.openai.com:443": 1
      },
      "scheme": "https"
    }
  }'
```

â¶ Configure the OpenAI API key in the [`proxy-rewrite`](https://docs.api7.ai/hub/proxy-rewrite.md) plugin. Alternatively, you can choose to attach the API key in every client request if you do not wish to configure the key in APISIX.

â· Prepend a system message to set the behavior of the assistant.

â¸ Append additional user message to the user-defined prompt.

Create a route with the `ai-prompt-decorator` plugin configured as such:

adc.yaml

```
services:
  - name: prompt-decorator-service
    routes:
      - name: prompt-decorator-route
        uris:
          - /v1/chat/completions
        methods:
          - POST
        plugins:
          proxy-rewrite:
            headers:
              set:
                Authorization: "Bearer ${OPENAI_API_KEY}"
          ai-prompt-decorator:
            prepend:
              - role: system
                content: "Answer briefly and conceptually."
            append:
              - role: user
                content: "End the answer with a simple analogy."
        upstream:
          type: roundrobin
          nodes:
            - host: api.openai.com
              port: 443
              weight: 1
          scheme: https
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

â¶ Configure the OpenAI API key in the [`proxy-rewrite`](https://docs.api7.ai/hub/proxy-rewrite.md) plugin. Alternatively, you can choose to attach the API key in every client request if you do not wish to configure the key in APISIX.

â· Prepend a system message to set the behavior of the assistant.

â¸ Append additional user message to the user-defined prompt.

* Gateway API
* APISIX CRD

Create a route with the `ai-prompt-decorator` plugin configured as such:

ai-prompt-decorator-ic.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: ai-prompt-decorator-plugin-config
spec:
  plugins:
    - name: proxy-rewrite
      config:
        headers:
          set:
            Authorization: "Bearer sk-REDACTED-EXAMPLE-KEY"
    - name: ai-prompt-decorator
      config:
        prepend:
          - role: system
            content: "Answer briefly and conceptually."
        append:
          - role: user
            content: "End the answer with a simple analogy."
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: prompt-decorator-route
spec:
  parentRefs:
    - name: apisix
  rules:
    - matches:
        - path:
            type: Exact
            value: /v1/chat/completions
          method: POST
      filters:
        - type: ExtensionRef
          extensionRef:
            group: apisix.apache.org
            kind: PluginConfig
            name: ai-prompt-decorator-plugin-config
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-prompt-decorator-ic.yaml
```

â¶ Configure the OpenAI API key in the [`proxy-rewrite`](https://docs.api7.ai/hub/proxy-rewrite.md) plugin. Alternatively, you can choose to attach the API key in every client request if you do not wish to configure the key in APISIX.

â· Prepend a system message to set the behavior of the assistant.

â¸ Append additional user message to the user-defined prompt.

Create a route with the `ai-prompt-decorator` plugin configured as such:

ai-prompt-decorator-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: prompt-decorator-route
spec:
  ingressClassName: apisix
  http:
    - name: prompt-decorator-route
      match:
        paths:
          - /v1/chat/completions
        methods:
          - POST
      plugins:
        - name: proxy-rewrite
          enable: true
          config:
            headers:
              set:
                Authorization: "Bearer sk-REDACTED-EXAMPLE-KEY"
        - name: ai-prompt-decorator
          enable: true
          config:
            prepend:
              - role: system
                content: "Answer briefly and conceptually."
            append:
              - role: user
                content: "End the answer with a simple analogy."
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-prompt-decorator-ic.yaml
```

â¶ Configure the OpenAI API key in the [`proxy-rewrite`](https://docs.api7.ai/hub/proxy-rewrite.md) plugin. Alternatively, you can choose to attach the API key in every client request if you do not wish to configure the key in APISIX.

â· Prepend a system message to set the behavior of the assistant.

â¸ Append additional user message to the user-defined prompt.

Send a POST request to the route specifying the model and a sample message in the request body:

```
curl "http://127.0.0.1:9080/v1/chat/completions" -X POST \
  -H "Content-Type: application/json" \
  -H "Host: api.openai.com:443" \
  -d '{
    "model": "gpt-4",
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
