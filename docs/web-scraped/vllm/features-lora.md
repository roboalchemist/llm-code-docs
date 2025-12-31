# Source: https://docs.vllm.ai/en/stable/features/lora/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/features/lora.md "Edit this page")

# LoRA Adapters[¶](#lora-adapters "Permanent link")

This document shows you how to use [LoRA adapters](https://arxiv.org/abs/2106.09685) with vLLM on top of a base model.

LoRA adapters can be used with any vLLM model that implements [SupportsLoRA](../../api/vllm/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsLoRA "            SupportsLoRA").

Adapters can be efficiently served on a per-request basis with minimal overhead. First we download the adapter(s) and save them locally with

    from huggingface_hub import snapshot_download

    sql_lora_path = snapshot_download(repo_id="yard1/llama-2-7b-sql-lora-test")

Then we instantiate the base model and pass in the `enable_lora=True` flag:

    from vllm import LLM, SamplingParams
    from vllm.lora.request import LoRARequest

    llm = LLM(model="meta-llama/Llama-2-7b-hf", enable_lora=True)

We can now submit the prompts and call `llm.generate` with the `lora_request` parameter. The first parameter of `LoRARequest` is a human identifiable name, the second parameter is a globally unique ID for the adapter and the third parameter is the path to the LoRA adapter.

Code

    sampling_params = SamplingParams(
        temperature=0,
        max_tokens=256,
        stop=["[/assistant]"],
    )

    prompts = [
        "[user] Write a SQL query to answer the question based on the table schema.\n\n context: CREATE TABLE table_name_74 (icao VARCHAR, airport VARCHAR)\n\n question: Name the ICAO for lilongwe international airport [/user] [assistant]",
        "[user] Write a SQL query to answer the question based on the table schema.\n\n context: CREATE TABLE table_name_11 (nationality VARCHAR, elector VARCHAR)\n\n question: When Anchero Pantaleone was the elector what is under nationality? [/user] [assistant]",
    ]

    outputs = llm.generate(
        prompts,
        sampling_params,
        lora_request=LoRARequest("sql_adapter", 1, sql_lora_path),
    )

Check out [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/offline_inference/multilora_inference.py](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/multilora_inference.py) for an example of how to use LoRA adapters with the async engine and how to use more advanced configuration options.

## Serving LoRA Adapters[¶](#serving-lora-adapters "Permanent link")

LoRA adapted models can also be served with the Open-AI compatible vLLM server. To do so, we use `--lora-modules = =` to specify each LoRA module when we kick off the server:

    vllm serve meta-llama/Llama-2-7b-hf \
        --enable-lora \
        --lora-modules sql-lora=$HOME/.cache/huggingface/hub/models--yard1--llama-2-7b-sql-lora-test/snapshots/0dfa347e8877a4d4ed19ee56c140fa518470028c/

Note

The commit ID `0dfa347e8877a4d4ed19ee56c140fa518470028c` may change over time. Please check the latest commit ID in your environment to ensure you are using the correct one.

The server entrypoint accepts all other LoRA configuration parameters (`max_loras`, `max_lora_rank`, `max_cpu_loras`, etc.), which will apply to all forthcoming requests. Upon querying the `/models` endpoint, we should see our LoRA along with its base model (if `jq` is not installed, you can follow [this guide](https://jqlang.org/download/) to install it.):

Command

    curl localhost:8000/v1/models | jq .
    ,
            
        ]
    }

Requests can specify the LoRA adapter as if it were any other model via the `model` request parameter. The requests will be processed according to the server-wide LoRA configuration (i.e. in parallel with base model requests, and potentially other LoRA adapter requests if they were provided and `max_loras` is set high enough).

The following is an example request

    curl http://localhost:8000/v1/completions \
        -H "Content-Type: application/json" \
        -d '' | jq

## Dynamically serving LoRA Adapters[¶](#dynamically-serving-lora-adapters "Permanent link")

In addition to serving LoRA adapters at server startup, the vLLM server supports dynamically configuring LoRA adapters at runtime through dedicated API endpoints and plugins. This feature can be particularly useful when the flexibility to change models on-the-fly is needed.

Note: Enabling this feature in production environments is risky as users may participate in model adapter management.

To enable dynamic LoRA configuration, ensure that the environment variable `VLLM_ALLOW_RUNTIME_LORA_UPDATING` is set to `True`.

    export VLLM_ALLOW_RUNTIME_LORA_UPDATING=True

### Using API Endpoints[¶](#using-api-endpoints "Permanent link")

Loading a LoRA Adapter:

To dynamically load a LoRA adapter, send a POST request to the `/v1/load_lora_adapter` endpoint with the necessary details of the adapter to be loaded. The request payload should include the name and path to the LoRA adapter.

Example request to load a LoRA adapter:

    curl -X POST http://localhost:8000/v1/load_lora_adapter \
    -H "Content-Type: application/json" \
    -d ''

Upon a successful request, the API will respond with a `200 OK` status code from `vllm serve`, and `curl` returns the response body: `Success: LoRA adapter 'sql_adapter' added successfully`. If an error occurs, such as if the adapter cannot be found or loaded, an appropriate error message will be returned.

Unloading a LoRA Adapter:

To unload a LoRA adapter that has been previously loaded, send a POST request to the `/v1/unload_lora_adapter` endpoint with the name or ID of the adapter to be unloaded.

Upon a successful request, the API responds with a `200 OK` status code from `vllm serve`, and `curl` returns the response body: `Success: LoRA adapter 'sql_adapter' removed successfully`.

Example request to unload a LoRA adapter:

    curl -X POST http://localhost:8000/v1/unload_lora_adapter \
    -H "Content-Type: application/json" \
    -d ''

### Using Plugins[¶](#using-plugins "Permanent link")

Alternatively, you can use the LoRAResolver plugin to dynamically load LoRA adapters. LoRAResolver plugins enable you to load LoRA adapters from both local and remote sources such as local file system and S3. On every request, when there\'s a new model name that hasn\'t been loaded yet, the LoRAResolver will try to resolve and load the corresponding LoRA adapter.

You can set up multiple LoRAResolver plugins if you want to load LoRA adapters from different sources. For example, you might have one resolver for local files and another for S3 storage. vLLM will load the first LoRA adapter that it finds.

You can either install existing plugins or implement your own. By default, vLLM comes with a [resolver plugin to load LoRA adapters from a local directory.](https://github.com/vllm-project/vllm/tree/main/vllm/plugins/lora_resolvers) To enable this resolver, set `VLLM_ALLOW_RUNTIME_LORA_UPDATING` to True, set `VLLM_PLUGINS` to include `lora_filesystem_resolver`, and then set `VLLM_LORA_RESOLVER_CACHE_DIR` to a local directory. When vLLM receives a request using a LoRA adapter `foobar`, it will first look in the local directory for a directory `foobar`, and attempt to load the contents of that directory as a LoRA adapter. If successful, the request will complete as normal and that adapter will then be available for normal use on the server.

Alternatively, follow these example steps to implement your own plugin:

1.  Implement the LoRAResolver interface.

    Example of a simple S3 LoRAResolver implementation

    ::: 
        import os
        import s3fs
        from vllm.lora.request import LoRARequest
        from vllm.lora.resolver import LoRAResolver

        class S3LoRAResolver(LoRAResolver):
            def __init__(self):
                self.s3 = s3fs.S3FileSystem()
                self.s3_path_format = os.getenv("S3_PATH_TEMPLATE")
                self.local_path_format = os.getenv("LOCAL_PATH_TEMPLATE")

            async def resolve_lora(self, base_model_name, lora_name):
                s3_path = self.s3_path_format.format(base_model_name=base_model_name, lora_name=lora_name)
                local_path = self.local_path_format.format(base_model_name=base_model_name, lora_name=lora_name)

                # Download the LoRA from S3 to the local path
                await self.s3._get(
                    s3_path, local_path, recursive=True, maxdepth=1
                )

                lora_request = LoRARequest(
                    lora_name=lora_name,
                    lora_path=local_path,
                    lora_int_id=abs(hash(lora_name)),
                )
                return lora_request
    :::

2.  Register `LoRAResolver` plugin.

    ::: 
        from vllm.lora.resolver import LoRAResolverRegistry

        s3_resolver = S3LoRAResolver()
        LoRAResolverRegistry.register_resolver("s3_resolver", s3_resolver)
    :::

    For more details, refer to the [vLLM\'s Plugins System](../../design/plugin_system/).

## New format for `--lora-modules`[¶](#new-format-for-lora-modules "Permanent link") 

In the previous version, users would provide LoRA modules via the following format, either as a key-value pair or in JSON format. For example:

    --lora-modules sql-lora=$HOME/.cache/huggingface/hub/models--yard1--llama-2-7b-sql-lora-test/snapshots/0dfa347e8877a4d4ed19ee56c140fa518470028c/

This would only include the `name` and `path` for each LoRA module, but did not provide a way to specify a `base_model_name`. Now, you can specify a base_model_name alongside the name and path using JSON format. For example:

    --lora-modules ''

To provide the backward compatibility support, you can still use the old key-value format (name=path), but the `base_model_name` will remain unspecified in that case.

## LoRA model lineage in model card[¶](#lora-model-lineage-in-model-card "Permanent link")

The new format of `--lora-modules` is mainly to support the display of parent model information in the model card. Here\'s an explanation of how your current response supports this:

-   The `parent` field of LoRA model `sql-lora` now links to its base model `meta-llama/Llama-2-7b-hf`. This correctly reflects the hierarchical relationship between the base model and the LoRA adapter.
-   The `root` field points to the artifact location of the lora adapter.

Command output

    $ curl http://localhost:8000/v1/models

    
            ]
            },
            
            ]
            }
        ]
    }

