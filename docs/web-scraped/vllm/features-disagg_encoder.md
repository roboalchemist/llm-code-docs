# Source: https://docs.vllm.ai/en/stable/features/disagg_encoder/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/features/disagg_encoder.md "Edit this page")

# Disaggregated Encoder[¶](#disaggregated-encoder "Permanent link")

A **disaggregated encoder** runs the vision-encoder stage of a multimodal LLM in a process that is separate from the pre-fill / decoder stage. Deploying these two stages in independent vLLM instances brings three practical benefits:

1.  **Independent, fine-grained scaling**
2.  **Lower time-to-first-token (TTFT)**
3.  **Cross-process reuse and caching of encoder outputs**

Design doc: <https://docs.google.com/document/d/1aed8KtC6XkXtdoV87pWT0a8OJlZ-CpnuLLzmR8l9BAE>

------------------------------------------------------------------------

## 1 Motivation[¶](#1-motivation "Permanent link") 

### 1. Independent, fine-grained scaling[¶](#1-independent-fine-grained-scaling "Permanent link") 

-   Vision encoders are lightweight, while language models are orders of magnitude larger.
-   The language model can be parallelised without affecting the encoder fleet.
-   Encoder nodes can be added or removed independently.

### 2. Lower time-to-first-token (TTFT)[¶](#2-lower-time-to-first-token-ttft "Permanent link") 

-   Language-only requests bypass the vision encoder entirely.
-   Encoder output is injected only at required attention layers, shortening the pre-fill critical path.

### 3. Cross-process reuse and caching[¶](#3-cross-process-reuse-and-caching "Permanent link") 

-   In-process encoders confine reuse to a single worker.
-   A remote, shared cache lets any worker retrieve existing embeddings, eliminating redundant computation.

------------------------------------------------------------------------

## 2 Usage Example[¶](#2-usage-example "Permanent link") 

The current reference pathway is **ExampleConnector**.\
Below ready-to-run scripts shows the workflow:

1 Encoder instance + 1 PD instance: `examples/online_serving/disaggregated_encoder/disagg_1e1pd_example.sh`

1 Encoder instance + 1 Prefill instance + 1 Decode instance: `examples/online_serving/disaggregated_encoder/disagg_1e1p1d_example.sh`

------------------------------------------------------------------------

## 3 Test Script[¶](#3-test-script "Permanent link") 

Please refer to the directories `tests/v1/ec_connector`

## 4 Development[¶](#4-development "Permanent link") 

Disaggregated encoding is implemented by running two parts:

-   **Encoder instance** -- a vLLM instance to performs vision encoding.
-   **Prefill/Decode (PD) instance(s)** -- runs language pre-fill and decode.
    -   PD can be in either a single normal instance with `disagg_encoder_example.sh` (E-\>PD) or in disaggregated instances with `disagg_epd_example.sh` (E-\>P-\>D)

A connector transfers encoder-cache (EC) embeddings from the encoder instance to the PD instance.\
All related code is under `vllm/distributed/ec_transfer`.

### Key abstractions[¶](#key-abstractions "Permanent link")

-   **ECConnector** -- interface for retrieving EC caches produced by the encoder.
    -   *Scheduler role* -- checks cache existence and schedules loads.
    -   *Worker role* -- loads the embeddings into memory.

Here is a figure illustrating disaggregate encoder flow:

[![Disaggregated Encoder Flow](../../assets/features/disagg_encoder/disagg_encoder_flow.png)](../../assets/features/disagg_encoder/disagg_encoder_flow.png)

For the PD disaggregation part, the Prefill instance receive cache exactly the same as the disaggregate encoder flow above. Prefill instance executes 1 step (prefill -\> 1 token output) and then transfer KV cache to the Decode instance for the remaining execution. The KV transfer part purely happens after the execute of the PDinstance.

`docs/features/disagg_prefill.md` shows the brief idea about the disaggregated prefill (v0)

We create the example setup with the **NixlConnector** from `vllm/distributed/kv_transfer/kv_connector/v1/nixl_connector.py` and referred to the `tests/v1/kv_connector/nixl_integration/toy_proxy_server.py` to facilitate the kv transfer between P and D;

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [December 9, 2025] ]