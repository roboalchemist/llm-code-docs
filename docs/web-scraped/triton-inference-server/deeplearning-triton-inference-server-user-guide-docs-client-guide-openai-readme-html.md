# Source: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html

Title: OpenAI-Compatible Frontend for Triton Inference Server — NVIDIA Triton Inference Server

URL Source: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html

Published Time: Sat, 28 Feb 2026 01:09:17 GMT

Markdown Content:
OpenAI-Compatible Frontend for Triton Inference Server — NVIDIA Triton Inference Server
===============

[Skip to main content](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#main-content)

Back to top- [x] - [x] 

Ctrl+K

[![Image 1: NVIDIA Triton Inference Server - Home](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_static/nvidia-logo-horiz-rgb-blk-for-screen.svg) NVIDIA Triton Inference Server](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/contents.html)

*   [GitHub](https://github.com/triton-inference-server/server "GitHub")

[![Image 2: NVIDIA Triton Inference Server - Home](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_static/nvidia-logo-horiz-rgb-blk-for-screen.svg) NVIDIA Triton Inference Server](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/contents.html)

*   [GitHub](https://github.com/triton-inference-server/server "GitHub")

Table of Contents

*   [Home](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/introduction/index.html)
*   [Release notes](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/introduction/release_notes.html)
*   [Compatibility matrix](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/introduction/compatibility.html)

Getting Started

*   [Quick Deployment Guide by backend](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/getting_started/quick_deployment.html)

    *   [Quickstart](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/getting_started/quickstart.html)
    *   [TRT-LLM](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/getting_started/llm.html)
    *   [vLLM](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Popular_Models_Guide/Llama2/vllm_guide.html)
    *   [Python with HuggingFace](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Quick_Deploy/HuggingFaceTransformers/README.html)
    *   [PyTorch](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Quick_Deploy/PyTorch/README.html)
    *   [ONNX](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Quick_Deploy/ONNX/README.html)
    *   [Openvino](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Quick_Deploy/OpenVINO/README.html)

*   [LLM With TensorRT-LLM](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/getting_started/trtllm_user_guide.html)
*   [Multimodal model](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Popular_Models_Guide/Llava1.5/llava_trtllm_guide.html)
*   [Stable diffusion](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Popular_Models_Guide/StableDiffusion/README.html)

Scaling guide

*   [Multi-Node (AWS)](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Deployment/Kubernetes/EKS_Multinode_Triton_TRTLLM/README.html)
*   [Multi-Instance](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Deployment/Kubernetes/TensorRT-LLM_Autoscaling_and_Load_Balancing/README.html)

LLM Features

*   [Constrained Decoding](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Constrained_Decoding/README.html)
*   [Function Calling](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Function_Calling/README.html)
*   [Speculative Decoding](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/llm_features/speculative_decoding.html)

    *   [Overview](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/README.html)
    *   [TRT-LLM](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html)
    *   [vLLM](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/vLLM/README.html)

Client

*   [API Reference](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/api_reference.html)

    *   [OpenAI API](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#)
    *   [KServe API](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/kserve.html)

        *   [HTTP/REST and GRPC Protocol](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/customization_guide/inference_protocols.html)
        *   [Extensions](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/kserve_extension.html)

            *   [Binary tensor data extension](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/protocol/extension_binary_data.html)
            *   [Classification extension](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/protocol/extension_classification.html)
            *   [Schedule policy extension](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/protocol/extension_schedule_policy.html)
            *   [Sequence extension](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/protocol/extension_sequence.html)
            *   [Shared-memory extension](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/protocol/extension_shared_memory.html)
            *   [Model configuration extension](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/protocol/extension_model_configuration.html)
            *   [Model repository extension](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/protocol/extension_model_repository.html)
            *   [Statistics extension](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/protocol/extension_statistics.html)
            *   [Trace extension](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/protocol/extension_trace.html)
            *   [Logging extension](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/protocol/extension_logging.html)
            *   [Parameters extension](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/protocol/extension_parameters.html)

*   [In-Process Triton Server API](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/in_process.html)

    *   [C/C++](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/customization_guide/inprocess_c_api.html)
    *   [Python](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/python.html)

        *   [Overview](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/README.html)
        *   [Kafka I/O](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/examples/kafka-io/README.html)
        *   [Rayserve](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Triton_Inference_Server_Python_API/examples/rayserve/README.html)

    *   [Java](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/customization_guide/inprocess_java_api.html)

*   [Client Libraries](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html)
*   [Python tritonclient Package API](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient_api.html)

    *   [tritonclient](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.html)

        *   [tritonclient.grpc](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.html)

            *   [tritonclient.grpc.aio](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.aio.html)
            *   [tritonclient.grpc.auth](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.grpc.auth.html)

        *   [tritonclient.http](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.html)

            *   [tritonclient.http.aio](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.aio.html)
            *   [tritonclient.http.auth](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.auth.html)

        *   [tritonclient.utils](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html)

            *   [tritonclient.utils.cuda_shared_memory](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.cuda_shared_memory.html)
            *   [tritonclient.utils.shared_memory](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.shared_memory.html)

Server

*   [Concurrent Model Execution](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/model_execution.html)
*   [Scheduler](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/scheduler.html)
*   [Batcher](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/batcher.html)
*   [Model Pipelines](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/server_guide/model_pipelines.html)

    *   [Ensemble](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/ensemble_models.html)
    *   [Business Logic Scripting](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/bls.html)

*   [State Management](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/server_guide/state_management.html)

    *   [Implicit State Management](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/implicit_state_management.html)

*   [Request Cancellation](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/request_cancellation.html)
*   [Rate Limiter](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/rate_limiter.html)
*   [Caching](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/response_cache.html)
*   [Metrics](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/metrics.html)
*   [Tracing](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/trace.html)

Model Management

*   [Repository](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/model_repository.html)
*   [Configuration](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/model_configuration.html)
*   [Optimization](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/optimization.html)
*   [Controls](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/model_management.html)
*   [Decoupled models](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/decoupled_models.html)
*   [Custom operators](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/custom_operations.html)

Backends

*   [TensorRT-LLM](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tensorrtllm_backend/README.html)
*   [vLLM](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/backend_guide/vllm.html)

    *   [vLLM Backend](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/vllm_backend/README.html)
    *   [Multi-LoRA](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/vllm_backend/docs/llama_multi_lora_tutorial.html)

*   [Python Backend](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/python_backend/README.html)
*   [PyTorch](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/pytorch_backend/README.html)
*   [ONNX Runtime](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/onnxruntime_backend/README.html)
*   [TensorRT](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tensorrt_backend/README.html)
*   [FIL](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/fil_backend/README.html)
*   [DALI](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/dali_backend/README.html)
*   [Custom](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/backend/README.html)

Performance benchmarking and tuning

*   [GenAI Perf Analyzer](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_benchmark/genai_perf.html)

    *   [Overview](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html)
    *   [Large language models](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/docs/tutorial.html)
    *   [Visual language models](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/docs/multi_modal.html)
    *   [Embedding models](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/docs/embeddings.html)
    *   [Ranking models](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/docs/rankings.html)
    *   [Multiple LoRA adapters](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/docs/lora.html)

*   [Performance Analyzer](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_benchmark/perf_analyzer.html)

    *   [Triton Performance Analyzer](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/README.html)
    *   [Documentation](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/docs/README.html)
    *   [Quick Start](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/docs/quick_start.html)
    *   [Recommended Installation Method](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/docs/install.html)
    *   [CLI Reference](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/docs/cli.html)
    *   [Inference Load Modes](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/docs/inference_load_modes.html)
    *   [Input Data](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/docs/input_data.html)
    *   [Measurement Modes](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/docs/measurements_metrics.html)
    *   [Benchmarking Triton via HTTP or gRPC endpoint](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/docs/benchmarking.html)

*   [Model Analyzer](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_benchmark/model_analyzer.html)

    *   [Triton Model Analyzer](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/model_analyzer/README.html)
    *   [Documentation](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/model_analyzer/docs/README.html)
    *   [Quick Start](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/model_analyzer/docs/quick_start.html)
    *   [Recommended Installation Method](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/model_analyzer/docs/install.html)
    *   [CLI Reference](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/model_analyzer/docs/cli.html)
    *   [Launch Modes](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/model_analyzer/docs/launch_modes.html)
    *   [Table of Contents](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/model_analyzer/docs/config.html)
    *   [Table of Contents](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/model_analyzer/docs/config_search.html)
    *   [Metrics](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/model_analyzer/docs/metrics.html)
    *   [Checkpointing](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/model_analyzer/docs/checkpoints.html)
    *   [Reports](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/model_analyzer/docs/report.html)
    *   [Kubernetes](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/model_analyzer/docs/kubernetes_deploy.html)
    *   [Model Types](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/model_analyzer/docs/model_types.html)
    *   [Ensemble Model](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/model_analyzer/docs/ensemble_quick_start.html)
    *   [BLS Model](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/model_analyzer/docs/bls_quick_start.html)
    *   [Multi-Model](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/model_analyzer/docs/mm_quick_start.html)

*   [Model Navigator](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/model_navigator/README.html)

Debugging

*   [Guide](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/debugging_guide.html)

*   [](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/contents.html)
*   [API Reference](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/api_reference.html)
*   OpenAI-Compa...

OpenAI-Compatible Frontend for Triton Inference Server[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#openai-compatible-frontend-for-triton-inference-server "Link to this heading")
=====================================================================================================================================================================================================================================================

Pre-requisites[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#pre-requisites "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

1.   Docker + NVIDIA Container Runtime

2.   A correctly configured `HF_TOKEN` for access to HuggingFace models.

    *   The current examples and testing primarily use the [`meta-llama/Meta-Llama-3.1-8B-Instruct`](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct) model, but you can manually bring your own models and adjust accordingly.

VLLM[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#vllm "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------

1.   Launch the container and install dependencies:

*   Mounts the `~/.huggingface/cache` for re-use of downloaded models across runs, containers, etc.

*   Sets the [`HF_TOKEN`](https://huggingface.co/docs/huggingface_hub/en/package_reference/environment_variables#hftoken) environment variable to access gated models, make sure this is set in your local environment if needed.

docker run -it --net=host --gpus all --rm \
 -v ${HOME}/.cache/huggingface:/root/.cache/huggingface \
 -e HF_TOKEN \
 nvcr.io/nvidia/tritonserver:26.02-vllm-python-py3

1.   Launch the OpenAI-compatible Triton Inference Server:

cd /opt/tritonserver/python/openai

# NOTE: Adjust the --tokenizer based on the model being used
python3 openai_frontend/main.py --model-repository tests/vllm_models --tokenizer meta-llama/Meta-Llama-3.1-8B-Instruct

Example output

...
+-----------------------+---------+--------+
| Model                 | Version | Status |
+-----------------------+---------+--------+
| llama-3.1-8b-instruct | 1       | READY  | <- Correct Model Loaded in Triton
+-----------------------+---------+--------+
...
Found model: name='llama-3.1-8b-instruct', backend='vllm'
[WARNING] Adding CORS for the following origins: ['http://localhost']
INFO:     Started server process [126]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:9000 (Press CTRL+C to quit) <- OpenAI Frontend Started Successfully

1.   Send a `/v1/chat/completions` request:

*   Note the use of `jq` is optional, but provides a nicely formatted output for JSON responses.

MODEL="llama-3.1-8b-instruct"
curl -s http://localhost:9000/v1/chat/completions -H 'Content-Type: application/json' -d '{
 "model": "'${MODEL}'",
 "messages": [{"role": "user", "content": "Say this is a test!"}]
}' | jq

Example output

{
 "id": "cmpl-0242093d-51ae-11f0-b339-e7480668bfbe",
 "choices": [
 {
 "finish_reason": "stop",
 "index": 0,
 "message":
 {
 "content": "This is only a test.",
 "tool_calls": null,
 "role": "assistant",
 "function_call": null
 },
 "logprobs": null
 }
 ],
 "created": 1750846825,
 "model": "llama-3.1-8b-instruct",
 "system_fingerprint": null,
 "object": "chat.completion",
 "usage": {
 "completion_tokens": 7,
 "prompt_tokens": 42,
 "total_tokens": 49
 }
}

1.   Send a `/v1/completions` request:

*   Note the use of `jq` is optional, but provides a nicely formatted output for JSON responses.

MODEL="llama-3.1-8b-instruct"
curl -s http://localhost:9000/v1/completions -H 'Content-Type: application/json' -d '{
 "model": "'${MODEL}'",
 "prompt": "Machine learning is"
}' | jq

Example output

{
 "id": "cmpl-58fba3a0-51ae-11f0-859d-e7480668bfbe",
 "choices": [
 {
 "finish_reason": "stop",
 "index": 0,
 "logprobs": null,
 "text": " an amazing field that can truly understand the hidden patterns that exist in the data,"
 }
 ],
 "created": 1750846970,
 "model": "llama-3.1-8b-instruct",
 "system_fingerprint": null,
 "object": "text_completion",
 "usage": {
 "completion_tokens": 16,
 "prompt_tokens": 4,
 "total_tokens": 20
 }
}

1.   Benchmark with `genai-perf`:

*   To install genai-perf in this container, see the instructions [here](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#install-genai-perf-ubuntu-24-04-python-3-10)

*   Or try using genai-perf from the [SDK container](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/tritonserver)

MODEL="llama-3.1-8b-instruct"
TOKENIZER="meta-llama/Meta-Llama-3.1-8B-Instruct"
genai-perf profile \
 --model ${MODEL} \
 --tokenizer ${TOKENIZER} \
 --service-kind openai \
 --endpoint-type chat \
 --url localhost:9000 \
 --streaming

Example output

2024-10-14 22:43 [INFO] genai_perf.parser:82 - Profiling these models: llama-3.1-8b-instruct
2024-10-14 22:43 [INFO] genai_perf.wrapper:163 - Running Perf Analyzer : 'perf_analyzer -m llama-3.1-8b-instruct --async --input-data artifacts/llama-3.1-8b-instruct-openai-chat-concurrency1/inputs.json -i http --concurrency-range 1 --endpoint v1/chat/completions --service-kind openai -u localhost:9000 --measurement-interval 10000 --stability-percentage 999 --profile-export-file artifacts/llama-3.1-8b-instruct-openai-chat-concurrency1/profile_export.json'
                              NVIDIA GenAI-Perf | LLM Metrics
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━┓
┃                         Statistic ┃    avg ┃    min ┃    max ┃    p99 ┃    p90 ┃    p75 ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━┩
│          Time to first token (ms) │  71.66 │  64.32 │  86.52 │  76.13 │  74.92 │  73.26 │
│          Inter token latency (ms) │  18.47 │  18.25 │  18.72 │  18.67 │  18.61 │  18.53 │
│              Request latency (ms) │ 348.00 │ 274.60 │ 362.27 │ 355.41 │ 352.29 │ 350.66 │
│            Output sequence length │  15.96 │  12.00 │  16.00 │  16.00 │  16.00 │  16.00 │
│             Input sequence length │ 549.66 │ 548.00 │ 551.00 │ 550.00 │ 550.00 │ 550.00 │
│ Output token throughput (per sec) │  45.84 │    N/A │    N/A │    N/A │    N/A │    N/A │
│      Request throughput (per sec) │   2.87 │    N/A │    N/A │    N/A │    N/A │    N/A │
└───────────────────────────────────┴────────┴────────┴────────┴────────┴────────┴────────┘
2024-10-14 22:44 [INFO] genai_perf.export_data.json_exporter:62 - Generating artifacts/llama-3.1-8b-instruct-openai-chat-concurrency1/profile_export_genai_perf.json
2024-10-14 22:44 [INFO] genai_perf.export_data.csv_exporter:71 - Generating artifacts/llama-3.1-8b-instruct-openai-chat-concurrency1/profile_export_genai_perf.csv

1.   Use the OpenAI python client directly:

from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:9000/v1",
    api_key="EMPTY",
)

model = "llama-3.1-8b-instruct"
completion = client.chat.completions.create(
    model=model,
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {"role": "user", "content": "What are LLMs?"},
    ],
    max_completion_tokens=256,
)

print(completion.choices[0].message.content)

1.   Run tests (NOTE: The server should not be running, the tests will handle starting/stopping the server as necessary):

cd /opt/tritonserver/python/openai/
pip install -r requirements-test.txt

pytest -v tests/

### LoRA Adapters[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#lora-adapters "Link to this heading")

If the command line argument `--lora-separator=<separator_string>` is provided when starting the OpenAI Frontend, a LoRA adaptor listed in `multi_lora.json` may be selected by appending the LoRA name to the model name, separated by the LoRA separator, on the inference request in `<model_name><separator_string><lora_name>` format.

For example

# start server with model named gemma-2b
python3 openai_frontend/main.py --lora-separator=_lora_ ...

# inference without LoRA
curl -s http://localhost:9000/v1/completions -H 'Content-Type: application/json' -d '{
 "model": "gemma-2b",
 "temperature": 0,
 "prompt": "When was the wheel invented?"
}'
{
 ...
 "choices":[{..."text":"\n\nThe wheel was invented by the Sumerians in Mesopotamia around 350"}],
 ...
}

# inference with LoRA named doll
curl -s http://localhost:9000/v1/completions -H 'Content-Type: application/json' -d '{
 "model": "gemma-2b_lora_doll",
 "temperature": 0,
 "prompt": "When was the wheel invented?"
}'
{
 ...
 "choices":[{..."text":"\n\nThe wheel was invented in Mesopotamia around 3500 BC.\n\n"}],
 ...
}

# inference with LoRA named sheep
curl -s http://localhost:9000/v1/completions -H 'Content-Type: application/json' -d '{
 "model": "gemma-2b_lora_sheep",
 "temperature": 0,
 "prompt": "When was the wheel invented?"
}'
{
 ...
 "choices":[{..."text":"\n\nThe wheel was invented around 3000 BC in Mesopotamia.\n\n"}],
 ...
}

When listing or retrieving model(s), the model id will include the LoRA name in the same `<model_name><separator_string><lora_name>` format for each LoRA adapter listed on the `multi_lora.json`. Note: The LoRA name inclusion is limited to locally stored models, inference requests are not limited though.

#### vLLM[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#id1 "Link to this heading")

See the [vLLM documentation](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/vllm_backend/docs/llama_multi_lora_tutorial.html) on how to serve a vLLM model with LoRA adapters.

#### TensorRT-LLM[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#tensorrt-llm "Link to this heading")

Similarly, see [TensorRT-LLM document](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tensorrtllm_backend/docs/lora.html) on how to prepare LoRA-enabled TensorRT-LLM engines and generate LoRA tensors. The path of LoRA adapter in `multi_lora.json` is the directory of `model.lora_config.npy` and `model.lora_weights.npy` tensors.

For example
model repository

inflight_batcher_llm
├── postprocessing
|   ├── 1
|   |   └── model.py
|   └── config.pbtxt
├── preprocessing
|   ├── 1
|   |   └── model.py
|   └── config.pbtxt
├── tensorrt_llm
|   ├── 1
|   |   └── model.py
|   └── config.pbtxt
└── tensorrt_llm_bls
    ├── 1
    |   ├── Japanese-Alpaca-LoRA-7b-v0-weights
    |   |   ├── model.lora_config.npy
    |   |   └── model.lora_weights.npy
    |   ├── luotuo-lora-7b-0.1-weights
    |   |   ├── model.lora_config.npy
    |   |   └── model.lora_weights.npy
    |   ├── model.py
    |   └── multi_lora.json
    └── config.pbtxt

multi_lora.json

{
  "doll": "inflight_batcher_llm/tensorrt_llm_bls/1/luotuo-lora-7b-0.1-weights",
  "sheep": "inflight_batcher_llm/tensorrt_llm_bls/1/Japanese-Alpaca-LoRA-7b-v0-weights"
}

### Embedding Models[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#embedding-models "Link to this heading")

Currently, OpenAI-Compatible Frontend supports loading embedding models and embeddings endpoints via vLLM backend. Check [vLLM supported models](https://docs.vllm.ai/en/latest/models/supported_models.html#embedding) for all supported embedding models from vLLM.

1.   Launch the container and install dependencies:

*   Mounts the `~/.huggingface/cache` for re-use of downloaded models across runs, containers, etc.

*   Sets the [`HF_TOKEN`](https://huggingface.co/docs/huggingface_hub/en/package_reference/environment_variables#hftoken) environment variable to access gated models, make sure this is set in your local environment if needed.

docker run -it --net=host --gpus all --rm \
 -v ${HOME}/.cache/huggingface:/root/.cache/huggingface \
 -e HF_TOKEN \
 nvcr.io/nvidia/tritonserver:26.02-vllm-python-py3

1.   Launch the OpenAI-compatible Triton Inference Server:

cd /opt/tritonserver/python/openai

# NOTE: Embeddings endpoint does not require "--tokenizer"
python3 openai_frontend/main.py --model-repository tests/vllm_embedding_models

Example output

...
+------------------+---------+--------+
| Model            | Version | Status |
+------------------+---------+--------+
| all-MiniLM-L6-v2 | 1       | READY  | <- Correct Model Loaded in Triton
+------------------+---------+--------+
...
Found model: name='all-MiniLM-L6-v2', backend='vllm'
[WARNING] Adding CORS for the following origins: ['http://localhost']
INFO:     Started server process [133]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:9000 (Press CTRL+C to quit) <- OpenAI Frontend Started Successfully

1.   Send a `/v1/embeddings` request:

*   Note the use of `jq` is optional, but provides a nicely formatted output for JSON responses.

MODEL="all-MiniLM-L6-v2"
curl -s http://localhost:9000/v1/embeddings \
 -H 'Content-Type: application/json' \
 -d '{
 "model": "'${MODEL}'",
 "input": "The food was delicious and the waiter...",
 "dimensions": 10,
 "encoding_format": "float"
 }' | jq

Example output

{
 "object": "list",
 "data": [
 {
 "object": "embedding",
 "embedding": [
 -0.1914404183626175,
 0.4000193178653717,
 0.058502197265625,
 0.18909454345703125,
 -0.4690297544002533,
 0.004936536308377981,
 0.45893096923828125,
 -0.31141534447669983,
 0.18299102783203125,
 -0.4907582700252533
 ],
 "index": 0
 }
 ],
 "model": "all-MiniLM-L6-v2",
 "usage": {
 "prompt_tokens": 12,
 "total_tokens": 12
 }
}

TensorRT-LLM[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#id2 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

1.   Prepare your model repository for a TensorRT-LLM model, build the engine, etc. You can try any of the following options:

*   [Triton CLI](https://github.com/triton-inference-server/triton_cli/)

*   [TRT-LLM Backend Quickstart](https://github.com/triton-inference-server/tensorrtllm_backend?tab=readme-ov-file#quick-start)

1.   Launch the container:

*   Mounts the `~/.huggingface/cache` for re-use of downloaded models across runs, containers, etc.

*   Sets the [`HF_TOKEN`](https://huggingface.co/docs/huggingface_hub/en/package_reference/environment_variables#hftoken) environment variable to access gated models, make sure this is set in your local environment if needed.

docker run -it --net=host --gpus all --rm \
 -v ${HOME}/.cache/huggingface:/root/.cache/huggingface \
 -e HF_TOKEN \
 -e TRTLLM_ORCHESTRATOR=1 \
 nvcr.io/nvidia/tritonserver:26.02-trtllm-python-py3

1.   Install dependencies inside the container:

# Install python bindings for tritonserver and tritonfrontend
pip install /opt/tritonserver/python/triton*.whl

# Install application requirements
git clone https://github.com/triton-inference-server/server.git
cd server/python/openai/
pip install -r requirements.txt

1.   Launch the OpenAI server:

# NOTE: Adjust the --tokenizer based on the model being used
python3 openai_frontend/main.py --model-repository path/to/models --tokenizer meta-llama/Meta-Llama-3.1-8B-Instruct

1.   Send a `/v1/chat/completions` request:

*   Note the use of `jq` is optional, but provides a nicely formatted output for JSON responses.

# MODEL should be the client-facing model name in your model repository for a pipeline like TRT-LLM.
# For example, this could also be "ensemble", or something like "gpt2" if generated from Triton CLI
MODEL="tensorrt_llm_bls"
curl -s http://localhost:9000/v1/chat/completions -H 'Content-Type: application/json' -d '{
 "model": "'${MODEL}'",
 "messages": [{"role": "user", "content": "Say this is a test!"}]
}' | jq

Example output

{
 "id": "cmpl-5ad4f860-bf13-11f0-b137-b75b7f0a8586",
 "choices": [
 {
 "finish_reason": "stop",
 "index": 0,
 "message": {
 "content": "It looks like you're ready to see if I'm functioning properly. What would",
 "tool_calls": null,
 "role": "assistant",
 "function_call": null
 },
 "logprobs": null
 }
 ],
 "created": 1762875029,
 "model": "tensorrt_llm_bls",
 "system_fingerprint": null,
 "object": "chat.completion",
 "usage": {
 "prompt_tokens": 42,
 "total_tokens": 58,
 "completion_tokens": 16
 }
}

The other examples should be the same as vLLM, except that you should set `MODEL="tensorrt_llm_bls"` or `MODEL="ensemble"`, everywhere applicable as seen in the example request above.

KServe Frontends[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#kserve-frontends "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To support serving requests through both the OpenAI-Compatible and KServe Predict v2 frontends to the same running Triton Inference Server, the `tritonfrontend` python bindings are included for optional use in this application as well.

You can opt-in to including these additional frontends, assuming `tritonfrontend` is installed, with `--enable-kserve-frontends` like below:

python3 openai_frontend/main.py \
  --model-repository tests/vllm_models \
  --tokenizer meta-llama/Meta-Llama-3.1-8B-Instruct \
  --enable-kserve-frontends

See `python3 openai_frontend/main.py --help` for more information on the available arguments and default values.

For more information on the `tritonfrontend` python bindings, see the docs [here](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/customization_guide/tritonfrontend.html).

Model Parallelism Support[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#model-parallelism-support "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   [x] vLLM ([EngineArgs](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/vllm_backend/README.html#using-the-vllm-backend))

    *   ex: Configure `tensor_parallel_size: 2` in the [model.json](https://github.com/triton-inference-server/vllm_backend/blob/main/samples/model_repository/vllm_model/1/model.json)

*   [x] TensorRT-LLM ([Orchestrator Mode](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tensorrtllm_backend/README.html#orchestrator-mode))

    *   Set the following environment variable: `export TRTLLM_ORCHESTRATOR=1`

*   [ ] TensorRT-LLM ([Leader Mode](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tensorrtllm_backend/README.html#leader-mode))

    *   Not currently supported

Tool Calling[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#tool-calling "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

The OpenAI frontend supports `tools` and `tool_choice` in the `v1/chat/completions` API. Please refer to the OpenAI API reference for more details about these parameters: [tools](https://platform.openai.com/docs/api-reference/chat/create#chat-create-tools), [tool_choice](https://platform.openai.com/docs/api-reference/chat/create#chat-create-tool_choice)

To enable the tool-calling feature, add the `--tool-call-parser {parser_name}` flag when starting the server. The two available parsers are `llama3` and `mistral`. The `llama3` parser supports tool-calling features for LLaMA 3.1, 3.2, and 3.3 models, while the `mistral` parser supports tool-calling features for the Mistral Instruct model.

Example for launching the OpenAI frontend with a tool call parser:

python3 openai_frontend/main.py \
  --model-repository tests/vllm_models \
  --tokenizer meta-llama/Meta-Llama-3.1-8B-Instruct \
  --tool-call-parser llama3

Example for making a tool calling request:

import json
from openai import OpenAI

def get_current_weather(city: str, state: str, unit: "str"):
    return (
        "The weather in Dallas, Texas is 85 degrees fahrenheit. It is "
        "partly cloudly, with highs in the 90's."
    )

available_tools = {"get_current_weather": get_current_weather}

openai_api_key = "EMPTY"
openai_api_base = "http://localhost:9000/v1"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

model = "llama-3.1-8b-instruct" # change this to the model in the repository

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The city to find the weather for, e.g. 'San Francisco'",
                    },
                    "state": {
                        "type": "string",
                        "description": "the two-letter abbreviation for the state that the city is"
                        " in, e.g. 'CA' which would mean 'California'",
                    },
                    "unit": {
                        "type": "string",
                        "description": "The unit to fetch the temperature in",
                        "enum": ["celsius", "fahrenheit"],
                    },
                },
                "required": ["city", "state", "unit"],
            },
        },
    }
]

messages = [
    {
        "role": "system",
        "content": "You're a helpful assistant! Answer the users question best you can.",
    },
    {"role": "user", "content": "What is the weather in Dallas, Texas in Fahrenheit?"},
]

tool_calls = client.chat.completions.create(
    messages=messages, model=model, tools=tools, max_completion_tokens=128
)
function_name = tool_calls.choices[0].message.tool_calls[0].function.name
function_arguments = tool_calls.choices[0].message.tool_calls[0].function.arguments

print(f"function name: " f"{function_name}")
print(f"function arguments: {function_arguments}")
print(f"tool calling result: {available_tools[function_name](https://github.com/triton-inference-server/server/blob/main/docs/client_guide/**json.loads(function_arguments))}")

Example output:

function name: get_current_weather
function arguments: {"city": "Dallas", "state": "TX", "unit": "fahrenheit"}
tool calling result: The weather in Dallas, Texas is 85 degrees fahrenheit. It is partly cloudly, with highs in the 90's.

### Named Tool Calling[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#named-tool-calling "Link to this heading")

The OpenAI frontend supports named function calling, utilizing structured outputs in the vLLM backend and guided decoding in TensorRT-LLM backend. Users can specify one of the tools in `tool_choice` to force the model to select a specific tool for function calling.

> [!NOTE] For instructions on enabling guided decoding in the TensorRT-LLM backend, please refer to [this guide](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tensorrtllm_backend/docs/guided_decoding.html)

Example for making a named tool calling request:

import json
from openai import OpenAI

def get_current_weather(city: str, state: str, unit: "str"):
    return (
        "The weather in Dallas, Texas is 85 degrees fahrenheit. It is "
        "partly cloudly, with highs in the 90's."
    )

def get_n_day_weather_forecast(city: str, state: str, unit: str, num_days: int):
    return (
        f"The weather in Dallas, Texas is 85 degrees fahrenheit in next {num_days} days."
    )

available_tools = {"get_current_weather": get_current_weather,
                  "get_n_day_weather_forecast": get_n_day_weather_forecast}

openai_api_key = "EMPTY"
openai_api_base = "http://localhost:9000/v1"
client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)
model = "llama-3.1-8b-instruct" # change this to the model in the repository
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The city to find the weather for, e.g. 'San Francisco'",
                    },
                    "state": {
                        "type": "string",
                        "description": "the two-letter abbreviation for the state that the city is"
                        " in, e.g. 'CA' which would mean 'California'",
                    },
                    "unit": {
                        "type": "string",
                        "description": "The unit to fetch the temperature in",
                        "enum": ["celsius", "fahrenheit"],
                    },
                },
                "required": ["city", "state", "unit"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_n_day_weather_forecast",
            "description": "Get an N-day weather forecast",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The city to find the weather for, "
                        "e.g. 'San Francisco'",
                    },
                    "state": {
                        "type": "string",
                        "description": "must the two-letter abbreviation for the state "
                        "that the city is in, e.g. 'CA' which would "
                        "mean 'California'",
                    },
                    "unit": {
                        "type": "string",
                        "description": "The unit to fetch the temperature in",
                        "enum": ["celsius", "fahrenheit"],
                    },
                    "num_days": {
                        "type": "integer",
                        "description": "The number of days to forecast",
                    },
                },
                "required": ["city", "state", "unit", "num_days"],
            },
        },
     }
]

tool_choice = {"function": {"name": "get_n_day_weather_forecast"}, "type": "function"}

messages = [
    {
        "role": "system",
        "content": "You're a helpful assistant! Answer the users question best you can.",
    },
    {"role": "user", "content": "What is the weather in Dallas, Texas in Fahrenheit?"},
]

tool_calls = client.chat.completions.create(
    messages=messages, model=model, tools=tools, tool_choice=tool_choice, max_completion_tokens=128
)
function_name = tool_calls.choices[0].message.tool_calls[0].function.name
function_arguments = tool_calls.choices[0].message.tool_calls[0].function.arguments

print(f"function name: {function_name}")
print(f"function arguments: {function_arguments}")
print(f"tool calling result: {available_tools[function_name](https://github.com/triton-inference-server/server/blob/main/docs/client_guide/**json.loads(function_arguments))}")

Example output:

function name: get_n_day_weather_forecast
function arguments: {"city": "Dallas", "state": "TX", "unit": "fahrenheit", num_days: 1}
tool calling result: The weather in Dallas, Texas is 85 degrees fahrenheit in next 1 days.

Limit Endpoint Access[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#limit-endpoint-access "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The OpenAI-compatible server supports restricting access to specific API endpoints through authentication headers. This feature allows you to protect sensitive endpoints while keeping others publicly accessible.

### Configuration[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#configuration "Link to this heading")

Use the `--openai-restricted-api` command-line argument to configure endpoint restrictions:

--openai-restricted-api <API_1>,<API_2>,... <restricted-key> <restricted-value>

*   **`API`**: A comma-separated list of APIs to be included in this group. Note that currently a given API is not allowed to be included in multiple groups. The following protocols / APIs are recognized:

    *   **inference**: Chat completions and text completions endpoints

        *   `POST /v1/chat/completions`

        *   `POST /v1/completions`

    *   **embedding**: Embedding endpoint

        *   `POST /v1/embeddings`

    *   **model-repository**: Model listing and information endpoints

        *   `GET /v1/models`

        *   `GET /v1/models/{model_name}`

    *   **metrics**: Server metrics endpoint

        *   `GET /metrics`

    *   **health**: Health check endpoint

        *   `GET /health/ready`

*   **`restricted-key`**: The HTTP request header to be checked when a request is received.

*   **`restricted-value`**: The header value required to access the specified protocols.

### Examples[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#examples "Link to this heading")

#### Restrict Inference API Endpoints Only[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#restrict-inference-api-endpoints-only "Link to this heading")

--openai-restricted-api "inference api-key my-secret-key"

Clients must include the header:

curl -H "api-key: my-secret-key" \
 -X POST http://localhost:9000/v1/chat/completions \
 -d '{"model": "my-model", "messages": [{"role": "user", "content": "Hello"}]}'

#### Restrict Multiple API Endpoints[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#restrict-multiple-api-endpoints "Link to this heading")

# Different authentication for different APIs
--openai-restricted-api "inference user-key user-secret" \
--openai-restricted-api "model-repository admin-key admin-secret"

# Multiple APIs in single argument with shared authentication
--openai-restricted-api "inference,model-repository shared-key shared-secret"

[previous API Reference](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/api_reference.html "previous page")[next KServe API](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/kserve.html "next page")

 On this page 

*   [Pre-requisites](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#pre-requisites)
*   [VLLM](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#vllm)
    *   [LoRA Adapters](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#lora-adapters)
        *   [vLLM](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#id1)
        *   [TensorRT-LLM](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#tensorrt-llm)

    *   [Embedding Models](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#embedding-models)

*   [TensorRT-LLM](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#id2)
*   [KServe Frontends](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#kserve-frontends)
*   [Model Parallelism Support](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#model-parallelism-support)
*   [Tool Calling](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#tool-calling)
    *   [Named Tool Calling](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#named-tool-calling)

*   [Limit Endpoint Access](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#limit-endpoint-access)
    *   [Configuration](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#configuration)
    *   [Examples](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#examples)
        *   [Restrict Inference API Endpoints Only](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#restrict-inference-api-endpoints-only)
        *   [Restrict Multiple API Endpoints](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html#restrict-multiple-api-endpoints)

[![Image 3: NVIDIA](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_static/nvidia-logo-horiz-rgb-1c-blk-for-screen.svg)![Image 4: NVIDIA](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_static/nvidia-logo-horiz-rgb-1c-wht-for-screen.svg)](https://www.nvidia.com/)

[Privacy Policy](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/) | [Your Privacy Choices](https://www.nvidia.com/en-us/about-nvidia/privacy-center/) | [Terms of Service](https://www.nvidia.com/en-us/about-nvidia/terms-of-service/) | [Accessibility](https://www.nvidia.com/en-us/about-nvidia/accessibility/) | [Corporate Policies](https://www.nvidia.com/en-us/about-nvidia/company-policies/) | [Product Security](https://www.nvidia.com/en-us/product-security/) | [Contact](https://www.nvidia.com/en-us/contact/)

Copyright © 2018-2026, NVIDIA Corporation.
