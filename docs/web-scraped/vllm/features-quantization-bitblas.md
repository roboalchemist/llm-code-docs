# Source: https://docs.vllm.ai/en/stable/features/quantization/bitblas/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/features/quantization/bitblas.md "Edit this page")

# BitBLAS[¶](#bitblas "Permanent link")

vLLM now supports [BitBLAS](https://github.com/microsoft/BitBLAS) for more efficient and flexible model inference. Compared to other quantization frameworks, BitBLAS provides more precision combinations.

Note

Ensure your hardware supports the selected `dtype` (`torch.bfloat16` or `torch.float16`). Most recent NVIDIA GPUs support `float16`, while `bfloat16` is more common on newer architectures like Ampere or Hopper. For details see [supported hardware](../#supported-hardware).

Below are the steps to utilize BitBLAS with vLLM.

    pip install bitblas>=0.1.0

vLLM reads the model\'s config file and supports pre-quantized checkpoints.

You can find pre-quantized models on:

-   [Hugging Face (BitBLAS)](https://huggingface.co/models?search=bitblas)
-   [Hugging Face (GPTQ)](https://huggingface.co/models?search=gptq)

Usually, these repositories have a `quantize_config.json` file that includes a `quantization_config` section.

## Read bitblas format checkpoint[¶](#read-bitblas-format-checkpoint "Permanent link")

    from vllm import LLM
    import torch

    # "hxbgsyxh/llama-13b-4bit-g-1-bitblas" is a pre-quantized checkpoint.
    model_id = "hxbgsyxh/llama-13b-4bit-g-1-bitblas"
    llm = LLM(
        model=model_id,
        dtype=torch.bfloat16,
        trust_remote_code=True,
        quantization="bitblas",
    )

## Read gptq format checkpoint[¶](#read-gptq-format-checkpoint "Permanent link")

Code

    from vllm import LLM
    import torch

    # "hxbgsyxh/llama-13b-4bit-g-1" is a pre-quantized checkpoint.
    model_id = "hxbgsyxh/llama-13b-4bit-g-1"
    llm = LLM(
        model=model_id,
        dtype=torch.float16,
        trust_remote_code=True,
        quantization="bitblas",
        max_model_len=1024,
    )

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [October 15, 2025] ]