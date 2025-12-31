# Source: https://docs.vllm.ai/en/stable/examples/online_serving/elastic_ep/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/online_serving/elastic_ep.md "Edit this page")

# Elastic Ep[¶](#elastic-ep "Permanent link")

Source <https://github.com/vllm-project/vllm/tree/main/examples/online_serving/elastic_ep>.

## Bench[¶](#bench "Permanent link")

    #!/bin/bash

    MODEL_NAME="deepseek-ai/DeepSeek-V2-Lite"
    LOCAL_MODEL_PATH="/models/models--deepseek-ai--DeepSeek-V2-Lite/snapshots/604d5664dddd88a0433dbae533b7fe9472482de0"
    HOST="localhost"
    PORT=8006
    NUM_PROMPTS=20
    REQUEST_RATE=5

    # Parse command line arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
            --model)
                MODEL_NAME="$2"
                shift 2
                ;;
            --local-model)
                MODEL_NAME=$LOCAL_MODEL_PATH
                shift
                ;;
            --host)
                HOST="$2"
                shift 2
                ;;
            --port)
                PORT="$2"
                shift 2
                ;;
            --num-prompts)
                NUM_PROMPTS="$2"
                shift 2
                ;;
            --request-rate)
                REQUEST_RATE="$2"
                shift 2
                ;;
            -h|--help)
                echo "Usage: $0 [OPTIONS]"
                echo "Options:"
                echo "  --model MODEL_NAME           Set model name or path (default: deepseek-ai/DeepSeek-V2-Lite)"
                echo "  --local-model                Use local model path (convenience option)"
                exit 0
                ;;
            *)
                echo "Unknown option: $1"
                echo "Use -h or --help for usage information"
                exit 1
                ;;
        esac
    done

    vllm bench serve \
        --model $MODEL_NAME \
        --host $HOST \
        --port $PORT \
        --num-prompts $NUM_PROMPTS \
        --request-rate $REQUEST_RATE

## Scale[¶](#scale "Permanent link")

    #!/usr/bin/env python3
    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project

    import argparse
    import json
    import sys

    import requests

    def scale(host, port, new_dp_size):
        url = f"http://:/scale_elastic_ep"
        payload = 
        headers = 

        print(f"Sending scale request to ")
        print(f"Payload: ")

        try:
            response = requests.post(url, json=payload, headers=headers, timeout=300)

            print(f"Status Code: ")
            print(f"Response: ")

            if response.status_code == 200:
                print("Scale up/down request successful!")
                return True
            else:
                print("Scale up/down request failed!")
                return False

        except requests.exceptions.RequestException as e:
            print(f"Request failed: ")
            return False

    def main():
        parser = argparse.ArgumentParser(description="Test scale up/down functionality")
        parser.add_argument("--host", default="localhost", help="API server host")
        parser.add_argument("--port", type=int, default=8006, help="API server port")
        parser.add_argument(
            "--new-dp-size", type=int, default=2, help="New data parallel size"
        )

        args = parser.parse_args()

        success = scale(args.host, args.port, args.new_dp_size)
        sys.exit(0 if success else 1)

    if __name__ == "__main__":
        main()

## Serve Deepseek V2[¶](#serve-deepseek-v2 "Permanent link")

    #!/bin/bash

    HOST="0.0.0.0"
    PORT=8006
    DATA_PARALLEL_SIZE=4
    REDUNDANT_EXPERTS=0
    LOCAL_MODEL_PATH="/models/models--deepseek-ai--DeepSeek-V2-Lite/snapshots/604d5664dddd88a0433dbae533b7fe9472482de0"
    MODEL_NAME="deepseek-ai/DeepSeek-V2-Lite"

    while [[ $# -gt 0 ]]; do
        case $1 in
            --dp)
                DATA_PARALLEL_SIZE="$2"
                shift 2
                ;;
            --re)
                REDUNDANT_EXPERTS="$2"
                shift 2
                ;;
            --host)
                HOST="$2"
                shift 2
                ;;
            --port)
                PORT="$2"
                shift 2
                ;;
            --model)
                MODEL_NAME="$2"
                shift 2
                ;;
            --local-model)
                MODEL_NAME=$LOCAL_MODEL_PATH
                shift
                ;;
            -h|--help)
                echo "Usage: $0 [OPTIONS]"
                echo "Options:"
                echo "  --dp SIZE                    Set data parallel size (default: 4)"
                echo "  --re SIZE                    Set redundant experts (default: 0)"
                echo "  --host HOST                  Set host address (default: 0.0.0.0)"
                echo "  --port PORT                  Set port number (default: 8006)"
                echo "  --model MODEL_NAME           Set model name or path"
                echo "  -h, --help                   Show this help message"
                exit 0
                ;;
            *)
                echo "Unknown option: $1"
                echo "Use -h or --help for usage information"
                exit 1
                ;;
        esac
    done

    echo "Starting vLLM server for $MODEL_NAME with data parallel size: $DATA_PARALLEL_SIZE and redundant experts: $REDUNDANT_EXPERTS"

    export RAY_DEDUP_LOGS=0
    export VLLM_ALL2ALL_BACKEND="pplx"
    export VLLM_USE_DEEP_GEMM=1

    vllm serve $MODEL_NAME \
        --data-parallel-size $DATA_PARALLEL_SIZE \
        --data-parallel-size-local $DATA_PARALLEL_SIZE \
        --data-parallel-backend ray \
        --enforce-eager \
        --enable-expert-parallel \
        --enable-eplb \
        --num-redundant-experts $REDUNDANT_EXPERTS \
        --trust-remote-code \
        --host $HOST \
        --port $PORT