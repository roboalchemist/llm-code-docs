# Source: https://docs.together.ai/docs/serverless-models.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Serverless Models

<Columns cols={4}>
  <Card title="Chat" icon="message-circle" href="#chat-models" horizontal />

  <Card title="Image" icon="photo" href="#image-models" horizontal />

  <Card title="Vision" icon="eye" href="#vision-models" horizontal />

  <Card title="Video" icon="video" href="#video-models" horizontal />

  <Card title="Audio" icon="volume" href="#audio-models" horizontal />

  <Card title="Embedding" icon="vector-bezier-2" href="#embedding-models" horizontal />

  <Card title="Rerank" icon="arrows-sort" href="#rerank-models" horizontal />

  <Card title="Moderation" icon="shield-check" href="#moderation-models" horizontal />
</Columns>

## Chat models

If you're not sure which chat model to use, check out our [recommended models](/docs/recommended-models) doc for which models to use for what use cases.

<Note>
  **Cached input token pricing now available for MiniMax M2.5** — Cached input tokens are billed at just **\$0.06 per 1M tokens**, an 80% discount from the standard input price. This applies automatically for cached tokens.
</Note>

| Organization | Model Name                       | API Model String                                  | Context length | Input pricing (per 1M tokens) | Cached input pricing (per 1M tokens) | Output pricing (per 1M tokens) | Quantization | Function Calling | Structured Outputs |
| :----------- | :------------------------------- | :------------------------------------------------ | :------------- | :---------------------------- | :----------------------------------- | :----------------------------- | :----------- | :--------------- | :----------------- |
| Minimax      | Minimax M2.5                     | MiniMaxAI/MiniMax-M2.5                            | 228700         | \$0.30                        | \$0.06                               | \$1.20                         | FP4          | Yes              | Yes                |
| Qwen         | Qwen3.5 397B A17B                | Qwen/Qwen3.5-397B-A17B                            | 262144         | \$0.60                        | -                                    | \$3.60                         | BF16         | Yes              | Yes                |
| Qwen         | Qwen3.5 9B                       | Qwen/Qwen3.5-9B                                   | 262144         | \$0.10                        | -                                    | \$0.15                         | FP8          | Yes              | Yes                |
| Moonshot     | Kimi K2.5                        | moonshotai/Kimi-K2.5                              | 262144         | \$0.50                        | -                                    | \$2.80                         | INT4         | Yes              | Yes                |
| Z.ai         | GLM-5                            | zai-org/GLM-5                                     | 202752         | \$1.00                        | -                                    | \$3.20                         | FP4          | Yes              | Yes                |
| OpenAI       | GPT-OSS 120B                     | openai/gpt-oss-120b                               | 128000         | \$0.15                        | -                                    | \$0.60                         | MXFP4        | Yes              | Yes                |
| OpenAI       | GPT-OSS 20B                      | openai/gpt-oss-20b                                | 128000         | \$0.05                        | -                                    | \$0.20                         | MXFP4        | Yes              | Yes                |
| DeepSeek     | DeepSeek-V3.1                    | deepseek-ai/DeepSeek-V3.1                         | 128000         | \$0.60                        | -                                    | \$1.70                         | FP8          | Yes              | Yes                |
| Z.ai         | GLM 4.7                          | zai-org/GLM-4.7                                   | 202752         | \$0.45                        | -                                    | \$2.00                         | FP8          | Yes              | Yes                |
| Z.ai         | GLM 4.5 Air                      | zai-org/GLM-4.5-Air-FP8                           | 131072         | \$0.20                        | -                                    | \$1.10                         | FP8          | Yes              | Yes                |
| Qwen         | Qwen3-Coder-Next                 | Qwen/Qwen3-Coder-Next-FP8                         | 262144         | \$0.50                        | -                                    | \$1.20                         | FP8          | Yes              | Yes                |
| Qwen         | Qwen3-Next-80B-A3B-Instruct      | Qwen/Qwen3-Next-80B-A3B-Instruct                  | 262144         | \$0.15                        | -                                    | \$1.50                         | BF16         | Yes              | Yes                |
| Qwen         | Qwen3 235B-A22B Thinking 2507    | Qwen/Qwen3-235B-A22B-Thinking-2507                | 262144         | \$0.65                        | -                                    | \$3.00                         | FP8          | Yes              | Yes                |
| Qwen         | Qwen3-Coder 480B-A35B Instruct   | Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8           | 256000         | \$2.00                        | -                                    | \$2.00                         | FP8          | Yes              | Yes                |
| Qwen         | Qwen3 235B-A22B Instruct 2507    | Qwen/Qwen3-235B-A22B-Instruct-2507-tput           | 262144         | \$0.20                        | -                                    | \$0.60                         | FP8          | Yes              | Yes                |
| DeepSeek     | DeepSeek-R1-0528                 | deepseek-ai/DeepSeek-R1                           | 163839         | \$3.00                        | -                                    | \$7.00                         | FP8          | Yes              | Yes                |
| Meta         | Llama 4 Maverick<br />(17Bx128E) | meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 | 1048576        | \$0.27                        | -                                    | \$0.85                         | FP8          | Yes              | Yes                |
| Meta         | Llama 3.3 70B Instruct Turbo     | meta-llama/Llama-3.3-70B-Instruct-Turbo           | 131072         | \$0.88                        | -                                    | \$0.88                         | FP8          | Yes              | Yes                |
| Deep Cogito  | Cogito v2.1 671B                 | deepcogito/cogito-v2-1-671b                       | 32768          | \$1.25                        | -                                    | \$1.25                         | FP8          | -                | Yes                |
| Essential AI | Rnj-1 Instruct                   | essentialai/rnj-1-instruct                        | 32768          | \$0.15                        | -                                    | \$0.15                         | BF16         | Yes              | Yes                |
| Mistral AI   | Mistral Small 3 Instruct (24B)   | mistralai/Mistral-Small-24B-Instruct-2501         | 32768          | \$0.10                        | -                                    | \$0.30                         | FP16         | Yes              | Yes                |
| Meta         | Llama 3.1 8B Instruct Turbo      | meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo       | 131072         | \$0.18                        | -                                    | \$0.18                         | FP8          | Yes              | Yes                |
| Qwen         | Qwen 2.5 7B Instruct Turbo       | Qwen/Qwen2.5-7B-Instruct-Turbo                    | 32768          | \$0.30                        | -                                    | \$0.30                         | FP8          | Yes              | Yes                |
| Arcee        | Arcee AI Trinity Mini            | arcee-ai/trinity-mini                             | 32768          | \$0.045                       | -                                    | \$0.15                         | -            | Yes              | Yes                |
| Meta         | Llama 3 8B Instruct Lite         | meta-llama/Meta-Llama-3-8B-Instruct-Lite          | 8192           | \$0.10                        | -                                    | \$0.10                         | INT4         | -                | Yes                |
| Google       | Gemma Instruct (2B)              | google/gemma-2b-it\*                              | 8192           | \$0.00                        | -                                    | \$0.00                         | FP16         | -                | -                  |
| Google       | Gemma 3N E4B Instruct            | google/gemma-3n-E4B-it                            | 32768          | \$0.02                        | -                                    | \$0.04                         | FP8          | -                | Yes                |
| Mistral AI   | Mistral (7B) Instruct v0.2       | mistralai/Mistral-7B-Instruct-v0.2                | 32768          | \$0.20                        | -                                    | \$0.20                         | FP16         | Yes              | Yes                |

