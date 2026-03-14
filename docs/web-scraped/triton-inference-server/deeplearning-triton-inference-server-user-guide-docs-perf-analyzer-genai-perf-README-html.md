# Source: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html

Title: GenAI-Perf — NVIDIA Triton Inference Server

URL Source: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html

Published Time: Sat, 28 Feb 2026 01:03:58 GMT

Markdown Content:
GenAI-Perf — NVIDIA Triton Inference Server
===============

[Skip to main content](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#main-content)

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
*   [PyTorch](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/pytorch_backend/README.html)
*   [ONNX Runtime](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/onnxruntime_backend/README.html)
*   [TensorRT](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tensorrt_backend/README.html)
*   [FIL](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/fil_backend/README.html)
*   [DALI](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/dali_backend/README.html)
*   [Custom](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/backend/README.html)

Performance benchmarking and tuning

*   [GenAI Perf Analyzer](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_benchmark/genai_perf.html)

    *   [Overview](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#)
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
*   [GenAI Performance Analyzer](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_benchmark/genai_perf.html)
*   GenAI-Perf

GenAI-Perf[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#genai-perf "Link to this heading")
==================================================================================================================================================================

⚠️ **GenAI-Perf is being phased out.** We are no longer actively developing new features for GenAI-Perf. For new performance benchmarking needs, please use [AIPerf](https://github.com/ai-dynamo/aiperf) instead.

GenAI-Perf is a command line tool for measuring the throughput and latency of generative AI models as served through an inference server. For large language models (LLMs), GenAI-Perf provides metrics such as [output token throughput](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#output_token_throughput_metric), [time to first token](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#time_to_first_token_metric), [time to second token](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#time_to_second_token_metric), [inter token latency](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#inter_token_latency_metric), and [request throughput](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#request_throughput_metric). For a full list of metrics please see the [Metrics section](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#metrics).

Users specify a model name, an inference server URL, the type of inputs to use (synthetic or from a dataset defined via a file), and the type of load to generate (number of concurrent requests, request rate).

GenAI-Perf generates the specified load, measures the performance of the inference server and reports the metrics in a simple table as console output. The tool also logs all results in a csv and json file that can be used to derive additional metrics and visualizations. The inference server must already be running when GenAI-Perf is run.

You can use GenAI-Perf to run performance benchmarks on

*   [Large Language Models](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/docs/tutorial.html)

*   [Multi-Modal Language Models](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/docs/multi_modal.html)

*   [Embedding Models](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/docs/embeddings.html)

*   [Ranking Models](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/docs/rankings.html)

*   [Multiple LoRA Adapters](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/docs/lora.html)

You can also use GenAI-Perf to run benchmarks on your custom APIs using either [customizable frontends](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/docs/customizable_frontends.html) or [customizable payloads](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/docs/customizable_payloads.html). Customizable frontends provide more customizability, while customizable payloads allow you to specify specific payload schemas using a Jinja2 template.

Installation[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#installation "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

The easiest way to install GenAI-Perf is through pip.

### Install GenAI-Perf (Ubuntu 24.04, Python 3.10+)[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#install-genai-perf-ubuntu-24-04-python-3-10 "Link to this heading")

pip install genai-perf

**NOTE**: you must already have CUDA 12 installed

Alternatively, to install the container:
[Triton Server SDK container](https://ngc.nvidia.com/catalog/containers/nvidia:tritonserver)

Pull the latest release using the following command:

export RELEASE="25.01"

docker run -it --net=host --gpus=all nvcr.io/nvidia/tritonserver:${RELEASE}-py3-sdk

# Validate the genai-perf command works inside the container:
genai-perf --help

You can also build Perf Analyzer [from source](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/docs/install.html#build-from-source) to use alongside GenAI-Perf as well.

Quick Start[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#quick-start "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this quick start, we will use GenAI-Perf to run performance benchmarking on the GPT-2 model running on Triton Inference Server with a TensorRT-LLM engine.

### Serve GPT-2 TensorRT-LLM model using Triton CLI[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#serve-gpt-2-tensorrt-llm-model-using-triton-cli "Link to this heading")

You can follow the [quickstart guide](https://github.com/triton-inference-server/triton_cli?tab=readme-ov-file#serving-a-trt-llm-model) in the Triton CLI Github repository to serve GPT-2 on the Triton server with the TensorRT-LLM backend. **NOTE**: pip dependency error messages can be safely ignored.

The full instructions are copied below for convenience:

# This container comes with all of the dependencies for building TRT-LLM engines
# and serving the engine with Triton Inference Server.
docker run -ti \
 --gpus all \
 --network=host \
 --shm-size=1g --ulimit memlock=-1 \
 -v /tmp:/tmp \
 -v ${HOME}/.cache/huggingface:/root/.cache/huggingface \
 nvcr.io/nvidia/tritonserver:25.01-trtllm-python-py3

# Install the Triton CLI
pip install git+https://github.com/triton-inference-server/triton_cli.git@0.1.2

# Build TRT LLM engine and generate a Triton model repository pointing at it
triton remove -m all
triton import -m gpt2 --backend tensorrtllm

# Start Triton pointing at the default model repository
triton start

### Running GenAI-Perf[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#running-genai-perf "Link to this heading")

Now we can run GenAI-Perf inside the Triton Inference Server SDK container:

genai-perf profile \
 -m gpt2 \
 --backend tensorrtllm \
 --streaming

Example output:

                              NVIDIA GenAI-Perf | LLM Metrics
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━┓
┃                         Statistic ┃    avg ┃    min ┃    max ┃    p99 ┃    p90 ┃    p75 ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━┩
│          Time to first token (ms) │  16.26 │  12.39 │  17.25 │  17.09 │  16.68 │  16.56 │
│          Inter token latency (ms) │   1.85 │   1.55 │   2.04 │   2.02 │   1.97 │   1.92 │
│              Request latency (ms) │ 499.20 │ 451.01 │ 554.61 │ 548.69 │ 526.13 │ 514.19 │
│            Output sequence length │ 261.90 │ 256.00 │ 298.00 │ 296.60 │ 270.00 │ 265.00 │
│             Input sequence length │ 550.06 │ 550.00 │ 553.00 │ 551.60 │ 550.00 │ 550.00 │
│ Output token throughput (per sec) │ 520.87 │    N/A │    N/A │    N/A │    N/A │    N/A │
│      Request throughput (per sec) │   1.99 │    N/A │    N/A │    N/A │    N/A │    N/A │
└───────────────────────────────────┴────────┴────────┴────────┴────────┴────────┴────────┘

See [Tutorial](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/docs/tutorial.html) for additional examples.

Configuration File[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#configuration-file "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In addition to setting options via the command-line, GenAI-Perf supports the passing in of a config file (in YAML format). The command is:

genai-perf config -f <config_file>

### Creating a Template Config File[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#creating-a-template-config-file "Link to this heading")

In order to make it easier for you to use config files, we have added a new subcommand that generates a template config file containing all possible options, pre-populated to their default settings. The command to create this is:

genai-perf create-template

By default the config file is named `genai_perf_config.yaml`, but you can change that by passing in a custom name using the `-f` option.

 For less experienced users, you can include `-v/--verbose` and the config file will also contain descriptions for each option (similar to what you would see using `-h` from the command line).

Here is a sample section of what the template config file looks like:

  endpoint:
    model_selection_strategy: round_robin
    backend: tensorrtllm
    custom:
    type: kserve
    streaming: False
    server_metrics_urls: http://localhost:8002/metrics
    url: localhost:8001
    grpc_method:

and with `--verbose`:

 endpoint:
 # When multiple model are specified, this is how a specific model should be assigned to a prompt.
 # round_robin: nth prompt in the list gets assigned to n-mod len(models).
 # random: assignment is uniformly random
 model_selection_strategy: round_robin

 # When benchmarking Triton, this is the backend of the model.
 # For the TENSORRT-LLM backend,you currently must set 'exclude_input_in_output' to true
 # in the model config to not echo the input tokens
 backend: tensorrtllm

 # Set a custom endpoint that differs from the OpenAI defaults.
 custom:

 # The type to send requests to on the server.
 type: kserve

 # An option to enable the use of the streaming API.
 streaming: False

 # The list of server metrics URLs.
 # These are used for Telemetry metric reporting.
 server_metrics_urls: http://localhost:9400/metrics

 # URL of the endpoint to target for benchmarking.
 url: localhost:8001

 # A fully-qualified gRPC method name in '<package>.<service>/<method>' format.
 # The option is only supported by dynamic gRPC service kind and is
 # required to identify the RPC to use when sending requests to the server.
 grpc_method:

### Overriding Config Options[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#overriding-config-options "Link to this heading")

Once you have setup your config file to your liking, there could be times where you might want to re-profile with just a few options changed.

 Rather than editing your config you can include the `--override-config` option on the CLI along with the options you want to change. For example:

genai-perf config -f genai_perf_config.yaml --override-config --warmup-request-count 100 --concurrency 32

Analyze[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#analyze "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------

GenAI-Perf can be used to sweep through PA or GenAI-Perf stimulus allowing the user to profile multiple scenarios with a single command. See [Analyze](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/docs/analyze.html) for details on how this subcommand can be utilized.

Visualization[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#visualization "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

GenAI-Perf can also generate various plots that visualize the performance of the current profile run. This is disabled by default but users can easily enable it by passing the `--generate-plots` option when running the benchmark:

genai-perf profile \
 -m gpt2 \
 --backend tensorrtllm \
 --streaming \
 --concurrency 1 \
 --generate-plots

This will generate a [set of default plots](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/docs/example_plots.html) such as:

*   Time to first token (TTFT) analysis

*   Request latency analysis

*   TTFT vs Input sequence lengths

*   Inter token latencies vs Token positions

*   Input sequence lengths vs Output sequence lengths

Process Export Files[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#process-export-files "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

GenAI-Perf can be used to process multiple profile export files from distributed runs and generate outputs with aggregated metrics. See [Process Export Files](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/docs/process_export_files.html) for details on how this subcommand can be utilized.

Model Inputs[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#model-inputs "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

GenAI-Perf supports model input prompts from either synthetically generated inputs, or from a dataset defined via a file.

When the dataset is synthetic, you can specify the following options:

*   `--num-dataset-entries <int>`: The number of unique payloads to sample from. These will be reused until benchmarking is complete.

*   `--synthetic-input-tokens-mean <int>`: The mean of number of tokens in the generated prompts when using synthetic data, >= 1.

*   `--synthetic-input-tokens-stddev <int>`: The standard deviation of number of tokens in the generated prompts when using synthetic data, >= 0.

*   `--random-seed <int>`: The seed used to generate random values, >= 0.

*   `--request-count <int>`: The number of requests to benchmark

*   `--warmup-request-count <int>`: The number of requests to send before benchmarking

When the dataset is coming from a file, you can specify the following options:

*   `--input-file <path>`: The input file or directory containing the prompts or filepaths to images to use for benchmarking as JSON objects.

For any dataset, you can specify the following options:

*   `--num-prefix-prompts <int>`: The number of synthetic prefix prompts to sample from. If this value is >0, synthetic prefix prompts will be prepended to user prompts.

*   `--output-tokens-mean <int>`: The mean number of tokens in each output. Ensure the `--tokenizer` value is set correctly, >= 1.

*   `--output-tokens-stddev <int>`: The standard deviation of the number of tokens in each output. This is only used when output-tokens-mean is provided, >= 1.

*   `--output-tokens-mean-deterministic`: When using `--output-tokens-mean`, this flag can be set to improve precision by setting the minimum number of tokens equal to the requested number of tokens. This is currently supported with Triton. Note that there is still some variability in the requested number of output tokens, but GenAi-Perf attempts its best effort with your model to get the right number of output tokens.

*   `--prefix-prompt-length <int>`: The number of tokens to include in each prefix prompt. This value is only used if –num-prefix-prompts is positive.

You can optionally set additional model inputs with the following option:

*   `--extra-inputs <input_name>:<value>`: An additional input for use with the model with a singular value, such as `stream:true` or `max_tokens:5`. This flag can be repeated to supply multiple extra inputs.

For [Large Language Models](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/docs/tutorial.html), there is no batch size (i.e. batch size is always `1`). Each request includes the inputs for one individual inference. Other modes such as the [embeddings](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/docs/embeddings.html) and [rankings](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/docs/rankings.html) endpoints support client-side batching, where `--batch-size-text N` means that each request sent will include the inputs for `N` separate inferences, allowing them to be processed together.

### Use moon_cake file as input payload[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#use-moon-cake-file-as-input-payload "Link to this heading")

Genai-perf supports `--input-file payload:<file>` as the command option to use a payload file with a fixed schedule workload for profiling.

The payload file is in [moon_cake format](https://github.com/kvcache-ai/Mooncake) which contains a `timestamp` field and you can optionally add `input_length`, `output_length`, `text_input`, `session_id`, `hash_ids` and `priority`. For further examples using these fields, you can refer to our [multi-turn session benchmark tutorial](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/docs/multi_turn.html#approach-2-benchmark-with-a-custom-dataset).

Here is an example file:

{
    "timestamp": 0,
    "input_length": 6955,
    "output_length": 52,
    "hash_ids": [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 2353, 2354]
}
{
    "timestamp": 10535,	# in milli-second
    "input_length": 6472,
    "output_length": 26,
    "hash_ids": [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 2366]
}
{
    "timestamp": 27482,
    "input_length": 6955,
    "output_length": 52,
    "hash_ids": [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 2353, 2354]
}

`hash_ids` are a list of hash_id, each of which maps to a unique synthetic prompt sequence with `block_size` (current block size is 512) of tokens after tokenizer encoding, defined in [create_synthetic_prompt](https://github.com/triton-inference-server/perf_analyzer/blob/main/genai-perf/genai_perf/inputs/retrievers/synthetic_prompt_generator.py#L37). Since the same hash_id maps to the same input block, it is effective to test features such as kv cache and speculative decoding.

### How to generate a payload file[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#how-to-generate-a-payload-file "Link to this heading")

#### 1. Synthetic data from sampling[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#synthetic-data-from-sampling "Link to this heading")

[Nvidia Dynamo](https://github.com/ai-dynamo/dynamo) provides [a script](https://github.com/ai-dynamo/dynamo/blob/main/benchmarks/sin_load_generator/sin_synth.py) (with [README](https://github.com/ai-dynamo/dynamo/blob/main/benchmarks/sin_load_generator/README.md)) to generate synthetic moon_cake style payload:

python sin_synth.py \
 --time-duration 600 \
 --request-rate-min 5 \
 --request-rate-max 20 \
 --request-rate-period 150 \
 --isl1 3000 \
 --osl1 150 \
 --isl2 3000 \
 --osl2 150

This will generate a mooncake style payload file with

*   duration = 600 seconds

*   isl/osl = 3000/150

*   request rate varies sinusoidally from 0.75 to 3 requests with a period of 150 seconds For other models and GPU SKUs, adjust the request rate ranges accordingly to match the load.

Example genai-perf command to run the generated payload:

genai-perf profile \
 --tokenizer deepseek-ai/DeepSeek-R1-Distill-Llama-8B \
 -m deepseek-ai/DeepSeek-R1-Distill-Llama-8B \
 --endpoint-type chat \
 --url http://localhost:8000 \
 --streaming \
 --input-file payload:sin_b512_t600_rr5.0-20.0-150.0_io3000150-3000150-0.2-0.8-10.jsonl

#### 2. Record real traffic and replay[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#record-real-traffic-and-replay "Link to this heading")

We recommend users to build a traffic footprint collector over their inference service to generate the moon_cake format payload file based on real service traffic. Although popular inference servers do not support this feature, users can add this feature to their inference service.

Example code:

# Hypothetical integration with the inference engine
import InferenceEngine  # Assume this exists

engine = InferenceEngine()
logger = Logger("mooncake_traffic.jsonl")

def process_request(prompt: str):
    result = engine.infer(prompt)
    logger.log_request({
        "input_length": len(engine.tokenize(prompt)),
        "output_length": len(engine.tokenize(result)),
        "text_input": prompt,
        "session_id": str(uuid.uuid4()),
        "hash_ids": engine.get_kvcache_hashes(prompt),
        "priority": 1
    })
    return result

Authentication[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#authentication "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

GenAI-Perf can benchmark secure endpoints such as OpenAI, which require API key authentication. To do so, you must add your API key directly in the command. Add the following flag to your command.

-H "Authorization: Bearer ${API_KEY}" -H "Accept: text/event-stream"

Metrics[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#metrics "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------

GenAI-Perf collects a diverse set of metrics that captures the performance of the inference server.

| Metric | Description | Aggregations |
| --- | --- | --- |
| Time to First Token | Time between when a request is sent and when its first response is received, one value per request in benchmark | Avg, min, max, p99, p90, p75 |
| Time to Second Token | Time between when the first streaming response is received and when the second streaming response is received, one value per request in benchmark | Avg, min, max, p99, p90, p75 |
| Inter Token Latency | Time between intermediate responses for a single request divided by the number of generated tokens of the latter response, one value per response per request in benchmark | Avg, min, max, p99, p90, p75 |
| Output Token Throughput Per User | Total number of output tokens (excluding the first token) divided by the total duration of the generation phase of each request | Avg, min, max, p99, p90, p75 |
| Request Latency | Time between when a request is sent and when its final response is received, one value per request in benchmark | Avg, min, max, p99, p90, p75 |
| Output Sequence Length | Total number of output tokens of a request, one value per request in benchmark | Avg, min, max, p99, p90, p75 |
| Input Sequence Length | Total number of input tokens of a request, one value per request in benchmark | Avg, min, max, p99, p90, p75 |
| Output Token Throughput | Total number of output tokens from benchmark divided by benchmark duration | None–one value per benchmark |
| Request Throughput | Number of final responses from benchmark divided by benchmark duration | None–one value per benchmark |

### GPU Telemetry[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#gpu-telemetry "Link to this heading")

During benchmarking, GPU metrics such as GPU power usage, GPU utilization, energy consumption, and total GPU memory are automatically collected. These metrics are collected from the `/metrics` endpoint exposed by the [DCGM Exporter](https://github.com/NVIDIA/dcgm-exporter), which must be running on the **same machine** as the inference server.

GenAI-Perf collects the following GPU metrics during benchmarking:

### Power Metrics[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#power-metrics "Link to this heading")

*   `gpu_power_usage`

*   `gpu_power_limit`

*   `energy_consumption`

### Memory Metrics[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#memory-metrics "Link to this heading")

*   `total_gpu_memory`

*   `gpu_memory_used`

*   `gpu_memory_free`

### Temperature Metrics[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#temperature-metrics "Link to this heading")

*   `gpu_temperature`

*   `gpu_memory_temperature`

### Clock Metrics[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#clock-metrics "Link to this heading")

*   `gpu_clock_sm`

*   `gpu_clock_memory`

### Utilization Metrics[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#utilization-metrics "Link to this heading")

*   `gpu_utilization`

*   `sm_utilization`

*   `memory_copy_utilization`

*   `video_encoder_utilization`

*   `video_decoder_utilization`

### ECC Metrics[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#ecc-metrics "Link to this heading")

*   `total_ecc_sbe_volatile`

*   `total_ecc_dbe_volatile`

*   `total_ecc_sbe_aggregate`

*   `total_ecc_dbe_aggregate`

### Errors and Violations Metrics[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#errors-and-violations-metrics "Link to this heading")

*   `xid_last_error`

*   `power_throttle_duration`

*   `thermal_throttle_duration`

### Retired Pages Metrics[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#retired-pages-metrics "Link to this heading")

*   `retired_pages_sbe`

*   `retired_pages_dbe`

### NVLink Error Metrics[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#nvlink-error-metrics "Link to this heading")

*   `total_nvlink_crc_flit_errors`

*   `total_nvlink_crc_data_errors`

### PCIE Metrics[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#pcie-metrics "Link to this heading")

*   `pcie_transmit_throughput`

*   `pcie_receive_throughput`

*   `pcie_replay_counter`

> [!Note] Use the `--verbose` flag to print telemetry metrics on the console.

To collect GPU metrics, follow the [GPU Telmetry tutorial](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/docs/gpu_telemetry.html). Use the provided [`custom-metrics.csv`](https://github.com/triton-inference-server/perf_analyzer/blob/main/genai-perf/docs/assets/custom_gpu_metrics.csv) to ensure all required metrics are included in the output.

Command Line Options[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#command-line-options "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### `-h`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#h "Link to this heading")

### `--help`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#help "Link to this heading")

Show the help message and exit.

### Config Options[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#config-options "Link to this heading")

#### `-f`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#f "Link to this heading")

#### `--file`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#file "Link to this heading")

The path to the config file - REQUIRED.

#### `--override-config`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#override-config "Link to this heading")

An option that allows the user to override values specified in the config file.

### Template Options[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#template-options "Link to this heading")

#### `-f`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#id1 "Link to this heading")

#### `--file`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#id2 "Link to this heading")

The name of the template file to be created. Default is `genai_perf_config.yaml`.

### Endpoint Options:[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#endpoint-options "Link to this heading")

#### `-m <list>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#m-list "Link to this heading")

#### `--model <list>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#model-list "Link to this heading")

The names of the models to benchmark. A single model is recommended, unless you are [profiling multiple LoRA adapters](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/docs/lora.html). (default: `None`)

#### `--model-selection-strategy {round_robin, random}`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#model-selection-strategy-round-robin-random "Link to this heading")

When multiple models are specified, this is how a specific model is assigned to a prompt. Round robin means that each model receives a request in order. Random means that assignment is uniformly random (default: `round_robin`)

#### `--backend {tensorrtllm,vllm}`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#backend-tensorrtllm-vllm "Link to this heading")

When benchmarking Triton, this is the backend of the model. (default: tensorrtllm)

#### `--endpoint <str>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#endpoint-str "Link to this heading")

Set a custom endpoint that differs from the OpenAI defaults. (default: `None`)

#### `--endpoint-type <str>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#endpoint-type-str "Link to this heading")

The endpoint-type to send requests to on the server. (default: `kserve`)

#### `--server-metrics-urls <list>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#server-metrics-urls-list "Link to this heading")

The list of server metrics URLs. These are used for Telemetry metric reporting when benchmarking. Example usage: –server-metrics-urls http://server1:9400/metrics http://server2:9400/metrics. (default: `http://localhost:9400/metrics`)

#### `--streaming`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#streaming "Link to this heading")

An option to enable the use of the streaming API. (default: `False`)

#### `-u <url>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#u-url "Link to this heading")

#### `--url <url>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#url-url "Link to this heading")

URL of the endpoint to target for benchmarking. (default: `None`)

#### `--grpc-method <str>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#grpc-method-str "Link to this heading")

A fully-qualified gRPC method name in ‘./’ format. The option is only supported with dynamic gRPC and is required to identify the RPC to use when sending requests to the server. (default: `None`)

### Input Options[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#input-options "Link to this heading")

#### `--audio-length-mean <int>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#audio-length-mean-int "Link to this heading")

The mean length of audio data in seconds. (default: `0`)

#### `--audio-length-stddev <int>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#audio-length-stddev-int "Link to this heading")

The standard deviation of the length of audio data in seconds. (default: `0`)

#### `--audio-format <str>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#audio-format-str "Link to this heading")

The format of the audio data. Currently we support wav and mp3 format. (default: `wav`)

#### `--audio-depths <int>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#audio-depths-int "Link to this heading")

A list of audio bit depths to randomly select from in bits. (default: `[16]`)

#### `--audio-sample-rates <int>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#audio-sample-rates-int "Link to this heading")

A list of audio sample rates to randomly select from in kHz. (default: `[16]`)

#### `--audio-num-channels <int>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#audio-num-channels-int "Link to this heading")

The number of audio channels to use for the audio data generation. Currently only 1 (mono) and 2 (stereo) are supported. (default: `1` (mono channel))

#### `-b <int>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#b-int "Link to this heading")

#### `--batch-size <int>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#batch-size-int "Link to this heading")

#### `–batch-size-text [#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#batch-size-text "Link to this heading")

The text batch size of the requests GenAI-Perf should send. (default: `1`)

#### `–batch-size-text [#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#id3 "Link to this heading")

The text batch size of the requests GenAI-Perf should send. (default: `1`)

#### `--batch-size-audio <int>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#batch-size-audio-int "Link to this heading")

The audio batch size of the requests GenAI-Perf should send. This is currently only supported with the OpenAI `multimodal` endpoint type. (default: `1`)

#### `--batch-size-text <int>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#batch-size-text-int "Link to this heading")

The text batch size of the requests GenAI-Perf should send. This is currently only supported with the [embeddings](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/docs/embeddings.html), and [rankings](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/docs/rankings.html) endpoint types. (default: `1`)

#### `--batch-size-image <int>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#batch-size-image-int "Link to this heading")

The image batch size of the requests GenAI-Perf should send. This is currently only supported with the image retrieval endpoint type. (default: `1`)

#### `--extra-inputs <str>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#extra-inputs-str "Link to this heading")

Provide additional inputs to include with every request. You can repeat this flag for multiple inputs. Inputs should be in an input_name:value format. Alternatively, a string representing a json formatted dict can be provided. (default: `None`)

#### `--header <str>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#header-str "Link to this heading")

#### `--H <str>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#h-str "Link to this heading")

Add a custom header to the requests. Headers must be specified as ‘Header:Value’. You can repeat this flag for multiple headers. (default: `None`)

#### `--input-file <path>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#input-file-path "Link to this heading")

The input file or directory for profiling. Each line should be a JSON object with a `text` or `image` field in JSONL format. Example: `{"text": "Your prompt here"}`. To use synthetic files, prefix with `synthetic:` followed by a comma-separated list of filenames without extensions (Example: `synthetic:queries,passages`). To use a payload file with a fixed schedule workload, prefix with `payload:` followed by the filename (Example: `payload:input.jsonl`). (default: `None`)

#### `--num-dataset-entries <int>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#num-dataset-entries-int "Link to this heading")

The number of unique payloads to sample from. These will be reused until benchmarking is complete. (default: `100`)

#### `--num-prefix-prompts <int>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#num-prefix-prompts-int "Link to this heading")

The number of prefix prompts to select from. If this value is not zero, these are prompts that are prepended to input prompts. This is useful for benchmarking models that use a K-V cache. (default: `0`)

#### `--output-tokens-mean <int>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#output-tokens-mean-int "Link to this heading")

#### `--osl`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#osl "Link to this heading")

The mean number of tokens in each output. Ensure the `--tokenizer` value is set correctly. (default: `-1`)

#### `--output-tokens-mean-deterministic`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#output-tokens-mean-deterministic "Link to this heading")

When using `--output-tokens-mean`, this flag can be set to improve precision by setting the minimum number of tokens equal to the requested number of tokens. This is currently supported with Triton. Note that there is still some variability in the requested number of output tokens, but GenAi-Perf attempts its best effort with your model to get the right number of output tokens. (default: `False`)

#### `--output-tokens-stddev <int>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#output-tokens-stddev-int "Link to this heading")

The standard deviation of the number of tokens in each output. This is only used when `--output-tokens-mean` is provided. (default: `0`)

#### `--random-seed <int>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#random-seed-int "Link to this heading")

The seed used to generate random values. If not provided, a random seed will be used.

#### `--request-count <int>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#request-count-int "Link to this heading")

#### `--num-requests <int>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#num-requests-int "Link to this heading")

The number of requests to use for measurement. (default: `10`)

#### `--synthetic-input-tokens-mean <int>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#synthetic-input-tokens-mean-int "Link to this heading")

#### `--isl`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#isl "Link to this heading")

The mean of number of tokens in the generated prompts when using synthetic data. (default: `550`)

#### `--synthetic-input-tokens-stddev <int>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#synthetic-input-tokens-stddev-int "Link to this heading")

The standard deviation of number of tokens in the generated prompts when using synthetic data. (default: `0`)

#### `--prefix-prompt-length <int>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#prefix-prompt-length-int "Link to this heading")

The number of tokens in each prefix prompt. This value is only used if –num-prefix-prompts is positive. Note that due to the prefix and user prompts being concatenated, the number of tokens in the final prompt may be off by one. (default: `100`)

#### `--image-width-mean <int>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#image-width-mean-int "Link to this heading")

The mean width of images in pixels when generating synthetic image data. (default: `0`)

#### `--image-width-stddev <int>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#image-width-stddev-int "Link to this heading")

The standard deviation of width of images in pixels when generating synthetic image data. (default: `0`)

#### `--image-height-mean <int>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#image-height-mean-int "Link to this heading")

The mean height of images in pixels when generating synthetic image data. (default: `0`)

#### `--image-height-stddev <int>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#image-height-stddev-int "Link to this heading")

The standard deviation of height of images in pixels when generating synthetic image data. (default: `0`)

#### `--image-format <str>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#image-format-str "Link to this heading")

The compression format of the images. If format is not selected, format of generated image is selected at random.

#### `--warmup-request-count <int>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#warmup-request-count-int "Link to this heading")

#### `--num-warmup-requests <int>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#num-warmup-requests-int "Link to this heading")

The number of warmup requests to send before benchmarking. (default: `0`)

### Profiling Options[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#profiling-options "Link to this heading")

#### `--concurrency <int>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#concurrency-int "Link to this heading")

The concurrency value to benchmark. (default: `None`)

#### `--measurement-interval <int>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#measurement-interval-int "Link to this heading")

#### `-p <int>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#p-int "Link to this heading")

The time interval used for each measurement in milliseconds. Perf Analyzer will sample a time interval specified and take measurement over the requests completed within that time interval. When using the default stability percentage, GenAI-Perf will benchmark for 3*(measurement_interval) milliseconds.

#### `--request-rate <float>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#request-rate-float "Link to this heading")

Sets the request rate for the load generated by PA. (default: `None`)

#### `--fixed-schedule`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#fixed-schedule "Link to this heading")

An option to enable fixed schedule (trace) inference load mode. (default: `False`)

#### `-s <float>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#s-float "Link to this heading")

#### `--stability-percentage <float>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#stability-percentage-float "Link to this heading")

The allowed variation in latency measurements when determining if a result is stable. The measurement is considered as stable if the ratio of max / min from the recent 3 measurements is within (stability percentage) in terms of both infer per second and latency. (default: `999`)

### Output Options[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#output-options "Link to this heading")

#### `--artifact-dir`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#artifact-dir "Link to this heading")

The directory to store all the (output) artifacts generated by GenAI-Perf and Perf Analyzer. (default: `artifacts`)

#### `--checkpoint-dir`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#checkpoint-dir "Link to this heading")

The directory to store/restore the checkpoint generated by GenAI-Perf.

#### `--generate-plots`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#generate-plots "Link to this heading")

An option to enable the generation of plots. (default: False)

#### `--enable-checkpointing`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#enable-checkpointing "Link to this heading")

Enables the checkpointing of the GenAI-Perf state. This is useful for running GenAI-Perf in a stateful manner. (default: False)

#### `--profile-export-file <path>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#profile-export-file-path "Link to this heading")

The path where the perf_analyzer profile export will be generated. By default, the profile export will be to `profile_export.json`. The genai-perf files will be exported to `<profile_export_file>_genai_perf.json` and `<profile_export_file>_genai_perf.csv`. For example, if the profile export file is `profile_export.json`, the genai-perf file will be exported to `profile_export_genai_perf.csv`. (default: `profile_export.json`)

### Session Options[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#session-options "Link to this heading")

#### `--num-sessions`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#num-sessions "Link to this heading")

The number of sessions to simulate. This is used when generating synthetic session data. (default: `0`)

#### `--session-concurrency <int>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#session-concurrency-int "Link to this heading")

The number of concurrent sessions to benchmark. This must be specified when benchmarking sessions. (default: `0`)

#### `--session-delay-ratio <float>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#session-delay-ratio-float "Link to this heading")

A ratio to scale multi-turn delays when using a payload file. This allows adjusting the timing between turns in a session without changing the payload file. (default: `1.0`)

#### `--session-turn-delay-mean`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#session-turn-delay-mean "Link to this heading")

The mean delay (in milliseconds) between turns in a session. (default: `0`)

#### `--session-turn-delay-stddev`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#session-turn-delay-stddev "Link to this heading")

The standard deviation of the delay (in milliseconds) between turns in a session. (default: `0`)

#### `--session-turns-mean`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#session-turns-mean "Link to this heading")

The mean number of turns per session. (default: `1`)

#### `--session-turns-stddev`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#session-turns-stddev "Link to this heading")

The standard deviation of the number of turns per session. (default: `0`)

### Tokenizer Options[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#tokenizer-options "Link to this heading")

#### `--tokenizer <str>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#tokenizer-str "Link to this heading")

The HuggingFace tokenizer to use to interpret token metrics from prompts and responses. The value can be the name of a tokenizer or the filepath of the tokenizer. The default value is the model name. (default: “<model_value>”)

#### `--tokenizer-revision <str>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#tokenizer-revision-str "Link to this heading")

The specific tokenizer model version to use. It can be a branch name, tag name, or commit ID. (default: `main`)

#### `--tokenizer-trust-remote-code`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#tokenizer-trust-remote-code "Link to this heading")

Allow custom tokenizer to be downloaded and executed. This carries security risks and should only be used for repositories you trust. This is only necessary for custom tokenizers stored in HuggingFace Hub. (default: `False`)

### Other Options[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#other-options "Link to this heading")

#### `-v`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#v "Link to this heading")

#### `--verbose`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#verbose "Link to this heading")

An option to enable verbose mode. (default: `False`)

#### `--version`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#version "Link to this heading")

An option to print the version and exit.

#### `-g <list>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#g-list "Link to this heading")

#### `--goodput <list>`[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#goodput-list "Link to this heading")

An option to provide constraints in order to compute goodput. Specify goodput constraints as ‘key:value’ pairs, where the key is a valid metric name, and the value is a number representing either milliseconds or a throughput value per second. For example, ‘request_latency:300’ or ‘output_token_throughput_per_user:600’. Multiple key:value pairs can be provided, separated by spaces. (default: `None`)

Known Issues[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#known-issues "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   GenAI-Perf can be slow to finish if a high request-rate is provided

*   Token counts may not be exact

[previous GenAI Performance Analyzer](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_benchmark/genai_perf.html "previous page")[next Profile Large Language Models with GenAI-Perf](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/docs/tutorial.html "next page")

 On this page 

*   [Installation](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#installation)
    *   [Install GenAI-Perf (Ubuntu 24.04, Python 3.10+)](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#install-genai-perf-ubuntu-24-04-python-3-10)

*   [Quick Start](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#quick-start)
    *   [Serve GPT-2 TensorRT-LLM model using Triton CLI](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#serve-gpt-2-tensorrt-llm-model-using-triton-cli)
    *   [Running GenAI-Perf](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#running-genai-perf)

*   [Configuration File](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#configuration-file)
    *   [Creating a Template Config File](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#creating-a-template-config-file)
    *   [Overriding Config Options](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#overriding-config-options)

*   [Analyze](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#analyze)
*   [Visualization](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#visualization)
*   [Process Export Files](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#process-export-files)
*   [Model Inputs](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#model-inputs)
    *   [Use moon_cake file as input payload](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#use-moon-cake-file-as-input-payload)
    *   [How to generate a payload file](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#how-to-generate-a-payload-file)
        *   [1. Synthetic data from sampling](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#synthetic-data-from-sampling)
        *   [2. Record real traffic and replay](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#record-real-traffic-and-replay)

*   [Authentication](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#authentication)
*   [Metrics](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#metrics)
    *   [GPU Telemetry](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#gpu-telemetry)
    *   [Power Metrics](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#power-metrics)
    *   [Memory Metrics](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#memory-metrics)
    *   [Temperature Metrics](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#temperature-metrics)
    *   [Clock Metrics](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#clock-metrics)
    *   [Utilization Metrics](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#utilization-metrics)
    *   [ECC Metrics](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#ecc-metrics)
    *   [Errors and Violations Metrics](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#errors-and-violations-metrics)
    *   [Retired Pages Metrics](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#retired-pages-metrics)
    *   [NVLink Error Metrics](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#nvlink-error-metrics)
    *   [PCIE Metrics](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#pcie-metrics)

*   [Command Line Options](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#command-line-options)
    *   [`-h`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#h)
    *   [`--help`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#help)
    *   [Config Options](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#config-options)
        *   [`-f`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#f)
        *   [`--file`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#file)
        *   [`--override-config`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#override-config)

    *   [Template Options](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#template-options)
        *   [`-f`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#id1)
        *   [`--file`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#id2)

    *   [Endpoint Options:](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#endpoint-options)
        *   [`-m <list>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#m-list)
        *   [`--model <list>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#model-list)
        *   [`--model-selection-strategy {round_robin, random}`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#model-selection-strategy-round-robin-random)
        *   [`--backend {tensorrtllm,vllm}`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#backend-tensorrtllm-vllm)
        *   [`--endpoint <str>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#endpoint-str)
        *   [`--endpoint-type <str>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#endpoint-type-str)
        *   [`--server-metrics-urls <list>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#server-metrics-urls-list)
        *   [`--streaming`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#streaming)
        *   [`-u <url>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#u-url)
        *   [`--url <url>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#url-url)
        *   [`--grpc-method <str>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#grpc-method-str)

    *   [Input Options](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#input-options)
        *   [`--audio-length-mean <int>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#audio-length-mean-int)
        *   [`--audio-length-stddev <int>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#audio-length-stddev-int)
        *   [`--audio-format <str>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#audio-format-str)
        *   [`--audio-depths <int>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#audio-depths-int)
        *   [`--audio-sample-rates <int>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#audio-sample-rates-int)
        *   [`--audio-num-channels <int>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#audio-num-channels-int)
        *   [`-b <int>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#b-int)
        *   [`--batch-size <int>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#batch-size-int)
        *   [`–batch-size-text](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#batch-size-text)
        *   [`–batch-size-text](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#id3)
        *   [`--batch-size-audio <int>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#batch-size-audio-int)
        *   [`--batch-size-text <int>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#batch-size-text-int)
        *   [`--batch-size-image <int>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#batch-size-image-int)
        *   [`--extra-inputs <str>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#extra-inputs-str)
        *   [`--header <str>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#header-str)
        *   [`--H <str>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#h-str)
        *   [`--input-file <path>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#input-file-path)
        *   [`--num-dataset-entries <int>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#num-dataset-entries-int)
        *   [`--num-prefix-prompts <int>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#num-prefix-prompts-int)
        *   [`--output-tokens-mean <int>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#output-tokens-mean-int)
        *   [`--osl`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#osl)
        *   [`--output-tokens-mean-deterministic`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#output-tokens-mean-deterministic)
        *   [`--output-tokens-stddev <int>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#output-tokens-stddev-int)
        *   [`--random-seed <int>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#random-seed-int)
        *   [`--request-count <int>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#request-count-int)
        *   [`--num-requests <int>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#num-requests-int)
        *   [`--synthetic-input-tokens-mean <int>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#synthetic-input-tokens-mean-int)
        *   [`--isl`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#isl)
        *   [`--synthetic-input-tokens-stddev <int>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#synthetic-input-tokens-stddev-int)
        *   [`--prefix-prompt-length <int>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#prefix-prompt-length-int)
        *   [`--image-width-mean <int>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#image-width-mean-int)
        *   [`--image-width-stddev <int>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#image-width-stddev-int)
        *   [`--image-height-mean <int>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#image-height-mean-int)
        *   [`--image-height-stddev <int>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#image-height-stddev-int)
        *   [`--image-format <str>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#image-format-str)
        *   [`--warmup-request-count <int>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#warmup-request-count-int)
        *   [`--num-warmup-requests <int>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#num-warmup-requests-int)

    *   [Profiling Options](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#profiling-options)
        *   [`--concurrency <int>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#concurrency-int)
        *   [`--measurement-interval <int>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#measurement-interval-int)
        *   [`-p <int>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#p-int)
        *   [`--request-rate <float>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#request-rate-float)
        *   [`--fixed-schedule`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#fixed-schedule)
        *   [`-s <float>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#s-float)
        *   [`--stability-percentage <float>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#stability-percentage-float)

    *   [Output Options](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#output-options)
        *   [`--artifact-dir`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#artifact-dir)
        *   [`--checkpoint-dir`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#checkpoint-dir)
        *   [`--generate-plots`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#generate-plots)
        *   [`--enable-checkpointing`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#enable-checkpointing)
        *   [`--profile-export-file <path>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#profile-export-file-path)

    *   [Session Options](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#session-options)
        *   [`--num-sessions`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#num-sessions)
        *   [`--session-concurrency <int>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#session-concurrency-int)
        *   [`--session-delay-ratio <float>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#session-delay-ratio-float)
        *   [`--session-turn-delay-mean`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#session-turn-delay-mean)
        *   [`--session-turn-delay-stddev`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#session-turn-delay-stddev)
        *   [`--session-turns-mean`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#session-turns-mean)
        *   [`--session-turns-stddev`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#session-turns-stddev)

    *   [Tokenizer Options](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#tokenizer-options)
        *   [`--tokenizer <str>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#tokenizer-str)
        *   [`--tokenizer-revision <str>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#tokenizer-revision-str)
        *   [`--tokenizer-trust-remote-code`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#tokenizer-trust-remote-code)

    *   [Other Options](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#other-options)
        *   [`-v`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#v)
        *   [`--verbose`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#verbose)
        *   [`--version`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#version)
        *   [`-g <list>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#g-list)
        *   [`--goodput <list>`](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#goodput-list)

*   [Known Issues](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html#known-issues)

[![Image 3: NVIDIA](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_static/nvidia-logo-horiz-rgb-1c-blk-for-screen.svg)![Image 4: NVIDIA](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_static/nvidia-logo-horiz-rgb-1c-wht-for-screen.svg)](https://www.nvidia.com/)

[Privacy Policy](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/) | [Your Privacy Choices](https://www.nvidia.com/en-us/about-nvidia/privacy-center/) | [Terms of Service](https://www.nvidia.com/en-us/about-nvidia/terms-of-service/) | [Accessibility](https://www.nvidia.com/en-us/about-nvidia/accessibility/) | [Corporate Policies](https://www.nvidia.com/en-us/about-nvidia/company-policies/) | [Product Security](https://www.nvidia.com/en-us/product-security/) | [Contact](https://www.nvidia.com/en-us/contact/)

Copyright © 2018-2026, NVIDIA Corporation.
