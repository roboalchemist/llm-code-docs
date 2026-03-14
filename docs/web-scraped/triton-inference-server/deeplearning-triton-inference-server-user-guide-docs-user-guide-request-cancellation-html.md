# Source: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/request_cancellation.html

Title: Request Cancellation — NVIDIA Triton Inference Server

URL Source: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/request_cancellation.html

Markdown Content:
Request Cancellation — NVIDIA Triton Inference Server
===============

[Skip to main content](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/request_cancellation.html#main-content)

Back to top- [x] - [x] 

Ctrl+K

[![Image 1: NVIDIA Triton Inference Server - Home](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_static/nvidia-logo-horiz-rgb-blk-for-screen.svg)![Image 2: NVIDIA Triton Inference Server - Home](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_static/nvidia-logo-horiz-rgb-wht-for-screen.svg) NVIDIA Triton Inference Server](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/contents.html)

2.66.0 (current release)

[2.66.0 (current release)](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/index.htmluser_guide/request_cancellation.html)[2.65.0](https://docs.nvidia.com/deeplearning/triton-inference-server/archives/triton-inference-server-2650/user-guide/docsuser_guide/request_cancellation.html)[2.64.0](https://docs.nvidia.com/deeplearning/triton-inference-server/archives/triton-inference-server-2640/user-guide/docsuser_guide/request_cancellation.html)[2.63.0](https://docs.nvidia.com/deeplearning/triton-inference-server/archives/triton-inference-server-2630/user-guide/docsuser_guide/request_cancellation.html)[2.62.0](https://docs.nvidia.com/deeplearning/triton-inference-server/archives/triton-inference-server-2620/user-guide/docsuser_guide/request_cancellation.html)[2.61.0](https://docs.nvidia.com/deeplearning/triton-inference-server/archives/triton-inference-server-2610/user-guide/docsuser_guide/request_cancellation.html)[2.60.0](https://docs.nvidia.com/deeplearning/triton-inference-server/archives/triton-inference-server-2600/user-guide/docsuser_guide/request_cancellation.html)[2.59.1](https://docs.nvidia.com/deeplearning/triton-inference-server/archives/triton-inference-server-2591/user-guide/docsuser_guide/request_cancellation.html)[2.59.0](https://docs.nvidia.com/deeplearning/triton-inference-server/archives/triton-inference-server-2590/user-guide/docsuser_guide/request_cancellation.html)[2.58.0](https://docs.nvidia.com/deeplearning/triton-inference-server/archives/triton-inference-server-2580/user-guide/docsuser_guide/request_cancellation.html)[2.57.0](https://docs.nvidia.com/deeplearning/triton-inference-server/archives/triton-inference-server-2570/user-guide/docsuser_guide/request_cancellation.html)[2.56.0](https://docs.nvidia.com/deeplearning/triton-inference-server/archives/triton-inference-server-2560/user-guide/docsuser_guide/request_cancellation.html)[older releases](https://docs.nvidia.com/deeplearning/triton-inference-server/archives/user_guide/request_cancellation.html)

Search Ctrl+K

*   [GitHub](https://github.com/triton-inference-server/server)

Search Ctrl+K

[![Image 3: NVIDIA Triton Inference Server - Home](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_static/nvidia-logo-horiz-rgb-blk-for-screen.svg)![Image 4: NVIDIA Triton Inference Server - Home](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_static/nvidia-logo-horiz-rgb-wht-for-screen.svg) NVIDIA Triton Inference Server](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/contents.html)

2.66.0 (current release)

[2.66.0 (current release)](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/index.htmluser_guide/request_cancellation.html)[2.65.0](https://docs.nvidia.com/deeplearning/triton-inference-server/archives/triton-inference-server-2650/user-guide/docsuser_guide/request_cancellation.html)[2.64.0](https://docs.nvidia.com/deeplearning/triton-inference-server/archives/triton-inference-server-2640/user-guide/docsuser_guide/request_cancellation.html)[2.63.0](https://docs.nvidia.com/deeplearning/triton-inference-server/archives/triton-inference-server-2630/user-guide/docsuser_guide/request_cancellation.html)[2.62.0](https://docs.nvidia.com/deeplearning/triton-inference-server/archives/triton-inference-server-2620/user-guide/docsuser_guide/request_cancellation.html)[2.61.0](https://docs.nvidia.com/deeplearning/triton-inference-server/archives/triton-inference-server-2610/user-guide/docsuser_guide/request_cancellation.html)[2.60.0](https://docs.nvidia.com/deeplearning/triton-inference-server/archives/triton-inference-server-2600/user-guide/docsuser_guide/request_cancellation.html)[2.59.1](https://docs.nvidia.com/deeplearning/triton-inference-server/archives/triton-inference-server-2591/user-guide/docsuser_guide/request_cancellation.html)[2.59.0](https://docs.nvidia.com/deeplearning/triton-inference-server/archives/triton-inference-server-2590/user-guide/docsuser_guide/request_cancellation.html)[2.58.0](https://docs.nvidia.com/deeplearning/triton-inference-server/archives/triton-inference-server-2580/user-guide/docsuser_guide/request_cancellation.html)[2.57.0](https://docs.nvidia.com/deeplearning/triton-inference-server/archives/triton-inference-server-2570/user-guide/docsuser_guide/request_cancellation.html)[2.56.0](https://docs.nvidia.com/deeplearning/triton-inference-server/archives/triton-inference-server-2560/user-guide/docsuser_guide/request_cancellation.html)[older releases](https://docs.nvidia.com/deeplearning/triton-inference-server/archives/user_guide/request_cancellation.html)

*   [GitHub](https://github.com/triton-inference-server/server)

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

*   [Request Cancellation](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/request_cancellation.html#)
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
*   Request Cancellation

Request Cancellation[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/request_cancellation.html#request-cancellation "Link to this heading")
======================================================================================================================================================================================

Starting from r23.10, Triton supports handling request cancellation received from the gRPC client or a C API user. Long running inference requests such as for auto generative large language models may run for an indeterminate amount of time or indeterminate number of steps. Additionally clients may enqueue a large number of requests as part of a sequence or request stream and later determine the results are no longer needed. Continuing to process requests whose results are no longer required can significantly impact server resources.

Issuing Request Cancellation[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/request_cancellation.html#issuing-request-cancellation "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### In-Process C API[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/request_cancellation.html#in-process-c-api "Link to this heading")

[In-Process Triton Server C API](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/customization_guide/inprocess_c_api.html) has been enhanced with `TRITONSERVER_InferenceRequestCancel` and `TRITONSERVER_InferenceRequestIsCancelled` to issue cancellation and query whether cancellation has been issued on an inflight request respectively. Read more about the APIs in [tritonserver.h](https://github.com/triton-inference-server/core/blob/main/include/triton/core/tritonserver.h).

### gRPC Endpoint[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/request_cancellation.html#grpc-endpoint "Link to this heading")

In addition, [gRPC endpoint](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/customization_guide/inference_protocols.html#http-rest-and-grpc-protocols) can now detect cancellation from the client and attempt to terminate request. At present, only gRPC python client supports issuing request cancellation to the server endpoint. See [request-cancellation](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#request-cancellation) for more details on how to issue requests from the client-side. See gRPC guide on RPC [cancellation](https://grpc.io/docs/guides/cancellation/) for finer details.

Handling in Triton Core[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/request_cancellation.html#handling-in-triton-core "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Triton core checks for requests that have been cancelled at some critical points when using [dynamic](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/batcher.html#dynamic-batcher) or [sequence](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/batcher.html#sequence-batcher) batching. The checking is also performed between each [ensemble](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/scheduler.html#ensemble-scheduler) steps and terminates further processing if the request is cancelled.

On detecting a cancelled request, Triton core responds with CANCELLED status. If a request is cancelled when using [sequence_batching](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/batcher.html#sequence-batcher), then all the pending requests in the same sequence will also be cancelled. The sequence is represented by the requests that has identical sequence id.

**Note**: Currently, Triton core does not detect cancellation status of a request once it is forwarded to [rate limiter](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/rate_limiter.html). Improving the request cancellation detection and handling within Triton core is work in progress.

Handling in Backend[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/request_cancellation.html#handling-in-backend "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Upon receiving request cancellation, Triton does its best to terminate request at various points. However, once a request has been given to the backend for execution, it is up to the individual backends to detect and handle request termination. Currently, the following backends support early termination:

*   [TensorRT-LLM backend](https://github.com/triton-inference-server/tensorrtllm_backend)

*   [vLLM backend](https://github.com/triton-inference-server/vllm_backend)

*   [python backend](https://github.com/triton-inference-server/python_backend)

Python backend is a special case where we expose the APIs to detect cancellation status of the request but it is up to the `model.py` developer to detect whether the request is cancelled and terminate further execution.

**For the backend developer**: The backend APIs have also been enhanced to let the backend detect whether the request received from Triton core has been cancelled. See `TRITONBACKEND_RequestIsCancelled` and `TRITONBACKEND_ResponseFactoryIsCancelled` in [tritonbackend.h](https://github.com/triton-inference-server/core/blob/main/include/triton/core/tritonbackend.h) for more details. The backend upon detecting request cancellation can stop processing it any further. The Python models running behind Python backend can also query the cancellation status of request and response_sender. See [this](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/python_backend/README.html#request-cancellation-handling) section in python backend documentation for more details.

[previous Implicit State Management](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/implicit_state_management.html "previous page")[next Rate Limiter](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/rate_limiter.html "next page")

 On this page 

*   [Issuing Request Cancellation](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/request_cancellation.html#issuing-request-cancellation)
    *   [In-Process C API](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/request_cancellation.html#in-process-c-api)
    *   [gRPC Endpoint](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/request_cancellation.html#grpc-endpoint)

*   [Handling in Triton Core](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/request_cancellation.html#handling-in-triton-core)
*   [Handling in Backend](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/request_cancellation.html#handling-in-backend)

[![Image 5: NVIDIA](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_static/nvidia-logo-horiz-rgb-1c-blk-for-screen.svg)![Image 6: NVIDIA](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_static/nvidia-logo-horiz-rgb-1c-wht-for-screen.svg)](https://www.nvidia.com/)

[Privacy Policy](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/) | [Your Privacy Choices](https://www.nvidia.com/en-us/about-nvidia/privacy-center/) | [Terms of Service](https://www.nvidia.com/en-us/about-nvidia/terms-of-service/) | [Accessibility](https://www.nvidia.com/en-us/about-nvidia/accessibility/) | [Corporate Policies](https://www.nvidia.com/en-us/about-nvidia/company-policies/) | [Product Security](https://www.nvidia.com/en-us/product-security/) | [Contact](https://www.nvidia.com/en-us/contact/)

Copyright © 2018-2026, NVIDIA Corporation.
