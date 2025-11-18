# Venice Documentation

Source: https://docs.venice.ai/llms-full.txt

---

# Introduction
Source: https://docs.venice.ai/api-reference/api-spec

Reference documentation for the Venice API

The Venice API offers HTTP-based REST and streaming interfaces for building AI applications with uncensored models and private inference. You can create with text generation, image creation, embeddings, and more, all without restrictive content policies. Integration examples and SDKs are available in the [documentation](/overview/getting-started).

## Authentication

The Venice API uses API keys for authentication. Create and manage your API keys in your [API settings](https://venice.ai/settings/api).

All API requests require HTTP Bearer authentication:

```
Authorization: Bearer VENICE_API_KEY
```

<Note>
  Your API key is a secret. Do not share it or expose it in any client-side code.
</Note>

## OpenAI Compatibility

Venice's API implements the OpenAI API specification, ensuring compatibility with existing OpenAI clients and tools. This allows you to integrate with Venice using the familiar OpenAI interface while accessing Venice's unique features and uncensored models.

### Setup

Configure your client to use Venice's base URL (`https://api.venice.ai/api/v1`) and make your first request:

<CodeGroup>
  ```bash curl theme={null}
  curl https://api.venice.ai/api/v1/chat/completions \
    -H "Authorization: Bearer $VENICE_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "venice-uncensored",
      "messages": [{"role": "user", "content": "Hello!"}]
    }'
  ```

  ```javascript JavaScript theme={null}
  import OpenAI from "openai";

  const client = new OpenAI({
    apiKey: process.env.VENICE_API_KEY,
    baseURL: "https://api.venice.ai/api/v1",
  });

  const response = await client.chat.completions.create({
    model: "venice-uncensored",
    messages: [{ role: "user", content: "Hello!" }]
  });

  console.log(response.choices[0].message.content);
  ```

  ```python Python theme={null}
  import os
  from openai import OpenAI

  client = OpenAI(
      api_key=os.environ.get("VENICE_API_KEY"),
      base_url="https://api.venice.ai/api/v1"
  )

  response = client.chat.completions.create(
      model="venice-uncensored",
      messages=[{"role": "user", "content": "Hello!"}]
  )

  print(response.choices[0].message.content)
  ```
</CodeGroup>

## Venice-Specific Features

### System Prompts

Venice provides default system prompts designed to ensure uncensored and natural model responses. You have two options for handling system prompts:

1. **Default Behavior**: Your system prompts are appended to Venice's defaults
2. **Custom Behavior**: Disable Venice's system prompts entirely

#### Disabling Venice System Prompts

Use the `venice_parameters` option to remove Venice's default system prompts:

<CodeGroup>
  ```bash curl theme={null}
  curl https://api.venice.ai/api/v1/chat/completions \
    -H "Authorization: Bearer $VENICE_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "venice-uncensored",
      "messages": [
        {"role": "system", "content": "Your custom system prompt"},
        {"role": "user", "content": "Why is the sky blue?"}
      ],
      "venice_parameters": {
        "include_venice_system_prompt": false
      }
    }'
  ```

  ```javascript JavaScript theme={null}
  const completion = await client.chat.completions.create({
    model: "venice-uncensored",
    messages: [
      {
        role: "system",
        content: "Your custom system prompt",
      },
      {
        role: "user",
        content: "Why is the sky blue?",
      },
    ],
    venice_parameters: {
      include_venice_system_prompt: false,
    },
  });
  ```

  ```python Python theme={null}
  response = client.chat.completions.create(
      model="venice-uncensored",
      messages=[
          {"role": "system", "content": "Your custom system prompt"},
          {"role": "user", "content": "Why is the sky blue?"}
      ],
      extra_body={
          "venice_parameters": {
              "include_venice_system_prompt": False
          }
      }
  )
  ```
</CodeGroup>

### Venice Parameters

The `venice_parameters` object allows you to access Venice-specific features not available in the standard OpenAI API:

| Parameter                            | Type    | Description                                                                                                                                                                                                                 | Default |
| ------------------------------------ | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `character_slug`                     | string  | The character slug of a public Venice character (discoverable as "Public ID" on the published character page)                                                                                                               | -       |
| `strip_thinking_response`            | boolean | Strip `<think></think>` blocks from the response (applicable to reasoning/thinking models)                                                                                                                                  | `false` |
| `disable_thinking`                   | boolean | On supported reasoning models, disable thinking and strip the `<think></think>` blocks from the response                                                                                                                    | `false` |
| `enable_web_search`                  | string  | Enable web search for this request (`off`, `on`, `auto` - auto enables based on model's discretion)<br />Additional usage-based pricing applies, see [pricing](/overview/pricing#web-search-and-scraping).                  | `off`   |
| `enable_web_scraping`                | boolean | Enable web scraping of URLs detected in the user message. Scraped content augments responses and bypasses web search<br />Additional usage-based pricing applies, see [pricing](/overview/pricing#web-search-and-scraping). | `false` |
| `enable_web_citations`               | boolean | When web search is enabled, request that the LLM cite its sources using `[REF]0[/REF]` format                                                                                                                               | `false` |
| `include_search_results_in_stream`   | boolean | Experimental: Include search results in the stream as the first emitted chunk                                                                                                                                               | `false` |
| `return_search_results_as_documents` | boolean | Surface search results in an OpenAI-compatible tool call named `venice_web_search_documents` for LangChain integration                                                                                                      | `false` |
| `include_venice_system_prompt`       | boolean | Whether to include Venice's default system prompts alongside specified system prompts                                                                                                                                       | `true`  |

<Note>
  These parameters can also be specified as model suffixes appended to the model name (e.g., `qwen3-235b:enable_web_search=auto`). See [Model Feature Suffixes](/api-reference/endpoint/chat/model_feature_suffix) for details.
</Note>

## Response Headers Reference

All Venice API responses include HTTP headers that provide metadata about the request, rate limits, model information, and account balance. In addition to error codes returned from API responses, you can inspect these headers to get the unique ID of a particular API request, monitor rate limiting, and track your account balance.

Venice recommends logging request IDs (`CF-RAY` header) in production deployments for more efficient troubleshooting with our support team, should the need arise.

The table below provides a comprehensive reference of all headers you may encounter:

| Header                                      | Type   | Purpose                                                                               | When Returned                                   |
| ------------------------------------------- | ------ | ------------------------------------------------------------------------------------- | ----------------------------------------------- |
| **Standard HTTP Headers**                   |        |                                                                                       |                                                 |
| `Content-Type`                              | string | MIME type of the response body (`application/json`, `text/csv`, `image/png`, etc.)    | Always                                          |
| `Content-Encoding`                          | string | Encoding used to compress the response body (`gzip`, `br`)                            | When client sends `Accept-Encoding` header      |
| `Content-Disposition`                       | string | How content should be displayed (e.g., `attachment; filename=export.csv`)             | When downloading files or exports               |
| `Date`                                      | string | RFC 7231 formatted timestamp when the response was generated                          | Always                                          |
| **Request Identification**                  |        |                                                                                       |                                                 |
| `CF-RAY`                                    | string | Unique identifier for this API request, used for troubleshooting and support requests | Always                                          |
| `x-venice-version`                          | string | Current version/revision of the Venice API service (e.g., `20250828.222653`)          | Always                                          |
| `x-venice-timestamp`                        | string | Server timestamp when the request was processed (ISO 8601 format)                     | When timestamp tracking is enabled              |
| `x-venice-host-name`                        | string | Hostname of the server that processed the request                                     | Error responses and debugging scenarios         |
| **Model Information**                       |        |                                                                                       |                                                 |
| `x-venice-model-id`                         | string | Unique identifier of the AI model used for the request (e.g., `venice-01-lite`)       | Inference endpoints using AI models             |
| `x-venice-model-name`                       | string | Friendly/display name of the AI model used (e.g., `Venice Lite`)                      | Inference endpoints using AI models             |
| `x-venice-model-router`                     | string | Router/backend service that handled the model inference                               | Inference endpoints when routing info available |
| `x-venice-model-deprecation-warning`        | string | Warning message for models scheduled for deprecation                                  | When using a deprecated model                   |
| `x-venice-model-deprecation-date`           | string | Date when the model will be deprecated (ISO 8601 date)                                | When using a deprecated model                   |
| **Rate Limiting Information**               |        |                                                                                       |                                                 |
| `x-ratelimit-limit-requests`                | number | Maximum number of requests allowed in the current time window                         | All authenticated requests                      |
| `x-ratelimit-remaining-requests`            | number | Number of requests remaining in the current time window                               | All authenticated requests                      |
| `x-ratelimit-reset-requests`                | number | Unix timestamp when the request rate limit resets                                     | All authenticated requests                      |
| `x-ratelimit-limit-tokens`                  | number | Maximum number of tokens (prompt + completion) allowed in the time window             | All authenticated requests                      |
| `x-ratelimit-remaining-tokens`              | number | Number of tokens remaining in the current time window                                 | All authenticated requests                      |
| `x-ratelimit-reset-tokens`                  | number | Duration in seconds until the token rate limit resets                                 | All authenticated requests                      |
| `x-ratelimit-type`                          | string | Type of rate limit applied (`user`, `api_key`, `global`)                              | When rate limiting is enforced                  |
| **Pagination Headers**                      |        |                                                                                       |                                                 |
| `x-pagination-limit`                        | number | Number of items per page                                                              | Paginated endpoints                             |
| `x-pagination-page`                         | number | Current page number (1-based)                                                         | Paginated endpoints                             |
| `x-pagination-total`                        | number | Total number of items across all pages                                                | Paginated endpoints                             |
| `x-pagination-total-pages`                  | number | Total number of pages                                                                 | Paginated endpoints                             |
| **Account Balance Information**             |        |                                                                                       |                                                 |
| `x-venice-balance-diem`                     | string | Your DIEM token balance before the request was processed                              | All authenticated requests                      |
| `x-venice-balance-usd`                      | string | Your USD credit balance before the request was processed                              | All authenticated requests                      |
| `x-venice-balance-vcu`                      | string | Your Venice Compute Unit (VCU) balance before the request was processed               | All authenticated requests                      |
| **Content Safety Headers**                  |        |                                                                                       |                                                 |
| `x-venice-is-blurred`                       | string | Indicates if generated image was blurred due to content policies (`true`/`false`)     | Image generation with Safe Venice enabled       |
| `x-venice-is-content-violation`             | string | Indicates if content violates Venice's content policies (`true`/`false`)              | Content generation endpoints                    |
| `x-venice-is-adult-model-content-violation` | string | Indicates if content violates adult model content policies (`true`/`false`)           | Image generation endpoints                      |
| `x-venice-contains-minor`                   | string | Indicates if image contains minors (`true`/`false`)                                   | Image analysis endpoints with age detection     |
| **Client Information**                      |        |                                                                                       |                                                 |
| `x-venice-middleface-version`               | string | Version of the Venice middleface client                                               | Requests from Venice middleface clients         |
| `x-venice-mobile-version`                   | string | Version of the Venice mobile app client                                               | Requests from mobile applications               |
| `x-venice-request-timestamp-ms`             | number | Client-provided request timestamp in milliseconds                                     | When client provides timestamp in request       |
| `x-venice-control-instance`                 | string | Control instance identifier for debugging                                             | Image generation endpoints for debugging        |
| **Authentication Headers**                  |        |                                                                                       |                                                 |
| `x-auth-refreshed`                          | string | Indicates authentication token was refreshed during request (`true`/`false`)          | When authentication tokens are auto-refreshed   |
| `x-retry-count`                             | number | Number of retry attempts for the request                                              | When request retries occur                      |

### Important Notes

* **Header Name Case**: HTTP headers are case-insensitive, but Venice uses lowercase with hyphens for consistency
* **String Values**: Boolean values in headers are returned as strings (`"true"` or `"false"`)
* **Numeric Values**: Large numbers and balance values may be returned as strings to prevent precision loss
* **Optional Headers**: Not all headers are returned in every response; presence depends on the endpoint and request context
* **Compression**: Use `Accept-Encoding: gzip, br` in requests to receive compressed responses where supported

### Example: Accessing Response Headers

```javascript  theme={null}
// After making an API request, access headers from the response object
const requestId = response.headers.get('CF-RAY');
const remainingRequests = response.headers.get('x-ratelimit-remaining-requests');
const remainingTokens = response.headers.get('x-ratelimit-remaining-tokens');
const usdBalance = response.headers.get('x-venice-balance-usd');

// Check for model deprecation warnings
const deprecationWarning = response.headers.get('x-venice-model-deprecation-warning');
if (deprecationWarning) {
  console.warn(`Model Deprecation: ${deprecationWarning}`);
}
```

## Best Practices

1. **Rate Limiting**: Monitor `x-ratelimit-remaining-requests` and `x-ratelimit-remaining-tokens` headers and implement exponential backoff
2. **Balance Monitoring**: Track `x-venice-balance-usd` and `x-venice-balance-diem` headers to avoid service interruptions
3. **System Prompts**: Test with and without Venice's system prompts to find the best fit for your use case
4. **API Keys**: Keep your API keys secure and rotate them regularly
5. **Request Logging**: Log `CF-RAY` header values for troubleshooting with support
6. **Model Deprecation**: Check for `x-venice-model-deprecation-warning` headers when using models

## Differences from OpenAI's API

While Venice maintains high compatibility with the OpenAI API specification, there are some key differences:

1. **venice\_parameters**: Additional configurations like `enable_web_search`, `character_slug`, and `strip_thinking_response` for extended functionality
2. **System Prompts**: Venice appends your system prompts to defaults that optimize for uncensored responses (disable with `include_venice_system_prompt: false`)
3. **Model Ecosystem**: Venice offers its own [model lineup](/overview/models) including uncensored and reasoning models - use Venice model IDs rather than OpenAI mappings
4. **Response Headers**: Unique headers for balance tracking (`x-venice-balance-usd`, `x-venice-balance-diem`), model deprecation warnings, and content safety flags
5. **Content Policies**: More permissive policies with dedicated uncensored models and optional content filtering

## API Stability

Venice maintains backward compatibility for v1 endpoints and parameters. For model lifecycle policy, deprecation notices, and migration guidance, see [Deprecations](/overview/deprecations).

## Swagger Configuration

You can find the complete swagger definition for the Venice API here: [https://api.venice.ai/doc/api/swagger.yaml](https://api.venice.ai/doc/api/swagger.yaml)


# Create API Key
Source: https://docs.venice.ai/api-reference/endpoint/api_keys/create

POST /api_keys
Create a new API key.



# Delete API Key
Source: https://docs.venice.ai/api-reference/endpoint/api_keys/delete

DELETE /api_keys
Delete an API key.



# Generate API Key with Web3 Wallet
Source: https://docs.venice.ai/api-reference/endpoint/api_keys/generate_web3_key/get

GET /api_keys/generate_web3_key
Returns the token required to generate an API key via a wallet.

## Autonomous Agent API Key Creation

Please see [this guide](/overview/guides/generating-api-key-agent) on how to use this endpoint.

***


# Generate API Key with Web3 Wallet
Source: https://docs.venice.ai/api-reference/endpoint/api_keys/generate_web3_key/post

POST /api_keys/generate_web3_key
Authenticates a wallet holding sVVV and creates an API key.

## Autonomous Agent API Key Creation

Please see [this guide](/overview/guides/generating-api-key-agent) on how to use this endpoint.

***


# Get API Key Details
Source: https://docs.venice.ai/api-reference/endpoint/api_keys/get

GET /api_keys/{id}
Return details about a specific API key, including rate limits and balance data.



# List API Keys
Source: https://docs.venice.ai/api-reference/endpoint/api_keys/list

GET /api_keys
Return a list of API keys.



# Rate Limit Logs
Source: https://docs.venice.ai/api-reference/endpoint/api_keys/rate_limit_logs

GET /api_keys/rate_limits/log
Returns the last 50 rate limits that the account exceeded.

## Experimental Endpoint

<Warning>
  This is an experimental endpoint and may be subject to change.
</Warning>

## Postman Collection

For additional examples, please see this [Postman Collection](https://www.postman.com/veniceai/workspace/venice-ai-workspace/folder/38652128-b1bd9f3e-507b-46c5-ad35-be7419ea5ad3?action=share\&creator=38652128\&ctx=documentation\&active-environment=38652128-ef110f4e-d3e1-43b5-8029-4d6877e62041).


# Rate Limits and Balances
Source: https://docs.venice.ai/api-reference/endpoint/api_keys/rate_limits

GET /api_keys/rate_limits
Return details about user balances and rate limits.



# Speech API (Beta)
Source: https://docs.venice.ai/api-reference/endpoint/audio/speech

POST /audio/speech
Converts text to speech using various voice models and formats.



# Billing Usage API (Beta)
Source: https://docs.venice.ai/api-reference/endpoint/billing/usage

GET /billing/usage
Get paginated billing usage data for the authenticated user. NOTE: This is a beta endpoint and may be subject to change.

Exports usage data for a user. Descriptions of response fields can be found below:

* **timestamp**: The timestamp the billing usage entry was created
* **sku**: The product associated with the billing usage entry
* **pricePerUnitUsd**: The price per unit in USD
* **unit**: The number of units consumed
* **amount**: The total amount charged for the billing usage entry
* **currency**: The currency charged for the billing usage entry
* **notes**: Notes about the billing usage entry
* **inferenceDetails.requestId**: The request ID associated with the inference
* **inferenceDetails.inferenceExecutionTime**: Time taken for inference execution in milliseconds
* **inferenceDetails.promptTokens**: Number of tokens requested in the prompt. Only present for LLM usage.
* **inferenceDetails.completionTokens**: Number of tokens used in the completion. Only present for LLM usage.


# Get Character
Source: https://docs.venice.ai/api-reference/endpoint/characters/get

GET /characters/{slug}
This is a preview API and may change. Returns a single character by its slug.

## Experimental Endpoint

<Warning>
  This is an experimental endpoint and may be subject to change.
</Warning>

## Postman Collection

For additional examples, please see this [Postman Collection](https://www.postman.com/veniceai/workspace/062d2eda-cd10-4f2f-83b4-083178d85fc5/request/38652128-8cca56f0-e7b7-4afa-855a-c41f9a6d53e2?action=share\&source=copy-link\&creator=48156591\&ctx=documentation).


# List Characters
Source: https://docs.venice.ai/api-reference/endpoint/characters/list

GET /characters
This is a preview API and may change. Returns a list of characters supported in the API.

## Experimental Endpoint

<Warning>
  This is an experimental endpoint and may be subject to change.
</Warning>

## Postman Collection

For additional examples, please see this [Postman Collection](https://www.postman.com/veniceai/workspace/venice-ai-workspace/folder/38652128-b1bd9f3e-507b-46c5-ad35-be7419ea5ad3?action=share\&creator=38652128\&ctx=documentation\&active-environment=38652128-ef110f4e-d3e1-43b5-8029-4d6877e62041).


# Chat Completions
Source: https://docs.venice.ai/api-reference/endpoint/chat/completions

POST /chat/completions
Run text inference based on the supplied parameters. Long running requests should use the streaming API by setting stream=true in your request.

## Postman Collection

For additional examples, please see this [Postman Collection](https://www.postman.com/veniceai/workspace/venice-ai-workspace/folder/38652128-5a71391b-5dd8-4fe8-80be-197a958907fe?action=share\&creator=38652128\&ctx=documentation\&active-environment=38652128-ef110f4e-d3e1-43b5-8029-4d6877e62041).

***


# Model Feature Suffix
Source: https://docs.venice.ai/api-reference/endpoint/chat/model_feature_suffix



Venice supports additional capabilities within it's models that can be powered by the `venice_parameters` input on the chat completions endpoint.

In certain circumstances, you may be using a client that does not let you modify the request body. For those platforms, you can utilize Venice's Model Feature Suffix offering to pass flags in via the model ID.

## Syntax

The Model Feature Suffix follows this pattern:

```
<model_id>:<parameter>=<value>
```

For multiple parameters, chain them with `&`:

```
<model_id>:<parameter1>=<value1>&<parameter2>=<value2>&<parameter3>=<value3>
```

## Examples

### To Set Web Search to Auto

```
default:enable_web_search=auto
```

### To Enable Web Search and Disable System Prompt

```
default:enable_web_search=on&include_venice_system_prompt=false
```

### To Enable Web Search and Add Citations to the Response

```
default:enable_web_search=on&enable_web_citations=true
```

### To Enable Web Search with Full Page Scraping

```
default:enable_web_search=on&enable_web_scraping=true
```

### To Use a Character

```
default:character_slug=alan-watts
```

### To Hide Thinking Blocks on a Reasoning Model Response

```
qwen3-4b:strip_thinking_response=true
```

### To Disable Thinking on Supported Reasoning Models

Certain reasoning models (like Qwen 3) support disabling the thinking process. You can activate using the suffix below:

```
qwen3-4b:disable_thinking=true
```

### To Add Web Search Results to a Streaming Response

This will enable web search, add citations to the response body and include the search results in the stream as the final response message.

You can see an example of this in our [Postman Collection here](https://www.postman.com/veniceai/workspace/venice-ai-workspace/request/38652128-ceef3395-451c-4391-bc7e-a40377e0357b?action=share\&source=copy-link\&creator=38652128\&active-environment=ef110f4e-d3e1-43b5-8029-4d6877e62041).

```
qwen3-4b:enable_web_search=on&enable_web_citations=true&include_search_results_in_stream=true
```

## Postman Example

You can view an example of this feature in our [Postman Collection here](https://www.postman.com/veniceai/workspace/venice-ai-workspace/request/38652128-857f29ff-ee70-4c7c-beba-ef884bdc93be?action=share\&creator=38652128\&ctx=documentation\&active-environment=38652128-ef110f4e-d3e1-43b5-8029-4d6877e62041).


# Generate Embeddings
Source: https://docs.venice.ai/api-reference/endpoint/embeddings/generate

POST /embeddings
Create embeddings for the supplied input.



# Edit (aka Inpaint)
Source: https://docs.venice.ai/api-reference/endpoint/image/edit

POST /image/edit
Edit or modify an image based on the supplied prompt. The image can be provided either as a multipart form-data file upload or as a base64-encoded string in a JSON request.

## Experimental Endpoint

<Warning>
  This is an experimental endpoint and may be subject to change.
</Warning>

## Postman Collection

For additional examples, please see this [Postman Collection](https://www.postman.com/veniceai/workspace/venice-ai-workspace/folder/38652128-2d156cd6-a9bc-4586-8a8b-98e4b5c4435d?action=share\&source=copy-link\&creator=38652128\&ctx=documentation).

***

<Warning>
  Venice’s image editor runs on the Qwen-Image model, which blocks any request that tries to generate or add explicit sexual imagery, sexualise minors or make adults look child-like, or depict real-world violence or gore.
</Warning>


# Generate Images
Source: https://docs.venice.ai/api-reference/endpoint/image/generate

POST /image/generate
Generate an image based on input parameters

## Postman Collection

For additional examples, please see this [Postman Collection](https://www.postman.com/veniceai/workspace/venice-ai-workspace/folder/38652128-0adc004d-2edf-4b88-a3bb-0f868c791c9c?action=share\&source=copy-link\&creator=38652128\&ctx=documentation).

***


# Generate Images (OpenAI Compatible API)
Source: https://docs.venice.ai/api-reference/endpoint/image/generations

POST /images/generations
Generate an image based on input parameters using an OpenAI compatible endpoint. This endpoint does not support the full feature set of the Venice Image Generation endpoint, but is compatible with the existing OpenAI endpoint.



# Image Styles
Source: https://docs.venice.ai/api-reference/endpoint/image/styles

GET /image/styles
List available image styles that can be used with the generate API.

## Postman Collection

For additional examples, please see this [Postman Collection](https://www.postman.com/veniceai/workspace/venice-ai-workspace/folder/38652128-04b32328-197f-4548-b15e-79d4ab0728b1?action=share\&source=copy-link\&creator=38652128\&ctx=documentation).

***


# Upscale and Enhance
Source: https://docs.venice.ai/api-reference/endpoint/image/upscale

POST /image/upscale
Upscale or enhance an image based on the supplied parameters. Using a scale of 1 with enhance enabled will only run the enhancer. The image can be provided either as a multipart form-data file upload or as a base64-encoded string in a JSON request.

## Postman Collection

For additional examples, please see this [Postman Collection](https://www.postman.com/veniceai/workspace/venice-ai-workspace/folder/38652128-8c268e3a-614f-4e49-9816-e4b8d1597818?action=share\&source=copy-link\&creator=38652128\&ctx=documentation).

***


# Compatibility Mapping
Source: https://docs.venice.ai/api-reference/endpoint/models/compatibility_mapping

GET /models/compatibility_mapping
Returns a list of model compatibility mappings and the associated model.

## Postman Collection

For additional examples, please see this [Postman Collection](https://www.postman.com/veniceai/workspace/venice-ai-workspace/folder/38652128-59dfa959-7038-4cd8-b8ba-80cf09f2f026?action=share\&source=copy-link\&creator=38652128\&ctx=documentation).

***


# List Models
Source: https://docs.venice.ai/api-reference/endpoint/models/list

GET /models
Returns a list of available models supported by the Venice.ai API for both text and image inference.

## Postman Collection

For additional examples, please see this [Postman Collection](https://www.postman.com/veniceai/workspace/venice-ai-workspace/folder/38652128-59dfa959-7038-4cd8-b8ba-80cf09f2f026?action=share\&source=copy-link\&creator=38652128\&ctx=documentation).

***


# Traits
Source: https://docs.venice.ai/api-reference/endpoint/models/traits

GET /models/traits
Returns a list of model traits and the associated model.

## Postman Collection

For additional examples, please see this [Postman Collection](https://www.postman.com/veniceai/workspace/venice-ai-workspace/folder/38652128-59dfa959-7038-4cd8-b8ba-80cf09f2f026?action=share\&source=copy-link\&creator=38652128\&ctx=documentation).

***


# Error Codes
Source: https://docs.venice.ai/api-reference/error-codes

Predictable error codes for the Venice API

When an error occurs in the API, we return a consistent error response format that includes an error code, HTTP status code, and a descriptive message. This reference lists all possible error codes that you might encounter while using our API, along with their corresponding HTTP status codes and messages.

| Error Code                           | HTTP Status | Message                                                                                                           | Log Level |
| ------------------------------------ | ----------- | ----------------------------------------------------------------------------------------------------------------- | --------- |
| `AUTHENTICATION_FAILED`              | 401         | Authentication failed                                                                                             | -         |
| `AUTHENTICATION_FAILED_INACTIVE_KEY` | 401         | Authentication failed - Pro subscription is inactive. Please upgrade your subscription to continue using the API. | -         |
| `INVALID_API_KEY`                    | 401         | Invalid API key provided                                                                                          | -         |
| `UNAUTHORIZED`                       | 403         | Unauthorized access                                                                                               | -         |
| `INVALID_REQUEST`                    | 400         | Invalid request parameters                                                                                        | -         |
| `INVALID_MODEL`                      | 400         | Invalid model specified                                                                                           | -         |
| `CHARACTER_NOT_FOUND`                | 404         | No character could be found from the provided character\_slug                                                     | -         |
| `INVALID_CONTENT_TYPE`               | 415         | Invalid content type                                                                                              | -         |
| `INVALID_FILE_SIZE`                  | 413         | File size exceeds maximum limit                                                                                   | -         |
| `INVALID_IMAGE_FORMAT`               | 400         | Invalid image format                                                                                              | -         |
| `CORRUPTED_IMAGE`                    | 400         | The image file is corrupted or unreadable                                                                         | -         |
| `RATE_LIMIT_EXCEEDED`                | 429         | Rate limit exceeded                                                                                               | -         |
| `MODEL_NOT_FOUND`                    | 404         | Specified model not found                                                                                         | -         |
| `INFERENCE_FAILED`                   | 500         | Inference processing failed                                                                                       | error     |
| `UPSCALE_FAILED`                     | 500         | Image upscaling failed                                                                                            | error     |
| `UNKNOWN_ERROR`                      | 500         | An unknown error occurred                                                                                         | error     |


# Rate Limits
Source: https://docs.venice.ai/api-reference/rate-limiting

This page describes the request and token rate limits for the Venice API.

## Failed Request Rate Limits

Failed requests including 500 errors, 503 capacity errors, 429 rate limit errors are should be retried with exponential back off.

For 429 rate limit errors, please use `x-ratelimit-reset-requests` and `x-ratelimit-remaining-requests` to determine when to next retry.

To protect our infrastructure from abuse, if an user generates more than 20 failed requests in a 30 second window, the API will return a 429 error indicating the error rate limit has been reached:

```
Too many failed attempts (> 20) resulting in a non-success status code. Please wait 30s and try again. See https://docs.venice.ai/api-reference/rate-limiting for more information.
```

## Paid Tier Rate Limits

Rate limits apply to users who have purchased API credits or staked VVV to gain Diem.

Helpful links:

* [Real time rate limits](https://docs.venice.ai/api-reference/endpoint/api_keys/rate_limits?playground=open)
* [Rate limit logs](https://docs.venice.ai/api-reference/endpoint/api_keys/rate_limit_logs?playground=open) - View requests that have hit the rate limiter

<Note>We will continue to monitor usage. As we add compute capacity to the network, we will review these limits. If you are consistently hitting rate limits, please contact [**support@venice.ai**](mailto:support@venice.ai) or post in the #API channel in Discord for assistance and we can work with you to raise your limits.</Note>

### Paid Tier - LLMs

***

| Model                 | Model ID          | Req / Min | Req / Day | Tokens / Min |
| --------------------- | ----------------- | :-------: | :-------- | :----------: |
| Llama 3.2 3B          | llama-3.2-3b      |    500    | 288,000   |   1,000,000  |
| Venice Small          | qwen3-4b          |    500    | 288,000   |   1,000,000  |
| Venice Uncensored 1.1 | venice-uncensored |     75    | 54,000    |    750,000   |
| Venice Medium (3.1)   | mistral-31-24b    |     75    | 54,000    |    750,000   |
| Llama 3.3 70B         | llama-3.3-70b     |     50    | 36,000    |    750,000   |
| Venice Large 1.1      | qwen3-235b        |     20    | 15,000    |    750,000   |

### Paid Tier - Image Models

***

| Model            | Model ID | Req / Min | Req / Day |
| ---------------- | -------- | --------- | :-------- |
| All Image Models | All      | 20        | 28,800    |

### Paid Tier - Audio Models

***

| Model            | Model ID | Req / Min | Req / Day |
| ---------------- | -------- | :-------: | :-------: |
| All Audio Models | All      |     60    |   86,400  |

### Paid Tier - Embedding Models

***

| Model  | Model ID              | Req / Min | Req / Day | Tokens / Min |
| ------ | --------------------- | :-------: | :-------- | :----------: |
| BGE-M3 | text-embedding-bge-m3 |    500    | 288,000   |   1,000,000  |

## Rate Limit and Consumption Headers

You can monitor your API utilization and remaining requests by evaluating the following headers:

<div style={{ overflowX: 'auto' }}>
  | Header                                                                       | Description                                                                             |
  | ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
  | <div style={{whiteSpace: 'nowrap'}}>**x-ratelimit-limit-requests**</div>     | The number of requests you've made in the current evaluation period.                    |
  | <div style={{whiteSpace: 'nowrap'}}>**x-ratelimit-remaining-requests**</div> | The remaining requests you can make in the current evaluation period.                   |
  | <div style={{whiteSpace: 'nowrap'}}>**x-ratelimit-reset-requests**</div>     | The unix time stamp when the rate limit will reset.                                     |
  | <div style={{whiteSpace: 'nowrap'}}>**x-ratelimit-limit-tokens**</div>       | The number of total (prompt + completion) tokens used within a 1 minute sliding window. |
  | <div style={{whiteSpace: 'nowrap'}}>**x-ratelimit-remaining-tokens**</div>   | The remaining number of total tokens that can be used during the evaluation period.     |
  | <div style={{whiteSpace: 'nowrap'}}>**x-ratelimit-reset-tokens**</div>       | The duration of time in seconds until the token rate limit resets.                      |
  | <div style={{whiteSpace: 'nowrap'}}>**x-venice-balance-diem**</div>          | The user's Diem balance before the request has been processed.                          |
  | <div style={{whiteSpace: 'nowrap'}}>**x-venice-balance-usd**</div>           | The user's USD balance before the request has been processed.                           |
</div>


# Venice AI
Source: https://docs.venice.ai/overview/about-venice



# The AI platform that doesn't spy on you

Build AI with no data retention, permissionless access, and compute you permanently own.

<CardGroup cols={3}>
  <Card title="Start Building" href="/overview/getting-started" target="_blank" icon="rocket">
    Make your first request in minutes.
  </Card>

  <Card title="View Models" href="/overview/models" target="_blank" icon="database">
    Compare capabilities, context, and base models.
  </Card>

  <Card title="API Reference" href="/api-reference" target="_blank" icon="rectangle-code">
    Endpoints, payloads, and examples.
  </Card>
</CardGroup>

## OpenAI Compatibility

Use your existing OpenAI code with just a base URL change.

<CodeGroup>
  ```bash Curl theme={null}
  curl https://api.venice.ai/api/v1/chat/completions \
    -H "Authorization: Bearer $VENICE_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "venice-uncensored",
      "messages": [{"role": "user", "content": "Hello World!"}]
    }'
  ```

  ```ts TypeScript theme={null}
  import OpenAI from "openai";

  const openai = new OpenAI({
    apiKey: process.env.VENICE_API_KEY!,
    baseURL: "https://api.venice.ai/api/v1",
  });

  const completion = await openai.chat.completions.create({
    model: "venice-uncensored",
    messages: [{ role: "user", content: "Hello World!" }],
  });

  console.log(completion.choices[0].message.content);
  ```

  ```python Python theme={null}
  import openai

  client = openai.OpenAI(
      api_key="your-api-key",
      base_url="https://api.venice.ai/api/v1"
  )

  response = client.chat.completions.create(
      model="venice-uncensored",
      messages=[{"role": "user", "content": "Hello World!"}]
  )

  print(response.choices[0].message.content)
  ```

  ```go Go theme={null}
  package main

  import (
      "context"
      "fmt"
      "os"
      "github.com/openai/openai-go"
  )

  func main() {
      client, err := openai.NewClient(os.Getenv("VENICE_API_KEY"))
      if err != nil {
          fmt.Printf("Error creating client: %v\n", err)
          return
      }
      
      client.BaseURL = "https://api.venice.ai/api/v1"
      
      resp, err := client.CreateChatCompletion(
          context.Background(),
          openai.ChatCompletionRequest{
              Model: "venice-uncensored",
              Messages: []openai.ChatCompletionMessage{
                  {
                      Role:    openai.ChatMessageRoleUser,
                      Content: "Hello World!",
                  },
              },
          },
      )
      
      if err != nil {
          fmt.Printf("Error: %v\n", err)
          return
      }
      
      fmt.Println(resp.Choices[0].Message.Content)
  }
  ```

  ```php PHP theme={null}
  <?php

  require_once 'vendor/autoload.php';

  use OpenAI\Client;

  $client = OpenAI::client('your-api-key');
  $client->setBaseUrl('https://api.venice.ai/api/v1');

  $response = $client->chat()->create([
      'model' => 'venice-uncensored',
      'messages' => [
          [
              'role' => 'user',
              'content' => 'Hello World!'
          ]
      ]
  ]);

  echo $response->choices[0]->message->content;
  ```

  ```csharp C# theme={null}
  using OpenAI;

  var client = new OpenAIClient("your-api-key");
  client.BaseUrl = "https://api.venice.ai/api/v1";

  var chatCompletion = await client.GetChatCompletionsAsync(new ChatCompletionOptions
  {
      Model = "venice-uncensored",
      Messages = { new ChatMessage(ChatRole.User, "Hello World!") }
  });

  Console.WriteLine(chatCompletion.Value.Choices[0].Message.Content);
  ```

  ```java Java theme={null}
  import com.openai.OpenAI;
  import com.openai.OpenAIHttpException;
  import com.openai.core.ApiError;
  import com.openai.types.chat.ChatCompletionRequest;
  import com.openai.types.chat.ChatCompletionResponse;
  import com.openai.types.chat.ChatMessage;

  public class Main {
      public static void main(String[] args) {
          OpenAI client = OpenAI.builder()
              .apiKey(System.getenv("VENICE_API_KEY"))
              .baseUrl("https://api.venice.ai/api/v1")
              .build();

          try {
              ChatCompletionResponse response = client.chatCompletions().create(
                  ChatCompletionRequest.builder()
                      .model("venice-uncensored")
                      .messages(ChatMessage.of("Hello World!"))
                      .build()
              );
              
              System.out.println(response.choices().get(0).message().content());
          } catch (OpenAIHttpException e) {
              System.err.println("Error: " + e.getMessage());
          }
      }
  }
  ```

  ```swift Swift theme={null}
  import OpenAI

  let client = OpenAI(apiToken: "your-api-key")
  client.baseURL = "https://api.venice.ai/api/v1"

  Task {
      do {
          let response = try await client.chats.create(
              model: "venice-uncensored",
              messages: [.init(role: .user, content: "Hello World!")]
          )
          
          print(response.choices[0].message.content ?? "")
      } catch {
          print("Error: \(error)")
      }
  }
  ```
</CodeGroup>

## Build with Venice APIs

Access chat, image generation (generate/upscale/edit), audio (TTS), and characters.

<CardGroup cols={2}>
  <Card title="Chat Completions" href="/api-reference/endpoint/chat/completions" icon="message">
    **Text + reasoning**

    Vision, tool use, streaming
  </Card>

  <Card title="Image Generation" href="/api-reference/endpoint/image/generations" icon="image">
    **Generate, upscale, and edit**

    Models for styles, quality, and uncensored
  </Card>

  <Card title="Audio Synthesis" href="/api-reference/endpoint/audio/speech" icon="headphones">
    **Text → speech**

    60+ multilingual voices
  </Card>

  <Card title="AI Characters" href="/api-reference/endpoint/characters/list" icon="user">
    **Characters API**

    Create, list, and chat with personas
  </Card>
</CardGroup>

[View all API endpoints →](/api-reference)

## Popular Models

Copy a Model ID and use it as `model` in your requests.

<Card title="Venice Large 1.1" icon="brain">
  Flagship model for deep reasoning and production agents.

  Model ID: `qwen3-235b`
  Base: Qwen 3 235B (Venice‑tuned)
  Context: 131k • Modalities: Text → Text

  **Use cases**

  * Agent planning and tool use
  * Complex code & system design
  * Long‑context reasoning

  ```json  theme={null}
  {"model":"qwen3-235b","messages":[{"role":"user","content":"Plan a zero‑downtime DB migration in 3 steps"}]}
  ```
</Card>

<CardGroup cols={2}>
  <Card title="Venice Uncensored" icon="shield">
    **Unfiltered generation**

    Model ID: `venice-uncensored`

    Base model: Venice Uncensored 1.1

    Context: 32k • Best for: uncensored creative, red‑team testing

    ```json  theme={null}
    {"model":"venice-uncensored","messages":[{"role":"user","content":"Write an unfiltered analysis of content moderation policies"}]}
    ```
  </Card>

  <Card title="Venice Medium 3.1" icon="eye">
    **Vision + tools**

    Model ID: `mistral-31-24b`

    Base model: Mistral 3.1 24B

    Context: 131k • Supports: Vision, Function calling, image analysis

    ```json  theme={null}
    {"model":"mistral-31-24b","messages":[{"role":"user","content":"Describe this image"}]}
    ```
  </Card>

  <Card title="Venice Small" icon="bolt">
    **Fast and cost‑efficient**

    Model ID: `qwen3-4b`

    Base model: Qwen 3 4B

    Context: 40k • Best for: chatbots, classification, light reasoning

    ```json  theme={null}
    {"model":"qwen3-4b","messages":[{"role":"user","content":"Summarize:"}]}
    ```
  </Card>

  <Card title="Venice SD35" icon="image">
    **Image generation**

    Model ID: `venice-sd35`

    Base model: SD3.5 Large

    Best for: Text‑to‑image, photorealism, product shots, light upscaling

    ```json  theme={null}
    {"model":"venice-sd35","prompt":"a serene canal in venice at sunset"}
    ```
  </Card>
</CardGroup>

[View all models →](/overview/models)

## Extend models with built‑in tools

Toggle on compatible models using `venice_parameters` or model suffixes

<CardGroup cols={4}>
  <Card title="Web Search" icon="globe">
    **Real‑time web results**
  </Card>

  <Card title="Reasoning Mode" icon="brain">
    **Advanced reasoning**
  </Card>

  <Card title="Vision Processing" icon="eye">
    **Image understanding**
  </Card>

  <Card title="Function Calling" icon="link">
    **Tool use / APIs**
  </Card>
</CardGroup>

<Accordion title="Web Search Code Samples">
  Enable real-time web search with citations on **all text models**. Get up-to-date information from the internet and include source citations in responses. Works with any Venice text model.

  <CodeGroup>
    ```bash Curl theme={null}
    curl https://api.venice.ai/api/v1/chat/completions \
      -H "Authorization: Bearer $VENICE_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "qwen3-235b",
        "messages": [{"role": "user", "content": "What are the latest developments in AI?"}],
        "venice_parameters": {
          "enable_web_search": "auto"
        }
      }'
    ```

    ```ts TypeScript theme={null}
    import OpenAI from "openai";

    const openai = new OpenAI({
      apiKey: process.env.VENICE_API_KEY!,
      baseURL: "https://api.venice.ai/api/v1",
    });

    const completion = await openai.chat.completions.create({
      model: "qwen3-235b",
      messages: [{ role: "user", content: "What are the latest developments in AI?" }],
      // @ts-ignore - Venice-specific parameter
      venice_parameters: {
        enable_web_search: "auto"
      }
    });

    console.log(completion.choices[0].message.content);
    ```

    ```python Python theme={null}
    import openai

    client = openai.OpenAI(
        api_key="your-api-key",
        base_url="https://api.venice.ai/api/v1"
    )

    response = client.chat.completions.create(
        model="qwen3-235b",
        messages=[{"role": "user", "content": "What are the latest developments in AI?"}],
            extra_body={
            "venice_parameters": {
                "enable_web_search": "auto"
            }
        }
    )

    print(response.choices[0].message.content)
    ```

    ```go Go theme={null}
    package main

    import (
        "context"
        "fmt"
        "os"
        "github.com/openai/openai-go"
    )

    func main() {
        client, err := openai.NewClient(os.Getenv("VENICE_API_KEY"))
        if err != nil {
            fmt.Printf("Error creating client: %v\n", err)
            return
        }
        
        client.BaseURL = "https://api.venice.ai/api/v1"
        
        // Note: Go client doesn't support venice_parameters directly
        // Use model suffix approach instead
        resp, err := client.CreateChatCompletion(
            context.Background(),
            openai.ChatCompletionRequest{
                Model: "qwen3-235b:enable_web_search=on&enable_web_citations=true",
                Messages: []openai.ChatCompletionMessage{
                    {
                        Role:    openai.ChatMessageRoleUser,
                        Content: "What are the latest developments in AI?",
                    },
                },
            },
        )
        
        if err != nil {
            fmt.Printf("Error: %v\n", err)
            return
        }
        
        fmt.Println(resp.Choices[0].Message.Content)
    }
    ```

    ```php PHP theme={null}
    <?php

    require_once 'vendor/autoload.php';

    use OpenAI\Client;

    $client = OpenAI::client('your-api-key');
    $client->setBaseUrl('https://api.venice.ai/api/v1');

    $response = $client->chat()->create([
        'model' => 'qwen3-235b:enable_web_search=on&enable_web_citations=true',
        'messages' => [
            [
                'role' => 'user',
                'content' => 'What are the latest developments in AI?'
            ]
        ]
    ]);

    echo $response->choices[0]->message->content;
    ```

    ```csharp C# theme={null}
    using OpenAI;

    var client = new OpenAIClient("your-api-key");
    client.BaseUrl = "https://api.venice.ai/api/v1";

    var chatCompletion = await client.GetChatCompletionsAsync(new ChatCompletionOptions
    {
        Model = "qwen3-235b:enable_web_search=on&enable_web_citations=true",
        Messages = { new ChatMessage(ChatRole.User, "What are the latest developments in AI?") }
    });

    Console.WriteLine(chatCompletion.Value.Choices[0].Message.Content);
    ```

    ```java Java theme={null}
    import com.openai.OpenAI;
    import com.openai.OpenAIHttpException;
    import com.openai.core.ApiError;
    import com.openai.types.chat.ChatCompletionRequest;
    import com.openai.types.chat.ChatCompletionResponse;
    import com.openai.types.chat.ChatMessage;

    public class Main {
        public static void main(String[] args) {
            OpenAI client = OpenAI.builder()
                .apiKey(System.getenv("VENICE_API_KEY"))
                .baseUrl("https://api.venice.ai/api/v1")
                .build();

            try {
                ChatCompletionResponse response = client.chatCompletions().create(
                    ChatCompletionRequest.builder()
                        .model("qwen3-235b:enable_web_search=on&enable_web_citations=true")
                        .messages(ChatMessage.of("What are the latest developments in AI?"))
                        .build()
                );
                
                System.out.println(response.choices().get(0).message().content());
            } catch (OpenAIHttpException e) {
                System.err.println("Error: " + e.getMessage());
            }
        }
    }
    ```

    ```bash Model Suffix theme={null}
    # Alternative approach: append parameters directly to model ID
    curl https://api.venice.ai/api/v1/chat/completions \
      -H "Authorization: Bearer $VENICE_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "qwen3-235b:enable_web_search=on&enable_web_citations=true",
        "messages": [{"role": "user", "content": "What are the latest developments in AI?"}]
      }'
    ```
  </CodeGroup>
</Accordion>

<Accordion title="Reasoning Mode Code Samples">
  Advanced step-by-step reasoning with visible thinking process. Available on **reasoning models**: `qwen3-4b`, `qwen3-235b`. Shows detailed problem-solving steps in `<think>` tags.

  <CodeGroup>
    ```bash Curl theme={null}
    curl https://api.venice.ai/api/v1/chat/completions \
      -H "Authorization: Bearer $VENICE_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "qwen3-235b",
        "messages": [{"role": "user", "content": "Solve: If x + 2y = 10 and 3x - y = 5, what are x and y?"}],
        "venice_parameters": {
          "strip_thinking_response": false
        }
      }'
    ```

    ```ts TypeScript theme={null}
    import OpenAI from "openai";

    const openai = new OpenAI({
      apiKey: process.env.VENICE_API_KEY!,
      baseURL: "https://api.venice.ai/api/v1",
    });

    const completion = await openai.chat.completions.create({
      model: "qwen3-235b",
      messages: [{ role: "user", content: "Solve: If x + 2y = 10 and 3x - y = 5, what are x and y?" }],
      // @ts-ignore - Venice-specific parameter
      venice_parameters: {
        strip_thinking_response: false
      }
    });

    console.log(completion.choices[0].message.content);
    ```

    ```python Python theme={null}
    import openai

    client = openai.OpenAI(
        api_key="your-api-key",
        base_url="https://api.venice.ai/api/v1"
    )

    response = client.chat.completions.create(
        model="qwen3-235b",
        messages=[{"role": "user", "content": "Solve: If x + 2y = 10 and 3x - y = 5, what are x and y?"}],
        extra_body={
            "venice_parameters": {
                "strip_thinking_response": False
            }
        }
    )

    print(response.choices[0].message.content)
    ```

    ```go Go theme={null}
    package main

    import (
        "context"
        "fmt"
        "os"
        "github.com/openai/openai-go"
    )

    func main() {
        client, err := openai.NewClient(os.Getenv("VENICE_API_KEY"))
        if err != nil {
            fmt.Printf("Error creating client: %v\n", err)
            return
        }
        
        client.BaseURL = "https://api.venice.ai/api/v1"
        
        resp, err := client.CreateChatCompletion(
            context.Background(),
            openai.ChatCompletionRequest{
                Model: "qwen3-235b",
                Messages: []openai.ChatCompletionMessage{
                    {
                        Role:    openai.ChatMessageRoleUser,
                        Content: "Solve: If x + 2y = 10 and 3x - y = 5, what are x and y?",
                    },
                },
            },
        )
        
        if err != nil {
            fmt.Printf("Error: %v\n", err)
            return
        }
        
        fmt.Println(resp.Choices[0].Message.Content)
    }
    ```

    ```php PHP theme={null}
    <?php

    require_once 'vendor/autoload.php';

    use OpenAI\Client;

    $client = OpenAI::client('your-api-key');
    $client->setBaseUrl('https://api.venice.ai/api/v1');

    $response = $client->chat()->create([
        'model' => 'qwen3-235b',
        'messages' => [
            [
                'role' => 'user',
                'content' => 'Solve: If x + 2y = 10 and 3x - y = 5, what are x and y?'
            ]
        ]
    ]);

    echo $response->choices[0]->message->content;
    ```

    ```csharp C# theme={null}
    using OpenAI;

    var client = new OpenAIClient("your-api-key");
    client.BaseUrl = "https://api.venice.ai/api/v1";

    var chatCompletion = await client.GetChatCompletionsAsync(new ChatCompletionOptions
    {
        Model = "qwen3-235b",
        Messages = { new ChatMessage(ChatRole.User, "Solve: If x + 2y = 10 and 3x - y = 5, what are x and y?") }
    });

    Console.WriteLine(chatCompletion.Value.Choices[0].Message.Content);
    ```

    ```java Java theme={null}
    import com.openai.OpenAI;
    import com.openai.OpenAIHttpException;
    import com.openai.core.ApiError;
    import com.openai.types.chat.ChatCompletionRequest;
    import com.openai.types.chat.ChatCompletionResponse;
    import com.openai.types.chat.ChatMessage;

    public class Main {
        public static void main(String[] args) {
            OpenAI client = OpenAI.builder()
                .apiKey(System.getenv("VENICE_API_KEY"))
                .baseUrl("https://api.venice.ai/api/v1")
                .build();

            try {
                ChatCompletionResponse response = client.chatCompletions().create(
                    ChatCompletionRequest.builder()
                        .model("qwen3-235b")
                        .messages(ChatMessage.of("Solve: If x + 2y = 10 and 3x - y = 5, what are x and y?"))
                        .build()
                );
                
                System.out.println(response.choices().get(0).message().content());
            } catch (OpenAIHttpException e) {
                System.err.println("Error: " + e.getMessage());
            }
        }
    }
    ```

    ```bash Model Suffix theme={null}
    # Alternative approach: append parameters directly to model ID
    curl https://api.venice.ai/api/v1/chat/completions \
      -H "Authorization: Bearer $VENICE_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "qwen3-235b:strip_thinking_response=true",
        "messages": [{"role": "user", "content": "Solve this math problem"}]
      }'
    ```
  </CodeGroup>
</Accordion>

<Accordion title="Vision Processing Code Samples">
  Image understanding and multimodal analysis. Available on **vision models**: `mistral-31-24b`. Upload images via base64 data URIs or URLs for analysis, description, and reasoning.

  <CodeGroup>
    ```bash Curl theme={null}
    curl https://api.venice.ai/api/v1/chat/completions \
      -H "Authorization: Bearer $VENICE_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "mistral-31-24b",
        "messages": [
          {
            "role": "user",
            "content": [
              {"type": "text", "text": "What do you see in this image?"},
              {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,..."}}
            ]
          }
        ]
      }'
    ```

    ```ts TypeScript theme={null}
    import OpenAI from "openai";

    const openai = new OpenAI({
      apiKey: process.env.VENICE_API_KEY!,
      baseURL: "https://api.venice.ai/api/v1",
    });

    const completion = await openai.chat.completions.create({
      model: "mistral-31-24b",
      messages: [
        {
          role: "user",
          content: [
            { type: "text", text: "What do you see in this image?" },
            { type: "image_url", image_url: { url: "data:image/jpeg;base64,..." } }
          ]
        }
      ]
    });

    console.log(completion.choices[0].message.content);
    ```

    ```python Python theme={null}
    import openai

    client = openai.OpenAI(
        api_key="your-api-key",
        base_url="https://api.venice.ai/api/v1"
    )

    response = client.chat.completions.create(
        model="mistral-31-24b",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What do you see in this image?"},
                    {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,..."}}
                ]
            }
        ]
    )

    print(response.choices[0].message.content)
    ```

    ```go Go theme={null}
    package main

    import (
        "context"
        "fmt"
        "os"
        "github.com/openai/openai-go"
    )

    func main() {
        client, err := openai.NewClient(os.Getenv("VENICE_API_KEY"))
        if err != nil {
            fmt.Printf("Error creating client: %v\n", err)
            return
        }
        
        client.BaseURL = "https://api.venice.ai/api/v1"
        
        resp, err := client.CreateChatCompletion(
            context.Background(),
            openai.ChatCompletionRequest{
                Model: "mistral-31-24b",
                Messages: []openai.ChatCompletionMessage{
                    {
                        Role: openai.ChatMessageRoleUser,
                        Content: []openai.ChatCompletionContentPart{
                            {Type: "text", Text: "What do you see in this image?"},
                            {Type: "image_url", ImageURL: &openai.ChatCompletionContentPartImageURL{URL: "data:image/jpeg;base64,..."}},
                        },
                    },
                },
            },
        )
        
        if err != nil {
            fmt.Printf("Error: %v\n", err)
            return
        }
        
        fmt.Println(resp.Choices[0].Message.Content)
    }
    ```

    ```php PHP theme={null}
    <?php

    require_once 'vendor/autoload.php';

    use OpenAI\Client;

    $client = OpenAI::client('your-api-key');
    $client->setBaseUrl('https://api.venice.ai/api/v1');

    $response = $client->chat()->create([
        'model' => 'mistral-31-24b',
        'messages' => [
            [
                'role' => 'user',
                'content' => [
                    ['type' => 'text', 'text' => 'What do you see in this image?'],
                    ['type' => 'image_url', 'image_url' => ['url' => 'data:image/jpeg;base64,...']]
                ]
            ]
        ]
    ]);

    echo $response->choices[0]->message->content;
    ```

    ```csharp C# theme={null}
    using OpenAI;

    var client = new OpenAIClient("your-api-key");
    client.BaseUrl = "https://api.venice.ai/api/v1";

    var chatCompletion = await client.GetChatCompletionsAsync(new ChatCompletionOptions
    {
        Model = "mistral-31-24b",
        Messages = { 
            new ChatMessage(ChatRole.User, [
                ChatMessageContentPart.CreateTextPart("What do you see in this image?"),
                ChatMessageContentPart.CreateImagePart(new Uri("data:image/jpeg;base64,..."))
            ])
        }
    });

    Console.WriteLine(chatCompletion.Value.Choices[0].Message.Content);
    ```

    ```java Java theme={null}
    import com.openai.OpenAI;
    import com.openai.OpenAIHttpException;
    import com.openai.core.ApiError;
    import com.openai.types.chat.*;

    public class Main {
        public static void main(String[] args) {
            OpenAI client = OpenAI.builder()
                .apiKey(System.getenv("VENICE_API_KEY"))
                .baseUrl("https://api.venice.ai/api/v1")
                .build();

            try {
                ChatCompletionResponse response = client.chatCompletions().create(
                    ChatCompletionRequest.builder()
                        .model("mistral-31-24b")
                        .messages(ChatMessage.builder()
                            .role(ChatMessage.Role.USER)
                            .content(ChatMessage.Content.ofMultiple(
                                ChatMessage.ContentPart.text("What do you see in this image?"),
                                ChatMessage.ContentPart.imageUrl("data:image/jpeg;base64,...")
                            ))
                            .build())
                        .build()
                );
                
                System.out.println(response.choices().get(0).message().content());
            } catch (OpenAIHttpException e) {
                System.err.println("Error: " + e.getMessage());
            }
        }
    }
    ```

    ```bash Model Suffix theme={null}
    # Alternative approach: append parameters directly to model ID
    curl https://api.venice.ai/api/v1/chat/completions \
      -H "Authorization: Bearer $VENICE_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "mistral-31-24b:enable_web_search=auto",
        "messages": [
          {
            "role": "user",
            "content": [
              {"type": "text", "text": "What do you see in this image and find similar examples online?"},
              {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,..."}}
            ]
          }
        ]
      }'
    ```
  </CodeGroup>
</Accordion>

<Accordion title="Function Calling Code Samples">
  Tool use and external API integration. Available on **function calling models**: `qwen3-235b`, `qwen3-4b`, `mistral-31-24b`, `llama-3.2-3b`, `llama-3.3-70b`. Define tools for the model to call external APIs, databases, or custom functions.

  <CodeGroup>
    ```bash Curl theme={null}
    curl https://api.venice.ai/api/v1/chat/completions \
      -H "Authorization: Bearer $VENICE_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "qwen3-235b",
        "messages": [{"role": "user", "content": "What is the weather like in New York?"}],
        "tools": [
          {
            "type": "function",
            "function": {
              "name": "get_weather",
              "description": "Get current weather for a location",
              "parameters": {
                "type": "object",
                "properties": {
                  "location": {"type": "string", "description": "City name"}
                },
                "required": ["location"]
              }
            }
          }
        ]
      }'
    ```

    ```ts TypeScript theme={null}
    import OpenAI from "openai";

    const openai = new OpenAI({
      apiKey: process.env.VENICE_API_KEY!,
      baseURL: "https://api.venice.ai/api/v1",
    });

    const completion = await openai.chat.completions.create({
      model: "qwen3-235b",
      messages: [{ role: "user", content: "What is the weather like in New York?" }],
      tools: [
        {
          type: "function",
          function: {
            name: "get_weather",
            description: "Get current weather for a location",
            parameters: {
              type: "object",
              properties: {
                location: { type: "string", description: "City name" }
              },
              required: ["location"]
            }
          }
        }
      ]
    });

    console.log(completion.choices[0].message.content);
    ```

    ```python Python theme={null}
    import openai

    client = openai.OpenAI(
        api_key="your-api-key",
        base_url="https://api.venice.ai/api/v1"
    )

    response = client.chat.completions.create(
        model="qwen3-235b",
        messages=[{"role": "user", "content": "What is the weather like in New York?"}],
        tools=[
            {
                "type": "function",
                "function": {
                    "name": "get_weather",
                    "description": "Get current weather for a location",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "location": {"type": "string", "description": "City name"}
                        },
                        "required": ["location"]
                    }
                }
            }
        ]
    )

    print(response.choices[0].message.content)
    ```

    ```go Go theme={null}
    package main

    import (
        "context"
        "fmt"
        "os"
        "github.com/openai/openai-go"
    )

    func main() {
        client, err := openai.NewClient(os.Getenv("VENICE_API_KEY"))
        if err != nil {
            fmt.Printf("Error creating client: %v\n", err)
            return
        }
        
        client.BaseURL = "https://api.venice.ai/api/v1"
        
        resp, err := client.CreateChatCompletion(
            context.Background(),
            openai.ChatCompletionRequest{
                Model: "qwen3-235b",
                Messages: []openai.ChatCompletionMessage{
                    {
                        Role:    openai.ChatMessageRoleUser,
                        Content: "What is the weather like in New York?",
                    },
                },
                Tools: []openai.ChatCompletionTool{
                    {
                        Type: openai.ChatCompletionToolTypeFunction,
                        Function: &openai.FunctionDefinition{
                            Name:        "get_weather",
                            Description: "Get current weather for a location",
                            Parameters: map[string]interface{}{
                                "type": "object",
                                "properties": map[string]interface{}{
                                    "location": map[string]interface{}{
                                        "type":        "string",
                                        "description": "City name",
                                    },
                                },
                                "required": []string{"location"},
                            },
                        },
                    },
                },
            },
        )
        
        if err != nil {
            fmt.Printf("Error: %v\n", err)
            return
        }
        
        fmt.Println(resp.Choices[0].Message.Content)
    }
    ```

    ```php PHP theme={null}
    <?php

    require_once 'vendor/autoload.php';

    use OpenAI\Client;

    $client = OpenAI::client('your-api-key');
    $client->setBaseUrl('https://api.venice.ai/api/v1');

    $response = $client->chat()->create([
        'model' => 'qwen3-235b',
        'messages' => [
            [
                'role' => 'user',
                'content' => 'What is the weather like in New York?'
            ]
        ],
        'tools' => [
            [
                'type' => 'function',
                'function' => [
                    'name' => 'get_weather',
                    'description' => 'Get current weather for a location',
                    'parameters' => [
                        'type' => 'object',
                        'properties' => [
                            'location' => [
                                'type' => 'string',
                                'description' => 'City name'
                            ]
                        ],
                        'required' => ['location']
                    ]
                ]
            ]
        ]
    ]);

    echo $response->choices[0]->message->content;
    ```

    ```csharp C# theme={null}
    using OpenAI;

    var client = new OpenAIClient("your-api-key");
    client.BaseUrl = "https://api.venice.ai/api/v1";

    var chatCompletion = await client.GetChatCompletionsAsync(new ChatCompletionOptions
    {
        Model = "qwen3-235b",
        Messages = { new ChatMessage(ChatRole.User, "What is the weather like in New York?") },
        Tools = {
            ChatTool.CreateFunctionTool(
                functionName: "get_weather",
                functionDescription: "Get current weather for a location",
                functionParameters: BinaryData.FromString("""
                {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "City name"
                        }
                    },
                    "required": ["location"]
                }
                """)
            )
        }
    });

    Console.WriteLine(chatCompletion.Value.Choices[0].Message.Content);
    ```

    ```java Java theme={null}
    import com.openai.OpenAI;
    import com.openai.OpenAIHttpException;
    import com.openai.core.ApiError;
    import com.openai.types.chat.*;

    public class Main {
        public static void main(String[] args) {
            OpenAI client = OpenAI.builder()
                .apiKey(System.getenv("VENICE_API_KEY"))
                .baseUrl("https://api.venice.ai/api/v1")
                .build();

            try {
                ChatCompletionResponse response = client.chatCompletions().create(
                    ChatCompletionRequest.builder()
                        .model("qwen3-235b")
                        .messages(ChatMessage.of("What is the weather like in New York?"))
                        .tools(ChatCompletionTool.builder()
                            .type(ChatCompletionToolType.FUNCTION)
                            .function(FunctionDefinition.builder()
                                .name("get_weather")
                                .description("Get current weather for a location")
                                .parameters(FunctionParameters.builder()
                                    .putProperty("location", FunctionParameters.Property.builder()
                                        .type("string")
                                        .description("City name")
                                        .build())
                                    .required("location")
                                    .build())
                                .build())
                            .build())
                        .build()
                );
                
                System.out.println(response.choices().get(0).message().content());
            } catch (OpenAIHttpException e) {
                System.err.println("Error: " + e.getMessage());
            }
        }
    }
    ```

    ```bash Model Suffix theme={null}
    # Alternative approach: append parameters directly to model ID
    curl https://api.venice.ai/api/v1/chat/completions \
      -H "Authorization: Bearer $VENICE_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "qwen3-235b:enable_web_search=auto",
        "messages": [{"role": "user", "content": "What is the weather like in New York?"}],
        "tools": [
          {
            "type": "function",
            "function": {
              "name": "get_weather",
              "description": "Get current weather for a location",
              "parameters": {
                "type": "object",
                "properties": {
                  "location": {"type": "string", "description": "City name"}
                },
                "required": ["location"]
              }
            }
          }
        ]
      }'
    ```
  </CodeGroup>
</Accordion>

### Available Parameters

| Parameter                      | Options             | Description                             |
| ------------------------------ | ------------------- | --------------------------------------- |
| `enable_web_search`            | `off`, `on`, `auto` | Enable real-time web search             |
| `enable_web_scraping`          | `true`, `false`     | Scrape URLs detected in user message    |
| `enable_web_citations`         | `true`, `false`     | Include citations in web search results |
| `strip_thinking_response`      | `true`, `false`     | Hide reasoning steps from response      |
| `disable_thinking`             | `true`, `false`     | Disable reasoning mode entirely         |
| `include_venice_system_prompt` | `true`, `false`     | Include Venice system prompts           |
| `character_slug`               | string              | Use a specific AI character             |

[View all parameters →](/api-reference/api-spec#venice-parameters)

## Pricing Options

<CardGroup cols={3}>
  <Card title="Pro subscription" href="https://venice.ai/chat" icon="star">
    **\$10 in free credits**

    One‑time credit when you upgrade
  </Card>

  <Card title="Buy DIEM" href="https://venice.ai/token" icon="coins">
    **Permanent access**

    Stake DIEM for daily compute allocation
  </Card>

  <Card title="Pay-as-you-go (USD)" href="/overview/pricing" icon="credit-card">
    **USD payments**

    Fund your account in USD and pay per usage
  </Card>
</CardGroup>

## Start building today

Get your API key and make your first request.

<CardGroup cols={2}>
  <Card title="Getting Started" href="/overview/getting-started" icon="rocket">
    Step-by-step guide to your first API call
  </Card>

  <Card title="API Reference" href="/api-reference" icon="rectangle-code">
    Complete API documentation and endpoints
  </Card>

  <Card title="Postman Collection" href="/overview/guides/postman" icon="play">
    Ready-to-use API examples and testing
  </Card>

  <Card title="AI Agents" href="/overview/guides/ai-agents" icon="robot">
    Build with Eliza and other agent frameworks
  </Card>
</CardGroup>

<Warning>
  Venice's API is rapidly evolving. Join our [Discord](https://discord.gg/askvenice) to provide feedback and request new features. Your input shapes our development roadmap.
</Warning>

***

These docs are open source and can be contributed to on [Github](https://github.com/veniceai/api-docs). For additional guidance, see our blog post: ["How to use Venice API"](https://venice.ai/blog/how-to-use-venice-api)


# Deprecations
Source: https://docs.venice.ai/overview/deprecations

Model inclusion and lifecycle policy and deprecations for the Venice API

## Model inclusion and lifecycle policy for the Venice API

The Venice API exists to give developers unrestricted private access to production-grade models free from hidden filters or black-box decisions.

As models improve, we occasionally retire older ones in favor of smarter, faster, or more capable alternatives. We design these transitions to be predictable and low‑friction.

## Model Deprecations

We know deprecations can be disruptive. That’s why we aim to deprecate only when necessary, and we design features like traits and Venice-branded models to minimize disruption.

We may deprecate a model when:

* A newer model offers a clear improvement for the same use case
* The model no longer meets our standards for performance or reliability
* It sees consistently low usage, and continuing to support it would fragment the experience for everyone else

## Deprecation Process

When a model meets deprecation criteria, we announce the change with 30–60 days' notice. Deprecation notices are published via the [changelog](https://featurebase.venice.ai/changelog) and our [Discord server](https://discord.gg/askvenice). When you call a deprecated model during the notice period, the API response will include a deprecation warning.

During the notice period, the model remains available, though in some cases we may reduce infrastructure capacity. We always provide a recommended replacement, and when needed, offer migration guidance to help the transition.

After the sunset date, requests to the model will automatically route to a model of similar processing power at the same or lower price. If routing is not possible for technical or safety reasons, the API will return a 410 Gone response. If a deprecated model was selected via a trait (such as `default_code`, `default_vision`, or `fastest`) that trait will be reassigned to a compatible replacement.

We never remove models silently or alter behavior without versioning. You’ll always know what’s running and how to prepare for what’s next.

<Note>
  Performance-only upgrades: We may roll out improvements that preserve model behavior while improving performance, latency, or cost efficiency. These updates are backward-compatible and require no customer action.
</Note>

See the [Model Deprecation Tracker](#model-deprecation-tracker) below. For earlier announcements, consult the [changelog](https://featurebase.venice.ai/changelog) and our [Discord server](https://discord.gg/askvenice).

## How models are selected for the Venice API

We carefully select which models to make available based on performance, reliability, and real-world developer needs. To be included, a model must demonstrate strong performance, behave consistently under OpenAI-compatible endpoints, and offer a clear improvement over at least one of the models we already support.

Models we’re evaluating may first be released in beta to gather feedback and validate performance at scale.

We don’t expose models that are redundant, unproven, or not ready for consistent production use. Our goal is to keep the Venice API clean, capable, and optimized for what developers actually build.

Learn more in [Model Deprecations](/overview/deprecations#model-deprecations) and <a href="/overview/models" target="_blank" rel="noopener noreferrer">Current Model List</a>.

## Versioning and Aliases

All Venice models are identified by a unique, permanent ID. For example:

`venice-uncensored`
`qwen3-235b`
`llama-3.3-70b`
`mistral-31-24b`

Model IDs are stable. If there's a breaking change, we will release a new model ID (for example, add a version like v2). If there are no breaking changes, we may update the existing model and will communicate significant changes.

To provide flexibility, Venice also maintains symbolic aliases — implemented through traits — that point to the recommended default model for a given task. Examples include:

* `default` → currently routes to `llama-3.3-70b`
* `function_calling_default` → currently routes to `llama-3.3-70b`
* `default_vision` → currently routes to `mistral-31-24b`
* `most_uncensored` → currently routes to `venice-uncensored`
* `fastest` → currently routes to `llama-3.2-3b`

Traits offer a stable abstraction for selecting models while giving Venice the flexibility to improve the underlying implementation. Developers who prefer automatic access to the latest recommended models can rely on trait-based aliases.

For applications that require strict consistency and predictable behavior, we recommend referencing fixed model IDs.

## Beta Models

We sometimes release models in beta to gather feedback and confirm their performance before a full production rollout. Beta models are available to all users but are **not recommended for production use**.

Beta status does not guarantee promotion to production. A beta model may be removed if it is too costly to run, performs poorly at scale, or raises safety concerns. Beta models can change without notice and may have limited documentation or support. Models that prove stable, broadly useful, and aligned with our standards are promoted to general availability.

**Important considerations for beta models:**

* May be changed or removed at any time without the standard deprecation notice period
* Not suitable for production applications or critical workflows
* May have inconsistent performance, availability, or behavior
* Limited or no migration support if removed
* Best used for testing, evaluation, and experimental projects

For production applications, we recommend using the stable models from our [main model lineup](/overview/models).

### Join the Beta Testing Program

Want to help shape Venice's future models and features? Join our beta testing program to get early access to new models before they're released publicly, provide feedback that influences development, and help us validate performance at scale.

[Learn how to join the beta testing group](https://venice.ai/faqs#how-do-i-join-the-beta-testing-group)

## Feedback

You can submit your feedback or request through our [Featurebase portal](https://featurebase.venice.ai). We maintain a public [changelog](https://featurebase.venice.ai/changelog), roadmap tracker, and transparent rationale for adding, upgrading, or removing models, and we encourage continuous community participation.

## Model Deprecation Tracker

The following models are scheduled for deprecation. We recommend migrating to the suggested replacements before the removal date.

<Note>
  **Migration Guide: `qwen3-235b`**

  Starting December 14, 2025, `qwen3-235b` splits into two models with better pricing. The `disable_thinking` parameter will stop working.

  **Your options:**

  * **Keep using `qwen3-235b`** - Automatically gets thinking behavior
  * **Switch to `qwen3-235b-a22b-instruct-2507`** - Non-thinking model with lower cost

  **If you use `disable_thinking=true`**: Switch to `qwen3-235b-a22b-instruct-2507` before December 14.
</Note>

| Deprecated Model | Replacement                                                        | Removal by   | Status    | Reason                                                  |
| ---------------- | ------------------------------------------------------------------ | ------------ | --------- | ------------------------------------------------------- |
| `qwen3-235b`     | `qwen3-235b-a22b-thinking-2507` or `qwen3-235b-a22b-instruct-2507` | Dec 14, 2025 | Available | Splitting into specialized models with improved pricing |


# Getting Started
Source: https://docs.venice.ai/overview/getting-started



Get up and running with the Venice API in minutes. Generate an API key, make your first request, and start building.

## Quickstart

<Steps>
  <Step title="Get your API key">
    Head to your [Venice API Settings](https://venice.ai/settings/api) and generate a new API key.

    For a detailed walkthrough with screenshots, check out the [API Key guide](/overview/guides/generating-api-key).
  </Step>

  <Step title="Set up your API key">
    Add your API key to your environment. You can export it in your shell:

    ```bash  theme={null}
    export VENICE_API_KEY='your-api-key-here'
    ```

    Or add it to a `.env` file in your project:

    ```bash  theme={null}
    VENICE_API_KEY=your-api-key-here
    ```
  </Step>

  <Step title="Install the SDK">
    Venice is OpenAI-compatible, so you can use the OpenAI SDK. If you prefer to use cURL or raw HTTP requests, you can skip this step.

    <CodeGroup>
      ```bash Python theme={null}
      pip install openai
      ```

      ```bash Node.js theme={null}
      npm install openai
      ```
    </CodeGroup>
  </Step>

  <Step title="Send your first request">
    <CodeGroup>
      ```python Python theme={null}
      import os
      from openai import OpenAI

      client = OpenAI(
          api_key=os.getenv("VENICE_API_KEY"),
          base_url="https://api.venice.ai/api/v1"
      )

      completion = client.chat.completions.create(
          model="venice-uncensored",
          messages=[
              {"role": "system", "content": "You are a helpful AI assistant"},
              {"role": "user", "content": "Why is privacy important?"}
          ]
      )

      print(completion.choices[0].message.content)
      ```

      ```javascript Node.js theme={null}
      import OpenAI from 'openai';

      const client = new OpenAI({
          apiKey: process.env.VENICE_API_KEY,
          baseURL: 'https://api.venice.ai/api/v1'
      });

      const completion = await client.chat.completions.create({
          model: 'venice-uncensored',
          messages: [
              { role: 'system', content: 'You are a helpful AI assistant' },
              { role: 'user', content: 'Why is privacy important?' }
          ]
      });

      console.log(completion.choices[0].message.content);
      ```

      ```bash cURL theme={null}
      curl https://api.venice.ai/api/v1/chat/completions \
        -H "Authorization: Bearer $VENICE_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "model": "venice-uncensored",
          "messages": [
            {"role": "system", "content": "You are a helpful AI assistant"},
            {"role": "user", "content": "Why is privacy important?"}
          ]
        }'
      ```
    </CodeGroup>

    **Message roles:**

    * `system` - Instructions for how the model should behave
    * `user` - Your prompts or questions
    * `assistant` - Previous model responses (for multi-turn conversations)
    * `tool` - Function calling results (when using tools)
  </Step>

  <Step title="Choose your model (optional)">
    Venice has multiple models for different use cases. Popular choices:

    * `llama-3.3-70b` - Balanced performance, great for most use cases
    * `qwen3-235b` - Most powerful flagship model for complex tasks
    * `mistral-31-24b` - Vision + function calling support
    * `venice-uncensored` - No content filtering

    <Card title="View All Models" icon="database" href="/overview/models">
      Browse the complete list of models with pricing, capabilities, and context limits
    </Card>
  </Step>

  <Step title="Use Venice Parameters">
    You can choose to enable Venice-specific features like web search using `venice_parameters`:

    <CodeGroup>
      ```python Python theme={null}
      import os
      from openai import OpenAI

      client = OpenAI(
          api_key=os.environ.get("VENICE_API_KEY"),
          base_url="https://api.venice.ai/api/v1"
      )

      completion = client.chat.completions.create(
          model="venice-uncensored",
          messages=[
              {"role": "user", "content": "What are the latest developments in AI?"}
          ],
          extra_body={
              "venice_parameters": {
                  "enable_web_search": "auto",
                  "include_venice_system_prompt": True
              }
          }
      )

      print(completion.choices[0].message.content)
      ```

      ```javascript Node.js theme={null}
      import OpenAI from 'openai';

      const client = new OpenAI({
          apiKey: process.env.VENICE_API_KEY,
          baseURL: 'https://api.venice.ai/api/v1'
      });

      const completion = await client.chat.completions.create({
          model: 'venice-uncensored',
          messages: [
              { role: 'user', content: 'What are the latest developments in AI?' }
          ],
          venice_parameters: {
              enable_web_search: 'auto',
              include_venice_system_prompt: true
          }
      });

      console.log(completion.choices[0].message.content);
      ```

      ```bash cURL theme={null}
      curl https://api.venice.ai/api/v1/chat/completions \
        -H "Authorization: Bearer $VENICE_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "model": "venice-uncensored",
          "messages": [
            {"role": "user", "content": "What are the latest developments in AI?"}
          ],
          "venice_parameters": {
            "enable_web_search": "auto",
            "include_venice_system_prompt": true
          }
        }'
      ```
    </CodeGroup>

    See all [available parameters](https://docs.venice.ai/api-reference/api-spec#venice-parameters).
  </Step>

  <Step title="Enable streaming (optional)">
    Stream responses in real-time using `stream=True`:

    <CodeGroup>
      ```python Python theme={null}
      import os
      from openai import OpenAI

      client = OpenAI(
          api_key=os.environ.get("VENICE_API_KEY"),
          base_url="https://api.venice.ai/api/v1"
      )

      stream = client.chat.completions.create(
          model="venice-uncensored",
          messages=[{"role": "user", "content": "Write a short story about AI"}],
          stream=True
      )

      for chunk in stream:
          if chunk.choices and chunk.choices[0].delta.content is not None:
              print(chunk.choices[0].delta.content, end="")
      ```

      ```javascript Node.js theme={null}
      import OpenAI from 'openai';

      const client = new OpenAI({
          apiKey: process.env.VENICE_API_KEY,
          baseURL: 'https://api.venice.ai/api/v1'
      });

      const stream = await client.chat.completions.create({
          model: 'venice-uncensored',
          messages: [{ role: 'user', content: 'Write a short story about AI' }],
          stream: true
      });

      for await (const chunk of stream) {
          if (chunk.choices && chunk.choices[0]?.delta?.content) {
              process.stdout.write(chunk.choices[0].delta.content);
          }
      }
      ```

      ```bash cURL theme={null}
      curl https://api.venice.ai/api/v1/chat/completions \
        -H "Authorization: Bearer $VENICE_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "model": "venice-uncensored",
          "messages": [
            {"role": "user", "content": "Write a short story about AI"}
          ],
          "stream": true
        }'
      ```
    </CodeGroup>
  </Step>

  <Step title="Customize response behavior (optional)">
    Control how the model responds with parameters like temperature, max tokens, and more:

    <CodeGroup>
      ```python Python theme={null}
      import os
      from openai import OpenAI

      client = OpenAI(
          api_key=os.environ.get("VENICE_API_KEY"),
          base_url="https://api.venice.ai/api/v1"
      )

      completion = client.chat.completions.create(
          model="venice-uncensored",
          messages=[
              {"role": "system", "content": "You are a creative storyteller"},
              {"role": "user", "content": "Tell me a creative story"}
          ],
          temperature=0.8,
          max_tokens=500,
          top_p=0.9,
          frequency_penalty=0.5,
          presence_penalty=0.5,
          extra_body={
              "venice_parameters": {
                  "include_venice_system_prompt": False
              }
          }
      )

      print(completion.choices[0].message.content)
      ```

      ```javascript Node.js theme={null}
      import OpenAI from 'openai';

      const client = new OpenAI({
          apiKey: process.env.VENICE_API_KEY,
          baseURL: 'https://api.venice.ai/api/v1'
      });

      const completion = await client.chat.completions.create({
          model: 'venice-uncensored',
          messages: [
              { role: 'system', content: 'You are a creative storyteller' },
              { role: 'user', content: 'Tell me a creative story' }
          ],
          temperature: 0.8,
          max_tokens: 500,
          top_p: 0.9,
          frequency_penalty: 0.5,
          presence_penalty: 0.5,
          venice_parameters: {
              include_venice_system_prompt: false
          }
      });

      console.log(completion.choices[0].message.content);
      ```

      ```bash cURL theme={null}
      curl https://api.venice.ai/api/v1/chat/completions \
        -H "Authorization: Bearer $VENICE_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "model": "venice-uncensored",
          "messages": [
            {"role": "system", "content": "You are a creative storyteller"},
            {"role": "user", "content": "Tell me a creative story"}
          ],
          "temperature": 0.8,
          "max_tokens": 500,
          "top_p": 0.9,
          "frequency_penalty": 0.5,
          "presence_penalty": 0.5,
          "stream": false,
          "venice_parameters": {
            "include_venice_system_prompt": false
          }
        }'
      ```
    </CodeGroup>

    Check out the [Chat Completions docs](/api-reference/endpoint/chat/completions) for more information on all supported parameters.
  </Step>
</Steps>

***

## More Capabilities

### Image Generation

Create images from text prompts using diffusion models:

<CodeGroup>
  ```python Python theme={null}
  import os
  import requests

  url = "https://api.venice.ai/api/v1/image/generate"

  payload = {
      "model": "venice-sd35",
      "prompt": "A cyberpunk city with neon lights and rain",
      "width": 1024,
      "height": 1024,
      "format": "webp"
  }

  headers = {
      "Authorization": f"Bearer {os.getenv('VENICE_API_KEY')}",
      "Content-Type": "application/json"
  }

  response = requests.post(url, json=payload, headers=headers)

  print(response.json())
  ```

  ```javascript Node.js theme={null}
  const url = 'https://api.venice.ai/api/v1/image/generate';

  const options = {
      method: 'POST',
      headers: {
          'Authorization': `Bearer ${process.env.VENICE_API_KEY}`,
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({
          model: 'venice-sd35',
          prompt: 'A cyberpunk city with neon lights and rain',
          width: 1024,
          height: 1024,
          format: 'webp'
      })
  };

  try {
      const response = await fetch(url, options);
      const data = await response.json();
      console.log(data);
  } catch (error) {
      console.error(error);
  }
  ```

  ```bash cURL theme={null}
  curl https://api.venice.ai/api/v1/image/generate \
    -H "Authorization: Bearer $VENICE_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "venice-sd35",
      "prompt": "A cyberpunk city with neon lights and rain",
      "width": 1024,
      "height": 1024
    }'
  ```
</CodeGroup>

**Note:** The response returns base64-encoded images in the `images` array. Decode the base64 string to save or display the image.

**Popular Image Models:**

* `qwen-image` - Highest quality image generation
* `venice-sd35` - Default choice, works with all features
* `hidream` - Fast generation for production use

<Card title="View All Image Models" icon="image" href="/overview/models#image-models">
  See all available image models with pricing and capabilities
</Card>

For more advanced parameter options like `cfg_scale`, `negative_prompt`, `style_preset`, `seed`, `variants`, and more, check out the [Images API Reference](/api-reference/endpoint/image/generate).

### Image Editing

Modify existing images with AI-powered inpainting using the Qwen-Image model:

<CodeGroup>
  ```python Python theme={null}
  import os
  import requests
  import base64

  url = "https://api.venice.ai/api/v1/image/edit"

  with open("image.jpg", "rb") as f:
      image_base64 = base64.b64encode(f.read()).decode('utf-8')

  payload = {
      "prompt": "Colorize",
      "image": image_base64
  }

  headers = {
      "Authorization": f"Bearer {os.getenv('VENICE_API_KEY')}",
      "Content-Type": "application/json"
  }

  response = requests.post(url, json=payload, headers=headers)

  with open("edited_image.png", "wb") as f:
      f.write(response.content)
  ```

  ```javascript Node.js theme={null}
  import fs from 'fs';

  const imageBuffer = fs.readFileSync('image.jpg');
  const imageBase64 = imageBuffer.toString('base64');

  const options = {
      method: 'POST',
      headers: {
          'Authorization': `Bearer ${process.env.VENICE_API_KEY}`,
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({
          prompt: 'Colorize',
          image: imageBase64
      })
  };

  const response = await fetch('https://api.venice.ai/api/v1/image/edit', options);
  const imageData = await response.arrayBuffer();
  fs.writeFileSync('edited_image.png', Buffer.from(imageData));
  ```

  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.venice.ai/api/v1/image/edit \
    --header "Authorization: Bearer $VENICE_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
      "prompt": "Colorize",
      "image": "iVBORw0KGgoAAAANSUhEUgAAAgAAAAIACAIAAAB7GkOtAAAAIGNIUk0A..."
    }'
  ```
</CodeGroup>

**Note:** The image editor uses the Qwen-Image model and is an experimental endpoint. Send the input image as a base64-encoded string, and the API returns the edited image as binary data.

See the [Image Edit API](/api-reference/endpoint/image/edit) for all parameters.

### Image Upscaling

Enhance and upscale images to higher resolutions:

<CodeGroup>
  ```python Python theme={null}
  import os
  import requests
  import base64

  url = "https://api.venice.ai/api/v1/image/upscale"

  with open("image.jpg", "rb") as f:
      image_base64 = base64.b64encode(f.read()).decode('utf-8')

  payload = {
      "image": image_base64,
      "scale": 2
  }

  headers = {
      "Authorization": f"Bearer {os.getenv('VENICE_API_KEY')}",
      "Content-Type": "application/json"
  }

  response = requests.post(url, json=payload, headers=headers)

  with open("upscaled_image.png", "wb") as f:
      f.write(response.content)
  ```

  ```javascript Node.js theme={null}
  import fs from 'fs';

  const imageBuffer = fs.readFileSync('image.jpg');
  const imageBase64 = imageBuffer.toString('base64');

  const options = {
      method: 'POST',
      headers: {
          'Authorization': `Bearer ${process.env.VENICE_API_KEY}`,
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({
          image: imageBase64,
          scale: 2
      })
  };

  const response = await fetch('https://api.venice.ai/api/v1/image/upscale', options);
  const imageData = await response.arrayBuffer();
  fs.writeFileSync('upscaled_image.png', Buffer.from(imageData));
  ```

  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.venice.ai/api/v1/image/upscale \
    --header "Authorization: Bearer $VENICE_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
      "image": "iVBORw0KGgoAAAANSUhEUgAAAgAAAAIACAIAAAB7GkOtAAAAIGNIUk0A...",
      "scale": 2
    }'
  ```
</CodeGroup>

**Note:** Send the input image as a base64-encoded string, and the API returns the upscaled image as binary data.

See the [Image Upscale API](/api-reference/endpoint/image/upscale) for all parameters.

### Text-to-Speech

Convert text to audio with 60+ multilingual voices:

<CodeGroup>
  ```python Python theme={null}
  import os
  import requests

  response = requests.post(
      "https://api.venice.ai/api/v1/audio/speech",
      headers={
          "Authorization": f"Bearer {os.getenv('VENICE_API_KEY')}",
          "Content-Type": "application/json"
      },
      json={
          "input": "Hello, welcome to Venice Voice.",
          "model": "tts-kokoro",
          "voice": "af_sky"
      }
  )

  with open("speech.mp3", "wb") as f:
      f.write(response.content)
  ```

  ```javascript Node.js theme={null}
  import fs from 'fs';

  const response = await fetch('https://api.venice.ai/api/v1/audio/speech', {
      method: 'POST',
      headers: {
          'Authorization': `Bearer ${process.env.VENICE_API_KEY}`,
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({
          input: 'Hello, welcome to Venice Voice.',
          model: 'tts-kokoro',
          voice: 'af_sky'
      })
  });

  const audioBuffer = await response.arrayBuffer();
  fs.writeFileSync('speech.mp3', Buffer.from(audioBuffer));
  ```

  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.venice.ai/api/v1/audio/speech \
    --header "Authorization: Bearer $VENICE_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
      "input": "Hello, welcome to Venice Voice.",
      "model": "tts-kokoro",
      "voice": "af_sky"
    }' \
    --output speech.mp3
  ```
</CodeGroup>

The `tts-kokoro` model supports 60+ multilingual voices including `af_sky`, `af_nova`, `am_liam`, `bf_emma`, `zf_xiaobei`, and `jm_kumo`.

See the [TTS API](/api-reference/endpoint/audio/speech) for all voice options.

### Embeddings

Generate vector embeddings for semantic search, RAG, and recommendations:

<CodeGroup>
  ```python Python theme={null}
  import os
  import requests

  url = "https://api.venice.ai/api/v1/embeddings"

  payload = {
      "model": "text-embedding-bge-m3",
      "input": "Privacy-first AI infrastructure for semantic search",
      "encoding_format": "float"
  }

  headers = {
      "Authorization": f"Bearer {os.getenv('VENICE_API_KEY')}",
      "Content-Type": "application/json"
  }

  response = requests.post(url, json=payload, headers=headers)

  print(response.json())
  ```

  ```javascript Node.js theme={null}
  const url = 'https://api.venice.ai/api/v1/embeddings';

  const options = {
      method: 'POST',
      headers: {
          'Authorization': `Bearer ${process.env.VENICE_API_KEY}`,
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({
          model: 'text-embedding-bge-m3',
          input: 'Privacy-first AI infrastructure for semantic search',
          encoding_format: 'float'
      })
  };

  try {
      const response = await fetch(url, options);
      const data = await response.json();
      console.log(data);
  } catch (error) {
      console.error(error);
  }
  ```

  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.venice.ai/api/v1/embeddings \
    --header "Authorization: Bearer $VENICE_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
      "model": "text-embedding-bge-m3",
      "input": "Privacy-first AI infrastructure for semantic search",
      "encoding_format": "float"
    }'
  ```
</CodeGroup>

See the [Embeddings API](/api-reference/endpoint/embeddings/generate) for batch processing and advanced options.

### Vision (Multimodal)

Analyze images alongside text using vision-capable models like `mistral-31-24b`:

<CodeGroup>
  ```python Python theme={null}
  import os
  from openai import OpenAI

  client = OpenAI(
      api_key=os.getenv("VENICE_API_KEY"),
      base_url="https://api.venice.ai/api/v1"
  )

  response = client.chat.completions.create(
      model="mistral-31-24b",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "What is in this image?"},
                  {
                      "type": "image_url",
                      "image_url": {"url": "https://www.gstatic.com/webp/gallery/1.jpg"}
                  }
              ]
          }
      ]
  )

  print(response.choices[0].message.content)
  ```

  ```javascript Node.js theme={null}
  import OpenAI from 'openai';

  const client = new OpenAI({
      apiKey: process.env.VENICE_API_KEY,
      baseURL: 'https://api.venice.ai/api/v1'
  });

  const response = await client.chat.completions.create({
      model: 'mistral-31-24b',
      messages: [
          {
              role: 'user',
              content: [
                  { type: 'text', text: 'What is in this image?' },
                  {
                      type: 'image_url',
                      image_url: { url: 'https://www.gstatic.com/webp/gallery/1.jpg' }
                  }
              ]
          }
      ]
  });

  console.log(response.choices[0].message.content);
  ```

  ```bash cURL theme={null}
  curl https://api.venice.ai/api/v1/chat/completions \
    -H "Authorization: Bearer $VENICE_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "mistral-31-24b",
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "What is in this image?"
            },
            {
              "type": "image_url",
              "image_url": {
                "url": "https://www.gstatic.com/webp/gallery/1.jpg"
              }
            }
          ]
        }
      ]
    }'
  ```
</CodeGroup>

### Function Calling

Define functions that models can call to interact with external tools and APIs:

<CodeGroup>
  ```python Python theme={null}
  import os
  from openai import OpenAI

  client = OpenAI(
      api_key=os.getenv("VENICE_API_KEY"),
      base_url="https://api.venice.ai/api/v1"
  )

  tools = [
      {
          "type": "function",
          "function": {
              "name": "get_weather",
              "description": "Get the current weather in a location",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "location": {
                          "type": "string",
                          "description": "The city and state"
                      }
                  },
                  "required": ["location"]
              }
          }
      }
  ]

  response = client.chat.completions.create(
      model="llama-3.3-70b",
      messages=[{"role": "user", "content": "What's the weather in San Francisco?"}],
      tools=tools
  )

  print(response.choices[0].message)
  ```

  ```javascript Node.js theme={null}
  import OpenAI from 'openai';

  const client = new OpenAI({
      apiKey: process.env.VENICE_API_KEY,
      baseURL: 'https://api.venice.ai/api/v1'
  });

  const tools = [
      {
          type: 'function',
          function: {
              name: 'get_weather',
              description: 'Get the current weather in a location',
              parameters: {
                  type: 'object',
                  properties: {
                      location: {
                          type: 'string',
                          description: 'The city and state'
                      }
                  },
                  required: ['location']
              }
          }
      }
  ];

  const response = await client.chat.completions.create({
      model: 'llama-3.3-70b',
      messages: [{ role: 'user', content: "What's the weather in San Francisco?" }],
      tools: tools
  });

  console.log(response.choices[0].message);
  ```

  ```bash cURL theme={null}
  curl https://api.venice.ai/api/v1/chat/completions \
    -H "Authorization: Bearer $VENICE_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "llama-3.3-70b",
      "messages": [
        {
          "role": "user",
          "content": "What'\''s the weather in San Francisco?"
        }
      ],
      "tools": [
        {
          "type": "function",
          "function": {
            "name": "get_weather",
            "description": "Get the current weather in a location",
            "parameters": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The city and state"
                }
              },
              "required": ["location"]
            }
          }
        }
      ]
    }'
  ```
</CodeGroup>

**Supported models:** `llama-3.3-70b`, `qwen3-235b`, `mistral-31-24b`, `qwen3-4b`

***

## Next Steps

Now that you've made your first requests, explore more of what Venice API has to offer:

<CardGroup cols={2}>
  <Card title="Browse Models" icon="database" href="/overview/models">
    Compare all available models with their capabilities, pricing, and context limits
  </Card>

  <Card title="API Reference" icon="code" href="/api-reference/api-spec">
    Explore detailed API documentation with all endpoints and parameters
  </Card>

  <Card title="Structured Responses" icon="brackets-curly" href="/overview/guides/structured-responses">
    Learn how to get JSON responses with guaranteed schemas
  </Card>

  <Card title="AI Agents Guide" icon="robot" href="/overview/guides/ai-agents">
    Build autonomous AI agents with Venice API and frameworks like Eliza
  </Card>
</CardGroup>

### Additional Resources

<CardGroup cols={2}>
  <Card title="Rate Limiting" icon="gauge" href="/api-reference/rate-limiting">
    Understand rate limits and best practices for production usage
  </Card>

  <Card title="Error Codes" icon="triangle-exclamation" href="/api-reference/error-codes">
    Reference for handling API errors and troubleshooting issues
  </Card>

  <Card title="Postman Collection" icon="bolt" href="/overview/guides/postman">
    Import our complete Postman collection for easy testing
  </Card>

  <Card title="Privacy & Security" icon="shield" href="/overview/privacy">
    Learn about Venice's privacy-first architecture and data handling
  </Card>
</CardGroup>

***

## Need Help?

* **Discord Community**: Join our [Discord server](https://discord.gg/askvenice) for support and discussions
* **Documentation**: Browse our [complete API reference](/api-reference/api-spec)
* **Status Page**: Check service status at [veniceai-status.com](https://veniceai-status.com)
* **Twitter**: Follow [@AskVenice](https://x.com/AskVenice) for updates

<Resources />


# AI Agents
Source: https://docs.venice.ai/overview/guides/ai-agents

Venice is supported with the following AI Agent communities.

* [Coinbase Agentkit](https://www.coinbase.com/developer-platform/discover/launches/introducing-agentkit)

* [Eliza](https://github.com/ai16z/eliza) - Venice support introduced via this [PR](https://github.com/ai16z/eliza/pull/1008).

## Eliza Instructions

To setup Eliza with Venice, follow these instructions. A full blog post with more detail can be found [here](https://venice.ai/blog/how-to-build-a-social-media-ai-agent-with-elizaos-venice-api).

* Clone the Eliza repository:

```bash  theme={null}
# Clone the repository
git clone https://github.com/ai16z/eliza.git
```

* Copy `.env.example` to `.env`

* Update `.env` specifying your `VENICE_API_KEY`, and model selections for  `SMALL_VENICE_MODEL`, `MEDIUM_VENICE_MODEL`, `LARGE_VENICE_MODEL`, `IMAGE_VENICE_MODEL`, instructions on generating your key can be found [here](/overview/guides/generating-api-key).

* Create a new character in the `/characters/` folder with a filename similar to  `your_character.character.json`to specify the character profile, tools/functions, and Venice.ai as the model provider:

```typescript  theme={null}
   modelProvider: "venice"
```

* Build the repo:

```bash  theme={null}
pnpm i
pnpm build
pnpm start
```

* Start your character

```bash  theme={null}
pnpm start --characters="characters/<your_character>.character.json"
```

* Start the local UI to chat with the agent

<img src="https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/eliza-config.png?fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=d6dff632864fd7a54e6ba3d2d558fd0a" alt="" data-og-width="1172" width="1172" data-og-height="1002" height="1002" data-path="images/eliza-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/eliza-config.png?w=280&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=cf44735fc0525bf0427569ec6831c8ac 280w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/eliza-config.png?w=560&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=f1a8a917ac07b317bd0dc6f8d58b9e23 560w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/eliza-config.png?w=840&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=6ef04f414b49054af6f71e08102ceb7f 840w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/eliza-config.png?w=1100&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=6a4ca049a1f1e9f1c409fa5d5bc98ed1 1100w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/eliza-config.png?w=1650&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=6026f1fdf6cca494e93a94c68b8f57f6 1650w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/eliza-config.png?w=2500&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=ec0b898e6060ab5b2a1f62751a2ce78e 2500w" />


# Generating an API Key
Source: https://docs.venice.ai/overview/guides/generating-api-key



Venice's API is protected via API keys. To begin using the Venice API, you'll first need to generate a new key. Follow these steps to get started.

<Steps>
  <Step title="Visit the API Settings Page">
    To get to the API settings page, by visiting [https://venice.ai/settings/api](https://venice.ai/settings/api). This page is accessible by clicking "API" in the left hand toolbar, or by clicking “API” within your user settings.

    Within this dashboard, you're able to view your Diem and USD balances, your API Tier, your API Usage, and your API Keys.

    <Frame>
      <img src="https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/API-Overview.png?fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=0077ee4359a34036007b6cc94967adbf" alt="API Overview" data-og-width="2572" width="2572" data-og-height="1252" height="1252" data-path="images/guides/API-Overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/API-Overview.png?w=280&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=e846521d3874f780ee11b5f2cfcd15ff 280w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/API-Overview.png?w=560&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=aaaf8a8c96de1f9f48466ac82703caa7 560w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/API-Overview.png?w=840&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=98918b29973a499c40b96c2ab87a6726 840w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/API-Overview.png?w=1100&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=c7dedd1e4e2da578c3902ae2f0788101 1100w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/API-Overview.png?w=1650&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=4deecf2a10e87e9142f83f0a1e641f29 1650w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/API-Overview.png?w=2500&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=81f7e4f1b3713cf16c84d573a553f0ef 2500w" />
    </Frame>
  </Step>

  <Step title="Click Generate New API Key">
    Scroll down the dashboard and select "Generate New API Key". You'll be presented with a list of options.

    * **Description:** This is used to name your API key

    * **API Key Type:**

      * “Admin” keys have the ability to delete or generate additional API keys programmatically.

      * “Inference Only” keys are only permitted to run inference.

    * **Expires at:** You can choose to set an expiration date for the API key after which it will cease to function. By default, a date will not be set, and the key will work in perpetuity.

    * **Epoch Consumption Limits:** This allows you to create limits for API usage from the individual API key. You can choose to limit the Diem or USD amount allowable within a given epoch (24hrs).

    <Frame>
      <img src="https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/api-keys/create-key.png?fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=b053f218d2aaa8c88bbd802a7d6ddc50" alt="Generate New API Key" data-og-width="2624" width="2624" data-og-height="1296" height="1296" data-path="images/guides/api-keys/create-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/api-keys/create-key.png?w=280&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=0f2afc0a5ff0d7082674fca359c3fa62 280w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/api-keys/create-key.png?w=560&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=db9c8ffd40a01eac65f6c17e9f726838 560w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/api-keys/create-key.png?w=840&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=92f9c039ea5dc316e59006b65dd1c41f 840w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/api-keys/create-key.png?w=1100&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=c35cf11766f8c774e68d59ca9b6268d5 1100w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/api-keys/create-key.png?w=1650&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=c5b95320320ddc865b5cad607ca8a100 1650w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/api-keys/create-key.png?w=2500&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=9a5fe0e9e9151e795fd48b3422e965d0 2500w" />
    </Frame>
  </Step>

  <Step title="Generate the key">
    Clicking Generate will show you the API key.

    <Warning>
      **Important:** This key is only shown once. Make sure to copy it and store it in a safe place. If you lose it, you'll need to delete it and create a new one.
    </Warning>

    <Frame>
      <img src="https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/api-keys/result.png?fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=1a9ede76b5428bd0dc00291ea73d93f7" alt="Your API Key" data-og-width="1198" width="1198" data-og-height="660" height="660" data-path="images/guides/api-keys/result.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/api-keys/result.png?w=280&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=deaf0f447a6aab1a230fd0f5bcf0fa94 280w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/api-keys/result.png?w=560&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=e46d47c3e10195f5ad51fc7b5b7c33a6 560w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/api-keys/result.png?w=840&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=12a4038b4af62c624f32c9c3968c0522 840w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/api-keys/result.png?w=1100&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=b0f2e2f5da7c2e651739f72e56257781 1100w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/api-keys/result.png?w=1650&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=8eb0819d5c5a50d74570b12634253311 1650w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/api-keys/result.png?w=2500&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=1377d84068a97a6c209c5356069b4e8a 2500w" />
    </Frame>
  </Step>
</Steps>


# Autonomous Agent API Key Creation
Source: https://docs.venice.ai/overview/guides/generating-api-key-agent



Autonomous AI Agents can programmatically access Venice.ai's APIs without any human interaction using the "api\_keys" endpoint. AI Agents are now able to manage their own wallets on the BASE blockchain, allowing them to programmatically acquire and stake VVV token to earn a daily Diem inference allocation. Venice's new API endpoint allows them to automate further by generating their own API key.&#x20;

To autonomously generate an API key within an agent, you must:

<Steps>
  <Step title="Acquire VVV">
    The agent will need VVV token to complete this process. This can be achieved by sending tokens directly to the agent wallet, or having the agent swap on a Decentralized Exchange (DEX), like [Aerodrome](https://aerodrome.finance/swap?from=eth\&to=0xacfe6019ed1a7dc6f7b508c02d1b04ec88cc21bf\&chain0=8453\&chain1=8453) or [Uniswap](https://app.uniswap.org/swap?chain=base\&inputCurrency=NATIVE\&outputCurrency=0xacfe6019ed1a7dc6f7b508c02d1b04ec88cc21bf).
  </Step>

  <Step title="Stake VVV with Venice">
    Once funded, the agent will need to stake the VVV tokens within the [Venice Staking Smart Contract](https://basescan.org/address/0x321b7ff75154472b18edb199033ff4d116f340ff#code). To accomplish this you first must approve VVV tokens for staking, then execute a "stake" transaction.&#x20;

    <Frame as="div">
      <img src="https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/SC-Stake.png?fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=6a2180bbdc58f95990e99568d7015bbc" alt="Smart Contract Staking" data-og-width="812" width="812" data-og-height="324" height="324" data-path="images/guides/SC-Stake.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/SC-Stake.png?w=280&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=64d66069edc7f3060c1046bef50a2a18 280w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/SC-Stake.png?w=560&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=b8e22d317889626cf500e3355e1b2b45 560w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/SC-Stake.png?w=840&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=131a37bcfb65773721f179340ce2a390 840w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/SC-Stake.png?w=1100&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=6b6c2ffa9d7d32c41b4e389f7b4747b3 1100w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/SC-Stake.png?w=1650&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=91c6003ebbce068d5724090802f5be30 1650w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/guides/SC-Stake.png?w=2500&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=6c46ebbf0b5bc252ede57a11b096c71d 2500w" />
    </Frame>

    When the transaction is complete, you will see the VVV tokens exit the wallet and sVVV tokens returned to your wallet. This indicates a successful stake.&#x20;
  </Step>

  <Step title="Obtain Validation Token">
    To generate an API key, you need to first obtain your validation token. You can get this by calling this [API endpoint ](https://docs.venice.ai/api-reference/endpoint/api_keys/generate_web3_key/get)`https://api.venice.ai/api/v1/api_keys/generate_web3_key` . The API response will provide you with a "token".&#x20;

    Here is an example request:

    ```
    curl --request GET \
      --url https://api.venice.ai/api/v1/api_keys/generate_web3_key
    ```
  </Step>

  <Step title="Sign for Wallet Validation">
    Sign the token with the wallet holding VVV to complete the association between the wallet and token.&#x20;
  </Step>

  <Step title="Generate API Key">
    Now you can call this same [API endpoint](https://docs.venice.ai/api-reference/endpoint/api_keys/generate_web3_key/get) `https://api.venice.ai/api/v1/api_keys/generate_web3_key` to create your API key.&#x20;

    You will need the following information to proceed, which is described further within the "[Generating API Key Guide](https://docs.venice.ai/overview/guides/generating-api-key)":

    * API Key Type: Inference or Admin

    * ConsumptionLimit: To be used if you want to limit the API key usage

    * Signature: The signed token from step 4

    * Token: The unsigned token from step 3

    * Address: The agent's wallet address

    * Description: String to describe your API Key

    * ExpiresAt: Option to set an expiration date for the API key (empty for no expiration)

    Here is an example request:

    ```
    curl --request POST \
      --url https://api.venice.ai/api/v1/api_keys/generate_web3_key \
      --header 'Authorization: Bearer ' \
      --header 'Content-Type: application/json' \
      --data '{
      "description": "Web3 API Key",
      "apiKeyType": "INFERENCE",
      "signature": "<signed token>",
      "token": "<unsigned token>",
      "address": "<wallet address>",
      "consumptionLimit": {
        "diem": 1
      }
    }'
    ```
  </Step>
</Steps>

Example code to interact with this API can be found below:

```
import { ethers } from "ethers";

// NOTE: This is an example. To successfully generate a key, your address must be holding
// and staking VVV.
const wallet = ethers.Wallet.createRandom()
const address = wallet.address
console.log("Created address:", address)

// Request a JWT from Venice's API
const response = await fetch('https://api.venice.ai/api/v1/api_keys/generate_web3_key')
const token = (await response.json()).data.token
console.log("Validation Token:", token)

// Sign the token with your wallet and pass that back to the API to generate an API key
const signature = await wallet.signMessage(token)
const postResponse = await fetch('https://api.venice.ai/api/v1/api_keys/generate_web3_key', {
  method: 'POST',
  body: JSON.stringify({
    address,
    signature,
    token,
    apiKeyType: 'ADMIN'
  })
})

await postResponse.json()
```


# Integrations
Source: https://docs.venice.ai/overview/guides/integrations

Here is a list of third party tools with Venice.ai integrations.

[How to use Venice API](https://venice.ai/blog/how-to-use-venice-api) reference guide.

## Venice Confirmed Integrations

* Agents

  * [ElizaOS](https://venice.ai/blog/how-to-build-a-social-media-ai-agent-with-elizaos-venice-api) (local build)

  * [ElizaOS](https://venice.ai/blog/how-to-launch-an-elizaos-agent-on-akash-using-venice-api-in-less-than-10-minutes) (via [Akash Template](https://console.akash.network/templates/akash-network-awesome-akash-Venice-ElizaOS))

* Coding

  * [Cursor IDE](https://venice.ai/blog/how-to-code-with-the-venice-api-in-cursor-a-quick-guide)

  * [Cline](https://venice.ai/blog/how-to-use-the-venice-api-with-cline-in-vscode-a-developers-guide) (VSC Extension)

  * [ROO Code ](https://venice.ai/blog/how-to-use-the-roo-ai-coding-assistant-in-private-with-venice-api-a-quick-guide)(VSC Extension)

  * [VOID IDE](https://venice.ai/blog/how-to-use-open-source-ai-code-editor-void-in-private-with-venice-api)&#x20;

* Assistants

  * [Brave Leo Browser ](https://venice.ai/blog/how-to-use-brave-leo-ai-with-venice-api-a-privacy-first-browser-ai-assistant)

## Community Confirmed&#x20;

These integrations have been confirmed by the community. Venice is in the process of confirming these integrations and creating how-to guides for each of the following:

* Agents/Bots

  * [Coinbase Agentkit](https://www.coinbase.com/developer-platform/discover/launches/introducing-agentkit)

  * [Eliza\_Starter](https://github.com/Baidis/eliza-Venice) Simplified Eliza setup.

  * [Venice AI Discord Bot](https://bobbiebeach.space/blog/venice-ai-discord-bot-full-setup-guide-features/)

  * [JanitorAI](https://janitorai.com/)

* Coding

  * [Aider](https://github.com/Aider-AI/aider), AI pair programming in your terminal

  * [Alexcodes.app](https://alexcodes.app/)

* Assistants

  * [Jan - Local AI Assistant](https://github.com/janhq/jan)

  * [llm-venice](https://github.com/ar-jan/llm-venice)

  * [unOfficial PHP SDK for Venice](https://github.com/georgeglarson/venice-ai-php)

  * [Msty](https://msty.app)

  * [Open WebUI](https://github.com/open-webui/open-webui)

  * [Librechat](https://www.librechat.ai/)

  * [ScreenSnapAI](https://screensnap.ai/)

## Venice API Raw Data

Many users have requested access to Venice API docs and data in a format acceptable for use with RAG (Retrieval-Augmented Generation) for various purposes. The full API specification is available within the "API Swagger" document below, in yaml format. The Venice API documents included throughout this API Reference webpage are available from the link below, with most documents in .mdx format.

[API Swagger](https://api.venice.ai/doc/api/swagger.yaml)

[API Docs](https://github.com/veniceai/api-docs/archive/refs/heads/main.zip)


# Using Postman
Source: https://docs.venice.ai/overview/guides/postman



## Overview

Venice provides a comprehensive Postman collection that allows developers to explore and test the full capabilities of our API. This collection includes pre-configured requests, examples, and environment variables to help you get started quickly with Venice's AI services.

## Accessing the Collection

Our official Postman collection is available in the Venice AI Workspace:

* [Venice AI Postman Workspace](https://www.postman.com/veniceai/workspace/venice-ai-workspace)
* [Venice AI Postman Examples](https://postman.venice.ai/)

## Collection Features

* **Ready-to-Use Requests**: Pre-configured API calls for all Venice endpoints
* **Environment Templates**: Properly structured environment variables
* **Request Examples**: Real-world usage examples for each endpoint
* **Response Samples**: Example responses to help you understand the API's output
* **Documentation**: Inline documentation for each request

## Getting Started

<Steps>
  <Step title="Fork the Collection">
    * Navigate to the Venice AI Workspace
    * Click "Fork" to create your own copy of the collection
    * Choose your workspace destination
  </Step>

  <Step title="Set Up Your Environment">
    * Create a new environment in Postman
    * Add your Venice API key
    * Configure the base URL: `https://api.venice.ai/api/v1`
  </Step>

  <Step title="Make Your First Request">
    * Select any request from the collection
    * Ensure your environment is selected
    * Click "Send" to test the API
  </Step>
</Steps>

## Available Endpoints

The collection includes examples for all Venice API endpoints:

* Text Generation
* Image Generation
* Model Information
* Image Upscaling
* System Prompt Configuration

## Best Practices

* Keep your API key secure and never share it
* Use environment variables for sensitive information
* Test responses in the Postman console before implementation
* Review the example responses for expected data structures

<Note>*Note: The Postman collection is regularly updated to reflect the latest API changes and features.*</Note>


# Structured Responses
Source: https://docs.venice.ai/overview/guides/structured-responses

Using structured responses within the Venice API

Venice has now included structured outputs via “response\_format” as an available field in the API. This field enables you to generate responses to your prompts that follow a specific pre-defined format. With this new method, the models are less likely to hallucinate incorrect keys or values within the response, which was more prevalent when attempting through system prompt manipulation or via function calling.

The structured output “response\_format” field utilizes the OpenAI API format, and is further described in the openAI guide [here](https://platform.openai.com/docs/guides/structured-outputs). OpenAI also released an introduction article to using stuctured outputs within the API specifically [here](https://openai.com/index/introducing-structured-outputs-in-the-api/). As this is advanced functionality, there are a handful of “gotchas” on the bottom of this page that should be followed.

This functionality is not natively available for all models. Please refer to the models section [here](https://docs.venice.ai/api-reference/endpoint/models/list?playground=open), and look for “supportsResponseSchema” for applicable models.

```json  theme={null}
    {
      "id": "venice-uncensored",
      "type": "text",
      "object": "model",
      "created": 1726869022,
      "owned_by": "venice.ai",
      "model_spec": {
        "availableContextTokens": 32768,
        "capabilities": {
          "supportsFunctionCalling": true,
          "supportsResponseSchema": true,
          "supportsWebSearch": true
        },
```

### How to use Structured Responses

To properly use the “response\_format” you can define your schema with various “properties”, representing categories of outputs, each with individually configured data types. These objects can be nested to create more advanced structures of outputs.

Here is an example of an API call using response\_format to explain the step-by-step process of solving a math equation.

You can see that the properties were configured to require both “steps” and “final\_answer” within the response. Within nesting, the steps category consists of both an “explanation” and an “output”, each as strings.

```json  theme={null}
curl --request POST \
  --url https://api.venice.ai/api/v1/chat/completions \
  --header 'Authorization: Bearer <api-key>' \
  --header 'Content-Type: application/json' \
  --data '{
  "model": "venice-uncensored",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful math tutor."
    },
    {
      "role": "user",
      "content": "solve 8x + 31 = 2"
    }
  ],
  "response_format": {
    "type": "json_schema",
    "json_schema": {
      "name": "math_response",
      "strict": true,
      "schema": {
        "type": "object",
        "properties": {
          "steps": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "explanation": {
                  "type": "string"
                },
                "output": {
                  "type": "string"
                }
              },
              "required": ["explanation", "output"],
              "additionalProperties": false
            }
          },
          "final_answer": {
            "type": "string"
          }
        },
        "required": ["steps", "final_answer"],
        "additionalProperties": false
      }
    }
  }
}

```

Here is the response that was received from the model. You can see that the structure followed the requirements by first providing the “steps” with the “explanation” and “output” of each step, and then the “final answer”.

```json  theme={null}
{
  "steps": [
    {
      "explanation": "Subtract 31 from both sides to isolate the term with x.",
      "output": "8x + 31 - 31 = 2 - 31"
    },
    {
      "explanation": "This simplifies to 8x = -29.",
      "output": "8x = -29"
    },
    {
      "explanation": "Divide both sides by 8 to solve for x.",
      "output": "x = -29 / 8"
    }
  ],
  "final_answer": "x = -29 / 8"
}

```

Although this is a simple example, this can be extrapolated into more advanced use cases like: Data Extraction, Chain of Thought Exercises, UI Generation, Data Categorization and many others.

### Gotchas

Here are some key requirements to keep in mind when using Structured Outputs via response\_format:

* Initial requests using response\_format may take longer to generate a response. Subsequent requests will not experience the same latency as the initial request.

* For larger queries, the model can fail to complete if either `max_tokens` or model timeout are reached, or if any rate limits are violated

* Incorrect schema format will result in errors on completion, usually due to timeout

* Although response\_format ensures the model will output a particular way, it does not guarantee that the model provided the correct information within. The content is driven by the prompt and the model performance.

* Structured Outputs via response\_format are not compatible with parallel function calls

* Important: All fields or parameters must include a `required` tag. To make a field optional, you need to add a `null` option within the `type`of the field, like this `"type": ["string", "null"]`&#x20;

* It is possible to make fields optional by giving a `null` options within the required field to allow an empty response.

* Important: `additionalProperties` must be set to false for response\_format to work properly

* Important: `strict` must be set to true for response\_format to work properly


# Current Models
Source: https://docs.venice.ai/overview/models

Complete list of available models on Venice AI platform

## Text Models

| Model Name                                                                                               | Model ID                         | Price (in/out)  | Context Limit | Capabilities                | Traits                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------- | --------------- | ------------- | --------------------------- | ----------------------------------- |
| [Venice Uncensored 1.1](https://huggingface.co/cognitivecomputations/Dolphin-Mistral-24B-Venice-Edition) | `venice-uncensored`              | `$0.20 / $0.90` | 32,768        | —                           | most\_uncensored                    |
| [Venice Small](https://huggingface.co/Qwen/Qwen3-4B)                                                     | `qwen3-4b`                       | `$0.05 / $0.15` | 32,768        | Function Calling, Reasoning | —                                   |
| [Venice Medium (3.1)](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503)              | `mistral-31-24b`                 | `$0.50 / $2.00` | 131,072       | Function Calling, Vision    | default\_vision                     |
| [Venice Large 1.1 (D)](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507-FP8)                    | `qwen3-235b`                     | `$0.45 / $3.50` | 131,072       | Function Calling, Reasoning | —                                   |
| [Qwen 3 235B A22B Thinking 2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Thinking-2507-FP8)          | `qwen3-235b-a22b-thinking-2507`  | `$0.45 / $3.50` | 131,072       | Function Calling, Reasoning | —                                   |
| [Qwen 3 235B A22B Instruct 2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507-FP8)          | `qwen3-235b-a22b-instruct-2507`  | `$0.15 / $0.75` | 131,072       | Function Calling            | —                                   |
| [Llama 3.2 3B](https://huggingface.co/meta-llama/Llama-3.2-3B)                                           | `llama-3.2-3b`                   | `$0.15 / $0.60` | 131,072       | Function Calling            | fastest                             |
| [Llama 3.3 70B](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct)                                | `llama-3.3-70b`                  | `$0.70 / $2.80` | 131,072       | Function Calling            | default, function\_calling\_default |
| [Qwen 3 Coder 480B](https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct)                          | `qwen3-coder-480b-a35b-instruct` | `$0.75 / $3.00` | 262,144       | Function Calling            | default\_code                       |
| [GLM 4.6](https://huggingface.co/zai-org/GLM-4.6)                                                        | `zai-org-glm-4.6`                | `$0.85 / $2.75` | 202,752       | Function Calling            | —                                   |

*Pricing is per 1M tokens (input / output). Additional usage-based pricing applies when using `enable_web_search` or `enable_web_scraping`, see [search pricing details](/overview/pricing#web-search-and-scraping).*

<Info>
  **Model Change Notice**: Starting **December 14, 2025**, `qwen3-235b` will be deprecated and calls will automatically route to `qwen3-235b-a22b-thinking-2507`.

  The `disable_thinking` parameter will be ignored. For non-thinking behavior, use `qwen3-235b-a22b-instruct-2507` directly. [Learn more about model changes](/overview/deprecations#model-deprecation-tracker).
</Info>

### Popular Text Models

`zai-org-glm-4.6` GLM 4.6 - High-intelligence flagship model\
`mistral-31-24b` Venice Medium (3.1) - Vision + function calling\
`qwen3-4b` Venice Small - Fast, affordable for most tasks\
`qwen3-235b-a22b-thinking-2507` Qwen 3 235B A22B Thinking - Advanced reasoning with thinking

### Text Model Categories

**Reasoning Models**

`qwen3-235b-a22b-thinking-2507` Qwen 3 235B A22B Thinking - Advanced reasoning with thinking\
`qwen3-4b` Venice Small - Efficient reasoning model

**Vision-Capable Models**

`mistral-31-24b` Venice Medium (3.1) - Vision-capable model\
`google-gemma-3-27b-it` Google Gemma 3 27B (beta)

**Cost-Optimized Models**

`qwen3-4b` Venice Small - Best balance of speed and cost\
`llama-3.2-3b` Llama 3.2 3B - Fastest for simple tasks\
`qwen3-235b-a22b-instruct-2507` Qwen 3 235B A22B Instruct - Optimized high-performance

**Uncensored Models**

`venice-uncensored` Venice Uncensored 1.1 - No content filtering

**High-Intelligence Models**

`qwen3-235b-a22b-thinking-2507` Qwen 3 235B A22B Thinking - Most powerful flagship model\
`zai-org-glm-4.6` GLM 4.6 - High-intelligence alternative\
`deepseek-ai-DeepSeek-R1` DeepSeek R1 (beta) - Advanced reasoning model
`llama-3.3-70b` Llama 3.3 70B - Balanced high-intelligence

### Beta Models

| Model Name                                                                             | Model ID                  | Price (in/out)  | Context Limit | Capabilities             | Traits |
| -------------------------------------------------------------------------------------- | ------------------------- | --------------- | ------------- | ------------------------ | ------ |
| [OpenAI GPT OSS 120B](https://huggingface.co/openai/gpt-oss-120b)                      | `openai-gpt-oss-120b`     | `$0.07 / $0.30` | 131,072       | Function Calling         | —      |
| [Google Gemma 3 27B Instruct](https://huggingface.co/google/gemma-3-27b-it)            | `google-gemma-3-27b-it`   | `$0.12 / $0.20` | 202,752       | Function Calling, Vision | —      |
| [Qwen 3 Next 80B](https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct)             | `qwen3-next-80b`          | `$0.35 / $1.90` | 262,144       | Function Calling         | —      |
| [DeepSeek R1](https://huggingface.co/deepseek-ai/DeepSeek-R1)                          | `deepseek-ai-DeepSeek-R1` | `$0.85 / $2.75` | 131,072       | Function Calling         | —      |
| [Hermes 3 Llama 3.1 405B](https://huggingface.co/NousResearch/Hermes-3-Llama-3.1-405B) | `hermes-3-llama-3.1-405b` | `$1.10 / $3.00` | 131,072       | —                        | —      |

<Warning>
  **Beta models are experimental and not recommended for production use.** These models may be changed, removed, or replaced at any time without notice. Use them for testing and evaluation purposes only. For production applications, use the stable models listed above.
</Warning>

***

## Image Models

| Model Name                                                                     | Model ID          | Price   | Model Source               | Traits                 |
| ------------------------------------------------------------------------------ | ----------------- | ------- | -------------------------- | ---------------------- |
| [Venice SD35](https://huggingface.co/stabilityai/stable-diffusion-3.5-large)   | `venice-sd35`     | `$0.01` | Stable Diffusion 3.5 Large | default, eliza-default |
| [HiDream](https://huggingface.co/HiDream-ai/HiDream-I1-Dev)                    | `hidream`         | `$0.01` | HiDream I1 Dev             | —                      |
| [Qwen Image](https://huggingface.co/Qwen/Qwen-Image)                           | `qwen-image`      | `$0.01` | Qwen Image                 | —                      |
| [Lustify SDXL](https://civitai.com/models/573152/lustify-sdxl-nsfw-checkpoint) | `lustify-sdxl`    | `$0.01` | Lustify SDXL               | —                      |
| [Lustify v7](https://civitai.com/models/573152/lustify-sdxl-nsfw-checkpoint)   | `lustify-v7`      | `$0.01` | Lustify v7                 | —                      |
| [Anime (WAI)](https://civitai.com/models/827184?modelVersionId=1761560)        | `wai-Illustrious` | `$0.01` | WAI-Illustrious            | —                      |

### Popular Image Models

`qwen-image` Qwen Image - Highest quality image generation\
`venice-sd35` Venice SD35 - Default choice with Eliza integration\
`lustify-sdxl` Lustify SDXL - Uncensored image generation\
`hidream` HiDream - Production-ready generation

### Image Model Categories

**High-Quality Models**

`qwen-image` Qwen Image - Highest quality output\
`hidream` HiDream - Production-ready generation

**Default Models**

`venice-sd35` Venice SD35 - Default choice, Eliza-optimized

**Special Purpose Models**

`lustify-sdxl` Lustify SDXL - Adult content generation\
`lustify-v7` Lustify v7 - Adult content generation\
`wai-Illustrious` Anime (WAI) - Anime-style generation

***

## Audio Models

### Text-to-Speech Models

`tts-kokoro` Kokoro TTS - 60+ multilingual voices for natural speech

| Model Name                                                         | Model ID     | Price                | Voices Available | Model Source |
| ------------------------------------------------------------------ | ------------ | -------------------- | ---------------- | ------------ |
| [Kokoro Text to Speech](https://huggingface.co/hexgrad/Kokoro-82M) | `tts-kokoro` | `$3.50` per 1M chars | 60+ voices       | Kokoro-82M   |

<Note>
  The tts-kokoro model supports a wide range of multilingual and stylistic voices (including af\_nova, am\_liam, bf\_emma, zf\_xiaobei, and jm\_kumo). Voice is selected using the voice parameter in the request payload.
</Note>

***

## Embedding Models

`text-embedding-bge-m3` BGE-M3 - Versatile embedding model for text similarity

| Model Name                                           | Model ID                | Price                         | Model Source        |
| ---------------------------------------------------- | ----------------------- | ----------------------------- | ------------------- |
| [BGE-M3](https://huggingface.co/KimChen/bge-m3-GGUF) | `text-embedding-bge-m3` | `$0.15 / $0.60` per 1M tokens | KimChen/bge-m3-GGUF |

## Image Processing Models

`upscaler` Image Upscaler - Enhance image resolution up to 4x\
`qwen-image` Qwen Image - Multimodal image editing model

### Image Upscaler

| Model Name | Model ID   | Price   | Upscale Options          |
| ---------- | ---------- | ------- | ------------------------ |
| Upscaler   | `upscaler` | `$0.01` | `2x ($0.02), 4x ($0.08)` |

### Image Editing (Inpaint)

| Model Name                                           | Model ID     | Price   | Model Source | Traits               |
| ---------------------------------------------------- | ------------ | ------- | ------------ | -------------------- |
| [Qwen Image](https://huggingface.co/Qwen/Qwen-Image) | `qwen-image` | `$0.04` | Qwen Image   | specialized\_editing |

## Model Features

* **Vision**: Ability to process and understand images
* **Reasoning**: Advanced logical reasoning capabilities
* **Function Calling**: Support for calling external functions and tools
* **Traits**: Special characteristics or optimizations (e.g., fastest, most\_intelligent, most\_uncensored)

## Usage Notes

* Input pricing refers to tokens sent to the model
* Output pricing refers to tokens generated by the model
* Context limits define the maximum number of tokens the model can process in a single request
* (D) Scheduled for deprecation. For timelines and migration guidance, see the [Deprecation Tracker](/overview/deprecations#model-deprecation-tracker).


# API Pricing
Source: https://docs.venice.ai/overview/pricing



### Pro Users

Pro subscribers receive a one-time \$10 API credit when upgrading to Pro. Use it to test and build small apps. You can scale your usage by buying credits, buying Diem, or staking VVV.

### Paid Tier

Choose how you pay for API usage:

<Steps>
  <Step title="Buy API Credits">
    Pay in USD via the [API Dashboard](https://venice.ai/settings/api). Credits are applied to usage automatically.
  </Step>

  <Step title="Buy Diem (1 Diem = $1/day)">
    Purchase Diem directly. Each Diem grants \$1 of compute per day at the same rates as USD.
  </Step>

  <Step title="Stake to Earn Diem (1 Diem = $1/day)">
    Stake tokens to receive daily Diem allocations (each Diem grants \$1 of compute per day). Manage staking and Diem at the [Token Dashboard](https://venice.ai/token).
  </Step>
</Steps>

## Model Pricing

All prices are in USD. Diem users pay the same rates (1 Diem = \$1 of compute per day).

### Chat Models

Prices per 1M tokens, with separate pricing for input and output tokens. You will only be charged for the tokens you use.
You can estimate the token count of a chat request using [this calculator](https://quizgecko.com/tools/token-counter).

| Model                          | Model ID                         |  Input | Output | Capabilities                |
| ------------------------------ | -------------------------------- | :----: | :----: | --------------------------- |
| Venice Small                   | `qwen3-4b`                       | \$0.05 | \$0.15 | Function Calling, Reasoning |
| Qwen 3 235B A22B Instruct 2507 | `qwen3-235b-a22b-instruct-2507`  | \$0.15 | \$0.75 | Function Calling            |
| Llama 3.2 3B                   | `llama-3.2-3b`                   | \$0.15 | \$0.60 | Function Calling            |
| Venice Uncensored              | `venice-uncensored`              | \$0.20 | \$0.90 | Uncensored                  |
| Venice Large (D)               | `qwen3-235b`                     | \$0.45 | \$3.50 | Function Calling, Reasoning |
| Qwen 3 235B A22B Thinking 2507 | `qwen3-235b-a22b-thinking-2507`  | \$0.45 | \$3.50 | Function Calling, Reasoning |
| Venice Medium (3.1)            | `mistral-31-24b`                 | \$0.50 | \$2.00 | Function Calling, Vision    |
| Llama 3.3 70B                  | `llama-3.3-70b`                  | \$0.70 | \$2.80 | Function Calling            |
| Qwen 3 Coder 480B              | `qwen3-coder-480b-a35b-instruct` | \$0.75 | \$3.00 | Function Calling            |
| GLM 4.6                        | `zai-org-glm-4.6`                | \$0.85 | \$2.75 | Function Calling            |

#### Beta Chat Models

| Model                          | Model ID                  |  Input | Output | Capabilities             |
| ------------------------------ | ------------------------- | :----: | :----: | ------------------------ |
| OpenAI GPT OSS 120B (beta)     | `openai-gpt-oss-120b`     | \$0.07 | \$0.30 | Function Calling         |
| Google Gemma 3 27B (beta)      | `google-gemma-3-27b-it`   | \$0.12 | \$0.20 | Function Calling, Vision |
| Qwen 3 Next 80B (beta)         | `qwen3-next-80b`          | \$0.35 | \$1.90 | Function Calling         |
| DeepSeek R1 (beta)             | `deepseek-ai-DeepSeek-R1` | \$0.85 | \$2.75 | Function Calling         |
| Hermes 3 Llama 3.1 405B (beta) | `hermes-3-llama-3.1-405b` | \$1.10 | \$3.00 |                          |

<Warning>
  Beta models are experimental and not recommended for production use. These models may be changed, removed, or replaced at any time without notice. [Learn more about beta models](/overview/deprecations#beta-models)
</Warning>

### Web Search and Scraping

Web Search and Web Scraping features run on dedicated compute infrastructure designed for large-scale crawling and real-time content extraction. These features are usage-based and charged per API call when enabled:

| Feature      |  Venice Models  |   Other Models  | Parameters                  |
| ------------ | :-------------: | :-------------: | --------------------------- |
| Web Search   | \$10 / 1K calls | \$25 / 1K calls | `enable_web_search: true`   |
| Web Scraping | \$10 / 1K calls | \$25 / 1K calls | `enable_web_scraping: true` |

**Venice Models**: `venice-uncensored`, `qwen3-4b`, `mistral-31-24b`, `qwen3-235b`

<Info>
  Web Scraping automatically detects up to 3 URLs per message, scrapes and converts content into structured markdown, and adds the extracted text into model context. These charges apply in addition to standard model token pricing.
</Info>

### Embedding Models

Prices per 1M tokens:

| Model  | Model ID                |  Input | Output |
| ------ | ----------------------- | :----: | :----: |
| BGE-M3 | `text-embedding-bge-m3` | \$0.15 | \$0.60 |

### Image Models

Image models are priced per generation:

| Model                  |  Price |
| ---------------------- | :----: |
| Generation             | \$0.01 |
| Upscale / Enhance (2x) | \$0.02 |
| Upscale / Enhance (4x) | \$0.08 |
| Edit (aka Inpaint)     | \$0.04 |

### Audio Models

Prices per 1M characters:

| Model      | Model ID     |  Price |
| ---------- | ------------ | :----: |
| Kokoro TTS | `tts-kokoro` | \$3.50 |


# Privacy
Source: https://docs.venice.ai/overview/privacy



Nearly all AI apps and services collect user data (personal information, prompt text, and AI text and image responses) in central servers, which they can access, and which they can (and do) share with third parties, ranging from ad networks to governments. Even if a company wants to keep this data safe, data breaches happen [all the time](https://www.wired.com/story/wired-guide-to-data-breaches/), often unreported.

> The only way to achieve reasonable user privacy is to avoid collecting this information in the first place. This is harder to do from an engineering perspective, but we believe it’s the correct approach.

### Privacy as a principle

One of Venice’s guiding principles is user privacy. The platform's architecture flows from this philosophical principle, and every component is designed with this objective in mind.

#### Architecture

The Venice API replicates the same technical architecture as the Venice platform from a backend perspective.

**Venice does not store or log any prompt or model responses on our servers.** API calls are forwarded directly to GPUs running across a collection of decentralized providers over encrypted HTTPS paths.

<img src="https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/privacy-architecture.png?fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=dc109b987638ae5757c4987a971ae809" alt="Venice AI Privacy Architecture" data-og-width="2042" width="2042" data-og-height="812" height="812" data-path="images/privacy-architecture.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/privacy-architecture.png?w=280&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=73d83e285d8065397e72037b907d1509 280w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/privacy-architecture.png?w=560&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=43300078e2e65b024c97164342926b05 560w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/privacy-architecture.png?w=840&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=2994c6fd3f18dd7a18fff305ebb02e2d 840w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/privacy-architecture.png?w=1100&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=e819afb6dd5d785c5fbb176f4b2cb40e 1100w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/privacy-architecture.png?w=1650&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=03b65f4716d95c25ab92e4e733405bc8 1650w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/privacy-architecture.png?w=2500&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=863ab31cb8e886e2f2f67975c6a7fcab 2500w" />


