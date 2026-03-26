# Source: https://docs.api7.ai/hub/ai-aliyun-content-moderation.md

# ai-aliyun-content-moderation

The `ai-aliyun-content-moderation` plugin supports the integration with [Aliyun Machine-Assisted Moderation Plus](https://help.aliyun.com/document_detail/2671445.html) to check request bodies for risk level when proxying to LLMs, such as profanity, hate speech, insult, harassment, violence, and more, rejecting requests if the evaluated outcome exceeds the configured threshold.

Please ensure that the `access_key_secret` is correctly configured in the plugin. If misconfigured, all requests will bypass the plugin to be directly forwarded to the LLM upstream, and you will see a `Specified signature is not matched with our calculation` in the gateway's error log from the plugin.

The `ai-aliyun-content-moderation` plugin should be used with either [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) or [`ai-proxy-multi`](https://docs.api7.ai/hub/ai-proxy-multi.md) plugin for proxying LLM requests.

<!-- -->

## Demo[â](#demo "Direct link to Demo")

The following demo demonstrates the [moderate request content toxicity example](#moderate-request-content-toxicity) in API7 Enterprise using the Dashboard, where you can moderate request content for toxicity and customize the rejection code and message.

## Examples[â](#examples "Direct link to Examples")

The following examples will be using OpenAI as the upstream service provider.

Before proceeding, create an [OpenAI account](https://openai.com) and obtain an [API key](https://openai.com/blog/openai-api). If you are working with other LLM providers, please refer to the provider's documentation to obtain an API key.

Additionally, create an [Aliyun account](https://www.aliyun.com), enable Machine-Assisted Moderation Plus, and obtain the endpoint, region ID, access key ID, and access key secret.

You can optionally save these information to environment variables:

```
# replace with your data
export OPENAI_API_KEY=sk-REDACTED-EXAMPLE-KEY
export ALIYUN_ENDPOINT=https://green-cip.cn-shanghai.aliyuncs.com
export ALIYUN_REGION_ID=cn-shanghai
export ALIYUN_ACCESS_KEY_ID=LTAI5yXKZP77gR3BQQM9WJnA
export ALIYUN_ACCESS_KEY_SECRET=hT2YpkqLs9FIjh3dyznBw7RMux5OKv
```

### Moderate Request Content Toxicity[â](#moderate-request-content-toxicity "Direct link to Moderate Request Content Toxicity")

The following example demonstrates how you can use the plugin to moderate content toxicity in requests and customize rejection code and message.

* Admin API
* ADC
* Ingress Controller

Create a route to the LLM chat completion endpoint using the [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugin and configure the integration details as well as the deny code and message in the `ai-aliyun-content-moderation` plugin:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-aliyun-content-moderation-route",
    "uri": "/anything",
    "plugins": {
      "ai-aliyun-content-moderation": {
        "endpoint": "'"$ALIYUN_ENDPOINT"'",
        "region_id": "'"$ALIYUN_REGION_ID"'",
        "access_key_id": "'"$ALIYUN_ACCESS_KEY_ID"'",
        "access_key_secret": "'"$ALIYUN_ACCESS_KEY_SECRET"'",
        "deny_code": 400,
        "deny_message": "Request contains forbidden content, such as hate speech or violence."
      },
      "ai-proxy": {
        "provider": "openai",
        "auth": {
          "header": {
            "Authorization": "Bearer '"$OPENAI_API_KEY"'"
          }
        }
      }
    }
  }'
```

â¶ Configure the rejection HTTP status code.

â· Configure the rejection message.

Create a route with the `ai-aliyun-content-moderation` and [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugins configured as such:

adc.yaml

```
services:
  - name: aliyun-moderation-service
    routes:
      - name: aliyun-moderation-route
        uris:
          - /anything
        methods:
          - POST
        plugins:
          ai-aliyun-content-moderation:
            endpoint: "${ALIYUN_ENDPOINT}"
            region_id: "${ALIYUN_REGION_ID}"
            access_key_id: "${ALIYUN_ACCESS_KEY_ID}"
            access_key_secret: "${ALIYUN_ACCESS_KEY_SECRET}"
            deny_code: 400
            deny_message: "Request contains forbidden content, such as hate speech or violence."
          ai-proxy:
            provider: openai
            auth:
              header:
                Authorization: "Bearer ${OPENAI_API_KEY}"
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

â¶ Configure the rejection HTTP status code.

â· Configure the rejection message.

* Gateway API
* APISIX CRD

Create a route with the `ai-aliyun-content-moderation` and [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugins configured as such:

ai-aliyun-moderation-ic.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: ai-aliyun-moderation-plugin-config
spec:
  plugins:
    - name: ai-aliyun-content-moderation
      config:
        endpoint: "https://green-cip.cn-shanghai.aliyuncs.com"
        region_id: "cn-shanghai"
        access_key_id: "LTAI5yXKZP77gR3BQQM9WJnA"
        access_key_secret: "hT2YpkqLs9FIjh3dyznBw7RMux5OKv"
        deny_code: 400
        deny_message: "Request contains forbidden content, such as hate speech or violence."
    - name: ai-proxy
      config:
        provider: openai
        auth:
          header:
            Authorization: "Bearer sk-REDACTED-EXAMPLE-KEY"
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: aliyun-moderation-route
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
            name: ai-aliyun-moderation-plugin-config
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-aliyun-moderation-ic.yaml
```

â¶ Configure the rejection HTTP status code.

â· Configure the rejection message.

Create a route with the `ai-aliyun-content-moderation` and [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugins configured as such:

ai-aliyun-moderation-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: aliyun-moderation-route
spec:
  ingressClassName: apisix
  http:
    - name: aliyun-moderation-route
      match:
        paths:
          - /anything
        methods:
          - POST
      plugins:
        - name: ai-aliyun-content-moderation
          enable: true
          config:
            endpoint: "https://green-cip.cn-shanghai.aliyuncs.com"
            region_id: "cn-shanghai"
            access_key_id: "LTAI5yXKZP77gR3BQQM9WJnA"
            access_key_secret: "hT2YpkqLs9FIjh3dyznBw7RMux5OKv"
            deny_code: 400
            deny_message: "Request contains forbidden content, such as hate speech or violence."
        - name: ai-proxy
          enable: true
          config:
            provider: openai
            auth:
              header:
                Authorization: "Bearer sk-REDACTED-EXAMPLE-KEY"
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-aliyun-moderation-ic.yaml
```

â¶ Configure the rejection HTTP status code.

â· Configure the rejection message.

Send a POST request to the route with a system prompt and a user question with a profane word in the request body:

```
curl -i "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4",
    "messages": [
      { "role": "system", "content": "You are a mathematician" },
      { "role": "user", "content": "Stupid, what is 1+1?" }
    ]
  }'
```

You should receive an `HTTP/1.1 400 Bad Request` response and see the following message:

```
{
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 124,
    "prompt_tokens": 31,
    "total_tokens": 155
  },
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "Request contains forbidden content, such as hate speech or violence."
      },
      "finish_reason": "stop",
      "index": 0
    }
  ],
  "model": "gpt-4",
  "id": "c9466bbf-e010-469d-949a-a10f25525964"
}
```

Send another request to the route with a typical question in the request body:

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

### Adjust Risk Level Threshold[â](#adjust-risk-level-threshold "Direct link to Adjust Risk Level Threshold")

The following example demonstrates how you can use adjust the threshold of risk level, which regulates whether a request/response should be allowed through.

* Admin API
* ADC
* Ingress Controller

Create a route to the LLM chat completion endpoint using the [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugin and configure the `risk_level_bar` in `ai-aliyun-content-moderation` to be `high`:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-aliyun-content-moderation-route",
    "uri": "/anything",
    "plugins": {
      "ai-aliyun-content-moderation": {
        "endpoint": "'"$ALIYUN_ENDPOINT"'",
        "region_id": "'"$ALIYUN_REGION_ID"'",
        "access_key_id": "'"$ALIYUN_ACCESS_KEY_ID"'",
        "access_key_secret": "'"$ALIYUN_ACCESS_KEY_SECRET"'",
        "deny_code": 400,
        "deny_message": "Request contains forbidden content, such as hate speech or violence.",
        "risk_level_bar": "high"
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

Create a route with the `ai-aliyun-content-moderation` and [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugins configured as such:

adc.yaml

```
services:
  - name: aliyun-moderation-service
    routes:
      - name: aliyun-moderation-route
        uris:
          - /anything
        methods:
          - POST
        plugins:
          ai-aliyun-content-moderation:
            endpoint: "${ALIYUN_ENDPOINT}"
            region_id: "${ALIYUN_REGION_ID}"
            access_key_id: "${ALIYUN_ACCESS_KEY_ID}"
            access_key_secret: "${ALIYUN_ACCESS_KEY_SECRET}"
            deny_code: 400
            deny_message: "Request contains forbidden content, such as hate speech or violence."
            risk_level_bar: high
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

* Gateway API
* APISIX CRD

Create a route with the `ai-aliyun-content-moderation` and [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugins configured as such:

ai-aliyun-moderation-threshold-ic.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: ai-aliyun-moderation-plugin-config
spec:
  plugins:
    - name: ai-aliyun-content-moderation
      config:
        endpoint: "https://green-cip.cn-shanghai.aliyuncs.com"
        region_id: "cn-shanghai"
        access_key_id: "LTAI5yXKZP77gR3BQQM9WJnA"
        access_key_secret: "hT2YpkqLs9FIjh3dyznBw7RMux5OKv"
        deny_code: 400
        deny_message: "Request contains forbidden content, such as hate speech or violence."
        risk_level_bar: high
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
  name: aliyun-moderation-route
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
            name: ai-aliyun-moderation-plugin-config
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-aliyun-moderation-threshold-ic.yaml
```

Create a route with the `ai-aliyun-content-moderation` and [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) plugins configured as such:

ai-aliyun-moderation-threshold-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: aliyun-moderation-route
spec:
  ingressClassName: apisix
  http:
    - name: aliyun-moderation-route
      match:
        paths:
          - /anything
        methods:
          - POST
      plugins:
        - name: ai-aliyun-content-moderation
          enable: true
          config:
            endpoint: "https://green-cip.cn-shanghai.aliyuncs.com"
            region_id: "cn-shanghai"
            access_key_id: "LTAI5yXKZP77gR3BQQM9WJnA"
            access_key_secret: "hT2YpkqLs9FIjh3dyznBw7RMux5OKv"
            deny_code: 400
            deny_message: "Request contains forbidden content, such as hate speech or violence."
            risk_level_bar: high
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
kubectl apply -f ai-aliyun-moderation-threshold-ic.yaml
```

Send a POST request to the route with a system prompt and a user question with a profane word in the request body:

```
curl -i "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4",
    "messages": [
      { "role": "system", "content": "You are a mathematician" },
      { "role": "user", "content": "Stupid, what is 1+1?" }
    ]
  }'
```

You should receive an `HTTP/1.1 400 Bad Request` response and see the following message:

```
{
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 124,
    "prompt_tokens": 31,
    "total_tokens": 155
  },
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "Request contains forbidden content, such as hate speech or violence."
      },
      "finish_reason": "stop",
      "index": 0
    }
  ],
  "model": "gpt-4",
  "id": "c9466bbf-e010-469d-949a-a10f25525964"
}
```

Update the `risk_level_bar` in the plugin to `max`:

```
curl "http://127.0.0.1:9180/apisix/admin/routes/ai-aliyun-content-moderation-route" -X PATCH \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "plugins": {
      "ai-aliyun-content-moderation": {
        "risk_level_bar": "max"
      }
    }
  }'
```

Send the same request to the route:

```
curl -i "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      { "role": "system", "content": "You are a mathematician" },
      { "role": "user", "content": "Stupid, what is 1+1?" }
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

This is because the word "stupid" has a risk level of `high`, which is lower than the configured threshold of `max`. To see the Aliyun moderation outcome, you can update the gateway's log level to `debug` as such:

conf/config.yaml

```
nginx_config:
  error_log_level: debug
```

[Reload the gateway](https://docs.api7.ai/apisix/reference/apisix-cli.md#apisix-reload) for configuration changes to take effect.

For example, for the request above, you should see a debug log entry similar to the following:

```
{
  "RequestId": "29F7AD19-074B-54AC-B240-B297AD96883F",
  "Message": "OK",
  "Data": {
    ...,
    "RiskLevel": "high",
    "Result": [
      {
        "RiskWords": "are&you&stupid",
        ...
      }
    ]
  },
  "Code": 200
}
```
