# Source: https://docs.vllm.ai/en/stable/features/quantization/bnb/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/features/quantization/bnb.md "Edit this page")

# BitsAndBytes[¶](#bitsandbytes "Permanent link")

vLLM now supports [BitsAndBytes](https://github.com/TimDettmers/bitsandbytes) for more efficient model inference. BitsAndBytes quantizes models to reduce memory usage and enhance performance without significantly sacrificing accuracy. Compared to other quantization methods, BitsAndBytes eliminates the need for calibrating the quantized model with input data.

Below are the steps to utilize BitsAndBytes with vLLM.

    pip install bitsandbytes>=0.46.1

vLLM reads the model\'s config file and supports both in-flight quantization and pre-quantized checkpoint.

You can find bitsandbytes quantized models on [Hugging Face](https://huggingface.co/models?search=bitsandbytes). And usually, these repositories have a config.json file that includes a quantization_config section.

## Read quantized checkpoint[¶](#read-quantized-checkpoint "Permanent link")

For pre-quantized checkpoints, vLLM will try to infer the quantization method from the config file, so you don\'t need to explicitly specify the quantization argument.

    from vllm import LLM
    import torch
    # unsloth/tinyllama-bnb-4bit is a pre-quantized checkpoint.
    model_id = "unsloth/tinyllama-bnb-4bit"
    llm = LLM(
        model=model_id,
        dtype=torch.bfloat16,
        trust_remote_code=True,
    )

## Inflight quantization: load as 4bit quantization[¶](#inflight-quantization-load-as-4bit-quantization "Permanent link")

For inflight 4bit quantization with BitsAndBytes, you need to explicitly specify the quantization argument.

    from vllm import LLM
    import torch
    model_id = "huggyllama/llama-7b"
    llm = LLM(
        model=model_id,
        dtype=torch.bfloat16,
        trust_remote_code=True,
        quantization="bitsandbytes",
    )

## OpenAI Compatible Server[¶](#openai-compatible-server "Permanent link")

Append the following to your model arguments for 4bit inflight quantization:

    --quantization bitsandbytes

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [October 15, 2025] ]