## Default LoRA Models For Multimodal Models[¶](#default-lora-models-for-multimodal-models "Permanent link")

Some models, e.g., [Granite Speech](https://huggingface.co/ibm-granite/granite-speech-3.3-8b) and [Phi-4-multimodal-instruct](https://huggingface.co/microsoft/Phi-4-multimodal-instruct) multimodal, contain LoRA adapter(s) that are expected to always be applied when a given modality is present. This can be a bit tedious to manage with the above approaches, as it requires the user to send the `LoRARequest` (offline) or to filter requests between the base model and LoRA model (server) depending on the content of the request\'s multimodal data.

To this end, we allow registration of default multimodal LoRAs to handle this automatically, where users can map each modality to a LoRA adapter to automatically apply it when the corresponding inputs are present. Note that currently, we only allow one LoRA per prompt; if several modalities are provided, each of which are registered to a given modality, none of them will be applied.

Example usage for offline inference

    from transformers import AutoTokenizer
    from vllm import LLM, SamplingParams
    from vllm.assets.audio import AudioAsset

    model_id = "ibm-granite/granite-speech-3.3-2b"
    tokenizer = AutoTokenizer.from_pretrained(model_id)

    def get_prompt(question: str, has_audio: bool):
        """Build the input prompt to send to vLLM."""
        if has_audio:
            question = f"<|audio|>"
        chat = [
            ,
        ]
        return tokenizer.apply_chat_template(chat, tokenize=False)

    llm = LLM(
        model=model_id,
        enable_lora=True,
        max_lora_rank=64,
        max_model_len=2048,
        limit_mm_per_prompt=,
        # Will always pass a `LoRARequest` with the `model_id`
        # whenever audio is contained in the request data.
        default_mm_loras = ,
        enforce_eager=True,
    )

    question = "can you transcribe the speech into a written format?"
    prompt_with_audio = get_prompt(
        question=question,
        has_audio=True,
    )
    audio = AudioAsset("mary_had_lamb").audio_and_sample_rate

    inputs = 
    }

    outputs = llm.generate(
        inputs,
        sampling_params=SamplingParams(
            temperature=0.2,
            max_tokens=64,
        ),
    )

You can also pass a json dictionary of `--default-mm-loras` mapping modalities to LoRA model IDs. For example, when starting the server:

    vllm serve ibm-granite/granite-speech-3.3-2b \
        --max-model-len 2048 \
        --enable-lora \
        --default-mm-loras '' \
        --max-lora-rank 64

Note: Default multimodal LoRAs are currently only available for `.generate` and chat completions.

## Using Tips[¶](#using-tips "Permanent link")

### Configuring `max_lora_rank`[¶](#configuring-max_lora_rank "Permanent link")

The `--max-lora-rank` parameter controls the maximum rank allowed for LoRA adapters. This setting affects memory allocation and performance:

-   **Set it to the maximum rank** among all LoRA adapters you plan to use
-   **Avoid setting it too high** - using a value much larger than needed wastes memory and can cause performance issues

For example, if your LoRA adapters have ranks \[16, 32, 64\], use `--max-lora-rank 64` rather than 256

    # Good: matches actual maximum rank
    vllm serve model --enable-lora --max-lora-rank 64

    # Bad: unnecessarily high, wastes memory
    vllm serve model --enable-lora --max-lora-rank 256

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [November 18, 2025] ]