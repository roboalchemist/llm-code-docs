# Source: https://deepinfra.com/docs/advanced/aisdk

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

     3. AI SDK

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

     2. [LlamaIndex](/docs/advanced/llama-index)

     3. AI SDK

     4. [AutoGen](/docs/advanced/autogen)

     5. [Okta SSO](/docs/advanced/okta)

  7. [Tutorials & Examples](/docs/tutorials)

     1. [Stable Diffusion (Text to Image)](/docs/tutorials/stable-diffusion)

     2. [Whisper (Speech to Text)](/docs/tutorials/whisper)

     3. [Deprecated Models](/docs/advanced/deprecated)

  8. [Miscellaneous](/docs/misc)

     1. [Data Subprocessors](/docs/misc/subprocessors)

# AI SDK

The [AI SDK](https://sdk.vercel.ai/) by Vercel is the AI Toolkit for
TypeScript and JavaScript from the creators of Next.js. It is a free open-
source library that gives you the tools you need to build AI-powered products.

What's even better is that it works with [LLM models by
DeepInfra](/models/text-generation) out of the box. You can check [AI SDK
docs](https://sdk.vercel.ai/providers/ai-sdk-providers/deepinfra#deepinfra-
provider).

# Install AI SDK

    
    
    npm install ai @ai-sdk/deepinfra
    
    
    copy

# LLM Examples

