# Source: https://docs.vllm.ai/en/stable/examples/online_serving/disaggregated_encoder/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/online_serving/disaggregated_encoder.md "Edit this page")

# Disaggregated Encoder[¶](#disaggregated-encoder "Permanent link")

Source <https://github.com/vllm-project/vllm/tree/main/examples/online_serving/disaggregated_encoder>.

These example scripts that demonstrate the disaggregated encoder (EPD) features of vLLM.

For a detailed explanation of the EPD features, please refer to the [Disaggregated Encoder Feature Documentation](https://github.com/vllm-project/vllm/tree/main/docs/features/disagg_encoder.md).

## Files[¶](#files "Permanent link")

-   `disagg_epd_proxy.py` - Proxy script that demonstrates the XeYpZd setup (X encode instances, Y prefill instances, Z decode instances). Currently stable for the 1e1p1d configuration.

-   `disagg_1e1p1d_example.sh` - Sets up the 1e1p1d configuration, runs the VisionArena benchmark, and processes a single request with a local image.

-   `disagg_1e1pd_example.sh` - Sets up the 1e1pd configuration, runs the VisionArena benchmark, and processes a single request with a local image.

### Custom Configuration[¶](#custom-configuration "Permanent link")

    # Use specific GPUs
    GPU_E=0 GPU_PD=1 GPU_P=1 GPU_D=2 bash disagg_1e1p1d_example.sh

    # Use specific ports
    ENDPOINT_PORT=10001 bash disagg_1e1p1d_example.sh

    # Use specific model
    MODEL="Qwen/Qwen2.5-VL-3B-Instruct" bash disagg_1e1p1d_example.sh

    # Use specific storage path
    EC_SHARED_STORAGE_PATH="/tmp/my_ec_cache" bash disagg_1e1p1d_example.sh

## Encoder Instances[¶](#encoder-instances "Permanent link")

Encoder engines should be launched with the following flags:

-   `--enforce-eager` **(required)** -- The current EPD implementation is only compatible with encoder instances running in this mode.

-   `--no-enable-prefix-caching` **(required)** -- Encoder instances do not consume KV cache; prefix caching is disabled to avoid conflicts with other features.

-   `--max-num-batched-tokens=<large value>` **(default: 2048)** -- This flag controls the token scheduling budget per decoding step and is irrelevant to encoder-only instances. **Set it to a very high value (effectively unlimited) to bypass scheduler limitations.** The actual token budget is managed by the encoder cache manager.

## Local media inputs[¶](#local-media-inputs "Permanent link")

To support local image inputs (from your `MEDIA_PATH` directory), add the following flag to the encoder instance:

    --allowed-local-media-path $MEDIA_PATH

The vllm instances and `disagg_encoder_proxy` supports local URIs with `` as multimodal inputs. Each URI is passed unchanged from the `disagg_encoder_proxy` to the encoder instance so that the encoder can load the media locally.

## EC connector and KV transfer[¶](#ec-connector-and-kv-transfer "Permanent link")

The `ECExampleonnector` is used to store the encoder cache on local disk and facilitate transfer. To enable the encoder disaggregation feature, add the following configuration:

    # Add to encoder instance: 
    --ec-transfer-config '
    }' 

    # Add to prefill/prefill+decode instance: 
    --ec-transfer-config '
    }' 

`$EC_SHARED_STORAGE_PATH` is the path where the EC connector temporarily stores the cache.

If you enable prefill instance (`--prefill-servers-urls` not disabled), you will need \--kv-transfer-config to facilitate the PD disaggregation. Currently, we use the `NixlConnector` for this purpose. Refer to `tests/v1/kv_connector/nixl_integration` for more example codes on PD disaggregation with Nixl.

    # Add to prefill instance:    
    --kv-transfer-config '' 

    # Add to decode instance:
    --kv-transfer-config '' 

