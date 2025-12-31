# Source: https://docs.vllm.ai/en/stable/configuration/env_vars/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/configuration/env_vars.md "Edit this page")

# Environment Variables[¶](#environment-variables "Permanent link")

vLLM uses the following environment variables to configure the system:

Warning

Please note that `VLLM_PORT` and `VLLM_HOST_IP` set the port and ip for vLLM\'s **internal usage**. It is not the port and ip for the API server. If you use `--host $VLLM_HOST_IP` and `--port $VLLM_PORT` to start the API server, it will not work.

All environment variables used by vLLM are prefixed with `VLLM_`. **Special care should be taken for Kubernetes users**: please do not name the service as `vllm`, otherwise environment variables set by Kubernetes might conflict with vLLM\'s environment variables, because [Kubernetes sets environment variables for each service with the capitalized service name as the prefix](https://kubernetes.io/docs/concepts/services-networking/service/#environment-variables).

    logger = logging.getLogger(__name__)

    environment_variables: dict[str, Callable[[], Any]] = 
        # or a space separated values table file:
        # meta-llama/Llama-3.2-1B   /tmp/Llama-3.2-1B
        "VLLM_MODEL_REDIRECT_PATH": lambda: os.environ.get(
            "VLLM_MODEL_REDIRECT_PATH", None
        ),
        # Whether to use atomicAdd reduce in gptq/awq marlin kernel.
        "VLLM_MARLIN_USE_ATOMIC_ADD": lambda: os.environ.get(
            "VLLM_MARLIN_USE_ATOMIC_ADD", "0"
        )
        == "1",
        # Whether to use marlin kernel in mxfp4 quantization method
        "VLLM_MXFP4_USE_MARLIN": lambda: maybe_convert_bool(
            os.environ.get("VLLM_MXFP4_USE_MARLIN", None)
        ),
        # The activation dtype for marlin kernel
        "VLLM_MARLIN_INPUT_DTYPE": env_with_choices(
            "VLLM_MARLIN_INPUT_DTYPE", None, ["int8", "fp8"]
        ),
        # Whether to use DeepEPLL kernels for NVFP4 quantization and dispatch method
        # only supported on Blackwell GPUs and with
        # https://github.com/deepseek-ai/DeepEP/pull/341
        "VLLM_DEEPEPLL_NVFP4_DISPATCH": lambda: bool(
            int(os.getenv("VLLM_DEEPEPLL_NVFP4_DISPATCH", "0"))
        ),
        # Whether to turn on the outlines cache for V1
        # This cache is unbounded and on disk, so it's not safe to use in
        # an environment with potentially malicious users.
        "VLLM_V1_USE_OUTLINES_CACHE": lambda: os.environ.get(
            "VLLM_V1_USE_OUTLINES_CACHE", "0"
        )
        == "1",
        # Gap between padding buckets for the forward pass. So we have
        # 8, we will run forward pass with [16, 24, 32, ...].
        "VLLM_TPU_BUCKET_PADDING_GAP": lambda: int(
            os.environ["VLLM_TPU_BUCKET_PADDING_GAP"]
        )
        if "VLLM_TPU_BUCKET_PADDING_GAP" in os.environ
        else 0,
        "VLLM_TPU_MOST_MODEL_LEN": lambda: maybe_convert_int(
            os.environ.get("VLLM_TPU_MOST_MODEL_LEN", None)
        ),
        # Whether using Pathways
        "VLLM_TPU_USING_PATHWAYS": lambda: bool(
            "proxy" in os.getenv("JAX_PLATFORMS", "").lower()
        ),
        # Allow use of DeepGemm kernels for fused moe ops.
        "VLLM_USE_DEEP_GEMM": lambda: bool(int(os.getenv("VLLM_USE_DEEP_GEMM", "1"))),
        # Allow use of DeepGemm specifically for MoE fused ops (overrides only MoE).
        "VLLM_MOE_USE_DEEP_GEMM": lambda: bool(
            int(os.getenv("VLLM_MOE_USE_DEEP_GEMM", "1"))
        ),
        # Whether to use E8M0 scaling when DeepGEMM is used on Blackwell GPUs.
        "VLLM_USE_DEEP_GEMM_E8M0": lambda: bool(
            int(os.getenv("VLLM_USE_DEEP_GEMM_E8M0", "1"))
        ),
        # DeepGemm JITs the kernels on-demand. The warmup attempts to make DeepGemm
        # JIT all the required kernels before model execution so there is no
        # JIT'ing in the hot-path. However, this warmup increases the engine
        # startup time by a couple of minutes.
        # Available options:
        #  - "skip"  : Skip warmup.
        #  - "full"  : Warmup deepgemm by running all possible gemm shapes the
        #   engine could encounter.
        #  - "relax" : Select gemm shapes to run based on some heuristics. The
        #   heuristic aims to have the same effect as running all possible gemm
        #   shapes, but provides no guarantees.
        "VLLM_DEEP_GEMM_WARMUP": env_with_choices(
            "VLLM_DEEP_GEMM_WARMUP",
            "relax",
            [
                "skip",
                "full",
                "relax",
            ],
        ),
        # Whether to use fused grouped_topk used for MoE expert selection.
        "VLLM_USE_FUSED_MOE_GROUPED_TOPK": lambda: bool(
            int(os.getenv("VLLM_USE_FUSED_MOE_GROUPED_TOPK", "1"))
        ),
        # Allow use of FlashInfer MoE kernels for fused moe ops.
        "VLLM_USE_FLASHINFER_MOE_FP16": lambda: bool(
            int(os.getenv("VLLM_USE_FLASHINFER_MOE_FP16", "0"))
        ),
        # Allow use of FlashInfer MoE kernels for fused moe ops.
        "VLLM_USE_FLASHINFER_MOE_FP8": lambda: bool(
            int(os.getenv("VLLM_USE_FLASHINFER_MOE_FP8", "0"))
        ),
        # Allow use of FlashInfer CUTLASS kernels for fused moe ops.
        "VLLM_USE_FLASHINFER_MOE_FP4": lambda: bool(
            int(os.getenv("VLLM_USE_FLASHINFER_MOE_FP4", "0"))
        ),
        # If set to 1, use the FlashInfer
        # MXFP8 (activation) x MXFP4 (weight) MoE backend.
        "VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8": lambda: bool(
            int(os.getenv("VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8", "0"))
        ),
        # If set to 1, use the FlashInfer CUTLASS backend for
        # MXFP8 (activation) x MXFP4 (weight) MoE.
        # This is separate from the TRTLLMGEN path controlled by
        # VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8.
        "VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8_CUTLASS": lambda: bool(
            int(os.getenv("VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8_CUTLASS", "0"))
        ),
        # If set to 1, use the FlashInfer
        # BF16 (activation) x MXFP4 (weight) MoE backend.
        "VLLM_USE_FLASHINFER_MOE_MXFP4_BF16": lambda: bool(
            int(os.getenv("VLLM_USE_FLASHINFER_MOE_MXFP4_BF16", "0"))
        ),
        # Control the cache sized used by the xgrammar compiler. The default
        # of 512 MB should be enough for roughly 1000 JSON schemas.
        # It can be changed with this variable if needed for some reason.
        "VLLM_XGRAMMAR_CACHE_MB": lambda: int(os.getenv("VLLM_XGRAMMAR_CACHE_MB", "512")),
        # Control the threshold for msgspec to use 'zero copy' for
        # serialization/deserialization of tensors. Tensors below
        # this limit will be encoded into the msgpack buffer, and
        # tensors above will instead be sent via a separate message.
        # While the sending side still actually copies the tensor
        # in all cases, on the receiving side, tensors above this
        # limit will actually be zero-copy decoded.
        "VLLM_MSGPACK_ZERO_COPY_THRESHOLD": lambda: int(
            os.getenv("VLLM_MSGPACK_ZERO_COPY_THRESHOLD", "256")
        ),
        # If set, allow insecure serialization using pickle.
        # This is useful for environments where it is deemed safe to use the
        # insecure method and it is needed for some reason.
        "VLLM_ALLOW_INSECURE_SERIALIZATION": lambda: bool(
            int(os.getenv("VLLM_ALLOW_INSECURE_SERIALIZATION", "0"))
        ),
        # IP address used for NIXL handshake between remote agents.
        "VLLM_NIXL_SIDE_CHANNEL_HOST": lambda: os.getenv(
            "VLLM_NIXL_SIDE_CHANNEL_HOST", "localhost"
        ),
        # Port used for NIXL handshake between remote agents.
        "VLLM_NIXL_SIDE_CHANNEL_PORT": lambda: int(
            os.getenv("VLLM_NIXL_SIDE_CHANNEL_PORT", "5600")
        ),
        # Port used for Mooncake handshake between remote agents.
        "VLLM_MOONCAKE_BOOTSTRAP_PORT": lambda: int(
            os.getenv("VLLM_MOONCAKE_BOOTSTRAP_PORT", "8998")
        ),
        # all2all backend for vllm's expert parallel communication
        # Available options:
        # - "naive": naive all2all implementation using broadcasts
        # - "allgather_reducescatter": all2all implementation based on allgather and
        #  reducescatter
        # - "pplx": use pplx kernels
        # - "deepep_high_throughput", use deepep high-throughput kernels
        # - "deepep_low_latency", use deepep low-latency kernels
        # - "flashinfer_all2allv", use flashinfer alltoallv kernels for mnnvl
        "VLLM_ALL2ALL_BACKEND": env_with_choices(
            "VLLM_ALL2ALL_BACKEND",
            "allgather_reducescatter",
            [
                "naive",
                "pplx",
                "deepep_high_throughput",
                "deepep_low_latency",
                "allgather_reducescatter",
                "flashinfer_all2allv",
            ],
        ),
        # Flashinfer MoE backend for vLLM's fused Mixture-of-Experts support.
        # Both require compute capability 10.0 or above.
        # Available options:
        # - "throughput":  [default]
        #     Uses CUTLASS kernels optimized for high-throughput batch inference.
        # - "latency":
        #     Uses TensorRT-LLM kernels optimized for low-latency inference.
        "VLLM_FLASHINFER_MOE_BACKEND": env_with_choices(
            "VLLM_FLASHINFER_MOE_BACKEND",
            "latency",
            ["throughput", "latency", "masked_gemm"],
        ),
        # Control the workspace buffer size for the FlashInfer backend.
        "VLLM_FLASHINFER_WORKSPACE_BUFFER_SIZE": lambda: int(
            os.getenv("VLLM_FLASHINFER_WORKSPACE_BUFFER_SIZE", str(394 * 1024 * 1024))
        ),
        # Control the maximum number of tokens per expert supported by the
        # NVFP4 MoE CUTLASS Kernel. This value is used to create a buffer for
        # the blockscale tensor of activations NVFP4 Quantization.
        # This is used to prevent the kernel from running out of memory.
        "VLLM_MAX_TOKENS_PER_EXPERT_FP4_MOE": lambda: int(
            os.getenv("VLLM_MAX_TOKENS_PER_EXPERT_FP4_MOE", "163840")
        ),
        # Specifies the thresholds of the communicated tensor sizes under which
        # vllm should use flashinfer fused allreduce. The variable should be a
        # JSON with the following format:
        #     
        # Unspecified world sizes will fall back to
        #     
        "VLLM_FLASHINFER_ALLREDUCE_FUSION_THRESHOLDS_MB": lambda: json.loads(
            os.getenv("VLLM_FLASHINFER_ALLREDUCE_FUSION_THRESHOLDS_MB", "")
        ),
        # MoE routing strategy selector.
        # See `RoutingSimulator.get_available_strategies()` # for available
        # strategies.
        # Custom routing strategies can be registered by
        # RoutingSimulator.register_strategy()
        # Note: custom strategies may not produce correct model outputs
        "VLLM_MOE_ROUTING_SIMULATION_STRATEGY": lambda: os.environ.get(
            "VLLM_MOE_ROUTING_SIMULATION_STRATEGY", ""
        ).lower(),
        # Regex timeout for use by the vLLM tool parsing plugins.
        "VLLM_TOOL_PARSE_REGEX_TIMEOUT_SECONDS": lambda: int(
            os.getenv("VLLM_TOOL_PARSE_REGEX_TIMEOUT_SECONDS", "1")
        ),
        # Reduce CPU usage when vLLM is idle. Enabling this will incur small
        # latency penalty when a request eventually comes.
        "VLLM_SLEEP_WHEN_IDLE": lambda: bool(int(os.getenv("VLLM_SLEEP_WHEN_IDLE", "0"))),
        # Control the max chunk bytes (in MB) for the rpc message queue.
        # Object larger than this threshold will be broadcast to worker
        # processes via zmq.
        "VLLM_MQ_MAX_CHUNK_BYTES_MB": lambda: int(
            os.getenv("VLLM_MQ_MAX_CHUNK_BYTES_MB", "16")
        ),
        # Timeout in seconds for execute_model RPC calls in multiprocessing
        # executor (only applies when TP > 1).
        "VLLM_EXECUTE_MODEL_TIMEOUT_SECONDS": lambda: int(
            os.getenv("VLLM_EXECUTE_MODEL_TIMEOUT_SECONDS", "300")
        ),
        # KV Cache layout used throughout vllm.
        # Some common values are:
        # - NHD
        # - HND
        # Where N=num_blocks, H=num_heads and D=head_size. The default value will
        # leave the layout choice to the backend. Mind that backends may only
        # implement and support a subset of all possible layouts.
        "VLLM_KV_CACHE_LAYOUT": env_with_choices(
            "VLLM_KV_CACHE_LAYOUT", None, ["NHD", "HND"]
        ),
        # Enable checking whether the generated logits contain NaNs,
        # indicating corrupted output. Useful for debugging low level bugs
        # or bad hardware but it may add compute overhead.
        "VLLM_COMPUTE_NANS_IN_LOGITS": lambda: bool(
            int(os.getenv("VLLM_COMPUTE_NANS_IN_LOGITS", "0"))
        ),
        # Controls whether or not emulations are used for NVFP4
        # generations on machines < 100 for compressed-tensors
        # models
        "VLLM_USE_NVFP4_CT_EMULATIONS": lambda: bool(
            int(os.getenv("VLLM_USE_NVFP4_CT_EMULATIONS", "0"))
        ),
        # Time (in seconds) after which the KV cache on the producer side is
        # automatically cleared if no READ notification is received from the
        # consumer. This is only applicable when using NixlConnector in a
        # disaggregated decode-prefill setup.
        "VLLM_NIXL_ABORT_REQUEST_TIMEOUT": lambda: int(
            os.getenv("VLLM_NIXL_ABORT_REQUEST_TIMEOUT", "480")
        ),
        # Timeout (in seconds) for MooncakeConnector in PD disaggregated setup.
        "VLLM_MOONCAKE_ABORT_REQUEST_TIMEOUT": lambda: int(
            os.getenv("VLLM_MOONCAKE_ABORT_REQUEST_TIMEOUT", "480")
        ),
        # Controls whether or not to use cudnn prefill
        "VLLM_USE_CUDNN_PREFILL": lambda: bool(
            int(os.getenv("VLLM_USE_CUDNN_PREFILL", "0"))
        ),
        # Controls whether to use TRT-LLM ragged DeepSeek prefill
        "VLLM_USE_TRTLLM_RAGGED_DEEPSEEK_PREFILL": lambda: bool(
            int(os.getenv("VLLM_USE_TRTLLM_RAGGED_DEEPSEEK_PREFILL", "0"))
        ),
        # If set to 1/True, use the TRTLLM attention backend in flashinfer.
        # If set to 0/False, use the default attention backend in flashinfer.
        # If not set, auto-detect the attention backend in flashinfer.
        "VLLM_USE_TRTLLM_ATTENTION": lambda: (
            None
            if "VLLM_USE_TRTLLM_ATTENTION" not in os.environ
            else os.environ["VLLM_USE_TRTLLM_ATTENTION"].lower() in ("1", "true")
        ),
        # If set to 1, when we use fp8 kv, we do not quantize Q to fp8
        "VLLM_FLASHINFER_DISABLE_Q_QUANTIZATION": lambda: bool(
            int(os.getenv("VLLM_FLASHINFER_DISABLE_Q_QUANTIZATION", "0"))
        ),
        # If set, it means we pre-downloaded cubin files and flashinfer will
        # read the cubin files directly.
        "VLLM_HAS_FLASHINFER_CUBIN": lambda: bool(
            int(os.getenv("VLLM_HAS_FLASHINFER_CUBIN", "0"))
        ),
        # Supported options:
        # - "flashinfer-cudnn": use flashinfer cudnn GEMM backend
        # - "flashinfer-trtllm": use flashinfer trtllm GEMM backend
        # - "flashinfer-cutlass": use flashinfer cutlass GEMM backend
        # - <none>: automatically pick an available backend
        "VLLM_NVFP4_GEMM_BACKEND": env_with_choices(
            "VLLM_NVFP4_GEMM_BACKEND",
            None,
            ["flashinfer-cudnn", "flashinfer-trtllm", "flashinfer-cutlass", "cutlass"],
        ),
        # Controls garbage collection during CUDA graph capture.
        # If set to 0 (default), enables GC freezing to speed up capture time.
        # If set to 1, allows GC to run during capture.
        "VLLM_ENABLE_CUDAGRAPH_GC": lambda: bool(
            int(os.getenv("VLLM_ENABLE_CUDAGRAPH_GC", "0"))
        ),
        # Used to force set up loopback IP
        "VLLM_LOOPBACK_IP": lambda: os.getenv("VLLM_LOOPBACK_IP", ""),
        # Used to set the process name prefix for vLLM processes.
        # This is useful for debugging and monitoring purposes.
        # The default value is "VLLM".
        "VLLM_PROCESS_NAME_PREFIX": lambda: os.getenv("VLLM_PROCESS_NAME_PREFIX", "VLLM"),
        # Allow chunked local attention with hybrid kv cache manager.
        # Currently using the Hybrid KV cache manager with chunked local attention
        # in the Llama4 models (the only models currently using chunked local attn)
        # causes a latency regression. For this reason, we disable it by default.
        # This flag is used to allow users to enable it if they want to (to save on
        # kv-cache memory usage and enable longer contexts)
        # TODO(lucas): Remove this flag once latency regression is resolved.
        "VLLM_ALLOW_CHUNKED_LOCAL_ATTN_WITH_HYBRID_KV_CACHE": lambda: bool(
            int(os.getenv("VLLM_ALLOW_CHUNKED_LOCAL_ATTN_WITH_HYBRID_KV_CACHE", "0"))
        ),
        # Enables support for the "store" option in the OpenAI Responses API.
        # When set to 1, vLLM's OpenAI server will retain the input and output
        # messages for those requests in memory. By default, this is disabled (0),
        # and the "store" option is ignored.
        # NOTE/WARNING:
        # 1. Messages are kept in memory only (not persisted to disk) and will be
        #    lost when the vLLM server shuts down.
        # 2. Enabling this option will cause a memory leak, as stored messages are
        #    never removed from memory until the server terminates.
        "VLLM_ENABLE_RESPONSES_API_STORE": lambda: bool(
            int(os.getenv("VLLM_ENABLE_RESPONSES_API_STORE", "0"))
        ),
        # If set, use the fp8 mfma in rocm paged attention.
        "VLLM_ROCM_FP8_MFMA_PAGE_ATTN": lambda: bool(
            int(os.getenv("VLLM_ROCM_FP8_MFMA_PAGE_ATTN", "0"))
        ),
        # Whether to use pytorch symmetric memory for allreduce
        "VLLM_ALLREDUCE_USE_SYMM_MEM": lambda: bool(
            int(os.getenv("VLLM_ALLREDUCE_USE_SYMM_MEM", "1"))
        ),
        # Experimental: use this to enable MCP tool calling for non harmony models
        "VLLM_USE_EXPERIMENTAL_PARSER_CONTEXT": lambda: bool(
            int(os.getenv("VLLM_USE_EXPERIMENTAL_PARSER_CONTEXT", "0"))
        ),
        # Allows vllm to find tuned config under customized folder
        "VLLM_TUNED_CONFIG_FOLDER": lambda: os.getenv("VLLM_TUNED_CONFIG_FOLDER", None),
        # Valid values are container,code_interpreter,web_search_preview
        # ex VLLM_GPT_OSS_SYSTEM_TOOL_MCP_LABELS=container,code_interpreter
        # If the server_label of your mcp tool is not in this list it will
        # be completely ignored.
        "VLLM_GPT_OSS_SYSTEM_TOOL_MCP_LABELS": env_set_with_choices(
            "VLLM_GPT_OSS_SYSTEM_TOOL_MCP_LABELS",
            default=[],
            choices=["container", "code_interpreter", "web_search_preview"],
        ),
        # Allows harmony instructions to be injected on system messages
        "VLLM_GPT_OSS_HARMONY_SYSTEM_INSTRUCTIONS": lambda: bool(
            int(os.getenv("VLLM_GPT_OSS_HARMONY_SYSTEM_INSTRUCTIONS", "0"))
        ),
        # Enable automatic retry when tool call JSON parsing fails
        # If enabled, returns an error message to the model to retry
        # If disabled (default), raises an exception and fails the request
        "VLLM_TOOL_JSON_ERROR_AUTOMATIC_RETRY": lambda: bool(
            int(os.getenv("VLLM_TOOL_JSON_ERROR_AUTOMATIC_RETRY", "0"))
        ),
        # Add optional custom scopes for profiling, disable to avoid overheads
        "VLLM_CUSTOM_SCOPES_FOR_PROFILING": lambda: bool(
            int(os.getenv("VLLM_CUSTOM_SCOPES_FOR_PROFILING", "0"))
        ),
        # Add optional nvtx scopes for profiling, disable to avoid overheads
        "VLLM_NVTX_SCOPES_FOR_PROFILING": lambda: bool(
            int(os.getenv("VLLM_NVTX_SCOPES_FOR_PROFILING", "0"))
        ),
        # Represent block hashes in KV cache events as 64-bit integers instead of
        # raw bytes. Defaults to True for backward compatibility.
        "VLLM_KV_EVENTS_USE_INT_BLOCK_HASHES": lambda: bool(
            int(os.getenv("VLLM_KV_EVENTS_USE_INT_BLOCK_HASHES", "1"))
        ),
        # Name of the shared memory buffer used for object storage.
        # Only effective when mm_config.mm_processor_cache_type == "shm".
        "VLLM_OBJECT_STORAGE_SHM_BUFFER_NAME": lambda: os.getenv(
            "VLLM_OBJECT_STORAGE_SHM_BUFFER_NAME", "VLLM_OBJECT_STORAGE_SHM_BUFFER"
        ),
        # The size in MB of the buffers (NVL and RDMA) used by DeepEP
        "VLLM_DEEPEP_BUFFER_SIZE_MB": lambda: int(
            os.getenv("VLLM_DEEPEP_BUFFER_SIZE_MB", "1024")
        ),
        # Force DeepEP to use intranode kernel for inter-node communication in
        # high throughput mode. This is useful archive higher prefill throuhgput
        # on system supports multi-node nvlink (e.g GB200).
        "VLLM_DEEPEP_HIGH_THROUGHPUT_FORCE_INTRA_NODE": lambda: bool(
            int(os.getenv("VLLM_DEEPEP_HIGH_THROUGHPUT_FORCE_INTRA_NODE", "0"))
        ),
        # Allow DeepEP to use MNNVL (multi-node nvlink) for internode_ll kernel,
        # turn this for better latency on GB200 like system
        "VLLM_DEEPEP_LOW_LATENCY_USE_MNNVL": lambda: bool(
            int(os.getenv("VLLM_DEEPEP_LOW_LATENCY_USE_MNNVL", "0"))
        ),
        # The number of SMs to allocate for communication kernels when running DBO
        # the rest of the SMs on the device will be allocated to compute
        "VLLM_DBO_COMM_SMS": lambda: int(os.getenv("VLLM_DBO_COMM_SMS", "20")),
        # Enable max_autotune & coordinate_descent_tuning in inductor_config
        # to compile static shapes passed from compile_sizes in compilation_config
        # If set to 1, enable max_autotune; By default, this is enabled (1)
        "VLLM_ENABLE_INDUCTOR_MAX_AUTOTUNE": lambda: bool(
            int(os.getenv("VLLM_ENABLE_INDUCTOR_MAX_AUTOTUNE", "1"))
        ),
        # If set to 1, enable coordinate_descent_tuning;
        # By default, this is enabled (1)
        "VLLM_ENABLE_INDUCTOR_COORDINATE_DESCENT_TUNING": lambda: bool(
            int(os.getenv("VLLM_ENABLE_INDUCTOR_COORDINATE_DESCENT_TUNING", "1"))
        ),
        # Flag to enable NCCL symmetric memory allocation and registration
        "VLLM_USE_NCCL_SYMM_MEM": lambda: bool(
            int(os.getenv("VLLM_USE_NCCL_SYMM_MEM", "0"))
        ),
        # NCCL header path
        "VLLM_NCCL_INCLUDE_PATH": lambda: os.environ.get("VLLM_NCCL_INCLUDE_PATH", None),
        # Flag to enable FBGemm kernels on model execution
        "VLLM_USE_FBGEMM": lambda: bool(int(os.getenv("VLLM_USE_FBGEMM", "0"))),
        # GC debug config
        # - VLLM_GC_DEBUG=0: disable GC debugger
        # - VLLM_GC_DEBUG=1: enable GC debugger with gc.collect elpased times
        # - VLLM_GC_DEBUG='': enable GC debugger with
        #                                      top 5 collected objects
        "VLLM_GC_DEBUG": lambda: os.getenv("VLLM_GC_DEBUG", ""),
        # Debug workspace allocations.
        # logging of workspace resize operations.
        "VLLM_DEBUG_WORKSPACE": lambda: bool(int(os.getenv("VLLM_DEBUG_WORKSPACE", "0"))),
        # Disables parallel execution of shared_experts via separate cuda stream
        "VLLM_DISABLE_SHARED_EXPERTS_STREAM": lambda: bool(
            int(os.getenv("VLLM_DISABLE_SHARED_EXPERTS_STREAM", "0"))
        ),
        # Limits when we run shared_experts in a separate stream.
        # We found out that for large batch sizes, the separate stream
        # execution is not beneficial (most likely because of the input clone)
        # TODO(alexm-redhat): Tune to be more dynamic based on GPU type
        "VLLM_SHARED_EXPERTS_STREAM_TOKEN_THRESHOLD": lambda: int(
            int(os.getenv("VLLM_SHARED_EXPERTS_STREAM_TOKEN_THRESHOLD", 256))
        ),
        # Format for saving torch.compile cache artifacts
        # - "binary": saves as binary file
        #     Safe for multiple vllm serve processes accessing the same torch compile cache.
        # - "unpacked": saves as directory structure (for inspection/debugging)
        #     NOT multiprocess safe - race conditions may occur with multiple processes.
        #     Allows viewing and setting breakpoints in Inductor's code output files.
        "VLLM_COMPILE_CACHE_SAVE_FORMAT": env_with_choices(
            "VLLM_COMPILE_CACHE_SAVE_FORMAT", "binary", ["binary", "unpacked"]
        ),
        # Flag to enable v2 model runner.
        "VLLM_USE_V2_MODEL_RUNNER": lambda: bool(
            int(os.getenv("VLLM_USE_V2_MODEL_RUNNER", "0"))
        ),
    }

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [November 19, 2025] ]