# Source: https://docs.together.ai/docs/serverless-models.md

# Serverless Models

## Chat models

> In the table below, models marked as "Turbo" are quantized to FP8 and those marked as "Lite" are INT4. All our other models are at full precision (FP16).

If you're not sure which chat model to use, we currently recommend **Llama 3.3 70B Turbo** (`meta-llama/Llama-3.3-70B-Instruct-Turbo`) to get started.

| Organization    | Model Name                           | API Model String                                  | Context length | Quantization |
| :-------------- | :----------------------------------- | :------------------------------------------------ | :------------- | :----------- |
| Moonshot        | Kimi K2 Instruct 0905                | moonshotai/Kimi-K2-Instruct-0905                  | 262144         | FP8          |
| Moonshot        | Kimi K2 Thinking                     | moonshotai/Kimi-K2-Thinking                       | 262144         | INT4         |
| DeepSeek        | DeepSeek-V3.1                        | deepseek-ai/DeepSeek-V3.1                         | 128000         | FP8          |
| OpenAI          | GPT-OSS 120B                         | openai/gpt-oss-120b                               | 128000         | MXFP4        |
| OpenAI          | GPT-OSS 20B                          | openai/gpt-oss-20b                                | 128000         | MXFP4        |
| Moonshot        | Kimi K2 Instruct                     | moonshotai/Kimi-K2-Instruct                       | 128000         | FP8          |
| Z.ai            | GLM 4.6                              | zai-org/GLM-4.6                                   | 202752         | FP8          |
| Z.ai            | GLM 4.5 Air                          | zai-org/GLM-4.5-Air-FP8                           | 131072         | FP8          |
| Qwen            | Qwen3 235B-A22B Thinking 2507        | Qwen/Qwen3-235B-A22B-Thinking-2507                | 262144         | FP8          |
| Qwen            | Qwen3-Coder 480B-A35B Instruct       | Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8           | 256000         | FP8          |
| Qwen            | Qwen3 235B-A22B Instruct 2507        | Qwen/Qwen3-235B-A22B-Instruct-2507-tput           | 262144         | FP8          |
| Qwen            | Qwen3-Next-80B-A3B-Instruct          | Qwen/Qwen3-Next-80B-A3B-Instruct                  | 262144         | BF16         |
| Qwen            | Qwen3-Next-80B-A3B-Thinking          | Qwen/Qwen3-Next-80B-A3B-Thinking                  | 262144         | BF16         |
| DeepSeek        | DeepSeek-R1-0528                     | deepseek-ai/DeepSeek-R1                           | 163839         | FP8          |
| DeepSeek        | DeepSeek-R1-0528 Throughput          | deepseek-ai/DeepSeek-R1-0528-tput                 | 163839         | FP8          |
| DeepSeek        | DeepSeek-V3-0324                     | deepseek-ai/DeepSeek-V3                           | 163839         | FP8          |
| Meta            | Llama 4 Maverick<br />(17Bx128E)     | meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 | 1048576        | FP8          |
| Meta            | Llama 4 Scout<br />(17Bx16E)         | meta-llama/Llama-4-Scout-17B-16E-Instruct         | 1048576        | FP16         |
| Meta            | Llama 3.3 70B Instruct Turbo         | meta-llama/Llama-3.3-70B-Instruct-Turbo           | 131072         | FP8          |
| Deep Cogito     | Cogito v2 Preview 70B                | deepcogito/cogito-v2-preview-llama-70B            | 32768          | BF16         |
| Deep Cogito     | Cogito v2 Preview 109B MoE           | deepcogito/cogito-v2-preview-llama-109B-MoE       | 32768          | BF16         |
| Deep Cogito     | Cogito v2 Preview 405B               | deepcogito/cogito-v2-preview-llama-405B           | 32768          | BF16         |
| Deep Cogito     | Cogito v2.1 671B                     | deepcogito/cogito-v2-1-671b                       | 32768          | FP8          |
| Mistral AI      | Magistral Small 2506 API             | mistralai/Magistral-Small-2506                    | 40960          | BF16         |
| Mistral AI      | Ministral 3 14B Instruct 2512        | mistralai/Ministral-3-14B-Instruct-2512           | 262144         | BF16         |
| Marin Community | Marin 8B Instruct                    | marin-community/marin-8b-instruct                 | 4096           | FP16         |
| Essential AI    | Rnj-1 Instruct                       | essentialai/rnj-1-instruct                        | 32768          | BF16         |
| Mistral AI      | Mistral Small 3 Instruct (24B)       | mistralai/Mistral-Small-24B-Instruct-2501         | 32768          | FP16         |
| Meta            | Llama 3.1 8B Instruct Turbo          | meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo       | 131072         | FP8          |
| Qwen            | Qwen 2.5 7B Instruct Turbo           | Qwen/Qwen2.5-7B-Instruct-Turbo                    | 32768          | FP8          |
| Qwen            | Qwen 2.5 72B Instruct Turbo          | Qwen/Qwen2.5-72B-Instruct-Turbo                   | 32768          | FP8          |
| Qwen            | Qwen2.5 Vision Language 72B Instruct | Qwen/Qwen2.5-VL-72B-Instruct                      | 32768          | FP8          |
| Qwen            | Qwen3 235B A22B Throughput           | Qwen/Qwen3-235B-A22B-fp8-tput                     | 40960          | FP8          |
| Arcee           | Arcee AI Trinity Mini                | arcee-ai/trinity-mini                             | 32768          | -            |
| Meta            | Llama 3.1 405B Instruct Turbo        | meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo     | 130815         | FP8          |
| Meta            | Llama 3.2 3B Instruct Turbo          | meta-llama/Llama-3.2-3B-Instruct-Turbo            | 131072         | FP16         |
| Meta            | Llama 3 8B Instruct Lite             | meta-llama/Meta-Llama-3-8B-Instruct-Lite          | 8192           | INT4         |
| Meta            | Llama 3 70B Instruct Reference       | meta-llama/Llama-3-70b-chat-hf                    | 8192           | FP16         |
| Google          | Gemma Instruct (2B)                  | google/gemma-2b-it\*                              | 8192           | FP16         |
| Google          | Gemma 3N E4B Instruct                | google/gemma-3n-E4B-it                            | 32768          | FP8          |
| Gryphe          | MythoMax-L2 (13B)                    | Gryphe/MythoMax-L2-13b\*                          | 4096           | FP16         |
| Mistral AI      | Mistral (7B) Instruct v0.2           | mistralai/Mistral-7B-Instruct-v0.2                | 32768          | FP16         |
| Mistral AI      | Mistral (7B) Instruct v0.3           | mistralai/Mistral-7B-Instruct-v0.3                | 32768          | FP16         |
| NVIDIA          | Nemotron Nano 9B v2                  | nvidia/NVIDIA-Nemotron-Nano-9B-v2                 | 131072         | BF16         |