## Proxy Instance Flags (`disagg_epd_proxy.py`)[¶](#proxy-instance-flags-disagg_epd_proxypy "Permanent link") 

  Flag                       Description
  -------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------
  `--encode-servers-urls`    Comma-separated list of encoder endpoints. Every multimodal item extracted from the request is fanned out to one of these URLs in a round-robin fashion.
  `--prefill-servers-urls`   Comma-separated list of prefill endpoints. Set to `disable`, `none`, or `""` to skip the dedicated prefill phase and run E+PD (encoder + combined prefill/decode).
  `--decode-servers-urls`    Comma-separated list of decode endpoints. Non-stream and stream paths both round-robin over this list.
  `--host`, `--port`         Bind address for the proxy itself (defaults: `0.0.0.0:8000`).

Example usage: For E + PD setup:

    $ python disagg_encoder_proxy.py \
          --encode-servers-urls "http://e1:8001,http://e2:8002" \
          --prefill-servers-urls "disable" \
          --decode-servers-urls "http://pd1:8003,http://pd2:8004"

For E + P + D setup:

    $ python disagg_encoder_proxy.py \
          --encode-servers-urls "http://e1:8001,http://e2:8001" \
          --prefill-servers-urls "http://p1:8003,http://p2:8004" \ 
          --decode-servers-urls "http://d1:8005,http://d2:8006"

## Example materials[¶](#example-materials "Permanent link")

