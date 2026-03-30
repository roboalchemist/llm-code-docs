# Source: https://docs.api7.ai/hub/ai-request-rewrite.md

# ai-request-rewrite

The `ai-request-rewrite` plugin processes client requests by forwarding them to LLM services for transformation before relaying them to upstream services. This enables LLM-powered modifications such as data redaction, content enrichment, or reformatting. The plugin supports the integration with OpenAI, DeepSeek, Gemini, Vertex AI, Anthropic, OpenRouter, and other OpenAI-compatible APIs.

<!-- -->

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can configure `ai-request-rewrite` for different scenarios.

The examples will use OpenAI as the LLM service. To follow along, obtain the OpenAI [API key](https://openai.com/blog/openai-api) and save it to an environment variable:

```
export OPENAI_API_KEY=sk-REDACTED-EXAMPLE-KEY   # replace with your API key
```

### Redact Sensitive Information[â](#redact-sensitive-information "Direct link to Redact Sensitive Information")

The following example demonstrates how you can use the `ai-request-rewrite` plugin to redact sensitive information before the request reaches the upstream service.

* Admin API
* ADC
* Ingress Controller

Create a route and configure the `ai-request-rewrite` plugin as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-request-rewrite-route",
    "uri": "/anything",
    "methods": ["POST"],
    "plugins": {
      "ai-request-rewrite": {
        "provider": "openai",
        "auth": {
          "header": {
            "Authorization": "Bearer '"$OPENAI_API_KEY"'"
          }
        },
        "options":{
          "model": "gpt-4"
        },
        "prompt": "Given a JSON request body, identify and mask any sensitive information such as credit card numbers, social security numbers, and personal identification numbers (e.g., passport or driver'\''s license numbers). Replace detected sensitive values with a masked format (e.g., \"*** **** **** 1234\") for credit card numbers. Ensure the JSON structure remains unchanged."
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org:80": 1
      }
    }
  }'
```

â¶ Specify the provider to be `openai`.

â· Attach OpenAI API key in the `Authorization` header.

â¸ Specify the name of the model.

â¹ Specify what information to redact before the request reaches the upstream service.

Create a route with the `ai-request-rewrite` plugin configured as such:

adc.yaml

```
services:
  - name: ai-request-rewrite-service
    routes:
      - name: ai-request-rewrite-route
        uris:
          - /anything
        methods:
          - POST
        plugins:
          ai-request-rewrite:
            provider: openai
            auth:
              header:
                Authorization: "Bearer ${OPENAI_API_KEY}"
            options:
              model: gpt-4
            prompt: "Given a JSON request body, identify and mask any sensitive information such as credit card numbers, social security numbers, and personal identification numbers (e.g., passport or driver's license numbers). Replace detected sensitive values with a masked format (e.g., \"*** **** **** 1234\") for credit card numbers. Ensure the JSON structure remains unchanged."
        upstream:
          type: roundrobin
          nodes:
            - host: httpbin.org
              port: 80
              weight: 1
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

â¶ Specify the provider to be `openai`.

â· Attach OpenAI API key in the `Authorization` header.

â¸ Specify the name of the model.

â¹ Specify what information to redact before the request reaches the upstream service.

* Gateway API
* APISIX CRD

Create a route with the `ai-request-rewrite` plugin configured as such:

ai-request-rewrite-ic.yaml

```
apiVersion: v1
kind: Service
metadata:
  namespace: aic
  name: httpbin-external-domain
spec:
  type: ExternalName
  externalName: httpbin.org
---
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: ai-request-rewrite-plugin-config
spec:
  plugins:
    - name: ai-request-rewrite
      config:
        provider: openai
        auth:
          header:
            Authorization: "Bearer sk-REDACTED-EXAMPLE-KEY"
        options:
          model: gpt-4
        prompt: "Given a JSON request body, identify and mask any sensitive information such as credit card numbers, social security numbers, and personal identification numbers (e.g., passport or driver's license numbers). Replace detected sensitive values with a masked format (e.g., \"*** **** **** 1234\") for credit card numbers. Ensure the JSON structure remains unchanged."
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: ai-request-rewrite-route
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
            name: ai-request-rewrite-plugin-config
      backendRefs:
        - name: httpbin-external-domain
          port: 80
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-request-rewrite-ic.yaml
```

