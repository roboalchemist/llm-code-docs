# Source: https://docs.vllm.ai/en/stable/features/quantization/modelopt/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/features/quantization/modelopt.md "Edit this page")

# NVIDIA Model Optimizer[¶](#nvidia-model-optimizer "Permanent link")

The [NVIDIA Model Optimizer](https://github.com/NVIDIA/Model-Optimizer) is a library designed to optimize models for inference with NVIDIA GPUs. It includes tools for Post-Training Quantization (PTQ) and Quantization Aware Training (QAT) of Large Language Models (LLMs), Vision Language Models (VLMs), and diffusion models.

We recommend installing the library with:

    pip install nvidia-modelopt

## Quantizing HuggingFace Models with PTQ[¶](#quantizing-huggingface-models-with-ptq "Permanent link")

You can quantize HuggingFace models using the example scripts provided in the Model Optimizer repository. The primary script for LLM PTQ is typically found within the `examples/llm_ptq` directory.

Below is an example showing how to quantize a model using modelopt\'s PTQ API:

Code

    import modelopt.torch.quantization as mtq
    from transformers import AutoModelForCausalLM

    # Load the model from HuggingFace
    model = AutoModelForCausalLM.from_pretrained("<path_or_model_id>")

    # Select the quantization config, for example, FP8
    config = mtq.FP8_DEFAULT_CFG

    # Define a forward loop function for calibration
    def forward_loop(model):
        for data in calib_set:
            model(data)

    # PTQ with in-place replacement of quantized modules
    model = mtq.quantize(model, config, forward_loop)

After the model is quantized, you can export it to a quantized checkpoint using the export API:

    import torch
    from modelopt.torch.export import export_hf_checkpoint

    with torch.inference_mode():
        export_hf_checkpoint(
            model,  # The quantized model.
            export_dir,  # The directory where the exported files will be stored.
        )

The quantized checkpoint can then be deployed with vLLM. As an example, the following code shows how to deploy `nvidia/Llama-3.1-8B-Instruct-FP8`, which is the FP8 quantized checkpoint derived from `meta-llama/Llama-3.1-8B-Instruct`, using vLLM:

Code

    from vllm import LLM, SamplingParams

    def main():
        model_id = "nvidia/Llama-3.1-8B-Instruct-FP8"

        # Ensure you specify quantization="modelopt" when loading the modelopt checkpoint
        llm = LLM(model=model_id, quantization="modelopt", trust_remote_code=True)

        sampling_params = SamplingParams(temperature=0.8, top_p=0.9)

        prompts = [
            "Hello, my name is",
            "The president of the United States is",
            "The capital of France is",
            "The future of AI is",
        ]

        outputs = llm.generate(prompts, sampling_params)

        for output in outputs:
            prompt = output.prompt
            generated_text = output.outputs[0].text
            print(f"Prompt: , Generated text: ")

    if __name__ == "__main__":
        main()

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [December 8, 2025] ]