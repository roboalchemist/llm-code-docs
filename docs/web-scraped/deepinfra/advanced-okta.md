# Source: https://deepinfra.com/docs/advanced/okta

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

     2. [LoRA Adapter Models](/docs/advanced/lora)

     3. [LoRA Image Adapters](/docs/advanced/lora_text_to_image)

  6. [Integrations](/docs/integrations)

     1. [LangChain](/docs/advanced/langchain)

     2. [LlamaIndex](/docs/advanced/llama-index)

     3. [AI SDK](/docs/advanced/aisdk)

     4. [AutoGen](/docs/advanced/autogen)

     5. Okta SSO

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

     2. [LoRA Adapter Models](/docs/advanced/lora)

     3. [LoRA Image Adapters](/docs/advanced/lora_text_to_image)

  6. [Integrations](/docs/integrations)

     1. [LangChain](/docs/advanced/langchain)

     2. [LlamaIndex](/docs/advanced/llama-index)

     3. [AI SDK](/docs/advanced/aisdk)

     4. [AutoGen](/docs/advanced/autogen)

     5. Okta SSO

  7. [Tutorials & Examples](/docs/tutorials)

     1. [Stable Diffusion (Text to Image)](/docs/tutorials/stable-diffusion)

     2. [Whisper (Speech to Text)](/docs/tutorials/whisper)

     3. [Deprecated Models](/docs/advanced/deprecated)

  8. [Miscellaneous](/docs/misc)

     1. [Data Subprocessors](/docs/misc/subprocessors)

# Okta SSO

## Contents

  * Supported features
  * Configuration steps
  * SP Initiated SSO
  * Notes

## Supported Features

  * Single Sign-On (OpenID Connect) initiated via Okta
  * Single Sign-On (OpenID Connect) initiated via DeepInfra
  * Automatically creates user accounts in DeepInfra on first sign in

## Configuration Steps

  * Install the DeepInfra application in your Okta instance
  * Fill in the configuration options: 
    * **Team ID** \-- your okta subdomain is a great starting point. If you need multiple disjoint teams in the same okta instance a.k.a. multi-tenancy, you can use `subdomain-group`, for the **Team ID**. Lowercase only, starting with subdomain, dashes for separators.
    * **Use Stage** \-- leave this blank
  * Assign the users or groups that should be able to log into DeepInfra
  * Go to the DeepInfra App (inside Okta) → Sign On tab and take note of the **Client ID** and **Client Secret**.
  * For the **Issuer** (normally your okta domain): there should be a section that has a link titled _OpenID Provider Metadata_. Click this link. In the JSON document shown, look for a key titled “issuer” and copy the URL-value
  * Send an email to [feedback@deepinfra.com](mailto:feedback@deepinfra.com) that you'd like to setup Okta SSO, including: 
    * Team ID
    * Issuer
    * Client ID
    * Client Secret
    * Admin email -- the email address of the user, who will be admin of the team
  * After the setup is complete the users can start signing in: 
    * via okta (from dashboard)
    * via deepinfra's [sso login](/login_sso), where they need to enter the **Team ID**
  * The user whose email matches the **Admin email** specified in the email will become team admin on first login

## SP-initiated SSO

The sign-in process is initiated from DeepInfra.

  1. From your browser, navigate to the [deepinfra login page](https://deepinfra.com/login).
  2. Click on `Corporate SSO` button.
  3. Enter your **Team ID** and click `SSO Login`
  4. Enter your Okta credentials (your email and password) and click "Sign in with Okta". If your credentials are valid, you are redirected to the DeepInfra dashboard. From there you can click on `Team` to see yourself and the other team members.

## Notes

  * admin can change team member roles (currently toggle between member and admin)
  * admin has access to billing dashboard
  * all team members have acess to the same api-tokens and models
  * if you're interested in single-user-experience -- i.e each person having his own tokens and models, let us know!

[AutoGen](/docs/advanced/autogen)[Tutorials & Examples](/docs/tutorials)

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

[anthropic/claude-3-7-sonnet-latest](/anthropic/claude-3-7-sonnet-latest)[zai-
org/GLM-4.6](/zai-org/GLM-4.6)[deepseek-ai/DeepSeek-V3.2-Exp](/deepseek-
ai/DeepSeek-V3.2-Exp)[moonshotai/Kimi-K2-Instruct-0905](/moonshotai/Kimi-K2-Instruct-0905)[deepseek-
ai/DeepSeek-V3.1](/deepseek-ai/DeepSeek-V3.1)

Featured Models

[deepseek-ai/DeepSeek-OCR](/deepseek-ai/DeepSeek-
OCR)[hexgrad/Kokoro-82M](/hexgrad/Kokoro-82M)[meta-
llama/Llama-3.3-70B-Instruct-Turbo](/meta-llama/Llama-3.3-70B-Instruct-
Turbo)[Qwen/Qwen3-Coder-480B-A35B-Instruct-
Turbo](/Qwen/Qwen3-Coder-480B-A35B-Instruct-Turbo)[deepseek-
ai/DeepSeek-R1-Distill-Llama-70B](/deepseek-ai/DeepSeek-R1-Distill-Llama-70B)

![Built With Love in Palo Alto](/_next/static/media/love.ce60156e.svg)

[](https://linkedin.com/company/deep-
infra)[](https://x.com/DeepInfra)[](https://github.com/DeepInfra)[](https://discord.gg/x88dCvhqYq)

© 2026 Deep Infra. All rights reserved.

[Privacy Policy](/privacy)[Terms of Service](/terms)

