# Source: https://docs.anyscale.com/llm/serving/intro.md

# What is LLM serving?

[View Markdown](/llm/serving/intro.md)

# What is LLM serving?

LLM serving describes a large language model deployed to production to handle user prompts and generate responses.

This page provides an overview of LLM serving fundamentals, from text generation mechanics to essential optimization techniques for building performant, scalable applications.

## How LLMs generate text[​](#generate-text "Direct link to How LLMs generate text")

LLMs operate as next-token predictors.

*Tokens* are the basic units that language models process. A token can represent a word, subword, or character. Models such as GPT typically use subword tokens, especially for rare or compound words. The model converts all text to tokens before processing.

LLMs process text input and generate output one token at a time until they reach a stopping criterion or maximum length.

LLM inference operates through two distinct phases that determine performance characteristics: the prefill phase and decode phase.

### Prefill phase[​](#prefill "Direct link to Prefill phase")

In the prefill phase, the model encodes all input tokens simultaneously to prepare for generation. The following describes this phase:

* The model processes the entire input in parallel for high efficiency.
* It computes key-value pairs as intermediate representations.
* It maximizes GPU utilization through parallelized computations.

### Decode phase[​](#decode "Direct link to Decode phase")

In the decode phase, the model generates tokens sequentially, with each token depending on all previous tokens. The following describes this phase:

* The model operates sequentially, which reduces efficiency for large outputs.
* It's limited by memory bandwidth rather than compute capacity.
* It underutilizes GPU resources compared to the prefill phase.

note

The model loads the entire key-value (KV) cache to maintain generation context during the decode phase. See [Key-value (KV) caching](#kv-cache).

## Key concepts for LLM serving[​](#key-concepts "Direct link to Key concepts for LLM serving")

Efficient LLM serving requires specific optimization strategies to manage computational and memory challenges. You must understand the following concepts to optimize your workloads for memory management, redundant calculations, and hardware utilization.

### Key-value (KV) caching[​](#kv-cache "Direct link to Key-value (KV) caching")

KV caching eliminates redundant computations during text generation. Instead of recalculating keys and values for the entire sequence when you add each token, the system:

1. Caches computed K and V values for all previous tokens.
2. Computes K and V only for the new token.
3. Reuses cached values for context.

Efficiently using KV caching accelerates generation and reduces computational overhead for longer sequences.

### Paged attention[​](#paged-attention "Direct link to Paged attention")

Paged attention optimizes KV cache memory management by addressing allocation inefficiencies. Traditional approaches allocate large, continuous memory blocks that waste resources because cache sizes are unpredictable.

Paged attention works by doing the following:

* It divides the KV cache into fixed-size *pages*.
* It stores pages non-contiguously in GPU memory.
* It manages pages similar to virtual memory in operating systems.

Paged attention provides the following benefits:

* Reduced memory fragmentation.
* Increased concurrent request capacity.
* Improved overall memory utilization.

### Continuous batching[​](#continuous-batching "Direct link to Continuous batching")

Continuous batching optimizes throughput by eliminating GPU idle time during inference.

Traditional static batching works as follows:

* The system waits for all requests in a batch to complete.
* This creates idle time when requests finish at different rates.
* It underutilizes GPU resources.

Continuous batching improves this model by doing the following:

* The system immediately replaces completed requests with new ones.
* It maintains constant GPU utilization.
* It increases concurrent user capacity.

This scheduling algorithm significantly improves throughput compared to static batching approaches.

### Memory requirements for LLM serving[​](#memory-requirements "Direct link to Memory requirements for LLM serving")

GPU memory allocation includes three primary components:

| Component                    | Description                  | Scaling factors                                    |
| ---------------------------- | ---------------------------- | -------------------------------------------------- |
| **Model weights**            | Model parameters             | Model size, precision (such as FP16, FP8, or INT4) |
| **KV cache**                 | Token representations        | Batch size, context length                         |
| **Activations and overhead** | Temporary buffers, framework | Model architecture, batch size                     |

For detailed memory calculations and GPU selection, see [Choose a GPU for LLM serving](/llm/serving/gpu-guidance.md).

### Context window considerations[​](#context-window "Direct link to Context window considerations")

The context window defines the maximum tokens a model can process (input + output). This parameter directly affects memory usage and the use cases you can support.

| Context length      | Typical use cases                    | Memory impact             |
| ------------------- | ------------------------------------ | ------------------------- |
| **4k-8k tokens**    | Q\&A, simple chat                    | Low KV cache requirements |
| **32k-128k tokens** | Document analysis, summarization     | Moderate memory usage     |
| **128k+ tokens**    | Multi-step agents, complex reasoning | High memory requirements  |

### Parallelism strategies[​](#parallelism "Direct link to Parallelism strategies")

When your models exceed single-GPU capacity, you can use parallelism strategies:

| Strategy                      | Description                                   | Use case                              |
| ----------------------------- | --------------------------------------------- | ------------------------------------- |
| **Tensor Parallelism (TP)**   | Splits model layers across GPUs within a node | Models up to 8x GPU memory            |
| **Pipeline Parallelism (PP)** | Splits model layers across multiple nodes     | Models exceeding single-node capacity |

For detailed parallelism configuration, see [Choose a GPU for LLM serving](/llm/serving/gpu-guidance.md).

## Selecting an LLM for production[​](#selecting-model "Direct link to Selecting an LLM for production")

When you choose a model for inference, consider the following factors:

* Model quality benchmarks
* Task and domain alignment
* Model performance characteristics

### Model quality benchmarks[​](#benchmarks "Direct link to Model quality benchmarks")

You can evaluate models using established benchmarks:

* [Chatbot Arena](https://huggingface.co/spaces/lmarena-ai/chatbot-arena-leaderboard) for conversational capabilities.
* [MMLU-Pro](https://huggingface.co/spaces/TIGER-Lab/MMLU-Pro) for domain-specific performance.

### Task and domain alignment[​](#task-alignment "Direct link to Task and domain alignment")

| Model type                   | Best for                                       | Example use cases                      |
| ---------------------------- | ---------------------------------------------- | -------------------------------------- |
| **Base models**              | Next-token prediction, open-ended continuation | Sentence completion, code autocomplete |
| **Instruction-tuned models** | Following explicit directions                  | Chatbots, coding assistants            |

You should also consider the following:

* Verify that the model's context window meets your requirements.
* Select models trained on data that matches your domain (such as scientific text or code).

### Model performance characteristics[​](#performance-chars "Direct link to Model performance characteristics")

* **Reasoning-optimized models**: Better at complex problem-solving but typically slower and may deviate from instructions.
* **Fast-inference models**: Offer lower latency and more consistent prompt adherence, ideal for production chatbots.
* **Hybrid-thinking models**: Combine deliberate, step-by-step reasoning with rapid-response inference in one model. For example, Alibaba's Qwen 3 switches between a "Thinking Mode" for deep reasoning and a "Non-thinking Mode" for quick answers, delivering both accuracy and low latency.