The examples below show how to use the AI SDK with DeepInfra and large
language models. Make sure to get your API key from DeepInfra. You have to
[Login](https://deepinfra.com/login?from=%2Fdash) and get your token.

## Text Generation

    
    
    import { createDeepInfra } from "@ai-sdk/deepinfra";
    import { generateText } from "ai";
    
    const deepinfra = createDeepInfra({
      apiKey: "$DEEPINFRA_TOKEN",
    });
    
    const { text, usage, finishReason } = await generateText({
      model: deepinfra("meta-llama/Llama-3.3-70B-Instruct-Turbo"),
      prompt: "Write a vegetarian lasagna recipe for 4 people.",
    });
    
    console.log(text);
    console.log(usage);
    console.log(finishReason);
    
    
    copy

You can improve the answers further by providing a system message

    
    
    import { createDeepInfra } from "@ai-sdk/deepinfra";
    import { generateText } from "ai";
    
    const deepinfra = createDeepInfra({
      apiKey: "$DEEPINFRA_TOKEN",
    });
    
    const { text, usage, finishReason } = await generateText({
      model: deepinfra("meta-llama/Llama-3.3-70B-Instruct-Turbo"),
      prompt: "Write a vegetarian lasagna recipe for 4 people.",
      system:
        "You are a professional writer. " +
        "You write simple, clear, and concise content.",
    });
    
    console.log(text);
    console.log(usage);
    console.log(finishReason);
    
    
    copy

## Streaming

Generating text is nice, but your users don't want to wait when large amount
of text is generated. For those use cases you can use streaming.

    
    
    import { createDeepInfra } from "@ai-sdk/deepinfra";
    import { streamText } from "ai";
    
    const deepinfra = createDeepInfra({
      apiKey: "$DEEPINFRA_TOKEN",
    });
    
    const result = streamText({
      model: deepinfra("meta-llama/Llama-3.3-70B-Instruct-Turbo"),
      prompt: "Invent a new holiday and describe its traditions.",
      system:
        "You are a professional writer. You write simple, clear, and concise content.",
    });
    
    for await (const textPart of result.textStream) {
      console.log(textPart);
    }
    
    console.log(await result.usage);
    console.log(await result.finishReason);
    
    
    copy

### Conversations

To create a longer chat-like conversation you have to add each response
message and each of the user's messages to every request. This way the model
will have the context and will be able to provide better answers. You can
tweak it even further by providing a system message.

    
    
    import { createDeepInfra } from "@ai-sdk/deepinfra";
    import { generateText } from "ai";
    
    const deepinfra = createDeepInfra({
      apiKey: "$DEEPINFRA_TOKEN",
    });
    
    const { text, usage, finishReason } = await generateText({
      model: deepinfra("meta-llama/Llama-3.3-70B-Instruct-Turbo"),
      messages: [
        { role: "system", content: "Respond like a michelin starred chef." },
        {
          role: "user",
          content: "Can you name at least two different techniques to cook lamb?",
        },
        {
          role: "assistant",
          content:
            'Bonjour! Let me tell you, my friend, cooking lamb is an art form, and I\'m more than happy to share with you not two, but three of my favorite techniques to coax out the rich, unctuous flavors and tender textures of this majestic protein. First, we have the classic "Sous Vide" method. Next, we have the ancient art of "Sous le Sable". And finally, we have the more modern technique of "Hot Smoking."',
        },
        { role: "user", content: "Tell me more about the second method." },
      ],
    });
    
    console.log(text);
    console.log(usage);
    console.log(finishReason);
    
    
    copy

### Conversations & Streaming

Of course a conversation response can also be streaming and it is very simple.

    
    
    import { createDeepInfra } from "@ai-sdk/deepinfra";
    import { streamText } from "ai";
    
    const deepinfra = createDeepInfra({
      apiKey: "$DEEPINFRA_TOKEN",
    });
    
    const result = streamText({
      model: deepinfra("meta-llama/Llama-3.3-70B-Instruct-Turbo"),
      messages: [
        { role: "system", content: "Respond like a michelin starred chef." },
        {
          role: "user",
          content: "Can you name at least two different techniques to cook lamb?",
        },
        {
          role: "assistant",
          content:
            'Bonjour! Let me tell you, my friend, cooking lamb is an art form, and I\'m more than happy to share with you not two, but three of my favorite techniques to coax out the rich, unctuous flavors and tender textures of this majestic protein. First, we have the classic "Sous Vide" method. Next, we have the ancient art of "Sous le Sable". And finally, we have the more modern technique of "Hot Smoking."',
        },
        { role: "user", content: "Tell me more about the second method." },
      ],
    });
    
    for await (const textPart of result.textStream) {
      console.log(textPart);
    }
    
    console.log(await result.usage);
    console.log(await result.finishReason);
    
    
    copy

## Generating structured data

Getting text, streaming or not, is amazing but when two systems work together
a structured approach is even better.

    
    
    import { createDeepInfra } from "@ai-sdk/deepinfra";
    import { generateObject } from "ai";
    import { z } from "zod";
    
    const deepinfra = createDeepInfra({
      apiKey: "$DEEPINFRA_TOKEN",
    });
    
    const { object, usage, finishReason } = await generateObject({
      model: deepinfra("meta-llama/Llama-3.3-70B-Instruct-Turbo"),
      schema: z.object({
        recipe: z.object({
          name: z.string(),
          ingredients: z.array(z.object({ name: z.string(), amount: z.string() })),
          steps: z.array(z.string()),
        }),
      }),
      prompt: "Generate a lasagna recipe.",
    });
    
    console.log(object.recipe.name);
    console.log(object.recipe.ingredients);
    console.log(object.recipe.steps);
    console.log(usage);
    console.log(finishReason);
    
    
    copy

You can ask for more specific things like enums, too.

    
    
    import { createDeepInfra } from "@ai-sdk/deepinfra";
    import { generateObject } from "ai";
    import { z } from "zod";
    
    const deepinfra = createDeepInfra({
      apiKey: "$DEEPINFRA_TOKEN",
    });
    
    const { object, usage, finishReason } = await generateObject({
      model: deepinfra("meta-llama/Llama-3.3-70B-Instruct-Turbo"),
      output: "enum",
      enum: ["action", "comedy", "drama", "horror", "sci-fi"],
      prompt:
        "Classify the genre of this movie plot: " +
        '"A group of astronauts travel through a wormhole in search of a ' +
        'new habitable planet for humanity."',
    });
    
    console.log(object);
    console.log(usage);
    console.log(finishReason);
    
    
    copy

## Tool / Function calling

Tool calling allows models to call external functions provided by the user,
and use the results to generate a comprehensive response to the user query.
They are very powerful.

    
    
    import { createDeepInfra } from "@ai-sdk/deepinfra";
    import { generateText, tool } from "ai";
    
    const deepinfra = createDeepInfra({
      apiKey: "$DEEPINFRA_TOKEN",
    });
    
    const result = await generateText({
      model: deepinfra("meta-llama/Llama-3.3-70B-Instruct-Turbo"),
      tools: {
        weather: tool({
          description: "Get the weather in a location",
          parameters: z.object({
            location: z.string().describe("The location to get the weather for"),
          }),
          execute: async ({ location }) => ({
            location,
            temperature: 72 + Math.floor(Math.random() * 21) - 10,
          }),
        }),
      },
      prompt: "What is the weather in San Francisco?",
      maxSteps: 2, // without it a text response is not generated, only the tool response
    });
    
    console.log(result.text);
    console.log(result.usage);
    console.log(result.finishReason);
    
    
    copy

## Conversations and tool calling

Let's see how tool calling works when you are having a conversation

    
    
    import { createDeepInfra } from "@ai-sdk/deepinfra";
    import { generateText, tool } from "ai";
    
    const deepinfra = createDeepInfra({
      apiKey: "$DEEPINFRA_TOKEN",
    });
    
    const messages = [
      { role: "user", content: "What is the weather in San Francisco?" },
    ];
    
    const first_result = await generateText({
      model: deepinfra("meta-llama/Llama-3.3-70B-Instruct-Turbo"),
      tools: {
        weather: tool({
          description: "Get the weather in a location",
          parameters: z.object({
            location: z.string().describe("The location to get the weather for"),
          }),
          execute: async ({ location }) => ({
            location,
            temperature: 72 + Math.floor(Math.random() * 21) - 10,
          }),
        }),
      },
      messages: messages,
      maxSteps: 2, // without it a text response is not generated, only the tool response
    });
    
    console.log(first_result.text);
    
    // Let's continue our conversation
    messages.push(...result.response.messages);
    messages.push({
      role: "user",
      content: "Is this normal temperature for the summer?",
    });
    
    const second_result = await generateText({
      model: deepinfra("meta-llama/Llama-3.3-70B-Instruct-Turbo"),
      tools: {
        weather: tool({
          description: "Get the weather in a location",
          parameters: z.object({
            location: z.string().describe("The location to get the weather for"),
          }),
          execute: async ({ location }) => ({
            location,
            temperature: 72 + Math.floor(Math.random() * 21) - 10,
          }),
        }),
      },
      messages: messages,
      maxSteps: 2,
    });
    
    console.log(second_result.text);
    
    
    copy

[LlamaIndex](/docs/advanced/llama-index)[AutoGen](/docs/advanced/autogen)

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
ai/DeepSeek-V3.1](/deepseek-ai/DeepSeek-V3.1)[zai-org/GLM-4.6](/zai-
org/GLM-4.6)[anthropic/claude-3-7-sonnet-latest](/anthropic/claude-3-7-sonnet-
latest)[moonshotai/Kimi-K2-Instruct-0905](/moonshotai/Kimi-K2-Instruct-0905)

Featured Models

[deepseek-ai/DeepSeek-V3.1](/deepseek-
ai/DeepSeek-V3.1)[Qwen/Qwen3-235B-A22B-Thinking-2507](/Qwen/Qwen3-235B-A22B-Thinking-2507)[sesame/csm-1b](/sesame/csm-1b)[deepseek-
ai/DeepSeek-V3-0324](/deepseek-ai/DeepSeek-V3-0324)[deepseek-
ai/DeepSeek-V3](/deepseek-ai/DeepSeek-V3)

![Built With Love in Palo Alto](/_next/static/media/love.ce60156e.svg)

[](https://linkedin.com/company/deep-
infra)[](https://x.com/DeepInfra)[](https://github.com/DeepInfra)[](https://discord.gg/x88dCvhqYq)

© 2026 Deep Infra. All rights reserved.

[Privacy Policy](/privacy)[Terms of Service](/terms)

