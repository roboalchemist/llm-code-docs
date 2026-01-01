# Source: https://deepinfra.com/docs/openai_api

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

     1. OpenAI-Compatible API

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

     3. [Running Inference](/docs/inference)

     4. [Data Privacy & Security](/docs/data)

  2. [API Reference](/docs/api-reference)

     1. OpenAI-Compatible API

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

# OpenAI API

We offer OpenAI compatible API for all [LLM models](/models/text-generation)
and all [Embeddings models](/models/embeddings).

The APIs we support are:

  * [chat completion](https://platform.openai.com/docs/guides/gpt/chat-completions-api) — both streaming and regular
  * [completion](https://platform.openai.com/docs/guides/gpt/completions-api) — both streaming and regular
  * [embeddings](https://platform.openai.com/docs/guides/embeddings) — supported for all embeddings models.

The endpoint for the OpenAI APIs is `https://api.deepinfra.com/v1/openai`.

You can do HTTP requests. You can also use the official Python and Node.js
libraries. In all cases streaming is also supported.

### Official libraries

For Python you should run

    
    
    pip install openai
    
    
    copy

For JavaScript/Node.js you should run

    
    
    npm install openai
    
    
    copy

### Chat Completions

The Chat Completions API is the easiest to use. You exchange messages and it
just works. You can change the model to another LLM and it will continue
working.

PythonJavaScriptbash

    
    
    from openai import OpenAI
    
    openai = OpenAI(
        api_key="$DEEPINFRA_TOKEN",
        base_url="https://api.deepinfra.com/v1/openai",
    )
    
    stream = True # or False
    
    chat_completion = openai.chat.completions.create(
        model="meta-llama/Meta-Llama-3-8B-Instruct",
        messages=[{"role": "user", "content": "Hello"}],
        stream=stream,
    )
    
    if stream:
        for event in chat_completion:
            if event.choices[0].finish_reason:
                print(event.choices[0].finish_reason,
                      event.usage['prompt_tokens'],
                      event.usage['completion_tokens'])
            else:
                print(event.choices[0].delta.content)
    else:
        print(chat_completion.choices[0].message.content)
        print(chat_completion.usage.prompt_tokens, chat_completion.usage.completion_tokens)
    
    
    copy

You can see more complete examples at the documentation page of each model.

### Conversations with Chat Completions

To create a longer chat-like conversation you have to add each response
message and each of the user's messages to every request. This way the model
will have the context and will be able to provide better answers. You can
tweak it even further by providing a system message.

PythonJavaScriptbash

    
    
    from openai import OpenAI
    
    openai = OpenAI(
        api_key="$DEEPINFRA_TOKEN",
        base_url="https://api.deepinfra.com/v1/openai",
    )
    
    stream = True # or False
    
    chat_completion = openai.chat.completions.create(
        model="meta-llama/Meta-Llama-3-8B-Instruct",
        messages=[
            {"role": "system", "content": "Respond like a michelin starred chef."},
            {"role": "user", "content": "Can you name at least two different techniques to cook lamb?"},
            {"role": "assistant", "content": "Bonjour! Let me tell you, my friend, cooking lamb is an art form, and I'm more than happy to share with you not two, but three of my favorite techniques to coax out the rich, unctuous flavors and tender textures of this majestic protein. First, we have the classic \"Sous Vide\" method. Next, we have the ancient art of \"Sous le Sable\". And finally, we have the more modern technique of \"Hot Smoking.\""},
            {"role": "user", "content": "Tell me more about the second method."},
        ],
        stream=stream,
    )
    
    if stream:
        for event in chat_completion:
            if event.choices[0].finish_reason:
                print(event.choices[0].finish_reason,
                      event.usage['prompt_tokens'],
                      event.usage['completion_tokens'])
            else:
                print(event.choices[0].delta.content)
    else:
        print(chat_completion.choices[0].message.content)
        print(chat_completion.usage.prompt_tokens, chat_completion.usage.completion_tokens)
    
    
    copy

The longer the conversation gets, the more time it takes the model to generate
the response. The number of messages that you can have in a conversation is
limited by the context size of a model. Larger models also usually take more
time to respond and are more expensive.

### Completions

This is an advanced API. You should know how to format the input to make it
work. Different models might have a different input format. The example below
is for [meta-llama/Meta-Llama-3-8B-Instruct](/meta-llama/Meta-
Llama-3-8B-Instruct). You can see the model's input format in the API section
on its page.

PythonJavaScriptbash

    
    
    from openai import OpenAI
    
    openai = OpenAI(
        api_key="$DEEPINFRA_TOKEN",
        base_url="https://api.deepinfra.com/v1/openai",
    )
    
    stream = True # or False
    
    completion = openai.completions.create(
        model='meta-llama/Meta-Llama-3-8B-Instruct',
        prompt='<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n\nHello!<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n',
        stop=['<|eot_id|>'],
        stream=stream,
    )
    
    if stream:
        for event in completion:
            if event.choices[0].finish_reason:
                print(event.choices[0].finish_reason,
                      event.usage.prompt_tokens,
                      event.usage.completion_tokens)
            else:
                print(event.choices[0].text)
    else:
        print(completion.choices[0].text)
        print(completion.usage.prompt_tokens, completion.usage.completion_tokens)
    
    
    copy

For every model you can check its input format in the API section on its page.

### Embeddings

DeepInfra supports the OpenAI embeddings API. The following creates an
embedding vector representing the input text

PythonJavaScriptbash

    
    
    from openai import OpenAI
    
    openai = OpenAI(
        api_key="$DEEPINFRA_TOKEN",
        base_url="https://api.deepinfra.com/v1/openai",
    )
    
    input = "The food was delicious and the waiter...", # or an array ["hello", "world"]
    
    embeddings = openai.embeddings.create(
      model="BAAI/bge-large-en-v1.5",
      input=input,
      encoding_format="float"
    )
    
    if isinstance(input, str):
        print(embeddings.data[0].embedding)
    else:
        for i in range(len(input)):
            print(embeddings.data[i].embedding)
    
    print(embeddings.usage.prompt_tokens)
    
    
    copy

### Image Generation

You can use the OpenAI compatible API to generate images. Here's an example
using Python:

PythonJavaScriptbash

    
    
    import io
    import base64
    from PIL import Image
    from openai import OpenAI
    
    client = OpenAI(
        api_key="$DEEPINFRA_TOKEN",
        base_url="https://api.deepinfra.com/v1/openai"
    )
    
    if __name__ == "__main__":
        response = client.images.generate(
            prompt="A photo of an astronaut riding a horse on Mars.",
            size="1024x1024",
            quality="standard",
            n=1,
        )
        b64_json = response.data[0].b64_json
        image_bytes = base64.b64decode(b64_json)
        image = Image.open(io.BytesIO(image_bytes))
        image.save("output.png")
    
    
    copy

## Model parameter

Some models have more than one version available, you can infer against a
particular version by specifying `{"model": "MODEL_NAME:VERSION", ...}`
format.

You could also infer against a `deploy_id`, by using `{"model":
"deploy_id:DEPLOY_ID", ...}`. This is especially useful for [Custom
LLMs](/docs/advanced/custom_llms), you can infer before the deployment is
running (and before you have the model-name+version pair).

## Caveats

Please note that we might not be 100% compatible yet, let us know in discord
or by email if something you require is missing. Supported request attributes:

ChatCompletions and Completions:

  * `model`, including specifying `version`/`deploy_id` support
  * `messages` (roles `system`, `user`, `assistant`)
  * `max_tokens`
  * `stream`
  * `temperature`
  * `top_p`
  * `stop`
  * `n`
  * `presence_penalty`
  * `frequency_penalty`
  * `response_format` (`{"type": "json"}` only, it will return default format when omitted)
  * `tools`, `tool_choice`
  * `echo`, `logprobs` \-- only for (non chat) completions

`deploy_id` might not be immediately avaiable if the model is currently
deploying

Embeddings:

  * `model`
  * `input`
  * `encoding_format` \-- `float` only

Images:

  * `model` \-- Defaults to FLUX Schnell
  * `quality` and `style` \-- only available for compatibility.
  * `response_format` \-- only `b64_json` supported for now.

You can see even more details on each model's page.

[API Reference](/docs/api-reference)[DeepInfra Native
API](/docs/deep_infra_api)

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
ai/DeepSeek-V3.1)[moonshotai/Kimi-K2-Instruct-0905](/moonshotai/Kimi-K2-Instruct-0905)[deepseek-
ai/DeepSeek-V3.2-Exp](/deepseek-ai/DeepSeek-V3.2-Exp)[zai-org/GLM-4.6](/zai-
org/GLM-4.6)[anthropic/claude-3-7-sonnet-latest](/anthropic/claude-3-7-sonnet-
latest)

Featured Models

[Qwen/Qwen3-235B-A22B-Thinking-2507](/Qwen/Qwen3-235B-A22B-Thinking-2507)[sesame/csm-1b](/sesame/csm-1b)[meta-
llama/Llama-3.3-70B-Instruct-Turbo](/meta-llama/Llama-3.3-70B-Instruct-
Turbo)[nvidia/Nemotron-3-Nano-30B-A3B](/nvidia/Nemotron-3-Nano-30B-A3B)[moonshotai/Kimi-K2-Instruct-0905](/moonshotai/Kimi-K2-Instruct-0905)

![Built With Love in Palo Alto](/_next/static/media/love.ce60156e.svg)

[](https://linkedin.com/company/deep-
infra)[](https://x.com/DeepInfra)[](https://github.com/DeepInfra)[](https://discord.gg/x88dCvhqYq)

© 2026 Deep Infra. All rights reserved.

[Privacy Policy](/privacy)[Terms of Service](/terms)

