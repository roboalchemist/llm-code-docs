# Source: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html

Title: Speculative Decoding with TensorRT-LLM — NVIDIA Triton Inference Server

URL Source: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html

Published Time: Sat, 28 Feb 2026 00:57:37 GMT

Markdown Content:
Speculative Decoding with TensorRT-LLM — NVIDIA Triton Inference Server
===============

[Skip to main content](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#main-content)

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
    *   [TRT-LLM](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#)
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
*   [Speculative Decoding](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/llm_features/speculative_decoding.html)
*   Speculative...

Speculative Decoding with TensorRT-LLM[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#speculative-decoding-with-tensorrt-llm "Link to this heading")
======================================================================================================================================================================================================================================================

*   [About Speculative Decoding](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#about-speculative-decoding)

*   [EAGLE](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#eagle)

*   [MEDUSA](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#medusa)

*   [Draft Model-Based Speculative Decoding](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#draft-model-based-speculative-decoding)

About Speculative Decoding[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#about-speculative-decoding "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This tutorial shows how to build and serve speculative decoding models in Triton Inference Server with [TensorRT-LLM Backend](https://github.com/triton-inference-server/tensorrtllm_backend) on a single node with one GPU. Please go to [Speculative Decoding](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/README.html) main page to learn more about other supported backends.

According to [Spec-Bench](https://sites.google.com/view/spec-bench), EAGLE is currently the top-performing approach for speeding up LLM inference across different tasks. In this tutorial, we’ll focus on [EAGLE](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#eagle) and demonstrate how to make it work with Triton Inference Server. However, we’ll also cover [MEDUSA](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#medusa) and [Draft Model-Based Speculative Decoding](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#draft-model-based-speculative-decoding) for those interested in exploring alternative methods. This way, you can choose the best fit for your needs.

EAGLE[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#eagle "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

EAGLE ([paper](https://arxiv.org/pdf/2401.15077) | [github](https://github.com/SafeAILab/EAGLE) | [blog](https://sites.google.com/view/eagle-llm)) is a speculative decoding technique that accelerates Large Language Model (LLM) inference by predicting future tokens based on contextual features extracted from the LLM’s second-top layer. It employs a lightweight Auto-regression Head to predict the next feature vector, which is then used to generate tokens through the LLM’s frozen classification head, achieving significant speedups (2x-3x faster than vanilla decoding) while maintaining output quality and distribution consistency. EAGLE-2, an improved version, further enhances performance by using confidence scores from the draft model to dynamically adjust the draft tree structure, resulting in even faster inference speeds.

_NOTE: EAGLE-2 is not supported via Triton Inference Server using TensorRT-LLM backend yet._

### Acquiring EAGLE Model and its Base Model[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#acquiring-eagle-model-and-its-base-model "Link to this heading")

In this example, we will be using the [EAGLE-Vicuna-7B-v1.3](https://huggingface.co/yuhuili/EAGLE-Vicuna-7B-v1.3) model. More types of EAGLE models can be found [here](https://huggingface.co/yuhuili). The base model [Vicuna-7B-v1.3](https://huggingface.co/lmsys/vicuna-7b-v1.3) is also needed for EAGLE to work.

To download both models, run the following command:

# Install git-lfs if needed
apt-get update && apt-get install git-lfs -y --no-install-recommends
git lfs install
git clone https://huggingface.co/lmsys/vicuna-7b-v1.3
git clone https://huggingface.co/yuhuili/EAGLE-Vicuna-7B-v1.3

### Launch Triton TensorRT-LLM container[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#launch-triton-tensorrt-llm-container "Link to this heading")

Launch Triton docker container with TensorRT-LLM backend. Note that we’re mounting the downloaded EAGLE and base models to `/hf-models` in the docker container. Make an `engines` folder outside docker to reuse engines for future runs. Please, make sure to replace <xx.yy> with the version of Triton that you want to use (must be >= 25.01). The latest Triton Server container is recommended and can be found [here](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/tritonserver/tags).

docker run --rm -it --net host --shm-size=2g \
 --ulimit memlock=-1 --ulimit stack=67108864 --gpus all \
 -v </path/to/eagle/and/base/model/>:/hf-models \
 -v </path/to/engines>:/engines \
 nvcr.io/nvidia/tritonserver:<xx.yy>-trtllm-python-py3

### Create Engines for Each Model [skip this step if you already have an engine][#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#create-engines-for-each-model-skip-this-step-if-you-already-have-an-engine "Link to this heading")

TensorRT-LLM requires each model to be compiled for the configuration you need before running. To do so, before you run your model for the first time on Triton Server you will need to create a TensorRT-LLM engine.

Starting with [24.04 release](https://github.com/triton-inference-server/server/releases/tag/v2.45.0), Triton Server TensrRT-LLM container comes with pre-installed TensorRT-LLM package, which allows users to build engines inside the Triton container. Simply follow the next steps in the container:

BASE_MODEL=/hf-models/vicuna-7b-v1.3
EAGLE_MODEL=/hf-models/EAGLE-Vicuna-7B-v1.3
CKPT_PATH=/tmp/ckpt/vicuna/7b/
ENGINE_DIR=/engines/eagle-vicuna-7b/1-gpu/
CONVERT_CHKPT_SCRIPT=/app/examples/eagle/convert_checkpoint.py
python3 ${CONVERT_CHKPT_SCRIPT} --model_dir ${BASE_MODEL} \
 --eagle_model_dir ${EAGLE_MODEL} \
 --output_dir ${CKPT_PATH} \
 --dtype float16 \
 --max_draft_len 63 \
 --num_eagle_layers 4 \
 --max_non_leaves_per_layer 10
trtllm-build --checkpoint_dir ${CKPT_PATH} \
 --output_dir ${ENGINE_DIR} \
 --gemm_plugin float16 \
 --use_paged_context_fmha enable \
 --speculative_decoding_mode eagle \
 --max_batch_size 4

To verify that the engine is built correctly, run the following command:

python3 /app/examples/run.py --engine_dir ${ENGINE_DIR} \
 --tokenizer_dir ${BASE_MODEL} \
 --max_output_len=100 \
 --input_text "Once upon"

Sample output:

> Input [Text 0]: "<s> Once upon"
> Output [Text 0 Beam 0]: "a time, there was a young girl who loved to read. She would spend hours in the library, devouring books of all genres. She had a special love for fairy tales, and would often dream of living in a magical world where she could meet princes and princesses, and have adventures with talking animals.
> One day, while she was reading a book, she came across a passage that spoke to her heart. It said, "You are the author of"
> [TensorRT-LLM][INFO] Refreshed the MPI local session

### Serving with Triton[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#serving-with-triton "Link to this heading")

The last step is to create a Triton readable model and serve it. You can find a template of a model that uses inflight batching in [tensorrtllm_backend/all_models/inflight_batcher_llm](https://github.com/NVIDIA/TensorRT-LLM/tree/main/triton_backend/all_models/inflight_batcher_llm). To run EAGLE model, you will need to:

1.   Copy over the inflight batcher models repository

cp -R /app/all_models/inflight_batcher_llm /opt/tritonserver/.

1.   Modify config.pbtxt for the preprocessing, postprocessing and processing steps.

TOKENIZER_DIR=/hf-models/vicuna-7b-v1.3
TOKENIZER_TYPE=auto
ENGINE_DIR=/engines/eagle-vicuna-7b/1-gpu/
DECOUPLED_MODE=false
MODEL_FOLDER=/opt/tritonserver/inflight_batcher_llm
MAX_BATCH_SIZE=4
INSTANCE_COUNT=1
MAX_QUEUE_DELAY_MS=10000
TRITON_BACKEND=tensorrtllm
LOGITS_DATATYPE="TYPE_FP32"
FILL_TEMPLATE_SCRIPT=/app/tools/fill_template.py
python3 ${FILL_TEMPLATE_SCRIPT} -i ${MODEL_FOLDER}/preprocessing/config.pbtxt tokenizer_dir:${TOKENIZER_DIR},tokenizer_type:${TOKENIZER_TYPE},triton_max_batch_size:${MAX_BATCH_SIZE},preprocessing_instance_count:${INSTANCE_COUNT}
python3 ${FILL_TEMPLATE_SCRIPT} -i ${MODEL_FOLDER}/postprocessing/config.pbtxt tokenizer_dir:${TOKENIZER_DIR},tokenizer_type:${TOKENIZER_TYPE},triton_max_batch_size:${MAX_BATCH_SIZE},postprocessing_instance_count:${INSTANCE_COUNT}
python3 ${FILL_TEMPLATE_SCRIPT} -i ${MODEL_FOLDER}/tensorrt_llm_bls/config.pbtxt triton_max_batch_size:${MAX_BATCH_SIZE},decoupled_mode:${DECOUPLED_MODE},bls_instance_count:${INSTANCE_COUNT},logits_datatype:${LOGITS_DATATYPE}
python3 ${FILL_TEMPLATE_SCRIPT} -i ${MODEL_FOLDER}/ensemble/config.pbtxt triton_max_batch_size:${MAX_BATCH_SIZE},logits_datatype:${LOGITS_DATATYPE}
python3 ${FILL_TEMPLATE_SCRIPT} -i ${MODEL_FOLDER}/tensorrt_llm/config.pbtxt triton_backend:${TRITON_BACKEND},triton_max_batch_size:${MAX_BATCH_SIZE},decoupled_mode:${DECOUPLED_MODE},engine_dir:${ENGINE_DIR},max_queue_delay_microseconds:${MAX_QUEUE_DELAY_MS},batching_strategy:inflight_fused_batching,encoder_input_features_data_type:TYPE_FP16,logits_datatype:${LOGITS_DATATYPE}

_NOTE: you can specify `eagle\_choices` by manually changing tensorrt\_llm/config.pbtxt. If you do not specify any choices, the default, [mc\_sim\_7b\_63](https://github.com/FasterDecoding/Medusa/blob/main/medusa/model/medusa\_choices.py#L1) choices are used. For more information regarding choices tree, refer to [Medusa Tree](https://nvidia.github.io/TensorRT-LLM/advanced/speculative-decoding.html#medusa-tree)._

1.   Launch Tritonserver

Launch Tritonserver with the [launch_triton_server.py](https://github.com/triton-inference-server/tensorrtllm_backend/blob/release/0.5.0/scripts/launch_triton_server.py) script. Here, we launch a single instance of `tritonserver` with MPI by setting `--world_size=1`.

python3 /app/scripts/launch_triton_server.py --world_size=1 --model_repo=/opt/tritonserver/inflight_batcher_llm

> You should expect the following response:
> 
> 
> 
> ...
> I0503 22:01:25.210518 1175 grpc_server.cc:2463] Started GRPCInferenceService at 0.0.0.0:8001
> I0503 22:01:25.211612 1175 http_server.cc:4692] Started HTTPService at 0.0.0.0:8000
> I0503 22:01:25.254914 1175 http_server.cc:362] Started Metrics Service at 0.0.0.0:8002

To stop Triton Server inside the container, run:

pkill tritonserver

_NOTE: do not forget to run above command to stop Triton Server if launch Tritionserver failed due to various reasons. Otherwise, it could cause OOM or MPI issues._

### Send Inference Requests[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#send-inference-requests "Link to this heading")

You can test the results of the run with:

1.   The [inflight_batcher_llm_client.py](https://github.com/NVIDIA/TensorRT-LLM/blob/main/triton_backend/inflight_batcher_llm/client/inflight_batcher_llm_client.py) script. Run below in another terminal:

# Using the SDK container as an example. <xx.yy> is the version of Triton Server you are using.
docker run --rm -it --net host --shm-size=2g \
 --ulimit memlock=-1 --ulimit stack=67108864 --gpus all \
 -v </path/to/eagle/and/base/model/>:/hf-models \
 nvcr.io/nvidia/tritonserver:<xx.yy>-py3-sdk
# Install extra dependencies for the script
pip3 install transformers sentencepiece
python3 /tensorrtllm_client/inflight_batcher_llm_client.py --request-output-len 50 --tokenizer-dir /hf-models/vicuna-7b-v1.3 --text "What is ML?"

> You should expect the following response:
> 
> 
> 
> ...
> Input: What is ML?
> Output beam 0:
> ML is a branch of AI that allows computers to learn from data, identify patterns, and make predictions. It is a powerful tool that can be used in a variety of industries, including healthcare, finance, and transportation.
> ...

1.   The [generate endpoint](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/protocol/extension_generate.html).

curl -X POST localhost:8000/v2/models/ensemble/generate -d '{"text_input": "What is ML?", "max_tokens": 50, "bad_words": "", "stop_words": "", "pad_id": 2, "end_id": 2}'

> You should expect the following response:
> 
> 
> 
> {"model_name":"ensemble","model_version":"1","sequence_end":false,"sequence_id":0,"sequence_start":false,"text_output":"What is ML?\nML is a branch of AI that allows computers to learn from data, identify patterns, and make predictions. It is a powerful tool that can be used in a variety of industries, including healthcare, finance, and transportation."}

### Evaluating Performance with Gen-AI Perf[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#evaluating-performance-with-gen-ai-perf "Link to this heading")

Gen-AI Perf is a command line tool for measuring the throughput and latency of generative AI models as served through an inference server. You can read more about Gen-AI Perf [here](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html). We will use Gen-AI Perf to evaluate the performance gain of EAGLE model over the base model.

_NOTE: below experiment is done on a single node with one GPU - RTX 5880 (48GB GPU memory). The number below is only for reference. The actual number may vary due to the different hardware and environment._

1.   Prepare Dataset

We will be using the HumanEval dataset for our evaluation, which is used in the original EAGLE paper. The HumanEval dataset has been converted to the format required by EAGLE and is available [here](https://github.com/SafeAILab/EAGLE/blob/main/eagle/data/humaneval/question.jsonl). To make it compatible for Gen-AI Perf, we need to do another conversion. You may use other datasets besides HumanEval as well, as long as it could be converted to the format required by Gen-AI Perf. Note that MT-bench could not be used since Gen-AI Perf does not support multiturn dataset as input yet. Follow the steps below to download and convert the dataset.

wget https://raw.githubusercontent.com/SafeAILab/EAGLE/main/eagle/data/humaneval/question.jsonl

# dataset-converter.py file can be found in the parent folder of this README.
python3 dataset-converter.py --input_file question.jsonl --output_file converted_humaneval.jsonl

1.   Install GenAI-Perf (Ubuntu 24.04, Python 3.10+)

pip install genai-perf

_NOTE: you must already have CUDA 12 installed._

1.   Run Gen-AI Perf

Run the following command in the SDK container:

genai-perf \
 profile \
 -m ensemble \
 --service-kind triton \
 --backend tensorrtllm \
 --input-file /path/to/converted/dataset/converted_humaneval.jsonl \
 --tokenizer /path/to/hf-models/vicuna-7b-v1.3/ \
 --profile-export-file my_profile_export.json \
 --url localhost:8001 \
 --concurrency 1

_NOTE: When benchmarking the speedup of speculative decoding versus the base model, use `--concurrency 1`. This setting is crucial because speculative decoding is designed to trade extra computation for reduced token generation latency. By limiting concurrency, we avoid saturating hardware resources with multiple requests, allowing for a more accurate assessment of the technique’s latency benefits. This approach ensures that the benchmark reflects the true performance gains of speculative decoding in real-world, low-concurrency scenarios._

A sample output that looks like this:

                                   NVIDIA GenAI-Perf | LLM Metrics
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┓
┃                         Statistic ┃      avg ┃    min ┃      max ┃      p99 ┃      p90 ┃      p75 ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━┩
│              Request Latency (ms) │ 1,355.35 │ 387.84 │ 2,002.81 │ 2,000.44 │ 1,868.83 │ 1,756.85 │
│   Output Sequence Length (tokens) │   348.27 │ 153.00 │   534.00 │   517.25 │   444.50 │   426.75 │
│    Input Sequence Length (tokens) │   156.54 │  63.00 │   278.00 │   265.75 │   203.00 │   185.75 │
│ Output Token Throughput (per sec) │   256.94 │    N/A │      N/A │      N/A │      N/A │      N/A │
│      Request Throughput (per sec) │     0.74 │    N/A │      N/A │      N/A │      N/A │      N/A │
│             Request Count (count) │    26.00 │    N/A │      N/A │      N/A │      N/A │      N/A │
└───────────────────────────────────┴──────────┴────────┴──────────┴──────────┴──────────┴──────────┘

1.   Run Gen-AI Perf on Base Model

To compare performance between EAGLE and base model (i.e. vanilla LLM w/o speculative decoding), we need to run Gen-AI Perf Tool on the base model as well. To do so, we need to repeat the steps above for the base model with minor changes.

Kill the existing Triton Server and run the following command in the Triton Server container:

pkill tritonserver

Build the TRT-LLM engine for the base model:

BASE_MODEL=/hf-models/vicuna-7b-v1.3
CKPT_PATH=/tmp/ckpt/vicuna-base/7b/
ENGINE_DIR=/engines/vicuna-7b/1-gpu/
CONVERT_CHKPT_SCRIPT=/app/examples/llama/convert_checkpoint.py
python3 ${CONVERT_CHKPT_SCRIPT} --model_dir ${BASE_MODEL} \
 --output_dir ${CKPT_PATH} \
 --dtype float16
trtllm-build --checkpoint_dir ${CKPT_PATH} \
 --output_dir ${ENGINE_DIR} \
 --remove_input_padding enable \
 --gpt_attention_plugin float16 \
 --context_fmha enable \
 --gemm_plugin float16 \
 --paged_kv_cache enable \
 --max_batch_size 4

Create a Triton readable model for the base model:

mkdir -p /opt/tritonserver/vicuna_base
cp -R /app/all_models/inflight_batcher_llm /opt/tritonserver/vicuna_base/.

TOKENIZER_DIR=/hf-models/vicuna-7b-v1.3
TOKENIZER_TYPE=auto
ENGINE_DIR=/engines/vicuna-7b/1-gpu/
DECOUPLED_MODE=false
MODEL_FOLDER=/opt/tritonserver/vicuna_base/inflight_batcher_llm
MAX_BATCH_SIZE=4
INSTANCE_COUNT=1
MAX_QUEUE_DELAY_MS=10000
TRITON_BACKEND=tensorrtllm
LOGITS_DATATYPE="TYPE_FP32"
FILL_TEMPLATE_SCRIPT=/app/tools/fill_template.py
python3 ${FILL_TEMPLATE_SCRIPT} -i ${MODEL_FOLDER}/preprocessing/config.pbtxt tokenizer_dir:${TOKENIZER_DIR},tokenizer_type:${TOKENIZER_TYPE},triton_max_batch_size:${MAX_BATCH_SIZE},preprocessing_instance_count:${INSTANCE_COUNT}
python3 ${FILL_TEMPLATE_SCRIPT} -i ${MODEL_FOLDER}/postprocessing/config.pbtxt tokenizer_dir:${TOKENIZER_DIR},tokenizer_type:${TOKENIZER_TYPE},triton_max_batch_size:${MAX_BATCH_SIZE},postprocessing_instance_count:${INSTANCE_COUNT}
python3 ${FILL_TEMPLATE_SCRIPT} -i ${MODEL_FOLDER}/tensorrt_llm_bls/config.pbtxt triton_max_batch_size:${MAX_BATCH_SIZE},decoupled_mode:${DECOUPLED_MODE},bls_instance_count:${INSTANCE_COUNT},logits_datatype:${LOGITS_DATATYPE}
python3 ${FILL_TEMPLATE_SCRIPT} -i ${MODEL_FOLDER}/ensemble/config.pbtxt triton_max_batch_size:${MAX_BATCH_SIZE},logits_datatype:${LOGITS_DATATYPE}
python3 ${FILL_TEMPLATE_SCRIPT} -i ${MODEL_FOLDER}/tensorrt_llm/config.pbtxt triton_backend:${TRITON_BACKEND},triton_max_batch_size:${MAX_BATCH_SIZE},decoupled_mode:${DECOUPLED_MODE},engine_dir:${ENGINE_DIR},max_queue_delay_microseconds:${MAX_QUEUE_DELAY_MS},batching_strategy:inflight_fused_batching,encoder_input_features_data_type:TYPE_FP16,logits_datatype:${LOGITS_DATATYPE}

Launch Triton Server with the base model:

python3 /app/scripts/launch_triton_server.py --world_size=1 --model_repo=/opt/tritonserver/vicuna_base/inflight_batcher_llm

Run Gen-AI Perf Tool on Base Model:

genai-perf \
 profile \
 -m ensemble \
 --service-kind triton \
 --backend tensorrtllm \
 --input-file /path/to/converted/dataset/converted_humaneval.jsonl \
 --tokenizer /path/to/hf-models/vicuna-7b-v1.3/ \
 --profile-export-file my_profile_export.json \
 --url localhost:8001 \
 --concurrency 1

Sample performance output for base model:

                                    NVIDIA GenAI-Perf | LLM Metrics
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┓
┃                         Statistic ┃      avg ┃      min ┃      max ┃      p99 ┃      p90 ┃      p75 ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━┩
│              Request Latency (ms) │ 2,663.13 │ 1,017.15 │ 4,197.72 │ 4,186.59 │ 4,096.25 │ 4,090.93 │
│   Output Sequence Length (tokens) │   310.75 │   153.00 │   441.00 │   440.12 │   431.70 │   415.50 │
│    Input Sequence Length (tokens) │   145.67 │    63.00 │   195.00 │   194.12 │   186.90 │   185.25 │
│ Output Token Throughput (per sec) │   116.68 │      N/A │      N/A │      N/A │      N/A │      N/A │
│      Request Throughput (per sec) │     0.38 │      N/A │      N/A │      N/A │      N/A │      N/A │
│             Request Count (count) │    12.00 │      N/A │      N/A │      N/A │      N/A │      N/A │
└───────────────────────────────────┴──────────┴──────────┴──────────┴──────────┴──────────┴──────────┘

1.   Compare Performance

From the sample runs above, we can see that the EAGLE model has a lower latency and higher throughput than the base model. Specifically, the EAGLE model can generate 256.94 tokens per second, while the base model can only generate 116.68 tokens per second with a speed up of 2.2x.

As stated above, the number above is gathered from a single node with one GPU - RTX 5880 (48GB GPU memory). The actual number may vary due to the different hardware and environment.

Medusa[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#medusa "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

MEDUSA ([paper](https://arxiv.org/pdf/2401.10774) | [github](https://github.com/FasterDecoding/Medusa) | [blog](https://sites.google.com/view/medusa-llm)) is a speculative decoding framework that, like EAGLE, aims to accelerate LLM inference. However, there are several key differences between the two approaches:

*   Architecture: MEDUSA adds extra decoding heads to LLMs to predict multiple subsequent tokens in parallel, while EAGLE extrapolates second-top-layer contextual feature vectors of LLMs.

*   Generation structure: MEDUSA generates a fully connected tree across adjacent layers through the Cartesian product, often resulting in nonsensical combinations. In contrast, EAGLE creates a sparser, more selective tree structure that is more context-aware1.

*   Consistency: MEDUSA’s non-greedy generation does not guarantee lossless performance, while EAGLE provably maintains consistency with vanilla decoding in the distribution of generated texts.

*   Accuracy: MEDUSA achieves an accuracy of about 0.6 in generating drafts, whereas EAGLE attains a higher accuracy of approximately 0.8 as claimed in the EAGLE paper.

*   Speed: EAGLE is reported to be 1.6x faster than MEDUSA for certained models as claimed in the EAGLE paper.

To run MEDUSA with Triton Inference Server, it is very similar to the steps above for EAGLE with only a few simple configuration changes. We only list the changes below. The rest steps not listed below are the same as the steps for EAGLE above, e.g. launch docker, launch triton server, send requests, evalaution.

### Download the MEDUSA model[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#download-the-medusa-model "Link to this heading")

We will be using [medusa-vicuna-7b-v1.3](https://huggingface.co/FasterDecoding/medusa-vicuna-7b-v1.3), same model family as what we used for EAGLE above:

git clone https://huggingface.co/FasterDecoding/medusa-vicuna-7b-v1.3

### Build the TRT-LLM engine for MEDUSA:[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#build-the-trt-llm-engine-for-medusa "Link to this heading")

BASE_MODEL=/hf-models/vicuna-7b-v1.3
MEDUSA_MODEL=/hf-models/medusa-vicuna-7b-v1.3
CKPT_PATH=/tmp/ckpt/vicuna-medusa/7b/
ENGINE_DIR=/engines/medusa-vicuna-7b/1-gpu/
CONVERT_CHKPT_SCRIPT=/app/examples/medusa/convert_checkpoint.py
python3 ${CONVERT_CHKPT_SCRIPT} --model_dir ${BASE_MODEL} \
 --medusa_model_dir ${MEDUSA_MODEL} \
 --output_dir ${CKPT_PATH} \
 --dtype float16 \
 --num_medusa_heads 4
trtllm-build --checkpoint_dir ${CKPT_PATH} \
 --output_dir ${ENGINE_DIR} \
 --gemm_plugin float16 \
 --speculative_decoding_mode medusa \
 --max_batch_size 4

### Create a Triton readable model for MEDUSA:[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#create-a-triton-readable-model-for-medusa "Link to this heading")

mkdir -p /opt/tritonserver/vicuna_medusa
cp -R /app/all_models/inflight_batcher_llm /opt/tritonserver/vicuna_medusa/.

TOKENIZER_DIR=/hf-models/vicuna-7b-v1.3
TOKENIZER_TYPE=auto
ENGINE_DIR=/engines/medusa-vicuna-7b/1-gpu/
DECOUPLED_MODE=false
MODEL_FOLDER=/opt/tritonserver/vicuna_medusa/inflight_batcher_llm
MAX_BATCH_SIZE=4
INSTANCE_COUNT=1
MAX_QUEUE_DELAY_MS=10000
TRITON_BACKEND=tensorrtllm
LOGITS_DATATYPE="TYPE_FP32"
FILL_TEMPLATE_SCRIPT=/app/tools/fill_template.py
python3 ${FILL_TEMPLATE_SCRIPT} -i ${MODEL_FOLDER}/preprocessing/config.pbtxt tokenizer_dir:${TOKENIZER_DIR},tokenizer_type:${TOKENIZER_TYPE},triton_max_batch_size:${MAX_BATCH_SIZE},preprocessing_instance_count:${INSTANCE_COUNT}
python3 ${FILL_TEMPLATE_SCRIPT} -i ${MODEL_FOLDER}/postprocessing/config.pbtxt tokenizer_dir:${TOKENIZER_DIR},tokenizer_type:${TOKENIZER_TYPE},triton_max_batch_size:${MAX_BATCH_SIZE},postprocessing_instance_count:${INSTANCE_COUNT}
python3 ${FILL_TEMPLATE_SCRIPT} -i ${MODEL_FOLDER}/tensorrt_llm_bls/config.pbtxt triton_max_batch_size:${MAX_BATCH_SIZE},decoupled_mode:${DECOUPLED_MODE},bls_instance_count:${INSTANCE_COUNT},logits_datatype:${LOGITS_DATATYPE}
python3 ${FILL_TEMPLATE_SCRIPT} -i ${MODEL_FOLDER}/ensemble/config.pbtxt triton_max_batch_size:${MAX_BATCH_SIZE},logits_datatype:${LOGITS_DATATYPE}
python3 ${FILL_TEMPLATE_SCRIPT} -i ${MODEL_FOLDER}/tensorrt_llm/config.pbtxt triton_backend:${TRITON_BACKEND},triton_max_batch_size:${MAX_BATCH_SIZE},decoupled_mode:${DECOUPLED_MODE},engine_dir:${ENGINE_DIR},max_queue_delay_microseconds:${MAX_QUEUE_DELAY_MS},batching_strategy:inflight_fused_batching,encoder_input_features_data_type:TYPE_FP16,logits_datatype:${LOGITS_DATATYPE}

Draft Model-Based Speculative Decoding[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#draft-model-based-speculative-decoding "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Draft Model-Based Speculative Decoding ([paper](https://arxiv.org/pdf/2302.01318)) is another (and earlier) approach to accelerate LLM inference, distinct from both EAGLE and MEDUSA. Here are the key differences:

*   Draft Generation: it uses a smaller, faster LLM as a draft model to predict multiple tokens ahead. This contrasts with EAGLE’s feature-level extrapolation and MEDUSA’s additional decoding heads.

*   Verification Process: it employs a chain-like structure for draft generation and verification, unlike EAGLE and MEDUSA which use tree-based attention mechanisms.

*   Consistency: it maintains distribution consistency with the target LLM in both greedy and non-greedy settings, similar to EAGLE but different from MEDUSA.

*   Efficiency: While effective, it is generally slower than both EAGLE and MEDUSA.

*   Implementation: it requires a separate draft model, which can be challenging to implement effectively for smaller target models. EAGLE and MEDUSA, in contrast, modify the existing model architecture.

*   Accuracy: its draft accuracy can vary depending on the draft model used, while EAGLE achieves a higher draft accuracy (about 0.8) compared to MEDUSA (about 0.6).

Please follow the steps [here](https://github.com/NVIDIA/TensorRT-LLM/blob/main/docs/source/legacy/advanced/speculative-decoding.md#draft-target-model) to run Draft Model-Based Speculative Decoding with Triton Inference Server.

[previous Speculative Decoding](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/README.html "previous page")[next Speculative Decoding with vLLM](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/vLLM/README.html "next page")

 On this page 

*   [About Speculative Decoding](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#about-speculative-decoding)
*   [EAGLE](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#eagle)
    *   [Acquiring EAGLE Model and its Base Model](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#acquiring-eagle-model-and-its-base-model)
    *   [Launch Triton TensorRT-LLM container](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#launch-triton-tensorrt-llm-container)
    *   [Create Engines for Each Model [skip this step if you already have an engine]](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#create-engines-for-each-model-skip-this-step-if-you-already-have-an-engine)
    *   [Serving with Triton](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#serving-with-triton)
    *   [Send Inference Requests](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#send-inference-requests)
    *   [Evaluating Performance with Gen-AI Perf](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#evaluating-performance-with-gen-ai-perf)

*   [Medusa](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#medusa)
    *   [Download the MEDUSA model](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#download-the-medusa-model)
    *   [Build the TRT-LLM engine for MEDUSA:](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#build-the-trt-llm-engine-for-medusa)
    *   [Create a Triton readable model for MEDUSA:](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#create-a-triton-readable-model-for-medusa)

*   [Draft Model-Based Speculative Decoding](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Speculative_Decoding/TRT-LLM/README.html#draft-model-based-speculative-decoding)

[![Image 3: NVIDIA](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_static/nvidia-logo-horiz-rgb-1c-blk-for-screen.svg)![Image 4: NVIDIA](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_static/nvidia-logo-horiz-rgb-1c-wht-for-screen.svg)](https://www.nvidia.com/)

[Privacy Policy](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/) | [Your Privacy Choices](https://www.nvidia.com/en-us/about-nvidia/privacy-center/) | [Terms of Service](https://www.nvidia.com/en-us/about-nvidia/terms-of-service/) | [Accessibility](https://www.nvidia.com/en-us/about-nvidia/accessibility/) | [Corporate Policies](https://www.nvidia.com/en-us/about-nvidia/company-policies/) | [Product Security](https://www.nvidia.com/en-us/product-security/) | [Contact](https://www.nvidia.com/en-us/contact/)

Copyright © 2018-2026, NVIDIA Corporation.
