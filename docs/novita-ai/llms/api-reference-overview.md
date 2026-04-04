# Source: https://novita.ai/docs/api-reference/api-reference-overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# API Reference Overview

## Welcome to Novita AI API Reference

This documentation provides comprehensive reference for all Novita AI APIs. Our APIs are organized into several categories:

## Base URLs

All API requests should be made to:

```
https://api.novita.ai
```

**OpenAI-Compatible Endpoints:**

```
https://api.novita.ai/openai
```

## API Groups

### Basic APIs

Fundamental APIs for authentication, billing, and account management.

| Endpoint                                                                    | Description                   | File Path                                           |
| --------------------------------------------------------------------------- | ----------------------------- | --------------------------------------------------- |
| [Authentication](/api-reference/basic-authentication)                       | API key authentication        | `api-reference/basic-authentication.mdx`            |
| [Error Codes](/api-reference/basic-error-code)                              | Unified error response format | `api-reference/basic-error-code.mdx`                |
| [Get User Balance](/api-reference/basic-get-user-balance)                   | Query account balance         | `api-reference/basic-get-user-balance.mdx`          |
| [Query Monthly Bill](/api-reference/basic-query-monthly-bill)               | Query monthly billing         | `api-reference/basic-query-monthly-bill.mdx`        |
| [Query Usage-Based Billing](/api-reference/basic-query-usage-based-billing) | Query usage-based billing     | `api-reference/basic-query-usage-based-billing.mdx` |
| [Query Fixed-Term Billing](/api-reference/basic-query-fixed-term-billing)   | Query fixed-term billing      | `api-reference/basic-query-fixed-term-billing.mdx`  |

### Model APIs

#### LLM APIs

Large Language Model APIs with OpenAI compatibility.

| Endpoint                                                                       | Description              | File Path                                                 |
| ------------------------------------------------------------------------------ | ------------------------ | --------------------------------------------------------- |
| [Create Chat Completion](/api-reference/model-apis-llm-create-chat-completion) | Create a chat completion | `api-reference/model-apis-llm-create-chat-completion.mdx` |
| [Create Completion](/api-reference/model-apis-llm-create-completion)           | Create a completion      | `api-reference/model-apis-llm-create-completion.mdx`      |
| [Create Embeddings](/api-reference/model-apis-llm-create-embeddings)           | Create embeddings        | `api-reference/model-apis-llm-create-embeddings.mdx`      |
| [Create Rerank](/api-reference/model-apis-llm-create-rerank)                   | Rerank search results    | `api-reference/model-apis-llm-create-rerank.mdx`          |
| [List Models](/api-reference/model-apis-llm-list-models)                       | List available models    | `api-reference/model-apis-llm-list-models.mdx`            |
| [Retrieve Model](/api-reference/model-apis-llm-retrieve-model)                 | Get model details        | `api-reference/model-apis-llm-retrieve-model.mdx`         |

**Batch Operations:**

| Endpoint                                                                         | Description           | File Path                                                  |
| -------------------------------------------------------------------------------- | --------------------- | ---------------------------------------------------------- |
| [Create Batch](/api-reference/model-apis-llm-create-batch)                       | Create a batch job    | `api-reference/model-apis-llm-create-batch.mdx`            |
| [Retrieve Batch](/api-reference/model-apis-llm-retrieve-batch)                   | Get batch job status  | `api-reference/model-apis-llm-retrieve-batch.mdx`          |
| [Cancel Batch](/api-reference/model-apis-llm-cancel-batch)                       | Cancel a batch job    | `api-reference/model-apis-llm-cancel-batch.mdx`            |
| [List Batches](/api-reference/model-apis-llm-list-batches)                       | List all batch jobs   | `api-reference/model-apis-llm-list-batches.mdx`            |
| [Upload Batch Input File](/api-reference/model-apis-llm-upload-batch-input-file) | Upload file for batch | `api-reference/model-apis-llm-upload-batch-input-file.mdx` |
| [List Files](/api-reference/model-apis-llm-list-files)                           | List uploaded files   | `api-reference/model-apis-llm-list-files.mdx`              |
| [Query File](/api-reference/model-apis-llm-query-file)                           | Get file metadata     | `api-reference/model-apis-llm-query-file.mdx`              |
| [Delete File](/api-reference/model-apis-llm-delete-file)                         | Delete a file         | `api-reference/model-apis-llm-delete-file.mdx`             |
| [Retrieve File Content](/api-reference/model-apis-llm-retrieve-file-content)     | Get file content      | `api-reference/model-apis-llm-retrieve-file-content.mdx`   |

#### Image, Audio and Video APIs

Multimodal AI APIs for content generation and editing.

**Core Endpoints:**

| Endpoint                                             | Description            | File Path                                  |
| ---------------------------------------------------- | ---------------------- | ------------------------------------------ |
| [Webhook](/api-reference/model-apis-webhook)         | Webhook configuration  | `api-reference/model-apis-webhook.mdx`     |
| [Get Model](/api-reference/model-apis-get-model)     | Query available models | `api-reference/model-apis-get-model.mdx`   |
| [Task Result](/api-reference/model-apis-task-result) | Get async task results | `api-reference/model-apis-task-result.mdx` |

