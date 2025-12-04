# Source: https://onnxruntime.ai/docs/genai/

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#onnx-runtime-generate-api) ONNX Runtime generate() API

*Note: this API is in preview and is subject to change.*

Run generative AI models with ONNX Runtime.

See the source code here: <https://github.com/microsoft/onnxruntime-genai>

This library provides the generative AI loop for ONNX models, including tokenization and other pre-processing, inference with ONNX Runtime, logits processing, search and sampling, and KV cache management.

Users can call a high level `generate()` method, or run each iteration of the model in a loop, generating one token at a time, and optionally updating generation parameters inside the loop.

It has support for greedy/beam search and TopP, TopK sampling to generate token sequences and built-in logits processing like repetition penalties. You can also easily add custom scoring.

Other supported features include applying chat templates and structured output (for tool calling)

------------------------------------------------------------------------

## Table of contents 

- [Tutorials](/docs/genai/tutorials/)
- [API docs](/docs/genai/api/)
- [How to](/docs/genai/howto/)
- [Reference](/docs/genai/reference/)