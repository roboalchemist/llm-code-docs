# Source: https://docs.anyscale.com/llm/serving/parameter-tuning.md

# Tune parameters for LLMs on Anyscale services

[View Markdown](/llm/serving/parameter-tuning.md)

# Tune parameters for LLMs on Anyscale services

This page helps you optimize vLLM and Ray Serve parameters for your specific workload requirements, including instructions for configuring memory management, inference optimization, and autoscaling for long context, high concurrency, or large model deployments.

## Memory management parameters in vLLM[​](#memory-management-parameters-in-vllm "Direct link to Memory management parameters in vLLM")

To deploy vLLM successfully, you must fit your model and KV cache within available GPU memory. Use these parameters to control memory allocation and performance optimization.

note

For complete vLLM engine parameter reference, see the [vLLM documentation](https://docs.vllm.ai/en/stable/configuration/engine_args.html#modelconfig).

For detailed memory calculations, see [Choose a GPU for LLM serving](/llm/serving/gpu-guidance.md).

| Parameter                | Description                                                                  | Best practices                                                                                                            |
| ------------------------ | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `tensor_parallel_size`   | Splits transformer layers across GPUs on same node (horizontal sharding)     | Set to the number of GPUs when your model exceeds single-GPU capacity. Requires high-speed interconnect.                  |
| `pipeline_parallel_size` | Vertically partitions model layers across nodes                              | Combine with `tensor_parallel_size` for models requiring >8 GPUs. Keep at `1` for single-node models.                     |
| `max_model_len`          | Maximum context length (prompt + generated tokens) for memory pre-allocation | Reduce for short-form tasks to save memory. Leave unset to use the model's native context window.                         |
| `gpu_memory_utilization` | Fraction (0.0-1.0) of GPU memory for model and KV cache                      | Default: `0.9`. Lower when you share GPU usage. Raise to `0.95` for more cache space.                                     |
| `max_num_seqs`           | Maximum concurrent sequences in active batch                                 | Upper limit only (no pre-allocation). Set slightly above your estimated concurrency. Avoid extreme values to prevent OOM. |

warning

`max_num_seqs` is an upper limit, not actual concurrency. vLLM determines the true concurrency dynamically based on available KV cache.

* **Too low** (one to two): Underutilizes GPU
* **Too high** (2000+): Causes OOM errors
* **Recommended**: 128-256 for most workloads

Check your deployment logs for actual concurrency values.

## Optimization scenarios[​](#optimization-scenarios "Direct link to Optimization scenarios")

### Scenario 1: Optimize for high concurrency[​](#scenario-1-optimize-for-high-concurrency "Direct link to Scenario 1: Optimize for high concurrency")

* **Goal:** Serve a large number of simultaneous users to maximize throughput.
* **Constraint:** You must support a large concurrency value.
* **Trade-offs:** To support many sequences, each one must consume as little memory as possible, which means you must limit context length. If you don't want to reduce the context length then you have to consider increasing the GPU memory pool or counts.

The following table explains which parameters to tune:

| Parameter                                           | Explanation                                                                                                                                                                                                                                                                                         |
| --------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `max_model_len`                                     | This is the most effective way to save memory. If your workload involves short Q\&A or chat, set a lower, realistic context length (for example, `1024` or `2048`) dramatically shrinks the memory footprint of each sequence. This allows more sequences to fit in a batch, increasing throughput. |
| `gpu_memory_utilization`                            | If your current concurrency is close to your target but just slightly under, consider increasing this value from the default `0.9` to `0.95`. This allocates more GPU memory for the KV cache, allowing you to support more concurrent sequences.                                                   |
| `tensor_parallel_size` and `pipeline_parallel_size` | If you need both high concurrency and a moderately long context, your only solution is to add more hardware. Using more GPUs increases the total memory available for the KV cache, accommodating more sequences.                                                                                   |

### Scenario 2: Load a very large model[​](#scenario-2-load-a-very-large-model "Direct link to Scenario 2: Load a very large model")

* **Goal:** Load a model that's too big for a single GPU.
* **Constraint:** The model weights themselves are the source of memory pressure, even before processing requests.
* **Trade-offs:** You must deploy more hardware. Tuning other parameters has no impact unless the cluster can load the model.

The following table explains which parameters to tune:

| Parameter                | Explanation                                                                                                                                    |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `tensor_parallel_size`   | Set to the number of available GPUs on the node (for example, `2`, `4`, `8`) to shard the model's layers.                                      |
| `pipeline_parallel_size` | For models that don't fit on a single 8-GPU node, you must also use pipeline parallelism to shard the model vertically across different nodes. |

### Scenario 3: Optimize for long context[​](#scenario-3-optimize-for-long-context "Direct link to Scenario 3: Optimize for long context")

* **Goal:** Process requests with very long context windows.
* **Constraint:** You can't significantly reduce `max_model_len`.
* **Trade-offs:** To support a few memory-heavy long sequences, you must choose between reducing concurrency or using more GPUs to increase the total memory available for the KV cache and accommodate longer sequences.

The following table explains which parameters to tune:

| Parameter                                           | Explanation                                                                                                                                                                                                                                                                     |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `gpu_memory_utilization`                            | If you are just short of supporting your desired context length, increase this value from the default `0.9` to `0.95`. This dedicates more GPU memory to the KV cache, enabling support for longer sequences.                                                                   |
| `tensor_parallel_size` and `pipeline_parallel_size` | If raising `gpu_memory_utilization` to `0.95` and lowering `max_num_seqs` to `1` still results in OOM errors, you must add more GPUs. Increase tensor parallelism or pipeline parallelism to expand the total GPU memory pool for the large KV cache required by long contexts. |

## Ray Serve autoscaling configuration[​](#ray-serve-autoscaling-configuration "Direct link to Ray Serve autoscaling configuration")

Autoscaling enables your deployment to dynamically adjust replicas based on traffic patterns, which optimizes performance and cost.

note

For detailed autoscaling documentation, see:

* [Ray Serve Autoscaling Guide](https://docs.ray.io/en/latest/serve/autoscaling-guide.html)
* Ray's [Advanced Autoscaling Guide](https://docs.ray.io/en/latest/serve/advanced-guides/advanced-autoscaling.html#serve-advanced-autoscaling)

### Replica count limits[​](#replica-count-limits "Direct link to Replica count limits")

| Parameter      | Description           | Best practices                                                                              |
| -------------- | --------------------- | ------------------------------------------------------------------------------------------- |
| `min_replicas` | Minimum replica count | Set to `0` for cost optimization (with cold-start trade-off). Set to `>0` for warm standby. |
| `max_replicas` | Maximum replica count | Must exceed `min_replicas`. Size for peak traffic plus headroom. Verify cluster capacity.   |

### Steady-state targets[​](#steady-state-targets "Direct link to Steady-state targets")

| Parameter                 | Description                            | Best practices                                                                                        |
| ------------------------- | -------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `max_ongoing_requests`    | Maximum in-flight requests per replica | Set equal to `max_num_seqs`. Keep 20—50% above `target_ongoing_requests`                              |
| `target_ongoing_requests` | Target average in-flight requests      | Lower for latency-sensitive apps. Raise for throughput-oriented workloads. Validate with load testing |

note

By default, Ray Serve LLM may set `max_ongoing_requests` and `target_ongoing_requests` to very large numbers (for example, `1e9`). Use the following guidelines to set appropriate values for effective autoscaling:

1. **Find max concurrency**: When you deploy, check the logs for the maximum concurrency supported by the KV cache

   * For example, with context length 8192, logs might show a max concurrency of \~47.

2. **Estimate effective batch size**: Based on your average request token length, calculate the number of requests that can be handled concurrently.

   * For example, if the model supports 47 sequences at 8192 tokens each, but your average input request is \~1000 tokens, the effective batch size is approximately (8192 / 1000) \* 47 ≈ 385 requests.

3. **Set hard caps**: Set the `max_num_seqs` parameter in vLLM and the `max_ongoing_requests` parameter in Ray Serve to the calculated value.

   * For example, 385.

4. **Set autoscaling target**: Set `target_ongoing_requests` to be 20-50% lower than the hard cap to provide a buffer for scaling.

   * For example, 300.

5. **Observe and adjust**: Monitor your application's autoscaling behavior under load and fine-tune these parameters to meet your performance and cost requirements.

### Traffic reaction parameters[​](#traffic-reaction-parameters "Direct link to Traffic reaction parameters")

| Parameter            | Description                               | Best practices                                                     |
| -------------------- | ----------------------------------------- | ------------------------------------------------------------------ |
| `upscale_delay_s`    | Delay before scaling up (default: 30s)    | Lower for faster burst response (might cause oscillations).        |
| `downscale_delay_s`  | Delay before scaling down (default: 600s) | Raise to maintain warm capacity. Lower to prioritize cost savings. |
| `upscaling_factor`   | Scale-up multiplier (default: 1.0)        | `>1` for aggressive scaling, `<1` for conservative.                |
| `downscaling_factor` | Scale-down multiplier (default: 1.0)      | `<1` for gentle downscaling, `>1` for aggressive cost reduction.   |
| `metrics_interval_s` | Metric reporting frequency (default: 10s) | Keep ≤ delay values. Lower for tighter control.                    |
| `look_back_period_s` | Averaging window (default: 30s)           | Shorter for bursty workloads, longer for smoothing.                |

## Troubleshooting common autoscaling issues[​](#troubleshooting-common-autoscaling-issues "Direct link to Troubleshooting common autoscaling issues")

| Issue                            | Solution                                                                                                |
| -------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Replica oscillation**          | Reduce `upscaling_factor` and `downscaling_factor`. Match `look_back_period_s` to your delay settings.  |
| **Latency spikes during bursts** | Reduce `upscale_delay_s`, increase `upscaling_factor`, ensure `metrics_interval_s` ≤ `upscale_delay_s`. |
| **Premature scale-down**         | Increase `downscale_delay_s`, reduce `downscaling_factor` for gentler scaling.                          |
