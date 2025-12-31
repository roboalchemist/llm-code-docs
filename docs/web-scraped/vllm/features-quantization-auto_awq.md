# Source: https://docs.vllm.ai/en/stable/features/quantization/auto_awq/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/features/quantization/auto_awq.md "Edit this page")

# AutoAWQ[¶](#autoawq "Permanent link")

> ⚠️ **Warning:** The `AutoAWQ` library is deprecated. This functionality has been adopted by the vLLM project in [`llm-compressor`](https://github.com/vllm-project/llm-compressor/tree/main/examples/awq). For the recommended quantization workflow, please see the AWQ examples in [`llm-compressor`](https://github.com/vllm-project/llm-compressor/tree/main/examples/awq). For more details on the deprecation, refer to the original [AutoAWQ repository](https://github.com/casper-hansen/AutoAWQ).

To create a new 4-bit quantized model, you can leverage [AutoAWQ](https://github.com/casper-hansen/AutoAWQ). Quantization reduces the model\'s precision from BF16/FP16 to INT4 which effectively reduces the total model memory footprint. The main benefits are lower latency and memory usage.

You can quantize your own models by installing AutoAWQ or picking one of the [6500+ models on Huggingface](https://huggingface.co/models?search=awq).

    pip install autoawq

After installing AutoAWQ, you are ready to quantize a model. Please refer to the [AutoAWQ documentation](https://casper-hansen.github.io/AutoAWQ/examples/#basic-quantization) for further details. Here is an example of how to quantize `mistralai/Mistral-7B-Instruct-v0.2`:

Code

    from awq import AutoAWQForCausalLM
    from transformers import AutoTokenizer

    model_path = "mistralai/Mistral-7B-Instruct-v0.2"
    quant_path = "mistral-instruct-v0.2-awq"
    quant_config = 

    # Load model
    model = AutoAWQForCausalLM.from_pretrained(
        model_path,
        low_cpu_mem_usage=True,
        use_cache=False,
    )
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

    # Quantize
    model.quantize(tokenizer, quant_config=quant_config)

    # Save quantized model
    model.save_quantized(quant_path)
    tokenizer.save_pretrained(quant_path)

    print(f'Model is quantized and saved at ""')

To run an AWQ model with vLLM, you can use [TheBloke/Llama-2-7b-Chat-AWQ](https://huggingface.co/TheBloke/Llama-2-7b-Chat-AWQ) with the following command:

    python examples/offline_inference/llm_engine_example.py \
        --model TheBloke/Llama-2-7b-Chat-AWQ \
        --quantization awq

AWQ models are also supported directly through the LLM entrypoint:

Code

    from vllm import LLM, SamplingParams

    # Sample prompts.
    prompts = [
        "Hello, my name is",
        "The president of the United States is",
        "The capital of France is",
        "The future of AI is",
    ]
    # Create a sampling params object.
    sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

    # Create an LLM.
    llm = LLM(model="TheBloke/Llama-2-7b-Chat-AWQ", quantization="AWQ")
    # Generate texts from the prompts. The output is a list of RequestOutput objects
    # that contain the prompt, generated text, and other information.
    outputs = llm.generate(prompts, sampling_params)
    # Print the outputs.
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: , Generated text: ")

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [October 15, 2025] ]