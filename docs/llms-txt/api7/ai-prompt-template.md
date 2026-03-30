# Source: https://docs.api7.ai/hub/ai-prompt-template.md

# ai-prompt-template

The `ai-prompt-template` plugin supports pre-configuring prompt templates that only accept user inputs in designated template variables, in a "fill in the blank" fashion.

## Examples[â](#examples "Direct link to Examples")

The following examples will use OpenAI as the upstream service provider. Before proceeding, create an [OpenAI account](https://openai.com) and an [API key](https://openai.com/blog/openai-api). You can optionally save the key to an environment variable as such:

```
export OPENAI_API_KEY=sk-REDACTED-EXAMPLE-KEY   # replace with your API key
```

If you are working with other LLM providers, please refer to the provider's documentation to obtain an API key.

### Configure a Template for Open Questions in Custom Complexity[â](#configure-a-template-for-open-questions-in-custom-complexity "Direct link to Configure a Template for Open Questions in Custom Complexity")

The following example demonstrates how to use the `ai-prompt-template` plugin to configure a template that can be used to answer open questions and accepts user-specified response complexity.

* Admin API
* ADC
* Ingress Controller

Create a route to the chat completion endpoint with pre-configured prompt templates as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-prompt-template-route",
    "uri": "/v1/chat/completions",
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
        }
      },
      "ai-prompt-template": {
        "templates": [
          {
            "name": "QnA with complexity",
            "template": {
              "model": "gpt-4",
              "messages": [
                {
                  "role": "system",
                  "content": "Answer in {{complexity}}."
                },
                {
                  "role": "user",
                  "content": "Explain {{prompt}}."
                }
              ]
            }
          }
        ]
      }
    }
  }'
```

â¶ Configure the OpenAI API key in the [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugin.

â· Name the template. When requesting the route, the request should include the template name.

â¸ Specify the model identifier.

â¹ Configure a prompt that obtains the user-defined answer complexity from the request body key `complexity`.

âº Configure a prompt that obtains the user-defined question from the request body key `prompt`.

Create a route with the `ai-prompt-template` and [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugins configured as such:

adc.yaml

```
services:
  - name: prompt-template-service
    routes:
      - name: prompt-template-route
        uris:
          - /v1/chat/completions
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
          ai-prompt-template:
            templates:
              - name: "QnA with complexity"
                template:
                  model: gpt-4
                  messages:
                    - role: system
                      content: "Answer in {{complexity}}."
                    - role: user
                      content: "Explain {{prompt}}."
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