**Image Generation:**

| Endpoint                                                   | Description               | File Path                                         |
| ---------------------------------------------------------- | ------------------------- | ------------------------------------------------- |
| [Text to Image](/api-reference/model-apis-txt2img)         | Generate images from text | `api-reference/model-apis-txt2img.mdx`            |
| [Image to Image](/api-reference/model-apis-img2img)        | Transform existing images | `api-reference/model-apis-img2img.mdx`            |
| [Reimagine](/api-reference/model-apis-reimagine)           | Reimagine compositions    | `api-reference/model-apis-reimagine.mdx`          |
| [FLUX.1 Schnell](/api-reference/model-apis-flux-1-schnell) | Fast image generation     | `api-reference/model-apis-flux-1-schnell.mdx`     |
| [Seedream 3.0](/api-reference/model-apis-seedream-3-0-t2i) | High-quality generation   | `api-reference/model-apis-seedream-3-0-t2i.mdx`   |
| [Seedream 4.0](/api-reference/model-apis-seedream-4-0)     | Advanced generation       | `api-reference/model-apis-seedream-4-0.mdx`       |
| [Qwen Image](/api-reference/model-apis-qwen-image-txt2img) | Qwen image generation     | `api-reference/model-apis-qwen-image-txt2img.mdx` |

**Image Editing:**

| Endpoint                                                           | Description            | File Path                                         |
| ------------------------------------------------------------------ | ---------------------- | ------------------------------------------------- |
| [Upscale](/api-reference/model-apis-upscale)                       | Image upscaling        | `api-reference/model-apis-upscale.mdx`            |
| [Remove Background](/api-reference/model-apis-remove-background)   | Background removal     | `api-reference/model-apis-remove-background.mdx`  |
| [Replace Background](/api-reference/model-apis-replace-background) | Background replacement | `api-reference/model-apis-replace-background.mdx` |
| [Inpainting](/api-reference/model-apis-inpainting)                 | Image inpainting       | `api-reference/model-apis-inpainting.mdx`         |
| [Image to Prompt](/api-reference/model-apis-image-to-prompt)       | Reverse engineering    | `api-reference/model-apis-image-to-prompt.mdx`    |

**Video Generation:**

| Endpoint                                                             | Description               | File Path                                            |
| -------------------------------------------------------------------- | ------------------------- | ---------------------------------------------------- |
| [Text to Video](/api-reference/model-apis-txt2video)                 | Generate videos from text | `api-reference/model-apis-txt2video.mdx`             |
| [Image to Video](/api-reference/model-apis-img2video)                | Animate images            | `api-reference/model-apis-img2video.mdx`             |
| [Hunyuan Video Fast](/api-reference/model-apis-hunyuan-video-fast)   | Fast video generation     | `api-reference/model-apis-hunyuan-video-fast.mdx`    |
| [Wan 2.5 T2V Preview](/api-reference/model-apis-wan-2.5-t2v-preview) | Wan 2.5 preview           | `api-reference/model-apis-wan-2.5-t2v-preview.mdx`   |
| [Kling V2.1 Master](/api-reference/model-apis-kling-v2.1-t2v-master) | Kling V2.1 master         | `api-reference/model-apis-kling-v2.1-t2v-master.mdx` |
| [Minimax Hailuo 02](/api-reference/model-apis-minimax-hailuo-02)     | Minimax Hailuo            | `api-reference/model-apis-minimax-hailuo-02.mdx`     |
| [Vidu Q1](/api-reference/model-apis-vidu-q1-text2video)              | Vidu Q1 generation        | `api-reference/model-apis-vidu-q1-text2video.mdx`    |

**Audio:**

| Endpoint                                                              | Description            | File Path                                                |
| --------------------------------------------------------------------- | ---------------------- | -------------------------------------------------------- |
| [Minimax Speech 02](/api-reference/model-apis-minimax-speech-02-hd)   | Minimax TTS HD         | `api-reference/model-apis-minimax-speech-02-hd.mdx`      |
| [Minimax Speech 2.8](/api-reference/model-apis-minimax-speech-2.8-hd) | Minimax 2.8 HD         | `api-reference/model-apis-minimax-speech-2.8-hd.mdx`     |
| [Fish Audio TTS](/api-reference/model-apis-fish-audio-text-to-speech) | Fish Audio TTS         | `api-reference/model-apis-fish-audio-text-to-speech.mdx` |
| [GLM TTS](/api-reference/model-apis-glm-tts)                          | GLM text-to-speech     | `api-reference/model-apis-glm-tts.mdx`                   |
| [GLM ASR](/api-reference/model-apis-glm-asr)                          | GLM speech recognition | `api-reference/model-apis-glm-asr.mdx`                   |

### GPU APIs

