# Source: https://docs.anyscale.com/llm.md

# LLMs and agentic AI on Anyscale

[View Markdown](/llm.md)

# LLMs and agentic AI on Anyscale

The Anyscale platform provides a comprehensive, end-to-end ecosystem for developing and deploying large language model (LLM) applications in production. Powered by the Ray distributed computing framework, Anyscale enables organizations to efficiently serve, fine-tune, and run batch inference on open source LLMs at scale, as well as build RAG and agentic applications with MCP. This document provides a high-level overview of these core capabilities.

## LLM serving[​](#serving "Direct link to LLM serving")

Anyscale offers a robust and scalable solution for deploying LLMs to handle real-time user requests with low latency and high throughput. Anyscale combines Ray Serve for orchestration with vLLM for high-performance inference.

Anyscale provides a managed, cost-effective, and performance-optimized serving infrastructure. The following table outlines the features that allow Anyscale to solve the primary challenges of LLM serving, which include managing GPU memory, minimizing latency, and ensuring scalability:

| Feature                               | Description                                                                                                                                                                                      |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Flexible orchestration with Ray Serve | Ray Serve acts as the scalable orchestration layer, simplifying production deployment.                                                                                                           |
| Automatic scaling                     | Automatically scales model replicas up and down (including to zero) based on traffic, optimizing GPU utilization and minimizing costs.                                                           |
| High-performance backends             | Integrates with state-of-the-art inference engines such as vLLM, which use techniques such as `PagedAttention` and continuous batching to maximize throughput and manage GPU memory effectively. |
| Unified multi-model deployment        | Serves multiple models or model variants from a single deployment, simplifying management.                                                                                                       |
| Dynamic multi-LoRA support            | Allows a single base model to serve requests for many different fine-tuned adapters simultaneously.                                                                                              |
| OpenAI-compatible API                 | Exposes a familiar API endpoint, allowing for seamless integration with existing applications built for OpenAI models.                                                                           |

