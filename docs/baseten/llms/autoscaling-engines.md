# Source: https://docs.baseten.co/engines/performance-concepts/autoscaling-engines.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Auto-Scaling Engines

> Performant auto-scaling custom tailored to Embedding and Generation Models on Baseten

# Auto-Scaling Engines

Beyond the [Introduction to autoscaling](/deployment/autoscaling), some adjustments specialized to models using dynamic batching are helpful.

Both BEI and Engine-Builder-LLM use **dynamic batching** to process parallel multiple requests. This increase in throughput comes at the cost of increased p50 latency.
Combining this feature with engine-specific autoscaling becomes a powerful tool for maintaining optimal performance across varying traffic patterns.

## BEI

BEI provides millisecond-range inference times and scales differently than other models. With too few replicas, backpressure can build up quickly.

**Key recommendations:**

* **Enable autoscaling** - BEI's millisecond-range inference and dynamic batching require autoscaling to handle variable traffic efficiently
* **Target utilization: 25%** - Low target provides headroom for traffic spikes and accommodates dynamic batching behavior
* **Concurrency: 96+ requests** - High concurrency allows maximum throughput. If unsure, start with 64 and 40% utilization and tune on live traffic.
* **Minimum concurrency: ≥8** - Never set below 8 for optimal performance

**Multi-payload routes** (`/rerank`, `/v1/embeddings`) can send multiple requests at once, challenging autoscaling based on concurrent requests. Use the [Performance client](/engines/performance-concepts/performance-client) for optimal scaling.

## Engine-Builder-LLM

Engine-Builder-LLM uses dynamic batching to maximize throughput, similar to BEI, but doesn't face the multi-payload challenge that BEI does with `/rerank` and `/v1/embeddings` routes.

**Key recommendations:**

* **Target utilization: 40-50%** - Lower than default to accommodate dynamic batching and provide headroom
* **Concurrency: 16-256 requests** - If unsure, start with 64 and 40% utilization and tune on live traffic.
* **Batch cases** - Use the Performance client for batch processing
* **Minimum concurrency: ≥8** - Never set below 8 for optimal performance
* **Lookahead works slightly better with lower batch-size** - Tune the concurrency to a same or slightly below `max_batch_size`, so that lookahead is aware that it can perform optimizations. This is partially also helpful for any `engine-builder-llm` engine, even if you're not using lookahead.

**Important**: Do not set concurrency above `max_batch_size` as it leads to on-replica queueing and negates the benefits of autoscaling.

General advice:
Tune the equilibrium on your live-traffic, cost, thoughput and latency targets. Your mean expected concurrency will be the concurrency\_target \* target\_utilization. Most engines are only provide marginal thoughput improvements when paired with 128 requests vs working on 256 requests at a time. Keeping a mean expected concurrency around 16-64 will allow for the best stability guarantees and proactive scaling descisions under variable traffic.

## Quick Reference

| **Setting**        | **BEI**      | **Engine-Builder-LLM** |
| ------------------ | ------------ | ---------------------- |
| Target utilization | 25%          | 40-50%                 |
| Concurrency        | 96+ (min ≥8) | 32-256                 |
| Batch size         | Flexible     | Flexible               |

## Further reading

* [BEI overview](/engines/bei/overview) - General BEI documentation
* [BEI reference config](/engines/bei/bei-reference) - Complete configuration options
* [Engine-Builder-LLM overview](/engines/engine-builder-llm/overview) - Generation model details
* [Embedding examples](/examples/bei) - Concrete deployment examples
* [Performance client documentation](/engines/performance-concepts/performance-client) - Client usage with embeddings
* [Quantization guide](/engines/performance-concepts/quantization-guide) - Hardware considerations
* [Performance optimization](/development/model/performance-optimization) - General performance guidance
