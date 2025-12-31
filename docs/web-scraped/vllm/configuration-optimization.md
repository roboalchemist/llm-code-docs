# Source: https://docs.vllm.ai/en/stable/configuration/optimization/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/configuration/optimization.md "Edit this page")

# Optimization and Tuning[¶](#optimization-and-tuning "Permanent link")

This guide covers optimization strategies and performance tuning for vLLM V1.

Tip

Running out of memory? Consult [this guide](../conserving_memory/) on how to conserve memory.

## Preemption[¶](#preemption "Permanent link")

Due to the autoregressive nature of transformer architecture, there are times when KV cache space is insufficient to handle all batched requests. In such cases, vLLM can preempt requests to free up KV cache space for other requests. Preempted requests are recomputed when sufficient KV cache space becomes available again. When this occurs, you may see the following warning:

    WARNING 05-09 00:49:33 scheduler.py:1057 Sequence group 0 is preempted by PreemptionMode.RECOMPUTE mode because there is not enough KV cache space. This can affect the end-to-end performance. Increase gpu_memory_utilization or tensor_parallel_size to provide more KV cache memory. total_cumulative_preemption_cnt=1

While this mechanism ensures system robustness, preemption and recomputation can adversely affect end-to-end latency. If you frequently encounter preemptions, consider the following actions:

-   Increase `gpu_memory_utilization`. vLLM pre-allocates GPU cache using this percentage of memory. By increasing utilization, you can provide more KV cache space.
-   Decrease `max_num_seqs` or `max_num_batched_tokens`. This reduces the number of concurrent requests in a batch, thereby requiring less KV cache space.
-   Increase `tensor_parallel_size`. This shards model weights across GPUs, allowing each GPU to have more memory available for KV cache. However, increasing this value may cause excessive synchronization overhead.
-   Increase `pipeline_parallel_size`. This distributes model layers across GPUs, reducing the memory needed for model weights on each GPU, indirectly leaving more memory available for KV cache. However, increasing this value may cause latency penalties.

You can monitor the number of preemption requests through Prometheus metrics exposed by vLLM. Additionally, you can log the cumulative number of preemption requests by setting `disable_log_stats=False`.

In vLLM V1, the default preemption mode is `RECOMPUTE` rather than `SWAP`, as recomputation has lower overhead in the V1 architecture.

## Chunked Prefill[¶](#chunked-prefill "Permanent link")

Chunked prefill allows vLLM to process large prefills in smaller chunks and batch them together with decode requests. This feature helps improve both throughput and latency by better balancing compute-bound (prefill) and memory-bound (decode) operations.

In V1, **chunked prefill is enabled by default whenever possible**. With chunked prefill enabled, the scheduling policy prioritizes decode requests. It batches all pending decode requests before scheduling any prefill operations. When there are available tokens in the `max_num_batched_tokens` budget, it schedules pending prefills. If a pending prefill request cannot fit into `max_num_batched_tokens`, it automatically chunks it.

This policy has two benefits:

-   It improves ITL and generation decode because decode requests are prioritized.
-   It helps achieve better GPU utilization by locating compute-bound (prefill) and memory-bound (decode) requests to the same batch.

### Performance Tuning with Chunked Prefill[¶](#performance-tuning-with-chunked-prefill "Permanent link")

You can tune the performance by adjusting `max_num_batched_tokens`:

-   Smaller values (e.g., 2048) achieve better inter-token latency (ITL) because there are fewer prefills slowing down decodes.
-   Higher values achieve better time to first token (TTFT) as you can process more prefill tokens in a batch.
-   For optimal throughput, we recommend setting `max_num_batched_tokens > 8192` especially for smaller models on large GPUs.
-   If `max_num_batched_tokens` is the same as `max_model_len`, that\'s almost the equivalent to the V0 default scheduling policy (except that it still prioritizes decodes).

    from vllm import LLM

    # Set max_num_batched_tokens to tune performance
    llm = LLM(model="meta-llama/Llama-3.1-8B-Instruct", max_num_batched_tokens=16384)

