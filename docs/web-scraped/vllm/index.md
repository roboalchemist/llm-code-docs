# Source: https://docs.vllm.ai/en/stable/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/README.md "Edit this page")

# Welcome to vLLM[¶](#welcome-to-vllm "Permanent link")

<figure>
<a href="assets/logos/vllm-logo-text-light.png" class="glightbox" data-type="image" data-width="auto" data-height="auto" data-desc-position="bottom"><img src="assets/logos/vllm-logo-text-light.png" class="logo-light" style="width:60.0%" data-align="center" alt="vLLM Light" /></a> <a href="assets/logos/vllm-logo-text-dark.png" class="glightbox" data-type="image" data-width="auto" data-height="auto" data-desc-position="bottom"><img src="assets/logos/vllm-logo-text-dark.png" class="logo-dark" style="width:60.0%" data-align="center" alt="vLLM Dark" /></a>
</figure>

**Easy, fast, and cheap LLM serving for everyone**

[Star](https://github.com/vllm-project/vllm) [Watch](https://github.com/vllm-project/vllm/subscription) [Fork](https://github.com/vllm-project/vllm/fork)

vLLM is a fast and easy-to-use library for LLM inference and serving.

Originally developed in the [Sky Computing Lab](https://sky.cs.berkeley.edu) at UC Berkeley, vLLM has evolved into a community-driven project with contributions from both academia and industry.

Where to get started with vLLM depends on the type of user. If you are looking to:

-   Run open-source models on vLLM, we recommend starting with the [Quickstart Guide](getting_started/quickstart/)
-   Build applications with vLLM, we recommend starting with the [User Guide](usage/)
-   Build vLLM, we recommend starting with [Developer Guide](contributing/)

For information about the development of vLLM, see:

-   [Roadmap](https://roadmap.vllm.ai)
-   [Releases](https://github.com/vllm-project/vllm/releases)

vLLM is fast with:

-   State-of-the-art serving throughput
-   Efficient management of attention key and value memory with [**PagedAttention**](https://blog.vllm.ai/2023/06/20/vllm.html)
-   Continuous batching of incoming requests
-   Fast model execution with CUDA/HIP graph
-   Quantization: [GPTQ](https://arxiv.org/abs/2210.17323), [AWQ](https://arxiv.org/abs/2306.00978), INT4, INT8, and FP8
-   Optimized CUDA kernels, including integration with FlashAttention and FlashInfer.
-   Speculative decoding
-   Chunked prefill

vLLM is flexible and easy to use with:

-   Seamless integration with popular HuggingFace models
-   High-throughput serving with various decoding algorithms, including *parallel sampling*, *beam search*, and more
-   Tensor, pipeline, data and expert parallelism support for distributed inference
-   Streaming outputs
-   OpenAI-compatible API server
-   Support for NVIDIA GPUs, AMD CPUs and GPUs, Intel CPUs and GPUs, PowerPC CPUs, Arm CPUs, and TPU. Additionally, support for diverse hardware plugins such as Intel Gaudi, IBM Spyre and Huawei Ascend.
-   Prefix caching support
-   Multi-LoRA support

For more information, check out the following:

-   [vLLM announcing blog post](https://vllm.ai) (intro to PagedAttention)
-   [vLLM paper](https://arxiv.org/abs/2309.06180) (SOSP 2023)
-   [How continuous batching enables 23x throughput in LLM inference while reducing p50 latency](https://www.anyscale.com/blog/continuous-batching-llm-inference) by Cade Daniel et al.
-   [vLLM Meetups](community/meetups/)

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [November 15, 2025] ]