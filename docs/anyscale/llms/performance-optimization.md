# Source: https://docs.anyscale.com/llm/serving/performance-optimization.md

# Optimize performance for Ray Serve LLM

[View Markdown](/llm/serving/performance-optimization.md)

# Optimize performance for Ray Serve LLM

This guide provides comprehensive optimization techniques for Ray Serve LLM. It explores fundamental performance bottlenecks—from compute to memory bandwidth—and discusses actionable strategies such as quantization, parallelism, and additional features to build a fast, scalable, and cost-effective LLM service.

## Understand critical performance bottlenecks in LLM serving[​](#bottlenecks "Direct link to Understand critical performance bottlenecks in LLM serving")

Optimizing Large Language Model (LLM) inference performance requires understanding the key bottlenecks that govern speed and efficiency. These bottlenecks occur in distinct phases of the generation process.

### Memory-size-bound[​](#memory-size-bound "Direct link to Memory-size-bound")

This limitation occurs when you want to deploy a large LLM or serve requests with extremely long context sizes, and the model weights, KV cache, and other tensors exceed the available GPU memory capacity.

* The primary bottleneck is the total GPU memory capacity.
* This forces the use of model parallelism (sharding the model across multiple GPUs with Tensor or Pipeline Parallelism), which introduces communication overhead.
* To optimize, use GPUs with larger memory to fit larger models and longer contexts on a single device. When sharding is necessary, high-speed interconnects become critical.

### Compute-bound (prefill phase)[​](#compute-bound "Direct link to Compute-bound (prefill phase)")

The prefill phase occurs when the LLM processes the input prompt. This involves large, parallel matrix-multiply operations that saturate the GPU's CUDA or Tensor Cores.

* The bottleneck is the raw computational throughput, measured in teraFLOPs.
* This phase determines the Time-to-first-token (TTFT).
* To optimize, use GPUs with higher teraflops to accelerate this initial processing step.

### Memory-bandwidth-bound (decode phase)[​](#memory-bandwidth-bound "Direct link to Memory-bandwidth-bound (decode phase)")

The decode phase involves the LLM generating subsequent tokens one by one. For each new token, the model must read the Key-Value (KV) cache from the GPU's high-bandwidth memory (HBM) and then write the new token's K/V vectors back to HBM. Methods such as PagedAttention optimize memory layout, but the phase remains bandwidth-limited.

* The bottleneck is the GPU memory bandwidth (measured in TB/s).
* This phase determines the inter-token latency (ITL), or the time between generated tokens. As the context grows, so does the KV cache, making this bottleneck more pronounced.
* To optimize, select GPUs with higher memory bandwidth (for example, Nvidia H100's 3.35 TB/s versus A100's 2.0 TB/s).

### Inter-GPU communication[​](#inter-gpu-communication "Direct link to Inter-GPU communication")

This bottleneck becomes a factor only when you use multi-GPU model parallelism (Tensor or Pipeline Parallelism).

* The bottleneck is the bandwidth of the GPU interconnect.
* High communication overhead between GPUs can significantly increase per-token latency, negating the benefits of distributed processing.
* To optimize, use GPU clusters with high-speed interconnects such as NVLink (for Nvidia GPUs) or Infinity Fabric (for AMD GPUs), which offer much higher bandwidth than standard PCIe connections.

## Core optimization strategies with GPUs[​](#gpu-strategies "Direct link to Core optimization strategies with GPUs")

A successful optimization strategy addresses these bottlenecks in a logical order.

Most workloads must first clear memory-size feasibility. The model and KV cache must fit. Once they fit on the target hardware, they're typically compute-bound (prefill), then become memory-bandwidth-bound (decode).

Follow this practical strategy to optimize performance with GPUs:

1. **Manage memory footprint**: Employ quantization to fit the model on fewer GPUs.

2. **Accelerate prefill**: Use GPUs with high teraflops to minimize TTFT.

