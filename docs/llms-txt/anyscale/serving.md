# Source: https://docs.anyscale.com/llm/serving.md

# Serve LLMs with Anyscale services

[View Markdown](/llm/serving.md)

# Serve LLMs with Anyscale services

This page provides an overview of how you can use Anyscale services to deploy large language models (LLMs) in production to generate text, answer questions, and power intelligent workflows at scale.

Anyscale services provide you with a production-grade solution through three integrated components:

* Ray Serve for orchestration and scaling.
* vLLM for inference.
* Anyscale for infrastructure management.

For an overview of LLM serving, see [What is LLM serving?](/llm/serving/intro.md) and learn more about Ray Serve LLM in their [documentation](https://docs.ray.io/en/latest/serve/llm/index.html).

## Tutorial categories[​](#tutorial-categories "Direct link to Tutorial categories")

These templates provide a fast path to serving LLMs using Ray Serve on Anyscale, with focused tutorials for different deployment scales, from single-GPU setups to multi-node clusters.

Each tutorial includes development and production setups, tips for configuring your cluster, and guidance on monitoring and scaling with Ray Serve. For hands-on experience, try our [Deploy LLM templates](https://console.anyscale.com/template-preview/deployment-serve-llm) in an Anyscale Workspace.

* [Deploy a small-sized LLM](https://console.anyscale.com/template-preview/deployment-serve-llm?file=%252Ffiles%252Fsmall-size-llm)<br /><!-- -->Deploy small-sized models on a single GPU, such as Llama 3 8 B, Mistral 7 B, or Phi-2.

* [Deploy a medium-sized LLM](https://console.anyscale.com/template-preview/deployment-serve-llm?file=%252Ffiles%252Fmedium-size-llm)<br /><!-- -->Deploy medium-sized models using tensor parallelism across 4—8 GPUs on a single node, such as Llama 3 70 B, Qwen 14 B, Mixtral 8x7 B.

* [Deploy a large-sized LLM](https://console.anyscale.com/template-preview/deployment-serve-llm?file=%252Ffiles%252Flarge-size-llm)<br /><!-- -->Deploy massive models using pipeline parallelism across a multi-node cluster, such as Deepseek-R1 or Llama-Nemotron-253 B.

* [Deploy a vision LLM](https://console.anyscale.com/template-preview/deployment-serve-llm?file=%252Ffiles%252Fvision-llm)<br /><!-- -->Deploy models with image and text input such as Qwen 2.5-VL-7 B-Instruct, MiniGPT-4, or Pixtral-12 B.

* [Deploy a reasoning LLM](https://console.anyscale.com/template-preview/deployment-serve-llm?file=%252Ffiles%252Freasoning-llm)<br /><!-- -->Deploy models with reasoning capabilities designed for long-context tasks, coding, or tool use, such as QwQ-32 B.

* [Deploy a hybrid reasoning LLM](https://console.anyscale.com/template-preview/deployment-serve-llm?file=%252Ffiles%252Fhybrid-reasoning-llm)<br /><!-- -->Deploy models that can switch between reasoning and non-reasoning modes for flexible usage, such as Qwen-3.

* [Deploy gpt-oss](https://console.anyscale.com/template-preview/deployment-serve-llm?file=%252Ffiles%252Fgpt-oss)<br /><!-- -->Deploy gpt-oss reasoning models at production scale, with `gpt-oss-20b` for lower-latency tasks and `gpt-oss-120b` for higher accuracy.

## Common challenges for serving LLMs[​](#challenges "Direct link to Common challenges for serving LLMs")

The following table outlines several common challenges for serving LLMs:

| Challenge            | Description                                                                                                                                                                                                           |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Managing GPU memory  | LLM weights and the KV cache consume tens to hundreds of gigabytes. You can use techniques such as paged attention, quantization, and efficient memory sharing to prevent out-of-memory errors.                       |
| Minimizing latency   | Your users expect fast, interactive responses. You can reduce time-to-first-token and subsequent token generation time with optimizations such as continuous batching, speculative decoding, and custom CUDA kernels. |
| Ensuring scalability | Production traffic patterns are unpredictable and bursty. Your serving solution must autoscale replicas quickly and reliably to meet demand without downtime.                                                         |
| Optimizing cost      | GPUs represent significant infrastructure costs. You need to maximize hardware utilization and scale to zero during idle periods to control expenses.                                                                 |

## Orchestration with Anyscale services[​](#orchestration "Direct link to Orchestration with Anyscale services")

Anyscale services extend Ray Serve by providing a scalable model serving library built on the Ray distributed runtime. With Ray Serve as your orchestration layer, you benefit from the following:

* **Automatic scaling and load balancing**: Automatically adds or removes model replicas based on real-time traffic patterns.
* **Unified multi-model deployment**: Deploy, manage, and route traffic to multiple models using a single configuration.
* **OpenAI-compatible API**: Use drop-in replacement endpoints for your existing OpenAI API clients.
* **Dynamic multi-LoRA support**: Serve a single base model with different LoRA adapters attached at request time.

## Inference with vLLM[​](#inference "Direct link to Inference with vLLM")

Ray Serve integrates with vLLM for inference. Key vLLM optimizations include the following:

* **PagedAttention**: Manages the KV cache as if it's virtual memory, eliminating memory fragmentation.
* **Continuous batching**: Maximizes GPU utilization by continuously adding new requests to processing batches.
* **Optimized CUDA kernels**: Integrates optimized kernels including FlashAttention and supports advanced quantization methods such as INT4 and FP8.

For more information on how Ray Serve LLM integrates with vLLM, you can learn more about its [architecture](https://docs.ray.io/en/latest/serve/llm/architecture/overview.html)

## Managed infrastructure and enterprise-ready features[​](#infra "Direct link to Managed infrastructure and enterprise-ready features")

Anyscale provides the infrastructure and tools you need to run Ray Serve securely and cost-effectively at scale, including the following:

* **Managed infrastructure**: Create optimized Ray clusters in your cloud account without manual provisioning.
* **Cost optimization**: Use pay-as-you-go, autoscaling node pools that scale to zero when idle.
* **Enterprise security**: Secure your deployments with private networking (VPC), single sign-on (SSO), and detailed audit logs.
* **Seamless scaling**: Handle traffic spikes through Ray Autoscaler and pre-warmed instance pools.
