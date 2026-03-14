# Source: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html

Title: tritonclient.utils — NVIDIA Triton Inference Server

URL Source: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html

Markdown Content:
tritonclient.utils — NVIDIA Triton Inference Server
===============

[Skip to main content](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#main-content)

Back to top- [x] - [x] 

Ctrl+K

[![Image 1: NVIDIA Triton Inference Server - Home](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_static/nvidia-logo-horiz-rgb-blk-for-screen.svg)![Image 2: NVIDIA Triton Inference Server - Home](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_static/nvidia-logo-horiz-rgb-wht-for-screen.svg) NVIDIA Triton Inference Server](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/contents.html)

 Choose version 

Search Ctrl+K

*   [GitHub](https://github.com/triton-inference-server/server "GitHub")

Search Ctrl+K

[![Image 3: NVIDIA Triton Inference Server - Home](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_static/nvidia-logo-horiz-rgb-blk-for-screen.svg)![Image 4: NVIDIA Triton Inference Server - Home](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_static/nvidia-logo-horiz-rgb-wht-for-screen.svg) NVIDIA Triton Inference Server](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/contents.html)

 Choose version 

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

    *   [OpenAI API](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client_guide/openai_readme.html)
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

        *   [tritonclient.utils](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#)

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
*   [Python tritonclient Package API](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient_api.html)
*   [tritonclient](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.html)
*   tritonclient.utils

tritonclient.utils[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#module-tritonclient.utils "Link to this heading")
====================================================================================================================================================================================================

Functions

[`deserialize_bf16_tensor`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.deserialize_bf16_tensor "tritonclient.utils.deserialize_bf16_tensor")(encoded_tensor)Deserializes an encoded bf16 tensor into a numpy array of dtype of python objects
[`deserialize_bytes_tensor`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.deserialize_bytes_tensor "tritonclient.utils.deserialize_bytes_tensor")(encoded_tensor)Deserializes an encoded bytes tensor into a numpy array of dtype of python objects
[`np_to_triton_dtype`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.np_to_triton_dtype "tritonclient.utils.np_to_triton_dtype")(np_dtype)
[`raise_error`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.raise_error "tritonclient.utils.raise_error")(msg)Raise error with the provided message
[`serialize_bf16_tensor`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.serialize_bf16_tensor "tritonclient.utils.serialize_bf16_tensor")(input_tensor)Serializes a bfloat16 tensor into a flat numpy array of bytes.
[`serialize_byte_tensor`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.serialize_byte_tensor "tritonclient.utils.serialize_byte_tensor")(input_tensor)Serializes a bytes tensor into a flat numpy array of length prepended bytes.
[`serialized_byte_size`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.serialized_byte_size "tritonclient.utils.serialized_byte_size")(tensor_value)Get the underlying number of bytes for a numpy ndarray.
[`triton_to_np_dtype`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.triton_to_np_dtype "tritonclient.utils.triton_to_np_dtype")(dtype)

Exceptions

[`InferenceServerException`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.InferenceServerException "tritonclient.utils.InferenceServerException")(msg[,status,...])Exception indicating non-Success status.

_exception_ tritonclient.utils.InferenceServerException(_msg_, _status=None_, _debug\_details=None_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.InferenceServerException "Link to this definition")
Exception indicating non-Success status.

Parameters:
*   **msg** (_str_) – A brief description of error

*   **status** (_str_) – The error code

*   **debug_details** (_str_) – The additional details on the error

debug_details()[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.InferenceServerException.debug_details "Link to this definition")
Get the detailed information about the exception for debugging purposes

Returns:
Returns the exception details

Return type:
str

message()[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.InferenceServerException.message "Link to this definition")
Get the exception message.

Returns:
The message associated with this exception, or None if no message.

Return type:
str

status()[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.InferenceServerException.status "Link to this definition")
Get the status of the exception.

Returns:
Returns the status of the exception

Return type:
str

tritonclient.utils.deserialize_bf16_tensor(_encoded\_tensor_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.deserialize_bf16_tensor "Link to this definition")
Deserializes an encoded bf16 tensor into a numpy array of dtype of python objects

Parameters:
**encoded_tensor** (_bytes_) – The encoded bytes tensor where each element is 2 bytes (size of bfloat16)

Returns:
**string_tensor** – The 1-D numpy array of type float32 containing the deserialized bytes in row-major form.

Return type:
np.array

tritonclient.utils.deserialize_bytes_tensor(_encoded\_tensor_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.deserialize_bytes_tensor "Link to this definition")
Deserializes an encoded bytes tensor into a numpy array of dtype of python objects

Parameters:
**encoded_tensor** (_bytes_) – The encoded bytes tensor where each element has its length in first 4 bytes followed by the content

Returns:
**string_tensor** – The 1-D numpy array of type object containing the deserialized bytes in row-major form.

Return type:
np.array

tritonclient.utils.np_to_triton_dtype(_np\_dtype_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.np_to_triton_dtype "Link to this definition")tritonclient.utils.raise_error(_msg_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.raise_error "Link to this definition")
Raise error with the provided message

tritonclient.utils.serialize_bf16_tensor(_input\_tensor_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.serialize_bf16_tensor "Link to this definition")
Serializes a bfloat16 tensor into a flat numpy array of bytes. The numpy array should use dtype of np.float32.

Parameters:
**input_tensor** (_np.array_) – The bfloat16 tensor to serialize.

Returns:
**serialized_bf16_tensor** – The 1-D numpy array of type uint8 containing the serialized bytes in row-major form.

Return type:
np.array

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.InferenceServerException "tritonclient.utils.InferenceServerException") – If unable to serialize the given tensor.

tritonclient.utils.serialize_byte_tensor(_input\_tensor_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.serialize_byte_tensor "Link to this definition")
Serializes a bytes tensor into a flat numpy array of length prepended bytes. The numpy array should use dtype of np.object. For np.bytes, numpy will remove trailing zeros at the end of byte sequence and because of this it should be avoided.

Parameters:
**input_tensor** (_np.array_) – The bytes tensor to serialize.

Returns:
**serialized_bytes_tensor** – The 1-D numpy array of type uint8 containing the serialized bytes in row-major form.

Return type:
np.array

Raises:
[**InferenceServerException**](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.InferenceServerException "tritonclient.utils.InferenceServerException") – If unable to serialize the given tensor.

tritonclient.utils.serialized_byte_size(_tensor\_value_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.serialized_byte_size "Link to this definition")
Get the underlying number of bytes for a numpy ndarray.

Parameters:
**tensor_value** (_numpy.ndarray_) – Numpy array to calculate the number of bytes for.

Returns:
Number of bytes present in this tensor

Return type:
int

tritonclient.utils.triton_to_np_dtype(_dtype_)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.triton_to_np_dtype "Link to this definition")
Modules

[`cuda_shared_memory`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.cuda_shared_memory.html#module-tritonclient.utils.cuda_shared_memory "tritonclient.utils.cuda_shared_memory")
[`shared_memory`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.shared_memory.html#module-tritonclient.utils.shared_memory "tritonclient.utils.shared_memory")

[previous tritonclient.http.auth](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.http.auth.html "previous page")[next tritonclient.utils.cuda_shared_memory](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.cuda_shared_memory.html "next page")

 On this page 

*   [`InferenceServerException`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.InferenceServerException)
    *   [`debug_details()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.InferenceServerException.debug_details)
    *   [`message()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.InferenceServerException.message)
    *   [`status()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.InferenceServerException.status)

*   [`deserialize_bf16_tensor()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.deserialize_bf16_tensor)
*   [`deserialize_bytes_tensor()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.deserialize_bytes_tensor)
*   [`np_to_triton_dtype()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.np_to_triton_dtype)
*   [`raise_error()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.raise_error)
*   [`serialize_bf16_tensor()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.serialize_bf16_tensor)
*   [`serialize_byte_tensor()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.serialize_byte_tensor)
*   [`serialized_byte_size()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.serialized_byte_size)
*   [`triton_to_np_dtype()`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient/tritonclient.utils.html#tritonclient.utils.triton_to_np_dtype)

[![Image 5: NVIDIA](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_static/nvidia-logo-horiz-rgb-1c-blk-for-screen.svg)![Image 6: NVIDIA](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_static/nvidia-logo-horiz-rgb-1c-wht-for-screen.svg)](https://www.nvidia.com/)

[Privacy Policy](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/) | [Your Privacy Choices](https://www.nvidia.com/en-us/about-nvidia/privacy-center/) | [Terms of Service](https://www.nvidia.com/en-us/about-nvidia/terms-of-service/) | [Accessibility](https://www.nvidia.com/en-us/about-nvidia/accessibility/) | [Corporate Policies](https://www.nvidia.com/en-us/about-nvidia/company-policies/) | [Product Security](https://www.nvidia.com/en-us/product-security/) | [Contact](https://www.nvidia.com/en-us/contact/)

Copyright © 2018-2026, NVIDIA Corporation.
