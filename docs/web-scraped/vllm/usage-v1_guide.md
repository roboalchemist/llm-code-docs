# Source: https://docs.vllm.ai/en/stable/usage/v1_guide/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/usage/v1_guide.md "Edit this page")

# vLLM V1[¶](#vllm-v1 "Permanent link")

Announcement

We have fully deprecated V0. Please read [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] RFC #18571](https://github.com/vllm-project/vllm/issues/18571) for more details.

If you have a use case that works on V0 Engine but not V1, please share it on [GitHub](https://github.com/vllm-project/vllm) or in the [vLLM Slack](https://inviter.co/vllm-slack).

vLLM V0 successfully supported a wide range of models and hardware, but as new features were developed independently, the system grew increasingly complex. This complexity made it harder to integrate new capabilities and introduced technical debt, revealing the need for a more streamlined and unified design.

Building on V0's success, vLLM V1 retains the stable and proven components from V0 (such as the models, GPU kernels, and utilities). At the same time, it significantly re-architects the core systems, covering the scheduler, KV cache manager, worker, sampler, and API server, to provide a cohesive, maintainable framework that better accommodates continued growth and innovation.

Specifically, V1 aims to:

-   Provide a **simple, modular, and easy-to-hack codebase**.
-   Ensure **high performance** with near-zero CPU overhead.
-   **Combine key optimizations** into a unified architecture.
-   Require **zero configs** by enabling features/optimizations by default.

We see significant performance improvements from upgrading to V1 core engine, in particular for long context scenarios. Please see performance benchmark (To be added).

For more details, check out the vLLM V1 blog post [vLLM V1: A Major Upgrade to vLLM's Core Architecture](https://blog.vllm.ai/2025/01/27/v1-alpha-release.html) (published Jan 27, 2025).

This living user guide outlines a few known **important changes and limitations** introduced by vLLM V1. The team has been working actively to bring V1 as the default engine, therefore this guide will be updated constantly as more features get supported on vLLM V1.

## Differences from V0[¶](#differences-from-v0 "Permanent link")

This section lists some differences in behavior between V0 and V1.

### Chunked Prefill[¶](#chunked-prefill "Permanent link")

Chunked prefill is enabled by default whenever possible, unlike in V0 where it was conditionally enabled based on model characteristics.

### CUDA Graphs[¶](#cuda-graphs "Permanent link")

CUDA graph capture takes up more memory in V1 than in V0.

### Semantic Changes to Logprobs[¶](#semantic-changes-to-logprobs "Permanent link")

#### Logprobs Calculation[¶](#logprobs-calculation "Permanent link")

By default, logprobs in V1 are now returned immediately once computed from the model's raw output (i.e. before applying any logits post-processing such as temperature scaling or penalty adjustments). As a result, the returned logprobs do not reflect the final adjusted probabilities used during sampling.

You can adjust this behavior by setting the `--logprobs-mode` flag. Four modes are supported: `raw_logprobs` (default), `processed_logprobs`, `raw_logits`, `processed_logits`. Raw means the values before applying any logit processors, like bad words. Processed means the values after applying all processors, including temperature and top_k/top_p.

#### Prompt Logprobs with Prefix Caching[¶](#prompt-logprobs-with-prefix-caching "Permanent link")

While V1 supports passing prompt logprobs with prefix caching enabled, it no longer caches the logprobs. For a request requiring prompt logprobs, the engine will ignore the prefix cache and recompute the prefill of full prompt to generate the logprobs.

## Feature Support[¶](#feature-support "Permanent link")

For each item, its support in vLLM V1 falls into one of the following states:

-   **🟢 Functional**: Fully operational with optimizations comparable to or better than V0.
-   **🟡 In Progress**: Planned to be in vLLM V1, with open PRs/RFCs.
-   **🔴 Removed**: Dropped from vLLM V1. Will only consider re-introducing if there is strong demand.

Note

vLLM V1's unified scheduler treats both prompt and output tokens the same way by using a simple dictionary (e.g., ``) to dynamically allocate a fixed token budget per request, enabling features like chunked prefills, prefix caching, and speculative decoding without a strict separation between prefill and decode phases.

The V1 scheduler supports multiple scheduling policies, including First-Come, First-Served (FCFS) and priority-based scheduling (where requests are processed based on assigned priority, with FCFS as a tie-breaker), configurable via the `--scheduling-policy` argument.

### Hardware[¶](#hardware "Permanent link")

  Hardware        Status
  --------------- --------
  **NVIDIA**      🟢
  **AMD**         🟢
  **INTEL GPU**   🟢
  **TPU**         🟢
  **CPU**         🟢

Note

More hardware platforms may be supported via plugins, e.g.:

-   [vllm-ascend](https://github.com/vllm-project/vllm-ascend)
-   [vllm-spyre](https://github.com/vllm-project/vllm-spyre)
-   [vllm-gaudi](https://github.com/vllm-project/vllm-gaudi)
-   [vllm-openvino](https://github.com/vllm-project/vllm-openvino)

Please check their corresponding repositories for more details.

### Models[¶](#models "Permanent link")

  Model Type                   Status
  ---------------------------- ---------------------------
  **Decoder-only Models**      🟢
  **Encoder-Decoder Models**   🟢 (Whisper), 🔴 (Others)
  **Pooling Models**           🟢
  **Mamba Models**             🟢
  **Multimodal Models**        🟢

See below for the status of models that are not yet supported or have more features planned in V1.

#### Pooling Models[¶](#pooling-models "Permanent link")

Now fully supported, with prefix caching and chunked prefill newly available for last-pooling models.

We are working on enabling prefix caching and chunked prefill for more categories of pooling models.

#### Mamba Models[¶](#mamba-models "Permanent link")

Models using selective state-space mechanisms instead of standard transformer attention are supported. Models that use Mamba-2 and Mamba-1 layers (e.g., `Mamba2ForCausalLM`, `MambaForCausalLM`,`FalconMambaForCausalLM`) are supported.

Hybrid models that combine Mamba-2 and Mamba-1 layers with standard attention layers are also supported (e.g., `BambaForCausalLM`, `Zamba2ForCausalLM`, `NemotronHForCausalLM`, `FalconH1ForCausalLM` and `GraniteMoeHybridForCausalLM`, `JambaForCausalLM`, `Plamo2ForCausalLM`).

Hybrid models with mechanisms different to Mamba are also supported (e.g, `MiniMaxText01ForCausalLM`, `MiniMaxM1ForCausalLM`, `Lfm2ForCausalLM`).

Please note that prefix caching is not yet supported for any of the above models.

#### Encoder-Decoder Models[¶](#encoder-decoder-models "Permanent link")

Whisper is supported. Other models requiring cross-attention between separate encoder and decoder (e.g., `BartForConditionalGeneration`, `MllamaForConditionalGeneration`) are no longer supported.

### Features[¶](#features "Permanent link")

  Feature                                       Status
  --------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Prefix Caching**                            🟢 Functional
  **Chunked Prefill**                           🟢 Functional
  **LoRA**                                      🟢 Functional
  **Logprobs Calculation**                      🟢 Functional
  **FP8 KV Cache**                              🟢 Functional
  **Spec Decode**                               🟢 Functional
  **Prompt Logprobs with Prefix Caching**       🟢 Functional
  **Structured Output Alternative Backends**    🟢 Functional
  **Concurrent Partial Prefills**               🟡 [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] In Progress](https://github.com/vllm-project/vllm/issues/14003)
  **best_of**                                   🔴 [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] Removed](https://github.com/vllm-project/vllm/issues/13361)
  **Per-Request Logits Processors**             🔴 [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] Removed](https://github.com/vllm-project/vllm/pull/13360)
  **GPU \<\> CPU KV Cache Swapping**            🔴 Removed
  **Request-level Structured Output Backend**   🔴 Removed

Note

vLLM V1's unified scheduler treats both prompt and output tokens the same way by using a simple dictionary (e.g., ``) to dynamically allocate a fixed token budget per request, enabling features like chunked prefills, prefix caching, and speculative decoding without a strict separation between prefill and decode phases.

#### Removed Features[¶](#removed-features "Permanent link")

As part of the major architectural rework in vLLM V1, several legacy features have been removed.

##### Sampling features[¶](#sampling-features "Permanent link")

-   **best_of**: This feature has been removed due to limited usage. See details at [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] RFC #13361](https://github.com/vllm-project/vllm/issues/13361).
-   **Per-Request Logits Processors**: In V0, users could pass custom processing functions to adjust logits on a per-request basis. In vLLM V1, this feature has been removed. Instead, we now support **global logits processors** which are set at startup time, see [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] RFC #17799](https://github.com/vllm-project/vllm/issues/17799).

##### KV Cache features[¶](#kv-cache-features "Permanent link")

-   **GPU \<\> CPU KV Cache Swapping**: with the new simplified core architecture, vLLM V1 no longer requires KV cache swapping to handle request preemptions.

##### Structured Output features[¶](#structured-output-features "Permanent link")

-   **Request-level Structured Output Backend**: Removed; alternative backends (outlines, guidance) with fallbacks are supported now.

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [November 23, 2025] ]