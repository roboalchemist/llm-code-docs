# Source: https://deepinfra.com/docs/advanced/json_mode

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

     3. [Rate Limits](/docs/advanced/rate-limits)

     4. [Webhooks](/docs/advanced/webhooks)

     5. [Authentication & Tokens](/docs/advanced/scoped_jwt)

  3. [Model Features](/docs/model-features)

     1. [Function Calling](/docs/advanced/function_calling)

     2. JSON Mode

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

     3. [Rate Limits](/docs/advanced/rate-limits)

     4. [Webhooks](/docs/advanced/webhooks)

     5. [Authentication & Tokens](/docs/advanced/scoped_jwt)

  3. [Model Features](/docs/model-features)

     1. [Function Calling](/docs/advanced/function_calling)

     2. JSON Mode

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

# JSON Mode

In addition to responding in text, the DeepInfra API has an option to request
that responsesbe returned in JSON format. [To learn more, read our
blog](/blog/json-mode).

We provide JSON mode both in our inference API as well as our OpenAI
compatible API, supported by [a lot of our models](/models?q=json).

## Using JSON Mode

Activating a JSON response in any of deepinfra's text APIs, including
`/v1/inference`, `/v1/openai/completions` and `/v1/openai/chat/completions` is
performed in the same way: adding a parameter `response_format` and setting
its value to `{"type": "json_object"}`

### Example

Let's go through some simple example of learning about scientific discoveries.

This is how you set up our endpoint

    
    
    import openai
    import json
    
    client = openai.OpenAI(
        base_url="https://api.deepinfra.com/v1/openai",
        api_key="<Your-DeepInfra-API-Key>",
    )
    
    
    copy

Here is an example of using the openai chat API to invoke a model with JSON
mode:

    
    
    messages = [
        {
            "role": "user",
            "content": "Provide a JSON list of 3 famous scientific breakthroughs in the past century, all of the countries which contributed, and in what year."
        }
    ]
    
    response = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.1",
        messages=messages,
        response_format={"type":"json_object"},
        tool_choice="auto",
    )
    

The resulting `response.choices[0].message.content` will contain a string with
JSON:

    
    
    {
      "breakthroughs": [
        {
          "name": "Penicillin",
          "country": "UK",
          "year": 1928
        },
        {
          "name": "The Double Helix Structure of DNA",
          "country": "US",
          "year": 1953
        },
        {
          "name": "Artificial Heart",
          "country": "US",
          "year": 2008
        }
      ]
    }
    
    
    copy

## Caveats and warnings

It is highly recommended to prompt the model to produce JSON. While this is
not strictly necessary, failing to prompt the model to produce JSON can
occasionally produce nonsensical responses as the model may misunderstand your
intent. For example, a model unaware it is producing JSON may mismatch a
quote, leading to stray `:` characters appearing in strings, which while still
technically valid JSON, may degrade the quality of the response.

Currently, the API will not guarantee the resulting JSON object is complete at
the end of a response.

For example, if the model stops due to `length`, the JSON object in the
response will be improperly terminated, for example in the middle of a string
or object.

### A note about JSON and model alignment and accuracy

As a big warning and caveat of JSON mode, JSON mode interferes with model's
alignment, or "self-control". In particular, when forced to produce a JSON
response, the model will be more likely to make up information rather than
explain that it does not know, or it will be more likely to behave in ways
that fall outside of its training, producing undesirable output rather than
objecting.

Let's take a really simple prompt:

    
    
    messages = [
        {
            "role": "user",
            "content": "What is the weather in San Francisco?"
        }
    ]
    response = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.1",
        messages=messages,
        tool_choice="auto",
    )
    
    
    copy

This prompt, using the default `"text"` `response_format` will give a
reasonable canned response:

    
    
    " I don't have real-time updates or location tracking capabilities, so I can't provide current weather information for San Francisco. Please check a reliable weather website or app for this information."
    

However, now let's add `response_format={"type": "json_object"}`. The model
now merrily produces a made-up weather forecast with no objection:

    
    
    {
      "location":"San Francisco",
      "weather":[
        {
          "timestamp":163856000,
          "description":"Mostly cloudy",
          "temperature":25,
          "feels_like":26.2,
          "humidity":80,
          "wind":{
            "speed":4.7,
            "degrees":0
          }
        }
      ]
    }
    
    
    copy

Because this output format effectively overly constrains the model in such a
way that it cannot produce alignment warnings, it instead responds with the
most probable tokens, a wildly inaccurate guess of today's weather.

[Function Calling](/docs/advanced/function_calling)[Multimodal
Models](/docs/advanced/multimodal)

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

[deepseek-ai/DeepSeek-V3.2-Exp](/deepseek-ai/DeepSeek-V3.2-Exp)[deepseek-
ai/DeepSeek-V3.1](/deepseek-ai/DeepSeek-V3.1)[anthropic/claude-3-7-sonnet-
latest](/anthropic/claude-3-7-sonnet-latest)[zai-org/GLM-4.6](/zai-
org/GLM-4.6)[moonshotai/Kimi-K2-Instruct-0905](/moonshotai/Kimi-K2-Instruct-0905)

Featured Models

[deepseek-ai/DeepSeek-V3](/deepseek-ai/DeepSeek-V3)[deepseek-
ai/DeepSeek-V3.1](/deepseek-
ai/DeepSeek-V3.1)[google/gemma-3-27b-it](/google/gemma-3-27b-it)[PaddlePaddle/PaddleOCR-
VL-0.9B](/PaddlePaddle/PaddleOCR-VL-0.9B)[mistralai/Mistral-
Small-3.2-24B-Instruct-2506](/mistralai/Mistral-Small-3.2-24B-Instruct-2506)

![Built With Love in Palo Alto](/_next/static/media/love.ce60156e.svg)

[](https://linkedin.com/company/deep-
infra)[](https://x.com/DeepInfra)[](https://github.com/DeepInfra)[](https://discord.gg/x88dCvhqYq)

© 2026 Deep Infra. All rights reserved.

[Privacy Policy](/privacy)[Terms of Service](/terms)

