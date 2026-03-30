# Source: https://docs.api7.ai/hub/ai-prompt-guard.md

# ai-prompt-guard

The `ai-prompt-guard` plugin safeguards your LLM endpoints by inspecting and validating incoming prompt messages. It checks the content of requests against user-defined allowed and denied patterns to ensure that only approved inputs are forwarded to upstream LLM. Based on its configuration, the plugin can either examine just the latest message or the entire conversation history, and it can be set to check prompts from all roles or only from end users.

When both `allow_patterns` and `deny_patterns` are configured, the plugin first ensures that at least one `allow_patterns` is matched. If none match, the request is rejected. If an allowed pattern is matched, it then checks for any occurrences of denied patterns.

<!-- -->

## Demo[â](#demo "Direct link to Demo")

The following demo demonstrates the [implement allow and deny patterns example](#implement-allow-and-deny-patterns) in API7 Enterprise using the Dashboard, where you can validate user prompts by defining both allow and deny patterns and understand how the allow pattern takes precedence.

## Examples[â](#examples "Direct link to Examples")

The following examples will be using OpenAI as the upstream service provider. Before proceeding, create an [OpenAI account](https://openai.com) and an [API key](https://openai.com/blog/openai-api). You can optionally save the key to an environment variable as such:

```
export OPENAI_API_KEY=sk-REDACTED-EXAMPLE-KEY   # replace with your API key
```

If you are working with other LLM providers, please refer to the provider's documentation to obtain an API key.

### Implement Allow and Deny Patterns[â](#implement-allow-and-deny-patterns "Direct link to Implement Allow and Deny Patterns")

The following example demonstrates how to use the `ai-prompt-guard` plugin to validate user prompts by defining both allow and deny patterns and understand how the allow pattern takes precedence.

Define the allow and deny patterns. You can optionally save them to environment variables for easier escape:

```
# allow US dollar amount
export ALLOW_PATTERN_1='\\$?\\(?\\d{1,3}(,\\d{3})*(\\.\\d{1,2})?\\)?'
# deny phone number in US number format
export DENY_PATTERN_1='(\\([0-9]{3}\\)|[0-9]{3}-)[0-9]{3}-[0-9]{4}'
```

* Admin API
* ADC
* Ingress Controller

Create a route that uses `ai-proxy` to proxy to OpenAI and `ai-prompt-guard` to inspect input prompts:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-prompt-guard-route",
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
      },
      "ai-prompt-guard": {
        "allow_patterns": [
          "'"$ALLOW_PATTERN_1"'"
        ],
        "deny_patterns": [
          "'"$DENY_PATTERN_1"'"
        ]
      }
    }
  }'
```

â¶ Specify the provider to be `openai`.

â· Attach the OpenAI API key in the `Authorization` header as a Bearer token.

â¸ Specify the name of the model.

â¹ Allow message pattern that matches any dollar amounts.

âº Deny message patterns that include any US phone number format.

Create a route with the `ai-prompt-guard` and [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugins configured as such:

adc.yaml

```
services:
  - name: prompt-guard-service
    routes:
      - name: prompt-guard-route
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
          ai-prompt-guard:
            allow_patterns:
              - '\$?\(?\d{1,3}(,\d{3})*(\.\d{1,2})?\)?'
            deny_patterns:
              - '(\([0-9]{3}\)|[0-9]{3}-)[0-9]{3}-[0-9]{4}'
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

â¶ Specify the provider to be `openai`.

â· Attach the OpenAI API key in the `Authorization` header as a Bearer token.

â¸ Specify the name of the model.

â¹ Allow message pattern that matches any dollar amounts.

âº Deny message patterns that include any US phone number format.

* Gateway API
* APISIX CRD

