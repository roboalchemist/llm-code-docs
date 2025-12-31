# Source: https://docs.vllm.ai/en/stable/examples/online_serving/disaggregated_prefill/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/online_serving/disaggregated_prefill.md "Edit this page")

# Disaggregated Prefill[¶](#disaggregated-prefill "Permanent link")

Source <https://github.com/vllm-project/vllm/blob/main/examples/online_serving/disaggregated_prefill.sh>.

    #!/bin/bash
    # This file demonstrates the example usage of disaggregated prefilling
    # We will launch 2 vllm instances (1 for prefill and 1 for decode),
    # and then transfer the KV cache between them.

    set -xe

    echo "🚧🚧 Warning: The usage of disaggregated prefill is experimental and subject to change 🚧🚧"
    sleep 1

    # meta-llama/Meta-Llama-3.1-8B-Instruct or deepseek-ai/DeepSeek-V2-Lite
    MODEL_NAME=$

    # Trap the SIGINT signal (triggered by Ctrl+C)
    trap 'cleanup' INT

    # Cleanup function
    cleanup() 

    if [[ -z "$" ]]; then
        export VLLM_HOST_IP=127.0.0.1
        echo "Using default VLLM_HOST_IP=127.0.0.1 (override by exporting VLLM_HOST_IP before running this script)"
    else
        echo "Using provided VLLM_HOST_IP=$"
    fi

    # install quart first -- required for disagg prefill proxy serve
    if python3 -c "import quart" &> /dev/null; then
        echo "Quart is already installed."
    else
        echo "Quart is not installed. Installing..."
        python3 -m pip install quart
    fi 

    # a function that waits vLLM server to start
    wait_for_server() /v1/models > /dev/null; do
          sleep 1
        done" && return 0 || return 1
    }

    # You can also adjust --kv-ip and --kv-port for distributed inference.

    # prefilling instance, which is the KV producer
    CUDA_VISIBLE_DEVICES=0 vllm serve $MODEL_NAME \
        --host 0.0.0.0 \
        --port 8100 \
        --max-model-len 100 \
        --gpu-memory-utilization 0.8 \
        --trust-remote-code \
        --kv-transfer-config \
        '}' &

    # decoding instance, which is the KV consumer  
    CUDA_VISIBLE_DEVICES=1 vllm serve $MODEL_NAME \
        --host 0.0.0.0 \
        --port 8200 \
        --max-model-len 100 \
        --gpu-memory-utilization 0.8 \
        --trust-remote-code \
        --kv-transfer-config \
        '}' &

    # wait until prefill and decode instances are ready
    wait_for_server 8100
    wait_for_server 8200

    # launch a proxy server that opens the service at port 8000
    # the workflow of this proxy:
    # - send the request to prefill vLLM instance (port 8100), change max_tokens 
    #   to 1
    # - after the prefill vLLM finishes prefill, send the request to decode vLLM 
    #   instance
    # NOTE: the usage of this API is subject to change --- in the future we will 
    # introduce "vllm connect" to connect between prefill and decode instances
    python3 ../../benchmarks/disagg_benchmarks/disagg_prefill_proxy_server.py &
    sleep 1

    # serve two example requests
    output1=$(curl -X POST -s http://localhost:8000/v1/completions \
    -H "Content-Type: application/json" \
    -d '')

    output2=$(curl -X POST -s http://localhost:8000/v1/completions \
    -H "Content-Type: application/json" \
    -d '')

    # Cleanup commands
    pgrep python | xargs kill -9
    pkill -f python

    echo ""

    sleep 1

    # Print the outputs of the curl requests
    echo ""
    echo "Output of first request: $output1"
    echo "Output of second request: $output2"

    echo "🎉🎉 Successfully finished 2 test requests! 🎉🎉"
    echo ""