# Source: https://deepinfra.com/docs/advanced/llama-index

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

     2. LlamaIndex

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

     2. [LoRA Adapter Models](/docs/advanced/lora)

     3. [LoRA Image Adapters](/docs/advanced/lora_text_to_image)

  6. [Integrations](/docs/integrations)

     1. [LangChain](/docs/advanced/langchain)

     2. LlamaIndex

     3. [AI SDK](/docs/advanced/aisdk)

     4. [AutoGen](/docs/advanced/autogen)

     5. [Okta SSO](/docs/advanced/okta)

  7. [Tutorials & Examples](/docs/tutorials)

     1. [Stable Diffusion (Text to Image)](/docs/tutorials/stable-diffusion)

     2. [Whisper (Speech to Text)](/docs/tutorials/whisper)

     3. [Deprecated Models](/docs/advanced/deprecated)

  8. [Miscellaneous](/docs/misc)

     1. [Data Subprocessors](/docs/misc/subprocessors)

# LlamaIndex

[LlamaIndex](https://www.llamaindex.ai) is a popular data framework for LLM
applications. And now it works with DeepInfra.

## Large Language Models (LLMs)

### Installation

First, install the necessary package:

    
    
    pip install llama-index-llms-deepinfra
    
    
    copy

### Initialization

Set up the `DeepInfraLLM` class with your API key and desired parameters:

    
    
    from llama_index.llms.deepinfra import DeepInfraLLM
    import asyncio
    
    llm = DeepInfraLLM(
        model="mistralai/Mixtral-8x22B-Instruct-v0.1",  # Default model name
        api_key="$DEEPINFRA_TOKEN",  # Replace with your DeepInfra API key
        temperature=0.5,
        max_tokens=50,
        additional_kwargs={"top_p": 0.9},
    )
    
    
    copy

### Synchronous Complete

Generate a text completion synchronously using the `complete` method:

    
    
    response = llm.complete("Hello World!")
    print(response.text)
    
    
    copy

### Synchronous Stream Complete

Generate a streaming text completion synchronously using the `stream_complete`
method:

    
    
    content = ""
    for completion in llm.stream_complete("Once upon a time"):
        content += completion.delta
        print(completion.delta, end="")
    
    
    copy

### Synchronous Chat

Generate a chat response synchronously using the `chat` method:

    
    
    from llama_index.core.base.llms.types import ChatMessage
    
    messages = [
        ChatMessage(role="user", content="Tell me a joke."),
    ]
    chat_response = llm.chat(messages)
    print(chat_response.message.content)
    
    
    copy

### Synchronous Stream Chat

Generate a streaming chat response synchronously using the `stream_chat`
method:

    
    
    messages = [
        ChatMessage(role="system", content="You are a helpful assistant."),
        ChatMessage(role="user", content="Tell me a story."),
    ]
    content = ""
    for chat_response in llm.stream_chat(messages):
        content += chat_response.delta
        print(chat_response.delta, end="")
    
    
    copy

### Asynchronous Complete

Generate a text completion asynchronously using the `acomplete` method:

    
    
    async def async_complete():
        response = await llm.acomplete("Hello Async World!")
        print(response.text)
    
    asyncio.run(async_complete())
    
    
    copy

### Asynchronous Stream Complete

Generate a streaming text completion asynchronously using the
`astream_complete` method:

    
    
    async def async_stream_complete():
        content = ""
        response = await llm.astream_complete("Once upon an async time")
        async for completion in response:
            content += completion.delta
            print(completion.delta, end="")
    
    asyncio.run(async_stream_complete())
    
    
    copy

### Asynchronous Chat

Generate a chat response asynchronously using the `achat` method:

    
    
    async def async_chat():
        messages = [
            ChatMessage(role="user", content="Tell me an async joke."),
        ]
        chat_response = await llm.achat(messages)
        print(chat_response.message.content)
    
    asyncio.run(async_chat())
    
    
    copy

### Asynchronous Stream Chat

Generate a streaming chat response asynchronously using the `astream_chat`
method:

    
    
    async def async_stream_chat():
        messages = [
            ChatMessage(role="system", content="You are a helpful assistant."),
            ChatMessage(role="user", content="Tell me an async story."),
        ]
        content = ""
        response = await llm.astream_chat(messages)
        async for chat_response in response:
            content += chat_response.delta
            print(chat_response.delta, end="")
    
    asyncio.run(async_stream_chat())
    
    
    copy

## Embeddings

[LlamaIndex](https://www.llamaindex.ai) can also work with DeepInfra
[embeddings models](/models/embeddings) to get embeddings for your text data.

### Installation

    
    
    pip install llama-index llama-index-embeddings-deepinfra
    
    
    copy

### Initialization

    
    
    from dotenv import load_dotenv, find_dotenv
    from llama_index.embeddings.deepinfra import DeepInfraEmbeddingModel
    
    _ = load_dotenv(find_dotenv())
    
    model = DeepInfraEmbeddingModel(
        model_id="BAAI/bge-large-en-v1.5",  # Use custom model ID
        api_token="YOUR_API_TOKEN",  # Optionally provide token here
        normalize=True,  # Optional normalization
        text_prefix="text: ",  # Optional text prefix
        query_prefix="query: ",  # Optional query prefix
    )
    
    
    copy

### Synchronous Requests

#### Get Text Embedding

    
    
    response = model.get_text_embedding("hello world")
    print(response)
    
    
    copy

#### Batch Requests

    
    
    texts = ["hello world", "goodbye world"]
    response_batch = model.get_text_embedding_batch(texts)
    print(response_batch)
    
    
    copy

#### Query Requests

    
    
    query_response = model.get_query_embedding("hello world")
    print(query_response)
    
    
    copy

### Asynchronous Requests

#### Get Text Embedding

    
    
    async def main():
        text = "hello world"
        async_response = await model.aget_text_embedding(text)
        print(async_response)
    
    if __name__ == "__main__":
        import asyncio
        asyncio.run(main())
    
    
    copy

[LangChain](/docs/advanced/langchain)[AI SDK](/docs/advanced/aisdk)

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
org/GLM-4.6](/zai-org/GLM-4.6)[deepseek-ai/DeepSeek-V3.2-Exp](/deepseek-
ai/DeepSeek-V3.2-Exp)[deepseek-ai/DeepSeek-V3.1](/deepseek-
ai/DeepSeek-V3.1)[anthropic/claude-3-7-sonnet-
latest](/anthropic/claude-3-7-sonnet-latest)

Featured Models

[MiniMaxAI/MiniMax-M2](/MiniMaxAI/MiniMax-M2)[openai/gpt-oss-20b](/openai/gpt-
oss-20b)[anthropic/claude-4-opus](/anthropic/claude-4-opus)[meta-
llama/Llama-4-Maverick-17B-128E-Instruct-FP8](/meta-
llama/Llama-4-Maverick-17B-128E-Instruct-FP8)[openai/gpt-
oss-120b](/openai/gpt-oss-120b)

![Built With Love in Palo Alto](/_next/static/media/love.ce60156e.svg)

[](https://linkedin.com/company/deep-
infra)[](https://x.com/DeepInfra)[](https://github.com/DeepInfra)[](https://discord.gg/x88dCvhqYq)

© 2026 Deep Infra. All rights reserved.

[Privacy Policy](/privacy)[Terms of Service](/terms)

