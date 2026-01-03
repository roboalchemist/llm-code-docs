# Source: https://deepinfra.com/docs/advanced/rate-limits

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

     3. [Running Inference](/docs/inference)

     4. [Data Privacy & Security](/docs/data)

  2. [API Reference](/docs/api-reference)

     1. [OpenAI-Compatible API](/docs/openai_api)

     2. [DeepInfra Native API](/docs/deep_infra_api)

     3. Rate Limits

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

     3. [Running Inference](/docs/inference)

     4. [Data Privacy & Security](/docs/data)

  2. [API Reference](/docs/api-reference)

     1. [OpenAI-Compatible API](/docs/openai_api)

     2. [DeepInfra Native API](/docs/deep_infra_api)

     3. Rate Limits

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

# Rate Limits

## 200 concurrent requests

By default every account has 200 concurrent requests limit per model. If you
are querying two different models simultaneously you will be able to handle a
total of 400 concurrent requests, 200 for each.

We've observed that this is plenty even for applications and serivces with
hundreds of thousands of daily active users.

For large processing batch jobs, like doing embeddings on a knowledge base,
you can use something like [token bucket rate limiting
algorithm](https://en.wikipedia.org/wiki/Token_bucket) to keep under 200
concurrent requests. You will still be able to finish you work in a reasonable
amount of time.

If you need more just let us know why and depending on your case we might
raise it. You can request rate limit increase in your
[dashboard](/dash/account)

## Understanding Concurrent Requests

A concurrent requests limit is the maximum number of requests processed
simultaneously. To illustrate how concurrent requests work, let's consider an
example:

Imagine your application is making requests to our system and has reached the
200 concurrent request limit. Suddenly, 10 of those requests are completed,
freeing up 10 slots. Your application can now send 10 new requests to our
system, which will then be processed concurrently with the remaining 190
requests. This means that even though you've reached the concurrent request
limit, your application can still continue to send new requests as old ones
are completed.

The rate at which you can send new requests depends on how long each request
takes to process. The actual number of requests per minute (RPM) varies based
on the duration of each request. Here are some examples:

Avg Request Duration| Limit| Approximate RPM  
---|---|---  
1 second| 200| 12000 RPM (200 concurrent requests x 60 seconds / 1 second per
request)  
10 seconds| 200| 1200 RPM (200 concurrent requests x 60 seconds / 10 seconds
per request)  
60 seconds| 200| 200 RPM (200 concurrent requests x 60 seconds / 60 seconds
per request)  
  
## Purpose of rate limits

Rate limits are established protocols designed to prevent abuse or misuse of
the API. They ensure fair and consistent access to the API for all users while
maintaining reliable performance.

## How do you check for rate limits?

You will be getting the HTTP **429** response status code with **Rate
limited** message.

Actions to take:

  * retry in a bit
  * or slow down your requests
  * or apply for increase by contacting us

Note: sometimes you might get **429** errors when the model gets too busy.
Typically, the auto-scaling logic will kick in. So if you retry in just a bit,
it should get resolved.

[DeepInfra Native
API](/docs/deep_infra_api)[Webhooks](/docs/advanced/webhooks)

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

[deepseek-ai/DeepSeek-V3.1](/deepseek-
ai/DeepSeek-V3.1)[moonshotai/Kimi-K2-Instruct-0905](/moonshotai/Kimi-K2-Instruct-0905)[zai-
org/GLM-4.6](/zai-org/GLM-4.6)[anthropic/claude-3-7-sonnet-
latest](/anthropic/claude-3-7-sonnet-latest)[deepseek-
ai/DeepSeek-V3.2-Exp](/deepseek-ai/DeepSeek-V3.2-Exp)

Featured Models

[meta-llama/Llama-4-Scout-17B-16E-Instruct](/meta-
llama/Llama-4-Scout-17B-16E-Instruct)[ResembleAI/chatterbox-
turbo](/ResembleAI/chatterbox-
turbo)[nvidia/Nemotron-3-Nano-30B-A3B](/nvidia/Nemotron-3-Nano-30B-A3B)[deepseek-
ai/DeepSeek-V3.2](/deepseek-ai/DeepSeek-V3.2)[openai/whisper-
large-v3-turbo](/openai/whisper-large-v3-turbo)

![Built With Love in Palo Alto](/_next/static/media/love.ce60156e.svg)

[](https://linkedin.com/company/deep-
infra)[](https://x.com/DeepInfra)[](https://github.com/DeepInfra)[](https://discord.gg/x88dCvhqYq)

© 2026 Deep Infra. All rights reserved.

[Privacy Policy](/privacy)[Terms of Service](/terms)

