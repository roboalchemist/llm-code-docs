# Source: https://docs.api7.ai/apisix/how-to-guide/ai-gateway/pre-define-prompt-templates.md

# Pre-Define Prompt Templates

When working with [large language models (LLMs)](https://en.wikipedia.org/wiki/Large_language_model), administrators may prefer to pre-configure a prompt template that accepts user inputs in designated fields, which allows the service to be re-used across the organization.

In this document, you will learn how to configure a prompt template in APISIX using the [`ai-prompt-template`](https://docs.api7.ai/hub/ai-prompt-template.md) plugin so that users can easily interact with the model by inserting values into the designated fields in a "fill in the blank" fashion. While the document will be using [OpenAI](https://openai.com/) as the sample upstream service, the procedure can be easily adapted to work with other LLM service providers.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker/).
* Install [cURL](https://curl.se/) to send requests to the services for validation.
* Follow the [Getting Started Tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker or on Kubernetes.

## Obtain an OpenAI API Key[â](#obtain-an-openai-api-key "Direct link to Obtain an OpenAI API Key")

Create an [OpenAI account](https://openai.com) and an [API key](https://openai.com/blog/openai-api) before proceeding. You can optionally save the key to an environment variable as such:

```
export OPENAI_API_KEY=sk-REDACTED-EXAMPLE-KEY   # replace with your API key
```

## Create a Route[â](#create-a-route "Direct link to Create a Route")

Create a route to the OpenAI API endpoint with a sample prompt template that accepts a user-defined prompt and answers in the specified complexity:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ai-prompt-template-route",
    "uri": "/anything",
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

â¶ Name the template set. When requesting the route, the request should include the template name.

â· Specify the model identifier.

â¸ Configure a prompt that obtains the user-defined answer complexity from the request body key `complexity`.

â¹ Configure a prompt that obtains the user-defined question from the request body key `prompt`.

## Verify[â](#verify "Direct link to Verify")

The route should now be available to be re-used to respond to a variety of questions with different levels of user-specified desired complexities.

Send a POST request to the route with a sample question and desired answer complexity in the request body:

```
curl "http://127.0.0.1:9080/anything" -X POST \
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

## Next Steps[â](#next-steps "Direct link to Next Steps")

You have now learned how to pre-define prompt templates in APISIX when integrating with LLM service providers, such that the same route can be re-used to take different user inputs and serve a variety of purposes.

If you would like to integrate with OpenAI's [streaming API](https://platform.openai.com/docs/api-reference/streaming), you can use the [`proxy-buffering`](https://docs.api7.ai/hub/proxy-buffering.md) plugin to disable NGINX's `proxy_buffering` directive to avoid server-sent events (SSE) being buffered.

In addition, you can integrate more capabilities that APISIX offers, such as [rate limiting](https://docs.api7.ai/apisix/how-to-guide/traffic-management/rate-limiting.md) and [caching](https://docs.api7.ai/hub/proxy-cache.md), to improve system availability and user experience.