3. **Accelerate decode**: Choose GPUs with the highest possible memory bandwidth to minimize ITL.

4. **Optimize parallelism**:

   <!-- -->

   * If multi-GPU is unavoidable, ensure you use high-speed NVLink interconnects.
   * Avoid over-sharding a model across many GPUs, especially over slower network links (for example, across different nodes), as the communication overhead can overwhelm any computational gains.

For more details, see [Choose a GPU for LLM serving](/llm/serving/gpu-guidance.md).

### Optimize LLM performance with quantization[​](#quantization "Direct link to Optimize LLM performance with quantization")

Quantization reduces the numerical precision of a model's weights, for example, by converting them from a 16-bit floating-point format to an 8-bit format. This technique significantly shrinks a model's memory footprint and can lead to major performance improvements.

Quantization provides several key advantages:

* **Reduced memory usage**: Allows larger models to run on fewer GPUs.
* **Faster inference speed**: Computations with lower-precision numbers are often quicker.
* **Increased throughput**: Enables the model to handle more requests simultaneously.

For instance, you can run an LLM originally released in BF16 format, such as [Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) (\~140 GB), at lower precision. An FP8 quantized version, such as [Llama-3.3-70B-Instruct-FP8-Dynamic](https://huggingface.co/cortecs/Llama-3.3-70B-Instruct-FP8-Dynamic), halves the memory requirement to approximately 70 GB while retaining 99% of the original model's benchmark performance.

note

Some models are released in a pre-quantized state. For example, some models from DeepSeek are available in 8-bit precision, while certain open source models from OpenAI use 4-bit.

When choosing any quantization method, evaluate the potential impact on model quality and confirm your GPU hardware is compatible.

For more details, see the vLLM documentation on [Quantization](https://docs.vllm.ai/en/stable/features/quantization/index.html) methods and supported hardware.

## Scale with parallelism[​](#parallelism "Direct link to Scale with parallelism")

Parallelism techniques distribute the workload across multiple GPUs to either serve larger models or handle more requests.

### Tensor and pipeline parallelism[​](#tensor-pipeline-parallelism "Direct link to Tensor and pipeline parallelism")

vLLM uses model parallelism techniques when a model is too large to fit on a single GPU.

* **Tensor Parallelism**: Splits individual layers of the model across multiple GPUs. It requires very high-speed interconnects (such as NVLink) as GPUs must synchronize frequently.
* **Pipeline Parallelism**: Splits model into stages, forming a pipeline that vLLM can split across devices or nodes. This reduces communication frequency compared to TP, but can suffer from "bubbles" where some GPUs are idle.

These strategies are necessary for memory-size-bound models but introduce inter-GPU communication overhead, making hardware choice critical. vLLM automatically manages this when you specify `tensor_parallel_size > 1`.

For detailed guidance on tuning vLLM parameters for memory management, see [Tune parameters for LLMs on Anyscale services](/llm/serving/parameter-tuning.md).

### Data parallel and expert parallel deployment for MoE LLMs[​](#moe-deployment "Direct link to Data parallel and expert parallel deployment for MoE LLMs")

Mixture-of-Experts (MoE) models replace the single feed-forward neural network (FFN) layer found in dense models with multiple parallel FFN layers, known as "experts." When the system processes input tokens, a router layer dynamically selects the top-k experts for each token, dispatching the token's hidden state to those chosen experts.

When serving MoE models, combining Expert Parallelism (EP) with Data Parallelism (DP) is an effective way to maximize throughput and efficiency. As described in the [vLLM Expert parallel deployment documentation](https://docs.vllm.ai/en/stable/serving/expert_parallel_deployment.html#expert-parallel-deployment), EP places distinct expert layers on separate GPUs so each expert executes locally. Use EP together with DP—outlined in the [vLLM Data parallel deployment guide](https://docs.vllm.ai/en/stable/serving/data_parallel_deployment.html)—as an effective way to maximize locality and throughput.

note

When using DP and EP, the system replicates attention (dense) weights across all GPUs by `DP_SIZE`, while expert weights split across GPUs, `EP_SIZE = DP_SIZE x TP_SIZE`. So increasing DP increases the number of shards for the experts, not copies.

For MoE models in an EP deployment, DP ranks must advance in lockstep: whenever any rank has requests in flight, ranks without scheduled work perform lightweight "dummy" forward passes. A dedicated DP Coordinator process orchestrates this behavior and runs a collective verification every N steps to determine when all ranks are idle and can pause. When tensor parallelism (TP) runs alongside DP, each expert can also distribute across TP ranks, so the communication group for an expert spans (DP × TP) ranks.

In all cases, load-balancing requests across DP ranks is beneficial. For online deployments, MoE can optimize routing by considering each DP engine's live state—its scheduled and queued requests and its prefix cache contents. Because prefix caches are independent per DP engine, directing similar or repeated prompts to the same engine maximizes cache hits and improves both latency and throughput.

## Accelerate model loading from S3 storage[​](#model-initialization "Direct link to Accelerate model loading from S3 storage")

Model loading time can become a significant bottleneck, especially for large models that require downloading weights from remote storage or loading sharded models across multiple GPUs. Ray Serve LLM supports streaming model weights directly from S3 to GPU memory with RunAI, significantly reducing model load latency. For strategies to reduce replica startup times, see [Deployment initialization](https://docs.ray.io/en/latest/serve/llm/user-guides/deployment-initialization.html). For benchmark data on startup latency, see [Replica startup latency benchmarks](https://docs.ray.io/en/latest/serve/llm/benchmarks.html#replica-startup-latency).

For large models, you can combine model weights streaming with model sharding using tensor parallelism. By pre-sharding model weights and storing them in S3, each GPU can load only its required shard directly, avoiding the overhead of loading the entire model and then distributing it. See [Ray Serve LLM: Model Sharding](https://docs.ray.io/en/latest/serve/llm/user-guides/deployment-initialization.html#model-sharding)

For more details about tuning RunAI in inference engine, see the [vLLM documentation](https://docs.vllm.ai/en/stable/models/extensions/runai_model_streamer/). You can forward engine-level parameters through the `engine_kwargs` argument of your `LLMConfig`.

## Additional features for latency and throughput optimization[​](#additional-features "Direct link to Additional features for latency and throughput optimization")

To further optimize latency and throughput, consider the following features:

### Fractional GPU allocation[​](#fractional-gpu "Direct link to Fractional GPU allocation")

Fractional GPU allocation enables running multiple model replicas on a single GPU by customizing placement groups. Instead of dedicating an entire GPU to one replica, the same physical GPU can be split across multiple LLM replicas. This approach maximizes GPU utilization and reduces infrastructure costs by serving more replicas with fewer GPUs.

Use fractional GPU allocation when your models are small enough that they don't require a full GPU for model weights and KV cache, and your workload has low to moderate concurrency that doesn't saturate a single replica. This works best with fixed replica counts rather than autoscaling, and requires careful memory management to prevent out-of-memory errors.

For detailed configuration instructions, deployment examples, and troubleshooting guidance, see the [Ray Serve LLM fractional GPU documentation](https://docs.ray.io/en/latest/serve/llm/user-guides/fractional-gpu.html).

### Automatic prefix caching[​](#prefix-caching "Direct link to Automatic prefix caching")

Prefix caching automatically stores the KV cache of completed requests in a global, on-GPU cache. If a new request arrives with a prompt that shares a common prefix (for example, a system prompt) with a cached entry, vLLM can reuse the cached state instead of recomputing it. This significantly reduces latency (TTFT) and compute load for applications with repetitive prompts, such as chatbots with fixed system instructions or RAG systems. It's enabled by default in vLLM. Disable it to simplify benchmarking by setting `enable_prefix_caching=False` in the vLLM engine arguments.

### Prefix cache-aware router[​](#cache-aware-router "Direct link to Prefix cache-aware router")

The `PrefixCacheAffinityRouter` is a specialized request router for Ray Serve LLM deployments. Its purpose is to route requests with similar input prefixes—such as identical system prompts or shared headers—to the same replica. This increases the likelihood that the engine's KV (prefix) cache can be reused, significantly improving throughput for workloads where many requests share long prefixes. This approach can yield more than a 2.5x throughput improvement for scenarios such as summarization or chat applications with multiple system prompts.

vLLM's Automatic Prefix Caching (APC) stores KV cache blocks from previous requests and reuses them when a new request has the same string prefix. vLLM uses block hashing and string-matching heuristics (not only exact token-ID matches) for robust cache hits. The `PrefixCacheAffinityRouter` further increases cache effectiveness by directing similar requests to the same engine replica, maximizing the chance that relevant cache blocks are already present. Under load skew, it automatically falls back to standard power-of-two-choices routing to redistribute load.

For more information, see [PrefixCacheAffinityRouter for LLM inference optimization](https://docs.ray.io/en/latest/serve/llm/prefix-aware-request-router.html).

### Chunked prefill[​](#chunked-prefill "Direct link to Chunked prefill")

Without chunked prefill, vLLM's scheduler can pause ongoing decode requests to process a newly arrived, large prefill request. Chunked prefill alters this behavior by breaking down large prefill tasks into smaller "chunks." This allows the scheduler to interleave prefill chunks with decode steps, preventing decode requests from stalling. vLLM enables this feature by default.

It improves ITL and fairness by ensuring that ongoing generations remain smooth and responsive, even when new, long prompts are submitted. It also improves GPU utilization by creating a better mix of compute-bound (prefill) and memory-bound (decode) operations.

In vLLM V1, chunked prefill is always enabled by default. The key parameter to tune is `max_num_batched_tokens`:

* A **lower** value prioritizes decode more heavily, improving ITL.
* A **higher** value (greater than 2048) allows more prefill work per batch, improving TTFT and overall throughput.

For more information, see the [vLLM Chunked Prefill](https://docs.vllm.ai/en/stable/configuration/optimization.html#chunked-prefill_1) documentation.

### Speculative decoding[​](#speculative-decoding "Direct link to Speculative decoding")

Speculative decoding accelerates inference by using a smaller, faster draft model to propose multiple candidate tokens in parallel. The main model then validates these proposals in a single forward pass, accepting correct predictions and rejecting incorrect ones. This approach maintains the same output quality as standard decoding while significantly reducing latency and improving throughput.

vLLM supports multiple speculative decoding methods, including draft models, n-gram matching, suffix decoding, MLP speculators, and EAGLE-based models. Each method trades off implementation complexity and speedup potential differently. Speculative decoding works best for latency-sensitive applications where the draft model is significantly faster than the main model and there's high agreement between the draft and target models.

For detailed configuration options, supported methods, implementation details, and current limitations, see the [vLLM Speculative Decoding documentation](https://docs.vllm.ai/en/stable/features/spec_decode/).

### Prefill and decode disaggregation[​](#prefill-decode-disaggregation "Direct link to Prefill and decode disaggregation")

This advanced strategy splits the workload across two separate vLLM engines: one dedicated to prefill and another dedicated to decode. The prefill engine computes KV cache blocks for incoming prompts and transfers them to the decode engine, which then generates subsequent tokens.

It physically isolates the compute-intensive prefill phase from the memory-bound decode phase. This prevents large prefill jobs from causing latency spikes (ITL) for active decode requests, leading to better service level objective attainment and a smoother user experience.

For more information, see [Prefill and Decode Disaggregation with KV Transfer Backends](https://docs.ray.io/en/latest/serve/llm/pd-dissagregation.html).
