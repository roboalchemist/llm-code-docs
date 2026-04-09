# Source: https://deepinfra.com/docs/advanced/scoped_jwt

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

     5. Authentication & Tokens

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

     3. [Rate Limits](/docs/advanced/rate-limits)

     4. [Webhooks](/docs/advanced/webhooks)

     5. Authentication & Tokens

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

# Scoped JWT authentication

## Contents

  * Overview
  * Format
    * Header
    * Payload
    * Signature
    * Token
  * Usage

## Overview

Scoped JWT authentication allows you to create scope-limited tokens for
accessing DeepInfra inference API endpoints.

For example, you can issue a scoped JWT and give it to a third party that you
provide services to. That third party can now directly do inference using the
JWT, but limited to your specification. You don't need to share your API key
with that party or to proxy their requests.

Scoped JWT tokens are associated with an API key, and they let you specify
expiration, allowed models and spending limit.

Inference usage done with a scoped JWT will be counted towards the API key
that was used for signing that token.

## Simple Usage

You can create JWT tokens with a POST to /v1/scoped-jwt:

    
    
    curl -X POST "https://api.deepinfra.com/v1/scoped-jwt" \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $DEEPINFRA_API_KEY" \
      -d '{
          "api_key_name": "auto",
          "models": ["deepseek-ai/DeepSeek-R1"],
          "expires_delta": 3600,
          "spending_limit": 1.0
      }'
    
    {"token":"jwt:eyJhbGciOiJIUzI1NiIsImtpZCxxxxxxxxxxxxxxxxxx"}
    
    
    copy

This creates a JWT token associated with api key `auto`, limited to
deepseek-r1, expiring in 1 hour, with spending limit 1.00 USD.

You can skip `models` (allow any model), `expires_delta` (no expiration -- ATM
that means 1 year) and `spending_limit` (no spending limit). Also you can
provide `expires_at` (unix TS) instead of `expires_delta`.

You can also check (decode) the JWT token via GET to /v1/scoped-jwt (make sure
the token used is the same as the encoding token).

    
    
    curl "https://api.deepinfra.com/v1/scoped-jwt?jwtoken=XXXX" \
        -H "Authorization: Bearer $DEEPINFRA_API_KEY"
    
    {
      "expires_at": 1738843515,
      "models": [
        "deepseek-ai/DeepSeek-R1"
      ],
      "spending_limit": 1
    }
    
    
    copy

## Usage

Once issued, the scoped JWT can be used in all inference endpoints in place of
an API key, but only if the restrictions are met (models allowed, before
expiration date, before money limit is exhausted).

    
    
    curl "https://api.deepinfra.com/v1/openai/chat/completions" \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $SCOPED_JWT" \
      -d '{
          "model": "deepseek-ai/DeepSeek-R1",
          "messages": [
            {
              "role": "user",
              "content": "Hello!"
            }
          ]
        }'
    
    
    copy

## Format

You can also create and inspect Scoped JWT tokens yourself, here is a detailed
explanation on how they are formed. The generral idea is that the payload
encodes the restrictions and the signature is based on the API key used.

### Header

For the standard `alg` field we only accept `HS256` value (HMAC-SHA256). This
is the algorithm you should use to produce the signature.

The `kid` field stores your key id. It is formed from your DeepInfra id and
the Base64 encoding of the name of the API key you use for signing. These two
parts are concatenate with a colon separator.

In the example bellow we specify a user with id `di:1000000000000` with an API
key named `auto`, which when Base64 encoded becomes `YXV0bw==`. Then we
concatenate the two with a colon to get the key id
`di:1000000000000:YXV0bw==`.

    
    
    {
        "alg": "HS256",
        "kid": "di:1000000000000:YXV0bw==",
        "typ": "JWT"
    }
    
    
    copy

### Payload

The `sub` field specifies again your user id. The `model` field specifies
which model the token is will be allows to access. The `exp` specifies an
expiration UTC timestamp in seconds, that can point to no later than week from
the moment of issuing the token.

    
    
    {
        "sub": "di:1000000000000",
        "model": "deepseek-ai/DeepSeek-R1",
        "exp": 1734616903
    }
    
    
    copy

### Signature

Employ the standard way of calculating the JWT signature, using your chosen
API key as a secret. We support only the HMAC-SHA256 algorithm.

    
    
    HMAC_SHA256(
      api_key,
      base64urlEncoding(header) + '.' + base64urlEncoding(payload)
    )
    

### Token

Finally, encode the the three parts and concatenate them with the period
separator to form the token.

    
    
    scoped_jwt = 'jwt:' + base64urlEncoding(header) + '.' +
        base64urlEncoding(payload) + '.' + base64urlEncoding(signature)
    

[Webhooks](/docs/advanced/webhooks)[Model Features](/docs/model-features)

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

[anthropic/claude-3-7-sonnet-latest](/anthropic/claude-3-7-sonnet-
latest)[moonshotai/Kimi-K2-Instruct-0905](/moonshotai/Kimi-K2-Instruct-0905)[zai-
org/GLM-4.6](/zai-org/GLM-4.6)[deepseek-ai/DeepSeek-V3.1](/deepseek-
ai/DeepSeek-V3.1)[deepseek-ai/DeepSeek-V3.2-Exp](/deepseek-
ai/DeepSeek-V3.2-Exp)

Featured Models

[MiniMaxAI/MiniMax-M2](/MiniMaxAI/MiniMax-M2)[meta-llama/Llama-
Guard-4-12B](/meta-llama/Llama-Guard-4-12B)[openai/whisper-
large-v3-turbo](/openai/whisper-
large-v3-turbo)[moonshotai/Kimi-K2-Instruct-0905](/moonshotai/Kimi-K2-Instruct-0905)[deepseek-
ai/DeepSeek-V3-0324](/deepseek-ai/DeepSeek-V3-0324)

![Built With Love in Palo Alto](/_next/static/media/love.ce60156e.svg)

[](https://linkedin.com/company/deep-
infra)[](https://x.com/DeepInfra)[](https://github.com/DeepInfra)[](https://discord.gg/x88dCvhqYq)

© 2026 Deep Infra. All rights reserved.

[Privacy Policy](/privacy)[Terms of Service](/terms)