\* The Free version of Llama 3.3 70B Instruct Turbo has a reduced rate limit of .6 requests/minute (36/hour) for users on the free tier and 3 requests/minute for any user who has added a credit card on file.

\*Deprecated model, see [Deprecations](/docs/deprecations) for more details

**Chat Model Examples**

* [PDF to Chat App](https://www.pdftochat.com/) - Chat with your PDFs (blogs, textbooks, papers)
* [Open Deep Research Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/Together_Open_Deep_Research_CookBook.ipynb) - Generate long form reports using a single prompt
* [RAG with Reasoning Models Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/RAG_with_Reasoning_Models.ipynb) - RAG with DeepSeek-R1
* [Fine-tuning Chat Models Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Finetuning/Finetuning_Guide.ipynb) - Tune Language models for conversation
* [Building Agents](https://github.com/togethercomputer/together-cookbook/tree/main/Agents) - Agent workflows with language models

## Image models

Use our [Images](/reference/post-images-generations) endpoint for Image Models.

| Organization      | Model Name                         | Model String for API                     | Default steps |
| :---------------- | :--------------------------------- | :--------------------------------------- | :------------ |
| Google            | Imagen 4.0 Preview                 | google/imagen-4.0-preview                | -             |
| Google            | Imagen 4.0 Fast                    | google/imagen-4.0-fast                   | -             |
| Google            | Imagen 4.0 Ultra                   | google/imagen-4.0-ultra                  | -             |
| Google            | Flash Image 2.5 (Nano Banana)      | google/flash-image-2.5                   | -             |
| Google            | Gemini 3 Pro Image (Nano Banana 2) | google/gemini-3-pro-image                | -             |
| Black Forest Labs | Flux.1 \[schnell] **(free)\***     | black-forest-labs/FLUX.1-schnell-Free    | N/A           |
| Black Forest Labs | Flux.1 \[schnell] (Turbo)          | black-forest-labs/FLUX.1-schnell         | 4             |
| Black Forest Labs | Flux.1 Dev                         | black-forest-labs/FLUX.1-dev             | 28            |
| Black Forest Labs | Flux1.1 \[pro]                     | black-forest-labs/FLUX.1.1-pro           | -             |
| Black Forest Labs | Flux.1 Kontext \[pro]              | black-forest-labs/FLUX.1-kontext-pro     | 28            |
| Black Forest Labs | Flux.1 Kontext \[max]              | black-forest-labs/FLUX.1-kontext-max     | 28            |
| Black Forest Labs | Flux.1 Kontext \[dev]              | black-forest-labs/FLUX.1-kontext-dev     | 28            |
| Black Forest Labs | FLUX.1 Krea \[dev]                 | black-forest-labs/FLUX.1-krea-dev        | 28            |
| Black Forest Labs | FLUX.2 \[pro]                      | black-forest-labs/FLUX.2-pro             | -             |
| Black Forest Labs | FLUX.2 \[dev]                      | black-forest-labs/FLUX.2-dev             | -             |
| Black Forest Labs | FLUX.2 \[flex]                     | black-forest-labs/FLUX.2-flex            | -             |
| ByteDance         | Seedream 3.0                       | ByteDance-Seed/Seedream-3.0              | -             |
| ByteDance         | Seedream 4.0                       | ByteDance-Seed/Seedream-4.0              | -             |
| Qwen              | Qwen Image                         | Qwen/Qwen-Image                          | -             |
| RunDiffusion      | Juggernaut Pro Flux                | RunDiffusion/Juggernaut-pro-flux         | -             |
| RunDiffusion      | Juggernaut Lightning Flux          | Rundiffusion/Juggernaut-Lightning-Flux   | -             |
| HiDream           | HiDream-I1-Full                    | HiDream-ai/HiDream-I1-Full               | -             |
| HiDream           | HiDream-I1-Dev                     | HiDream-ai/HiDream-I1-Dev                | -             |
| HiDream           | HiDream-I1-Fast                    | HiDream-ai/HiDream-I1-Fast               | -             |
| Ideogram          | Ideogram 3.0                       | ideogram/ideogram-3.0                    | -             |
| Lykon             | Dreamshaper                        | Lykon/DreamShaper                        | -             |
| Stability AI      | SD XL                              | stabilityai/stable-diffusion-xl-base-1.0 | -             |
| Stability AI      | Stable Diffusion 3                 | stabilityai/stable-diffusion-3-medium    | -             |

Note: Due to high demand, FLUX.1 \[schnell] Free has a model specific rate limit of 10 img/min. Image models can also only be used with credits. Users are unable to call Image models with a zero or negative balance.

\*Free model has reduced rate limits and performance compared to our paid Turbo endpoint for Flux Shnell named `black-forest-labs/FLUX.1-schnell`

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

If you're not sure which vision model to use, we currently recommend **Llama 4 Scout** (`meta-llama/Llama-4-Scout-17B-16E-Instruct`) to get started. For model specific rate limits, navigate [here](/docs/rate-limits).

| Organization | Model Name                           | API Model String                                  | Context length |
| :----------- | :----------------------------------- | :------------------------------------------------ | :------------- |
| Meta         | Llama 4 Maverick<br />(17Bx128E)     | meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 | 524288         |
| Meta         | Llama 4 Scout<br />(17Bx16E)         | meta-llama/Llama-4-Scout-17B-16E-Instruct         | 327680         |
| Qwen         | Qwen2.5 Vision Language 72B Instruct | Qwen/Qwen2.5-VL-72B-Instruct                      | 32768          |
| Qwen         | Qwen3-VL-32B-Instruct                | Qwen/Qwen3-VL-32B-Instruct                        | 256000         |
| Qwen         | Qwen3-VL-8B-Instruct                 | Qwen/Qwen3-VL-8B-Instruct                         | 262100         |

**Vision Model Examples**

* [LlamaOCR](https://llamaocr.com/) - A tool that takes documents (like receipts) and outputs markdown
* [Wireframe to Code](https://www.napkins.dev/) - A wireframe to app tool that takes in a UI mockup of a site and give you React code.
* [Extracting Structured Data from Images](https://github.com/togethercomputer/together-cookbook/blob/main/Structured_Text_Extraction_from_Images.ipynb) - Extract information from images as JSON

## Video models

| Organization | Model Name           | Model String for API        | Resolution / Duration |
| :----------- | :------------------- | :-------------------------- | :-------------------- |
| MiniMax      | MiniMax 01 Director  | minimax/video-01-director   | 720p / 5s             |
| MiniMax      | MiniMax Hailuo 02    | minimax/hailuo-02           | 768p / 10s            |
| Google       | Veo 2.0              | google/veo-2.0              | 720p / 5s             |
| Google       | Veo 3.0              | google/veo-3.0              | 720p / 8s             |
| Google       | Veo 3.0 + Audio      | google/veo-3.0-audio        | 720p / 8s             |
| Google       | Veo 3.0 Fast         | google/veo-3.0-fast         | 1080p / 8s            |
| Google       | Veo 3.0 Fast + Audio | google/veo-3.0-fast-audio   | 1080p / 8s            |
| ByteDance    | Seedance 1.0 Lite    | ByteDance/Seedance-1.0-lite | 720p / 5s             |
| ByteDance    | Seedance 1.0 Pro     | ByteDance/Seedance-1.0-pro  | 1080p / 5s            |
| PixVerse     | PixVerse v5          | pixverse/pixverse-v5        | 1080p / 5s            |
| Kuaishou     | Kling 2.1 Master     | kwaivgI/kling-2.1-master    | 1080p / 5s            |
| Kuaishou     | Kling 2.1 Standard   | kwaivgI/kling-2.1-standard  | 720p / 5s             |
| Kuaishou     | Kling 2.1 Pro        | kwaivgI/kling-2.1-pro       | 1080p / 5s            |
| Kuaishou     | Kling 2.0 Master     | kwaivgI/kling-2.0-master    | 1080p / 5s            |
| Kuaishou     | Kling 1.6 Standard   | kwaivgI/kling-1.6-standard  | 720p / 5s             |
| Kuaishou     | Kling 1.6 Pro        | kwaivgI/kling-1.6-pro       | 1080p / 5s            |
| Wan-AI       | Wan 2.2 I2V          | Wan-AI/Wan2.2-I2V-A14B      | -                     |
| Wan-AI       | Wan 2.2 T2V          | Wan-AI/Wan2.2-T2V-A14B      | -                     |
| Vidu         | Vidu 2.0             | vidu/vidu-2.0               | 720p / 8s             |
| Vidu         | Vidu Q1              | vidu/vidu-q1                | 1080p / 5s            |
| OpenAI       | Sora 2               | openai/sora-2               | 720p / 8s             |
| OpenAI       | Sora 2 Pro           | openai/sora-2-pro           | 1080p / 8s            |

## Audio models

Use our [Audio](/reference/audio-speech) endpoint for text-to-speech models. For speech-to-text models see [Transcription](/reference/audio-transcriptions) and [Translations](/reference/audio-translations)

| Organization | Modality       | Model Name       | Model String for API           |
| :----------- | :------------- | :--------------- | :----------------------------- |
| Canopy Labs  | Text-to-Speech | Orpheus 3B       | canopylabs/orpheus-3b-0.1-ft   |
| Kokoro       | Text-to-Speech | Kokoro           | hexgrad/Kokoro-82M             |
| Cartesia     | Text-to-Speech | Cartesia Sonic 2 | cartesia/sonic-2               |
| Cartesia     | Text-to-Speech | Cartesia Sonic   | cartesia/sonic                 |
| OpenAI       | Speech-to-Text | Whisper Large v3 | openai/whisper-large-v3        |
| Mistral AI   | Speech-to-Text | Voxtral Mini 3B  | mistralai/Voxtral-Mini-3B-2507 |

**Audio Model Examples**

* [PDF to Podcast Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/PDF_to_Podcast.ipynb) - Generate a NotebookLM style podcast given a PDF
* [Audio Podcast Agent Workflow](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/Serial_Chain_Agent_Workflow.ipynb) - Agent workflow to generate audio files given input content

## Embedding models

| Model Name                     | Model String for API                       | Model Size | Embedding Dimension | Context Window |
| :----------------------------- | ------------------------------------------ | :--------- | :------------------ | :------------- |
| M2-BERT-80M-32K-Retrieval      | togethercomputer/m2-bert-80M-32k-retrieval | 80M        | 768                 | 32768          |
| BGE-Large-EN-v1.5              | BAAI/bge-large-en-v1.5                     | 326M       | 1024                | 512            |
| BGE-Base-EN-v1.5               | BAAI/bge-base-en-v1.5                      | 102M       | 768                 | 512            |
| GTE-Modernbert-base            | Alibaba-NLP/gte-modernbert-base            | 149M       | 768                 | 8192           |
| Multilingual-e5-large-instruct | intfloat/multilingual-e5-large-instruct    | 560M       | 1024                | 514            |

**Embedding Model Examples**

* [Contextual RAG](https://docs.together.ai/docs/how-to-implement-contextual-rag-from-anthropic) - An open source implementation of contextual RAG by Anthropic
* [Code Generation Agent](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/Looping_Agent_Workflow.ipynb) - An agent workflow to generate and iteratively improve code
* [Multimodal Search and Image Generation](https://github.com/togethercomputer/together-cookbook/blob/main/Multimodal_Search_and_Conditional_Image_Generation.ipynb) - Search for images and generate more similar ones
* [Visualizing Embeddings](https://github.com/togethercomputer/together-cookbook/blob/main/Embedding_Visualization.ipynb) - Visualizing and clustering vector embeddings

## Rerank models

Our [Rerank API](/docs/rerank-overview) has built-in support for the following models, that we host via our serverless endpoints.

| Organization | Model Name   | Model Size | Model String for API                | Max Doc Size (tokens) | Max Docs |
| ------------ | ------------ | :--------- | ----------------------------------- | --------------------- | -------- |
| Salesforce   | LlamaRank    | 8B         | Salesforce/Llama-Rank-v1            | 8192                  | 1024     |
| MixedBread   | Rerank Large | 1.6B       | mixedbread-ai/Mxbai-Rerank-Large-V2 | 32768                 | -        |

**Rerank Model Examples**

* [Search and Reranking](https://github.com/togethercomputer/together-cookbook/blob/main/Search_with_Reranking.ipynb) - Simple semantic search pipeline improved using a reranker
* [Implementing Hybrid Search Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Open_Contextual_RAG.ipynb) - Implementing semantic + lexical search along with reranking

## Moderation models

Use our [Completions](/reference/completions-1) endpoint to run a moderation model as a standalone classifier, or use it alongside any of the other models above as a filter to safeguard responses from 100+ models, by specifying the parameter `"safety_model": "MODEL_API_STRING"`

| Organization | Model Name          | Model String for API             | Context length |
| :----------- | :------------------ | :------------------------------- | :------------- |
| Meta         | Llama Guard (8B)    | meta-llama/Meta-Llama-Guard-3-8B | 8192           |
| Meta         | Llama Guard 4 (12B) | meta-llama/Llama-Guard-4-12B     | 1048576        |
| Virtue AI    | Virtue Guard        | VirtueAI/VirtueGuard-Text-Lite   | 32768          |


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt