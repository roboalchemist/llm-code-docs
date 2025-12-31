# Source: https://docs.vllm.ai/en/stable/configuration/conserving_memory/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/configuration/conserving_memory.md "Edit this page")

# Conserving Memory[¶](#conserving-memory "Permanent link")

Large models might cause your machine to run out of memory (OOM). Here are some options that help alleviate this problem.

## Tensor Parallelism (TP)[¶](#tensor-parallelism-tp "Permanent link")

Tensor parallelism (`tensor_parallel_size` option) can be used to split the model across multiple GPUs.

The following code splits the model across 2 GPUs.

    from vllm import LLM

    llm = LLM(model="ibm-granite/granite-3.1-8b-instruct", tensor_parallel_size=2)

Warning

To ensure that vLLM initializes CUDA correctly, you should avoid calling related functions (e.g. [torch.cuda.set_device](https://pytorch.org/docs/stable/generated/torch.cuda.set_device.html#torch.cuda.set_device)) before initializing vLLM. Otherwise, you may run into an error like `RuntimeError: Cannot re-initialize CUDA in forked subprocess`.

To control which devices are used, please instead set the `CUDA_VISIBLE_DEVICES` environment variable.

Note

With tensor parallelism enabled, each process will read the whole model and split it into chunks, which makes the disk reading time even longer (proportional to the size of tensor parallelism).

You can convert the model checkpoint to a sharded checkpoint using [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/offline_inference/save_sharded_state.py](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/save_sharded_state.py). The conversion process might take some time, but later you can load the sharded checkpoint much faster. The model loading time should remain constant regardless of the size of tensor parallelism.

## Quantization[¶](#quantization "Permanent link")

Quantized models take less memory at the cost of lower precision.

Statically quantized models can be downloaded from HF Hub (some popular ones are available at [Red Hat AI](https://huggingface.co/RedHatAI)) and used directly without extra configuration.

Dynamic quantization is also supported via the `quantization` option \-- see [here](../../features/quantization/) for more details.

## Context length and batch size[¶](#context-length-and-batch-size "Permanent link")

You can further reduce memory usage by limiting the context length of the model (`max_model_len` option) and the maximum batch size (`max_num_seqs` option).

    from vllm import LLM

    llm = LLM(model="adept/fuyu-8b", max_model_len=2048, max_num_seqs=2)

## Reduce CUDA Graphs[¶](#reduce-cuda-graphs "Permanent link")

By default, we optimize model inference using CUDA graphs which take up extra memory in the GPU.

You can adjust `compilation_config` to achieve a better balance between inference speed and memory usage:

Code

    from vllm import LLM
    from vllm.config import CompilationConfig, CompilationMode

    llm = LLM(
        model="meta-llama/Llama-3.1-8B-Instruct",
        compilation_config=CompilationConfig(
            mode=CompilationMode.VLLM_COMPILE,
            # By default, it goes up to max_num_seqs
            cudagraph_capture_sizes=[1, 2, 4, 8, 16],
        ),
    )

You can disable graph capturing completely via the `enforce_eager` flag:

    from vllm import LLM

    llm = LLM(model="meta-llama/Llama-3.1-8B-Instruct", enforce_eager=True)

## Adjust cache size[¶](#adjust-cache-size "Permanent link")

If you run out of CPU RAM, try the following options:

-   (Multi-modal models only) you can set the size of multi-modal cache by setting `mm_processor_cache_gb` engine argument (default 4 GiB).
-   (CPU backend only) you can set the size of KV cache using `VLLM_CPU_KVCACHE_SPACE` environment variable (default 4 GiB).

## Multi-modal input limits[¶](#multi-modal-input-limits "Permanent link")

You can allow a smaller number of multi-modal items per prompt to reduce the memory footprint of the model:

    from vllm import LLM

    # Accept up to 3 images and 1 video per prompt
    llm = LLM(
        model="Qwen/Qwen2.5-VL-3B-Instruct",
        limit_mm_per_prompt=,
    )

You can go a step further and disable unused modalities completely by setting its limit to zero. For example, if your application only accepts image input, there is no need to allocate any memory for videos.

    from vllm import LLM

    # Accept any number of images but no videos
    llm = LLM(
        model="Qwen/Qwen2.5-VL-3B-Instruct",
        limit_mm_per_prompt=,
    )

You can even run a multi-modal model for text-only inference:

    from vllm import LLM

    # Don't accept images. Just text.
    llm = LLM(
        model="google/gemma-3-27b-it",
        limit_mm_per_prompt=,
    )

### Configurable options[¶](#configurable-options "Permanent link")

`limit_mm_per_prompt` also accepts configurable options per modality. In the configurable form, you still specify `count`, and you may optionally provide size hints that control how vLLM profiles and reserves memory for your multi‑modal inputs. This helps you tune memory for the actual media you expect, instead of the model's absolute maxima.

Configurable options by modality:

-   `image`: ``
-   `video`: ``
-   `audio`: ``

Details could be found in [`ImageDummyOptions`](../../api/vllm/config/multimodal/#vllm.config.multimodal.ImageDummyOptions "            ImageDummyOptions"), [`VideoDummyOptions`](../../api/vllm/config/multimodal/#vllm.config.multimodal.VideoDummyOptions "            VideoDummyOptions"), and [`AudioDummyOptions`](../../api/vllm/config/multimodal/#vllm.config.multimodal.AudioDummyOptions "            AudioDummyOptions").

Examples:

    from vllm import LLM

    # Up to 5 images per prompt, profile with 512x512.
    # Up to 1 video per prompt, profile with 32 frames at 640x640.
    llm = LLM(
        model="Qwen/Qwen2.5-VL-3B-Instruct",
        limit_mm_per_prompt=,
            "video": ,
        },
    )

For backward compatibility, passing an integer works as before and is interpreted as ``. For example:

-   `limit_mm_per_prompt=` is equivalent to `limit_mm_per_prompt=}`
-   You can mix formats: `limit_mm_per_prompt=}`

Note

-   The size hints affect memory profiling only. They shape the dummy inputs used to compute reserved activation sizes. They do not change how inputs are actually processed at inference time.
-   If a hint exceeds what the model can accept, vLLM clamps it to the model\'s effective maximum and may log a warning.

Warning

These size hints currently only affect activation memory profiling. Encoder cache size is determined by the actual inputs at runtime and is not limited by these hints.

## Multi-modal processor arguments[¶](#multi-modal-processor-arguments "Permanent link")

For certain models, you can adjust the multi-modal processor arguments to reduce the size of the processed multi-modal inputs, which in turn saves memory.

Here are some examples:

    from vllm import LLM

    # Available for Qwen2-VL series models
    llm = LLM(
        model="Qwen/Qwen2.5-VL-3B-Instruct",
        mm_processor_kwargs=,  # Default is 1280 * 28 * 28
    )

    # Available for InternVL series models
    llm = LLM(
        model="OpenGVLab/InternVL2-2B",
        mm_processor_kwargs=,  # Default is 12
    )

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [November 23, 2025] ]