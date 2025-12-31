# Source: https://docs.vllm.ai/en/stable/features/batch_invariance/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/features/batch_invariance.md "Edit this page")

# Batch Invariance[¶](#batch-invariance "Permanent link")

Note

Batch invariance is currently in beta. Some features are still under active development. Track progress and planned improvements at [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] Issue #27433](https://github.com/vllm-project/vllm/issues/27433)

This document shows how to enable batch invariance in vLLM. Batch invariance ensures that the output of a model is deterministic and independent of the batch size or the order of requests in a batch.

## Motivation[¶](#motivation "Permanent link")

Batch invariance is crucial for several use cases:

-   **Framework debugging**: Deterministic outputs make it easier to debug issues in the inference framework, as the same input will always produce the same output regardless of batching.
-   **Model debugging**: Helps identify issues in model implementations by ensuring consistent behavior across different batch configurations.
-   **Reinforcement Learning (RL)**: RL training often requires deterministic rollouts for reproducibility and stable training.
-   **Large-scale inference systems**: Systems that use vLLM as a component benefit from deterministic behavior for testing, validation, and consistency guarantees.

## Hardware Requirements[¶](#hardware-requirements "Permanent link")

Batch invariance currently requires NVIDIA GPUs with compute capability 9.0 or higher:

-   **H-series**: H100, H200
-   **B-series**: B100, B200

## Enabling Batch Invariance[¶](#enabling-batch-invariance "Permanent link")

Batch invariance can be enabled by setting the `VLLM_BATCH_INVARIANT` environment variable to `1`:

    export VLLM_BATCH_INVARIANT=1

### Online Inference (Server Mode)[¶](#online-inference-server-mode "Permanent link")

To start a vLLM server with batch invariance enabled:

    VLLM_BATCH_INVARIANT=1 vllm serve meta-llama/Llama-3.1-8B-Instruct

Then use the OpenAI-compatible client:

    from openai import OpenAI

    client = OpenAI(
        api_key="EMPTY",
        base_url="http://localhost:8000/v1",
    )

    # These requests will produce deterministic outputs
    # regardless of batch size or order
    response = client.completions.create(
        model="meta-llama/Llama-3.1-8B-Instruct",
        prompt="The future of AI is",
        max_tokens=100,
        temperature=0.7,
        seed=42,
    )

    print(response.choices[0].text)

### Offline Inference[¶](#offline-inference "Permanent link")

For offline batch inference with batch invariance:

    import os
    os.environ["VLLM_BATCH_INVARIANT"] = "1"

    from vllm import LLM, SamplingParams

    prompts = [
        "The future of AI is",
        "Machine learning enables",
        "Deep learning models can",
    ]

    sampling_params = SamplingParams(
        temperature=0.7,
        top_p=0.95,
        max_tokens=100,
        seed=42,
    )

    llm = LLM(
        model="meta-llama/Llama-3.1-8B-Instruct",
        tensor_parallel_size=1,
    )

    # Outputs will be deterministic regardless of batch size
    outputs = llm.generate(prompts, sampling_params)

    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: ")
        print(f"Generated: \n")

## Tested Models[¶](#tested-models "Permanent link")

Batch invariance has been tested and verified on the following models:

-   **DeepSeek series**: `deepseek-ai/DeepSeek-V3`, `deepseek-ai/DeepSeek-V3-0324`, `deepseek-ai/DeepSeek-R1`, `deepseek-ai/DeepSeek-V3.1`
-   **Qwen3 (Dense)**: `Qwen/Qwen3-1.7B`, `Qwen/Qwen3-8B`
-   **Qwen3 (MoE)**: `Qwen/Qwen3-30B-A3B`, `Qwen/Qwen3-Next-80B-A3B-Instruct`
-   **Llama 3**: `meta-llama/Llama-3.1-8B-Instruct`, `meta-llama/Llama-3.2-1B-Instruct`

Other models may also work, but these have been explicitly validated. If you encounter issues with a specific model, please report them on the [GitHub issue tracker](https://github.com/vllm-project/vllm/issues/new/choose).

## Implementation Details[¶](#implementation-details "Permanent link")

When batch invariance is enabled, vLLM:

1.  Uses deterministic kernel implementations for attention and other operations
2.  Ensures consistent numerical behavior across different batch sizes
3.  Disables certain optimizations that may introduce non-determinism (such as custom all-reduce operations in tensor parallel mode)

Note

Enabling batch invariance may impact performance compared to the default non-deterministic mode. This trade-off is intentional to guarantee reproducibility.

## Future Improvements[¶](#future-improvements "Permanent link")

The batch invariance feature is under active development. Planned improvements include:

-   Support for additional GPU architectures
-   Expanded model coverage
-   Performance optimizations
-   Additional testing and validation

For the latest status and to contribute ideas, see the [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] tracking issue](https://github.com/vllm-project/vllm/issues/27433).

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [October 31, 2025] ]