disagg_1e1p1d_example.sh

    #!/bin/bash
    set -euo pipefail

    declare -a PIDS=()

    ###############################################################################
    # Configuration -- override via env before running
    ###############################################################################
    MODEL="$"
    LOG_PATH="$"
    mkdir -p $LOG_PATH

    ENCODE_PORT="$"
    PREFILL_PORT="$"
    DECODE_PORT="$"
    PROXY_PORT="$"

    GPU_E="$"
    GPU_P="$"
    GPU_D="$"

    EC_SHARED_STORAGE_PATH="$"
    TIMEOUT_SECONDS="$"   # wait_for_server timeout

    NUM_PROMPTS="$"    # number of prompts to send in benchmark

    export UCX_TLS=all
    export UCX_NET_DEVICES=all

    ###############################################################################
    # Helpers
    ###############################################################################
    # Find the git repository root directory
    GIT_ROOT=$(git rev-parse --show-toplevel)

    START_TIME=$(date +"%Y%m%d_%H%M%S")
    ENC_LOG=$LOG_PATH/encoder_$.log
    P_LOG=$LOG_PATH/p_$.log
    D_LOG=$LOG_PATH/d_$.log
    PROXY_LOG=$LOG_PATH/proxy_$.log

    wait_for_server() 

    # Cleanup function
    cleanup() "; do
            if kill -0 "$pid" 2>/dev/null; then
                echo "Killing process $pid"
                kill "$pid" 2>/dev/null
            fi
        done

        # Wait a moment for graceful shutdown
        sleep 2

        # Force kill any remaining processes
        for pid in "$"; do
            if kill -0 "$pid" 2>/dev/null; then
                echo "Force killing process $pid"
                kill -9 "$pid" 2>/dev/null
            fi
        done

        # Kill the entire process group as backup
        kill -- -$$ 2>/dev/null

        echo "All processes stopped."
        exit 0
    }

    trap cleanup INT
    trap cleanup USR1
    trap cleanup TERM

    # clear previous cache
    echo "remove previous ec cache folder"
    rm -rf $EC_SHARED_STORAGE_PATH

    echo "make ec cache folder"
    mkdir -p $EC_SHARED_STORAGE_PATH

    ###############################################################################
    # Encoder worker
    ###############################################################################
    CUDA_VISIBLE_DEVICES="$GPU_E" vllm serve "$MODEL" \
        --gpu-memory-utilization 0.01 \
        --port "$ENCODE_PORT" \
        --enforce-eager \
        --enable-request-id-headers \
        --no-enable-prefix-caching \
        --max-num-batched-tokens 114688 \
        --max-num-seqs 128 \
        --allowed-local-media-path $/tests/v1/ec_connector/integration \
        --ec-transfer-config '
        }' \
        >"$" 2>&1 &

    PIDS+=($!)

    ###############################################################################
    # Prefill worker
    ###############################################################################
    CUDA_VISIBLE_DEVICES="$GPU_P" \
    UCX_NET_DEVICES=all \
    VLLM_NIXL_SIDE_CHANNEL_PORT=5559 \
    vllm serve "$MODEL" \
        --gpu-memory-utilization 0.7 \
        --port "$PREFILL_PORT" \
        --enforce-eager \
        --enable-request-id-headers \
        --max-num-seqs 128 \
        --allowed-local-media-path $/tests/v1/ec_connector/integration \
        --ec-transfer-config '
        }' \
        --kv-transfer-config '' \
        >"$" 2>&1 &

    PIDS+=($!)

    ###############################################################################
    # Decode worker
    ###############################################################################
    CUDA_VISIBLE_DEVICES="$GPU_D" \
    UCX_NET_DEVICES=all \
    VLLM_NIXL_SIDE_CHANNEL_PORT=6000 \
    vllm serve "$MODEL" \
        --gpu-memory-utilization 0.7 \
        --port "$DECODE_PORT" \
        --enforce-eager \
        --enable-request-id-headers \
        --max-num-seqs 128 \
        --allowed-local-media-path $/tests/v1/ec_connector/integration \
        --kv-transfer-config '' \
        >"$" 2>&1 &

    PIDS+=($!)

    # Wait for workers
    wait_for_server $ENCODE_PORT
    wait_for_server $PREFILL_PORT
    wait_for_server $DECODE_PORT

    ###############################################################################
    # Proxy
    ###############################################################################
    python disagg_epd_proxy.py \
        --host "0.0.0.0" \
        --port "$PROXY_PORT" \
        --encode-servers-urls "http://localhost:$ENCODE_PORT" \
        --prefill-servers-urls "http://localhost:$PREFILL_PORT" \
        --decode-servers-urls "http://localhost:$DECODE_PORT" \
        >"$" 2>&1 &

    PIDS+=($!)

    wait_for_server $PROXY_PORT
    echo "All services are up!"

    ###############################################################################
    # Benchmark
    ###############################################################################
    echo "Running benchmark (stream)..."
    vllm bench serve \
      --model               $MODEL \
      --backend             openai-chat \
      --endpoint            /v1/chat/completions \
      --dataset-name        hf \
      --dataset-path        lmarena-ai/VisionArena-Chat \
      --seed                0 \
      --num-prompts         $NUM_PROMPTS \
      --port                $PROXY_PORT

    PIDS+=($!)

    ###############################################################################
    # Single request with local image
    ###############################################################################
    echo "Running single request with local image (non-stream)..."
    curl http://127.0.0.1:$/v1/chat/completions \
        -H "Content-Type: application/json" \
        -d ''",
        "messages": [
        ,
        "'/tests/v1/ec_connector/integration/hato.jpg"}},
            
        ]}
        ]
        }'

    # cleanup
    echo "cleanup..."
    cleanup

