# Source: https://docs.vllm.ai/en/stable/features/quantization/int8/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/features/quantization/int8.md "Edit this page")

# INT8 W8A8[¶](#int8-w8a8 "Permanent link")

vLLM supports quantizing weights and activations to INT8 for memory savings and inference acceleration. This quantization method is particularly useful for reducing model size while maintaining good performance.

Please visit the HF collection of [quantized INT8 checkpoints of popular LLMs ready to use with vLLM](https://huggingface.co/collections/neuralmagic/int8-llms-for-vllm-668ec32c049dca0369816415).

Note

INT8 computation is supported on NVIDIA GPUs with compute capability \> 7.5 (Turing, Ampere, Ada Lovelace, Hopper).

Warning

**Blackwell GPU Limitation**: INT8 is not supported on compute capability \>= 100 (e.g., RTX 6000 Blackwell). Use [FP8 quantization](../fp8/) instead, or run on Hopper/Ada/Ampere architectures.

## Prerequisites[¶](#prerequisites "Permanent link")

To use INT8 quantization with vLLM, you\'ll need to install the [llm-compressor](https://github.com/vllm-project/llm-compressor/) library:

    pip install llmcompressor

Additionally, install `vllm` and `lm-evaluation-harness` for evaluation:

    pip install vllm git+https://github.com/EleutherAI/lm-evaluation-harness.git@206b7722158f58c35b7ffcd53b035fdbdda5126d#egg=lm-eval[api]

## Quantization Process[¶](#quantization-process "Permanent link")

The quantization process involves four main steps:

1.  Loading the model
2.  Preparing calibration data
3.  Applying quantization
4.  Evaluating accuracy in vLLM

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

### 2. Preparing Calibration Data[¶](#2-preparing-calibration-data "Permanent link") 

When quantizing activations to INT8, you need sample data to estimate the activation scales. It\'s best to use calibration data that closely matches your deployment data. For a general-purpose instruction-tuned model, you can use a dataset like `ultrachat`:

Code

    from datasets import load_dataset

    NUM_CALIBRATION_SAMPLES = 512
    MAX_SEQUENCE_LENGTH = 2048

    # Load and preprocess the dataset
    ds = load_dataset("HuggingFaceH4/ultrachat_200k", split="train_sft")
    ds = ds.shuffle(seed=42).select(range(NUM_CALIBRATION_SAMPLES))

    def preprocess(example):
        return 
    ds = ds.map(preprocess)

    def tokenize(sample):
        return tokenizer(sample["text"], padding=False, max_length=MAX_SEQUENCE_LENGTH, truncation=True, add_special_tokens=False)
    ds = ds.map(tokenize, remove_columns=ds.column_names)

### 3. Applying Quantization[¶](#3-applying-quantization "Permanent link") 

Now, apply the quantization algorithms:

Code

    from llmcompressor import oneshot
    from llmcompressor.modifiers.quantization import GPTQModifier
    from llmcompressor.modifiers.smoothquant import SmoothQuantModifier

    # Configure the quantization algorithms
    recipe = [
        SmoothQuantModifier(smoothing_strength=0.8),
        GPTQModifier(targets="Linear", scheme="W8A8", ignore=["lm_head"]),
    ]

    # Apply quantization
    oneshot(
        model=model,
        dataset=ds,
        recipe=recipe,
        max_seq_length=MAX_SEQUENCE_LENGTH,
        num_calibration_samples=NUM_CALIBRATION_SAMPLES,
    )

    # Save the compressed model: Meta-Llama-3-8B-Instruct-W8A8-Dynamic-Per-Token
    SAVE_DIR = MODEL_ID.split("/")[1] + "-W8A8-Dynamic-Per-Token"
    model.save_pretrained(SAVE_DIR, save_compressed=True)
    tokenizer.save_pretrained(SAVE_DIR)

This process creates a W8A8 model with weights and activations quantized to 8-bit integers.

### 4. Evaluating Accuracy[¶](#4-evaluating-accuracy "Permanent link") 

After quantization, you can load and run the model in vLLM:

    from vllm import LLM

    llm = LLM("./Meta-Llama-3-8B-Instruct-W8A8-Dynamic-Per-Token")

To evaluate accuracy, you can use `lm_eval`:

    lm_eval --model vllm \
      --model_args pretrained="./Meta-Llama-3-8B-Instruct-W8A8-Dynamic-Per-Token",add_bos_token=true \
      --tasks gsm8k \
      --num_fewshot 5 \
      --limit 250 \
      --batch_size 'auto'

Note

Quantized models can be sensitive to the presence of the `bos` token. Make sure to include the `add_bos_token=True` argument when running evaluations.

## Best Practices[¶](#best-practices "Permanent link")

-   Start with 512 samples for calibration data (increase if accuracy drops)
-   Use a sequence length of 2048 as a starting point
-   Employ the chat template or instruction template that the model was trained with
-   If you\'ve fine-tuned a model, consider using a sample of your training data for calibration

## Troubleshooting and Support[¶](#troubleshooting-and-support "Permanent link")

If you encounter any issues or have feature requests, please open an issue on the [vllm-project/llm-compressor](https://github.com/vllm-project/llm-compressor/issues) GitHub repository.

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [November 19, 2025] ]