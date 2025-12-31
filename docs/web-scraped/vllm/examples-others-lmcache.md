# Source: https://docs.vllm.ai/en/stable/examples/others/lmcache/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/others/lmcache.md "Edit this page")

# LMCache Examples[¶](#lmcache-examples "Permanent link")

Source <https://github.com/vllm-project/vllm/tree/main/examples/others/lmcache>.

This folder demonstrates how to use LMCache for disaggregated prefilling, CPU offloading and KV cache sharing.

## 1. Disaggregated Prefill in vLLM v1[¶](#1-disaggregated-prefill-in-vllm-v1 "Permanent link") 

This example demonstrates how to run LMCache with disaggregated prefill using NIXL on a single node.

### Prerequisites[¶](#prerequisites "Permanent link")

-   Install [LMCache](https://github.com/LMCache/LMCache). You can simply run `pip install lmcache`.
-   Install [NIXL](https://github.com/ai-dynamo/nixl).
-   At least 2 GPUs
-   Valid Hugging Face token (HF_TOKEN) for Llama 3.1 8B Instruct.

### Usage[¶](#usage "Permanent link")

Run `cd disagg_prefill_lmcache_v1` to get into `disagg_prefill_lmcache_v1` folder, and then run

    bash disagg_example_nixl.sh

to run disaggregated prefill and benchmark the performance.

### Components[¶](#components "Permanent link")

#### Server Scripts[¶](#server-scripts "Permanent link")

-   `disagg_prefill_lmcache_v1/disagg_vllm_launcher.sh` - Launches individual vLLM servers for prefill/decode, and also launches the proxy server.
-   `disagg_prefill_lmcache_v1/disagg_proxy_server.py` - FastAPI proxy server that coordinates between prefiller and decoder
-   `disagg_prefill_lmcache_v1/disagg_example_nixl.sh` - Main script to run the example

#### Configuration[¶](#configuration "Permanent link")

-   `disagg_prefill_lmcache_v1/configs/lmcache-prefiller-config.yaml` - Configuration for prefiller server
-   `disagg_prefill_lmcache_v1/configs/lmcache-decoder-config.yaml` - Configuration for decoder server

#### Log Files[¶](#log-files "Permanent link")

The main script generates several log files:

-   `prefiller.log` - Logs from the prefill server
-   `decoder.log` - Logs from the decode server
-   `proxy.log` - Logs from the proxy server

## 2. CPU Offload Examples[¶](#2-cpu-offload-examples "Permanent link") 

-   `python cpu_offload_lmcache.py -v v0` - CPU offloading implementation for vLLM v0
-   `python cpu_offload_lmcache.py -v v1` - CPU offloading implementation for vLLM v1

## 3. KV Cache Sharing[¶](#3-kv-cache-sharing "Permanent link") 

The `kv_cache_sharing_lmcache_v1.py` example demonstrates how to share KV caches between vLLM v1 instances.

## 4. Disaggregated Prefill in vLLM v0[¶](#4-disaggregated-prefill-in-vllm-v0 "Permanent link") 

The `disaggregated_prefill_lmcache_v0.py` provides an example of how to run disaggregated prefill in vLLM v0.

## Example materials[¶](#example-materials "Permanent link")

cpu_offload_lmcache.py

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    """
    This file demonstrates the example usage of cpu offloading
    with LMCache in vLLM v1 or v0.

    Usage:

        Specify vLLM version

        -v v0 : Use LMCacheConnector
                model = mistralai/Mistral-7B-Instruct-v0.2
                (Includes enable_chunked_prefill = True)

        -v v1 : Use LMCacheConnectorV1 (default)
                model = meta-llama/Meta-Llama-3.1-8B-Instruct
                (Without enable_chunked_prefill)

    Note that `lmcache` is needed to run this example.
    Requirements:
    https://docs.lmcache.ai/getting_started/installation.html#prerequisites
    Learn more about LMCache environment setup, please refer to:
    https://docs.lmcache.ai/getting_started/installation.html
    """

    import argparse
    import contextlib
    import os
    import time
    from dataclasses import asdict

    from lmcache.integration.vllm.utils import ENGINE_NAME
    from lmcache.v1.cache_engine import LMCacheEngineBuilder

    from vllm import LLM, SamplingParams
    from vllm.config import KVTransferConfig
    from vllm.engine.arg_utils import EngineArgs

    def setup_environment_variables():
        # LMCache-related environment variables
        # Use experimental features in LMCache
        os.environ["LMCACHE_USE_EXPERIMENTAL"] = "True"
        # LMCache is set to use 256 tokens per chunk
        os.environ["LMCACHE_CHUNK_SIZE"] = "256"
        # Enable local CPU backend in LMCache
        os.environ["LMCACHE_LOCAL_CPU"] = "True"
        # Set local CPU memory limit to 5.0 GB
        os.environ["LMCACHE_MAX_LOCAL_CPU_SIZE"] = "5.0"

    @contextlib.contextmanager
    def build_llm_with_lmcache(lmcache_connector: str, model: str):
        ktc = KVTransferConfig(
            kv_connector=lmcache_connector,
            kv_role="kv_both",
        )
        # Set GPU memory utilization to 0.8 for an A40 GPU with 40GB
        # memory. Reduce the value if your GPU has less memory.
        # Note: LMCache supports chunked prefill (see vLLM#14505, LMCache#392).
        llm_args = EngineArgs(
            model=model,
            kv_transfer_config=ktc,
            max_model_len=8000,
            gpu_memory_utilization=0.8,
        )

        llm = LLM(**asdict(llm_args))
        try:
            yield llm
        finally:
            # Clean up lmcache backend
            LMCacheEngineBuilder.destroy(ENGINE_NAME)

    def print_output(
        llm: LLM,
        prompt: list[str],
        sampling_params: SamplingParams,
        req_str: str,
    ):
        # Should be able to see logs like the following:
        # `LMCache INFO: Storing KV cache for 6006 out of 6006 tokens for request 0`
        # This indicates that the KV cache has been stored in LMCache.
        start = time.time()
        outputs = llm.generate(prompt, sampling_params)
        print("-" * 50)
        for output in outputs:
            generated_text = output.outputs[0].text
            print(f"Generated text: ")
        print(f"Generation took  seconds,  request done.")
        print("-" * 50)

    def parse_args():
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "-v",
            "--version",
            choices=["v0", "v1"],
            default="v1",
            help="Specify vLLM version (default: v1)",
        )
        return parser.parse_args()

    def main():
        lmcache_connector = "LMCacheConnectorV1"
        model = "meta-llama/Meta-Llama-3.1-8B-Instruct"
        setup_environment_variables()
        with build_llm_with_lmcache(lmcache_connector, model) as llm:
            # This example script runs two requests with a shared prefix.
            # Define the shared prompt and specific prompts
            shared_prompt = "Hello, how are you?" * 1000
            first_prompt = [
                shared_prompt + "Hello, my name is",
            ]
            second_prompt = [
                shared_prompt + "Tell me a very long story",
            ]

            sampling_params = SamplingParams(temperature=0, top_p=0.95, max_tokens=10)

            # Print the first output
            print_output(llm, first_prompt, sampling_params, "first")

            time.sleep(1)

            # print the second output
            print_output(llm, second_prompt, sampling_params, "second")

    if __name__ == "__main__":
        main()

disagg_prefill_lmcache_v0.py

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    """
    This file demonstrates the example usage of disaggregated prefilling
    with LMCache.
    We will launch 2 vllm instances (GPU 0 for prefill and GPU 1 for decode),
    and launch an additional LMCache server.
    KV cache is transferred in the following manner:
    vLLM prefill node -> LMCache server -> vLLM decode node.

    Note that `pip install lmcache` is needed to run this example.
    Learn more about LMCache in https://github.com/LMCache/LMCache.
    """

    import os
    import subprocess
    import time
    from multiprocessing import Event, Process

    from lmcache.experimental.cache_engine import LMCacheEngineBuilder
    from lmcache.integration.vllm.utils import ENGINE_NAME

    from vllm import LLM, SamplingParams
    from vllm.config import KVTransferConfig

    # LMCache-related environment variables
    # The port to start LMCache server
    port = 8100
    # Use experimental features in LMCache
    os.environ["LMCACHE_USE_EXPERIMENTAL"] = "True"
    # LMCache is set to use 256 tokens per chunk
    os.environ["LMCACHE_CHUNK_SIZE"] = "256"
    # Disable local CPU backend in LMCache
    os.environ["LMCACHE_LOCAL_CPU"] = "False"
    # Set local CPU memory buffer limit to 5.0 GB
    os.environ["LMCACHE_MAX_LOCAL_CPU_SIZE"] = "5.0"
    # Set the remote URL for LMCache server
    os.environ["LMCACHE_REMOTE_URL"] = f"lm://localhost:"
    # Set the serializer/deserializer between vllm and LMCache server
    # `naive` indicates using raw bytes of the tensor without any compression
    os.environ["LMCACHE_REMOTE_SERDE"] = "naive"

    prompts = [
        "Hello, how are you?" * 1000,
    ]

    def run_prefill(prefill_done, prompts):
        # We use GPU 0 for prefill node.
        os.environ["CUDA_VISIBLE_DEVICES"] = "0"

        sampling_params = SamplingParams(temperature=0, top_p=0.95, max_tokens=1)

        ktc = KVTransferConfig(
            kv_connector="LMCacheConnector",
            kv_role="kv_producer",
            kv_rank=0,
            kv_parallel_size=2,
        )
        # Set GPU memory utilization to 0.8 for an A40 GPU with 40GB
        # memory. Reduce the value if your GPU has less memory.
        llm = LLM(
            model="mistralai/Mistral-7B-Instruct-v0.2",
            kv_transfer_config=ktc,
            max_model_len=8000,
            gpu_memory_utilization=0.8,
            enforce_eager=True,
        )

        # llm.generate(prompts, sampling_params)
        outputs = llm.generate(prompts, sampling_params)
        for output in outputs:
            generated_text = output.outputs[0].text
            print(f"Generated text: ")
        print("Prefill node is finished.")
        prefill_done.set()

        # Clean up lmcache backend
        LMCacheEngineBuilder.destroy(ENGINE_NAME)

    def run_decode(prefill_done, prompts, timeout=1):
        # We use GPU 1 for decode node.
        os.environ["CUDA_VISIBLE_DEVICES"] = "1"

        sampling_params = SamplingParams(temperature=0, top_p=0.95, max_tokens=10)

        ktc = KVTransferConfig(
            kv_connector="LMCacheConnector",
            kv_role="kv_consumer",
            kv_rank=1,
            kv_parallel_size=2,
        )
        # Set GPU memory utilization to 0.8 for an A40 GPU with 40GB
        # of memory. Reduce the value if your GPU has less memory.
        llm = LLM(
            model="mistralai/Mistral-7B-Instruct-v0.2",
            kv_transfer_config=ktc,
            max_model_len=8000,
            gpu_memory_utilization=0.8,
            enforce_eager=True,
        )

        print("Waiting for prefill node to finish...")
        prefill_done.wait()
        time.sleep(timeout)

        outputs = llm.generate(prompts, sampling_params)
        for output in outputs:
            generated_text = output.outputs[0].text
            print(f"Generated text: ")

        # Clean up lmcache backend
        LMCacheEngineBuilder.destroy(ENGINE_NAME)

    def run_lmcache_server(port):
        server_proc = subprocess.Popen(
            ["python", "-m", "lmcache.experimental.server", "localhost", str(port)]
        )
        return server_proc

    def main():
        prefill_done = Event()
        prefill_process = Process(target=run_prefill, args=(prefill_done, prompts))
        decode_process = Process(target=run_decode, args=(prefill_done, prompts))
        lmcache_server_process = run_lmcache_server(port)

        # Start prefill node
        prefill_process.start()

        # Start decode node
        decode_process.start()

        # Clean up the processes
        decode_process.join()
        prefill_process.terminate()
        lmcache_server_process.terminate()
        lmcache_server_process.wait()

    if __name__ == "__main__":
        main()

disagg_prefill_lmcache_v1/configs/lmcache-decoder-config.yaml

    local_cpu: False
    max_local_cpu_size: 0
    #local_disk: 
    max_local_disk_size: 0
    remote_serde: NULL

    enable_nixl: True
    nixl_role: "receiver"
    nixl_peer_host: "localhost"
    nixl_peer_port: 55555
    nixl_buffer_size: 1073741824 # 1GB
    nixl_buffer_device: "cuda"
    nixl_enable_gc: True

disagg_prefill_lmcache_v1/configs/lmcache-prefiller-config.yaml

    local_cpu: False
    max_local_cpu_size: 0
    #local_disk: 
    max_local_disk_size: 0
    remote_serde: NULL

    enable_nixl: True
    nixl_role: "sender"
    nixl_peer_host: "localhost"
    nixl_peer_port: 55555
    nixl_buffer_size: 1073741824 # 1GB
    nixl_buffer_device: "cuda"
    nixl_enable_gc: True

disagg_prefill_lmcache_v1/disagg_example_nixl.sh

    #!/bin/bash

    echo "Warning: LMCache disaggregated prefill support for vLLM v1 is experimental and subject to change."

    PIDS=()

    # Switch to the directory of the current script
    cd "$(dirname "$")"

    check_hf_token() 

    check_num_gpus() 

    ensure_python_library_installed() 

    cleanup() 

    wait_for_server() /v1/completions" > /dev/null; then
          return 0
        fi

        local now=$(date +%s)
        if (( now - start_time >= timeout_seconds )); then
          echo "Timeout waiting for server"
          return 1
        fi

        sleep 1
      done
    }

    main() 

    main

