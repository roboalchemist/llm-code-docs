# Source: https://docs.vllm.ai/en/stable/features/quantization/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/features/quantization/README.md "Edit this page")

# Quantization[¶](#quantization "Permanent link")

Quantization trades off model precision for smaller memory footprint, allowing large models to be run on a wider range of devices.

Contents:

-   [AutoAWQ](auto_awq/)
-   [AutoRound](auto_round/)
-   [BitsAndBytes](bnb/)
-   [BitBLAS](bitblas/)
-   [GGUF](gguf/)
-   [GPTQModel](gptqmodel/)
-   [INC](inc/)
-   [INT4 W4A16](int4/)
-   [INT8 W8A8](int8/)
-   [FP8 W8A8](fp8/)
-   [NVIDIA Model Optimizer](modelopt/)
-   [AMD Quark](quark/)
-   [Quantized KV Cache](quantized_kvcache/)
-   [TorchAO](torchao/)

## Supported Hardware[¶](#supported-hardware "Permanent link")

The table below shows the compatibility of various quantization implementations with different hardware platforms in vLLM:

  Implementation          Volta   Turing   Ampere   Ada   Hopper   AMD GPU   Intel GPU   Intel Gaudi   x86 CPU
  ----------------------- ------- -------- -------- ----- -------- --------- ----------- ------------- ---------
  AWQ                     ❌      ✅︎       ✅︎       ✅︎    ✅︎       ❌        ✅︎          ❌            ✅︎
  GPTQ                    ✅︎      ✅︎       ✅︎       ✅︎    ✅︎       ❌        ✅︎          ❌            ✅︎
  Marlin (GPTQ/AWQ/FP8)   ❌      ❌       ✅︎       ✅︎    ✅︎       ❌        ❌          ❌            ❌
  INT8 (W8A8)             ❌      ✅︎       ✅︎       ✅︎    ✅︎       ❌        ❌          ❌            ✅︎
  FP8 (W8A8)              ❌      ❌       ❌       ✅︎    ✅︎       ✅︎        ❌          ❌            ❌
  BitBLAS                 ✅︎      ✅       ✅︎       ✅︎    ✅︎       ❌        ❌          ❌            ❌
  BitBLAS (GPTQ)          ❌      ❌       ✅︎       ✅︎    ✅︎       ❌        ❌          ❌            ❌
  bitsandbytes            ✅︎      ✅︎       ✅︎       ✅︎    ✅︎       ❌        ❌          ❌            ❌
  DeepSpeedFP             ✅︎      ✅︎       ✅︎       ✅︎    ✅︎       ❌        ❌          ❌            ❌
  GGUF                    ✅︎      ✅︎       ✅︎       ✅︎    ✅︎       ✅︎        ❌          ❌            ❌
  INC (W8A8)              ❌      ❌       ❌       ❌    ❌       ❌        ❌          ✅︎            ❌

-   Volta refers to SM 7.0, Turing to SM 7.5, Ampere to SM 8.0/8.6, Ada to SM 8.9, and Hopper to SM 9.0.
-   ✅︎ indicates that the quantization method is supported on the specified hardware.
-   ❌ indicates that the quantization method is not supported on the specified hardware.

Note

For information on quantization support on Google TPU, please refer to the [TPU-Inference Recommended Models and Features](https://docs.vllm.ai/projects/tpu/en/latest/recommended_models_features/) documentation.

Note

This compatibility chart is subject to change as vLLM continues to evolve and expand its support for different hardware platforms and quantization methods.

For the most up-to-date information on hardware support and quantization methods, please refer to [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] vllm/model_executor/layers/quantization](https://github.com/vllm-project/vllm/tree/main/vllm/model_executor/layers/quantization) or consult with the vLLM development team.

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [December 8, 2025] ]