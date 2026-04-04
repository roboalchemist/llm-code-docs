# Source: https://docs.api7.ai/hub/ai-aws-content-moderation.md

# ai-aws-content-moderation

The `ai-aws-content-moderation` plugin supports the integration with [AWS Comprehend](https://aws.amazon.com/comprehend/) to check request bodies for toxicity when proxying to LLMs, such as profanity, hate speech, insult, harassment, violence, and more, rejecting requests if the evaluated outcome exceeds the configured threshold.

<!-- -->

## Examples[â](#examples "Direct link to Examples")

The following examples will be using OpenAI as the upstream service provider.

Before proceeding, create an [OpenAI account](https://openai.com) and obtain an [API key](https://openai.com/blog/openai-api). If you are working with other LLM providers, please refer to the provider's documentation to obtain an API key.

Additionally, create [AWS IAM user access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) for APISIX to access [AWS Comprehend](https://aws.amazon.com/comprehend/).

You can optionally save these keys to environment variables:

```
# replace with your keys
export OPENAI_API_KEY=sk-REDACTED-EXAMPLE-KEY
export AWS_ACCESS_KEY=AKIAIOSFODNN7EXAMPLE
export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

### Moderate Profanity[â](#moderate-profanity "Direct link to Moderate Profanity")

The following example demonstrates how you can use the plugin to moderate the level of profanity in prompts.

* Admin API
* ADC
* Ingress Controller

Create a route to the LLM chat completion endpoint using the [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugin and configure the allowed profanity level in `ai-aws-content-moderation`:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-aws-content-moderation-route",
    "uri": "/post",
    "plugins": {
      "ai-aws-content-moderation": {
        "comprehend": {
          "access_key_id": "'"$AWS_ACCESS_KEY"'",
          "secret_access_key": "'"$AWS_SECRET_ACCESS_KEY"'",
          "region": "us-east-1"
        },
        "moderation_categories": {
          "PROFANITY": 0.1
        }
      },
      "ai-proxy": {
        "provider": "openai",
        "auth": {
          "header": {
            "Authorization": "Bearer '"$OPENAI_API_KEY"'"
          }
        },
        "model": "gpt-4"
      }
    }
  }'
```

â¶ Update with your AWS Comprehend region.

â· Configure the profanity threshold to a low value to allow a lower degree of profanity.

Create a route with the `ai-aws-content-moderation` and [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugins configured as such:

adc.yaml

```
services:
  - name: aws-moderation-service
    routes:
      - name: aws-moderation-route
        uris:
          - /post
        methods:
          - POST
        plugins:
          ai-aws-content-moderation:
            comprehend:
              access_key_id: "${AWS_ACCESS_KEY}"
              secret_access_key: "${AWS_SECRET_ACCESS_KEY}"
              region: us-east-1
            moderation_categories:
              PROFANITY: 0.1
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

â¶ Update with your AWS Comprehend region.

â· Configure the profanity threshold to a low value to allow a lower degree of profanity.

* Gateway API
* APISIX CRD

Create a route with the `ai-aws-content-moderation` and [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugins configured as such:

ai-aws-moderation-ic.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: ai-aws-moderation-plugin-config
spec:
  plugins:
    - name: ai-aws-content-moderation
      config:
        comprehend:
          access_key_id: "AKIAIOSFODNN7EXAMPLE"
          secret_access_key: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
          region: us-east-1
        moderation_categories:
          PROFANITY: 0.1
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
  name: aws-moderation-route
spec:
  parentRefs:
    - name: apisix
  rules:
    - matches:
        - path:
            type: Exact
            value: /post
          method: POST
      filters:
        - type: ExtensionRef
          extensionRef:
            group: apisix.apache.org
            kind: PluginConfig
            name: ai-aws-moderation-plugin-config
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-aws-moderation-ic.yaml
```

â¶ Update with your AWS Comprehend region.

â· Configure the profanity threshold to a low value to allow a lower degree of profanity.

Create a route with the `ai-aws-content-moderation` and [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugins configured as such:

ai-aws-moderation-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: aws-moderation-route
spec:
  ingressClassName: apisix
  http:
    - name: aws-moderation-route
      match:
        paths:
          - /post
        methods:
          - POST
      plugins:
        - name: ai-aws-content-moderation
          enable: true
          config:
            comprehend:
              access_key_id: "AKIAIOSFODNN7EXAMPLE"
              secret_access_key: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
              region: us-east-1
            moderation_categories:
              PROFANITY: 0.1
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
kubectl apply -f ai-aws-moderation-ic.yaml
```

â¶ Update with your AWS Comprehend region.

â· Configure the profanity threshold to a low value to allow a lower degree of profanity.

Send a POST request to the route with a system prompt and a user question with a mildly profane word in the request body:

```
curl -i "http://127.0.0.1:9080/post" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      { "role": "system", "content": "You are a mathematician" },
      { "role": "user", "content": "Stupid, what is 1+1?" }
    ]
  }'
```

You should receive an `HTTP/1.1 400 Bad Request` response and see the following message:

```
request body exceeds PROFANITY threshold
```

Send another request to the route with a typical question in the request body:

```
curl -i "http://127.0.0.1:9080/post" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      { "role": "system", "content": "You are a mathematician" },
      { "role": "user", "content": "What is 1+1?" }
    ]
  }'
```

You should receive an `HTTP/1.1 200 OK` response with the model output:

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

### Moderate Overall Toxicity[â](#moderate-overall-toxicity "Direct link to Moderate Overall Toxicity")

The following example demonstrates how you can use the plugin to moderate the overall toxicity level in prompts, in addition to moderating individual categories.

* Admin API
* ADC
* Ingress Controller

Create a route to the LLM chat completion endpoint using the [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugin and configure the allowed profanity and overall toxicity levels in `ai-aws-content-moderation`:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-aws-content-moderation-route",
    "uri": "/post",
    "plugins": {
      "ai-aws-content-moderation": {
        "comprehend": {
          "access_key_id": "'"$AWS_ACCESS_KEY"'",
          "secret_access_key": "'"$AWS_SECRET_ACCESS_KEY"'",
          "region": "us-east-1"
        },
        "moderation_categories": {
          "PROFANITY": 1
        },
        "moderation_threshold": 0.2
      },
      "ai-proxy": {
        "provider": "openai",
        "auth": {
          "header": {
            "Authorization": "Bearer '"$OPENAI_API_KEY"'"
          }
        },
        "model": "gpt-4"
      }
    }
  }'
```

â¶ Update with your AWS Comprehend region.

â· Configure the profanity threshold to allow a high degree of profanity.

â¸ Configure the overall toxicity threshold to allow a low degree of toxicity.

Create a route with the `ai-aws-content-moderation` and [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugins configured as such:

adc.yaml

```
services:
  - name: aws-moderation-service
    routes:
      - name: aws-moderation-route
        uris:
          - /post
        methods:
          - POST
        plugins:
          ai-aws-content-moderation:
            comprehend:
              access_key_id: "${AWS_ACCESS_KEY}"
              secret_access_key: "${AWS_SECRET_ACCESS_KEY}"
              region: us-east-1
            moderation_categories:
              PROFANITY: 1
            moderation_threshold: 0.2
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

â¶ Update with your AWS Comprehend region.

â· Configure the profanity threshold to allow a high degree of profanity.

â¸ Configure the overall toxicity threshold to allow a low degree of toxicity.

* Gateway API
* APISIX CRD

Create a route with the `ai-aws-content-moderation` and [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugins configured as such:

ai-aws-moderation-toxicity-ic.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: ai-aws-moderation-plugin-config
spec:
  plugins:
    - name: ai-aws-content-moderation
      config:
        comprehend:
          access_key_id: "AKIAIOSFODNN7EXAMPLE"
          secret_access_key: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
          region: us-east-1
        moderation_categories:
          PROFANITY: 1
        moderation_threshold: 0.2
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
  name: aws-moderation-route
spec:
  parentRefs:
    - name: apisix
  rules:
    - matches:
        - path:
            type: Exact
            value: /post
          method: POST
      filters:
        - type: ExtensionRef
          extensionRef:
            group: apisix.apache.org
            kind: PluginConfig
            name: ai-aws-moderation-plugin-config
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-aws-moderation-toxicity-ic.yaml
```

â¶ Update with your AWS Comprehend region.

â· Configure the profanity threshold to allow a high degree of profanity.

â¸ Configure the overall toxicity threshold to allow a low degree of toxicity.

Create a route with the `ai-aws-content-moderation` and [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugins configured as such:

ai-aws-moderation-toxicity-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: aws-moderation-route
spec:
  ingressClassName: apisix
  http:
    - name: aws-moderation-route
      match:
        paths:
          - /post
        methods:
          - POST
      plugins:
        - name: ai-aws-content-moderation
          enable: true
          config:
            comprehend:
              access_key_id: "AKIAIOSFODNN7EXAMPLE"
              secret_access_key: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
              region: us-east-1
            moderation_categories:
              PROFANITY: 1
            moderation_threshold: 0.2
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
kubectl apply -f ai-aws-moderation-toxicity-ic.yaml
```

â¶ Update with your AWS Comprehend region.

â· Configure the profanity threshold to allow a high degree of profanity.

â¸ Configure the overall toxicity threshold to allow a low degree of toxicity.

Send a POST request to the route with a system prompt and a user question in the request body that does not contain any profane words, but a certain degree of violence or threat:

```
curl -i "http://127.0.0.1:9080/post" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      { "role": "system", "content": "You are a mathematician" },
      { "role": "user", "content": "I will kill you if you do not tell me what 1+1 equals" }
    ]
  }'
```

You should receive an `HTTP/1.1 400 Bad Request` response and see the following message:

```
request body exceeds toxicity threshold
```

Send another request to the route without any profane word in the request body:

```
curl -i "http://127.0.0.1:9080/post" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      { "role": "system", "content": "You are a mathematician" },
      { "role": "user", "content": "What is 1+1?" }
    ]
  }'
```

You should receive an `HTTP/1.1 200 OK` response with the model output:

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