disagg_prefill_lmcache_v1/disagg_proxy_server.py

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project

    import argparse
    import os
    import time
    from contextlib import asynccontextmanager

    import httpx
    import numpy as np
    from fastapi import FastAPI, Request
    from fastapi.responses import StreamingResponse

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        """
        Lifespan context manager to handle startup and shutdown events.
        """
        # Startup: Initialize clients
        prefiller_base_url = (
            f"http://:/v1"
        )
        decoder_base_url = (
            f"http://:/v1"
        )

        app.state.prefill_client = httpx.AsyncClient(
            timeout=None,
            base_url=prefiller_base_url,
            limits=httpx.Limits(
                max_connections=None,
                max_keepalive_connections=None,
            ),
        )
        app.state.decode_client = httpx.AsyncClient(
            timeout=None,
            base_url=decoder_base_url,
            limits=httpx.Limits(
                max_connections=None,
                max_keepalive_connections=None,
            ),
        )

        yield

        # Shutdown: Close clients
        await app.state.prefill_client.aclose()
        await app.state.decode_client.aclose()

    # Update FastAPI app initialization to use lifespan
    app = FastAPI(lifespan=lifespan)

    class StatsCalculator:
        def __init__(self):
            self._stats = []
            self._last_log_time = time.time()

        def add(self, value):
            self._stats.append(value)
            if time.time() - self._last_log_time > 5:
                self._log_stats()
                self._last_log_time = time.time()

        def _log_stats(self):
            # Print average, median, and 99th percentile
            np_arr = np.array(self._stats)
            output_str = (
                f"\nNum requests: "
                + "\nPrefill node TTFT stats:"
                + f"\n - Average (ms): "
                + f"\n - Median (ms): "
                + f"\n - 99th Percentile (ms): \n"
            )
            print(
                "===============================",
                output_str,
                "===============================",
            )

    stats_calculator = StatsCalculator()
    counter = 0

    def parse_args():
        parser = argparse.ArgumentParser()

        parser.add_argument("--port", type=int, default=8000)
        parser.add_argument("--host", type=str, default="localhost")
        parser.add_argument("--prefiller-host", type=str, default="localhost")
        parser.add_argument("--prefiller-port", type=int, default=8100)
        parser.add_argument("--decoder-host", type=str, default="localhost")
        parser.add_argument("--decoder-port", type=int, default=8200)
        args = parser.parse_args()
        return args

    # Initialize variables to hold the persistent clients
    app.state.prefill_client = None
    app.state.decode_client = None

    async def send_request_to_service(
        client: httpx.AsyncClient, endpoint: str, req_data: dict
    ):
        """
        Send a request to a service using a persistent client.
        """
        req_data = req_data.copy()
        req_data["max_tokens"] = 1
        if "max_completion_tokens" in req_data:
            req_data["max_completion_tokens"] = 1

        headers = "}
        response = await client.post(endpoint, json=req_data, headers=headers)
        response.raise_for_status()

        # read/consume the response body to release the connection
        # otherwise, it would http.ReadError
        await response.aread()

        return response

    async def stream_service_response(
        client: httpx.AsyncClient, endpoint: str, req_data: dict
    ):
        """
        Asynchronously stream the response from a service using a persistent client.
        """
        headers = "}
        async with client.stream(
            "POST", endpoint, json=req_data, headers=headers
        ) as response:
            response.raise_for_status()
            async for chunk in response.aiter_bytes():
                yield chunk

    @app.post("/v1/completions")
    async def handle_completions(request: Request):
        global counter, stats_calculator
        counter += 1

        st = time.time()
        try:
            req_data = await request.json()

            # Send request to prefill service, ignore the response
            await send_request_to_service(
                app.state.prefill_client, "/completions", req_data
            )

            et = time.time()
            stats_calculator.add(et - st)

            # Stream response from decode service
            async def generate_stream():
                async for chunk in stream_service_response(
                    app.state.decode_client, "/completions", req_data
                ):
                    yield chunk

            return StreamingResponse(generate_stream(), media_type="text/event-stream")

        except Exception as e:
            import sys
            import traceback

            exc_info = sys.exc_info()
            print("Error occurred in disagg prefill proxy server - completions endpoint")
            print(e)
            print("".join(traceback.format_exception(*exc_info)))
            raise

    @app.post("/v1/chat/completions")
    async def handle_chat_completions(request: Request):
        global counter, stats_calculator
        counter += 1

        st = time.time()
        try:
            req_data = await request.json()

            # Send request to prefill service, ignore the response
            await send_request_to_service(
                app.state.prefill_client, "/chat/completions", req_data
            )

            et = time.time()
            stats_calculator.add(et - st)

            # Stream response from decode service
            async def generate_stream():
                async for chunk in stream_service_response(
                    app.state.decode_client, "/chat/completions", req_data
                ):
                    yield chunk

            return StreamingResponse(generate_stream(), media_type="text/event-stream")

        except Exception as e:
            import sys
            import traceback

            exc_info = sys.exc_info()
            print(
                "Error occurred in disagg prefill proxy server  - chat completions endpoint"
            )
            print(e)
            print("".join(traceback.format_exception(*exc_info)))
            raise

    if __name__ == "__main__":
        global global_args
        global_args = parse_args()

        import uvicorn

        uvicorn.run(app, host=global_args.host, port=global_args.port)

