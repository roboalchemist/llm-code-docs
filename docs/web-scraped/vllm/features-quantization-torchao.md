# Source: https://docs.vllm.ai/en/stable/features/quantization/torchao/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/features/quantization/torchao.md "Edit this page")

# TorchAO[¶](#torchao "Permanent link")

TorchAO is an architecture optimization library for PyTorch, it provides high performance dtypes, optimization techniques and kernels for inference and training, featuring composability with native PyTorch features like torch.compile, FSDP etc.. Some benchmark numbers can be found [here](https://github.com/pytorch/ao/tree/main/torchao/quantization#benchmarks).

We recommend installing the latest torchao nightly with

    # Install the latest TorchAO nightly build
    # Choose the CUDA version that matches your system (cu126, cu128, etc.)
    pip install \
        --pre torchao>=10.0.0 \
        --index-url https://download.pytorch.org/whl/nightly/cu126

## Quantizing HuggingFace Models[¶](#quantizing-huggingface-models "Permanent link")

You can quantize your own huggingface model with torchao, e.g. [transformers](https://huggingface.co/docs/transformers/main/en/quantization/torchao) and [diffusers](https://huggingface.co/docs/diffusers/en/quantization/torchao), and save the checkpoint to huggingface hub like [this](https://huggingface.co/jerryzh168/llama3-8b-int8wo) with the following example code:

Code

    import torch
    from transformers import TorchAoConfig, AutoModelForCausalLM, AutoTokenizer
    from torchao.quantization import Int8WeightOnlyConfig

    model_name = "meta-llama/Meta-Llama-3-8B"
    quantization_config = TorchAoConfig(Int8WeightOnlyConfig())
    quantized_model = AutoModelForCausalLM.from_pretrained(
        model_name,
        dtype="auto",
        device_map="auto",
        quantization_config=quantization_config
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    input_text = "What are we having for dinner?"
    input_ids = tokenizer(input_text, return_tensors="pt").to("cuda")

    hub_repo = # YOUR HUB REPO ID
    tokenizer.push_to_hub(hub_repo)
    quantized_model.push_to_hub(hub_repo, safe_serialization=False)

Alternatively, you can use the [TorchAO Quantization space](https://huggingface.co/spaces/medmekk/TorchAO_Quantization) for quantizing models with a simple UI.

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [October 15, 2025] ]