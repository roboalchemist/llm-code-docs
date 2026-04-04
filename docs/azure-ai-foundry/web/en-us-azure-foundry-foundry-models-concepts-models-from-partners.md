# Source: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-from-partners

Title: Foundry Models from partners and community - Microsoft Foundry

URL Source: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-from-partners

Markdown Content:
This article lists capabilities for a selection of Microsoft Foundry Models from partners and community. Most Foundry Model providers are trusted third-party organizations, partners, research labs, and community contributors. The selection of models that you see in Foundry depends on the [kind of project](https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry#choosing-a-project) you use. To learn more about attributes of Foundry Models from partners and community, see [Explore Foundry Models](https://learn.microsoft.com/en-us/azure/foundry-classic/concepts/foundry-models-overview#models-from-partners-and-community).

Anthropic's flagship product is Claude, a frontier AI model trusted by leading enterprises and millions of users worldwide for complex tasks including coding, agents, financial analysis, research, and office tasks. Claude delivers exceptional performance while maintaining high safety standards.

To work with Claude models in Foundry, see [Deploy and use Claude models in Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-claude).

Important

To use Claude models in Microsoft Foundry, you must have a paid Azure subscription with a billing account in a country or region where Anthropic offers the models for purchase. The following subscription types are currently not supported:

*   Enterprise accounts located in Singapore or South Korea
*   Cloud Solution Provider subscriptions
*   Sponsored subscriptions that use Azure credits
*   Azure subscriptions that don't have an active pay-as-you-go billing method (for example, student, free trial, or startup credit–based accounts)

For a list of common subscription-related errors, see [Common error messages and solutions](https://learn.microsoft.com/en-us/marketplace/purchase-saas-offer-in-azure-portal#common-error-messages-and-solutions).

| Model | Type | Capabilities |
| --- | --- | --- |
| `claude-opus-4-6` **(Preview)** | Messages | - **Input:** text, image, and code - **Output:** text, image, and code (128,000 max tokens) - **Context window:** 1,000,000 (beta) - **Languages:**`en`, `fr`, `ar`, `zh`, `ja`, `ko`, `es`, `hi` - **Tool calling:** Yes (file search and code execution) - **Response formats:** Text in various formats (e.g., prose, lists, Markdown tables, JSON, HTML, code in various programming languages) |
| `claude-opus-4-5` **(Preview)** | Messages | - **Input:** text, image, and code - **Output:** text (64,000 max tokens) - **Context window:** 200,000 - **Languages:**`en`, `fr`, `ar`, `zh`, `ja`, `ko`, `es`, `hi` - **Tool calling:** Yes (file search and code execution) - **Response formats:** Text in various formats (e.g., prose, lists, Markdown tables, JSON, HTML, code in various programming languages) |
| `claude-opus-4-1` **(Preview)** | Messages | - **Input:** text, image, and code - **Output:** text (32,000 max tokens) - **Context window:** 200,000 - **Languages:**`en`, `fr`, `ar`, `zh`, `ja`, `ko`, `es`, `hi` - **Tool calling:** Yes (file search and code execution) - **Response formats:** Text in various formats (e.g., prose, lists, Markdown tables, JSON, HTML, code in various programming languages) |
| `claude-sonnet-4-6` **(Preview)** | Messages | - **Input:** text, image, and code - **Output:** text, image, and code (128,000 max tokens) - **Context window:** 1,000,000 (beta) - **Languages:**`en`, `fr`, `ar`, `zh`, `ja`, `ko`, `es`, `hi` - **Tool calling:** Yes (file search and code execution) - **Response formats:** Text in various formats (e.g., prose, lists, Markdown tables, JSON, HTML, code in various programming languages) |
| `claude-sonnet-4-5` **(Preview)** | Messages | - **Input:** text, image, and code - **Output:** text (64,000 max tokens) - **Context window:** 200,000 - **Languages:**`en`, `fr`, `ar`, `zh`, `ja`, `ko`, `es`, `hi` - **Tool calling:** Yes (file search and code execution) - **Response formats:** Text in various formats (e.g., prose, lists, Markdown tables, JSON, HTML, code in various programming languages) |
| `claude-haiku-4-5` **(Preview)** | Messages | - **Input:** text and image - **Output:** text (64,000 max tokens) - **Context window:** 200,000 - **Languages:**`en`, `fr`, `ar`, `zh`, `ja`, `ko`, `es`, `hi` - **Tool calling:** Yes (file search and code execution) - **Response formats:** Text in various formats (e.g., prose, lists, Markdown tables, JSON, HTML, code in various programming languages) |

See [Anthropic models in the Foundry portal](https://ai.azure.com/explore/models?&selectedCollection=anthropic/?cid=learnDocs).

The Cohere family of models includes various models optimized for different use cases, including chat completions and embeddings. Cohere models are optimized for various use cases that include reasoning, summarization, and question answering.

To deploy Cohere models in Foundry, see [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/deploy-foundry-models).

| Model | Type | Capabilities |
| --- | --- | --- |
| `Cohere-command-r-plus-08-2024` | chat-completion | - **Input:** text (131,072 tokens) - **Output:** text (4,096 tokens) - **Languages:**`en`, `fr`, `es`, `it`, `de`, `pt-br`, `ja`, `ko`, `zh-cn`, and `ar` - **Tool calling:** Yes - **Response formats:** Text, JSON |
| `Cohere-command-r-08-2024` | chat-completion | - **Input:** text (131,072 tokens) - **Output:** text (4,096 tokens) - **Languages:**`en`, `fr`, `es`, `it`, `de`, `pt-br`, `ja`, `ko`, `zh-cn`, and `ar` - **Tool calling:** Yes - **Response formats:** Text, JSON |
| `Cohere-embed-v3-english` | embeddings | - **Input:** text and images (512 tokens) - **Output:** Vector (1024 dim.) - **Languages:**`en` |
| `Cohere-embed-v3-multilingual` | embeddings | - **Input:** text (512 tokens) - **Output:** Vector (1024 dim.) - **Languages:**`en`, `fr`, `es`, `it`, `de`, `pt-br`, `ja`, `ko`, `zh-cn`, and `ar` |

See [Cohere models in the Foundry portal](https://ai.azure.com/explore/models?&selectedCollection=Cohere/?cid=learnDocs).

Meta Llama models and tools are a collection of pretrained and fine-tuned generative AI text and image reasoning models. Meta models range in scale to include:

*   Small language models (SLMs) like 1B and 3B Base and Instruct models for on-device and edge inferencing
*   Mid-size large language models (LLMs) like 7B, 8B, and 70B Base and Instruct models
*   High-performance models like Meta Llama 3.1-405B Instruct for synthetic data generation and distillation use cases.

To deploy Meta Llama models in Foundry, see [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/deploy-foundry-models).

| Model | Type | Capabilities |
| --- | --- | --- |
| `Llama-3.2-11B-Vision-Instruct` | chat-completion | - **Input:** text and image (128,000 tokens) - **Output:** text (8,192 tokens) - **Languages:**`en` - **Tool calling:** No - **Response formats:** Text |
| `Llama-3.2-90B-Vision-Instruct` | chat-completion | - **Input:** text and image (128,000 tokens) - **Output:** text (8,192 tokens) - **Languages:**`en` - **Tool calling:** No - **Response formats:** Text |
| `Meta-Llama-3.1-405B-Instruct` | chat-completion | - **Input:** text (131,072 tokens) - **Output:** text (8,192 tokens) - **Languages:**`en`, `de`, `fr`, `it`, `pt`, `hi`, `es`, and `th` - **Tool calling:** No - **Response formats:** Text |
| `Meta-Llama-3.1-8B-Instruct` | chat-completion | - **Input:** text (131,072 tokens) - **Output:** text (8,192 tokens) - **Languages:**`en`, `de`, `fr`, `it`, `pt`, `hi`, `es`, and `th` - **Tool calling:** No - **Response formats:** Text |
| `Llama-4-Scout-17B-16E-Instruct` | chat-completion | - **Input:** text and image (128,000 tokens) - **Output:** text (8,192 tokens) - **Languages:**`en` - **Tool calling:** No - **Response formats:** Text |

See [Meta models in the Foundry portal](https://ai.azure.com/explore/models?&selectedCollection=Meta/?cid=learnDocs). You can also find several Meta models available as [models sold directly by Azure](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?pivots=azure-direct-others).

Microsoft models include various model groups such as MAI models, Phi models, healthcare AI models, and more.

To deploy Microsoft models in Foundry, see [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/deploy-foundry-models).

| Model | Type | Capabilities |
| --- | --- | --- |
| `Phi-4-mini-instruct` | chat-completion | - **Input:** text (131,072 tokens) - **Output:** text (4,096 tokens) - **Languages:**`ar`, `zh`, `cs`, `da`, `nl`, `en`, `fi`, `fr`, `de`, `he`, `hu`, `it`, `ja`, `ko`, `no`, `pl`, `pt`, `ru`, `es`, `sv`, `th`, `tr`, and `uk` - **Tool calling:** No - **Response formats:** Text |
| `Phi-4-multimodal-instruct` | chat-completion | - **Input:** text, images, and audio (131,072 tokens) - **Output:** text (4,096 tokens) - **Languages:**`ar`, `zh`, `cs`, `da`, `nl`, `en`, `fi`, `fr`, `de`, `he`, `hu`, `it`, `ja`, `ko`, `no`, `pl`, `pt`, `ru`, `es`, `sv`, `th`, `tr`, and `uk` - **Tool calling:** No - **Response formats:** Text |
| `Phi-4` | chat-completion | - **Input:** text (16,384 tokens) - **Output:** text (16,384 tokens) - **Languages:**`en`, `ar`, `bn`, `cs`, `da`, `de`, `el`, `es`, `fa`, `fi`, `fr`, `gu`, `ha`, `he`, `hi`, `hu`, `id`, `it`, `ja`, `jv`, `kn`, `ko`, `ml`, `mr`, `nl`, `no`, `or`, `pa`, `pl`, `ps`, `pt`, `ro`, `ru`, `sv`, `sw`, `ta`, `te`, `th`, `tl`, `tr`, `uk`, `ur`, `vi`, `yo`, and `zh` - **Tool calling:** No - **Response formats:** Text |
| `Phi-4-reasoning` | chat-completion with reasoning content | - **Input:** text (32,768 tokens) - **Output:** text (32,768 tokens) - **Languages:**`en` - **Tool calling:** No - **Response formats:** Text |
| `Phi-4-mini-reasoning` | chat-completion with reasoning content | - **Input:** text (128,000 tokens) - **Output:** text (128,000 tokens) - **Languages:**`en` - **Tool calling:** No - **Response formats:** Text |

See [Microsoft models in the Foundry portal](https://ai.azure.com/explore/models?&selectedCollection=Microsoft/?cid=learnDocs). Microsoft models are also available as [models sold directly by Azure](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?pivots=azure-direct-others).

Mistral AI offers models for code generation, general-purpose chat, and multimodal tasks, including Codestral, Ministral, Mistral Small, and Mistral Medium.

To deploy Mistral AI models in Foundry, see [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/deploy-foundry-models).

| Model | Type | Capabilities |
| --- | --- | --- |
| `Codestral-2501` | chat-completion | - **Input:** text (262,144 tokens) - **Output:** text (4,096 tokens) - **Languages:** en - **Tool calling:** No - **Response formats:** Text |
| `Ministral-3B` | chat-completion | - **Input:** text (131,072 tokens) - **Output:** text (4,096 tokens) - **Languages:** fr, de, es, it, and en - **Tool calling:** Yes - **Response formats:** Text, JSON |
| `Mistral-small-2503` | chat-completion | - **Input:** text (32,768 tokens) - **Output:** text (4,096 tokens) - **Languages:** fr, de, es, it, and en - **Tool calling:** Yes - **Response formats:** Text, JSON |
| `Mistral-medium-2505` | chat-completion | - **Input:** text (128,000 tokens), image - **Output:** text (128,000 tokens) - **Tool calling:** No - **Response formats:** Text, JSON |

See [Mistral AI models in the Foundry portal](https://ai.azure.com/explore/models?&selectedCollection=Mistral+AI/?cid=learnDocs). Mistral models are also available as [models sold directly by Azure](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?pivots=azure-direct-others).

The Stability AI collection of image generation models includes Stable Image Core, Stable Image Ultra, and Stable Diffusion 3.5 Large. Stable Diffusion 3.5 Large accepts both image and text input.

To deploy Stability AI models in Foundry, see [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/deploy-foundry-models).

| Model | Type | Capabilities |
| --- | --- | --- |
| `Stable Diffusion 3.5 Large` | Image generation | - **Input:** text and image (1,000 tokens and 1 image) - **Output:** One Image - **Tool calling:** No - **Response formats**: Image (PNG and JPG) |
| `Stable Image Core` | Image generation | - **Input:** text (1,000 tokens) - **Output:** One Image - **Tool calling:** No - **Response formats:** Image (PNG and JPG) |
| `Stable Image Ultra` | Image generation | - **Input:** text (1,000 tokens) - **Output:** One Image - **Tool calling:** No - **Response formats:** Image (PNG and JPG) |

See [Stability AI models in the Foundry portal](https://ai.azure.com/explore/models?&selectedCollection=Stability+AI/?cid=learnDocs).

*   [Deployment overview for Foundry Models](https://learn.microsoft.com/en-us/azure/foundry-classic/concepts/deployments-overview)
*   [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/deploy-foundry-models)
*   [Deployment types in Foundry Models](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types)
*   [Azure Marketplace requirements for Foundry Models from partners](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/configure-marketplace)
*   [Region availability for Foundry Models](https://learn.microsoft.com/en-us/azure/foundry-classic/how-to/deploy-models-serverless-availability)
*   [Explore Foundry Models](https://learn.microsoft.com/en-us/azure/foundry-classic/concepts/foundry-models-overview)