disagg_prefill_lmcache_v1/disagg_vllm_launcher.sh

    #!/bin/bash

    SCRIPT_DIR="$(cd "$(dirname "$")" && pwd)"

    if [[ $# -lt 1 ]]; then
        echo "Usage: $0 <prefiller | decoder> [model]"
        exit 1
    fi

    if [[ $# -eq 1 ]]; then
        echo "Using default model: meta-llama/Llama-3.1-8B-Instruct"
        MODEL="meta-llama/Llama-3.1-8B-Instruct"
    else
        echo "Using model: $2"
        MODEL=$2
    fi

    # The prefillers and decoders in LMCache use the same hash seed for all chunk keys.
    # This seed must be aligned so that decoders can identify and retrieve KV cache
    # entries stored by prefillers.
    #
    # WARNING: Using a fixed hash seed is insecure and makes the application vulnerable to
    # denial-of-service attacks. In a production environment, this should be set to a
    # secure random value. This is set to a fixed value for demonstration purposes only.
    export PYTHONHASHSEED=$

    if [[ $1 == "prefiller" ]]; then
        # Prefiller listens on port 8100
        prefill_config_file=$SCRIPT_DIR/configs/lmcache-prefiller-config.yaml

        UCX_TLS=cuda_ipc,cuda_copy,tcp \
            LMCACHE_CONFIG_FILE=$prefill_config_file \
            LMCACHE_USE_EXPERIMENTAL=True \
            VLLM_ENABLE_V1_MULTIPROCESSING=1 \
            VLLM_WORKER_MULTIPROC_METHOD=spawn \
            CUDA_VISIBLE_DEVICES=0 \
            vllm serve $MODEL \
            --port 8100 \
            --enforce-eager \
            --kv-transfer-config \
            '}'

    elif [[ $1 == "decoder" ]]; then
        # Decoder listens on port 8200
        decode_config_file=$SCRIPT_DIR/configs/lmcache-decoder-config.yaml

        UCX_TLS=cuda_ipc,cuda_copy,tcp \
            LMCACHE_CONFIG_FILE=$decode_config_file \
            LMCACHE_USE_EXPERIMENTAL=True \
            VLLM_ENABLE_V1_MULTIPROCESSING=1 \
            VLLM_WORKER_MULTIPROC_METHOD=spawn \
            CUDA_VISIBLE_DEVICES=1 \
            vllm serve $MODEL \
            --port 8200 \
            --enforce-eager \
            --kv-transfer-config \
            '}'

    else
        echo "Invalid role: $1"
        echo "Should be either prefiller, decoder"
        exit 1
    fi

kv_cache_sharing_lmcache_v1.py

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    """
    This file demonstrates the example usage of remote KV cache sharing
    with LMCache.
    We will launch 2 vllm instances, and launch an additional LMCache server.
    KV cache is transferred in the following manner:
    (1) vLLM instance 1 -> LMCache server (KV cache store).
    (2) LMCache server -> vLLM instance 2 (KV cache reuse/retrieve).

    Note that lmcache needs to be installed to run this example.
    Learn more about LMCache in https://github.com/LMCache/LMCache.
    """

    import os
    import subprocess
    import time
    from multiprocessing import Event, Process

    from lmcache.integration.vllm.utils import ENGINE_NAME
    from lmcache.v1.cache_engine import LMCacheEngineBuilder

    from vllm import LLM, SamplingParams
    from vllm.config import KVTransferConfig

    # LMCache-related environment variables
    # The port to start LMCache server
    port = 8100
    # Use experimental features in LMCache
    os.environ["LMCACHE_USE_EXPERIMENTAL"] = "True"
    # LMCache is set to use 256 tokens per chunk
    os.environ["LMCACHE_CHUNK_SIZE"] = "256"
    # Disable local CPU backend in LMCache
    os.environ["LMCACHE_LOCAL_CPU"] = "False"
    # Set local CPU memory buffer limit to 5.0 GB
    os.environ["LMCACHE_MAX_LOCAL_CPU_SIZE"] = "5.0"
    # Set the remote URL for LMCache server
    os.environ["LMCACHE_REMOTE_URL"] = f"lm://localhost:"
    # Set the serializer/deserializer between vllm and LMCache server
    # `naive` indicates using raw bytes of the tensor without any compression
    os.environ["LMCACHE_REMOTE_SERDE"] = "naive"

    prompts = [
        "Hello, how are you?" * 1000,
    ]

    def run_store(store_done, prompts):
        # We use GPU 0 for KV cache store process.
        os.environ["CUDA_VISIBLE_DEVICES"] = "0"

        sampling_params = SamplingParams(temperature=0, top_p=0.95, max_tokens=10)

        ktc = KVTransferConfig(kv_connector="LMCacheConnectorV1", kv_role="kv_both")
        # Set GPU memory utilization to 0.8 for an A40 GPU with 40GB
        # memory. Reduce the value if your GPU has less memory.
        llm = LLM(
            model="mistralai/Mistral-7B-Instruct-v0.2",
            kv_transfer_config=ktc,
            max_model_len=8000,
            gpu_memory_utilization=0.8,
            enforce_eager=True,
        )

        outputs = llm.generate(prompts, sampling_params)
        for output in outputs:
            generated_text = output.outputs[0].text
            print(f"Generated text: ")
        print("KV cache store is finished.")
        store_done.set()

        # Clean up lmcache backend
        LMCacheEngineBuilder.destroy(ENGINE_NAME)

    def run_retrieve(store_done, prompts, timeout=1):
        # We use GPU 1 for KV cache retrieve process.
        os.environ["CUDA_VISIBLE_DEVICES"] = "1"

        sampling_params = SamplingParams(temperature=0, top_p=0.95, max_tokens=10)

        ktc = KVTransferConfig(kv_connector="LMCacheConnectorV1", kv_role="kv_both")
        # Set GPU memory utilization to 0.8 for an A40 GPU with 40GB
        # of memory. Reduce the value if your GPU has less memory.
        llm = LLM(
            model="mistralai/Mistral-7B-Instruct-v0.2",
            kv_transfer_config=ktc,
            max_model_len=8000,
            gpu_memory_utilization=0.8,
            enforce_eager=True,
        )

        print("Waiting for KV cache store to finish...")
        store_done.wait()
        time.sleep(timeout)

        outputs = llm.generate(prompts, sampling_params)
        for output in outputs:
            generated_text = output.outputs[0].text
            print(f"Generated text: ")

        # Clean up lmcache backend
        LMCacheEngineBuilder.destroy(ENGINE_NAME)

    def run_lmcache_server(port):
        server_proc = subprocess.Popen(
            ["python", "-m", "lmcache.v1.server", "localhost", str(port)]
        )
        return server_proc

    def main():
        store_done = Event()
        store_process = Process(target=run_store, args=(store_done, prompts))
        retrieve_process = Process(target=run_retrieve, args=(store_done, prompts))
        lmcache_server_process = run_lmcache_server(port)

        # Start KV cache store process
        store_process.start()

        # Start KV cache retrieve process
        retrieve_process.start()

        # Clean up the processes
        store_process.join()
        retrieve_process.terminate()
        lmcache_server_process.terminate()
        lmcache_server_process.wait()

    if __name__ == "__main__":
        main()