Create a route with the `ai-prompt-guard` and [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugins configured as such:

ai-prompt-guard-ic.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: ai-prompt-guard-plugin-config
spec:
  plugins:
    - name: ai-prompt-guard
      config:
        allow_patterns:
          - '\$?\(?\d{1,3}(,\d{3})*(\.\d{1,2})?\)?'
        deny_patterns:
          - '(\([0-9]{3}\)|[0-9]{3}-)[0-9]{3}-[0-9]{4}'
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
  name: prompt-guard-route
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
            name: ai-prompt-guard-plugin-config
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-prompt-guard-ic.yaml
```

â¶ Allow message pattern that matches any dollar amounts.

â· Deny message patterns that include any US phone number format.

â¸ Attach OpenAI API key in the `Authorization` header.

â¹ Specify the name of the model.

Create a route with the `ai-prompt-guard` and [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugins configured as such:

ai-prompt-guard-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: prompt-guard-route
spec:
  ingressClassName: apisix
  http:
    - name: prompt-guard-route
      match:
        paths:
          - /anything
        methods:
          - POST
      plugins:
        - name: ai-prompt-guard
          enable: true
          config:
            allow_patterns:
              - '\$?\(?\d{1,3}(,\d{3})*(\.\d{1,2})?\)?'
            deny_patterns:
              - '(\([0-9]{3}\)|[0-9]{3}-)[0-9]{3}-[0-9]{4}'
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
kubectl apply -f ai-prompt-guard-ic.yaml
```

â¶ Allow message pattern that matches any dollar amounts.

â· Deny message patterns that include any US phone number format.

â¸ Attach OpenAI API key in the `Authorization` header.

â¹ Specify the name of the model.

Send a request to the route to rate the fairness of a purchase:

```
curl -i "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      { "role": "system", "content": "Rate if the purchase is at a decent price in USD." },
      { "role": "user", "content": "John paid $12.5 for a hot brewed coffee in El Paso." }
    ]
  }'
```

You should see receive an `HTTP/1.1 200 OK` response similar to the following:

```
{
  ...
  "model": "gpt-4-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "The purchase is not at a decent price. Typically, a hot brewed coffee costs anywhere from $1 to $3 in most places in the US, so $12.5 is quite expensive.",
        "refusal": null
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  ...
}
```

Send another request to the route without any price in the message:

```
curl -i "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      { "role": "system", "content": "Rate if the purchase is at a decent price in USD." },
      { "role": "user", "content": "John paid a bit for a hot brewed coffee in El Paso." }
    ]
  }'
```

You should receive an `HTTP/1.1 400 Bad Request` response and see the following message:

```
{"message":"Request doesn't match allow patterns"}
```

Send a third request to the route with a phone number in the message:

```
curl -i "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      { "role": "system", "content": "Rate if the purchase is at a decent price in USD." },
      { "role": "user", "content": "John (647-200-9393) paid $12.5 for a hot brewed coffee in El Paso." }
    ]
  }'
```

You should receive an `HTTP/1.1 400 Bad Request` response and see the following message:

```
{"message":"Request contains prohibited content"}
```

By default, the plugin only inspect the input of `user` role and the last message. For instance, if you send a request including the prohibited content in the `system` prompt:

```
curl -i "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      { "role": "system", "content": "Rate if the purchase from 647-200-9393 is at a decent price in USD." },
      { "role": "user", "content": "John paid $12.5 for a hot brewed coffee in El Paso." }
    ]
  }'
```

You will receive an `HTTP/1.1 200 OK` response.

If you send a request including the prohibited content in the second last message:

```
curl -i "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      { "role": "system", "content": "Rate if the purchase is at a decent price in USD." },
      { "role": "user", "content": "Customer John contact: 647-200-9393" },
      { "role": "user", "content": "John paid $12.5 for a hot brewed coffee in El Paso." }
    ]
  }'
```

You will also receive an `HTTP/1.1 200 OK` response.

See the [next example](#validate-messages-from-all-roles-and-conversation-history) to see how to inspect messages from all roles and all messages.

### Validate Messages From All Roles and Conversation History[â](#validate-messages-from-all-roles-and-conversation-history "Direct link to Validate Messages From All Roles and Conversation History")

The following example demonstrates how to use the `ai-prompt-guard` plugin to validate prompts from all roles, such as `system` and `user`, and validate the entire conversation history instead of the last message.

Define the allow and deny patterns. You can optionally save them to environment variables for easier escape:

```
export ALLOW_PATTERN_1='\\$?\\(?\\d{1,3}(,\\d{3})*(\\.\\d{1,2})?\\)?'
export DENY_PATTERN_1='(\\([0-9]{3}\\)|[0-9]{3}-)[0-9]{3}-[0-9]{4}'
```

* Admin API
* ADC
* Ingress Controller

Create a route that uses `ai-proxy` to proxy to OpenAI and `ai-prompt-guard` to inspect input prompts:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-prompt-guard-route",
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
      },
      "ai-prompt-guard": {
        "match_all_roles": true,
        "match_all_conversation_history": true,
        "allow_patterns": [
          "'"$ALLOW_PATTERN_1"'"
        ],
        "deny_patterns": [
          "'"$DENY_PATTERN_1"'"
        ]
      }
    }
  }'
```

â¶ Validate messages from all roles.

â· Validate messages of the entire conversation.

Create a route with the `ai-prompt-guard` and [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugins configured as such:

adc.yaml

```
services:
  - name: prompt-guard-service
    routes:
      - name: prompt-guard-route
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
          ai-prompt-guard:
            match_all_roles: true
            match_all_conversation_history: true
            allow_patterns:
              - '\$?\(?\d{1,3}(,\d{3})*(\.\d{1,2})?\)?'
            deny_patterns:
              - '(\([0-9]{3}\)|[0-9]{3}-)[0-9]{3}-[0-9]{4}'
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

â¶ Validate messages from all roles.

â· Validate messages of the entire conversation.

* Gateway API
* APISIX CRD

Create a route with the `ai-prompt-guard` and [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugins configured as such:

ai-prompt-guard-history-ic.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: ai-prompt-guard-plugin-config
spec:
  plugins:
    - name: ai-prompt-guard
      config:
        match_all_roles: true
        match_all_conversation_history: true
        allow_patterns:
          - '\$?\(?\d{1,3}(,\d{3})*(\.\d{1,2})?\)?'
        deny_patterns:
          - '(\([0-9]{3}\)|[0-9]{3}-)[0-9]{3}-[0-9]{4}'
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
  name: prompt-guard-route
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
            name: ai-prompt-guard-plugin-config
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-prompt-guard-history-ic.yaml
```

â¶ Validate messages from all roles.

â· Validate messages of the entire conversation.

Create a route with the `ai-prompt-guard` and [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugins configured as such:

ai-prompt-guard-history-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: prompt-guard-route
spec:
  ingressClassName: apisix
  http:
    - name: prompt-guard-route
      match:
        paths:
          - /anything
        methods:
          - POST
      plugins:
        - name: ai-prompt-guard
          enable: true
          config:
            match_all_roles: true
            match_all_conversation_history: true
            allow_patterns:
              - '\$?\(?\d{1,3}(,\d{3})*(\.\d{1,2})?\)?'
            deny_patterns:
              - '(\([0-9]{3}\)|[0-9]{3}-)[0-9]{3}-[0-9]{4}'
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
kubectl apply -f ai-prompt-guard-history-ic.yaml
```

â¶ Validate messages from all roles.

â· Validate messages of the entire conversation.

Send a request including with prohibited content in the `system` prompt:

```
curl -i "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      { "role": "system", "content": "Rate if the purchase from 647-200-9393 is at a decent price in USD." },
      { "role": "user", "content": "John paid $12.5 for a hot brewed coffee in El Paso." }
    ]
  }'
```

You should receive an `HTTP/1.1 400 Bad Request` response and see the following message:

```
{"message":"Request contains prohibited content"}
```

Send a request with multiple messages from the same role with prohibited content:

```
curl -i "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      { "role": "system", "content": "Rate if the purchase is at a decent price in USD." },
      { "role": "user", "content": "Customer John contact: 647-200-9393" },
      { "role": "user", "content": "John paid $12.5 for a hot brewed coffee in El Paso." }
    ]
  }'
```

You should receive an `HTTP/1.1 400 Bad Request` response and see the following message:

```
{"message":"Request contains prohibited content"}
```

Send a request that conforms to the patterns:

```
curl -i "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      { "role": "system", "content": "Rate if the purchase is at a decent price in USD." },
      { "role": "system", "content": "The puchase is made in El Paso." },
      { "role": "user", "content": "Customer John contact: xxx-xxx-xxxx" },
      { "role": "user", "content": "John paid $12.5 for a hot brewed coffee." }
    ]
  }'
```

You should see receive an `HTTP/1.1 200 OK` response similar to the following:

```
{
  ...,
  "model": "gpt-4-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "$12.5 is generally considered quite expensive for a cup of brew coffee.",
        "refusal": null
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  ...
}
```
