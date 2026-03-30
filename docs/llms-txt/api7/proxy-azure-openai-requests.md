# Source: https://docs.api7.ai/apisix/how-to-guide/ai-gateway/proxy-azure-openai-requests.md

# Proxy Azure OpenAI Requests

[Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service) is a fully managed service that provides unified REST API access to OpenAI's language models, such as GPT-4 and GPT-3.5-Turbo. They can be easily integrated into applications to add capabilities such as content generation, text completion, semantic search, and more.

This guide will walk you through the process of integrating APISIX with [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service).

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Have an Azure account and log into the [Azure portal](https://portal.azure.com).
* Install [Docker](https://docs.docker.com/get-docker/).
* Install [cURL](https://curl.se/) to send requests to the services for validation.
* Follow the [Getting Started Tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker or on Kubernetes.

## Request Access to Azure OpenAI Service[â](#request-access-to-azure-openai-service "Direct link to Request Access to Azure OpenAI Service")

Before proceeding, you should first [request access to Azure OpenAI Service](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/limited-access) as part of Microsoft's commitment to responsible AI by filling out a registration form.

Please request the access for **GPT-3.5, GPT-3.5 Turbo, GPT-4, GPT-4 Turbo, and/or Embeddings Models** to follow along.

![request model access](https://static.api7.ai/uploads/2024/12/12/uXFnnAuj_request_access.png)

## Deploy an Azure OpenAI Service[â](#deploy-an-azure-openai-service "Direct link to Deploy an Azure OpenAI Service")

Once the access is granted, search for **Azure AI services**, navigate to the **Azure OpenAI** in the left panel, and click **Create Azure OpenAI**:

![Create Azure OpenAI Service](https://static.api7.ai/uploads/2024/05/16/kjS4CFVZ_create-azure-openai.jpeg)

Fill out the project and instance details:

![fill out information for the new instance](https://static.api7.ai/uploads/2024/05/16/98I2sQaK_instance-details.jpeg)

<br />

In the **Network** tab, select the **All networks** option, or adjust accordingly per your infrastructure:

![select all networks as the network option](https://static.api7.ai/uploads/2024/05/16/UoGT0P6b_network.jpeg)

<br />

Continue with the setup until the deployment is complete:

![deployment is complete](https://static.api7.ai/uploads/2024/05/16/VFZJ6lFN_deployment-complete.png)

## Obtain API Information[â](#obtain-api-information "Direct link to Obtain API Information")

Go to the [Azure AI Foundry](https://oai.azure.com/portal) and select **Chat**. Click **View Code**:

![Azure AI Foundry chat view code](https://static.api7.ai/uploads/2024/12/19/wOTdySSJ_view-code-light.png)

Switch the command to **curl** and select the **key authentication** tab:

![copy information from the generated code](https://static.api7.ai/uploads/2024/12/19/N2uP7k88_sample-code-light.png)

<br />

Copy the generated **curl command**, **endpoint**, and **API key**.

You can optionally save your API key to an environment variable:

```
export AZ_OPENAI_API_KEY=57cha9ee8e8a89a12c0aha174f180f4   # replace with your API key
```

## Create a Route to Azure OpenAI[â](#create-a-route-to-azure-openai "Direct link to Create a Route to Azure OpenAI")

Create a route and configure the `ai-proxy` plugin as such:

* Admin API
* ADC

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
        "options": {
          "model": "gpt-4"
        },
        "override": {
          "endpoint": "https://api7-auzre-openai.openai.azure.com/openai/deployments/gpt-4/chat/completions?api-version=2024-02-15-preview"
        }
      }
    }
  }'
```

â¶ Set the provider to `azure-openai`.

â· Attach Azure OpenAI API key in the header.

â¸ Specify the Azure OpenAI endpoint.

adc.yaml

```
services:
  - name: Azure OpenAI Service
    routes:
      - uris:
          - /anything
        name: azure-openai-route
        plugins:
          ai-proxy:
            provider: azure-openai
            auth:
              header:
                api-key: 57cha9ee8e8a89a12c0aha174f180f4
            options:
              model: gpt-4
            override:
              endpoint: https://api7-auzre-openai.openai.azure.com/openai/deployments/gpt-4/chat/completions?api-version=2024-02-15-preview
```

â¶ Set the provider to `azure-openai`.

â· Attach Azure OpenAI API key in the header.

â¸ Specify the Azure OpenAI endpoint.

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

## Next Steps[â](#next-steps "Direct link to Next Steps")

You have now learned how to integrate APISIX with Azure OpenAI Service. See [Azure OpenAI Service REST API reference](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference) to learn more.

If you would like to stream the Azure API response, you can set the [`stream` parameter](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference#completions) to `true` for Azure OpenAI Service and use the [`proxy-buffering`](https://docs.api7.ai/hub/proxy-buffering.md) plugin in APISIX to disable NGINX's `proxy_buffering` directive, which avoids the server-sent events (SSE) being buffered.

In addition, you can integrate more capabilities that APISIX offers, such as [rate limiting](https://docs.api7.ai/apisix/how-to-guide/traffic-management/rate-limiting.md) and [caching](https://docs.api7.ai/hub/proxy-cache.md), to improve system availability and user experience.
