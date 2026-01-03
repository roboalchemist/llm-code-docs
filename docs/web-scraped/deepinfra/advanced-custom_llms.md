# Source: https://deepinfra.com/docs/advanced/custom_llms

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

     2. [JSON Mode](/docs/advanced/json_mode)

     3. [Multimodal Models](/docs/advanced/multimodal)

     4. [Log Probabilities](/docs/advanced/log_probs)

     5. [Max Output Tokens](/docs/advanced/max_tokens_limit)

  4. [GPU Instances](/docs/gpu-instances)

     1. [Containers](/docs/gpu-instances/containers)

  5. [Custom Deployments](/docs/custom-deployments)

     1. Custom LLMs

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

     2. [JSON Mode](/docs/advanced/json_mode)

     3. [Multimodal Models](/docs/advanced/multimodal)

     4. [Log Probabilities](/docs/advanced/log_probs)

     5. [Max Output Tokens](/docs/advanced/max_tokens_limit)

  4. [GPU Instances](/docs/gpu-instances)

     1. [Containers](/docs/gpu-instances/containers)

  5. [Custom Deployments](/docs/custom-deployments)

     1. Custom LLMs

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

# Custom LLMs

You can now run a dedicated instance of your public or private LLM on
DeepInfra infrastructure.

## Overview

There are a number of benefits for running your own custom LLM instance:

  * predictable response times
  * auto-scaling support
  * run your own (finetuned or trained from scratch) model

There are of course some drawbacks:

  * pricing is for GPU uptime

It's important to understand that all our publicly available models, like
[mixtral 8x7](/mistralai/Mixtral-8x7B-Instruct-v0.1), are shared among many
users, and this lets us offer very competitive pricing as a result. When you
run your own model, you get full access to the GPUs and pay per GPU/hours your
model is up. So you have to have a sufficient load to justify this resource.

## Usage

### Creating a new deployment

A deployment is a particular configuration of your custom models. It has
fixed:

  * `model_name` \-- the name you'd use when doing inference (generation)
  * `gpu` type -- A100-80GB or H100-80GB supported now, expect more in the future
  * `num_gpus` \-- how many GPUs to use, bigger models require more GPUs (it should at least fit the weights and have some leftover for KV cache)
  * `max_batch_size` \-- how many requests to run in parallel (at most), other requests are queued up
  * weights -- currently Hugging Face is supported (including private repos)

It also has a few settings that can be changed dynamically:

  * `min_instances` \-- how many copies of the model to run at a minumum
  * `max_instances` \-- up to how many copies to scale during times of higher load

To create a new deployment, use the [the Web UI](/dash/deployments?new=custom-
llm):

[![Custom LLM Web UI](/blog/custom-llm-ui.webp)](/dash/deployments?new=custom-
llm)

Or, using the HTTP API:

    
    
    curl -X POST https://api.deepinfra.com/deploy/llm -d '{
        "model_name": "test-model",
        "gpu": "A100-80GB",
        "num_gpus": 2,
        "max_batch_size": 64,
        "hf": {
            "repo": "meta-llama/Llama-2-7b-chat-hf"
        },
        "settings": {
            "min_instances": 0,
            "max_instances": 1,
        }
    }' -H 'Content-Type: application/json' \
        -H "Authorization: Bearer $DEEPINFRA_TOKEN"
    
    
    copy

The deploy can be monitored via HTTP, or the Web dashboard.

Please note that the model full name is _github-username/model-name_. My
github username is `ichernev`, so the model above will have full name
`ichernev/test-model`.

### Using a deployment

When you create a deployment, the name you specify is prefixed by your github
username. So if I (ichernev) create a model `test-model`, it's full name will
be `ichernev/test-model`. You can then use this name during inference, or the
check the model web page:

You can use your model via:

  * Web demo page: <https://deepinfra.com/FULLNAME>
  * HTTP APIs (check <https://deepinfra.com/FULLNAME/api> for details) 
    * DeepInfra interface
    * OpenAI ChatCompletions API
    * OpenAI Completions API

### Updating a deployment

Once a deployment is running, its scaling parameters can be updated via the
deployment details page accessible from [Dashboard /
Deployments](/dash/deployments).

via HTTP:

    
    
    curl -X PUT https://api.deepinfra.com/deploy/DEPLOY_ID -d '{
        "settings": {
            "min_instances": 2,
            "max_instances": 2,
        }
    }' -H 'Content-Type: application/json' \
        -H "Authorization: Bearer YOUR_API_KEY"
    
    
    copy

You'd need your `DEPLOY_ID`. It is returned on creation, but also available in
Web Dashboard or via [HTTP API
`/deploy/list`](https://api.deepinfra.com/docs#/default/deploy_list_deploy_list_get).

### Deleting a deployment

When you want to permanently delete / discard a deployment, use:

  * the trash icon next to a deployment in [Dashboard / Deployments](/dash/deployments)
  * [DELETE /deploy/DEPLOY_ID](https://api.deepinfra.com/docs#/default/deploy_delete_deploy__deploy_id__delete)

## Limitations and Caveats

  * We're enforcing a limit of 4 GPUs per user maximum (4 instances x 1 GPU or 1 instance x 4 GPUs, for example). Contact us if you require more.
  * We try our best to satisfy all requests, but GPUs are a limited resource and sometimes there just isn't enough of it. This means that if try you upscale we might not be able to meet demand (say, you put `min_instances` == 3, but we can only run 2). You're only billed for what actually runs. The current numer of running instances is returned in the deploy object
  * Billing for Custom LLMs will happen weekly, in a separate invoice
  * Leaving a custom LLMs running (by mistake) can quickly rack up costs. For example if you forget to shutdown a custom LLM using 2 GPUs on Friday 5pm, and remember about it on Monday at 9am, that will cost you 256 USD (64h * 2 GPUs * 2 USD). Use spending limits in [payment settings](/dash/billing).
  * Quantization is currently not supported, work in progress

[Custom Deployments](/docs/custom-deployments)[LoRA Adapter
Models](/docs/advanced/lora)

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

[moonshotai/Kimi-K2-Instruct-0905](/moonshotai/Kimi-K2-Instruct-0905)[anthropic/claude-3-7-sonnet-
latest](/anthropic/claude-3-7-sonnet-latest)[deepseek-
ai/DeepSeek-V3.1](/deepseek-ai/DeepSeek-V3.1)[zai-org/GLM-4.6](/zai-
org/GLM-4.6)[deepseek-ai/DeepSeek-V3.2-Exp](/deepseek-ai/DeepSeek-V3.2-Exp)

Featured Models

[MiniMaxAI/MiniMax-M2](/MiniMaxAI/MiniMax-M2)[hexgrad/Kokoro-82M](/hexgrad/Kokoro-82M)[mistralai/Mistral-
Small-3.2-24B-Instruct-2506](/mistralai/Mistral-
Small-3.2-24B-Instruct-2506)[google/gemma-3-12b-it](/google/gemma-3-12b-it)[meta-
llama/Llama-3.3-70B-Instruct-Turbo](/meta-llama/Llama-3.3-70B-Instruct-Turbo)

![Built With Love in Palo Alto](/_next/static/media/love.ce60156e.svg)

[](https://linkedin.com/company/deep-
infra)[](https://x.com/DeepInfra)[](https://github.com/DeepInfra)[](https://discord.gg/x88dCvhqYq)

© 2026 Deep Infra. All rights reserved.

[Privacy Policy](/privacy)[Terms of Service](/terms)

