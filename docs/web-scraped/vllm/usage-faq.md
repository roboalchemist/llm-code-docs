# Source: https://docs.vllm.ai/en/stable/usage/faq/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/usage/faq.md "Edit this page")

# Frequently Asked Questions[¶](#frequently-asked-questions "Permanent link")

> Q: How can I serve multiple models on a single port using the OpenAI API?

A: Assuming that you\'re referring to using OpenAI compatible server to serve multiple models at once, that is not currently supported, you can run multiple instances of the server (each serving a different model) at the same time, and have another layer to route the incoming request to the correct server accordingly.

------------------------------------------------------------------------

> Q: Which model to use for offline inference embedding?

A: You can try [e5-mistral-7b-instruct](https://huggingface.co/intfloat/e5-mistral-7b-instruct) and [BAAI/bge-base-en-v1.5](https://huggingface.co/BAAI/bge-base-en-v1.5); more are listed [here](../../models/supported_models/).

By extracting hidden states, vLLM can automatically convert text generation models like [Llama-3-8B](https://huggingface.co/meta-llama/Meta-Llama-3-8B), [Mistral-7B-Instruct-v0.3](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3) into embedding models, but they are expected to be inferior to models that are specifically trained on embedding tasks.

------------------------------------------------------------------------

> Q: Can the output of a prompt vary across runs in vLLM?

A: Yes, it can. vLLM does not guarantee stable log probabilities (logprobs) for the output tokens. Variations in logprobs may occur due to numerical instability in Torch operations or non-deterministic behavior in batched Torch operations when batching changes. For more details, see the [Numerical Accuracy section](https://pytorch.org/docs/stable/notes/numerical_accuracy.html#batched-computations-or-slice-computations).

In vLLM, the same requests might be batched differently due to factors such as other concurrent requests, changes in batch size, or batch expansion in speculative decoding. These batching variations, combined with numerical instability of Torch operations, can lead to slightly different logit/logprob values at each step. Such differences can accumulate, potentially resulting in different tokens being sampled. Once a different token is sampled, further divergence is likely.

## Mitigation Strategies[¶](#mitigation-strategies "Permanent link")

-   For improved stability and reduced variance, use `float32`. Note that this will require more memory.
-   If using `bfloat16`, switching to `float16` can also help.
-   Using request seeds can aid in achieving more stable generation for temperature \> 0, but discrepancies due to precision differences may still occur.

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [July 8, 2025] ]