# Source: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/pytorch_backend/README.html

Title: PyTorch (LibTorch) Backend — NVIDIA Triton Inference Server

URL Source: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/pytorch_backend/README.html

Published Time: Sat, 28 Feb 2026 01:07:34 GMT

Markdown Content:
PyTorch (LibTorch) Backend — NVIDIA Triton Inference Server
===============

[Skip to main content](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/pytorch_backend/README.html#main-content)

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
*   [PyTorch](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/pytorch_backend/README.html#)
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
*   PyTorch...

PyTorch (LibTorch) Backend[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/pytorch_backend/README.html#pytorch-libtorch-backend "Link to this heading")
=======================================================================================================================================================================================

[![Image 3: License](https://img.shields.io/badge/License-BSD3-lightgrey.svg)](https://opensource.org/licenses/BSD-3-Clause)

The Triton backend for [PyTorch](https://github.com/pytorch/pytorch) is designed to run [TorchScript](https://pytorch.org/docs/stable/jit.html) models using the PyTorch C++ API. All models created in PyTorch using the python API must be traced/scripted to produce a TorchScript model.

You can learn more about Triton backends in the [Triton Backend](https://github.com/triton-inference-server/backend) repository.

Ask questions or report problems using [Triton Server issues](https://github.com/triton-inference-server/server/issues).

Be sure to read all the information below as well as the [general Triton documentation](https://github.com/triton-inference-server/server#triton-inference-server) available in the [Triton Server](https://github.com/triton-inference-server/server) repository.

Build the PyTorch Backend[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/pytorch_backend/README.html#build-the-pytorch-backend "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Use a recent cmake to build. First install the required dependencies.

apt-get install rapidjson-dev python3-dev python3-pip
pip3 install patchelf==0.17.2

An appropriate PyTorch container from [NVIDIA NGC Catalog](https://ngc.nvidia.com/) must be used. For example, to build a backend that uses the 23.04 version of the PyTorch container from NGC:

mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX:PATH=`pwd`/install -DTRITON_PYTORCH_DOCKER_IMAGE="nvcr.io/nvidia/pytorch:23.04-py3" ..
make install

The following required Triton repositories will be pulled and used in the build. By default, the `main` head will be used for each repository but the listed CMake argument can be used to override the value.

*   triton-inference-server/backend: `-DTRITON_BACKEND_REPO_TAG=[tag]`

*   triton-inference-server/core: `-DTRITON_CORE_REPO_TAG=[tag]`

*   triton-inference-server/common: `-DTRITON_COMMON_REPO_TAG=[tag]`

Build the PyTorch Backend With Custom PyTorch[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/pytorch_backend/README.html#build-the-pytorch-backend-with-custom-pytorch "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Currently, Triton requires that a specially patched version of PyTorch be used with the PyTorch backend. The full source for these PyTorch versions are available as Docker images from [NGC](https://ngc.nvidia.com/).

For example, the PyTorch version compatible with the 25.09 release of Triton is available as `nvcr.io/nvidia/pytorch:25.09-py3` which supports PyTorch version `2.9.0a0`.

> [!NOTE] Additional details and version information can be found in the container’s [release notes](https://docs.nvidia.com/deeplearning/frameworks/pytorch-release-notes/rel-25-09.html#rel-25-09).

Copy over the LibTorch and TorchVision headers and libraries from the [PyTorch NGC container](https://ngc.nvidia.com/catalog/containers/nvidia:pytorch) into local directories. You can see which headers and libraries are needed/copied from the docker.

mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX:PATH=`pwd`/install -DTRITON_PYTORCH_INCLUDE_PATHS="<PATH_PREFIX>/torch;<PATH_PREFIX>/torch/torch/csrc/api/include;<PATH_PREFIX>/torchvision" -DTRITON_PYTORCH_LIB_PATHS="<LIB_PATH_PREFIX>" ..
make install

Using the PyTorch Backend[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/pytorch_backend/README.html#using-the-pytorch-backend "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### PyTorch 2.0 Models[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/pytorch_backend/README.html#pytorch-2-0-models "Link to this heading")

PyTorch 2.0 features are available. However, Triton’s PyTorch backend requires a serialized representation of the model in the form a `model.pt` file. The serialized representation of the model can be generated using PyTorch’s [`torch.save()`](https://docs.pytorch.org/tutorials/beginner/saving_loading_models.html#id1) function to generate the `model.pt` file.

The model repository should look like:

model_repository/
`-- model_directory
 |-- 1
 | `-- model.pt
 `-- config.pbtxt

Where `model.pt` is the serialized representation of the model.

### TorchScript Models[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/pytorch_backend/README.html#torchscript-models "Link to this heading")

The model repository should look like:

model_repository/
`-- model_directory
 |-- 1
 | `-- model.pt
 `-- config.pbtxt

The `model.pt` is the TorchScript model file.

Configuration[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/pytorch_backend/README.html#configuration "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------

Triton exposes some flags to control the execution mode of the TorchScript models through the `Parameters` section of the model’s `config.pbtxt` file.

### Configuration Options[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/pytorch_backend/README.html#configuration-options "Link to this heading")

*   `default_model_name`: Instructs the Triton PyTorch backend to load the model from a file of the given name.

The model config specifying the option would look like:

default_model_name: "another_file_name.pt"  

### Parameters[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/pytorch_backend/README.html#parameters "Link to this heading")

*   `DISABLE_OPTIMIZED_EXECUTION`: Boolean flag to disable the optimized execution of TorchScript models. By default, the optimized execution is always enabled.

The initial calls to a loaded TorchScript model take a significant amount of time. Due to this longer model warmup ([pytorch #57894](https://github.com/pytorch/pytorch/issues/57894)), Triton also allows execution of models without these optimizations. In some models, optimized execution does not benefit performance ([pytorch #19978](https://github.com/pytorch/pytorch/issues/19978)) and in other cases impacts performance negatively ([pytorch #53824](https://github.com/pytorch/pytorch/issues/53824)).

The section of model config file specifying this parameter will look like:

parameters: {
 key: "DISABLE_OPTIMIZED_EXECUTION"
 value: { string_value: "true" }
}  
*   `INFERENCE_MODE`:

Boolean flag to enable the Inference Mode execution of TorchScript models. By default, the inference mode is enabled.

[InferenceMode](https://pytorch.org/cppdocs/notes/inference_mode.html) is a new RAII guard analogous to `NoGradMode` to be used when you are certain your operations will have no interactions with autograd. Compared to `NoGradMode`, code run under this mode gets better performance by disabling autograd.

Please note that in some models, InferenceMode might not benefit performance and in fewer cases might impact performance negatively.

To enable inference mode, use the configuration example below:

parameters: {
 key: "INFERENCE_MODE"
 value: { string_value: "true" }
}  
*   `DISABLE_CUDNN`:

Boolean flag to disable the cuDNN library. By default, cuDNN is enabled.

[cuDNN](https://developer.nvidia.com/cudnn) is a GPU-accelerated library of primitives for deep neural networks. It provides highly tuned implementations for standard routines.

Typically, models run with cuDNN enabled execute faster. However there are some exceptions where using cuDNN can be slower, cause higher memory usage, or result in errors.

To disable cuDNN, use the configuration example below:

parameters: {
 key: "DISABLE_CUDNN"
 value: { string_value: "true" }
}  
*   `ENABLE_WEIGHT_SHARING`:

Boolean flag to enable model instances on the same device to share weights. This optimization should not be used with stateful models. If not specified, weight sharing is disabled.

To enable weight sharing, use the configuration example below:

parameters: {
 key: "ENABLE_WEIGHT_SHARING"
 value: { string_value: "true" }
}  
*   `ENABLE_CACHE_CLEANING`:

Boolean flag to enable CUDA cache cleaning after each model execution. If not specified, cache cleaning is disabled. This flag has no effect if model is on CPU.

Setting this flag to true will likely negatively impact the performance due to additional CUDA cache cleaning operation after each model execution. Therefore, you should only use this flag if you serve multiple models with Triton and encounter CUDA out-of-memory issues during model executions.

To enable cleaning of the CUDA cache after every execution, use the configuration example below:

parameters: {
 key: "ENABLE_CACHE_CLEANING"
 value: { string_value: "true" }
}  
*   `INTER_OP_THREAD_COUNT`:

PyTorch allows using multiple CPU threads during TorchScript model inference. One or more inference threads execute a model’s forward pass on the given inputs. Each inference thread invokes a JIT interpreter that executes the ops of a model inline, one by one.

This parameter sets the size of this thread pool. The default value of this setting is the number of cpu cores.

> [!TIP] Refer to [CPU Threading TorchScript](https://pytorch.org/docs/stable/notes/cpu_threading_torchscript_inference.html) on how to set this parameter properly.

To set the inter-op thread count, use the configuration example below:

parameters: {
 key: "INTER_OP_THREAD_COUNT"
 value: { string_value: "1" }
}  

> [!NOTE] This parameter is set globally for the PyTorch backend. The value from the first model config file that specifies this parameter will be used. Subsequent values from other model config files, if different, will be ignored.

*   `INTRA_OP_THREAD_COUNT`:

In addition to the inter-op parallelism, PyTorch can also utilize multiple threads within the ops (intra-op parallelism). This can be useful in many cases, including element-wise ops on large tensors, convolutions, GEMMs, embedding lookups and others.

The default value for this setting is the number of CPU cores.

> [!TIP] Refer to [CPU Threading TorchScript](https://pytorch.org/docs/stable/notes/cpu_threading_torchscript_inference.html) on how to set this parameter properly.

To set the intra-op thread count, use the configuration example below:

parameters: {
 key: "INTRA_OP_THREAD_COUNT"
 value: { string_value: "1" }
}  
*   **Additional Optimizations**:

Three additional boolean parameters are available to disable certain Torch optimizations that can sometimes cause latency regressions in models with complex execution modes and dynamic shapes. If not specified, all are enabled by default.

`ENABLE_JIT_EXECUTOR`

`ENABLE_JIT_PROFILING`

### Model Instance Group Kind[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/pytorch_backend/README.html#model-instance-group-kind "Link to this heading")

The PyTorch backend supports the following kinds of [Model Instance Groups](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/model_configuration.html#instance-groups) where the input tensors are placed as follows:

*   `KIND_GPU`:

Inputs are prepared on the GPU device associated with the model instance.

*   `KIND_CPU`:

Inputs are prepared on the CPU.

*   `KIND_MODEL`:

Inputs are prepared on the CPU. When loading the model, the backend does not choose the GPU device for the model; instead, it respects the device(s) specified in the model and uses them as they are during inference.

This is useful when the model internally utilizes multiple GPUs, as demonstrated in [this example model](https://github.com/triton-inference-server/server/blob/main/qa/L0_libtorch_instance_group_kind_model/gen_models.py).

> [!IMPORTANT] If a device is not specified in the model, the backend uses the first available GPU device.

To set the model instance group, use the configuration example below:

instance_group {
 count: 2
 kind: KIND_GPU
}

### Customization[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/pytorch_backend/README.html#customization "Link to this heading")

The following PyTorch settings may be customized by setting parameters on the `config.pbtxt`.

[`torch.set_num_threads(int)`](https://pytorch.org/docs/stable/generated/torch.set_num_threads.html#torch.set_num_threads)

*   Key: `NUM_THREADS`

*   Value: The number of threads used for intra-op parallelism on CPU.

[`torch.set_num_interop_threads(int)`](https://pytorch.org/docs/stable/generated/torch.set_num_interop_threads.html#torch.set_num_interop_threads)

*   Key: `NUM_INTEROP_THREADS`

*   Value: The number of threads used for interop parallelism (e.g. in JIT interpreter) on CPU.

[`torch.compile()` parameters](https://pytorch.org/docs/stable/generated/torch.compile.html#torch-compile)

*   Key: `TORCH_COMPILE_OPTIONAL_PARAMETERS`

*   Value: Any of following parameter(s) encoded as a JSON object.

    *   `fullgraph` (`bool`): Whether it is ok to break model into several subgraphs.

    *   `dynamic` (`bool`): Use dynamic shape tracing.

    *   `backend` (`str`): The backend to be used.

    *   `mode` (`str`): Can be either `"default"`, `"reduce-overhead"`, or `"max-autotune"`.

    *   `options` (`dict`): A dictionary of options to pass to the backend.

    *   `disable` (`bool`): Turn `torch.compile()` into a no-op for testing.

For example:

parameters: {
 key: "NUM_THREADS"
 value: { string_value: "4" }
}
parameters: {
 key: "TORCH_COMPILE_OPTIONAL_PARAMETERS"
 value: { string_value: "{\"disable\": true}" }
}

Important Notes[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/pytorch_backend/README.html#important-notes "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   The execution of PyTorch model on GPU is asynchronous in nature. See [CUDA Asynchronous Execution](https://pytorch.org/docs/stable/notes/cuda.html#asynchronous-execution) for additional details. Consequently, an error in PyTorch model execution may be raised during the next few inference requests to the server. Setting environment variable `CUDA_LAUNCH_BLOCKING=1` when launching server will help in correctly debugging failing cases by forcing synchronous execution.

    *   The PyTorch model in such cases may or may not recover from the failed state and a restart of the server may be required to continue serving successfully.

*   PyTorch does not support Tensor of Strings but it does support models that accept a List of Strings as input(s) / produces a List of String as output(s). For these models Triton allows users to pass String input(s)/receive String output(s) using the String datatype. As a limitation of using List instead of Tensor for String I/O, only for 1-dimensional input(s)/output(s) are supported for I/O of String type.

*   In a multi-GPU environment, a potential runtime issue can occur when using [Tracing](https://pytorch.org/docs/stable/generated/torch.jit.trace.html) to generate a [TorchScript](https://pytorch.org/docs/stable/jit.html) model. This issue arises due to a device mismatch between the model instance and the tensor.

By default, Triton creates a single execution instance of the model for each available GPU. The runtime error occurs when a request is sent to a model instance with a different GPU device from the one used during the TorchScript generation process.

To address this problem, it is highly recommended to use [Scripting](https://pytorch.org/docs/stable/generated/torch.jit.script.html#torch.jit.script) instead of Tracing for model generation in a multi-GPU environment. Scripting avoids the device mismatch issue and ensures compatibility with different GPUs when used with Triton.

However, if using Tracing is unavoidable, there is a workaround available. You can explicitly specify the GPU device for the model instance in the [model configuration](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/model_configuration.html#instance-groups) to ensure that the model instance and the tensors used for inference are assigned to the same GPU device as on which the model was traced.

*   When using `KIND_MODEL` as model instance kind, the default device of the first parameter on the model is used.

> [!WARNING]
> 
> 
> *   Python functions optimizable by `torch.compile` may not be served directly in the `model.py` file, they need to be enclosed by a class extending the [`torch.nn.Module`](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module).
> 
> *   Model weights cannot be shared across multiple instances on the same GPU device.

[previous Python Backend](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/python_backend/README.html "previous page")[next ONNX Runtime Backend](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/onnxruntime_backend/README.html "next page")

 On this page 

*   [Build the PyTorch Backend](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/pytorch_backend/README.html#build-the-pytorch-backend)
*   [Build the PyTorch Backend With Custom PyTorch](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/pytorch_backend/README.html#build-the-pytorch-backend-with-custom-pytorch)
*   [Using the PyTorch Backend](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/pytorch_backend/README.html#using-the-pytorch-backend)
    *   [PyTorch 2.0 Models](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/pytorch_backend/README.html#pytorch-2-0-models)
    *   [TorchScript Models](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/pytorch_backend/README.html#torchscript-models)

*   [Configuration](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/pytorch_backend/README.html#configuration)
    *   [Configuration Options](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/pytorch_backend/README.html#configuration-options)
    *   [Parameters](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/pytorch_backend/README.html#parameters)
    *   [Model Instance Group Kind](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/pytorch_backend/README.html#model-instance-group-kind)
    *   [Customization](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/pytorch_backend/README.html#customization)

*   [Important Notes](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/pytorch_backend/README.html#important-notes)

[![Image 4: NVIDIA](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_static/nvidia-logo-horiz-rgb-1c-blk-for-screen.svg)![Image 5: NVIDIA](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_static/nvidia-logo-horiz-rgb-1c-wht-for-screen.svg)](https://www.nvidia.com/)

[Privacy Policy](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/) | [Your Privacy Choices](https://www.nvidia.com/en-us/about-nvidia/privacy-center/) | [Terms of Service](https://www.nvidia.com/en-us/about-nvidia/terms-of-service/) | [Accessibility](https://www.nvidia.com/en-us/about-nvidia/accessibility/) | [Corporate Policies](https://www.nvidia.com/en-us/about-nvidia/company-policies/) | [Product Security](https://www.nvidia.com/en-us/product-security/) | [Contact](https://www.nvidia.com/en-us/contact/)

Copyright © 2018-2026, NVIDIA Corporation.
