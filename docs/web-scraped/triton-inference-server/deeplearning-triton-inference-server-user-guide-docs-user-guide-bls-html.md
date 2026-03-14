# Source: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/bls.html

Title: Business Logic Scripting — NVIDIA Triton Inference Server

URL Source: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/bls.html

Published Time: Sat, 28 Feb 2026 01:07:43 GMT

Markdown Content:
Business Logic Scripting — NVIDIA Triton Inference Server
===============

[Skip to main content](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/bls.html#main-content)

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
    *   [Business Logic Scripting](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/bls.html#)

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
*   [Model Pipelines](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/server_guide/model_pipelines.html)
*   Business...

Business Logic Scripting[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/bls.html#business-logic-scripting "Link to this heading")
=============================================================================================================================================================================

Triton’s [ensemble](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/ensemble_models.html#ensemble-models) feature supports many use cases where multiple models are composed into a pipeline (or more generally a DAG, directed acyclic graph). However, there are many other use cases that are not supported because as part of the model pipeline they require loops, conditionals (if-then-else), data-dependent control-flow and other custom logic to be intermixed with model execution. We call this combination of custom logic and model executions _Business Logic Scripting (BLS)_.

Starting from 21.08, you can implement BLS in your Python model. A new set of utility functions allows you to execute inference requests on other models being served by Triton as a part of executing your Python model. Note that BLS should only be used inside the `execute` function and is not supported in the `initialize` or `finalize` methods. Example below shows how to use this feature:

import triton_python_backend_utils as pb_utils

class TritonPythonModel:
  ...
    def execute(self, requests):
      ...
      # Create an InferenceRequest object. `model_name`,
      # `requested_output_names`, and `inputs` are the required arguments and
      # must be provided when constructing an InferenceRequest object. Make
      # sure to replace `inputs` argument with a list of `pb_utils.Tensor`
      # objects.
      inference_request = pb_utils.InferenceRequest(
          model_name='model_name',
          requested_output_names=['REQUESTED_OUTPUT_1', 'REQUESTED_OUTPUT_2'],
          inputs=[<pb_utils.Tensor object>])

      # `pb_utils.InferenceRequest` supports request_id, correlation_id,
      # model version, timeout and preferred_memory in addition to the
      # arguments described above.
      # Note: Starting from the 24.03 release, the `correlation_id` parameter
      # supports both string and unsigned integer values.
      # These arguments are optional. An example containing all the arguments:
      # inference_request = pb_utils.InferenceRequest(model_name='model_name',
      # requested_output_names=['REQUESTED_OUTPUT_1', 'REQUESTED_OUTPUT_2'],
      # inputs=[<list of pb_utils.Tensor objects>],
      # request_id="1", correlation_id=4, model_version=1, flags=0, timeout=5,
      # preferred_memory=pb_utils.PreferredMemory(
      # pb_utils.TRITONSERVER_MEMORY_GPU, # or pb_utils.TRITONSERVER_MEMORY_CPU
      # 0))

      # Execute the inference_request and wait for the response
      inference_response = inference_request.exec()

      # Check if the inference response has an error
      if inference_response.has_error():
          raise pb_utils.TritonModelException(
            inference_response.error().message())
      else:
          # Extract the output tensors from the inference response.
          output1 = pb_utils.get_output_tensor_by_name(
            inference_response, 'REQUESTED_OUTPUT_1')
          output2 = pb_utils.get_output_tensor_by_name(
            inference_response, 'REQUESTED_OUTPUT_2')

          # Decide the next steps for model execution based on the received
          # output tensors. It is possible to use the same output tensors
          # to for the final inference response too.

In addition to the `inference_request.exec` function that allows you to execute blocking inference requests, `inference_request.async_exec` allows you to perform async inference requests. This can be useful when you do not need the result of the inference immediately. Using `async_exec` function, it is possible to have multiple inflight inference requests and wait for the responses only when needed. Example below shows how to use `async_exec`:

import triton_python_backend_utils as pb_utils
import asyncio

class TritonPythonModel:
  ...

    # You must add the Python 'async' keyword to the beginning of `execute`
    # function if you want to use `async_exec` function.
    async def execute(self, requests):
      ...
      # Create an InferenceRequest object. `model_name`,
      # `requested_output_names`, and `inputs` are the required arguments and
      # must be provided when constructing an InferenceRequest object. Make
      # sure to replace `inputs` argument with a list of `pb_utils.Tensor`
      # objects.
      inference_request = pb_utils.InferenceRequest(
          model_name='model_name',
          requested_output_names=['REQUESTED_OUTPUT_1', 'REQUESTED_OUTPUT_2'],
          inputs=[<pb_utils.Tensor object>])

      infer_response_awaits = []
      for i in range(4):
        # async_exec function returns an
        # [Awaitable](https://docs.python.org/3/library/asyncio-task.html#awaitables)
        # object.
        infer_response_awaits.append(inference_request.async_exec())

      # Wait for all of the inference requests to complete.
      infer_responses = await asyncio.gather(*infer_response_awaits)

      for infer_response in infer_responses:
        # Check if the inference response has an error
        if inference_response.has_error():
            raise pb_utils.TritonModelException(
              inference_response.error().message())
        else:
            # Extract the output tensors from the inference response.
            output1 = pb_utils.get_output_tensor_by_name(
              inference_response, 'REQUESTED_OUTPUT_1')
            output2 = pb_utils.get_output_tensor_by_name(
              inference_response, 'REQUESTED_OUTPUT_2')

            # Decide the next steps for model execution based on the received
            # output tensors.

A complete example for sync and async BLS in Python backend is included in the [Examples](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/python_backend/README.html#examples) section.

Using BLS with Decoupled Models[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/bls.html#using-bls-with-decoupled-models "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Starting from 23.03 release, you can execute inference requests on decoupled models in both [default mode](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/python_backend/README.html#default-mode) and [decoupled mode](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/python_backend/README.html#decoupled-mode). By setting the `decoupled` parameter to `True`, the `exec` and `async_exec` function will return an [iterator](https://docs.python.org/3/glossary.html#term-iterator) of inference responses returned by a decoupled model. If the `decoupled` parameter is set to `False`, the `exec` and `async_exec` function will return a single response as shown in the example above. Besides, you can set the timeout via the parameter ‘timeout’ in microseconds within the constructor of `InferenceRequest`. If the request times out, the request will respond with an error. The default of ‘timeout’ is 0 which indicates that the request has no timeout.

Additionally, starting from the 23.04 release, you have the flexibility to select a specific device to receive output tensors from BLS calls. This can be achieved by setting the optional `preferred_memory` parameter within the `InferenceRequest` constructor. To do this, you can create a `PreferredMemory` object and specify the `preferred_memory_type` as either `TRITONSERVER_MEMORY_GPU` or `TRITONSERVER_MEMORY_CPU`, as well as the `preferred_device_id` as an integer to indicate the memory type and device ID on which you wish to receive output tensors. If you do not specify the `preferred_memory` parameter, the output tensors will be allocated on the same device where the output tensors were received from the model to which the BLS call is made.

Example below shows how to use this feature:

import triton_python_backend_utils as pb_utils

class TritonPythonModel:
  ...
    def execute(self, requests):
      ...
      # Create an InferenceRequest object. `model_name`,
      # `requested_output_names`, and `inputs` are the required arguments and
      # must be provided when constructing an InferenceRequest object. Make
      # sure to replace `inputs` argument with a list of `pb_utils.Tensor`
      # objects.
      inference_request = pb_utils.InferenceRequest(
          model_name='model_name',
          requested_output_names=['REQUESTED_OUTPUT_1', 'REQUESTED_OUTPUT_2'],
          inputs=[<pb_utils.Tensor object>])

      # `pb_utils.InferenceRequest` supports request_id, correlation_id,
      # model version, timeout and preferred_memory in addition to the
      # arguments described above.
      # Note: Starting from the 24.03 release, the `correlation_id` parameter
      # supports both string and unsigned integer values.
      # These arguments are optional. An example containing all the arguments:
      # inference_request = pb_utils.InferenceRequest(model_name='model_name',
      # requested_output_names=['REQUESTED_OUTPUT_1', 'REQUESTED_OUTPUT_2'],
      # inputs=[<list of pb_utils.Tensor objects>],
      # request_id="1", correlation_id="ex-4", model_version=1, flags=0, timeout=5,
      # preferred_memory=pb_utils.PreferredMemory(
      # pb_utils.TRITONSERVER_MEMORY_GPU, # or pb_utils.TRITONSERVER_MEMORY_CPU
      # 0))

      # Execute the inference_request and wait for the response. Here we are
      # running a BLS request on a decoupled model, hence setting the parameter
      # 'decoupled' to 'True'.
      inference_responses = inference_request.exec(decoupled=True)

      for inference_response in inference_responses:
        # Check if the inference response has an error
        if inference_response.has_error():
            raise pb_utils.TritonModelException(
              inference_response.error().message())

        # For some models, it is possible that the last response is empty
        if len(infer_response.output_tensors()) > 0:
          # Extract the output tensors from the inference response.
          output1 = pb_utils.get_output_tensor_by_name(
            inference_response, 'REQUESTED_OUTPUT_1')
          output2 = pb_utils.get_output_tensor_by_name(
            inference_response, 'REQUESTED_OUTPUT_2')

          # Decide the next steps for model execution based on the received
          # output tensors. It is possible to use the same output tensors to
          # for the final inference response too.

In addition to the `inference_request.exec(decoupled=True)` function that allows you to execute blocking inference requests on decoupled models, `inference_request.async_exec(decoupled=True)` allows you to perform async inference requests. This can be useful when you do not need the result of the inference immediately. Using `async_exec` function, it is possible to have multiple inflight inference requests and wait for the responses only when needed. Example below shows how to use `async_exec`:

import triton_python_backend_utils as pb_utils
import asyncio

class TritonPythonModel:
  ...

    # You must add the Python 'async' keyword to the beginning of `execute`
    # function if you want to use `async_exec` function.
    async def execute(self, requests):
      ...
      # Create an InferenceRequest object. `model_name`,
      # `requested_output_names`, and `inputs` are the required arguments and
      # must be provided when constructing an InferenceRequest object. Make
      # sure to replace `inputs` argument with a list of `pb_utils.Tensor`
      # objects.
      inference_request = pb_utils.InferenceRequest(
          model_name='model_name',
          requested_output_names=['REQUESTED_OUTPUT_1', 'REQUESTED_OUTPUT_2'],
          inputs=[<pb_utils.Tensor object>])

      infer_response_awaits = []
      for i in range(4):
        # async_exec function returns an
        # [Awaitable](https://docs.python.org/3/library/asyncio-task.html#awaitables)
        # object.
        infer_response_awaits.append(
          inference_request.async_exec(decoupled=True))

      # Wait for all of the inference requests to complete.
      async_responses = await asyncio.gather(*infer_response_awaits)

      for infer_responses in async_responses:
        for infer_response in infer_responses:
          # Check if the inference response has an error
          if inference_response.has_error():
              raise pb_utils.TritonModelException(
                inference_response.error().message())

          # For some models, it is possible that the last response is empty
          if len(infer_response.output_tensors()) > 0:
              # Extract the output tensors from the inference response.
              output1 = pb_utils.get_output_tensor_by_name(
                inference_response, 'REQUESTED_OUTPUT_1')
              output2 = pb_utils.get_output_tensor_by_name(
                inference_response, 'REQUESTED_OUTPUT_2')

              # Decide the next steps for model execution based on the received
              # output tensors.

A complete example for sync and async BLS for decoupled models is included in the [Examples](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/python_backend/README.html#examples) section.

Starting from the 22.04 release, the lifetime of the BLS output tensors have been improved such that if a tensor is no longer needed in your Python model it will be automatically deallocated. This can increase the number of BLS requests that you can execute in your model without running into the out of GPU or shared memory error.

Note: Async BLS is not supported on Python 3.6 or lower due to the `async` keyword and `asyncio.run` being introduced in Python 3.7.

Model Loading API[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/bls.html#model-loading-api "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------

Starting from 23.07 release, you can use the model loading API to load models required by your BLS model. The model loading API is equivalent to the Triton C API for loading models which are documented in [tritonserver.h](https://github.com/triton-inference-server/core/blob/main/include/triton/core/tritonserver.h). Below is an example of how to use the model loading API:

import triton_python_backend_utils as pb_utils

class TritonPythonModel:
    def initialize(self, args):
        self.model_name="onnx_model"
        # Check if the model is ready, and load the model if it is not ready.
        # You can specify the model version in string format. The version is
        # optional, and if not provided, the server will choose a version based
        # on the model and internal policy.
        if not pb_utils.is_model_ready(model_name=self.model_name,
                                       model_version="1"):
            # Load the model from the model repository
            pb_utils.load_model(model_name=self.model_name)

            # Load the model with an optional override model config in JSON
            # representation. If provided, this config will be used for
            # loading the model.
            config = "{\"backend\":\"onnxruntime\", \"version_policy\":{\"specific\":{\"versions\":[1]}}}"
            pb_utils.load_model(model_name=self.model_name, config=config)

            # Load the mode with optional override files. The override files are
            # specified as a dictionary where the key is the file path (with
            # "file:" prefix) and the value is the file content as bytes. The
            # files will form the model directory that the model will be loaded
            # from. If specified, 'config' must be provided to be the model
            # configuration of the override model directory.
            with open('models/onnx_int32_int32_int32/1/model.onnx', 'rb') as file:
                data = file.read()
            files = {"file:1/model.onnx": data}
            pb_utils.load_model(model_name=self.model_name,
                                config=config, files=files)

    def execute(self, requests):
        # Execute the model
        ...
        # If the model is no longer needed, you can unload it. You can also
        # specify whether the dependents of the model should also be unloaded by
        # setting the 'unload_dependents' parameter to True. The default value
        # is False. Need to be careful when unloading the model as it can affect
        # other model instances or other models that depend on it.
        pb_utils.unload_model(model_name=self.model_name,
                              unload_dependents=True)

Note that the model loading API is only supported if the server is running in [explicit model control mode](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/model_management.html#model-control-mode-explicit). Additionally, the model loading API should only be used after the server has been running, which means that the BLS model should not be loaded during server startup. You can use different [client endpoints](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/protocol/extension_model_repository.html) to load the model after the server has been started. The model loading API is currently not supported during the `auto_complete_config` and `finalize` functions.

Using BLS with Stateful Models[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/bls.html#using-bls-with-stateful-models "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Stateful models](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/architecture.html#stateful-models) require setting additional flags in the inference request to indicate the start and end of a sequence. The `flags` argument in the `pb_utils.InferenceRequest` object can be used to indicate whether the request is the first or last request in the sequence. An example indicating that the request is starting the sequence:

inference_request = pb_utils.InferenceRequest(model_name='model_name',
  requested_output_names=['REQUESTED_OUTPUT_1', 'REQUESTED_OUTPUT_2'],
  inputs=[<list of pb_utils.Tensor objects>],
  request_id="1", correlation_id=4,
  flags=pb_utils.TRITONSERVER_REQUEST_FLAG_SEQUENCE_START)

For indicating the ending of the sequence you can use the `pb_utils.TRITONSERVER_REQUEST_FLAG_SEQUENCE_END` flag. If the request is both starting and ending a sequence at the same time (i.e. the sequence has only a single request), you can use the bitwise OR operator to enable both of the flags:

flags = pb_utils.TRITONSERVER_REQUEST_FLAG_SEQUENCE_START | pb_utils.TRITONSERVER_REQUEST_FLAG_SEQUENCE_END

Limitation[#](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/bls.html#limitation "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------

*   You need to make sure that the inference requests performed as a part of your model do not create a circular dependency. For example, if model A performs an inference request on itself and there are no more model instances ready to execute the inference request, the model will block on the inference execution forever.

*   Async BLS is not supported when running a Python model in decoupled mode.

[previous Ensemble Models](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/ensemble_models.html "previous page")[next State Management](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/server_guide/state_management.html "next page")

 On this page 

*   [Using BLS with Decoupled Models](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/bls.html#using-bls-with-decoupled-models)
*   [Model Loading API](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/bls.html#model-loading-api)
*   [Using BLS with Stateful Models](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/bls.html#using-bls-with-stateful-models)
*   [Limitation](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/bls.html#limitation)

[![Image 3: NVIDIA](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_static/nvidia-logo-horiz-rgb-1c-blk-for-screen.svg)![Image 4: NVIDIA](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/_static/nvidia-logo-horiz-rgb-1c-wht-for-screen.svg)](https://www.nvidia.com/)

[Privacy Policy](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/) | [Your Privacy Choices](https://www.nvidia.com/en-us/about-nvidia/privacy-center/) | [Terms of Service](https://www.nvidia.com/en-us/about-nvidia/terms-of-service/) | [Accessibility](https://www.nvidia.com/en-us/about-nvidia/accessibility/) | [Corporate Policies](https://www.nvidia.com/en-us/about-nvidia/company-policies/) | [Product Security](https://www.nvidia.com/en-us/product-security/) | [Contact](https://www.nvidia.com/en-us/contact/)

Copyright © 2018-2026, NVIDIA Corporation.
