# Source: https://deepinfra.com/docs/inference

We use essential cookies to make our site work. With your consent, we may also
use non-essential cookies to improve user experience and analyze website
traffic…

AcceptReject

[FLUX.2 is live!](https://deepinfra.com/models?q=flux-2) High-fidelity image
generation made simple.

[](/)

[Models](/models)

By Category

* * *

[Automatic Speech Recognition](/models/automatic-speech-
recognition)[Embeddings](/models/embeddings)[Reranker](/models/reranker)[Text
Generation](/models/text-generation)[Text To Image](/models/text-to-
image)[Text To Speech](/models/text-to-speech)[Text To Video](/models/text-to-
video)[Zero Shot Image Classification](/models/zero-shot-image-classification)

[View all models](/models)

By Family

* * *

[![anthropic
logo](/_next/static/media/anthropic.c6636fa8.svg)/Claude](/claude)[![deepseek-
ai
logo](/_next/static/media/deepseek.b1ec6c4e.svg)/DeepSeek](/deepseek)[![black-
forest-labs logo](/_next/static/media/bfl.7e050ff6.svg)/Flux](/flux)[![google
logo](/_next/static/media/google.09551b71.svg)/Gemini](/gemini)[![meta-llama
logo](/_next/static/media/meta.56a2e6fd.svg)/Llama](/llama)[![mistralai
logo](/_next/static/media/mistralai.ecbe51d4.svg)/Mistral](/mistral)[![nvidia
logo](/_next/static/media/nvidia.2165073d.svg)/Nemotron](/nemotron)[![qwen
logo](/_next/static/media/qwen.d6d74288.svg)/Qwen](/qwen)

[Docs](/docs)[Pricing](/pricing)[GPUs](/gpu-
instances)[Chat](/chat)[DeepStart](/deepstart)[Blog](/blog)

[Contact Sales](/contact-sales)[Log In](/login)

[Models](/models)

[Automatic Speech Recognition](/models/automatic-speech-
recognition)[Embeddings](/models/embeddings)[Reranker](/models/reranker)[Text
Generation](/models/text-generation)[Text To Image](/models/text-to-
image)[Text To Speech](/models/text-to-speech)[Text To Video](/models/text-to-
video)[Zero Shot Image Classification](/models/zero-shot-image-classification)

[Docs](/docs)

[Pricing](/pricing)

[GPUs](/gpu-instances)

[Chat](/chat)

[DeepStart](/deepstart)

[Blog](/blog)

Feedback

[Contact Sales](/contact-sales)

[Log In](/login)

  1. [Getting Started](/docs)

     1. [Quick Start Guide](/docs/getting-started)

     2. [Available Models](/docs/models)

     3. Running Inference

     4. [Data Privacy & Security](/docs/data)

  2. [API Reference](/docs/api-reference)

     1. [OpenAI-Compatible API](/docs/openai_api)

     2. [DeepInfra Native API](/docs/deep_infra_api)

     3. [Rate Limits](/docs/advanced/rate-limits)

     4. [Webhooks](/docs/advanced/webhooks)

     5. [Authentication & Tokens](/docs/advanced/scoped_jwt)

  3. [Model Features](/docs/model-features)

     1. [Function Calling](/docs/advanced/function_calling)

     2. [JSON Mode](/docs/advanced/json_mode)

     3. [Multimodal Models](/docs/advanced/multimodal)

     4. [Log Probabilities](/docs/advanced/log_probs)

     5. [Max Output Tokens](/docs/advanced/max_tokens_limit)

  4. [GPU Instances](/docs/gpu-instances)

     1. [Containers](/docs/gpu-instances/containers)

  5. [Custom Deployments](/docs/custom-deployments)

     1. [Custom LLMs](/docs/advanced/custom_llms)

     2. [LoRA Adapter Models](/docs/advanced/lora)

     3. [LoRA Image Adapters](/docs/advanced/lora_text_to_image)

  6. [Integrations](/docs/integrations)

     1. [LangChain](/docs/advanced/langchain)

     2. [LlamaIndex](/docs/advanced/llama-index)

     3. [AI SDK](/docs/advanced/aisdk)

     4. [AutoGen](/docs/advanced/autogen)

     5. [Okta SSO](/docs/advanced/okta)

  7. [Tutorials & Examples](/docs/tutorials)

     1. [Stable Diffusion (Text to Image)](/docs/tutorials/stable-diffusion)

     2. [Whisper (Speech to Text)](/docs/tutorials/whisper)

     3. [Deprecated Models](/docs/advanced/deprecated)

  8. [Miscellaneous](/docs/misc)

     1. [Data Subprocessors](/docs/misc/subprocessors)

Documentation

  1. [Getting Started](/docs)

     1. [Quick Start Guide](/docs/getting-started)

     2. [Available Models](/docs/models)

     3. Running Inference

     4. [Data Privacy & Security](/docs/data)

  2. [API Reference](/docs/api-reference)

     1. [OpenAI-Compatible API](/docs/openai_api)

     2. [DeepInfra Native API](/docs/deep_infra_api)

     3. [Rate Limits](/docs/advanced/rate-limits)

     4. [Webhooks](/docs/advanced/webhooks)

     5. [Authentication & Tokens](/docs/advanced/scoped_jwt)

  3. [Model Features](/docs/model-features)

     1. [Function Calling](/docs/advanced/function_calling)

     2. [JSON Mode](/docs/advanced/json_mode)

     3. [Multimodal Models](/docs/advanced/multimodal)

     4. [Log Probabilities](/docs/advanced/log_probs)

     5. [Max Output Tokens](/docs/advanced/max_tokens_limit)

  4. [GPU Instances](/docs/gpu-instances)

     1. [Containers](/docs/gpu-instances/containers)

  5. [Custom Deployments](/docs/custom-deployments)

     1. [Custom LLMs](/docs/advanced/custom_llms)

     2. [LoRA Adapter Models](/docs/advanced/lora)

     3. [LoRA Image Adapters](/docs/advanced/lora_text_to_image)

  6. [Integrations](/docs/integrations)

     1. [LangChain](/docs/advanced/langchain)

     2. [LlamaIndex](/docs/advanced/llama-index)

     3. [AI SDK](/docs/advanced/aisdk)

     4. [AutoGen](/docs/advanced/autogen)

     5. [Okta SSO](/docs/advanced/okta)

  7. [Tutorials & Examples](/docs/tutorials)

     1. [Stable Diffusion (Text to Image)](/docs/tutorials/stable-diffusion)

     2. [Whisper (Speech to Text)](/docs/tutorials/whisper)

     3. [Deprecated Models](/docs/advanced/deprecated)

  8. [Miscellaneous](/docs/misc)

     1. [Data Subprocessors](/docs/misc/subprocessors)

# Inference

Simple, scalable and cost-effective inference API is the main feature of
DeepInfra. We package state-of-the-art models into a simple rest API that you
can use to build your applications.

There are multiple ways to access the API with different endpoints. You can
choose the one that suits you best.

### OpenAI APIs

For LLMs there is the convenient OpenAI Chat Completions API, and the legacy
OpenAI Completions API. Embedding models also support the OpenAI APIs.

These can be accessed at the following endpoint

    
    
    https://api.deepinfra.com/v1/openai
    
    
    copy

This endpoint works with HTTP/Curl requests as well as with the official
OpenAI libraries for Python & Node.js.

You can [learn more here](/docs/openai_api)

### Inference Endpoints

Every model also has a dedicated inference endpoint.

    
    
    https://api.deepinfra.com/v1/inference/{model_name}
    
    
    copy

for example, for `meta-llama/Meta-Llama-3-8B-Instruct` the endpoint is

    
    
    https://api.deepinfra.com/v1/inference/meta-llama/Meta-Llama-3-8B-Instruct
    
    
    copy

These endpoints can be accessed with REST requests as well as with the
[official DeepInfra Node.js library](https://github.com/deepinfra/deepinfra-
node)

However, bare in mind that for certain cases, like LLMs, this API is more
advanced and harder to uses than the messaging OpenAI Chat Completions API.

### Streaming

All LLM models support streaming with all APIs and libraries, you just have to
pass the `stream` option. You can see many examples in the API section of
every model.

### Authentication

DeepInfra requires an API token to access any of its APIs. You can find yours
in the [dashboard](/dash/api_keys)

To authenticate your requests, you need to pass your API token in the
`Authorization` header with type `Bearer`.

    
    
    Authorization: bearer $AUTH_TOKEN
    

or pass it as a parameter to the appropriate library.

### Content types

Our inference API supports `multipart/form-data` and `application/json`
content types. We strongly suggest to use the latter whenever possible.

#### multipart/form-data

Using `multipart/form-data` makes sense when you want to send binary data such
as media files. Using this content type requires less bandwidth and is more
efficient for large files.

#### application/json

Using `application/json` makes sense when you want to send text data. You can
also use this content type for binary data, using data urls. For example:

    
    
    {
      "image": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBD..."
    }
    
    
    copy

### HTTP Status Codes

We use standard HTTP status codes to indicate the status of the request.

  * `200` \- OK. The request was successful.
  * `4xx` \- Bad Request. The request was invalid or cannot be served.
  * `5xx` \- Internal Server Error. Something went wrong on our side.

### Response Body

The response body is always a JSON object containing the model output. It also
contains metadata about the inference request like `request_id`, `cost`,
`runtime_ms` (except for LLMs), `tokens_input`, `tokens_generated` (LLMs
only).

Example response:

    
    
    {
      "request_id": "RfMWDr1NXCd7cnaegcm3A8q0",
      "inference_status": {
        "cost": 0.004639499820768833,
        "runtime_ms": 1285,
        "status": "succeeded"
      },
      "text": "Hello World"
    }
    
    
    copy

[Available Models](/docs/models)[Data Privacy & Security](/docs/data)

![Footer Logo](/_next/static/media/footer_logo.b3e9d8d3.svg)

![SOC 2
Certified](https://static.sprinto.com/_next/static/images/framework/soc2.png)![ISO
27001
Certified](https://static.sprinto.com/_next/static/images/framework/iso-27001.png)

Have questions or need a custom solution?

[Contact Sales](/contact-sales)

Company

[Pricing](/pricing)

[Docs](/docs)

[Compare](/compare)

[DeepStart](/deepstart)

[About](/about_us)

[Careers](https://jobs.gem.com/deep-infra)

[Contact us](/contact-sales)

[Trust Center](https://trust.deepinfra.com)

[DeepGPT](https://deepgpt.com)

Latest Models

[deepseek-ai/DeepSeek-V3.1](/deepseek-ai/DeepSeek-V3.1)[zai-org/GLM-4.6](/zai-
org/GLM-4.6)[moonshotai/Kimi-K2-Instruct-0905](/moonshotai/Kimi-K2-Instruct-0905)[deepseek-
ai/DeepSeek-V3.2-Exp](/deepseek-
ai/DeepSeek-V3.2-Exp)[anthropic/claude-3-7-sonnet-
latest](/anthropic/claude-3-7-sonnet-latest)

Featured Models

[Qwen/Qwen3-235B-A22B-Thinking-2507](/Qwen/Qwen3-235B-A22B-Thinking-2507)[moonshotai/Kimi-K2-Thinking](/moonshotai/Kimi-K2-Thinking)[sesame/csm-1b](/sesame/csm-1b)[openai/whisper-
large-v3-turbo](/openai/whisper-
large-v3-turbo)[Qwen/Qwen3-Coder-480B-A35B-Instruct](/Qwen/Qwen3-Coder-480B-A35B-Instruct)

![Built With Love in Palo Alto](/_next/static/media/love.ce60156e.svg)

[](https://linkedin.com/company/deep-
infra)[](https://x.com/DeepInfra)[](https://github.com/DeepInfra)[](https://discord.gg/x88dCvhqYq)

© 2026 Deep Infra. All rights reserved.

[Privacy Policy](/privacy)[Terms of Service](/terms)

