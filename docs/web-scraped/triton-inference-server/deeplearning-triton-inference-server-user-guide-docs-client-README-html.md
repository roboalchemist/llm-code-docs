# Source: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html

Title: Triton Client Libraries and Examples — NVIDIA Triton Inference Server

URL Source: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html

Published Time: Sat, 28 Feb 2026 01:09:12 GMT

Markdown Content:
Triton Client Libraries and Examples — NVIDIA Triton Inference Server
===============

[Skip to main content](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#main-content)

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

*   [Client Libraries](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#)
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
*   Triton...

[![Image 3: License](https://img.shields.io/badge/License-BSD3-lightgrey.svg)](https://opensource.org/licenses/BSD-3-Clause)

Triton Client Libraries and Examples[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#triton-client-libraries-and-examples "Link to this heading")
====================================================================================================================================================================================================

To simplify communication with Triton, the Triton project provides several client libraries and examples of how to use those libraries. Ask questions or report problems in the main Triton [issues page](https://github.com/triton-inference-server/server/issues).

The provided client libraries are:

*   [C++ and Python APIs](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#client-library-apis) that make it easy to communicate with Triton from your C++ or Python application. Using these libraries you can send either HTTP/REST or GRPC requests to Triton to access all its capabilities: inferencing, status and health, statistics and metrics, model repository management, etc. These libraries also support using system and CUDA shared memory for passing inputs to and receiving outputs from Triton.

*   [Java API](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#client-library-apis) (contributed by Alibaba Cloud PAI Team) that makes it easy to communicate with Triton from your Java application using HTTP/REST requests. For now, only a limited feature subset is supported.

*   The [protoc compiler](https://developers.google.com/protocol-buffers/docs/tutorials) can generate a GRPC API in a large number of programming languages.

    *   See [src/grpc_generated/go](https://github.com/triton-inference-server/client/blob/main/src/grpc_generated/go) for an example for the [Go programming language](https://golang.org/).

    *   See [src/grpc_generated/java](https://github.com/triton-inference-server/client/blob/main/src/grpc_generated/java) for an example for the Java and Scala programming languages.

    *   See [src/grpc_generated/javascript](https://github.com/triton-inference-server/client/blob/main/src/grpc_generated/javascript) for an example with JavaScript programming language.

There are also many example applications that show how to use these libraries. Many of these examples use models from the [example model repository](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/getting_started/quickstart.html#create-a-model-repository).

*   C++ and Python versions of _image\_client_, an example application that uses the C++ or Python client library to execute image classification models on Triton. See [Image Classification Example](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#image-classification-example).

*   Several simple [C++ examples](https://github.com/triton-inference-server/client/blob/main/src/c%2B%2B/examples) show how to use the C++ library to communicate with Triton to perform inferencing and other task. The C++ examples demonstrating the HTTP/REST client are named with a _simple\_http\__ prefix and the examples demonstrating the GRPC client are named with a _simple\_grpc\__ prefix. See [Simple Example Applications](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#simple-example-applications).

*   Several simple [Python examples](https://github.com/triton-inference-server/client/blob/main/src/python/examples) show how to use the Python library to communicate with Triton to perform inferencing and other task. The Python examples demonstrating the HTTP/REST client are named with a _simple\_http\__ prefix and the examples demonstrating the GRPC client are named with a _simple\_grpc\__ prefix. See [Simple Example Applications](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#simple-example-applications).

*   Several simple [Java examples](https://github.com/triton-inference-server/client/blob/main/src/java/src/main/java/triton/client/examples) show how to use the Java API to communicate with Triton to perform inferencing and other task.

*   A couple of [Python examples that communicate with Triton using a Python GRPC API](https://github.com/triton-inference-server/client/blob/main/src/python/examples) generated by the [protoc compiler](https://grpc.io/docs/guides/). _grpc\_client.py_ is a simple example that shows simple API usage. _grpc\_image\_client.py_ is functionally equivalent to _image\_client_ but that uses a generated GRPC client stub to communicate with Triton.

Getting the Client Libraries And Examples[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#getting-the-client-libraries-and-examples "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The easiest way to get the Python client library is to [use pip to install the tritonclient module](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#download-using-python-package-installer-pip). You can also download the C++, Python and Java client libraries from [Triton GitHub release](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#download-from-github), or [download a pre-built Docker image containing the client libraries](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#download-docker-image-from-ngc) from [NVIDIA GPU Cloud (NGC)](https://ngc.nvidia.com/).

It is also possible to build the client libraries with [cmake](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#build-using-cmake).

### Download Using Python Package Installer (pip)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#download-using-python-package-installer-pip "Link to this heading")

The GRPC and HTTP client libraries are available as a Python package that can be installed using a recent version of pip.

$ pip install tritonclient[all]

Using _all_ installs both the HTTP/REST and GRPC client libraries. There are two optional packages available, _grpc_ and _http_ that can be used to install support specifically for the protocol. For example, to install only the HTTP/REST client library use,

$ pip install tritonclient[http]

There is another optional package namely _cuda_, that must be installed in order to use cuda_shared_memory utilities. _all_ specification will install the _cuda_ package by default but in other cases _cuda_ needs to be explicitly specified for installing client with cuda_shared_memory support.

$ pip install tritonclient[http, cuda]

The components of the install packages are:

*   http

*   grpc [ `service_pb2`, `service_pb2_grpc`, `model_config_pb2` ]

*   utils [ linux distribution will include `shared_memory` and `cuda_shared_memory`]

### Download From GitHub[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#download-from-github "Link to this heading")

The client libraries can be downloaded from the [Triton GitHub release page](https://github.com/triton-inference-server/server/releases) corresponding to the release you are interested in. The client libraries are found in the “Assets” section of the release page in a tar file named after the version of the release and the OS, for example, v2.3.0_ubuntu2004.clients.tar.gz.

The pre-built libraries can be used on the corresponding host system or you can install them into the Triton container to have both the clients and server in the same container.

$ mkdir clients
$ cd clients
$ wget https://github.com/triton-inference-server/server/releases/download/<tarfile_path>
$ tar xzf <tarfile_name>

After installing, the libraries can be found in lib/, the headers in include/, the Python wheel files in python/, and the jar files in java/. The bin/ and python/ directories contain the built examples that you can learn more about below.

### Download Docker Image From NGC[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#download-docker-image-from-ngc "Link to this heading")

A Docker image containing the client libraries and examples is available from [NVIDIA GPU Cloud (NGC)](https://ngc.nvidia.com/). Before attempting to pull the container ensure you have access to NGC. For step-by-step instructions, see the [NGC Getting Started Guide](https://docs.nvidia.com/ngc/latest/ngc-user-guide.html).

Use docker pull to get the client libraries and examples container from NGC.

$ docker pull nvcr.io/nvidia/tritonserver:<xx.yy>-py3-sdk

Where <xx.yy> is the version that you want to pull. Within the container the client libraries are in /workspace/install/lib, the corresponding headers in /workspace/install/include, and the Python wheel files in /workspace/install/python. The image will also contain the built client examples.

**Important Note:** When running either the server or the client using Docker containers and using the [CUDA shared memory feature](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/protocol/extension_shared_memory.html#cuda-shared-memory) you need to add `--pid host` flag when launching the containers. The reason is that CUDA IPC APIs require the PID of the source and destination of the exported pointer to be different. Otherwise, Docker enables PID namespace which may result in equality between the source and destination PIDs. The error will be always observed when both of the containers are started in the non-interactive mode.

### Build Using CMake[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#build-using-cmake "Link to this heading")

The client library build is performed using CMake. To build the client libraries and examples with all features, first change directory to the root of this repo and checkout the release version of the branch that you want to build (or the _main_ branch if you want to build the under-development version).

$ git checkout main

If building the Java client you must first install Maven and a JDK appropriate for your OS. For example, for Ubuntu you should install the `default-jdk` package:

$ apt-get install default-jdk maven

Building on Windows vs. non-Windows requires different invocations because Triton on Windows does not yet support all the build options.

#### Non-Windows[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#non-windows "Link to this heading")

Use _cmake_ to configure the build. You should adjust the flags depending on the components of Triton Client you are working and would like to build.

If you are building on a release branch (or on a development branch that is based off of a release branch), then you must also use additional cmake arguments to point to that release branch for repos that the client build depends on. For example, if you are building the r21.10 client branch then you need to use the following additional cmake flags:

-DTRITON_COMMON_REPO_TAG=r21.10
-DTRITON_THIRD_PARTY_REPO_TAG=r21.10
-DTRITON_CORE_REPO_TAG=r21.10

Then use _make_ to build the clients and examples.

$ make cc-clients python-clients java-clients

When the build completes the libraries and examples can be found in the install directory.

#### Windows[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#windows "Link to this heading")

To build the clients you must install an appropriate C++ compiler and other dependencies required for the build. The easiest way to do this is to create the [Windows min Docker image](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/customization_guide/build.html#windows-10-min-image) and the perform the build within a container launched from that image.

> docker run  -it --rm win10-py3-min powershell

It is not necessary to use Docker or the win10-py3-min container for the build, but if you do not you must install the appropriate dependencies onto your host system.

Next use _cmake_ to configure the build. If you are not building within the win10-py3-min container then you will likely need to adjust the CMAKE_TOOLCHAIN_FILE location in the following command.

$ mkdir build
$ cd build
$ cmake -DVCPKG_TARGET_TRIPLET=x64-windows -DCMAKE_TOOLCHAIN_FILE='/vcpkg/scripts/buildsystems/vcpkg.cmake' -DCMAKE_INSTALL_PREFIX=install -DTRITON_ENABLE_CC_GRPC=ON -DTRITON_ENABLE_PYTHON_GRPC=ON -DTRITON_ENABLE_GPU=OFF -DTRITON_ENABLE_EXAMPLES=ON -DTRITON_ENABLE_TESTS=ON ..

If you are building on a release branch (or on a development branch that is based off of a release branch), then you must also use additional cmake arguments to point to that release branch for repos that the client build depends on. For example, if you are building the r21.10 client branch then you need to use the following additional cmake flags:

-DTRITON_COMMON_REPO_TAG=r21.10
-DTRITON_THIRD_PARTY_REPO_TAG=r21.10
-DTRITON_CORE_REPO_TAG=r21.10

Then use msbuild.exe to build.

$ msbuild.exe cc-clients.vcxproj -p:Configuration=Release -clp:ErrorsOnly
$ msbuild.exe python-clients.vcxproj -p:Configuration=Release -clp:ErrorsOnly

When the build completes the libraries and examples can be found in the install directory.

Client Library APIs[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#client-library-apis "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------

The C++ client API exposes a class-based interface. The commented interface is available in [grpc_client.h](https://github.com/triton-inference-server/client/blob/main/src/c%2B%2B/library/grpc_client.h), [http_client.h](https://github.com/triton-inference-server/client/blob/main/src/c%2B%2B/library/http_client.h), [common.h](https://github.com/triton-inference-server/client/blob/main/src/c%2B%2B/library/common.h).

The Python client API provides similar capabilities as the C++ API. The commented interface is available in [grpc](https://github.com/triton-inference-server/client/blob/main/src/python/library/tritonclient/grpc/__init__.py) and [http](https://github.com/triton-inference-server/client/blob/main/src/python/library/tritonclient/http/__init__.py).

The Java client API provides similar capabilities as the Python API with similar classes and methods. For more information please refer to the [Java client directory](https://github.com/triton-inference-server/client/blob/main/src/java).

### HTTP Options[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#http-options "Link to this heading")

#### SSL/TLS[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#ssl-tls "Link to this heading")

The client library allows communication across a secured channel using HTTPS protocol. Just setting these SSL options do not ensure the secure communication. Triton server should be running behind `https://` proxy such as nginx. The client can then establish a secure channel to the proxy. The [`qa/L0_https`](https://github.com/triton-inference-server/server/blob/main/qa/L0_https/test.sh) in the server repository demonstrates how this can be achieved.

For C++ client, see `HttpSslOptions` struct that encapsulates these options in [http_client.h](https://github.com/triton-inference-server/client/blob/main/src/c%2B%2B/library/http_client.h).

For Python client, look for the following options in [http/__init__.py](https://github.com/triton-inference-server/client/blob/main/src/python/library/tritonclient/http/__init__.py):

*   ssl

*   ssl_options

*   ssl_context_factory

*   insecure

The [C++](https://github.com/triton-inference-server/client/blob/main/src/c%2B%2B/examples/simple_http_infer_client.cc) and [Python](https://github.com/triton-inference-server/client/blob/main/src/python/examples/simple_http_infer_client.py) examples demonstrates how to use SSL/TLS settings on client side.

#### Compression[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#compression "Link to this heading")

The client library enables on-wire compression for HTTP transactions.

For C++ client, see `request_compression_algorithm` and `response_compression_algorithm` parameters in the `Infer` and `AsyncInfer` functions in [http_client.h](https://github.com/triton-inference-server/client/blob/main/src/c%2B%2B/library/http_client.h). By default, the parameter is set as `CompressionType::NONE`.

Similarly, for Python client, see `request_compression_algorithm` and `response_compression_algorithm` parameters in `infer` and `async_infer` functions in [http/__init__.py](https://github.com/triton-inference-server/client/blob/main/src/python/library/tritonclient/http/__init__.py).

The [C++](https://github.com/triton-inference-server/client/blob/main/src/c%2B%2B/examples/simple_http_infer_client.cc) and [Python](https://github.com/triton-inference-server/client/blob/main/src/python/examples/simple_http_infer_client.py) examples demonstrates how to use compression options.

#### ORCA Header Metrics[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#orca-header-metrics "Link to this heading")

In an effort to allow quick, on-demand metric retrieval for external load balancers such as the [Kubernetes Inference Gateway API](https://gateway-api-inference-extension.sigs.k8s.io/), Triton can include live KV-cache utilization and capacity metrics in the HTTP response header when processing inference requests. The motivation behind this method was to simplify the pipeline of metric scraping by not requiring separate service to hit the metrics endpoint, instead simply including a request header asking for metrics of a certain format in the response.

To use ORCA header metrics, Triton must be using the [TensorRT-LLM backend](https://github.com/triton-inference-server/tensorrtllm_backend) that exposes KV-cache metrics, and the HTTP inference request must include a header named `endpoint-load-metrics-format` with a value equal to one of the valid formats:

`text`

*   Native HTTP, comma sepatared key-value pairs with the map fields elided into the top level scope by prepending the ‘<map_name>’

*   Request header: `endpoint-load-metrics-format: text`

*   Ex. Response header: `endpoint-load-metrics: TEXT cpu_utilization=0.3, mem_utilization=0.8, rps_fractional=10.0, eps=1, named_metrics.custom_metric_util=0.4`

`json`

*   JSON encoding of the metrics.

*   Request header: `endpoint-load-metrics-format: json`

*   Ex. Response header: `endpoint-load-metrics: JSON {“cpu_utilization”: 0.3, “mem_utilization”: 0.8, “rps_fractional”: 10.0, “eps”: 1, “named_metrics”: {“custom-metric-util”: 0.4}}`

#### Python AsyncIO Support (Beta)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#python-asyncio-support-beta "Link to this heading")

_This feature is currently in beta and may be subject to change._

Advanced users may call the Python client via `async` and `await` syntax. The [infer](https://github.com/triton-inference-server/client/blob/main/src/python/examples/simple_http_aio_infer_client.py) example demonstrates how to infer with AsyncIO.

If using SSL/TLS with AsyncIO, look for the `ssl` and `ssl_context` options in [http/aio/__init__.py](https://github.com/triton-inference-server/client/blob/main/src/python/library/tritonclient/http/aio/__init__.py)

#### Python Client Plugin API (Beta)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#python-client-plugin-api-beta "Link to this heading")

_This feature is currently in beta and may be subject to change._

The Triton Client Plugin API lets you register custom plugins to add or modify request headers. This is useful if you have gateway in front of Triton Server that requires extra headers for each request, such as HTTP Authorization. By registering the plugin, your gateway will work with Python clients without additional configuration. Note that Triton Server does not implement authentication or authorization mechanisms and similarly, Triton Server is not the direct consumer of the additional headers.

The plugin must implement the `__call__` method. The signature of the `__call__` method should look like below:

class MyPlugin:
  def  __call__ (self, request):
 """This method will be called for every HTTP request. Currently, the only
 field that can be accessed by the request object is the `request.headers`
 field. This field must be updated in-place.
 """
       request.headers['my-header-key'] = 'my-header-value'

After the plugin implementation is complete, you can register the plugin by calling `register` on the `InferenceServerClient` object.

from tritonclient.http import InferenceServerClient

client = InferenceServerClient(...)

# Register the plugin
my_plugin = MyPlugin()
client.register_plugin(my_plugin)

# All the method calls will update the headers according to the plugin
# implementation.
client.infer(...)

To unregister the plugin, you can call the `client.unregister_plugin()` function.

##### Basic Auth[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#basic-auth "Link to this heading")

You can register the `BasicAuth` plugin that implements [Basic Authentication](https://en.wikipedia.org/wiki/Basic_access_authentication).

from tritonclient.grpc.auth import BasicAuth
from tritonclient.grpc import InferenceServerClient

basic_auth = BasicAuth('username', 'password')
client = InferenceServerClient('...')

client.register_plugin(basic_auth)

The example above shows how to register the plugin for gRPC client. The `BasicAuth` plugin can be registered similarly for HTTP and [AsyncIO](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#python-asyncio-support-beta) clients.

### GRPC Options[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#grpc-options "Link to this heading")

#### SSL/TLS[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#id1 "Link to this heading")

The client library allows communication across a secured channel using gRPC protocol.

For C++ client, see `SslOptions` struct that encapsulates these options in [grpc_client.h](https://github.com/triton-inference-server/client/blob/main/src/c%2B%2B/library/grpc_client.h).

For Python client, look for the following options in [grpc/__init__.py](https://github.com/triton-inference-server/client/blob/main/src/python/library/tritonclient/grpc/__init__.py):

*   ssl

*   root_certificates

*   private_key

*   certificate_chain

The [C++](https://github.com/triton-inference-server/client/blob/main/src/c%2B%2B/examples/simple_grpc_infer_client.cc) and [Python](https://github.com/triton-inference-server/client/blob/main/src/python/examples/simple_grpc_infer_client.py) examples demonstrates how to use SSL/TLS settings on client side. For information on the corresponding server-side parameters, refer to the [server documentation](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/customization_guide/inference_protocols.html#ssl-tls)

#### Compression[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#id2 "Link to this heading")

The client library also exposes options to use on-wire compression for gRPC transactions.

For C++ client, see `compression_algorithm` parameter in the `Infer`, `AsyncInfer` and `StartStream` functions in [grpc_client.h](https://github.com/triton-inference-server/client/blob/main/src/c%2B%2B/library/grpc_client.h). By default, the parameter is set as `GRPC_COMPRESS_NONE`.

Similarly, for Python client, see `compression_algorithm` parameter in `infer`, `async_infer` and `start_stream` functions in [grpc/__init__.py](https://github.com/triton-inference-server/client/blob/main/src/python/library/tritonclient/grpc/__init__.py).

The [C++](https://github.com/triton-inference-server/client/blob/main/src/c%2B%2B/examples/simple_grpc_infer_client.cc) and [Python](https://github.com/triton-inference-server/client/blob/main/src/python/examples/simple_grpc_infer_client.py) examples demonstrates how to configure compression for clients. For information on the corresponding server-side parameters, refer to the [server documentation](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/customization_guide/inference_protocols.html#compression).

#### GRPC KeepAlive[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#grpc-keepalive "Link to this heading")

Triton exposes GRPC KeepAlive parameters with the default values for both client and server described [here](https://github.com/grpc/grpc/blob/master/doc/keepalive.md).

You can find a `KeepAliveOptions` struct/class that encapsulates these parameters in both the [C++](https://github.com/triton-inference-server/client/blob/main/src/c%2B%2B/library/grpc_client.h) and [Python](https://github.com/triton-inference-server/client/blob/main/src/python/library/tritonclient/grpc/__init__.py) client libraries.

There is also a [C++](https://github.com/triton-inference-server/client/blob/main/src/c%2B%2B/examples/simple_grpc_keepalive_client.cc) and [Python](https://github.com/triton-inference-server/client/blob/main/src/python/examples/simple_grpc_keepalive_client.py) example demonstrating how to setup these parameters on the client-side. For information on the corresponding server-side parameters, refer to the [server documentation](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/customization_guide/inference_protocols.html#grpc-keepalive)

#### Custom GRPC Channel Arguments[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#custom-grpc-channel-arguments "Link to this heading")

Advanced users may require specific client-side GRPC Channel Arguments that are not currently exposed by Triton through direct means. To support this, Triton allows users to pass custom channel arguments upon creating a GRPC client. When using this option, it is up to the user to pass a valid combination of arguments for their use case; Triton cannot feasibly test every possible combination of channel arguments.

There is a [C++](https://github.com/triton-inference-server/client/blob/main/src/c%2B%2B/examples/simple_grpc_custom_args_client.cc) and [Python](https://github.com/triton-inference-server/client/blob/main/src/python/examples/simple_grpc_custom_args_client.py) example demonstrating how to construct and pass these custom arguments upon creating a GRPC client.

You can find a comprehensive list of possible GRPC Channel Arguments [here](https://grpc.github.io/grpc/core/group__grpc__arg__keys.html).

#### Python AsyncIO Support (Beta)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#id3 "Link to this heading")

_This feature is currently in beta and may be subject to change._

Advanced users may call the Python client via `async` and `await` syntax. The [infer](https://github.com/triton-inference-server/client/blob/main/src/python/examples/simple_grpc_aio_infer_client.py) and [stream](https://github.com/triton-inference-server/client/blob/main/src/python/examples/simple_grpc_aio_sequence_stream_infer_client.py) examples demonstrate how to infer with AsyncIO.

### Request Cancellation[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#request-cancellation "Link to this heading")

Starting from r23.10, triton python gRPC client can issue cancellation to inflight requests. This can be done by calling `cancel()` on the CallContext object returned by `async_infer()` API.

  ctx = client.async_infer(...)
  ctx.cancel()

For streaming requests, `cancel_requests=True` can be sent to `stop_stream()` API to terminate all the inflight requests sent via this stream.

  client.start_stream()
  for _ in range(10):
    client.async_stream_infer(...)

  # Cancels all pending requests on stream closure rather than blocking until requests complete
  client.stop_stream(cancel_requests=True)

See more details about these APIs in [grpc/_client.py](https://github.com/triton-inference-server/client/blob/main/src/python/library/tritonclient/grpc/_client.py).

For gRPC AsyncIO requests, an AsyncIO task wrapping an `infer()` coroutine can be safely cancelled.

  infer_task = asyncio.create_task(aio_client.infer(...))
  infer_task.cancel()

For gRPC AsyncIO streaming requests, `cancel()` can be called on the asynchronous iterator returned by `stream_infer()` API.

  responses_iterator = aio_client.stream_infer(...)
  responses_iterator.cancel()

See more details about these APIs in [grpc/aio/_ _init_ _.py](https://github.com/triton-inference-server/client/blob/main/src/python/library/tritonclient/grpc/aio/__init__.py).

See [request_cancellation](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/request_cancellation.html) in the server user-guide to learn about how this is handled on the server side. If writing your own gRPC clients in the language of choice consult gRPC guide on [cancellation](https://grpc.io/docs/guides/cancellation/#cancelling-an-rpc-call-on-the-client-side).

### GRPC Status Codes[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#grpc-status-codes "Link to this heading")

Starting from release 24.08, Triton server introduces support for gRPC error codes in streaming mode for all clients enhancing error reporting capabilities. When this feature is enabled, the Triton server will return standard gRPC error codes and subsequently close the stream after delivering the error. This feature is optional can be enabled by adding header with `triton_grpc_error` key and `true` as value. See [grpc error codes](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#GRPC-Status-Codes) in the server to learn about how this is handled on the server side. See gRPC guide on [status-codes](https://grpc.io/docs/guides/status-codes/) for more details. Below is a Python snippet to enable the feature. Without this header Triton server will continue streaming in default mode returning error message and status inside `InferenceServerException` object within the callback provided.

  triton_client = grpcclient.InferenceServerClient(triton_server_url)
  # New added header key value
  metadata = {"triton_grpc_error": "true"}
  triton_client.start_stream(
    callback=partial(callback, user_data), headers=metadata
  )

#### GRPC Status Codes During Server Shutdown[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#grpc-status-codes-during-server-shutdown "Link to this heading")

During shutdown, Triton will reject new incoming requests and clients may receive one of the following status codes before the endpoint closes:

1.   `StatusCode.CANCELLED`

    *   Returned by the GRPC endpoint indicating the endpoint has started to shutdown and cannot accept new requests.

2.   `StatusCode.UNAVAILABLE` with the message “GRPC server is shutting down and has stopped accepting new requests”

*   Returned by the Tritonserver indicating requests can no longer be added to the processing queue.

Simple Example Applications[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#simple-example-applications "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This section describes several of the simple example applications and the features that they illustrate.

### Bytes/String Datatype[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#bytes-string-datatype "Link to this heading")

Some frameworks support tensors where each element in the tensor is variable-length binary data. Each element can hold a string or an arbitrary sequence of bytes. On the client this datatype is BYTES (see [Datatypes](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/model_configuration.html#datatypes) for information on supported datatypes).

The Python client library uses numpy to represent input and output tensors. For BYTES tensors the dtype of the numpy array should be ‘np.object_’ as shown in the examples. For backwards compatibility with previous versions of the client library, ‘np.bytes_’ can also be used for BYTES tensors. However, using ‘np.bytes_’ is not recommended because using this dtype will cause numpy to remove all trailing zeros from each array element. As a result, binary sequences ending in zero(s) will not be represented correctly.

BYTES tensors are demonstrated in the C++ example applications simple_http_string_infer_client.cc and simple_grpc_string_infer_client.cc. String tensors are demonstrated in the Python example application simple_http_string_infer_client.py and simple_grpc_string_infer_client.py.

### System Shared Memory[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#system-shared-memory "Link to this heading")

Using system shared memory to communicate tensors between the client library and Triton can significantly improve performance in some cases.

Using system shared memory is demonstrated in the C++ example applications simple_http_shm_client.cc and simple_grpc_shm_client.cc. Using system shared memory is demonstrated in the Python example application simple_http_shm_client.py and simple_grpc_shm_client.py.

Python does not have a standard way of allocating and accessing shared memory so as an example a simple [system shared memory module](https://github.com/triton-inference-server/client/blob/main/src/python/library/tritonclient/utils/shared_memory) is provided that can be used with the Python client library to create, set and destroy system shared memory.

### CUDA Shared Memory[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#cuda-shared-memory "Link to this heading")

Using CUDA shared memory to communicate tensors between the client library and Triton can significantly improve performance in some cases.

Using CUDA shared memory is demonstrated in the C++ example applications simple_http_cudashm_client.cc and simple_grpc_cudashm_client.cc. Using CUDA shared memory is demonstrated in the Python example application simple_http_cudashm_client.py and simple_grpc_cudashm_client.py.

Python does not have a standard way of allocating and accessing shared memory so as an example a simple [CUDA shared memory module](https://github.com/triton-inference-server/client/blob/main/src/python/library/tritonclient/utils/cuda_shared_memory) is provided that can be used with the Python client library to create, set and destroy CUDA shared memory. The module currently supports numpy arrays ([example usage](https://github.com/triton-inference-server/client/blob/main/src/python/examples/simple_http_cudashm_client.py)) and DLPack tensors ([example usage](https://github.com/triton-inference-server/client/blob/main/src/python/library/tests/test_cuda_shared_memory.py)).

### Client API for Stateful Models[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#client-api-for-stateful-models "Link to this heading")

When performing inference using a [stateful model](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/architecture.html#stateful-models), a client must identify which inference requests belong to the same sequence and also when a sequence starts and ends.

Each sequence is identified with a sequence ID that is provided when an inference request is made. It is up to the clients to create a unique sequence ID. For each sequence the first inference request should be marked as the start of the sequence and the last inference requests should be marked as the end of the sequence.

The use of sequence ID and start and end flags are demonstrated in the C++ example applications simple_grpc_sequence_stream_infer_client.cc. The use of sequence ID and start and end flags are demonstrated in the Python example application simple_grpc_sequence_stream_infer_client.py.

Image Classification Example[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#image-classification-example "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The image classification example that uses the C++ client API is available at [src/c++/examples/image_client.cc](https://github.com/triton-inference-server/client/blob/main/src/c%2B%2B/examples/image_client.cc). The Python version of the image classification client is available at [src/python/examples/image_client.py](https://github.com/triton-inference-server/client/blob/main/src/python/examples/image_client.py).

To use image_client (or image_client.py) you must first have a running Triton that is serving one or more image classification models. The image_client application requires that the model have a single image input and produce a single classification output. If you don’t have a model repository with image classification models see [QuickStart](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/getting_started/quickstart.html) for instructions on how to create one.

Once Triton is running you can use the image_client application to send inference requests. You can specify a single image or a directory holding images. Here we send a request for the inception_graphdef model for an image from the [qa/images](https://github.com/triton-inference-server/server/tree/main/qa/images).

$ image_client -m inception_graphdef -s INCEPTION qa/images/mug.jpg
Request 0, batch size 1
Image 'qa/images/mug.jpg':
 0.754130 (505) = COFFEE MUG

The Python version of the application accepts the same command-line arguments.

$ python image_client.py -m inception_graphdef -s INCEPTION qa/images/mug.jpg
Request 0, batch size 1
Image 'qa/images/mug.jpg':
 0.826384 (505) = COFFEE MUG

The image_client and image_client.py applications use the client libraries to talk to Triton. By default image_client instructs the client library to use HTTP/REST protocol, but you can use the GRPC protocol by providing the -i flag. You must also use the -u flag to point at the GRPC endpoint on Triton.

$ image_client -i grpc -u localhost:8001 -m inception_graphdef -s INCEPTION qa/images/mug.jpg
Request 0, batch size 1
Image 'qa/images/mug.jpg':
 0.754130 (505) = COFFEE MUG

By default the client prints the most probable classification for the image. Use the -c flag to see more classifications.

$ image_client -m inception_graphdef -s INCEPTION -c 3 qa/images/mug.jpg
Request 0, batch size 1
Image 'qa/images/mug.jpg':
 0.754130 (505) = COFFEE MUG
 0.157077 (969) = CUP
 0.002880 (968) = ESPRESSO

The -b flag allows you to send a batch of images for inferencing. The image_client application will form the batch from the image or images that you specified. If the batch is bigger than the number of images then image_client will just repeat the images to fill the batch.

$ image_client -m inception_graphdef -s INCEPTION -c 3 -b 2 qa/images/mug.jpg
Request 0, batch size 2
Image 'qa/images/mug.jpg':
 0.754130 (505) = COFFEE MUG
 0.157077 (969) = CUP
 0.002880 (968) = ESPRESSO
Image 'qa/images/mug.jpg':
 0.754130 (505) = COFFEE MUG
 0.157077 (969) = CUP
 0.002880 (968) = ESPRESSO

Provide a directory instead of a single image to perform inferencing on all images in the directory.

$ image_client -m inception_graphdef -s INCEPTION -c 3 -b 2 qa/images
Request 0, batch size 2
Image '/opt/tritonserver/qa/images/car.jpg':
    0.819196 (818) = SPORTS CAR
    0.033457 (437) = BEACH WAGON
    0.031232 (480) = CAR WHEEL
Image '/opt/tritonserver/qa/images/mug.jpg':
    0.754130 (505) = COFFEE MUG
    0.157077 (969) = CUP
    0.002880 (968) = ESPRESSO
Request 1, batch size 2
Image '/opt/tritonserver/qa/images/vulture.jpeg':
    0.977632 (24) = VULTURE
    0.000613 (9) = HEN
    0.000560 (137) = EUROPEAN GALLINULE
Image '/opt/tritonserver/qa/images/car.jpg':
    0.819196 (818) = SPORTS CAR
    0.033457 (437) = BEACH WAGON
    0.031232 (480) = CAR WHEEL

The [grpc_image_client.py](https://github.com/triton-inference-server/client/blob/main/src/python/examples/grpc_image_client.py) application behaves the same as the image_client except that instead of using the client library it uses the GRPC generated library to communicate with Triton.

Ensemble Image Classification Example Application[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#ensemble-image-classification-example-application "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In comparison to the image classification example above, this example uses an ensemble of an image-preprocessing model implemented as a [DALI backend](https://github.com/triton-inference-server/dali_backend) and a TensorFlow Inception model. The ensemble model allows you to send the raw image binaries in the request and receive classification results without preprocessing the images on the client.

To try this example you should follow the [DALI ensemble example instructions](https://github.com/triton-inference-server/dali_backend/tree/075bb874ae99d20bf3bc67e26937cdb7b05a3b20/docs/examples/inception_ensemble).

**Important Note:** TensorFlow backend has been deprecated.

[previous Java bindings for In-Process Triton Server API](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/customization_guide/inprocess_java_api.html "previous page")[next Python tritonclient Package API](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_reference/tritonclient_api.html "next page")

 On this page 

*   [Getting the Client Libraries And Examples](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#getting-the-client-libraries-and-examples)
    *   [Download Using Python Package Installer (pip)](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#download-using-python-package-installer-pip)
    *   [Download From GitHub](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#download-from-github)
    *   [Download Docker Image From NGC](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#download-docker-image-from-ngc)
    *   [Build Using CMake](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#build-using-cmake)
        *   [Non-Windows](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#non-windows)
        *   [Windows](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#windows)

*   [Client Library APIs](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#client-library-apis)
    *   [HTTP Options](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#http-options)
        *   [SSL/TLS](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#ssl-tls)
        *   [Compression](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#compression)
        *   [ORCA Header Metrics](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#orca-header-metrics)
        *   [Python AsyncIO Support (Beta)](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#python-asyncio-support-beta)
        *   [Python Client Plugin API (Beta)](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#python-client-plugin-api-beta)
            *   [Basic Auth](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#basic-auth)

    *   [GRPC Options](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#grpc-options)
        *   [SSL/TLS](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#id1)
        *   [Compression](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#id2)
        *   [GRPC KeepAlive](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#grpc-keepalive)
        *   [Custom GRPC Channel Arguments](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#custom-grpc-channel-arguments)
        *   [Python AsyncIO Support (Beta)](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#id3)

    *   [Request Cancellation](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#request-cancellation)
    *   [GRPC Status Codes](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#grpc-status-codes)
        *   [GRPC Status Codes During Server Shutdown](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#grpc-status-codes-during-server-shutdown)

*   [Simple Example Applications](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#simple-example-applications)
    *   [Bytes/String Datatype](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#bytes-string-datatype)
    *   [System Shared Memory](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#system-shared-memory)
    *   [CUDA Shared Memory](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#cuda-shared-memory)
    *   [Client API for Stateful Models](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#client-api-for-stateful-models)

*   [Image Classification Example](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#image-classification-example)
*   [Ensemble Image Classification Example Application](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/client/README.html#ensemble-image-classification-example-application)

[![Image 4: NVIDIA](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_static/nvidia-logo-horiz-rgb-1c-blk-for-screen.svg)![Image 5: NVIDIA](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_static/nvidia-logo-horiz-rgb-1c-wht-for-screen.svg)](https://www.nvidia.com/)

[Privacy Policy](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/) | [Your Privacy Choices](https://www.nvidia.com/en-us/about-nvidia/privacy-center/) | [Terms of Service](https://www.nvidia.com/en-us/about-nvidia/terms-of-service/) | [Accessibility](https://www.nvidia.com/en-us/about-nvidia/accessibility/) | [Corporate Policies](https://www.nvidia.com/en-us/about-nvidia/company-policies/) | [Product Security](https://www.nvidia.com/en-us/product-security/) | [Contact](https://www.nvidia.com/en-us/contact/)

Copyright © 2018-2026, NVIDIA Corporation.
