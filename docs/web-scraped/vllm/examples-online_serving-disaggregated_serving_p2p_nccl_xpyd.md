# Source: https://docs.vllm.ai/en/stable/examples/online_serving/disaggregated_serving_p2p_nccl_xpyd/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/online_serving/disaggregated_serving_p2p_nccl_xpyd.md "Edit this page")

# Disaggregated Serving P2P Nccl Xpyd[¶](#disaggregated-serving-p2p-nccl-xpyd "Permanent link")

Source <https://github.com/vllm-project/vllm/tree/main/examples/online_serving/disaggregated_serving_p2p_nccl_xpyd>.

## Disagg Example P2P Nccl Xpyd[¶](#disagg-example-p2p-nccl-xpyd "Permanent link")

    #!/bin/bash

    # =============================================================================
    # vLLM Disaggregated Serving Script - P2P NCCL XpYd Architecture
    # =============================================================================
    # This script demonstrates disaggregated prefill and decode serving using
    # P2P NCCL communication. The architecture supports various XpYd configurations:
    #
    # - 1P3D: 1 Prefill server + 3 Decode servers (current default)
    # - 3P1D: 3 Prefill servers + 1 Decode server
    # - etc.
    #
    # Configuration can be customized via environment variables:
    #   MODEL: Model to serve
    #   PREFILL_GPUS: Comma-separated GPU IDs for prefill servers
    #   DECODE_GPUS: Comma-separated GPU IDs for decode servers
    #   PREFILL_PORTS: Comma-separated ports for prefill servers
    #   DECODE_PORTS: Comma-separated ports for decode servers
    #   PROXY_PORT: Proxy server port used to setup XpYd connection.
    #   TIMEOUT_SECONDS: Server startup timeout
    # =============================================================================

    # Configuration - can be overridden via environment variables
    MODEL=$
    TIMEOUT_SECONDS=$
    PROXY_PORT=$

    # Default 1P3D configuration (1 Prefill + 3 Decode)
    PREFILL_GPUS=$
    DECODE_GPUS=$
    PREFILL_PORTS=$
    DECODE_PORTS=$

    echo "Warning: P2P NCCL disaggregated prefill XpYd support for vLLM v1 is experimental and subject to change."
    echo ""
    echo "Architecture Configuration:"
    echo "  Model: $MODEL"
    echo "  Prefill GPUs: $PREFILL_GPUS, Ports: $PREFILL_PORTS"
    echo "  Decode GPUs: $DECODE_GPUS, Ports: $DECODE_PORTS"
    echo "  Proxy Port: $PROXY_PORT"
    echo "  Timeout: $s"
    echo ""

    PIDS=()

    # Switch to the directory of the current script
    cd "$(dirname "$")"

    check_required_files() "; do
            if [[ ! -f "$file" ]]; then
                echo "Required file $file not found in $(pwd)"
                exit 1
            fi
        done
    }

    check_hf_token() 

    check_num_gpus() 

    ensure_python_library_installed() 

    cleanup() 

    wait_for_server() /v1/completions" > /dev/null; then
          echo "Server on port $port is ready."
          return 0
        fi

        local now=$(date +%s)
        if (( now - start_time >= timeout_seconds )); then
          echo "Timeout waiting for server on port $port"
          return 1
        fi

        sleep 1
      done
    }

    main()  prefill server(s)..."
        for i in "$"; do
            local gpu_id=$
            local port=$
            local kv_port=$((21001 + i))

            echo "  Prefill server $((i+1)): GPU $gpu_id, Port $port, KV Port $kv_port"
            CUDA_VISIBLE_DEVICES=$gpu_id vllm serve $MODEL \
            --enforce-eager \
            --host 0.0.0.0 \
            --port $port \
            --tensor-parallel-size 1 \
            --seed 1024 \
            --dtype float16 \
            --max-model-len 10000 \
            --max-num-batched-tokens 10000 \
            --max-num-seqs 256 \
            --trust-remote-code \
            --gpu-memory-utilization 0.9 \
            --kv-transfer-config \
            "}" > prefill$((i+1)).log 2>&1 &
            PIDS+=($!)
        done

        # =============================================================================
        # Launch Decode Servers (Y Decoders)
        # =============================================================================
        echo ""
        echo "Starting $ decode server(s)..."
        for i in "$"; do
            local gpu_id=$
            local port=$
            local kv_port=$((22001 + i))

            echo "  Decode server $((i+1)): GPU $gpu_id, Port $port, KV Port $kv_port"
            CUDA_VISIBLE_DEVICES=$gpu_id vllm serve $MODEL \
            --enforce-eager \
            --host 0.0.0.0 \
            --port $port \
            --tensor-parallel-size 1 \
            --seed 1024 \
            --dtype float16 \
            --max-model-len 10000 \
            --max-num-batched-tokens 10000 \
            --max-num-seqs 256 \
            --trust-remote-code \
            --gpu-memory-utilization 0.7 \
            --kv-transfer-config \
            "}" > decode$((i+1)).log 2>&1 &
            PIDS+=($!)
        done

        # =============================================================================
        # Wait for All Servers to Start
        # =============================================================================
        echo ""
        echo "Waiting for all servers to start..."
        for port in "$" "$"; do
            if ! wait_for_server $port; then
                echo "Failed to start server on port $port"
                cleanup
                exit 1
            fi
        done

        echo ""
        echo "All servers are up. Starting benchmark..."

        # =============================================================================
        # Run Benchmark
        # =============================================================================
        cd ../../../benchmarks/
        vllm bench serve --port 10001 --seed $(date +%s) \
            --model $MODEL \
            --dataset-name random --random-input-len 7500 --random-output-len 200 \
            --num-prompts 200 --burstiness 100 --request-rate 2 | tee benchmark.log

        echo "Benchmarking done. Cleaning up..."

        cleanup
    }

    main

