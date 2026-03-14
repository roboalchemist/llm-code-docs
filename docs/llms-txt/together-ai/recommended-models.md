# Source: https://docs.together.ai/docs/recommended-models.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Recommended Models

> Find the right models for your use case

We host 100+ open-source models on our serverless inference platform and even more on dedicated endpoints. This guide helps you choose the right model for your specific use case.

For a complete list of all available models with detailed specifications, visit our [Serverless](/docs/serverless-models) and [Dedicated](/docs/dedicated-models) Models pages.

## Recommended Models by Use Case

| Use Case                   | Recommended Model             | Model String                              | Alternatives                                                                        | Learn More                                                                           |
| :------------------------- | :---------------------------- | :---------------------------------------- | :---------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------- |
| **Chat**                   | Kimi K2.5 (instant mode)      | `moonshotai/Kimi-K2.5`                    | `deepseek-ai/DeepSeek-V3.1`, `openai/gpt-oss-120b`                                  | [Chat](/docs/chat-overview)                                                          |
| **Reasoning**              | Kimi K2.5 (reasoning mode)    | `moonshotai/Kimi-K2.5`                    | `deepseek-ai/DeepSeek-R1`, `Qwen/Qwen3-235B-A22B-Thinking-2507`                     | [Reasoning Guide](/docs/reasoning-models-guide), [DeepSeek R1](/docs/deepseek-r1)    |
| **Coding Agents**          | Kimi K2.5 (reasoning mode)    | `moonshotai/Kimi-K2.5`                    | `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8`, `deepseek-ai/DeepSeek-V3.1`              | [Building Agents](/docs/how-to-build-coding-agents)                                  |
| **Small & Fast**           | GPT-OSS 20B                   | `openai/gpt-oss-20b`                      | `Qwen/Qwen2.5-7B-Instruct-Turbo`, `meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo`     | -                                                                                    |
| **Medium General Purpose** | GPT-OSS 120B                  | `openai/gpt-oss-120b`                     | `zai-org/GLM-4.5-Air-FP8`, `Qwen/Qwen3-Next-80B-A3B-Instruct`                       | -                                                                                    |
| **Function Calling**       | GLM-5                         | `zai-org/GLM-5`                           | `moonshotai/Kimi-K2.5`, `moonshotai/Kimi-K2-Instruct-0905`                          | [Function Calling](/docs/function-calling)                                           |
| **Vision**                 | Kimi K2.5                     | `moonshotai/Kimi-K2.5`                    | `meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8`, `Qwen/Qwen3-VL-8B-Instruct`    | [Vision](/docs/vision-overview), [OCR](/docs/quickstart-how-to-do-ocr)               |
| **Image Generation**       | Flash Image 2.5 (Nano Banana) | `google/flash-image-2.5`                  | `black-forest-labs/FLUX.2-pro`, `ByteDance-Seed/Seedream-4.0`                       | [Images](/docs/images-overview)                                                      |
| **Image-to-Image**         | Flash Image 2.5 (Nano Banana) | `google/flash-image-2.5`                  | `black-forest-labs/FLUX.1-kontext-max`, `google/gemini-3-pro-image`                 | [Flux Kontext](/docs/quickstart-flux-kontext)                                        |
| **Text-to-Video**          | Sora 2                        | `openai/sora-2-pro`                       | `google/veo-3.0`, `ByteDance/Seedance-1.0-pro`                                      | [Video Generation](/docs/videos-overview)                                            |
| **Image-to-Video**         | Veo 3.0                       | `google/veo-3.0`                          | `ByteDance/Seedance-1.0-pro`, `kwaivgI/kling-2.1-master`                            | [Video Generation](/docs/videos-overview)                                            |
| **Text-to-Speech**         | Cartesia Sonic 3              | `cartesia/sonic-3`                        | `canopylabs/orpheus-3b-0.1-ft`, `hexgrad/Kokoro-82M`                                | [Text-to-Speech](/docs/text-to-speech)                                               |
| **Speech-to-Text**         | Whisper Large v3              | `openai/whisper-large-v3`                 | `mistralai/Voxtral-Mini-3B-2507`                                                    | [Speech-to-Text](/docs/speech-to-text)                                               |
| **Embeddings**             | Multilingual E5 Large         | `intfloat/multilingual-e5-large-instruct` | -                                                                                   | [Embeddings](/reference/embeddings-2)                                                |
| **Rerank**                 | MixedBread Rerank Large       | `mixedbread-ai/Mxbai-Rerank-Large-V2`     | Only available as [Dedicated Endpoint](https://api.together.ai/endpoints/configure) | [Rerank](/docs/rerank-overview), [Guide](/docs/how-to-improve-search-with-rerankers) |
| **Moderation**             | Virtue Guard                  | `VirtueAI/VirtueGuard-Text-Lite`          | `meta-llama/Llama-Guard-4-12B`                                                      | -                                                                                    |

***

**Need Help Choosing?**

* Check our [Serverless Models](/docs/serverless-models) page for complete specifications
* See our [WhichLLM](https://whichllm.together.ai/) page which provides categorical benchmarks for the above usecases
* Review [Rate Limits](/docs/rate-limits) for your tier
* See [Pricing](https://together.ai/pricing) for cost information
* Visit [Inference FAQs](/docs/inference-faqs) for common questions

For high-volume production workloads, consider [Dedicated Inference](/docs/dedicated-inference) for guaranteed capacity and predictable performance.


Built with [Mintlify](https://mintlify.com).