To learn more, see the [Anyscale LLM serving and inference template](https://console.anyscale.com/template-preview/deployment-serve-llm).

## LLM post-training and agentic tuning[​](#post-training "Direct link to LLM post-training and agentic tuning")

Post-training allows you to adapt pre-trained foundation models to excel at specific applications, domains, and behavioral requirements, from improving task performance to creating autonomous agents that interact with tools and environments. Anyscale provides a powerful and flexible platform for post-training large language models, allowing you to scale your fine-tuning experiments with Ray.

You can choose the approach that best fits your needs, from full fine-tuning to parameter-efficient methods (LoRA, QLoRA, freeze-tuning) with distributed training strategies such as FSDP, DeepSpeed, and Megatron for efficient scaling across GPUs. This flexibility allows you to optimize for cost, speed, or maximum control, whether you're specializing a model for your domain or training it to autonomously use APIs and execute code.

The following table provides an overview of post-training methodologies supported on Anyscale:

| Methodology                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Continued pre-training                                | Extend a model's knowledge by continuing unsupervised training on domain-specific corpora. This injects specialized knowledge directly into the model's parameters, teaching it technical jargon and industry-specific concepts.                                                                                                                                                                                                                    |
| Supervised fine-tuning (SFT)                          | Train models to map prompts to desired responses using labeled examples. Key applications include:- Instruction following with high-quality prompt-response pairs.<br />- Task specialization (summarization, sentiment analysis, structured output generation).                                                                                                                                                                                    |
| Preference tuning and alignment                       | Refine model behavior based on human preferences for attributes such as helpfulness, safety, and politeness. Anyscale supports:- Traditional RLHF with reward modeling and PPO.<br />- Direct preference optimization methods: DPO, SimPO, ORPO, KTO.                                                                                                                                                                                               |
| Reinforcement Learning from Verifiable Rewards (RLVR) | Use automated, verifiable rewards for tasks where correctness can be objectively determined. Supported algorithms include:- PPO for maximum control.<br />- GRPO (Group Relative Policy Optimization) for simplified training without a critic model.<br />- DAPO (Decoupled Clip and Dynamic Sampling Policy Optimization) for enhanced diversity and efficiency.<br />- Common applications: code generation, text-to-SQL, tool use optimization. |
| Agentic tuning                                        | Train models to become autonomous agents that reason, plan, and interact with tools and environments. This advanced approach:- Optimizes for sequences of actions and multi-step reasoning rather than single responses.<br />- Develops reliable tool use including API calls, code execution, and database queries.<br />- Often employs RLVR methodologies (PPO, GRPO, DAPO) to learn from verifiable feedback.                                  |

For more details about when to choose different post-training methods, see [Core post-training methodologies](/llm/fine-tuning.md#core-post-training-methodologies).

For hands-on tutorials, see the following:

* [Fine-tuning with LLaMA-Factory](https://console.anyscale.com/template-preview/llm_finetuning)
* [Fine-tune an LLM with Ray Train and DeepSpeed](https://console.anyscale.com/template-preview/deepspeed_finetune)
* [GRPO with SkyRL](/tutorials/train-llm-with-skyrl.md)

## LLM batch inference[​](#batch-inference "Direct link to LLM batch inference")

For offline tasks such as data enrichment, analysis, or model evaluation on large datasets, Anyscale leverages `ray.data.llm` to provide scalable and efficient batch inference.

The following table provides an overview of features that help scale batch inference on Anyscale:

| Feature                                | Description                                                                                                                                                                                                                      |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Scalable data processing with Ray Data | Ray Data is a distributed data processing library that seamlessly scales LLM inference across a cluster of machines. It handles the parallelism and resource management required to process terabytes of data.                   |
| Optimized inference integration        | The `ray.data.llm` module integrates directly with high-performance engines such as vLLM, bringing the same optimizations from real-time serving (for example, continuous batching) to the batch context for maximum efficiency. |
| Simplified API                         | The `build_processor` API helps you easily configure and run inference jobs. You can target models running locally on the cluster using vLLM or query external models using an OpenAI-compatible API endpoint.                   |
| Support for multimodal models          | Ray Data LLM handles both text-only and vision-language models (VLMs), enabling batch processing of datasets containing text and images.                                                                                         |

To learn more, see the [text-to-text batch inference template](https://console.anyscale.com/template-preview/llm_batch_inference_text) or the [multimodal batch inference template](https://console.anyscale.com/template-preview/llm_batch_inference_vision).

## Retrieval-augmented generation (RAG)[​](#rag "Direct link to Retrieval-augmented generation (RAG)")

Anyscale provides a unified platform to build, deploy, and scale end-to-end RAG pipelines, which ground LLMs in external knowledge sources to provide up-to-date, accurate, and attributable responses. The following table provides an overview of capabilities:

| Capability                           | Description                                                                                                                                                                                                                                |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Scalable data ingestion and indexing | RAG pipelines begin with an offline data processing stage to create a vector index. Anyscale processes document corpuses with Ray Data, which handles chunking, embedding generation, and writing to vector databases in parallel.         |
| High-performance online serving      | You use Anyscale services to deploy a low-latency LLM online component to retrieve context and generate an answer. This allows both the retriever and the generator LLM to scale independently based on request volume.                    |
| End-to-end unified platform          | Anyscale uses the same framework to build and manage both the batch-oriented indexing pipeline and the latency-sensitive serving application. This simplifies the MLOps lifecycle, reduces system complexity, and accelerates development. |

To learn more, see:

* [Building scalable RAG pipelines](https://www.anyscale.com/blog/rag-pipelines-how-to) (blog post)
* [End-to-end RAG deep dive template](https://console.anyscale.com/template-preview/e2e-rag-deepdive)

## Agents and MCP (Model Context Protocol)[​](#agents-mcp "Direct link to Agents and MCP (Model Context Protocol)")

Anyscale is an ideal platform for building and operating sophisticated LLM agents, which use an LLM as a reasoning engine to plan and execute complex tasks by interacting with tools and external environments. The following table provides an overview of capabilities:

| Capability                  | Description                                                                                                                                                                                                                                                                                                                                                                                                         |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Complex agent orchestration | Agentic workflows are often dynamic and involve complex operations (for example, LLM calls, tool execution, state updates). Ray's distributed task and actor framework provides a natural and powerful way to orchestrate these workflows with arbitrary dependencies.                                                                                                                                              |
| Scalable MCP deployments    | You can package the tools an agent relies on (for example, code interpreters, database query engines, APIs) as independent microservices and deploy at scale using Ray Serve. By wrapping an MCP server in a Ray Serve deployment, each tool gains production-grade capabilities such as automatic autoscaling to handle variable loads, load balancing across replicas, and fault tolerance for high availability. |

To learn more, see:

* [Unlocking agentic AI with MCP](https://www.youtube.com/watch?v=R2vqlGJ5Wes) (webinar recording)
* [Deploy custom MCP servers with Ray Serve and Anyscale services template](https://console.anyscale.com/template-preview/mcp-ray-serve)
* [Deploy a LangChain agent with Ray Serve template](https://console.anyscale.com/template-preview/langchain-agent-ray-serve)

## Other generative AI capabilities[​](#other "Direct link to Other generative AI capabilities")

Beyond text-based LLMs, the Anyscale platform is a versatile solution for a wide range of generative AI workloads, leveraging its scalable compute infrastructure for different data modalities and model architectures. The following table provides an overview of capabilities:

| Capability           | Description                                                                                                                                                                                                                                                            |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Multimodal pipelines | Build complex, multi-stage pipelines that combine different models and data types. For example, use the `Whisper` model for scalable audio transcription and then pipe the results to an LLM for summarization, analysis, or content moderation (LLM-as-a-judge).      |
| Image generation     | Anyscale provides the raw GPU power needed for demanding image generation workloads. The platform supports both fine-tuning diffusion models such as Stable Diffusion on custom datasets and the massive computational task of pre-training these models from scratch. |

To learn more, see:

* [Entity recognition with LLMs template](https://console.anyscale.com/template-preview/entity-recognition-with-llms)
* [Audio curation with `Whisper` and LLM-as-a-judge template](https://console.anyscale.com/template-preview/audio-dataset-curation-llm-judge)
* [Stable Diffusion fine-tuning template](https://console.anyscale.com/template-preview/finetune-stable-diffusion)
* [Stable Diffusion pre-training template](https://console.anyscale.com/template-preview/stable-diffusion-pretraining)