â¶ Specify the provider to be `openai`.

â· Attach OpenAI API key in the `Authorization` header.

â¸ Specify the name of the model.

â¹ Specify what information to redact before the request reaches the upstream service.

Create a route with the `ai-request-rewrite` plugin configured as such:

ai-request-rewrite-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixUpstream
metadata:
  namespace: aic
  name: httpbin-external-domain
spec:
  ingressClassName: apisix
  externalNodes:
  - type: Domain
    name: httpbin.org
---
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: ai-request-rewrite-route
spec:
  ingressClassName: apisix
  http:
    - name: ai-request-rewrite-route
      match:
        paths:
          - /anything
        methods:
          - POST
      upstreams:
      - name: httpbin-external-domain
      plugins:
        - name: ai-request-rewrite
          enable: true
          config:
            provider: openai
            auth:
              header:
                Authorization: "Bearer sk-REDACTED-EXAMPLE-KEY"
            options:
              model: gpt-4
            prompt: "Given a JSON request body, identify and mask any sensitive information such as credit card numbers, social security numbers, and personal identification numbers (e.g., passport or driver's license numbers). Replace detected sensitive values with a masked format (e.g., \"*** **** **** 1234\") for credit card numbers. Ensure the JSON structure remains unchanged."
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-request-rewrite-ic.yaml
```

â¶ Specify the provider to be `openai`.

â· Attach OpenAI API key in the `Authorization` header.

â¸ Specify the name of the model.

â¹ Specify what information to redact before the request reaches the upstream service.

Send a POST request to the route with some personally identifiable information:

```
curl "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "content": "John said his debit card number is 4111 1111 1111 1111 and SIN is 123-45-6789."
  }'
```

You should receive a response similar to the following:

```
{
  "args": {},
  "data": "{\n    \"content\": \"John said his debit card number is **** **** **** 1111 and SIN is ***-**-****.\"\n  }"
  ...,
  "json": {
    "messages": [
      {
        "content": "Client information from customer service calls",
        "role": "system"
      }, 
      {
        "content": "John said his debit card number is **** **** **** 1111 and SIN is ***-**-****."
        "role": "user"
      }
    ], 
    "model": "openai"
  }, 
  "method": "POST", 
  "origin": "192.168.97.1, 103.97.2.170", 
  "url": "http://127.0.0.1/anything"
}
```

### Reformat Data[â](#reformat-data "Direct link to Reformat Data")

The following example demonstrates how you can use the `ai-request-rewrite` plugin to reformat data before the request reaches the upstream service.

* Admin API
* ADC
* Ingress Controller

Create a route and configure the `ai-request-rewrite` plugin as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-request-rewrite-route",
    "uri": "/anything",
    "methods": ["POST"],
    "plugins": {
      "ai-request-rewrite": {
        "provider": "openai",
        "auth": {
          "header": {
            "Authorization": "Bearer '"$OPENAI_API_KEY"'"
          }
        },
        "options":{
          "model": "gpt-4"
        },
        "prompt": "Convert natural language queries into structured JSON format with intent and extracted parameters."
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org:80": 1
      }
    }
  }'
```

â¶ Specify the provider to be `openai`.

â· Attach OpenAI API key in the `Authorization` header.

â¸ Specify the name of the model.

â¹ Specify how to reformat before the request reaches the upstream service.

Create a route with the `ai-request-rewrite` plugin configured as such:

adc.yaml

```
services:
  - name: ai-request-rewrite-service
    routes:
      - name: ai-request-rewrite-route
        uris:
          - /anything
        methods:
          - POST
        plugins:
          ai-request-rewrite:
            provider: openai
            auth:
              header:
                Authorization: "Bearer ${OPENAI_API_KEY}"
            options:
              model: gpt-4
            prompt: "Convert natural language queries into structured JSON format with intent and extracted parameters."
        upstream:
          type: roundrobin
          nodes:
            - host: httpbin.org
              port: 80
              weight: 1
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

â¶ Specify the provider to be `openai`.

â· Attach OpenAI API key in the `Authorization` header.

â¸ Specify the name of the model.

â¹ Specify how to reformat before the request reaches the upstream service.

* Gateway API
* APISIX CRD

Create a route with the `ai-request-rewrite` plugin configured as such:

ai-request-rewrite-ic.yaml

```
apiVersion: v1
kind: Service
metadata:
  namespace: aic
  name: httpbin-external-domain