See related papers for more details (<https://arxiv.org/pdf/2401.08671> or <https://arxiv.org/pdf/2308.16369>).

## Parallelism Strategies[¶](#parallelism-strategies "Permanent link")

vLLM supports multiple parallelism strategies that can be combined to optimize performance across different hardware configurations.

### Tensor Parallelism (TP)[¶](#tensor-parallelism-tp "Permanent link")

Tensor parallelism shards model parameters across multiple GPUs within each model layer. This is the most common strategy for large model inference within a single node.

**When to use:**

-   When the model is too large to fit on a single GPU
-   When you need to reduce memory pressure per GPU to allow more KV cache space for higher throughput

    from vllm import LLM

    # Split model across 4 GPUs
    llm = LLM(model="meta-llama/Llama-3.3-70B-Instruct", tensor_parallel_size=4)

For models that are too large to fit on a single GPU (like 70B parameter models), tensor parallelism is essential.

### Pipeline Parallelism (PP)[¶](#pipeline-parallelism-pp "Permanent link")

Pipeline parallelism distributes model layers across multiple GPUs. Each GPU processes different parts of the model in sequence.

**When to use:**

-   When you\'ve already maxed out efficient tensor parallelism but need to distribute the model further, or across nodes
-   For very deep and narrow models where layer distribution is more efficient than tensor sharding

Pipeline parallelism can be combined with tensor parallelism for very large models:

    from vllm import LLM

    # Combine pipeline and tensor parallelism
    llm = LLM(
        model="meta-llama/Llama-3.3-70B-Instruct,
        tensor_parallel_size=4,
        pipeline_parallel_size=2,
    )

### Expert Parallelism (EP)[¶](#expert-parallelism-ep "Permanent link")

Expert parallelism is a specialized form of parallelism for Mixture of Experts (MoE) models, where different expert networks are distributed across GPUs.

**When to use:**

-   Specifically for MoE models (like DeepSeekV3, Qwen3MoE, Llama-4)
-   When you want to balance the expert computation load across GPUs

Expert parallelism is enabled by setting `enable_expert_parallel=True`, which will use expert parallelism instead of tensor parallelism for MoE layers. It will use the same degree of parallelism as what you have set for tensor parallelism.

### Data Parallelism (DP)[¶](#data-parallelism-dp "Permanent link")

Data parallelism replicates the entire model across multiple GPU sets and processes different batches of requests in parallel.

**When to use:**

-   When you have enough GPUs to replicate the entire model
-   When you need to scale throughput rather than model size
-   In multi-user environments where isolation between request batches is beneficial

Data parallelism can be combined with the other parallelism strategies and is set by `data_parallel_size=N`. Note that MoE layers will be sharded according to the product of the tensor parallel size and data parallel size.

### Batch-level DP for Multi-Modal Encoders[¶](#batch-level-dp-for-multi-modal-encoders "Permanent link")

By default, TP is used to shard the weights of multi-modal encoders just like for language decoders, in order to reduce the memory and compute load on each GPU.

However, since the size of multi-modal encoders is very small compared to language decoders, there is relatively little gain from TP. On the other hand, TP incurs significant communication overhead because of all-reduce being performed after every layer.

Given this, it may be advantageous to instead shard the batched input data using TP, essentially performing batch-level DP. This has been shown to improve the throughput and TTFT by around 10% for `tensor_parallel_size=8`. For vision encoders that use hardware-unoptimized Conv3D operations, batch-level DP can provide another 40% improvement compared to regular TP.

Nevertheless, since the weights of the multi-modal encoder are replicated across each TP rank, there will be a minor increase in memory consumption and may cause OOM if you can barely fit the model already.

You can enable batch-level DP by setting `mm_encoder_tp_mode="data"`, for example:

    from vllm import LLM

    llm = LLM(
        model="Qwen/Qwen2.5-VL-72B-Instruct",
        tensor_parallel_size=4,
        # When mm_encoder_tp_mode="data",
        # the vision encoder uses TP=4 (not DP=1) to shard the input data,
        # so the TP size becomes the effective DP size.
        # Note that this is independent of the DP size for language decoder which is used in expert parallel setting.
        mm_encoder_tp_mode="data",
        # The language decoder uses TP=4 to shard the weights regardless
        # of the setting of mm_encoder_tp_mode
    )

Important

Batch-level DP is not to be confused with API request-level DP (which is instead controlled by `data_parallel_size`).

Batch-level DP needs to be implemented on a per-model basis, and enabled by setting `supports_encoder_tp_data = True` in the model class. Regardless, you need to set `mm_encoder_tp_mode="data"` in engine arguments to use this feature.

Known supported models (with corresponding benchmarks):

-   dots_ocr ([[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] Pull Request #25466](https://github.com/vllm-project/vllm/pull/25466))
-   GLM-4.1V or above ([[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] Pull Request #23168](https://github.com/vllm-project/vllm/pull/23168))
-   InternVL ([[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] Pull Request #23909](https://github.com/vllm-project/vllm/pull/23909))
-   Kimi-VL ([[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] Pull Request #23817](https://github.com/vllm-project/vllm/pull/23817))
-   Llama4 ([[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] Pull Request #18368](https://github.com/vllm-project/vllm/pull/18368))
-   MiniCPM-V-2.5 or above ([[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] Pull Request #23327](https://github.com/vllm-project/vllm/pull/23327), [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] Pull Request #23948](https://github.com/vllm-project/vllm/pull/23948))
-   Qwen2-VL or above ([[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] Pull Request #22742](https://github.com/vllm-project/vllm/pull/22742), [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] Pull Request #24955](https://github.com/vllm-project/vllm/pull/24955), [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] Pull Request #25445](https://github.com/vllm-project/vllm/pull/25445))
-   Step3 ([[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] Pull Request #22697](https://github.com/vllm-project/vllm/pull/22697))

## Input Processing[¶](#input-processing "Permanent link")

### Parallel Processing[¶](#parallel-processing "Permanent link")

You can run input processing in parallel via [API server scale-out](../../serving/data_parallel_deployment/#internal-load-balancing). This is useful when input processing (which is run inside the API server) becomes a bottleneck compared to model execution (which is run inside engine core) and you have excess CPU capacity.

    # Run 4 API processes and 1 engine core process
    vllm serve Qwen/Qwen2.5-VL-3B-Instruct --api-server-count 4

    # Run 4 API processes and 2 engine core processes
    vllm serve Qwen/Qwen2.5-VL-3B-Instruct --api-server-count 4 -dp 2

Note

API server scale-out is only available for online inference.

Warning

By default, 8 CPU threads are used in each API server to load media items (e.g. images) from request data.

If you apply API server scale-out, consider adjusting `VLLM_MEDIA_LOADING_THREAD_COUNT` to avoid CPU resource exhaustion.

Note

API server scale-out disables [multi-modal IPC caching](#ipc-caching) because it requires a one-to-one correspondence between API and engine core processes.

This does not impact [multi-modal processor caching](#processor-caching).

## Multi-Modal Caching[¶](#multi-modal-caching "Permanent link")

Multi-modal caching avoids repeated transfer or processing of the same multi-modal data, which commonly occurs in multi-turn conversations.

### Processor Caching[¶](#processor-caching "Permanent link")

Multi-modal processor caching is automatically enabled to avoid repeatedly processing the same multi-modal inputs in `BaseMultiModalProcessor`.

### IPC Caching[¶](#ipc-caching "Permanent link")

Multi-modal IPC caching is automatically enabled when there is a one-to-one correspondence between API (`P0`) and engine core (`P1`) processes, to avoid repeatedly transferring the same multi-modal inputs between them.

#### Key-Replicated Cache[¶](#key-replicated-cache "Permanent link")

By default, IPC caching uses a **key-replicated cache**, where cache keys exist in both the API (`P0`) and engine core (`P1`) processes, but the actual cache data resides only in `P1`.

#### Shared Memory Cache[¶](#shared-memory-cache "Permanent link")

When multiple worker processes are involved (e.g., when TP \> 1), a **shared-memory cache** is more efficient. This can be enabled by setting `mm_processor_cache_type="shm"`. In this mode, cache keys are stored on `P0`, while the cache data itself lives in shared memory accessible by all processes.

### Configuration[¶](#configuration "Permanent link")

You can adjust the size of the cache by setting the value of `mm_processor_cache_gb` (default 4 GiB).

If you do not benefit much from the cache, you can disable both IPC and processor caching completely via `mm_processor_cache_gb=0`.

Examples:

    # Use a larger cache
    llm = LLM(
        model="Qwen/Qwen2.5-VL-3B-Instruct",
        mm_processor_cache_gb=8,
    )

    # Use a shared-memory based IPC cache
    llm = LLM(
        model="Qwen/Qwen2.5-VL-3B-Instruct",
        tensor_parallel_size=2,
        mm_processor_cache_type="shm",
        mm_processor_cache_gb=8,
    )

    # Disable the cache
    llm = LLM(
        model="Qwen/Qwen2.5-VL-3B-Instruct",
        mm_processor_cache_gb=0,
    )

### Cache Placement[¶](#cache-placement "Permanent link")

Based on the configuration, the content of the multi-modal caches on `P0` and `P1` are as follows:

  mm_processor_cache_type   Cache Type               `P0` Cache   `P1` Engine Cache   `P1` Worker Cache   Max. Memory
  ------------------------- ------------------------ ------------ ------------------- ------------------- ----------------------------------------------
  lru                       Processor Caching        K + V        N/A                 N/A                 `mm_processor_cache_gb * data_parallel_size`
  lru                       Key-Replicated Caching   K            K + V               N/A                 `mm_processor_cache_gb * api_server_count`
  shm                       Shared Memory Caching    K            N/A                 V                   `mm_processor_cache_gb * api_server_count`
  N/A                       Disabled                 N/A          N/A                 N/A                 `0`

K: Stores the hashes of multi-modal items\
V: Stores the processed tensor data of multi-modal items

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [December 14, 2025] ]