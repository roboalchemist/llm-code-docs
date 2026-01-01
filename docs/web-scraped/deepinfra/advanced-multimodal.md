# Source: https://deepinfra.com/docs/advanced/multimodal

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

     3. Multimodal Models

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

     2. [JSON Mode](/docs/advanced/json_mode)

     3. Multimodal Models

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

# Using Multimodal models on DeepInfra

DeepInfra hosts multimodal models that support vision and language models
combined. These models can take both images and text as input and provide text
as output.

Currently, we host:

  * [meta-llama/Llama-3.2-90B-Vision-Instruct](/meta-llama/Llama-3.2-90B-Vision-Instruct)
  * [meta-llama/Llama-3.2-11B-Vision-Instruct](/meta-llama/Llama-3.2-11B-Vision-Instruct)
  * [Qwen/QVQ-72B-Preview](/Qwen/QVQ-72B-Preview)

## Quick start

Let's consider this image:

![Example image](https://shared.deepinfra.com/models/llava-
hf/llava-1.5-7b-hf/cover_image.ed4fba7a25b147e7fe6675e9f760585e11274e8ee72596e6412447260493cd4f-s600.webp)

If you ask `What’s in this image?`

The model will answer something like this

    
    
    In this image, a large, colorful animal, possibly a llama, is standing alone in a barren, red and orange landscape, close to a large volcano. The setting appears to be an artistic painting, possibly inspired by South American culture or a fantasy world with volcanoes. The llama is situated at the center of the scene, drawing attention to the contrasting colors and the fiery backdrop of the volcano. The overall atmosphere of the image suggests a sense of danger and mystery amidst the volcanic landscape.
    
    
    copy

Images are passed to the model in two ways:

  1. by passing link to the image (e.g. <https://example.com/image1.jpg>)
  2. by passing base64 encoded image directly in the request

Here is an example of the request.

    
    
    curl "https://api.deepinfra.com/v1/openai/chat/completions" \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $DEEPINFRA_TOKEN" \
      -d '{
        "model": "meta-llama/Llama-3.2-90B-Vision-Instruct",
        "messages": [
          {
            "role": "user",
            "content": [
              {
                "type": "image_url",
                "image_url": {
                  "url": "https://shared.deepinfra.com/models/llava-hf/llava-1.5-7b-hf/cover_image.ed4fba7a25b147e7fe6675e9f760585e11274e8ee72596e6412447260493cd4f-s600.webp"
                }
              },
              {
                "type": "text",
                "text": "What’s in this image?"
              }
            ]
          }
        ]
      }'
    
    
    copy

## Example of uploading base64 encoded image

Uploading images using base64 is convenient when you have images available
locally. Here is an example for it:

    
    
    from openai import OpenAI
    import base64
    import requests
    
    # Create an OpenAI client with your deepinfra token and endpoint
    openai = OpenAI(
        api_key="<your-DeepInfra-API-token>",
        base_url="https://api.deepinfra.com/v1/openai",
    )
    
    image_url = "https://shared.deepinfra.com/models/llava-hf/llava-1.5-7b-hf/cover_image.ed4fba7a25b147e7fe6675e9f760585e11274e8ee72596e6412447260493cd4f-s600.webp"
    base64_image = base64.b64encode(requests.get(image_url).content).decode("utf-8")
    
    chat_completion = openai.chat.completions.create(
        model="meta-llama/Llama-3.2-90B-Vision-Instruct",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    },
                    {
                        "type": "text",
                        "text": "What’s in this image?"
                    }
                ]
            }
        ]
    )
    
    print(chat_completion.choices[0].message.content)
    
    
    copy

## Passing multiple images

API allows to pass multiple images too.

    
    
    curl "https://api.deepinfra.com/v1/openai/chat/completions" \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $DEEPINFRA_TOKEN" \
      -d '{
        "model": "meta-llama/Llama-3.2-90B-Vision-Instruct",
        "messages": [
          {
            "role": "user",
            "content": [
              {
                "type": "image_url",
                "image_url": {
                  "url": "https://shared.deepinfra.com/models/llava-hf/llava-1.5-7b-hf/cover_image.ed4fba7a25b147e7fe6675e9f760585e11274e8ee72596e6412447260493cd4f-s600.webp"
                }
              },
              {
                "type": "image_url",
                "image_url": {
                  "url": "https://shared.deepinfra.com/models/meta-llama/Llama-2-7b-chat-hf/cover_image.10373e7a429dd725e0eb9e57cd20aeb815426c077217b27d9aedce37bd5c2173-s600.webp"
                }
              },
              {
                "type": "text",
                "text": "What’s in this image?"
              }
            ]
          }
        ]
      }'
    
    
    copy

## Calculating costs

Images are tokenized and passed to the model as input. The number of tokens
consumed by an image is reported in the response under
`"usage":{"prompt_tokens": <tokens-for-images-and-text>,...}`.

Different models work with different image resolutions. You can still pass
images of different resolutions, the model will rescale them automatically.
Read the documentation of the model to know the supported image resolutions.

## Limitations and Caveats

  * Supported image types are: jpg, png, and webp.
  * Images must be smaller than 20MB
  * Currently, we don't support passing image fidelity with `detail` argument.

[JSON Mode](/docs/advanced/json_mode)[Log
Probabilities](/docs/advanced/log_probs)

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

[deepseek-ai/DeepSeek-V3.2-Exp](/deepseek-ai/DeepSeek-V3.2-Exp)[zai-
org/GLM-4.6](/zai-org/GLM-4.6)[anthropic/claude-3-7-sonnet-
latest](/anthropic/claude-3-7-sonnet-latest)[deepseek-
ai/DeepSeek-V3.1](/deepseek-
ai/DeepSeek-V3.1)[moonshotai/Kimi-K2-Instruct-0905](/moonshotai/Kimi-K2-Instruct-0905)

Featured Models

[meta-llama/Llama-4-Scout-17B-16E-Instruct](/meta-
llama/Llama-4-Scout-17B-16E-Instruct)[mistralai/Mistral-
Small-3.2-24B-Instruct-2506](/mistralai/Mistral-
Small-3.2-24B-Instruct-2506)[meta-llama/Llama-3.3-70B-Instruct-Turbo](/meta-
llama/Llama-3.3-70B-Instruct-
Turbo)[Qwen/Qwen3-Next-80B-A3B-Instruct](/Qwen/Qwen3-Next-80B-A3B-Instruct)[meta-
llama/Llama-4-Maverick-17B-128E-Instruct-FP8](/meta-
llama/Llama-4-Maverick-17B-128E-Instruct-FP8)

![Built With Love in Palo Alto](/_next/static/media/love.ce60156e.svg)

[](https://linkedin.com/company/deep-
infra)[](https://x.com/DeepInfra)[](https://github.com/DeepInfra)[](https://discord.gg/x88dCvhqYq)

© 2026 Deep Infra. All rights reserved.

[Privacy Policy](/privacy)[Terms of Service](/terms)