â¶ Configure the OpenAI API key in the [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugin.

â· Name the template. When requesting the route, the request should include the template name.

â¸ Specify the model identifier.

â¹ Configure a prompt that obtains the user-defined answer complexity from the request body key `complexity`.

âº Configure a prompt that obtains the user-defined question from the request body key `prompt`.

* Gateway API
* APISIX CRD

Create a route with the `ai-prompt-template` and [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugins configured as such:

ai-prompt-template-ic.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: ai-prompt-template-plugin-config
spec:
  plugins:
    - name: ai-prompt-template
      config:
        templates:
          - name: "QnA with complexity"
            template:
              model: gpt-4
              messages:
                - role: system
                  content: "Answer in {{complexity}}."
                - role: user
                  content: "Explain {{prompt}}."
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
  name: prompt-template-route
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
            name: ai-prompt-template-plugin-config
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-prompt-template-ic.yaml
```

â¶ Name the template. When requesting the route, the request should include the template name.

â· Specify the model identifier.

â¸ Configure a prompt that obtains the user-defined answer complexity from the request body key `complexity`.

â¹ Configure a prompt that obtains the user-defined question from the request body key `prompt`.

âº Configure the OpenAI API key in the [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugin.

Create a route with the `ai-prompt-template` and [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugins configured as such:

ai-prompt-template-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: prompt-template-route
spec:
  ingressClassName: apisix
  http:
    - name: prompt-template-route
      match:
        paths:
          - /v1/chat/completions
        methods:
          - POST
      plugins:
        - name: ai-prompt-template
          enable: true
          config:
            templates:
              - name: "QnA with complexity"
                template:
                  model: gpt-4
                  messages:
                    - role: system
                      content: "Answer in {{complexity}}."
                    - role: user
                      content: "Explain {{prompt}}."
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
kubectl apply -f ai-prompt-template-ic.yaml
```

â¶ Name the template. When requesting the route, the request should include the template name.

â· Specify the model identifier.

â¸ Configure a prompt that obtains the user-defined answer complexity from the request body key `complexity`.

â¹ Configure a prompt that obtains the user-defined question from the request body key `prompt`.

âº Configure the OpenAI API key in the [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugin.

The route should now be available to be reused to respond to a variety of questions with different levels of user-specified desired complexity.

Send a POST request to the route with a sample question and desired answer complexity in the request body:

```
curl "http://127.0.0.1:9080/v1/chat/completions" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "template_name": "QnA with complexity",
    "complexity": "brief",
    "prompt": "quick sort"
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
        "content": "Quick sort is a highly efficient sorting algorithm that uses a divide-and-conquer approach to arrange elements in a list or array in order. Hereâs a brief explanation:\n\n1. **Choose a Pivot**: Select an element from the list as a 'pivot'. Common methods include choosing the first element, the last element, the middle element, or a random element.\n\n2. **Partitioning**: Rearrange the elements in the list such that all elements less than the pivot are moved before it, and all elements greater than the pivot are moved after it. The pivot is now in its final position.\n\n3. **Recursively Apply**: Recursively apply the same process to the sub-lists of elements to the left and right of the pivot.\n\nThe base case of the recursion is lists of size zero or one, which are already sorted.\n\nQuick sort has an average-case time complexity of O(n log n), making it suitable for large datasets. However, its worst-case time complexity is O(n^2), which occurs when the smallest or largest element is always chosen as the pivot. This can be mitigated by using good pivot selection strategies or randomization.",
        "role": "assistant"
      }
    }
  ],
  "created": 1723194057,
  "id": "chatcmpl-9uFmTYN4tfwaXZjyOQwcp0t5law4x",
  "model": "gpt-4o-2024-05-13",
  "object": "chat.completion",
  "system_fingerprint": "fp_abc28019ad",
  "usage": {
    "completion_tokens": 234,
    "prompt_tokens": 18,
    "total_tokens": 252
  }
}
```

### Configure Multiple Templates[â](#configure-multiple-templates "Direct link to Configure Multiple Templates")

The following example demonstrates how you can configure multiple templates on the same route. When requesting the route, users will be able to pass custom inputs to different templates by specifying the template name.

The example continues with the [last example](#configure-a-template-for-open-questions-in-custom-complexity). Update the plugin with another template:

* Admin API
* ADC
* Ingress Controller

Update the route with an additional template:

```
curl "http://127.0.0.1:9180/apisix/admin/routes/ai-prompt-template-route" -X PATCH \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "plugins": {
      "ai-prompt-template": {
        "templates": [
          {
            "name": "QnA with complexity",
            "template": {
              "model": "gpt-4",
              "messages": [
                {
                  "role": "system",
                  "content": "Answer in {{complexity}}."
                },
                {
                  "role": "user",
                  "content": "Explain {{prompt}}."
                }
              ]
            }
          },
          {
            "name": "echo",
            "template": {
              "model": "gpt-4",
              "messages": [
                {
                  "role": "user",
                  "content": "Echo {{prompt}}."
                }
              ]
            }
          }
        ]
      }
    }
  }'
```

Update the route configuration with an additional template:

adc.yaml

```
services:
  - name: prompt-template-service
    routes:
      - name: prompt-template-route
        uris:
          - /v1/chat/completions
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
          ai-prompt-template:
            templates:
              - name: "QnA with complexity"
                template:
                  model: gpt-4
                  messages:
                    - role: system
                      content: "Answer in {{complexity}}."
                    - role: user
                      content: "Explain {{prompt}}."
              - name: "echo"
                template:
                  model: gpt-4
                  messages:
                    - role: user
                      content: "Echo {{prompt}}."
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

* Gateway API
* APISIX CRD

Update the PluginConfig with an additional template:

ai-prompt-template-multi-ic.yaml

```
# Other Configs
# ---
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: ai-prompt-template-plugin-config
spec:
  plugins:
    - name: ai-prompt-template
      config:
        templates:
          - name: "QnA with complexity"
            template:
              model: gpt-4
              messages:
                - role: system
                  content: "Answer in {{complexity}}."
                - role: user
                  content: "Explain {{prompt}}."
          - name: "echo"
            template:
              model: gpt-4
              messages:
                - role: user
                  content: "Echo {{prompt}}."
    - name: ai-proxy
      config:
        provider: openai
        auth:
          header:
            Authorization: "Bearer sk-REDACTED-EXAMPLE-KEY"
        options:
          model: gpt-4
```

Apply the updated configuration to your cluster:

```
kubectl apply -f ai-prompt-template-multi-ic.yaml
```

Update the ApisixRoute with an additional template:

ai-prompt-template-multi-ic.yaml

```
# Other Configs
# ---
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: prompt-template-route
spec:
  ingressClassName: apisix
  http:
    - name: prompt-template-route
      match:
        paths:
          - /v1/chat/completions
        methods:
          - POST
      plugins:
        - name: ai-prompt-template
          enable: true
          config:
            templates:
              - name: "QnA with complexity"
                template:
                  model: gpt-4
                  messages:
                    - role: system
                      content: "Answer in {{complexity}}."
                    - role: user
                      content: "Explain {{prompt}}."
              - name: "echo"
                template:
                  model: gpt-4
                  messages:
                    - role: user
                      content: "Echo {{prompt}}."
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

Apply the updated configuration to your cluster:

```
kubectl apply -f ai-prompt-template-multi-ic.yaml
```

You should now be able to use both templates through the same route.

Send a POST request to the route and use the first template:

```
curl "http://127.0.0.1:9080/v1/chat/completions" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "template_name": "QnA with complexity",
    "complexity": "brief",
    "prompt": "quick sort"
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
        "content": "Quick sort is a highly efficient sorting algorithm that uses a divide-and-conquer approach to arrange elements in a list or array in order. Hereâs a brief explanation:\n\n1. **Choose a Pivot**: Select an element from the list as a 'pivot'. Common methods include choosing the first element, the last element, the middle element, or a random element.\n\n2. **Partitioning**: Rearrange the elements in the list such that all elements less than the pivot are moved before it, and all elements greater than the pivot are moved after it. The pivot is now in its final position.\n\n3. **Recursively Apply**: Recursively apply the same process to the sub-lists of elements to the left and right of the pivot.\n\nThe base case of the recursion is lists of size zero or one, which are already sorted.\n\nQuick sort has an average-case time complexity of O(n log n), making it suitable for large datasets. However, its worst-case time complexity is O(n^2), which occurs when the smallest or largest element is always chosen as the pivot. This can be mitigated by using good pivot selection strategies or randomization.",
        "role": "assistant"
      }
    }
  ],
  ...
}
```

Send a POST request to the route and use the second template:

```
curl "http://127.0.0.1:9080/v1/chat/completions" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "template_name": "echo",
    "prompt": "hello APISIX"
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
        "content": "hello APISIX",
        "role": "assistant"
      }
    }
  ],
  ...
}
```
