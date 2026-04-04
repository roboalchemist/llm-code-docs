# Source: https://docs.anyscale.com/llm/serving/gpu-guidance.md

# Choose a GPU for LLM serving

[View Markdown](/llm/serving/gpu-guidance.md)

# Choose a GPU for LLM serving

This page helps you select and configure GPUs for LLM serving on Anyscale. It includes instructions for calculating memory requirements, avoiding out-of-memory (OOM) errors, and implementing parallelism strategies for optimal performance.

## GPU memory allocation components[​](#memory-components "Direct link to GPU memory allocation components")

GPU memory in LLM deployments has three categories:

| Component                    | Type    | Description                                   | Scaling factors               |
| ---------------------------- | ------- | --------------------------------------------- | ----------------------------- |
| **Model weights**            | Static  | Model parameters, present at all times        | Model size, precision         |
| **KV cache and activations** | Dynamic | Token representations and temporary buffers   | Batch size, context length    |
| **Framework overhead**       | Static  | Runtime requirements before tensor allocation | Framework, model architecture |

## How does vLLM allocate GPU resources?[​](#vllm-allocation "Direct link to How does vLLM allocate GPU resources?")

vLLM follows a specific sequence when it allocates GPU resources. When you understand this process, you can better estimate memory requirements, prevent OOM errors, and optimize performance:

1. **Measure usable VRAM**: vLLM detects total GPU memory and applies a safety factor (`gpu_memory_utilization` = 80-95%)
2. **Load model weights**: vLLM copies model parameters to VRAM (this is the largest allocation and scales with model size and precision)
3. **Account for framework overhead**: vLLM reserves a buffer for CUDA drivers, PyTorch kernels, and logging
4. **Estimate peak activations**: vLLM predicts maximum temporary tensor usage during the forward pass
5. **Reserve KV cache**: vLLM allocates remaining memory for key-value tensors that store past tokens
6. **Derive concurrency limits**: vLLM calculates maximum simultaneous requests based on KV cache budget and sequence length

note

The `max_num_seqs` parameter sets an upper limit for scheduled sequences but doesn't pre-allocate KV cache blocks. vLLM dynamically determines the actual concurrency based on available memory.

### Example: Llama 3 8B memory allocation[​](#llama-example "Direct link to Example: Llama 3 8B memory allocation")

The following table shows GPU memory allocation for `meta-llama/Meta-Llama-3-8B-Instruct` with `max_model_len=8192`:

| Allocation step (in order executed) | Memory used (GiB) | Details                                                        |
| ----------------------------------- | ----------------- | -------------------------------------------------------------- |
| Measure usable VRAM (safety factor) | 19.78             | 90% of 21.98 GiB                                               |
| Load model weights                  | 14.96             | `model weights` take 14.96 GiB                                 |
| Framework/runtime overhead          | 0.06              | `non_torch_memory` takes 0.06 GiB (CUDA driver, kernels, logs) |
| Peak activations buffer             | 1.23              | `PyTorch activation peak memory` takes 1.23 GiB                |
| KV/attention cache                  | 3.53              | The rest of the memory reserved for the `KV Cache` is 3.53 GiB |
| Derive concurrency limits           | —                 | Maximum concurrency for 8192 tokens per request: 3.53x         |

**Notes:**

tip

**Memory optimization strategies:**

