# Source: https://docs.baseten.co/engines/bis-llm/advanced-features.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Gated features for BIS-LLM

> KV-aware routing, disaggregated serving, and other gated features

BIS-LLM provides features for large-scale deployments: KV cache optimization, disaggregated serving, and specialized inference strategies.

<Note>
  These advanced features are not fully self-serviceable. [Contact us](mailto:support@baseten.co) to enable them for your organization.
</Note>

## Available advanced features

### Routing and scaling

*KV-aware routing* and *disaggregated serving* optimize multi-replica deployments. KV-aware routing directs requests to replicas with the best cache hit potential, while disaggregated serving separates prefill and decode phases into independent clusters that scale separately. *Separate prefill and decode autoscaling* uses token-exact metrics to right-size each phase.

### MoE optimization

*WideEP* (expert parallelism) distributes experts across multiple GPUs for extremely large expert counts. These features work together to maximize hardware utilization on models like DeepSeek-V3 and Qwen3MoE.

### Attention and memory

*DP attention for MLA* (Multi-Head Latent Attention) compresses KV cache by projecting attention tensors into a compact latent space, *DP attention* helps to managed KV-Cache across GPU ranks, and tunes DeepSeek deployments for high throughput. *DeepSparseAttention* sparsifies the attention matrix based on token relevance. *Distributed KV storage* spreads KV cache across devices for long-context inference beyond single-device memory limits.

### Speculative decoding

*Speculative n-gram automata-based decoding* uses automata to predict tokens from n-gram patterns without full model computation. *Speculative MTP or Eagle3 decoding* uses draft-model approaches to predict and verify multiple future tokens.

### Kernel optimization

*Zero-overlap scheduling* overlaps computation and communication to hide latency. *Auto-tuned kernels* optimize kernel parameters for your specific hardware and model topology.

## KV-aware routing

KV-aware routing directs requests to replicas with the best chance of KV cache hits, routing based on cache availability and replica utilization.

KV-aware routing reduces inter-token latency by distributing load across replicas, improves time-to-first-token through cache hits on repeated queries, and increases global throughput through cache reuse.

## Disaggregated serving

Disaggregated serving separates prefill and decode phases into independent clusters, allowing each to scale and be optimized independently. This architecture is particularly valuable for large MoE models.

Disaggregated serving is available as a gated feature. [Contact us](mailto:support@baseten.co) to be paired with an engineer to discuss your needs.

Disaggregated serving enables independent scaling of prefill and decode resources, isolates time-critical TTFT metrics from throughput-focused phases, and optimizes costs by right-sizing each phase for its workload.

## Get started

### Choose the right configuration

**For advanced deployments** with large MoE models and planet-scale inference, [contact us](mailto:support@baseten.co).

**For standard deployments**:
Use the standard BIS-LLM configuration as documented in [BIS-LLM configuration](/engines/bis-llm/bis-llm-config).

## Model recommendations

### Models that benefit from advanced features

**Large MoE models:**

* DeepSeek-V3
* Qwen3MoE
* Kimi-K2
* GLM-4.7
* GPT-OSS

**Ideal use cases:**

* High-throughput API services
* Complex reasoning tasks
* Long-context applications, including agentic coding
* Planet-scale deployments

### When to use standard BIS-LLM or Engine-Builder-LLM

* Dense models under 70B parameters
* Standard MoE models under 30B parameters
* Development and testing environments
* Workloads with low KV cache hit rates

## Further reading

* [BIS-LLM overview](/engines/bis-llm/overview): Main engine documentation.
* [BIS-LLM reference config](/engines/bis-llm/bis-llm-config): Configuration options.
* [Structured outputs documentation](/engines/performance-concepts/structured-outputs): JSON schema validation.
* [Examples section](/examples/overview): Deployment examples.
