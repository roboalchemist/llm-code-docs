# Source: https://docs.vllm.ai/en/stable/features/mooncake_connector_usage/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/features/mooncake_connector_usage.md "Edit this page")

# MooncakeConnector Usage Guide[¶](#mooncakeconnector-usage-guide "Permanent link")

## About Mooncake[¶](#about-mooncake "Permanent link")

Mooncake aims to enhance the inference efficiency of large language models (LLMs), especially in slow object storage environments, by constructing a multi-level caching pool on high-speed interconnected DRAM/SSD resources. Compared to traditional caching systems, Mooncake utilizes (GPUDirect) RDMA technology to transfer data directly in a zero-copy manner, while maximizing the use of multi-NIC resources on a single machine.

For more details about Mooncake, please refer to [Mooncake project](https://github.com/kvcache-ai/Mooncake) and [Mooncake documents](https://kvcache-ai.github.io/Mooncake/).

## Prerequisites[¶](#prerequisites "Permanent link")

### Installation[¶](#installation "Permanent link")

Install mooncake through pip: `uv pip install mooncake-transfer-engine`.

Refer to [Mooncake official repository](https://github.com/kvcache-ai/Mooncake) for more installation instructions

## Usage[¶](#usage "Permanent link")

### Prefiller Node (192.168.0.2)[¶](#prefiller-node-19216802 "Permanent link") 

    vllm serve Qwen/Qwen2.5-7B-Instruct --port 8010 --kv-transfer-config ''

### Decoder Node (192.168.0.3)[¶](#decoder-node-19216803 "Permanent link") 

    vllm serve Qwen/Qwen2.5-7B-Instruct --port 8020 --kv-transfer-config ''

### Proxy[¶](#proxy "Permanent link")

    python tests/v1/kv_connector/nixl_integration/toy_proxy_server.py --prefiller-host 192.168.0.2 --prefiller-port 8010 --decoder-host 192.168.0.3 --decoder-port 8020

> NOTE: The Mooncake Connector currently uses the proxy from nixl_integration. This will be replaced with a self-developed proxy in the future.

Now you can send requests to the proxy server through port 8000.

## Environment Variables[¶](#environment-variables "Permanent link")

-   `VLLM_MOONCAKE_BOOTSTRAP_PORT`: Port for Mooncake bootstrap server

    -   Default: 8998
    -   Required only for prefiller instances
    -   Each vLLM worker needs a unique port on its host; using the same port number across different hosts is fine
    -   For TP/DP deployments, each worker\'s port on a node is computed as: base_port + dp_rank \* tp_size + tp_rank
    -   Used for the decoder notifying the prefiller

-   `VLLM_MOONCAKE_ABORT_REQUEST_TIMEOUT`: Timeout (in seconds) for automatically releasing the prefiller's KV cache for a particular request. (Optional)

    -   Default: 480
    -   If a request is aborted and the decoder has not yet notified the prefiller, the prefill instance will release its KV-cache blocks after this timeout to avoid holding them indefinitely.

## KV Role Options[¶](#kv-role-options "Permanent link")

-   **kv_producer**: For prefiller instances that generate KV caches
-   **kv_consumer**: For decoder instances that consume KV caches from prefiller
-   **kv_both**: Enables symmetric functionality where the connector can act as both producer and consumer. This provides flexibility for experimental setups and scenarios where the role distinction is not predetermined.

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [December 4, 2025] ]