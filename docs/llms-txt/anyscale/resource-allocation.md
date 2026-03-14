# Source: https://docs.anyscale.com/llm/batch-inference/resource-allocation.md

# Resource allocation for Ray Data LLM

[View Markdown](/llm/batch-inference/resource-allocation.md)

# Resource allocation for Ray Data LLM

Efficient LLM batch inference requires the right allocation of memory and compute resources. This guide helps you configure Ray Data LLM to match your available resources, workload requirements, and cost constraints.

## Overview[​](#overview "Direct link to Overview")

Resource allocation for Ray Data LLM involves three main areas:

**Parallelism configuration**: Allocate resources based on how your workload distributes across preprocessing workers, inference workers, and post-processing workers. Proper parallelism configuration ensures all stages of your pipeline utilize available resources efficiently.

**GPU memory planning**: Understand how Ray Data LLM allocates GPU memory across model weights, KV cache, and activations. Memory planning helps you avoid out-of-memory errors and allocate appropriate resources for your workload.

**Cost optimization**: Balance throughput, time to completion, and budget constraints. Understanding cost trade-offs helps you make informed decisions about GPU types, parallelism strategies, and memory configurations.

## Configure parallelism[​](#parallelism "Direct link to Configure parallelism")

Ray Data LLM processes your data through multiple stages: preprocessing, inference, and post-processing. Each stage has different resource requirements and can scale independently.

Understanding how to configure parallelism helps you maximize resource utilization across your cluster. Proper resource configuration prevents bottlenecks where some workers sit idle while others handle excessive load.

You can control the number of inference workers, adjust task distribution, and configure CPU or GPU allocation for your custom preprocessing and post-processing functions.

For detailed guidance on configuring parallelism, see [Configure parallelism for Ray Data LLM](/llm/batch-inference/resource-allocation/concurrency-and-batching.md).

## Understand GPU memory requirements[​](#memory "Direct link to Understand GPU memory requirements")

GPU memory determines which models you can run and how much throughput you can achieve. Ray Data LLM allocates GPU memory across several components, each with different characteristics and scaling behavior.

Model weights represent the largest static allocation and scale with model size and precision. KV cache stores attention keys and values for concurrent sequences and scales with context length and throughput requirements. Activations hold intermediate tensors during forward passes and scale with model size and batch processing parameters of your inference engine.

Understanding these memory components helps you estimate total GPU memory requirements, configure memory parameters appropriately, and troubleshoot out-of-memory errors.

For detailed guidance on GPU memory requirements, see [GPU memory requirements](/llm/batch-inference/resource-allocation/gpu-memory.md).

## Balance cost and performance[​](#cost "Direct link to Balance cost and performance")

Every batch inference job involves trade-offs between cost, throughput, and time to completion. Understanding these trade-offs helps you configure resources that meet your performance requirements within budget constraints.

GPU selection impacts both cost and throughput, but more expensive GPUs don't always provide proportionally better cost efficiency. Parallelism strategies affect how resources scale with workload size. Memory optimization techniques reduce costs by enabling smaller, cheaper GPUs.

Monitoring your workload's performance and costs helps you iterate toward optimal configurations. Track GPU utilization, throughput metrics, and cost per token to identify opportunities for improvement.

For detailed guidance on cost optimization, see [Cost and performance for Ray Data LLM batch inference](/llm/batch-inference/resource-allocation/cost-performance.md).

## Next steps[​](#next-steps "Direct link to Next steps")

Once you're familiar with resource allocation fundamentals, you can further improve throughput by tuning Ray Data LLM parameters. The default settings offer strong out-of-the-box optimizations. For advanced parameter tuning techniques, see [Optimize throughput for Ray Data LLM batch inference](/llm/batch-inference/throughput-optimization/tuning-strategies.md).
