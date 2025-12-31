# Source: https://docs.vllm.ai/en/stable/serving/offline_inference/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/serving/offline_inference.md "Edit this page")

# Offline Inference[¶](#offline-inference "Permanent link")

Offline inference is possible in your own code using vLLM\'s [`LLM`](../../api/vllm/#vllm.LLM "            LLM") class.

For example, the following code downloads the [`facebook/opt-125m`](https://huggingface.co/facebook/opt-125m) model from HuggingFace and runs it in vLLM using the default configuration.

    from vllm import LLM

    # Initialize the vLLM engine.
    llm = LLM(model="facebook/opt-125m")

After initializing the `LLM` instance, use the available APIs to perform model inference. The available APIs depend on the model type:

-   [Generative models](../../models/generative_models/) output logprobs which are sampled from to obtain the final output text.
-   [Pooling models](../../models/pooling_models/) output their hidden states directly.

Info

[API Reference](../../api/#offline-inference)

## Ray Data LLM API[¶](#ray-data-llm-api "Permanent link")

Ray Data LLM is an alternative offline inference API that uses vLLM as the underlying engine. This API adds several batteries-included capabilities that simplify large-scale, GPU-efficient inference:

-   Streaming execution processes datasets that exceed aggregate cluster memory.
-   Automatic sharding, load balancing, and autoscaling distribute work across a Ray cluster with built-in fault tolerance.
-   Continuous batching keeps vLLM replicas saturated and maximizes GPU utilization.
-   Transparent support for tensor and pipeline parallelism enables efficient multi-GPU inference.
-   Reading and writing to most popular file formats and cloud object storage.
-   Scaling up the workload without code changes.

Code

    import ray  # Requires ray>=2.44.1
    from ray.data.llm import vLLMEngineProcessorConfig, build_llm_processor

    config = vLLMEngineProcessorConfig(model_source="unsloth/Llama-3.2-1B-Instruct")
    processor = build_llm_processor(
        config,
        preprocess=lambda row: ,
                ,
            ],
            "sampling_params": ,
        },
        postprocess=lambda row: ,
    )

    ds = ray.data.from_items(["An old silent pond..."])
    ds = processor(ds)
    ds.write_parquet("local:///tmp/data/")

For more information about the Ray Data LLM API, see the [Ray Data LLM documentation](https://docs.ray.io/en/latest/data/working-with-llms.html).

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [October 17, 2025] ]