disagg_1e1pd_example.sh

    #!/bin/bash
    set -euo pipefail

    declare -a PIDS=()

    ###############################################################################
    # Configuration -- override via env before running
    ###############################################################################
    MODEL="$"
    LOG_PATH="$"
    mkdir -p $LOG_PATH

    ENCODE_PORT="$"
    PREFILL_DECODE_PORT="$"
    PROXY_PORT="$"

    GPU_E="$"
    GPU_PD="$"

    EC_SHARED_STORAGE_PATH="$"
    TIMEOUT_SECONDS="$"   # wait_for_server timeout

    NUM_PROMPTS="$"    # number of prompts to send in benchmark

    ###############################################################################
    # Helpers
    ###############################################################################
    # Find the git repository root directory
    GIT_ROOT=$(git rev-parse --show-toplevel)

    START_TIME=$(date +"%Y%m%d_%H%M%S")
    ENC_LOG=$LOG_PATH/encoder_$.log
    PD_LOG=$LOG_PATH/pd_$.log
    PROXY_LOG=$LOG_PATH/proxy_$.log

    wait_for_server() 

    # Cleanup function
    cleanup() "; do
            if kill -0 "$pid" 2>/dev/null; then
                echo "Killing process $pid"
                kill "$pid" 2>/dev/null
            fi
        done

        # Wait a moment for graceful shutdown
        sleep 2

        # Force kill any remaining processes
        for pid in "$"; do
            if kill -0 "$pid" 2>/dev/null; then
                echo "Force killing process $pid"
                kill -9 "$pid" 2>/dev/null
            fi
        done

        # Kill the entire process group as backup
        kill -- -$$ 2>/dev/null

        echo "All processes stopped."
        exit 0
    }

    trap cleanup INT
    trap cleanup USR1
    trap cleanup TERM

    # clear previous cache
    echo "remove previous ec cache folder"
    rm -rf $EC_SHARED_STORAGE_PATH

    echo "make ec cache folder"
    mkdir -p $EC_SHARED_STORAGE_PATH

    ###############################################################################
    # Encoder worker
    ###############################################################################
    CUDA_VISIBLE_DEVICES="$GPU_E" vllm serve "$MODEL" \
        --gpu-memory-utilization 0.01 \
        --port "$ENCODE_PORT" \
        --enforce-eager \
        --enable-request-id-headers \
        --no-enable-prefix-caching \
        --max-num-batched-tokens 114688 \
        --max-num-seqs 128 \
        --allowed-local-media-path $/tests/v1/ec_connector/integration \
        --ec-transfer-config '
        }' \
        >"$" 2>&1 &

    PIDS+=($!)

    ###############################################################################
    # Prefill+Decode worker
    ###############################################################################
    CUDA_VISIBLE_DEVICES="$GPU_PD" vllm serve "$MODEL" \
        --gpu-memory-utilization 0.7 \
        --port "$PREFILL_DECODE_PORT" \
        --enforce-eager \
        --enable-request-id-headers \
        --max-num-seqs 128 \
        --allowed-local-media-path $/tests/v1/ec_connector/integration \
        --ec-transfer-config '
        }' \
        >"$" 2>&1 &

    PIDS+=($!)

    # Wait for workers
    wait_for_server $ENCODE_PORT
    wait_for_server $PREFILL_DECODE_PORT

    ###############################################################################
    # Proxy
    ###############################################################################
    python disagg_epd_proxy.py \
        --host "0.0.0.0" \
        --port "$PROXY_PORT" \
        --encode-servers-urls "http://localhost:$ENCODE_PORT" \
        --prefill-servers-urls "disable" \
        --decode-servers-urls "http://localhost:$PREFILL_DECODE_PORT" \
        >"$" 2>&1 &

    PIDS+=($!)

    wait_for_server $PROXY_PORT
    echo "All services are up!"

    ###############################################################################
    # Benchmark
    ###############################################################################
    echo "Running benchmark (stream)..."
    vllm bench serve \
      --model               $MODEL \
      --backend             openai-chat \
      --endpoint            /v1/chat/completions \
      --dataset-name        hf \
      --dataset-path        lmarena-ai/VisionArena-Chat \
      --seed                0 \
      --num-prompts         $NUM_PROMPTS \
      --port                $PROXY_PORT

    PIDS+=($!)

    ###############################################################################
    # Single request with local image
    ###############################################################################
    echo "Running single request with local image (non-stream)..."
    curl http://127.0.0.1:$/v1/chat/completions \
        -H "Content-Type: application/json" \
        -d ''",
        "messages": [
        ,
        "'/tests/v1/ec_connector/integration/hato.jpg"}},
            
        ]}
        ]
        }'

    # cleanup
    echo "cleanup..."
    cleanup

