# Source: https://deepinfra.com/docs/advanced/lora

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

     1. [Custom LLMs](/docs/advanced/custom_llms)

     2. LoRA Adapter Models

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

     1. [Custom LLMs](/docs/advanced/custom_llms)

     2. LoRA Adapter Models

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

# Deploying LoRA adapter model

### How to deploy LoRA adapter model

  1. Navigate to the dashboard <https://deepinfra.com/dash>
  2. Click on the 'New Deployment' button
  3. Click on the 'LoRA Model' tab
  4. Fill the form: 
     * **LoRA model name** : model name used to reference the deployment
     * **Hugging Face Model Name** : Hugging Face model name
     * **Hugging Face Token** : (optional) Hugging Face token if the LoRA adapter model is private

### To use LoRA adapter model, you need

  1. LoRA adapter model hosted on Hugging Face
  2. Base model that supports LoRA adapter at DeepInfra (you can see the list of supported base models in upload lora form)
  3. Hugging Face token if the LoRA adapter model is private
  4. DeepInfra account, and DeepInfra API key

### Example flow:

Prerequisites:

  1. askardeepinfra/llama-3.1-8B-rank-32-example-lora
  2. The base model is meta-llama/Meta-Llama-3.1-8B-Instruct which is supported at DeepInfra
  3. The LoRA adapter model is public, so no need for Hugging Face token
  4. DeepInfra API key is generated from <https://deepinfra.com/dash/api_keys> page

Then I'm gonna deploy the model:

  1. Navigate to the dashboard <https://deepinfra.com/dash>
  2. Click on the 'New Deployment' button
  3. Click on the 'LoRA Model' tab
  4. Fill the form: 
     * **LoRA model name** : asdf/lora-example
     * **Hugging Face Model Name** : askardeepinfra/llama-3.1-8B-rank-32-example-lora
  5. Click on the 'Upload' button

Now the deployment should appear in <https://deepinfra.com/dash/deployments>
page, with a name asdf/lora-example. Initially the state is "Initializing",
after a while it should become "Deploying" and then "Running". Once the state
is "Running", you can use the model.

Navigate to <https://deepinfra.com/asdf/lora-example> where you can find all
the information about the the model including:

  1. Pricing
  2. Precision
  3. Demo page, where you can test the model
  4. API reference, where you can find information how to inference the model using REST API

I'll leave example of inference with curl below:

    
    
    curl "https://api.deepinfra.com/v1/openai/chat/completions" \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $DEEPINFRA_API_KEY" \
      -d '{
          "model": "asdf/lora-example",
          "messages": [
            {
              "role": "user",
              "content": "Hello!"
            }
          ]
        }'
    
    
    copy

[Custom LLMs](/docs/advanced/custom_llms)[LoRA Image
Adapters](/docs/advanced/lora_text_to_image)

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

[moonshotai/Kimi-K2-Instruct-0905](/moonshotai/Kimi-K2-Instruct-0905)[zai-
org/GLM-4.6](/zai-org/GLM-4.6)[deepseek-ai/DeepSeek-V3.1](/deepseek-
ai/DeepSeek-V3.1)[deepseek-ai/DeepSeek-V3.2-Exp](/deepseek-
ai/DeepSeek-V3.2-Exp)[anthropic/claude-3-7-sonnet-
latest](/anthropic/claude-3-7-sonnet-latest)

Featured Models

[openai/whisper-large-v3-turbo](/openai/whisper-
large-v3-turbo)[Qwen/Qwen3-32B](/Qwen/Qwen3-32B)[sesame/csm-1b](/sesame/csm-1b)[mistralai/Voxtral-
Mini-3B-2507](/mistralai/Voxtral-
Mini-3B-2507)[nvidia/Nemotron-3-Nano-30B-A3B](/nvidia/Nemotron-3-Nano-30B-A3B)

![Built With Love in Palo Alto](/_next/static/media/love.ce60156e.svg)

[](https://linkedin.com/company/deep-
infra)[](https://x.com/DeepInfra)[](https://github.com/DeepInfra)[](https://discord.gg/x88dCvhqYq)

© 2026 Deep Infra. All rights reserved.

[Privacy Policy](/privacy)[Terms of Service](/terms)

