# Source: https://docs.vllm.ai/en/stable/models/extensions/tensorizer/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/models/extensions/tensorizer.md "Edit this page")

# Loading models with CoreWeave\'s Tensorizer[¶](#loading-models-with-coreweaves-tensorizer "Permanent link")

vLLM supports loading models with [CoreWeave\'s Tensorizer](https://docs.coreweave.com/coreweave-machine-learning-and-ai/inference/tensorizer). vLLM model tensors that have been serialized to disk, an HTTP/HTTPS endpoint, or S3 endpoint can be deserialized at runtime extremely quickly directly to the GPU, resulting in significantly shorter Pod startup times and CPU memory usage. Tensor encryption is also supported.

vLLM fully integrates Tensorizer in to its model loading machinery. The following will give a brief overview on how to get started with using Tensorizer on vLLM.

## Installing Tensorizer[¶](#installing-tensorizer "Permanent link")

To install `tensorizer`, run `pip install vllm[tensorizer]`.

## The basics[¶](#the-basics "Permanent link")

To load a model using Tensorizer, the model first needs to be serialized by Tensorizer. [The example script](../../../examples/others/tensorize_vllm_model/) takes care of this process.

Let\'s walk through a basic example by serializing `facebook/opt-125m` using the script, and then loading it for inference.

## Serializing a vLLM model with Tensorizer[¶](#serializing-a-vllm-model-with-tensorizer "Permanent link")

To serialize a model with Tensorizer, call the example script with the necessary CLI arguments. The docstring for the script itself explains the CLI args and how to use it properly in great detail, and we\'ll use one of the examples from the docstring directly, assuming we want to serialize and save our model at our S3 bucket example `s3://my-bucket`:

    python examples/others/tensorize_vllm_model.py \
       --model facebook/opt-125m \
       serialize \
       --serialized-directory s3://my-bucket \
       --suffix v1

This saves the model tensors at `s3://my-bucket/vllm/facebook/opt-125m/v1`. If you intend on applying a LoRA adapter to your tensorized model, you can pass the HF id of the LoRA adapter in the above command, and the artifacts will be saved there too:

    python examples/others/tensorize_vllm_model.py \
       --model facebook/opt-125m \
       --lora-path <lora_id> \
       serialize \
       --serialized-directory s3://my-bucket \
       --suffix v1

## Serving the model using Tensorizer[¶](#serving-the-model-using-tensorizer "Permanent link")

Once the model is serialized where you want it, you can load the model using `vllm serve` or the `LLM` entrypoint. You can pass the directory where you saved the model to the `model` argument for `LLM()` and `vllm serve`. For example, to serve the tensorized model saved previously with the LoRA adapter, you\'d do:

    vllm serve s3://my-bucket/vllm/facebook/opt-125m/v1 \
        --load-format tensorizer \
        --enable-lora 

Or, with `LLM()`:

    from vllm import LLM
    llm = LLM(
        "s3://my-bucket/vllm/facebook/opt-125m/v1", 
        load_format="tensorizer",
        enable_lora=True,
    )

## Options for configuring Tensorizer[¶](#options-for-configuring-tensorizer "Permanent link")

`tensorizer`\'s core objects that serialize and deserialize models are `TensorSerializer` and `TensorDeserializer` respectively. In order to pass arbitrary kwargs to these, which will configure the serialization and deserialization processes, you can provide them as keys to `model_loader_extra_config` with `serialization_kwargs` and `deserialization_kwargs` respectively. Full docstrings detailing all parameters for the aforementioned objects can be found in `tensorizer`\'s [serialization.py](https://github.com/coreweave/tensorizer/blob/main/tensorizer/serialization.py) file.

As an example, CPU concurrency can be limited when serializing with `tensorizer` via the `limit_cpu_concurrency` parameter in the initializer for `TensorSerializer`. To set `limit_cpu_concurrency` to some arbitrary value, you would do so like this when serializing:

    python examples/others/tensorize_vllm_model.py \
       --model facebook/opt-125m \
       --lora-path <lora_id> \
       serialize \
       --serialized-directory s3://my-bucket \
       --serialization-kwargs '' \
       --suffix v1

As an example when customizing the loading process via `TensorDeserializer`, you could limit the number of concurrency readers during deserialization with the `num_readers` parameter in the initializer via `model_loader_extra_config` like so:

    vllm serve s3://my-bucket/vllm/facebook/opt-125m/v1 \
        --load-format tensorizer \
        --enable-lora \
        --model-loader-extra-config '}'

Or with `LLM()`:

    from vllm import LLM
    llm = LLM(
        "s3://my-bucket/vllm/facebook/opt-125m/v1", 
        load_format="tensorizer",
        enable_lora=True,
        model_loader_extra_config=},
    )

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [October 15, 2025] ]