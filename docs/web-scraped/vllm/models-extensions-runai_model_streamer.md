# Source: https://docs.vllm.ai/en/stable/models/extensions/runai_model_streamer/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/models/extensions/runai_model_streamer.md "Edit this page")

# Loading models with Run:ai Model Streamer[¶](#loading-models-with-runai-model-streamer "Permanent link")

Run:ai Model Streamer is a library to read tensors in concurrency, while streaming it to GPU memory. Further reading can be found in [Run:ai Model Streamer Documentation](https://github.com/run-ai/runai-model-streamer/blob/master/docs/README.md).

vLLM supports loading weights in Safetensors format using the Run:ai Model Streamer. You first need to install vLLM RunAI optional dependency:

    pip3 install vllm[runai]

To run it as an OpenAI-compatible server, add the `--load-format runai_streamer` flag:

    vllm serve /home/meta-llama/Llama-3.2-3B-Instruct \
        --load-format runai_streamer

To run model from AWS S3 object store run:

    vllm serve s3://core-llm/Llama-3-8b \
        --load-format runai_streamer

To run model from Google Cloud Storage run:

    vllm serve gs://core-llm/Llama-3-8b \
        --load-format runai_streamer

To run model from a S3 compatible object store run:

    RUNAI_STREAMER_S3_USE_VIRTUAL_ADDRESSING=0 \
    AWS_EC2_METADATA_DISABLED=true \
    AWS_ENDPOINT_URL=https://storage.googleapis.com \
    vllm serve s3://core-llm/Llama-3-8b \
        --load-format runai_streamer

## Tunable parameters[¶](#tunable-parameters "Permanent link")

You can tune parameters using `--model-loader-extra-config`:

You can tune `distributed` that controls whether distributed streaming should be used. This is currently only possible on CUDA and ROCM devices. This can significantly improve loading times from object storage or high-throughput network fileshares. You can read further about Distributed streaming [here](https://github.com/run-ai/runai-model-streamer/blob/master/docs/src/usage.md#distributed-streaming)

    vllm serve /home/meta-llama/Llama-3.2-3B-Instruct \
        --load-format runai_streamer \
        --model-loader-extra-config ''

You can tune `concurrency` that controls the level of concurrency and number of OS threads reading tensors from the file to the CPU buffer. For reading from S3, it will be the number of client instances the host is opening to the S3 server.

    vllm serve /home/meta-llama/Llama-3.2-3B-Instruct \
        --load-format runai_streamer \
        --model-loader-extra-config ''

You can control the size of the CPU Memory buffer to which tensors are read from the file, and limit this size. You can read further about CPU buffer memory limiting [here](https://github.com/run-ai/runai-model-streamer/blob/master/docs/src/env-vars.md#runai_streamer_memory_limit).

    vllm serve /home/meta-llama/Llama-3.2-3B-Instruct \
        --load-format runai_streamer \
        --model-loader-extra-config ''

Note

For further instructions about tunable parameters and additional parameters configurable through environment variables, read the [Environment Variables Documentation](https://github.com/run-ai/runai-model-streamer/blob/master/docs/src/env-vars.md).

## Sharded Model Loading[¶](#sharded-model-loading "Permanent link")

vLLM also supports loading sharded models using Run:ai Model Streamer. This is particularly useful for large models that are split across multiple files. To use this feature, use the `--load-format runai_streamer_sharded` flag:

    vllm serve /path/to/sharded/model --load-format runai_streamer_sharded

The sharded loader expects model files to follow the same naming pattern as the regular sharded state loader: `model-rank--part-.safetensors`. You can customize this pattern using the `pattern` parameter in `--model-loader-extra-config`:

    vllm serve /path/to/sharded/model \
        --load-format runai_streamer_sharded \
        --model-loader-extra-config '-part-.safetensors"}'

To create sharded model files, you can use the script provided in [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/offline_inference/save_sharded_state.py](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/save_sharded_state.py). This script demonstrates how to save a model in the sharded format that is compatible with the Run:ai Model Streamer sharded loader.

The sharded loader supports all the same tunable parameters as the regular Run:ai Model Streamer, including `concurrency` and `memory_limit`. These can be configured in the same way:

    vllm serve /path/to/sharded/model \
        --load-format runai_streamer_sharded \
        --model-loader-extra-config ''

Note

The sharded loader is particularly efficient for tensor or pipeline parallel models where each worker only needs to read its own shard rather than the entire checkpoint.

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [October 30, 2025] ]