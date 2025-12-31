# Source: https://docs.vllm.ai/en/stable/contributing/model/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/contributing/model/README.md "Edit this page")

# Summary[¶](#summary "Permanent link")

Important

Many decoder language models can now be automatically loaded using the [Transformers modeling backend](../../models/supported_models/#transformers) without having to implement them in vLLM. See if `vllm serve <model>` works first!

vLLM models are specialized [PyTorch](https://pytorch.org/) models that take advantage of various [features](../../features/#compatibility-matrix) to optimize their performance.

The complexity of integrating a model into vLLM depends heavily on the model\'s architecture. The process is considerably straightforward if the model shares a similar architecture with an existing model in vLLM. However, this can be more complex for models that include new operators (e.g., a new attention mechanism).

Read through these pages for a step-by-step guide:

-   [Basic Model](basic/)
-   [Registering a Model](registration/)
-   [Unit Testing](tests/)
-   [Multi-Modal Support](multimodal/)
-   [Speech-to-Text Support](transcription/)

Tip

If you are encountering issues while integrating your model into vLLM, feel free to open a [GitHub issue](https://github.com/vllm-project/vllm/issues) or ask on our [developer slack](https://slack.vllm.ai). We will be happy to help you out!

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [November 14, 2025] ]