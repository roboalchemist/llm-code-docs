# Source: https://docs.vllm.ai/en/stable/getting_started/quickstart/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/getting_started/quickstart.md "Edit this page")

# Quickstart[¶](#quickstart "Permanent link")

This guide will help you quickly get started with vLLM to perform:

-   [Offline batched inference](#offline-batched-inference)
-   [Online serving using OpenAI-compatible server](#openai-compatible-server)

## Prerequisites[¶](#prerequisites "Permanent link")

-   OS: Linux
-   Python: 3.10 \-- 3.13

## Installation[¶](#installation "Permanent link")

NVIDIA CUDAAMD ROCmGoogle TPU

If you are using NVIDIA GPUs, you can install vLLM using [pip](https://pypi.org/project/vllm/) directly.

It\'s recommended to use [uv](https://docs.astral.sh/uv/), a very fast Python environment manager, to create and manage Python environments. Please follow the [documentation](https://docs.astral.sh/uv/#getting-started) to install `uv`. After installing `uv`, you can create a new Python environment and install vLLM using the following commands:

    uv venv --python 3.12 --seed
    source .venv/bin/activate
    uv pip install vllm --torch-backend=auto

`uv` can [automatically select the appropriate PyTorch index at runtime](https://docs.astral.sh/uv/guides/integration/pytorch/#automatic-backend-selection) by inspecting the installed CUDA driver version via `--torch-backend=auto` (or `UV_TORCH_BACKEND=auto`). To select a specific backend (e.g., `cu126`), set `--torch-backend=cu126` (or `UV_TORCH_BACKEND=cu126`).

Another delightful way is to use `uv run` with `--with [dependency]` option, which allows you to run commands such as `vllm serve` without creating any permanent environment:

    uv run --with vllm vllm --help

You can also use [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html) to create and manage Python environments. You can install `uv` to the conda environment through `pip` if you want to manage it within the environment.

    conda create -n myenv python=3.12 -y
    conda activate myenv
    pip install --upgrade uv
    uv pip install vllm --torch-backend=auto

Use a pre-built docker image from Docker Hub. The public stable image is [rocm/vllm:latest](https://hub.docker.com/r/rocm/vllm). There is also a development image at [rocm/vllm-dev](https://hub.docker.com/r/rocm/vllm-dev).

The `-v` flag in the `docker run` command below mounts a local directory into the container. Replace `<path/to/your/models>` with the path on your host machine to the directory containing your models. The models will then be accessible inside the container at `/app/models`.

Commands

    docker pull rocm/vllm-dev:nightly # to get the latest image
    docker run -it --rm \
    --network=host \
    --group-add=video \
    --ipc=host \
    --cap-add=SYS_PTRACE \
    --security-opt seccomp=unconfined \
    --device /dev/kfd \
    --device /dev/dri \
    -v <path/to/your/models>:/app/models \
    -e HF_HOME="/app/models" \
    rocm/vllm-dev:nightly

To run vLLM on Google TPUs, you need to install the `vllm-tpu` package.

    uv pip install vllm-tpu

Note

For more detailed instructions, including Docker, installing from source, and troubleshooting, please refer to the [vLLM on TPU documentation](https://docs.vllm.ai/projects/tpu/en/latest/).

Note

For more detail and non-CUDA platforms, please refer [here](../installation/) for specific instructions on how to install vLLM.

## Offline Batched Inference[¶](#offline-batched-inference "Permanent link")

With vLLM installed, you can start generating texts for list of input prompts (i.e. offline batch inferencing). See the example script: [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/offline_inference/basic/basic.py](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/basic/basic.py)

The first line of this example imports the classes [LLM](../../api/vllm/#vllm.LLM "            LLM") and [SamplingParams](../../api/vllm/#vllm.SamplingParams "            SamplingParams"):

-   [LLM](../../api/vllm/#vllm.LLM "            LLM") is the main class for running offline inference with vLLM engine.
-   [SamplingParams](../../api/vllm/#vllm.SamplingParams "            SamplingParams") specifies the parameters for the sampling process.

    from vllm import LLM, SamplingParams

The next section defines a list of input prompts and sampling parameters for text generation. The [sampling temperature](https://arxiv.org/html/2402.05201v1) is set to `0.8` and the [nucleus sampling probability](https://en.wikipedia.org/wiki/Top-p_sampling) is set to `0.95`. You can find more information about the sampling parameters [here](../../api/#inference-parameters).

Important

By default, vLLM will use sampling parameters recommended by model creator by applying the `generation_config.json` from the Hugging Face model repository if it exists. In most cases, this will provide you with the best results by default if [SamplingParams](../../api/vllm/#vllm.SamplingParams "            SamplingParams") is not specified.

However, if vLLM\'s default sampling parameters are preferred, please set `generation_config="vllm"` when creating the [LLM](../../api/vllm/#vllm.LLM "            LLM") instance.

    prompts = [
        "Hello, my name is",
        "The president of the United States is",
        "The capital of France is",
        "The future of AI is",
    ]
    sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

The [LLM](../../api/vllm/#vllm.LLM "            LLM") class initializes vLLM\'s engine and the [OPT-125M model](https://arxiv.org/abs/2205.01068) for offline inference. The list of supported models can be found [here](../../models/supported_models/).

    llm = LLM(model="facebook/opt-125m")

Note

By default, vLLM downloads models from [Hugging Face](https://huggingface.co/). If you would like to use models from [ModelScope](https://www.modelscope.cn), set the environment variable `VLLM_USE_MODELSCOPE` before initializing the engine.

    export VLLM_USE_MODELSCOPE=True

Now, the fun part! The outputs are generated using `llm.generate`. It adds the input prompts to the vLLM engine\'s waiting queue and executes the vLLM engine to generate the outputs with high throughput. The outputs are returned as a list of `RequestOutput` objects, which include all of the output tokens.

    outputs = llm.generate(prompts, sampling_params)

    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: , Generated text: ")

Note

The `llm.generate` method does not automatically apply the model\'s chat template to the input prompt. Therefore, if you are using an Instruct model or Chat model, you should manually apply the corresponding chat template to ensure the expected behavior. Alternatively, you can use the `llm.chat` method and pass a list of messages which have the same format as those passed to OpenAI\'s `client.chat.completions`:

Code

    # Using tokenizer to apply chat template
    from transformers import AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained("/path/to/chat_model")
    messages_list = [
        []
        for prompt in prompts
    ]
    texts = tokenizer.apply_chat_template(
        messages_list,
        tokenize=False,
        add_generation_prompt=True,
    )

    # Generate outputs
    outputs = llm.generate(texts, sampling_params)

    # Print the outputs.
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: , Generated text: ")

    # Using chat interface.
    outputs = llm.chat(messages_list, sampling_params)
    for idx, output in enumerate(outputs):
        prompt = prompts[idx]
        generated_text = output.outputs[0].text
        print(f"Prompt: , Generated text: ")

## OpenAI-Compatible Server[¶](#openai-compatible-server "Permanent link")

vLLM can be deployed as a server that implements the OpenAI API protocol. This allows vLLM to be used as a drop-in replacement for applications using OpenAI API. By default, it starts the server at `http://localhost:8000`. You can specify the address with `--host` and `--port` arguments. The server currently hosts one model at a time and implements endpoints such as [list models](https://platform.openai.com/docs/api-reference/models/list), [create chat completion](https://platform.openai.com/docs/api-reference/chat/completions/create), and [create completion](https://platform.openai.com/docs/api-reference/completions/create) endpoints.

Run the following command to start the vLLM server with the [Qwen2.5-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct) model:

    vllm serve Qwen/Qwen2.5-1.5B-Instruct

Note

By default, the server uses a predefined chat template stored in the tokenizer. You can learn about overriding it [here](../../serving/openai_compatible_server/#chat-template).

Important

By default, the server applies `generation_config.json` from the huggingface model repository if it exists. This means the default values of certain sampling parameters can be overridden by those recommended by the model creator.

To disable this behavior, please pass `--generation-config vllm` when launching the server.

This server can be queried in the same format as OpenAI API. For example, to list the models:

    curl http://localhost:8000/v1/models

You can pass in the argument `--api-key` or environment variable `VLLM_API_KEY` to enable the server to check for API key in the header. You can pass multiple keys after `--api-key`, and the server will accept any of the keys passed, this can be useful for key rotation.

### OpenAI Completions API with vLLM[¶](#openai-completions-api-with-vllm "Permanent link")

Once your server is started, you can query the model with input prompts:

    curl http://localhost:8000/v1/completions \
        -H "Content-Type: application/json" \
        -d ''

Since this server is compatible with OpenAI API, you can use it as a drop-in replacement for any applications using OpenAI API. For example, another way to query the server is via the `openai` Python package:

Code

    from openai import OpenAI

    # Modify OpenAI's API key and API base to use vLLM's API server.
    openai_api_key = "EMPTY"
    openai_api_base = "http://localhost:8000/v1"
    client = OpenAI(
        api_key=openai_api_key,
        base_url=openai_api_base,
    )
    completion = client.completions.create(
        model="Qwen/Qwen2.5-1.5B-Instruct",
        prompt="San Francisco is a",
    )
    print("Completion result:", completion)

A more detailed client example can be found here: [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/offline_inference/basic/basic.py](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/basic/basic.py)

### OpenAI Chat Completions API with vLLM[¶](#openai-chat-completions-api-with-vllm "Permanent link")

vLLM is designed to also support the OpenAI Chat Completions API. The chat interface is a more dynamic, interactive way to communicate with the model, allowing back-and-forth exchanges that can be stored in the chat history. This is useful for tasks that require context or more detailed explanations.

You can use the [create chat completion](https://platform.openai.com/docs/api-reference/chat/completions/create) endpoint to interact with the model:

    curl http://localhost:8000/v1/chat/completions \
        -H "Content-Type: application/json" \
        -d ',
                
            ]
        }'

Alternatively, you can use the `openai` Python package:

Code

    from openai import OpenAI
    # Set OpenAI's API key and API base to use vLLM's API server.
    openai_api_key = "EMPTY"
    openai_api_base = "http://localhost:8000/v1"

    client = OpenAI(
        api_key=openai_api_key,
        base_url=openai_api_base,
    )

    chat_response = client.chat.completions.create(
        model="Qwen/Qwen2.5-1.5B-Instruct",
        messages=[
            ,
            ,
        ],
    )
    print("Chat response:", chat_response)

## On Attention Backends[¶](#on-attention-backends "Permanent link")

Currently, vLLM supports multiple backends for efficient Attention computation across different platforms and accelerator architectures. It automatically selects the most performant backend compatible with your system and model specifications.

If desired, you can also manually set the backend of your choice using the `--attention-backend` CLI argument:

    # For online serving
    vllm serve Qwen/Qwen2.5-1.5B-Instruct --attention-backend FLASH_ATTN

    # For offline inference
    python script.py --attention-backend FLASHINFER

Some of the available backend options include:

-   On NVIDIA CUDA: `FLASH_ATTN` or `FLASHINFER`.
-   On AMD ROCm: `TRITON_ATTN`, `ROCM_ATTN`, `ROCM_AITER_FA` or `ROCM_AITER_UNIFIED_ATTN`.

For AMD ROCm, you can further control the specific Attention implementation using the following options:

-   Triton Unified Attention: Set the environment variables `VLLM_ROCM_USE_AITER=0 VLLM_ROCM_USE_AITER_MHA=0` and pass `--attention-config.use_prefill_decode_attention=false` as a CLI argument.
-   AITER Unified Attention: Set the environment variables `VLLM_ROCM_USE_AITER=1 VLLM_USE_AITER_UNIFIED_ATTENTION=1 VLLM_ROCM_USE_AITER_MHA=0` and pass `--attention-config.use_prefill_decode_attention=false` as a CLI argument.
-   Triton Prefill-Decode Attention: Set the environment variables `VLLM_ROCM_USE_AITER=1 VLLM_ROCM_USE_AITER_MHA=0` and pass `--attention-config.use_prefill_decode_attention=true` as a CLI argument.
-   AITER Multi-head Attention: Set the environment variables `VLLM_ROCM_USE_AITER=1 VLLM_ROCM_USE_AITER_MHA=1` and pass `--attention-config.use_prefill_decode_attention=false` as a CLI argument.

Warning

There are no pre-built vllm wheels containing Flash Infer, so you must install it in your environment first. Refer to the [Flash Infer official docs](https://docs.flashinfer.ai/) or see [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] docker/Dockerfile](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile) for instructions on how to install it.

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [December 13, 2025] ]