spec:
  type: ExternalName
  externalName: httpbin.org
---
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: ai-request-rewrite-plugin-config
spec:
  plugins:
    - name: ai-request-rewrite
      config:
        provider: openai
        auth:
          header:
            Authorization: "Bearer sk-REDACTED-EXAMPLE-KEY"
        options:
          model: gpt-4
        prompt: "Convert natural language queries into structured JSON format with intent and extracted parameters."
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: ai-request-rewrite-route
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
            name: ai-request-rewrite-plugin-config
      backendRefs:
        - name: httpbin-external-domain
          port: 80
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-request-rewrite-ic.yaml
```

â¶ Specify the provider to be `openai`.

â· Attach OpenAI API key in the `Authorization` header.

â¸ Specify the name of the model.

â¹ Specify how to reformat before the request reaches the upstream service.

Create a route with the `ai-request-rewrite` plugin configured as such:

ai-request-rewrite-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixUpstream
metadata:
  namespace: aic
  name: httpbin-external-domain
spec:
  ingressClassName: apisix
  externalNodes:
  - type: Domain
    name: httpbin.org
---
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: ai-request-rewrite-route
spec:
  ingressClassName: apisix
  http:
    - name: ai-request-rewrite-route
      match:
        paths:
          - /anything
        methods:
          - POST
      upstreams:
      - name: httpbin-external-domain
      plugins:
        - name: ai-request-rewrite
          enable: true
          config:
            provider: openai
            auth:
              header:
                Authorization: "Bearer sk-REDACTED-EXAMPLE-KEY"
            options:
              model: gpt-4
            prompt: "Convert natural language queries into structured JSON format with intent and extracted parameters."
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-request-rewrite-ic.yaml
```

â¶ Specify the provider to be `openai`.

â· Attach OpenAI API key in the `Authorization` header.

â¸ Specify the name of the model.

â¹ Specify how to reformat before the request reaches the upstream service.

Send a POST request to the route with some personally identifiable information:

```
curl "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Book a flight from NYC to LA on April 10, 2022."
  }'
```

You should receive a response similar to the following:

```
{
  "args": {},
  "data": "{\n  \"intent\": \"BookFlight\",\n  \"parameters\": {\n    \"origin\": \"NYC\",\n    \"destination\": \"LA\",\n    \"date\": \"2022-04-10\"\n  }\n}", 
  ...,
  "json": {
    "intent": "BookFlight", 
    "parameters": {
      "date": "2022-04-10", 
      "destination": "LA", 
      "origin": "NYC"
    }
  },
  "method": "POST", 
  "origin": "192.168.97.1, 103.97.2.167", 
  "url": "http://127.0.0.1/anything"
}
```

### Summarize Information[â](#summarize-information "Direct link to Summarize Information")

The following example demonstrates how you can use the `ai-request-rewrite` plugin to summarize information before the request reaches the upstream service.

* Admin API
* ADC
* Ingress Controller

Create a route and configure the `ai-request-rewrite` plugin as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-request-rewrite-route",
    "uri": "/anything",
    "methods": ["POST"],
    "plugins": {
      "ai-request-rewrite": {
        "provider": "openai",
        "auth": {
          "header": {
            "Authorization": "Bearer '"$OPENAI_API_KEY"'"
          }
        },
        "options":{
          "model": "gpt-4"
        },
        "prompt": "Summarize lengthy input while preserving key details. Ensure the summary remains concise and informative."
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org:80": 1
      }
    }
  }'
```

â¶ Specify the provider to be `openai`.

â· Attach OpenAI API key in the `Authorization` header.

â¸ Specify the name of the model.

â¹ Specify the requirements to summarize information before the request reaches the upstream service.

Create a route with the `ai-request-rewrite` plugin configured as such:

adc.yaml

```
services:
  - name: ai-request-rewrite-service
    routes:
      - name: ai-request-rewrite-route
        uris:
          - /anything
        methods:
          - POST
        plugins:
          ai-request-rewrite:
            provider: openai
            auth:
              header:
                Authorization: "Bearer ${OPENAI_API_KEY}"
            options:
              model: gpt-4
            prompt: "Summarize lengthy input while preserving key details. Ensure the summary remains concise and informative."
        upstream:
          type: roundrobin
          nodes:
            - host: httpbin.org
              port: 80
              weight: 1
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

