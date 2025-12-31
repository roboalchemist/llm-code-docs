# Source: https://docs.vllm.ai/en/stable/features/quantization/fp8/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/features/quantization/fp8.md "Edit this page")

# FP8 W8A8[¶](#fp8-w8a8 "Permanent link")

vLLM supports FP8 (8-bit floating point) weight and activation quantization using hardware acceleration on GPUs such as Nvidia H100 and AMD MI300x. Currently, only Hopper and Ada Lovelace GPUs are officially supported for W8A8. Ampere GPUs are supported for W8A16 (weight-only FP8) utilizing Marlin kernels. Quantization of models with FP8 allows for a 2x reduction in model memory requirements and up to a 1.6x improvement in throughput with minimal impact on accuracy.

Please visit the HF collection of [quantized FP8 checkpoints of popular LLMs ready to use with vLLM](https://huggingface.co/collections/neuralmagic/fp8-llms-for-vllm-666742ed2b78b7ac8df13127).

The FP8 types typically supported in hardware have two distinct representations, each useful in different scenarios:

-   **E4M3**: Consists of 1 sign bit, 4 exponent bits, and 3 bits of mantissa. It can store values up to +/-448 and `nan`.
-   **E5M2**: Consists of 1 sign bit, 5 exponent bits, and 2 bits of mantissa. It can store values up to +/-57344, +/- `inf`, and `nan`. The tradeoff for the increased dynamic range is lower precision of the stored values.

Note

FP8 computation is supported on NVIDIA GPUs with compute capability \> 8.9 (Ada Lovelace, Hopper). FP8 models will run on compute capability \> 8.0 (Ampere) as weight-only W8A16, utilizing FP8 Marlin.

## Installation[¶](#installation "Permanent link")

To produce performant FP8 quantized models with vLLM, you\'ll need to install the [llm-compressor](https://github.com/vllm-project/llm-compressor/) library:

    pip install llmcompressor

## Quantization Process[¶](#quantization-process "Permanent link")

The quantization process involves three main steps:

1.  Loading the model
2.  Applying quantization
3.  Evaluating accuracy in vLLM

### 1. Loading the Model[¶](#1-loading-the-model "Permanent link") 

Load your model and tokenizer using the standard `transformers` AutoModel classes:

    from transformers import AutoTokenizer, AutoModelForCausalLM

    MODEL_ID = "meta-llama/Meta-Llama-3-8B-Instruct"
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        device_map="auto",
        dtype="auto",
    )
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

### 2. Applying Quantization[¶](#2-applying-quantization "Permanent link") 

For FP8 quantization, we can recover accuracy with simple RTN quantization. We recommend targeting all `Linear` layers using the `FP8_DYNAMIC` scheme, which uses:

-   Static, per-channel quantization on the weights
-   Dynamic, per-token quantization on the activations

Since simple RTN does not require data for weight quantization and the activations are quantized dynamically, we do not need any calibration data for this quantization flow.

Code

    from llmcompressor import oneshot
    from llmcompressor.modifiers.quantization import QuantizationModifier

    # Configure the simple PTQ quantization
    recipe = QuantizationModifier(
        targets="Linear",
        scheme="FP8_DYNAMIC",
        ignore=["lm_head"],
    )

    # Apply the quantization algorithm.
    oneshot(model=model, recipe=recipe)

    # Save the model: Meta-Llama-3-8B-Instruct-FP8-Dynamic
    SAVE_DIR = MODEL_ID.split("/")[1] + "-FP8-Dynamic"
    model.save_pretrained(SAVE_DIR)
    tokenizer.save_pretrained(SAVE_DIR)

### 3. Evaluating Accuracy[¶](#3-evaluating-accuracy "Permanent link") 

Install `vllm` and `lm-evaluation-harness` for evaluation:

    pip install vllm git+https://github.com/EleutherAI/lm-evaluation-harness.git@206b7722158f58c35b7ffcd53b035fdbdda5126d#egg=lm-eval[api]

Load and run the model in `vllm`:

    from vllm import LLM

    llm = LLM("./Meta-Llama-3-8B-Instruct-FP8-Dynamic")
    result = llm.generate("Hello my name is")
    print(result[0].outputs[0].text)

Evaluate accuracy with `lm_eval` (for example on 250 samples of `gsm8k`):

Note

Quantized models can be sensitive to the presence of the `bos` token. `lm_eval` does not add a `bos` token by default, so make sure to include the `add_bos_token=True` argument when running your evaluations.

    MODEL=$PWD/Meta-Llama-3-8B-Instruct-FP8-Dynamic
    lm_eval \
      --model vllm \
      --model_args pretrained=$MODEL,add_bos_token=True \
      --tasks gsm8k  --num_fewshot 5 --batch_size auto --limit 250

Here\'s an example of the resulting scores:

    |Tasks|Version|     Filter     |n-shot|  Metric   |   |Value|   |Stderr|
    |-----|------:|----------------|-----:|-----------|---|----:|---|-----:|
    |gsm8k|      3|flexible-extract|     5|exact_match|↑  |0.768|±  |0.0268|
    |     |       |strict-match    |     5|exact_match|↑  |0.768|±  |0.0268|

## Troubleshooting and Support[¶](#troubleshooting-and-support "Permanent link")

If you encounter any issues or have feature requests, please open an issue on the [vllm-project/llm-compressor](https://github.com/vllm-project/llm-compressor/issues) GitHub repository.

## Online Dynamic Quantization[¶](#online-dynamic-quantization "Permanent link")

Dynamic quantization of an original precision BF16/FP16 model to FP8 can be achieved with vLLM without any calibration data required. You can enable the feature by specifying `--quantization="fp8"` in the command line or setting `quantization="fp8"` in the LLM constructor.

In this mode, all Linear modules (except for the final `lm_head`) have their weights quantized down to FP8_E4M3 precision with a per-tensor scale. Activations have their minimum and maximum values calculated during each forward pass to provide a dynamic per-tensor scale for high accuracy. As a result, latency improvements are limited in this mode.

    from vllm import LLM

    llm = LLM("facebook/opt-125m", quantization="fp8")
    # INFO 06-10 17:55:42 model_runner.py:157] Loading model weights took 0.1550 GB
    result = llm.generate("Hello, my name is")
    print(result[0].outputs[0].text)

Warning

Currently, we load the model at original precision before quantizing down to 8-bits, so you need enough memory to load the whole model.

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [November 19, 2025] ]