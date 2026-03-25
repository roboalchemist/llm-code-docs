# Source: https://docs.anyscale.com/llm/batch-inference/resource-allocation/cost-performance.md

# Cost and performance for Ray Data LLM batch inference

[View Markdown](/llm/batch-inference/resource-allocation/cost-performance.md)

# Cost and performance for Ray Data LLM batch inference

This guide helps you understand cost implications when configuring Ray Data LLM batch inference. Understanding the trade-offs between GPU types, parallelism strategies, and memory configurations helps you balance your budget against performance requirements.

## GPU costs and selection[​](#gpu-costs "Direct link to GPU costs and selection")

Different GPUs have different price-performance characteristics. Approximate relative monthly costs for 1 GPU vary by region and provider:

| GPU type  | Relative cost | Memory | Best for                         |
| --------- | ------------- | ------ | -------------------------------- |
| T4        | 1× (baseline) | 16 GB  | Small models, budget constrained |
| L4        | 1.5-2×        | 24 GB  | 7-13B models, cost-effective     |
| A10G      | 2-2.5×        | 24 GB  | 7-13B models, good availability  |
| L40S      | 4-5×          | 48 GB  | 13-70B models, sweet spot        |
| A100-40GB | 4-5×          | 40 GB  | 13-30B models, fast inference    |
| A100-80GB | 7-8×          | 80 GB  | 30-70B models, long context      |
| H100      | 10-12×        | 80 GB  | 70-200B models, premium          |
| H200      | 12-15×        | 141 GB | 100B+ models, ultra-long context |

The GPU with the lowest absolute cost isn't always most cost-efficient. A more expensive GPU with faster processing time may be more cost-effective per token.