â¶ Specify the provider to be `openai`.

â· Attach OpenAI API key in the `Authorization` header.

â¸ Specify the name of the model.

â¹ Specify the requirements to summarize information before the request reaches the upstream service.

* Gateway API
* APISIX CRD

Create a route with the `ai-request-rewrite` plugin configured as such:

ai-request-rewrite-ic.yaml

```
apiVersion: v1
kind: Service
metadata:
  namespace: aic
  name: httpbin-external-domain
spec:
  type: ExternalName
  externalName: httpbin.org
---
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: ai-request-rewrite-plugin-config
spec:
  plugins:
    - name: ai-request-rewrite
      config:
        provider: openai
        auth:
          header:
            Authorization: "Bearer sk-REDACTED-EXAMPLE-KEY"
        options:
          model: gpt-4
        prompt: "Summarize lengthy input while preserving key details. Ensure the summary remains concise and informative."
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: ai-request-rewrite-route
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
            name: ai-request-rewrite-plugin-config
      backendRefs:
        - name: httpbin-external-domain
          port: 80
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-request-rewrite-ic.yaml
```

â¶ Specify the provider to be `openai`.

â· Attach OpenAI API key in the `Authorization` header.

â¸ Specify the name of the model.

â¹ Specify the requirements to summarize information before the request reaches the upstream service.

Create a route with the `ai-request-rewrite` plugin configured as such:

ai-request-rewrite-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixUpstream
metadata:
  namespace: aic
  name: httpbin-external-domain
spec:
  ingressClassName: apisix
  externalNodes:
  - type: Domain
    name: httpbin.org
---
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: ai-request-rewrite-route
spec:
  ingressClassName: apisix
  http:
    - name: ai-request-rewrite-route
      match:
        paths:
          - /anything
        methods:
          - POST
      upstreams:
      - name: httpbin-external-domain
      plugins:
        - name: ai-request-rewrite
          enable: true
          config:
            provider: openai
            auth:
              header:
                Authorization: "Bearer sk-REDACTED-EXAMPLE-KEY"
            options:
              model: gpt-4
            prompt: "Summarize lengthy input while preserving key details. Ensure the summary remains concise and informative."
```

Apply the configuration to your cluster:

```
kubectl apply -f ai-request-rewrite-ic.yaml
```

â¶ Specify the provider to be `openai`.

â· Attach OpenAI API key in the `Authorization` header.

â¸ Specify the name of the model.

â¹ Specify the requirements to summarize information before the request reaches the upstream service.

Send a POST request to the route with some personally identifiable information:

```
curl "http://127.0.0.1:9080/anything" -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Hey! So, Iâm planning a trip to Japan next spring for about three weeks, and I want to visit Tokyo, Kyoto, and Osaka, but Iâm not sure how to split my time between them. I really love history and cultural sites, so temples and shrines are a must. Iâm also a big foodie, especially into ramen and sushi, so Iâd love recommendations on the best spots. I prefer quieter areas for accommodation, but I donât mind traveling into busy areas for sightseeing. Oh, and Iâd also like to do a day trip somewhere outside these citiesâmaybe Hakone or Nara? I heard the cherry blossoms might still be in bloom in early April, so Iâd love to catch them if possible. Also, whatâs the best way to get aroundâshould I get a JR Pass, or would individual tickets be better? Thanks!"
  }'
```

You should receive a response similar to the following:

```
{
  "args": {},
  "data": "The individual is planning a three-week trip to Japan in the spring, looking to visit Tokyo, Kyoto, and Osaka. They are interested in history, culture, temples, and shrines. They love ramen and sushi, so are seeking food recommendations. Accommodation should be in quieter areas, but they are open to busy sites for sightseeing. Along with these cities, they plan to make a day trip to either Hakone or Nara, hoping to see the cherry blossoms in early April. The best transport method between buying the JR Pass or individual tickets is also a query.", 
  ...,
  "method": "POST", 
  "origin": "192.168.97.1, 103.97.2.171", 
  "url": "http://127.0.0.1/anything"
}
```