GPU instance management and serverless GPU endpoints.

#### GPU Instance

| Endpoint                                                       | Description          | File Path                                        |
| -------------------------------------------------------------- | -------------------- | ------------------------------------------------ |
| [Create Instance](/api-reference/gpu-instance-create-instance) | Create GPU instance  | `api-reference/gpu-instance-create-instance.mdx` |
| [List Instances](/api-reference/gpu-instance-list-instances)   | List all instances   | `api-reference/gpu-instance-list-instances.mdx`  |
| [Get Instance](/api-reference/gpu-instance-get-instance)       | Get instance details | `api-reference/gpu-instance-get-instance.mdx`    |
| [Start Instance](/api-reference/gpu-instance-start-instance)   | Start instance       | `api-reference/gpu-instance-start-instance.mdx`  |
| [Stop Instance](/api-reference/gpu-instance-stop-instance)     | Stop instance        | `api-reference/gpu-instance-stop-instance.mdx`   |
| [Delete Instance](/api-reference/gpu-instance-delete-instance) | Delete instance      | `api-reference/gpu-instance-delete-instance.mdx` |

**Template Management:**

| Endpoint                                                       | Description          | File Path                                        |
| -------------------------------------------------------------- | -------------------- | ------------------------------------------------ |
| [Create Template](/api-reference/gpu-instance-create-template) | Create template      | `api-reference/gpu-instance-create-template.mdx` |
| [List Templates](/api-reference/gpu-instance-list-templates)   | List templates       | `api-reference/gpu-instance-list-templates.mdx`  |
| [Get Template](/api-reference/gpu-instance-get-template)       | Get template details | `api-reference/gpu-instance-get-template.mdx`    |

**Product & Pricing:**

| Endpoint                                                   | Description       | File Path                                      |
| ---------------------------------------------------------- | ----------------- | ---------------------------------------------- |
| [List Products](/api-reference/gpu-instance-list-products) | List GPU products | `api-reference/gpu-instance-list-products.mdx` |

#### Serverless GPUs

| Endpoint                                                     | Description          | File Path                                      |
| ------------------------------------------------------------ | -------------------- | ---------------------------------------------- |
| [Create Endpoint](/api-reference/serverless-create-endpoint) | Create endpoint      | `api-reference/serverless-create-endpoint.mdx` |
| [List Endpoint](/api-reference/serverless-list-endpoint)     | List endpoints       | `api-reference/serverless-list-endpoint.mdx`   |
| [Get Endpoint](/api-reference/serverless-get-endpoint)       | Get endpoint details | `api-reference/serverless-get-endpoint.mdx`    |
| [Update Endpoint](/api-reference/serverless-update-endpoint) | Update endpoint      | `api-reference/serverless-update-endpoint.mdx` |
| [Delete Endpoint](/api-reference/serverless-delete-endpoint) | Delete endpoint      | `api-reference/serverless-delete-endpoint.mdx` |

## Quick Start

### 1. Get Your API Key

Visit the [settings page](https://novita.ai/settings/key-management) to create and manage your API keys.

### 2. Make Your First Request

```bash  theme={"system"}
curl --location 'https://api.novita.ai/v1/models' \
  --header 'Authorization: Bearer {{API Key}}'
```

### 3. Explore SDKs

We provide official SDKs for popular languages:

* [Python SDK](/guides/model-apis-sdks#python)
* [JavaScript/TypeScript SDK](/guides/model-apis-sdks#javascripttypescript)

## Authentication

All API requests require authentication using Bearer tokens. Include your API key in the Authorization header:

```
Authorization: Bearer {{API Key}}
```

See [Authentication](/api-reference/basic-authentication) for details.

## Error Handling

Novita AI uses standard HTTP status codes and returns errors in a unified format. See [Error Codes](/api-reference/basic-error-code) for complete error reference.

## Common Use Cases

| User Query                   | Go To                                                                               |
| ---------------------------- | ----------------------------------------------------------------------------------- |
| "How to get started?"        | [Quick Start](#quick-start) + [Authentication](/api-reference/basic-authentication) |
| "API not working, error 401" | [Error Codes](/api-reference/basic-error-code)                                      |
| "Generate images from text"  | [Text to Image](/api-reference/model-apis-txt2img)                                  |
| "Create chatbot with LLM"    | [Chat Completion](/api-reference/model-apis-llm-create-chat-completion)             |
| "Generate videos"            | [Text to Video](/api-reference/model-apis-txt2video)                                |
| "Deploy GPU instance"        | [Create Instance](/api-reference/gpu-instance-create-instance)                      |
| "Check my balance"           | [Get User Balance](/api-reference/basic-get-user-balance)                           |
| "OpenAI compatible API"      | [LLM API Guide](/guides/llm-api)                                                    |

## Need Help?

* [Discord Community](https://discord.gg/YyPFAzwp7P)
* [Email Support](mailto:support@novita.ai)
* [Console](https://novita.ai/console)


Built with [Mintlify](https://mintlify.com).