\*Deprecated model, see [Deprecations](/docs/deprecations) for more details.

**Chat Model Examples**

* [PDF to Chat App](https://www.pdftochat.com/) - Chat with your PDFs (blogs, textbooks, papers)
* [Open Deep Research Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/Together_Open_Deep_Research_CookBook.ipynb) - Generate long form reports using a single prompt
* [RAG with Reasoning Models Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/RAG_with_Reasoning_Models.ipynb) - RAG with DeepSeek-R1
* [Fine-tuning Chat Models Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Finetuning/Finetuning_Guide.ipynb) - Tune Language models for conversation
* [Building Agents](https://github.com/togethercomputer/together-cookbook/tree/main/Agents) - Agent workflows with language models

## Image models

Use our [Images](/reference/post-images-generations) endpoint for Image Models.

| Organization      | Model Name                         | Model String for API                     | Price per MP | Default steps |
| :---------------- | :--------------------------------- | :--------------------------------------- | :----------- | :------------ |
| Google            | Imagen 4.0 Preview                 | google/imagen-4.0-preview                | \$0.04       | -             |
| Google            | Imagen 4.0 Fast                    | google/imagen-4.0-fast                   | \$0.02       | -             |
| Google            | Imagen 4.0 Ultra                   | google/imagen-4.0-ultra                  | \$0.06       | -             |
| Google            | Flash Image 2.5 (Nano Banana)      | google/flash-image-2.5                   | \$0.039      | -             |
| Google            | Gemini 3 Pro Image (Nano Banana 2) | google/gemini-3-pro-image                | -            | -             |
| Black Forest Labs | Flux.1 \[schnell] (Turbo)          | black-forest-labs/FLUX.1-schnell         | \$0.0027     | 4             |
| Black Forest Labs | Flux1.1 \[pro]                     | black-forest-labs/FLUX.1.1-pro           | \$0.04       | -             |
| Black Forest Labs | Flux.1 Kontext \[pro]              | black-forest-labs/FLUX.1-kontext-pro     | \$0.04       | 28            |
| Black Forest Labs | Flux.1 Kontext \[max]              | black-forest-labs/FLUX.1-kontext-max     | \$0.08       | 28            |
| Black Forest Labs | FLUX.1 Krea \[dev]                 | black-forest-labs/FLUX.1-krea-dev        | \$0.025      | 28            |
| Black Forest Labs | FLUX.2 \[pro]                      | black-forest-labs/FLUX.2-pro             | -            | -             |
| Black Forest Labs | FLUX.2 \[dev]                      | black-forest-labs/FLUX.2-dev             | -            | -             |
| Black Forest Labs | FLUX.2 \[flex]                     | black-forest-labs/FLUX.2-flex            | -            | -             |
| ByteDance         | Seedream 3.0                       | ByteDance-Seed/Seedream-3.0              | \$0.018      | -             |
| ByteDance         | Seedream 4.0                       | ByteDance-Seed/Seedream-4.0              | \$0.03       | -             |
| Qwen              | Qwen Image                         | Qwen/Qwen-Image                          | \$0.0058     | -             |
| RunDiffusion      | Juggernaut Pro Flux                | RunDiffusion/Juggernaut-pro-flux         | \$0.0049     | -             |
| RunDiffusion      | Juggernaut Lightning Flux          | Rundiffusion/Juggernaut-Lightning-Flux   | \$0.0017     | -             |
| HiDream           | HiDream-I1-Full                    | HiDream-ai/HiDream-I1-Full               | \$0.009      | -             |
| HiDream           | HiDream-I1-Dev                     | HiDream-ai/HiDream-I1-Dev                | \$0.0045     | -             |
| HiDream           | HiDream-I1-Fast                    | HiDream-ai/HiDream-I1-Fast               | \$0.0032     | -             |
| Ideogram          | Ideogram 3.0                       | ideogram/ideogram-3.0                    | \$0.06       | -             |
| Lykon             | Dreamshaper                        | Lykon/DreamShaper                        | \$0.0006     | -             |
| Stability AI      | Stable Diffusion 3                 | stabilityai/stable-diffusion-3-medium    | \$0.0019     | -             |
| Stability AI      | SD XL                              | stabilityai/stable-diffusion-xl-base-1.0 | \$0.0019     | -             |

Note: Image models can only be used with credits. Users are unable to call Image models with a zero or negative balance.

**Image Model Examples**

* [Blinkshot.io](https://www.blinkshot.io/) - A realtime AI image playground built with Flux Schnell
* [Logo Creator](https://www.logo-creator.io/) - An logo generator that creates professional logos in seconds using Flux Pro 1.1
* [PicMenu](https://www.picmenu.co/) - A menu visualizer that takes a restaurant menu and generates nice images for each dish.
* [Flux LoRA Inference Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Flux_LoRA_Inference.ipynb) - Using LoRA fine-tuned image generations models

**How FLUX pricing works** For FLUX models (except for pro) pricing is based on the size of generated images (in megapixels) and the number of steps used (if the number of steps exceed the default steps).

* **Default pricing:** The listed per megapixel prices are for the default number of steps.
* **Using more or fewer steps:** Costs are adjusted based on the number of steps used **only if you go above the default steps**. If you use more steps, the cost increases proportionally using the formula below. If you use fewer steps, the cost *does not* decrease and is based on the default rate.

Here’s a formula to calculate cost:

Cost = MP × Price per MP × (Steps ÷ Default Steps)

Where:

* MP = (Width × Height ÷ 1,000,000)
* Price per MP = Cost for generating one megapixel at the default steps
* Steps = The number of steps used for the image generation. This is only factored in if going above default steps.

**How Pricing works for Gemini 3 Pro Image**
Gemini 3 Pro Image offers pricing based on the resolution of the image.

* 1080p and 2K: \$0.134/image
* 4K resolution: \$0.24 /image

Supported dimensions:
1K: 1024×1024 (1:1), 1248×832 (3:2), 832×1248 (2:3), 1184×864 (4:3), 864×1184 (3:4), 896×1152 (4:5), 1152×896 (5:4), 768×1344 (9:16), 1344×768 (16:9), 1536×672 (21:9).

2K: 2048×2048 (1:1), 2496×1664 (3:2), 1664×2496 (2:3), 2368×1728 (4:3), 1728×2368 (3:4), 1792×2304 (4:5), 2304×1792 (5:4), 1536×2688 (9:16), 2688×1536 (16:9), 3072×1344 (21:9).

4K: 4096×4096 (1:1), 4992×3328 (3:2), 3328×4992 (2:3), 4736×3456 (4:3), 3456×4736 (3:4), 3584×4608 (4:5), 4608×3584 (5:4), 3072×5376 (9:16), 5376×3072 (16:9), 6144×2688 (21:9).

## Vision models

If you're not sure which vision model to use, we currently recommend **Llama 4 Maverick** (`meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8`) to get started. For model specific rate limits, navigate [here](/docs/rate-limits).

| Organization | Model Name                       | API Model String                                  | Context length | Input pricing (per 1M tokens) | Output pricing (per 1M tokens) |
| :----------- | :------------------------------- | :------------------------------------------------ | :------------- | :---------------------------- | :----------------------------- |
| Meta         | Llama 4 Maverick<br />(17Bx128E) | meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 | 1048576        | \$0.27                        | \$0.85                         |
| Qwen         | Qwen3.5 397B A17B                | Qwen/Qwen3.5-397B-A17B                            | 262144         | \$0.60                        | \$3.60                         |
| Qwen         | Qwen3-VL-32B-Instruct            | Qwen/Qwen3-VL-32B-Instruct                        | 262144         | \$0.50                        | \$1.50                         |
| Qwen         | Qwen2.5-VL 72B Instruct          | Qwen/Qwen2.5-VL-72B-Instruct                      | 262144         | \$1.95                        | \$8.00                         |
| Qwen         | Qwen3-VL-8B-Instruct             | Qwen/Qwen3-VL-8B-Instruct                         | 262144         | \$0.18                        | \$0.68                         |
| Moonshot     | Kimi K2.5                        | moonshotai/Kimi-K2.5                              | 262144         | \$0.50                        | \$2.80                         |

**Vision Model Examples**

* [LlamaOCR](https://llamaocr.com/) - A tool that takes documents (like receipts) and outputs markdown
* [Wireframe to Code](https://www.napkins.dev/) - A wireframe to app tool that takes in a UI mockup of a site and give you React code.
* [Extracting Structured Data from Images](https://github.com/togethercomputer/together-cookbook/blob/main/Structured_Text_Extraction_from_Images.ipynb) - Extract information from images as JSON

## Video models

| Organization | Model Name           | Model String for API        | Price per video | Resolution / Duration |
| :----------- | :------------------- | :-------------------------- | :-------------- | :-------------------- |
| MiniMax      | MiniMax 01 Director  | minimax/video-01-director   | \$0.28          | 720p / 5s             |
| MiniMax      | MiniMax Hailuo 02    | minimax/hailuo-02           | \$0.49          | 768p / 10s            |
| Google       | Veo 2.0              | google/veo-2.0              | \$2.50          | 720p / 5s             |
| Google       | Veo 3.0              | google/veo-3.0              | \$1.60          | 720p / 8s             |
| Google       | Veo 3.0 + Audio      | google/veo-3.0-audio        | \$3.20          | 720p / 8s             |
| Google       | Veo 3.0 Fast         | google/veo-3.0-fast         | \$0.80          | 1080p / 8s            |
| Google       | Veo 3.0 Fast + Audio | google/veo-3.0-fast-audio   | \$1.20          | 1080p / 8s            |
| ByteDance    | Seedance 1.0 Lite    | ByteDance/Seedance-1.0-lite | \$0.14          | 720p / 5s             |
| ByteDance    | Seedance 1.0 Pro     | ByteDance/Seedance-1.0-pro  | \$0.57          | 1080p / 5s            |
| PixVerse     | PixVerse v5          | pixverse/pixverse-v5        | \$0.30          | 1080p / 5s            |
| Kuaishou     | Kling 2.1 Master     | kwaivgI/kling-2.1-master    | \$0.92          | 1080p / 5s            |
| Kuaishou     | Kling 2.1 Standard   | kwaivgI/kling-2.1-standard  | \$0.18          | 720p / 5s             |
| Kuaishou     | Kling 2.1 Pro        | kwaivgI/kling-2.1-pro       | \$0.32          | 1080p / 5s            |
| Kuaishou     | Kling 2.0 Master     | kwaivgI/kling-2.0-master    | \$0.92          | 1080p / 5s            |
| Kuaishou     | Kling 1.6 Standard   | kwaivgI/kling-1.6-standard  | \$0.19          | 720p / 5s             |
| Kuaishou     | Kling 1.6 Pro        | kwaivgI/kling-1.6-pro       | \$0.32          | 1080p / 5s            |
| Wan-AI       | Wan 2.2 I2V          | Wan-AI/Wan2.2-I2V-A14B      | \$0.31          | -                     |
| Wan-AI       | Wan 2.2 T2V          | Wan-AI/Wan2.2-T2V-A14B      | \$0.66          | -                     |
| Vidu         | Vidu 2.0             | vidu/vidu-2.0               | \$0.28          | 720p / 8s             |
| Vidu         | Vidu Q1              | vidu/vidu-q1                | \$0.22          | 1080p / 5s            |
| OpenAI       | Sora 2               | openai/sora-2               | \$0.80          | 720p / 8s             |
| OpenAI       | Sora 2 Pro           | openai/sora-2-pro           | \$2.40          | 1080p / 8s            |

## Audio models

Use our [Audio](/reference/audio-speech) endpoint for text-to-speech models. For speech-to-text models see [Transcription](/reference/audio-transcriptions) and [Translations](/reference/audio-translations)

| Organization | Modality       | Model Name       | Model String for API           | Pricing                     |
| :----------- | :------------- | :--------------- | :----------------------------- | :-------------------------- |
| Canopy Labs  | Text-to-Speech | Orpheus 3B       | canopylabs/orpheus-3b-0.1-ft   | $0.27 / $0.85 per 1M tokens |
| Kokoro       | Text-to-Speech | Kokoro           | hexgrad/Kokoro-82M             | $0.27 / $0.85 per 1M tokens |
| Cartesia     | Text-to-Speech | Cartesia Sonic 2 | cartesia/sonic-2               | \$65.00 per 1M chars        |
| Cartesia     | Text-to-Speech | Cartesia Sonic   | cartesia/sonic                 | \$65.00 per 1M chars        |
| OpenAI       | Speech-to-Text | Whisper Large v3 | openai/whisper-large-v3        | \$0.27 per audio min        |
| Mistral AI   | Speech-to-Text | Voxtral Mini 3B  | mistralai/Voxtral-Mini-3B-2507 | -                           |

**Audio Model Examples**

* [PDF to Podcast Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/PDF_to_Podcast.ipynb) - Generate a NotebookLM style podcast given a PDF
* [Audio Podcast Agent Workflow](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/Serial_Chain_Agent_Workflow.ipynb) - Agent workflow to generate audio files given input content

## Embedding models

| Model Name                     | Model String for API                    | Model Size | Embedding Dimension | Context Window | Pricing (per 1M tokens) |
| :----------------------------- | --------------------------------------- | :--------- | :------------------ | :------------- | :---------------------- |
| Multilingual-e5-large-instruct | intfloat/multilingual-e5-large-instruct | 560M       | 1024                | 514            | \$0.02                  |

**Embedding Model Examples**

* [Contextual RAG](https://docs.together.ai/docs/how-to-implement-contextual-rag-from-anthropic) - An open source implementation of contextual RAG by Anthropic
* [Code Generation Agent](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/Looping_Agent_Workflow.ipynb) - An agent workflow to generate and iteratively improve code
* [Multimodal Search and Image Generation](https://github.com/togethercomputer/together-cookbook/blob/main/Multimodal_Search_and_Conditional_Image_Generation.ipynb) - Search for images and generate more similar ones
* [Visualizing Embeddings](https://github.com/togethercomputer/together-cookbook/blob/main/Embedding_Visualization.ipynb) - Visualizing and clustering vector embeddings

## Rerank models

Our [Rerank API](/docs/rerank-overview) has built-in support for reranker model.

<Tip>
  There are currently no rerank models offered via serverless. Rerank models like `mixedbread-ai/mxbai-rerank-large-v2` are only available as [Dedicated Endpoints](https://api.together.ai/endpoints/configure). You can bring up a dedicated endpoint to use reranking in your applications.
</Tip>

**Rerank Model Examples**

* [Search and Reranking](https://github.com/togethercomputer/together-cookbook/blob/main/Search_with_Reranking.ipynb) - Simple semantic search pipeline improved using a reranker
* [Implementing Hybrid Search Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Open_Contextual_RAG.ipynb) - Implementing semantic + lexical search along with reranking

## Moderation models

Use our [Completions](/reference/completions-1) endpoint to run a moderation model as a standalone classifier, or use it alongside any of the other models above as a filter to safeguard responses from 100+ models, by specifying the parameter `"safety_model": "MODEL_API_STRING"`

| Organization | Model Name          | Model String for API           | Context length | Pricing (per 1M tokens) |
| :----------- | :------------------ | :----------------------------- | :------------- | :---------------------- |
| Meta         | Llama Guard 4 (12B) | meta-llama/Llama-Guard-4-12B   | 1048576        | \$0.20                  |
| Virtue AI    | Virtue Guard        | VirtueAI/VirtueGuard-Text-Lite | 32768          | \$0.20                  |


Built with [Mintlify](https://mintlify.com).