For detailed GPU specifications, see [GPU specifications comparison](/llm/serving/gpu-guidance.md#gpu-specifications-comparison).

## Parallelism and cost implications[​](#parallelism-cost "Direct link to Parallelism and cost implications")

Data parallelism involves distributing work across multiple independent inference workers, and the cost scales linearly with the number of concurrent workers. This approach works best for small to medium models that fit comfortably on a single GPU.

Model parallelism typically involves using more premium hardware with high-bandwidth interconnects to enable fast communication, increasing the cost per inference worker. For guidance on setting up model parallelism, see [Model parallelism](/llm/batch-inference/ray-data-llm.md#model-parallelism) and for guidance on selecting the right GPUs, see [NVLink interconnect specifications](/llm/serving/gpu-guidance.md#nvlink-interconnect-specifications).

This example shows a configuration that incurs the cost of 32 H100 GPUs per hour:

```
config = vLLMEngineProcessorConfig(
    model_source="deepseek-ai/DeepSeek-R1",
    accelerator_type="H100",
    engine_kwargs={
        "tensor_parallel_size": 8,  # 8 GPUs per node
        "pipeline_parallel_size": 2,  # Split across 2 nodes
        "distributed_executor_backend": "ray", # Required to enable cross-node parallelism
    },
    concurrency=2, # 2 independent workers
)
# Cost: 2x8x2= 32 H100 GPU hourly cost
```

Scaling your batch inference workload with parallelism affects both completion time and cost. Doubling compute resources roughly doubles GPU cost per hour but might halve job duration. This could keep total cost similar while delivering results faster.

## Cost estimation process[​](#cost-estimation "Direct link to Cost estimation process")

Run a sample of your dataset with a single GPU to estimate a baseline throughput per GPU (tokens per second).

```
throughput_per_GPU = compute_num_tokens(sample_data) / completion_time
```

Calculate your total dataset size in tokens and determine your target completion time based on your SLO requirements.

```
num_total_tokens = compute_num_tokens(dataset)
target_completion_time = ... (based on your SLO)
```

Divide total tokens by target duration to get a target throughput based on your dataset and SLO requirements.

```
target_throughput = num_total_tokens / target_completion_time
```

Divide your target throughput by your single-GPU throughput to estimate GPU count needed. Add a 10-20% buffer to account for variability and calculate total cost as GPU count times GPU hourly rate times duration.

```
num_GPU_needed = target_throughput / throughput_per_GPU
estimate_cost = num_GPU_needed x GPU_hourly_rate x target_completion_time
```

Once you have baseline estimates, explore optimization strategies and compare to your baseline estimates

## Cost optimization strategies[​](#cost-strategies "Direct link to Cost optimization strategies")

Beyond selecting appropriate GPUs and parallelism strategies, you can optimize configuration parameters to reduce costs while maintaining performance. These strategies focus on reducing GPU memory requirements, improving utilization, and leveraging cost-effective infrastructure options.

### Maximize GPU utilization[​](#maximize-gpu-utilization "Direct link to Maximize GPU utilization")

Maximizing GPU utilization helps you process more data with fewer GPUs, reducing infrastructure costs. When GPUs operate at higher utilization, you can achieve your throughput targets with fewer resources, directly lowering hourly costs.

Ray Data LLM provides strong default optimizations for GPU utilization out of the box. The default configuration balances throughput, memory usage, and fault tolerance for most workloads. For advanced tuning strategies to further improve utilization, see [Optimize throughput for Ray Data LLM batch inference](/llm/batch-inference/throughput-optimization/tuning-strategies.md).

### Use appropriate GPU types[​](#use-appropriate-gpu-types "Direct link to Use appropriate GPU types")

Selecting the wrong GPU tier can result in unnecessary cost. Make sure to match GPU memory to your model size to avoid overpaying for unused capacity. Using H100 for a 7B model wastes premium GPU cost, while trying to fit a 70B model on T4 GPUs won't work. For guidance on selecting the right GPU, see [Choose a GPU for LLM serving](/llm/serving/gpu-guidance.md).

### Apply quantization when acceptable[​](#apply-quantization-when-acceptable "Direct link to Apply quantization when acceptable")

FP8 quantization reduces model memory by approximately 50% compared to BF16, allowing 2× more concurrent sequences or enabling use of smaller, cheaper GPUs. For example, DeepSeek-R1-670B requires \~1340 GB in BF16 but only \~720 GB in FP8. This can significantly reduce GPU cost while maintaining similar throughput, with a trade-off on output quality.

For detailed guidance on configuring quantization for batch inference, see [Quantization for LLM batch inference](/llm/batch-inference/throughput-optimization/quantization.md).

### Leverage spot instances[​](#leverage-spot-instances "Direct link to Leverage spot instances")

Spot instances can be 50-80% cheaper than on-demand instances. Batch inference tolerates interruptions well because Ray Data LLM automatically retries failed tasks. Ensure your dataset is well-partitioned into smaller blocks for fine-grained recovery.

Enable spot instances preference for your Anyscale job in the compute config:

```
#my-job.yaml
name: my-job-name
...
compute_config: 
  head_node:
    instance_type: m5.8xlarge
  worker_nodes:
    - instance_type: p4d.24xlarge
      min_nodes: 1
      max_nodes: 5
      market_type: PREFER_SPOT
```

This configuration prefers spot instances but falls back to on-demand if necessary. If on-demand instances are running and spot instances become available, the on-demand instances are evicted and replaced with spot instances.

See [Create and manage jobs](/jobs/manage.md) for more details on configuring your Anyscale job.

### Enable autoscaling for inference workers[​](#enable-autoscaling-for-inference-workers "Direct link to Enable autoscaling for inference workers")

You can enable autoscaling to let Ray Data LLM dynamically adjust inference workers based on the workload demand. See [Autoscaling workers](/llm/batch-inference/resource-allocation/concurrency-and-batching.md#autoscaling)

note

The inference engine initialization is expensive. For batch jobs with predictable workloads, setting a fixed number of workers allocates GPU resources upfront and ensures predictable performance and costs.

## Monitoring performance and cost metrics[​](#monitoring "Direct link to Monitoring performance and cost metrics")

Monitor key performance and cost metrics throughout execution to identify optimization opportunities and ensure cost-effective resource usage. For comprehensive guidance on monitoring Ray Data LLM batch inference, including how to access Ray Dashboard, Ray Workloads, Metrics tab, and interpret performance metrics, see [Monitoring and measurement](/llm/batch-inference/throughput-optimization/tuning-strategies.md#monitoring).
