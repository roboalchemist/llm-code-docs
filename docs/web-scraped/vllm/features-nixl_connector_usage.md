# Source: https://docs.vllm.ai/en/stable/features/nixl_connector_usage/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/features/nixl_connector_usage.md "Edit this page")

# NixlConnector Usage Guide[¶](#nixlconnector-usage-guide "Permanent link")

NixlConnector is a high-performance KV cache transfer connector for vLLM\'s disaggregated prefilling feature. It provides fully asynchronous send/receive operations using the NIXL library for efficient cross-process KV cache transfer.

## Prerequisites[¶](#prerequisites "Permanent link")

### Installation[¶](#installation "Permanent link")

Install the NIXL library: `uv pip install nixl`, as a quick start.

-   Refer to [NIXL official repository](https://github.com/ai-dynamo/nixl) for more installation instructions
-   The specified required NIXL version can be found in [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] requirements/kv_connectors.txt](https://github.com/vllm-project/vllm/blob/main/requirements/kv_connectors.txt) and other relevant config files

For non-cuda platform, please install nixl with ucx build from source, instructed as below.

    python tools/install_nixl_from_source_ubuntu.py

### Transport Configuration[¶](#transport-configuration "Permanent link")

NixlConnector uses NIXL library for underlying communication, which supports multiple transport backends. UCX (Unified Communication X) is the primary default transport library used by NIXL. Configure transport environment variables:

    # Example UCX configuration, adjust according to your environment
    export UCX_TLS=all  # or specify specific transports like "rc,ud,sm,^cuda_ipc" ..etc
    export UCX_NET_DEVICES=all  # or specify network devices like "mlx5_0:1,mlx5_1:1"

Tip

When using UCX as the transport backend, NCCL environment variables (like `NCCL_IB_HCA`, `NCCL_SOCKET_IFNAME`) are not applicable to NixlConnector, so configure UCX-specific environment variables instead of NCCL variables.

## Basic Usage (on the same host)[¶](#basic-usage-on-the-same-host "Permanent link")

### Producer (Prefiller) Configuration[¶](#producer-prefiller-configuration "Permanent link")

Start a prefiller instance that produces KV caches

    # 1st GPU as prefiller
    CUDA_VISIBLE_DEVICES=0 \
    UCX_NET_DEVICES=all \
    VLLM_NIXL_SIDE_CHANNEL_PORT=5600 \
    vllm serve Qwen/Qwen3-0.6B \
      --port 8100 \
      --enforce-eager \
      --kv-transfer-config ''

### Consumer (Decoder) Configuration[¶](#consumer-decoder-configuration "Permanent link")

Start a decoder instance that consumes KV caches:

    # 2nd GPU as decoder
    CUDA_VISIBLE_DEVICES=1 \
    UCX_NET_DEVICES=all \
    VLLM_NIXL_SIDE_CHANNEL_PORT=5601 \
    vllm serve Qwen/Qwen3-0.6B \
      --port 8200 \
      --enforce-eager \
      --kv-transfer-config ''

### Proxy Server[¶](#proxy-server "Permanent link")

Use a proxy server to route requests between prefiller and decoder:

    python tests/v1/kv_connector/nixl_integration/toy_proxy_server.py \
      --port 8192 \
      --prefiller-hosts localhost \
      --prefiller-ports 8100 \
      --decoder-hosts localhost \
      --decoder-ports 8200

## Environment Variables[¶](#environment-variables "Permanent link")

-   `VLLM_NIXL_SIDE_CHANNEL_PORT`: Port for NIXL handshake communication

    -   Default: 5600
    -   **Required for both prefiller and decoder instances**
    -   Each vLLM worker needs a unique port on its host; using the same port number across different hosts is fine
    -   For TP/DP deployments, each worker\'s port on a node is computed as: base_port + dp_rank (e.g., with `--data-parallel-size=2` and base_port=5600, dp_rank 0..1 use port 5600, 5601 on that node).
    -   Used for the initial NIXL handshake between the prefiller and the decoder

-   `VLLM_NIXL_SIDE_CHANNEL_HOST`: Host for side channel communication

    -   Default: \"localhost\"
    -   Set when prefiller and decoder are on different machines
    -   Connection info is passed via KVTransferParams from prefiller to decoder for handshake

-   `VLLM_NIXL_ABORT_REQUEST_TIMEOUT`: Timeout (in seconds) for automatically releasing the prefiller's KV cache for a particular request. (Optional)

    -   Default: 480
    -   If a request is aborted and the decoder has not yet read the KV-cache blocks through the nixl channel, the prefill instance will release its KV-cache blocks after this timeout to avoid holding them indefinitely.

## Multi-Instance Setup[¶](#multi-instance-setup "Permanent link")

### Multiple Prefiller Instances on Different Machines[¶](#multiple-prefiller-instances-on-different-machines "Permanent link")

    # Prefiller 1 on Machine A (example IP: $)
    VLLM_NIXL_SIDE_CHANNEL_HOST=$ \
    VLLM_NIXL_SIDE_CHANNEL_PORT=5600 \
    UCX_NET_DEVICES=all \
    vllm serve Qwen/Qwen3-0.6B --port 8000 \
      --tensor-parallel-size 8 \
      --kv-transfer-config ''

    # Prefiller 2 on Machine B (example IP: $)
    VLLM_NIXL_SIDE_CHANNEL_HOST=$ \
    VLLM_NIXL_SIDE_CHANNEL_PORT=5600 \
    UCX_NET_DEVICES=all \
    vllm serve Qwen/Qwen3-0.6B --port 8000 \
      --tensor-parallel-size 8 \
      --kv-transfer-config ''

### Multiple Decoder Instances on Different Machines[¶](#multiple-decoder-instances-on-different-machines "Permanent link")

    # Decoder 1 on Machine C (example IP: $)
    VLLM_NIXL_SIDE_CHANNEL_HOST=$ \
    VLLM_NIXL_SIDE_CHANNEL_PORT=5600 \
    UCX_NET_DEVICES=all \
    vllm serve Qwen/Qwen3-0.6B --port 8000 \
      --tensor-parallel-size 8 \
      --kv-transfer-config ''

    # Decoder 2 on Machine D (example IP: $)
    VLLM_NIXL_SIDE_CHANNEL_HOST=$ \
    VLLM_NIXL_SIDE_CHANNEL_PORT=5600 \
    UCX_NET_DEVICES=all \
    vllm serve Qwen/Qwen3-0.6B --port 8000 \
      --tensor-parallel-size 8 \
      --kv-transfer-config ''

### Proxy for Multiple Instances[¶](#proxy-for-multiple-instances "Permanent link")

    python tests/v1/kv_connector/nixl_integration/toy_proxy_server.py \
      --port 8192 \
      --prefiller-hosts $ $ \
      --prefiller-ports 8000 8000 \
      --decoder-hosts $ $ \
      --decoder-ports 8000 8000

For multi-host DP deployment, only need to provide the host/port of the head instances.

### KV Role Options[¶](#kv-role-options "Permanent link")

-   **kv_producer**: For prefiller instances that generate KV caches
-   **kv_consumer**: For decoder instances that consume KV caches from prefiller
-   **kv_both**: Enables symmetric functionality where the connector can act as both producer and consumer. This provides flexibility for experimental setups and scenarios where the role distinction is not predetermined.

Tip

NixlConnector currently does not distinguish `kv_role`; the actual prefiller/decoder roles are determined by the upper-level proxy (e.g., `toy_proxy_server.py` using `--prefiller-hosts` and `--decoder-hosts`). Therefore, `kv_role` in `--kv-transfer-config` is effectively a placeholder and does not affect NixlConnector\'s behavior.

## Experimental Feature[¶](#experimental-feature "Permanent link")

### Heterogeneous KV Layout support[¶](#heterogeneous-kv-layout-support "Permanent link")

Support use case: Prefill with \'HND\' and decode with \'NHD\' with experimental configuration

    --kv-transfer-config ''

## Example Scripts/Code[¶](#example-scriptscode "Permanent link")

Refer to these example scripts in the vLLM repository:

-   [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] run_accuracy_test.sh](https://github.com/vllm-project/vllm/blob/main/tests/v1/kv_connector/nixl_integration/run_accuracy_test.sh)
-   [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] toy_proxy_server.py](https://github.com/vllm-project/vllm/blob/main/tests/v1/kv_connector/nixl_integration/toy_proxy_server.py)
-   [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] test_accuracy.py](https://github.com/vllm-project/vllm/blob/main/tests/v1/kv_connector/nixl_integration/test_accuracy.py)

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [December 10, 2025] ]