## Disagg Proxy P2P Nccl Xpyd[¶](#disagg-proxy-p2p-nccl-xpyd "Permanent link")

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project

    import os
    import socket
    import threading
    import time
    import uuid
    from typing import Any

    import aiohttp
    import msgpack
    import zmq
    from quart import Quart, make_response, request

    count = 0
    prefill_instances: dict[str, Any] =   # http_address: (zmq_address, stamp)
    decode_instances: dict[str, Any] =   # http_address: (zmq_address, stamp)

    prefill_cv = threading.Condition()
    decode_cv = threading.Condition()

    DEFAULT_PING_SECONDS = 5

    def _remove_oldest_instances(instances: dict[str, Any]) -> None:
        oldest_key = next(iter(instances), None)
        while oldest_key is not None:
            value = instances[oldest_key]
            if value[1] > time.time():
                break
            print(f"🔴Remove [HTTP:, ZMQ:, stamp:]")
            instances.pop(oldest_key, None)
            oldest_key = next(iter(instances), None)

    def _listen_for_register(poller, router_socket):
        while True:
            socks = dict(poller.poll())
            if router_socket in socks:
                remote_address, message = router_socket.recv_multipart()
                # data: 
                data = msgpack.loads(message)
                if data["type"] == "P":
                    global prefill_instances
                    global prefill_cv
                    with prefill_cv:
                        node = prefill_instances.get(data["http_address"], None)
                        prefill_instances[data["http_address"]] = (
                            data["zmq_address"],
                            time.time() + DEFAULT_PING_SECONDS,
                        )
                        _remove_oldest_instances(prefill_instances)

                elif data["type"] == "D":
                    global decode_instances
                    global decode_cv
                    with decode_cv:
                        node = decode_instances.get(data["http_address"], None)
                        decode_instances[data["http_address"]] = (
                            data["zmq_address"],
                            time.time() + DEFAULT_PING_SECONDS,
                        )
                        _remove_oldest_instances(decode_instances)
                else:
                    print(
                        "Unexpected, Received message from %s, data: %s",
                        remote_address,
                        data,
                    )
                    return

                if node is None:
                    print(f"🔵Add [HTTP:, ZMQ:]")

    def start_service_discovery(hostname, port):
        if not hostname:
            hostname = socket.gethostname()
        if port == 0:
            raise ValueError("Port cannot be 0")

        context = zmq.Context()
        router_socket = context.socket(zmq.ROUTER)
        router_socket.bind(f"tcp://:")

        poller = zmq.Poller()
        poller.register(router_socket, zmq.POLLIN)

        _listener_thread = threading.Thread(
            target=_listen_for_register, args=[poller, router_socket], daemon=True
        )
        _listener_thread.start()
        return _listener_thread

    AIOHTTP_TIMEOUT = aiohttp.ClientTimeout(total=6 * 60 * 60)

    app = Quart(__name__)

    def random_uuid() -> str:
        return str(uuid.uuid4().hex)

    async def forward_request(url, data, request_id):
        async with aiohttp.ClientSession(timeout=AIOHTTP_TIMEOUT) as session:
            headers = ",
                "X-Request-Id": request_id,
            }
            async with session.post(url=url, json=data, headers=headers) as response:
                if response.status == 200:
                    if True:
                        async for chunk_bytes in response.content.iter_chunked(1024):
                            yield chunk_bytes
                    else:
                        content = await response.read()
                        yield content

    @app.route("/v1/completions", methods=["POST"])
    @app.route("/v1/chat/completions", methods=["POST"])
    async def handle_request():
        try:
            original_request_data = await request.get_json()

            prefill_request = original_request_data.copy()
            # change max_tokens = 1 to let it only do prefill
            prefill_request["max_tokens"] = 1
            if "max_completion_tokens" in prefill_request:
                prefill_request["max_completion_tokens"] = 1

            global count
            global prefill_instances
            global prefill_cv
            with prefill_cv:
                prefill_list = list(prefill_instances.items())
                prefill_addr, prefill_zmq_addr = prefill_list[count % len(prefill_list)]
                prefill_zmq_addr = prefill_zmq_addr[0]

            global decode_instances
            global decode_cv
            with decode_cv:
                decode_list = list(decode_instances.items())
                decode_addr, decode_zmq_addr = decode_list[count % len(decode_list)]
                decode_zmq_addr = decode_zmq_addr[0]

            print(
                f"handle_request count: , [HTTP:, "
                f"ZMQ:] 👉 [HTTP:, "
                f"ZMQ:]"
            )
            count += 1

            request_id = (
                f"___prefill_addr____decode_addr_"
                f"_"
            )

            # finish prefill
            async for _ in forward_request(
                f"http://", prefill_request, request_id
            ):
                continue

            # return decode
            generator = forward_request(
                f"http://", original_request_data, request_id
            )
            response = await make_response(generator)
            response.timeout = None

            return response

        except Exception as e:
            import sys
            import traceback

            exc_info = sys.exc_info()
            print("Error occurred in disagg prefill proxy server")
            print(e)
            print("".join(traceback.format_exception(*exc_info)))

    if __name__ == "__main__":
        t = start_service_discovery("0.0.0.0", 30001)
        app.run(host="0.0.0.0", port=10001)
        t.join()