disagg_epd_proxy.py

    #!/usr/bin/env python3
    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    """
    disagg_encoder_proxy.py

    Proxy that routes OpenAI-compatible “/v1/chat/completions” requests to two
    clusters:
      • encode  (multimodal feature extraction)
      • decode  (language-model inference)

    For MM input we:
        1. Extract *every* image/audio item.
        2. Fire N concurrent requests to the encoder cluster
           (one request per item, with **all text removed**).
        3. Wait for all of them to succeed.
        4. Forward the *original* request to a decode server.
    """

    from __future__ import annotations

    import argparse
    import asyncio
    import logging
    import os
    import random
    import uuid
    from collections.abc import AsyncIterator

    import aiohttp
    import uvicorn
    from fastapi import FastAPI, HTTPException, Request
    from fastapi.responses import JSONResponse, StreamingResponse

    ###############################################################################
    # FastAPI app & global state
    ###############################################################################

    logging.basicConfig(
        level=logging.DEBUG, format="%(asctime)s %(levelname)s: %(message)s"
    )
    logger = logging.getLogger("proxy")

    app = FastAPI()
    encode_session: aiohttp.ClientSession | None = None
    prefill_session: aiohttp.ClientSession | None = None
    decode_session: aiohttp.ClientSession | None = None

    ###############################################################################
    # Utils
    ###############################################################################

    MM_TYPES = 

    def extract_mm_items(request_data: dict) -> list[dict]:
        """
        Return *all* image/audio items that appear anywhere in `messages`.

        Each returned dict looks like:
             }
        """
        items: list[dict] = []
        for msg in request_data.get("messages", []):
            content = msg.get("content")
            if not isinstance(content, list):
                continue

            for item in content:
                if item.get("type") in MM_TYPES:
                    items.append(item)
        return items

    async def fanout_encoder_primer(
        orig_request: dict,
        e_urls: list[str],
        req_id: str,
    ) -> None:
        """
        1. Build one request *per MM item* with all text removed.
        2. Send them concurrently to the encode cluster.
        3. Raise if any of them fails.
        """
        logger.info("[%s] Processing multimodal items...", req_id)

        mm_items = extract_mm_items(orig_request)
        if not mm_items:
            logger.info("[%s] No multimodal items, skipping encoder", req_id)
            return  # nothing to do

        logger.info("[%s] got %d multimodal items...", req_id, len(mm_items))

        tasks = []

        # Round-robin over encode servers to distribute load a bit
        url_cycle = (e_urls[i % len(e_urls)] for i in range(len(mm_items)))

        for idx, (item, target_url) in enumerate(zip(mm_items, url_cycle)):
            # Derive a *child* request id:  <parent>:<index>:<random-short>
            child_req_id = f"::"
            headers = 

            encoder_req = ,
                ],
                # Only need 1 token so the server actually runs the encoder path
                "max_tokens": 1,
                "stream": False,
            }
            tasks.append(
                encode_session.post(
                    f"/v1/chat/completions",
                    json=encoder_req,
                    headers=headers,
                )
            )

        results = await asyncio.gather(*tasks, return_exceptions=True)

        # Fail fast if any sub-request failed
        for idx, r in enumerate(results):
            if isinstance(r, Exception):
                logger.error(
                    "[%s] Encoder request #%d raised exception: %s",
                    req_id,
                    idx,
                    r,
                    exc_info=r,
                )
                raise HTTPException(
                    status_code=502, detail=f"Encoder request failed: "
                )
            if r.status != 200:
                try:
                    detail = await r.text()
                except Exception:
                    detail = "<unable to read body>"
                logger.error(
                    "[%s] Encoder request #%d returned status %s: %s",
                    req_id,
                    idx,
                    r.status,
                    detail,
                )
                raise HTTPException(
                    status_code=r.status,
                    detail=f"Encoder request failed: ",
                )

        logger.info(
            "[%s] All %d encoder requests completed successfully", req_id, len(mm_items)
        )

    async def maybe_prefill(
        req_data: dict,
        p_url: str,
        req_id: str,
    ) -> dict:
        """
        - Do prefill-only task if p_url exist;
        - Return modified request data with kv transfer params (for nixl connector)
        - Else, skip and return the original request data for decode
        """
        if p_url:
            logger.info("[%s] Processing through prefill: %s", req_id, p_url)

            prefill_response = await process_prefill_stage(req_data, p_url, req_id)
            # for nixl connector to facilitate kv transfer...
            prefill_response_json = await prefill_response.json()
            kv_transfer_params = prefill_response_json.get("kv_transfer_params", )
            if kv_transfer_params:
                req_data["kv_transfer_params"] = kv_transfer_params

            return req_data
        else:
            return req_data

    async def process_prefill_stage(
        req_data: dict,
        p_url: str,
        req_id: str,
    ) -> dict:
        """Process request through Prefill stage and return kv_transfer_params"""
        logger.info("[%s] Sending prefill request to: %s", req_id, p_url)

        prefill_request = req_data.copy()
        prefill_request["kv_transfer_params"] = 
        prefill_request["stream"] = False
        prefill_request["max_tokens"] = 1
        if "max_completion_tokens" in prefill_request:
            prefill_request["max_completion_tokens"] = 1
        if "stream_options" in prefill_request:
            del prefill_request["stream_options"]

        headers = 
        try:
            prefill_response = await prefill_session.post(
                f"/v1/chat/completions", json=prefill_request, headers=headers
            )
            prefill_response.raise_for_status()

            if prefill_response.status != 200:
                error_text = await prefill_response.text()
                logger.error(
                    "[%s] Prefill request failed with status %d: %s",
                    req_id,
                    prefill_response.status,
                    error_text,
                )
                raise HTTPException(
                    status_code=prefill_response.status,
                    detail=,
                )
            logger.info("[%s] Prefill request completed successfully", req_id)

            return prefill_response

        except Exception as e:
            logger.error("Prefill processing failed: %s", str(e))
            raise HTTPException(
                status_code=500,
                detail=,
            ) from e

    ###############################################################################
    # Middleware for request/response logging
    ###############################################################################

    @app.middleware("http")
    async def log_requests(request: Request, call_next):
        """Middleware to log all incoming requests and responses"""
        req_id = request.headers.get("x-request-id", str(uuid.uuid4()))

        # Log incoming request
        logger.info(
            ">>> [%s] %s %s from %s",
            req_id,
            request.method,
            request.url.path,
            request.client.host if request.client else "unknown",
        )

        try:
            # Process request
            response = await call_next(request)

            # Log response
            logger.info(
                "<<< [%s] %s %s completed with status %d",
                req_id,
                request.method,
                request.url.path,
                response.status_code,
            )

            return response
        except Exception as e:
            # Log errors
            logger.exception(
                "!!! [%s] %s %s failed with error: %s",
                req_id,
                request.method,
                request.url.path,
                str(e),
            )
            raise

    ###############################################################################
    # FastAPI lifecycle
    ###############################################################################

    @app.on_event("startup")
    async def on_startup() -> None:
        global encode_session, prefill_session, decode_session
        timeout = aiohttp.ClientTimeout(total=100_000)
        connector = aiohttp.TCPConnector(limit=0, force_close=False)
        encode_session = aiohttp.ClientSession(timeout=timeout, connector=connector)
        if app.state.p_urls:
            # only setup if prefill instance(s) exist
            prefill_session = aiohttp.ClientSession(timeout=timeout, connector=connector)
        decode_session = aiohttp.ClientSession(timeout=timeout, connector=connector)

    @app.on_event("shutdown")
    async def on_shutdown() -> None:
        global encode_session, prefill_session, decode_session
        if encode_session:
            await encode_session.close()
        if prefill_session:
            await prefill_session.close()
        if decode_session:
            await decode_session.close()

    ###############################################################################
    # Core forwarding
    ###############################################################################

    async def forward_non_stream(
        req_data: dict, req_id: str, e_urls: list[str], p_url: str, d_url: str
    ) -> dict:
        try:
            # Step 1: Process through Encoder instance (if has MM input)
            await fanout_encoder_primer(req_data, e_urls, req_id)

            # Step 2: Process through Prefill instance
            req_data = await maybe_prefill(req_data, p_url, req_id)

            # Step 3: Process through Decode instance
            logger.info("[%s] Forwarding to decode: %s", req_id, d_url)
            headers = 

            # Non-streaming response
            async with decode_session.post(
                f"/v1/chat/completions", json=req_data, headers=headers
            ) as resp:
                resp.raise_for_status()
                return await resp.json()

        except HTTPException:
            raise
        except Exception as e:
            logger.exception("[%s] Error in forward_non_stream: %s", req_id, str(e))
            raise HTTPException(status_code=500, detail=f"Proxy error: ") from e

    async def forward_stream(
        req_data: dict, req_id: str, e_urls: list[str], p_url: str, d_url: str
    ) -> AsyncIterator[str]:
        try:
            # Step 1: Process through Encoder instance (if has MM input)
            await fanout_encoder_primer(req_data, e_urls, req_id)

            # Step 2: Process through Prefill instance
            req_data = await maybe_prefill(req_data, p_url, req_id)

            # Step 3: Process through Decode instance
            logger.info("[%s] Starting streaming from decode: %s", req_id, d_url)
            headers = 

            # Streaming response
            async with decode_session.post(
                f"/v1/chat/completions",
                json=req_data,
                headers=headers,
            ) as resp:
                resp.raise_for_status()
                async for chunk in resp.content.iter_chunked(1024):
                    if chunk:
                        yield chunk.decode("utf-8", errors="ignore")

            logger.info("[%s] Streaming completed", req_id)

        except HTTPException:
            logger.exception("[%s] HTTPException in forward_stream", req_id)
            raise
        except Exception as e:
            logger.exception("[%s] Error in forward_stream: %s", req_id, str(e))
            raise HTTPException(
                status_code=500, detail=f"Proxy streaming error: "
            ) from e

    ###############################################################################
    # Public routes
    ###############################################################################

    @app.post("/v1/chat/completions")
    async def chat_completions(request: Request):
        try:
            req_data = await request.json()
            req_id = request.headers.get("x-request-id", str(uuid.uuid4()))

            e_urls = app.state.e_urls  # we want the full list for fan-out
            p_url = random.choice(app.state.p_urls) if app.state.p_urls else None
            d_url = random.choice(app.state.d_urls)

            is_streaming = req_data.get("stream", False)

            if is_streaming:
                return StreamingResponse(
                    forward_stream(req_data, req_id, e_urls, p_url, d_url),
                    media_type="text/event-stream",
                )
            result = await forward_non_stream(req_data, req_id, e_urls, p_url, d_url)
            return JSONResponse(content=result)

        except HTTPException:
            raise
        except Exception as e:
            logger.exception("Error in chat_completions endpoint: %s", str(e))
            raise HTTPException(
                status_code=500, detail=f"Request processing error: "
            ) from e

    @app.get("/v1/models")
    async def list_models():
        async with decode_session.get(f"/v1/models") as resp:
            resp.raise_for_status()
            return await resp.json()

    @app.get("/health")
    async def health_check():
        async def healthy(urls):
            if not urls:
                return "empty"
            for u in urls:
                try:
                    async with encode_session.get(f"/health") as resp:
                        resp.raise_for_status()
                except Exception:
                    return "unhealthy"
            return "healthy"

        e_status, p_status, d_status = await asyncio.gather(
            healthy(app.state.e_urls), healthy(app.state.p_urls), healthy(app.state.d_urls)
        )

        overall_healthy = all(
            status != "unhealthy" for status in (e_status, p_status, d_status)
        )

        status_code = 200 if overall_healthy else 503

        return JSONResponse(
            ,
            status_code=status_code,
        )

    ###############################################################################
    # Simple profiler fan-out (unchanged except for sessions)
    ###############################################################################

    async def _post_if_available(
        session: aiohttp.ClientSession,
        url: str,
        payload: dict,
        headers: dict,
    ) -> dict | None:
        """
        POST `payload` to `url`.

        Returns
        -------
        • The decoded JSON body on success (2xx)
        • None if the endpoint does not exist (404)
        • Raises for anything else.
        """
        try:
            resp = await session.post(url, json=payload, headers=headers)
            if resp.status == 404:  # profiling disabled on that server
                logger.warning("Profiling endpoint missing on %s", url)
                return None
            resp.raise_for_status()
            return await resp.json(content_type=None)
        except aiohttp.ClientResponseError as exc:
            # Pass 404 through the branch above, re-raise everything else
            if exc.status == 404:
                logger.warning("Profiling endpoint missing on %s", url)
                return None
            raise
        except Exception:
            # Network errors etc.: propagate
            raise

    async def _profile_cmd(cmd: str, payload: dict, e_url: str, p_url: str, d_url: str):
        """
        Fire & forget to both clusters, tolerate 404.
        """
        headers = "}

        encode_task = _post_if_available(
            encode_session, f"/_profile", payload, headers
        )
        prefill_task = (
            _post_if_available(prefill_session, f"/_profile", payload, headers)
            if p_url is not None
            else asyncio.sleep(0)
        )
        decode_task = _post_if_available(
            decode_session, f"/_profile", payload, headers
        )

        encode_res, prefill_res, decode_res = await asyncio.gather(
            encode_task, prefill_task, decode_task
        )

        # If *all* clusters said “I don’t have that route”, surface an error
        if encode_res is prefill_res is decode_res is None:
            raise HTTPException(
                status_code=503,
                detail="Profiling endpoints are disabled on all clusters",
            )

        return 

    @app.post("/start_profile")
    async def start_profile(request: Request):
        body = await request.json()
        # TODO: handle multi urls properly
        e_url = random.choice(app.state.e_urls)
        p_url = random.choice(app.state.p_urls) if app.state.p_urls else None
        d_url = random.choice(app.state.d_urls)
        return await _profile_cmd("start", body, e_url, p_url, d_url)

    @app.post("/stop_profile")
    async def stop_profile(request: Request):
        body = await request.json()
        # TODO: handle multi urls properly
        e_url = random.choice(app.state.e_urls)
        p_url = random.choice(app.state.p_urls) if app.state.p_urls else None
        d_url = random.choice(app.state.d_urls)
        return await _profile_cmd("stop", body, e_url, p_url, d_url)

    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("--host", default="0.0.0.0")
        parser.add_argument("--port", type=int, default=8000)
        parser.add_argument(
            "--encode-servers-urls",
            required=True,
            help='Comma-separated encode URLs ("http://e1:8001,http://e2:8001")',
        )
        parser.add_argument(
            "--prefill-servers-urls",
            required=True,
            help=(
                'Comma-separated prefill URLs ("http://p1:8003,http://p2:8004") ',
                'to enable E->P->D, set "disable" or "none" to enable E->PD',
            ),
        )
        parser.add_argument(
            "--decode-servers-urls",
            required=True,
            help='Comma-separated decode URLs ("http://d1:8005,http://d2:8006")',
        )

        args = parser.parse_args()
        app.state.e_urls = [
            u.strip() for u in args.encode_servers_urls.split(",") if u.strip()
        ]
        app.state.d_urls = [
            u.strip() for u in args.decode_servers_urls.split(",") if u.strip()
        ]
        # handle prefill instances
        if args.prefill_servers_urls.lower() in ("disable", "none", ""):
            app.state.p_urls = []
            logger.info(
                "Disaggregated prefill phase explicitly disabled by user. Running E + PD..."
            )
        else:
            app.state.p_urls = [
                u.strip() for u in args.prefill_servers_urls.split(",") if u.strip()
            ]
            logger.info("Disaggregated prefill phase is enabled. Running E + P + D...")

        logger.info("Proxy listening on %s:%s", args.host, args.port)
        logger.info("Encode servers: %s", app.state.e_urls)
        logger.info("Prefill instances %s", app.state.p_urls)
        logger.info("Decode servers: %s", app.state.d_urls)

        uvicorn.run(
            app,
            host=args.host,
            port=args.port,
            log_level="info",
            loop="uvloop",
            access_log=True,
        )