* **Reduce context length**: When you halve `max_model_len` from 8192 to 4096, you double potential concurrency.
* **Add GPU capacity**: You can use higher-memory GPUs or implement tensor parallelism.
* **Unit conversion**: 1 GiB is approximately 1.073 GB (A10G's 24 GB appears as 21.98 GiB after ECC overhead).

## Supported GPU types[​](#gpu-types "Direct link to Supported GPU types")

Anyscale supports GPUs from multiple vendors:

| Vendor      | GPU models                                                                 |
| ----------- | -------------------------------------------------------------------------- |
| Nvidia      | V100, P100, T4, P4, K80, A10G, L4, L40S, A100 (40GB/80GB), H100, H200, H20 |
| Intel       | GPU Max 1550, GPU Max 1100, Gaudi                                          |
| AMD         | Instinct MI100, MI210, MI250X, MI300X-OAM, Radeon R9/HD series             |
| Specialized | AWS Neuron Core, Google TPU (v2-v6e), Huawei Ascend 910B                   |

note

Not all GPUs are available in all cloud provider regions. Some GPU types require custom Anyscale cloud deployments.

For the complete list of supported accelerators, see the [Ray Serve LLM Config documentation](https://docs.ray.io/en/latest/serve/api/doc/ray.serve.llm.LLMConfig.html).

## GPU specifications comparison[​](#gpu-specifications-comparison "Direct link to GPU specifications comparison")

The following table compares commonly used GPUs for LLM serving. The specifications represent typical values and might vary by system configuration.

note

Cloud instance offerings change frequently. Check your cloud provider's documentation for current availability.

| GPU             | Architecture | Memory (GB) | CUDA cores | Bandwidth (TB/s) | Interconnect | AWS instance (single-GPU examples) | Google Cloud instance (single-GPU examples) |
| --------------- | ------------ | ----------- | ---------- | ---------------- | ------------ | ---------------------------------- | ------------------------------------------- |
| Nvidia T4       | Turing       | 16          | 2,560      | 0.32             | PCIe 3       | `g4dn.xlarge` (1 × T4)             | `n1-standard-4` + 1 × T4                    |
| Nvidia L4       | Ada          | 24          | 7,424      | 0.30             | PCIe 4       | `g6.xlarge` (1 × L4)               | `g2-standard-4` (1 × L4)                    |
| Nvidia L40S     | Ada          | 48          | 18,176     | 0.86             | PCIe 4       | `g6e.2xlarge` (1 × L40S)           | —                                           |
| Nvidia A10G     | Ampere       | 24          | 9,216      | 0.60             | PCIe 4       | `g5.xlarge` (1 × A10G)             | —                                           |
| Nvidia A100-40G | Ampere       | 40          | 6,912      | 1.60             | NVLink 3     | `p4d.24xlarge` (8 × A100-40G)      | `a2-highgpu-1g` (1 × A100-40G)              |
| Nvidia A100-80G | Ampere       | 80          | 6,912      | 2.0              | NVLink 3     | `p4de.24xlarge` (8 × A100-80G)     | `a2-ultragpu-1g` (1 × A100-80G)             |
| Nvidia H100     | Hopper       | 80          | 14,592     | 3.35             | NVLink 4     | `p5.48xlarge` (8 × H100)           | `a3-highgpu-8g` (8 × H100)                  |
| Nvidia H200     | Hopper HBM3e | 141         | 16,896     | 4.8              | NVLink 4     | `p5e.24xlarge` (8 × H200)          | `a3-ultragpu-8g` (8 × H200)                 |
| Nvidia B200     | Blackwell    | 180         | 16,896     | 8.0              | NVLink 5     | `p6-b200.48xlarge` (8 × B200)      | `a4-highgpu-8g` (8 × B200)                  |

### NVLink interconnect specifications[​](#nvlink-interconnect-specifications "Direct link to NVLink interconnect specifications")

NVLink provides high-speed GPU interconnection with significantly better performance than PCIe:

| Version        | Bandwidth      | Available on |
| -------------- | -------------- | ------------ |
| **NVLink 3.0** | Up to 600 GB/s | A100 series  |
| **NVLink 4.0** | Up to 900 GB/s | H100 series  |
| **NVLink 5.0** | Up to 1.8 TB/s | B200 series  |

## Selecting GPUs by model size[​](#selecting-gpus-by-model-size "Direct link to Selecting GPUs by model size")

| Model size           | Recommended GPUs                         | Configuration                |
| -------------------- | ---------------------------------------- | ---------------------------- |
| **Small (≤10B)**     | One to two L4 or A10G                    | Single GPU or TP=2           |
| **Medium (10B-70B)** | Two to four A10G/L40S or one to two A100 | Tensor parallelism required  |
| **Large (70B-500B)** | Multiple A100/H100/H200                  | Multi-GPU tensor parallelism |
| **Extreme (500B+)**  | Multi-node H100/H200/B200                | TP + pipeline parallelism    |

### Selection criteria[​](#selection-criteria "Direct link to Selection criteria")

| Criterion                | Why it matters                                 | Recommendation                                |
| ------------------------ | ---------------------------------------------- | --------------------------------------------- |
| **Memory capacity**      | Must fit model weights, KV cache, and overhead | Calculate requirements before selection       |
| **Memory bandwidth**     | Determines token generation speed              | Higher bandwidth for latency-sensitive apps   |
| **Interconnect**         | Affects multi-GPU scaling                      | NVLink for best performance                   |
| **Quantization support** | Reduces memory requirements                    | Check GPU compatibility with target precision |

tip

Quantization can reduce memory requirements by 50% or more. See the [vLLM quantization hardware support guide](https://docs.vllm.ai/en/stable/features/quantization/#supported-hardware) for GPU compatibility.

## Parallelism strategies for multi-GPU deployments[​](#parallelism-strategies "Direct link to Parallelism strategies for multi-GPU deployments")

You can use parallelism to serve models that exceed single-GPU capacity. Understanding these strategies helps you balance performance and cost when you select GPU configurations.

### Tensor parallelism (TP)[​](#tensor-parallelism "Direct link to Tensor parallelism (TP)")

Tensor parallelism splits model layers horizontally across GPUs within a single node.

| Aspect           | Details                                                        |
| ---------------- | -------------------------------------------------------------- |
| *Configuration*  | Set `tensor_parallel_size` to number of GPUs (use powers of 2) |
| *Best for*       | Models that fit within single-node memory when split           |
| *Requirements*   | High-speed interconnect (NVLink preferred)                     |
| *Typical values* | 2, 4, 8 GPUs                                                   |

### Pipeline parallelism (PP)[​](#pipeline-parallelism "Direct link to Pipeline parallelism (PP)")

Pipeline parallelism splits model layers vertically across multiple nodes.

| Aspect          | Details                                         |
| --------------- | ----------------------------------------------- |
| *Configuration* | Set `pipeline_parallel_size` to number of nodes |
| *Best for*      | Models exceeding single-node capacity           |
| *Trade-offs*    | Higher latency due to inter-node communication  |
| *Use when*      | Model requires more than 8 GPUs                 |

### Multi-node configuration[​](#multi-node "Direct link to Multi-node configuration")

```
# Configuration for multi-node deployments
tensor_parallel_size = 8  # GPUs per node
pipeline_parallel_size = 2  # Number of nodes
total_gpus = tensor_parallel_size * pipeline_parallel_size  # 16 GPUs total
```

## Context window and memory requirements[​](#context-memory "Direct link to Context window and memory requirements")

The context window (maximum model length) determines how many tokens a model can process in a single pass. This parameter directly impacts memory usage through the KV cache.

warning

The model truncates tokens beyond the context limit, which causes it to "forget" earlier content. Choose your context length based on your actual use case requirements.

### Context window (max model length) by model family[​](#context-by-model "Direct link to Context window (max model length) by model family")

| Model series                   | Max context window |
| ------------------------------ | ------------------ |
| `Llama 2` (7B, 13B, 70B)       | 4k tokens          |
| `Llama 3` (8B, 70B)            | 8k tokens          |
| `Llama 3.1` (8B, 70B, 405B)    | 128k tokens        |
| `Llama 3.2` (1B, 3B, 11B, 90B) | 128k tokens        |
| `Llama 4 Scout` (109B)         | 10M tokens         |
| `Llama 4 Maverick` (400B)      | 1M tokens          |
| `Mistral 7B v0.1`              | 8k tokens          |
| `Mistral 7B v0.2/v0.3`         | 32k tokens         |
| `Mixtral 8x7B`                 | 32k tokens         |
| `Mixtral 8x22B`                | 64k tokens         |
| `Mistral Small 3`              | 32k tokens         |
| `Qwen 3` (0.6B/1.7B/4B)        | 32k tokens         |
| `Qwen 3` (8B/14B/32B/235B)     | 128k tokens        |
| `Qwen 2.5`                     | 32k tokens         |
| `Qwen 1M`                      | 1M tokens          |
| `Gemma`/`Gemma 2`/`CodeGemma`  | 8k tokens          |
| `Gemma 3`                      | 128k tokens        |

### Context length selection guide[​](#context-selection "Direct link to Context length selection guide")

| Use case                | Recommended length | Example applications                  |
| ----------------------- | ------------------ | ------------------------------------- |
| **Short tasks**         | 4k-8k tokens       | Q\&A, simple chat, code completion    |
| **Document processing** | 32k-128k tokens    | Analysis, summarization, reports      |
| **Multi-step agents**   | 128k+ tokens       | Complex reasoning, tool use           |
| **Ultra-long context**  | 1M+ tokens         | Book analysis, codebase understanding |

tip

Configure context length based on your actual usage patterns, not the maximum model capacity. This approach optimizes memory usage and reduces costs.

## Estimating GPU resources[​](#estimating "Direct link to Estimating GPU resources")

Use the following calculation method to precisely estimate GPU requirements and prevent OOM errors:

### Step 1: Calculate minimum GPUs[​](#step1 "Direct link to Step 1: Calculate minimum GPUs")

```
min_gpus = model_size_gb / gpu_memory_gb
```

### Step 2: Apply safety factor[​](#step2 "Direct link to Step 2: Apply safety factor")

```
tensor_parallel_size = 2 * min_gpus  # Round to nearest power of 2
```

note

**Why use a 2x safety factor?**

* It provides a margin for memory overhead
* It prevents OOM errors under peak load
* It provides headroom for batch processing
* It accommodates KV cache growth

### Step 3: Adjust for workload requirements[​](#step3 "Direct link to Step 3: Adjust for workload requirements")

The 2x safety factor provides a baseline. Consider these additional factors:

| Requirement          | Action                           | Reference                                                                           |
| -------------------- | -------------------------------- | ----------------------------------------------------------------------------------- |
| Long context windows | Increase GPU memory or count     | [Tune parameters for LLMs on Anyscale services](/llm/serving/parameter-tuning.md)   |
| High concurrency     | Add more replicas                | [Ray Serve Autoscaling](https://docs.ray.io/en/latest/serve/autoscaling-guide.html) |
| Dynamic scaling      | Configure autoscaling parameters | [Tune parameters for LLMs on Anyscale services](/llm/serving/parameter-tuning.md)   |

### Examples[​](#examples "Direct link to Examples")

#### Example 1: `Llama-3.1-8B-Instruct` (`BF16`)[​](#example-1-llama-31-8b-instruct-bf16 "Direct link to example-1-llama-31-8b-instruct-bf16")

* **Model size**: 16 GB

* **GPU**: `A10G` (24 GB), `g5.12xlarge` instance with 4× `A10G`

* **Calculation**: 16 GB ÷ 24 GB ≈ 1 × 2 = 2 `A10G` GPUs

* **Configuration**:

  <!-- -->

  * Set `tensor_parallel_size = 2`
  * On a `g5.12xlarge` instance (4× `A10G`), use `TP=2` and configure Ray Serve with 2 replicas

* **Notes**:

  <!-- -->

  * `TP=2` with 2 replicas outperforms `TP=4` on `A10G` because these GPUs lack NVLink. When you set `TP=2` instead of `TP=4`, you reduce communication overhead per token and scale more efficiently for many independent requests.
  * To minimize latency, consider using `TP=1` with an `L40S` (48 GB memory).

#### Example 2: `Llama-3.1-70B-Instruct` (`BF16`)[​](#example-2-llama-31-70b-instruct-bf16 "Direct link to example-2-llama-31-70b-instruct-bf16")

* **Model size**: 140 GB

* **GPU**: `H100` (80 GB), `p5.48xlarge` instance with 8× `H100`

* **Calculation**: 140 GB ÷ 80 GB = 1.75 → × 2 ≈ 4 `H100` GPUs

* **Configuration**:

  <!-- -->

  * Set `tensor_parallel_size = 4` (when `max_model_len` is between 2k—32k tokens).
  * **Small-batch, low-latency use cases**: Use `TP=4` with two replicas in Ray Serve for minimal latency.
  * **Large-batch, long-context, throughput-optimized**: Use `TP=8` with a single replica to support the full 128k context length. H100 NVLink helps mitigate the slight extra inter-GPU communication latency.

#### Example 3: `DeepSeek R1-670B` (`FP8`)[​](#example-3-deepseek-r1-670b-fp8 "Direct link to example-3-deepseek-r1-670b-fp8")

* **Model size**: 720 GB

* **GPU**: `H100` (80 GB), `p5.48xlarge` instance with 8× `H100`

* **Calculation**: 720 GB ÷ 80 GB = 9 → × 2 = 18 GPUs required

* **Configuration**:

  <!-- -->

  * Set `tensor_parallel_size = 8`
  * Set `pipeline_parallel_size = 2`
  * **Total GPUs**: 16 (close to the theoretical 18)
  * Deploy with `TP=8` and `PP=2`
