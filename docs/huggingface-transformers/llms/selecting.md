# Source: https://huggingface.co/docs/transformers/v5.0.0/quantization/selecting.md

# Selecting a quantization method

There are many quantization methods available in Transformers for inference and fine-tuning. This guide helps you choose the most common and production-ready quantization techniques depending on your use case, and presents the advantages and disadvantages of each technique.

For a comprehensive overview of all supported methods and their features, refer back to the table in the [Overview](./overview).

## Inference

Consider the quantization methods below for inference.

| quantization method | use case |
|---|---|
| bitsandbytes | ease of use and QLoRA fine-tuning on NVIDIA and Intel GPUs |
| compressed-tensors | loading specific quantized formats (FP8, Sparse) |
| GPTQModel or AWQ | good 4-bit accuracy with upfront calibration |
| HQQ | fast on the fly quantization without calibration |
| torchao | flexibility and fast inference with torch.compile |

### No Calibration Required (On-the-fly Quantization)

These methods are generally easier to use as they don't need a separate calibration dataset or step.

#### bitsandbytes

| Pros                                                         | Cons                                                    |
|--------------------------------------------------------------|---------------------------------------------------------|
| Very simple, no calibration dataset required for inference.  | Primarily optimized for NVIDIA GPUs (CUDA).             |
| Good community support and widely adopted.                   | Inference speedup isn't guaranteed.                     |

See the [bitsandbytes documentation](./bitsandbytes) for more details.

#### HQQ (Half-Quadratic Quantization)

| Pros                                                                 | Cons                                                                       |
|----------------------------------------------------------------------|----------------------------------------------------------------------------|
| Fast quantization process, no calibration data needed.              | Accuracy can degrade significantly at bit depths 

The key takeaways are:

| Quantization & Methods                      | Memory Savings (vs bf16) | Accuracy             | Other Notes                                                        |
|-------------------------------------------- |------------------------- |--------------------- |------------------------------------------------------------------- |
| **8-bit** (bnb-int8, HQQ, Quanto, torchao, fp8) | ~2x             | Very close to baseline bf16 model   |                                                                    |
| **4-bit** (AWQ, GPTQ, HQQ, bnb-nf4)    | ~4x                      | Relatively high accuracy            | AWQ/GPTQ often lead in accuracy but need calibration. HQQ/bnb-nf4 are easy on-the-fly. |
| **Sub-4-bit** (VPTQ, AQLM, 2-bit GPTQ) | Extreme (>4x)            | Noticeable drop, especially at 2-bit | Quantization times can be very long (AQLM, VPTQ). Performance varies. |

> [!TIP]
> Always benchmark the performance (accuracy and speed) of the quantized model on your specific task and hardware to ensure it meets your requirements. Refer to the individual documentation pages linked above for detailed usage instructions.

