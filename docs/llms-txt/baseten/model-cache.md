# Source: https://docs.baseten.co/development/model/model-cache.md

# Cached weights 🆕

> Accelerate cold starts and availability by prefetching and caching your weights.

<Tip>
  ### What is a "cold start"?

  "Cold start" is a term used to describe the time taken when a request is received when the model is scaled to 0 until it is ready to handle the first request. This process is a critical factor in allowing your deployments to be responsive to traffic while maintaining your SLAs and lowering your costs.
  To optimize cold starts, we will go over the following stategies: Downloading them in a background thread in Rust that runs during the module import, caching weights in a distributed filesystem, and moving weights into the docker image.

  In practice, this reduces the cold start for large models to just a few seconds. For example, Stable Diffusion XL can take a few minutes to boot up without caching. With caching, it takes just under 10 seconds.
</Tip>

## Enabling Caching + Prefetching for a Model

To enable caching, simply add `model_cache` to your `config.yaml` with a valid `repo_id`. The `model_cache` has a few key configurations:

* `repo_id` (required): The repo name from Hugging Face or bucket/container from GCS, S3, or Azure.
* `revision` (required for Hugging Face): The revision of the huggingface repo, such as the sha or branch name such as `refs/pr/1` or `main`. Not needed for GCS, S3, or Azure.
* `use_volume`: Boolean flag to determine if the weights are downloaded to the Baseten Distributed Filesystem at runtime (recommended) or bundled into the container image (legacy, not recommended).
* `volume_folder`: string, folder name under which the model weights appear. Setting it to `my-llama-model` will mount the repo to `/app/model_cache/my-llama-model` at runtime.
* `allow_patterns`: Only cache files that match specified patterns. Utilize Unix shell-style wildcards to denote these patterns.
* `ignore_patterns`: Conversely, you can also denote file patterns to ignore, hence streamlining the caching process.
* `runtime_secret_name`: The name of your secret containing the credentials for a private repository or bucket, such as a `hf_access_token` or `gcs_service_account`.
* `kind`: The storage provider type for the model weights.
  * `"hf"` (default): Hugging Face
  * `"gcs"`: Google Cloud Storage
  * `"s3"`: AWS S3
  * `"azure"`: Azure Blob Storage

Here is an example of a well written `model_cache` for Stable Diffusion XL. Note how it only pulls the model weights that it needs using `allow_patterns`.

```yaml config.yaml theme={"system"}
model_cache:
  - repo_id: madebyollin/sdxl-vae-fp16-fix
    revision: 207b116dae70ace3637169f1ddd2434b91b3a8cd
    use_volume: true
    volume_folder: sdxl-vae-fp16
    allow_patterns:
      - config.json
      - diffusion_pytorch_model.safetensors
  - repo_id: stabilityai/stable-diffusion-xl-base-1.0
    revision: 462165984030d82259a11f4367a4eed129e94a7b
    use_volume: true
    volume_folder: stable-diffusion-xl-base
    allow_patterns:
      - "*.json"
      - "*.fp16.safetensors"
      - sd_xl_base_1.0.safetensors
  - repo_id: stabilityai/stable-diffusion-xl-refiner-1.0
    revision: 5d4cfe854c9a9a87939ff3653551c2b3c99a4356
    use_volume: true
    volume_folder: stable-diffusion-xl-refiner
    allow_patterns:
      - "*.json"
      - "*.fp16.safetensors"
      - sd_xl_refiner_1.0.safetensors
```

Many Hugging Face repos have model weights in different formats (`.bin`, `.safetensors`, `.h5`, `.msgpack`, etc.). You only need one of these most of the time. To minimize cold starts, ensure that you only cache the weights you need.

<Tip>
  ### What is weight "pre-fetching"?

  With `model_cache`, weights are pre-fetched by downloading your weights ahead of time in a dedicated Rust thread.
  This means, you can perform all kinds of preparation work (importing libraries, jit compilation of torch/triton modules), until you need access to the files.
  In practice, executing statements like `import tensorrt_llm` typically take 10–15 seconds. By that point, the first 5–10GB of the weights will have already been downloaded.
</Tip>

To use the `model_cache` config with truss,  we require you to actively interact with the `lazy_data_resolver`.
Before using any of the downloaded files, you must call the `lazy_data_resolver.block_until_download_complete()`. This will block until all files in the `/app/model_cache` directory are downloaded & ready to use.
This call must be either part of your `__init__` or `load` implementation.

```python model.py theme={"system"}
# <- download is invoked before here.
import torch # this line usually takes 2-5 seconds.
import tensorrt_llm # this line usually takes 10-15 seconds
import onnxruntime # this line usually takes 5-10 seconds

class Model:
    """example usage of `model_cache` in truss"""
    def __init__(self, *args, **kwargs):
        # `lazy_data_resolver` is passed as keyword-argument in init
        self._lazy_data_resolver = kwargs["lazy_data_resolver"]

    def load(self):
        # work that does not require the download may be done beforehand
        random_vector = torch.randn(1000)
        # important to collect the download before using any incomplete data
        self._lazy_data_resolver.block_until_download_complete()
        # after the call, you may use the /app/model_cache directory and the contents
        torch.load(
            "/app/model_cache/stable-diffusion-xl-base/model.fp16.safetensors"
        )
```

## Private Repositories/Cloud Storage

### Private Hugging Face repositories 🤗

For any public Hugging Face repo, you don't need to do anything else. Adding the `model_cache` key with an appropriate `repo_id` should be enough.

However, if you want to deploy a model from a gated repo like [Llama 2](https://huggingface.co/meta-llama/Llama-2-70b-chat-hf) to Baseten, there are a few steps you need to take:

<Steps>
  <Step title="Get Hugging Face API Key">
    [Grab an API key](https://huggingface.co/settings/tokens) from Hugging Face with `read` access. Make sure you have access to the model you want to serve.
  </Step>

  <Step title="Add it to Baseten Secrets Manager">
    Paste your API key in your [secrets manager in Baseten](https://app.baseten.co/settings/secrets) under the specified key, such as `hf_access_token`. You can read more about secrets [here](/development/model/secrets).
  </Step>

  <Step title="Update Config">
    In your Truss's `config.yaml`, add the secret key under `runtime_secret_name`:

    ```yaml config.yaml theme={"system"}
    model_cache:
    - repo_id: your-org/your-private-repo
      runtime_secret_name: hf_access_token
    ```
  </Step>
</Steps>

If you run into any issues, run through all the steps above again and make sure you did not misspell the name of the repo or secret name, or paste an incorrect API key.

### Private GCS Buckets

If you want to deploy a model from a private GCS bucket to Baseten, there are a few steps you need to take:

<Steps>
  <Step title="Get GCS Service Account Key">
    Create a [service account key](https://cloud.google.com/iam/docs/keys-create-delete#creating) in your GCS account for the project which contains the model weights.
  </Step>

  <Step title="Add it to Baseten Secrets Manager">
    Paste the contents of the `service_account.json` in your [secrets manager in Baseten](https://app.baseten.co/settings/secrets) under the specified key, e.g. `gcs_service_account`. You can read more about secrets [here](/development/model/secrets).

    At a minimum, you should have these credentials:

    ```json gcs_service_account theme={"system"}
      {
        "private_key_id": "xxxxxxx",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMI",
        "client_email": "b10-some@xxx-example.iam.gserviceaccount.com"
      }
    ```
  </Step>

  <Step title="Update Config">
    In your Truss's `config.yaml`, make sure to add the `runtime_secret_name` to your `model_cache` matching the above secret name:

    ```yaml config.yaml theme={"system"}
    model_cache:
    - repo_id: gs://your-private-bucket
      use_volume: true
      volume_folder: your-model-weights
      runtime_secret_name: gcs_service_account
      kind: "gcs"
    ```
  </Step>
</Steps>

It's easy to make a mistake in any of these steps. If you run into issues, you're encouraged to go through the steps again just in case. Please contact [Baseten support](mailto:support@baseten.co) if you continue to experience issues.

### Private S3 Buckets

If you want to deploy a model from a private S3 bucket to Baseten, there are a few steps you need to take:

<Steps>
  <Step title="Get S3 credentials">
    [Get the your `access_key_id` and `secret_access_key`](https://aws.amazon.com/blogs/security/how-to-find-update-access-keys-password-mfa-aws-management-console/) in your AWS account for the bucket that contains the model weights.
  </Step>

  <Step title="Add them to Baseten Secrets Manager">
    Paste the following `json` in your [secrets manager in Baseten](https://app.baseten.co/settings/secrets) under the specified key, e.g. `aws_secret_json`. You can read more about secrets [here](/development/model/secrets).

    ```json aws_secret_json theme={"system"}
      {
        "access_key_id": "XXXXX",
        "secret_access_key": "xxxxx/xxxxxx",
        "region": "us-west-2"
      }
    ```
  </Step>

  <Step title="Update Config">
    In your Truss's `config.yaml`, make sure to add the `runtime_secret_name` to your `model_cache` matching the above secret name:

    ```yaml config.yaml theme={"system"}
    model_cache:
    - repo_id: s3://your-private-bucket
      use_volume: true
      volume_folder: your-model-weights
      runtime_secret_name: aws_secret_json
      kind: "s3"
    ```
  </Step>
</Steps>

It's easy to make a mistake in any of these steps. If you run into issues, you're encouraged to go through the steps again just in case. Please contact [Baseten support](mailto:support@baseten.co) if you continue to experience issues.

### Private Azure Containers

If you want to deploy a model from a private Azure container to Baseten, there are a few steps you need to take:

<Steps>
  <Step title="Get Azure credentials">
    [Get the your `account_key`](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-get-info?tabs=portal#get-a-connection-string-for-the-storage-account) in your Azure account with the container that has the model weights.
  </Step>

  <Step title="Add them to Baseten Secrets Manager">
    Paste the following `json` in your [secrets manager in Baseten](https://app.baseten.co/settings/secrets) under the specified key, e.g. `azure_secret_json`. You can read more about secrets [here](/development/model/secrets).

    ```json azure_secret_json theme={"system"}
      {
          "account_key": "xxxxx",
      }
    ```
  </Step>

  <Step title="Update Config">
    In your Truss's `config.yaml`, make sure to add the `runtime_secret_name` to your `model_cache` matching the above secret name:

    ```yaml config.yaml theme={"system"}
    model_cache:
    - repo_id: az://your-private-container
      use_volume: true
      volume_folder: your-model-weights
      runtime_secret_name: azure_secret_json
      kind: "azure"
    ```
  </Step>
</Steps>

It's easy to make a mistake in any of these steps. If you run into issues, you're encouraged to go through the steps again just in case. Please contact [Baseten support](mailto:support@baseten.co) if you continue to experience issues.

## `model_cache` within Chains

To use `model_cache` for [chains](/development/chain/getting-started) - use the `Assets` specifier. In the example below, we will download `llama-3.2-1B`.
As this model is a gated huggingface model, we are setting the mounting token as part of the assets `chains.Assets(..., secret_keys=["hf_access_token"])`.
The model is quite small - in many cases, we will be able to download the model while `from transformers import pipeline` and `import torch` are running.

```python chain_cache.py theme={"system"}
import random
import truss_chains as chains

try:
    # imports on global level for PoemGeneratorLM, to save time during the download.
    from transformers import pipeline
    import torch
except ImportError:
    # RandInt does not have these dependencies.
    pass

class RandInt(chains.ChainletBase):
    async def run_remote(self, max_value: int) -> int:
        return random.randint(1, max_value)

@chains.mark_entrypoint
class PoemGeneratorLM(chains.ChainletBase):
    from truss import truss_config
    LLAMA_CACHE = truss_config.ModelRepo(
        repo_id="meta-llama/Llama-3.2-1B-Instruct",
        revision="c4219cc9e642e492fd0219283fa3c674804bb8ed",
        use_volume=True,
        volume_folder="llama_mini",
        ignore_patterns=["*.pth", "*.onnx"]
    )
    remote_config = chains.RemoteConfig(
        docker_image=chains.DockerImage(
            # The phi model needs some extra python packages.
            pip_requirements=[
                "transformers==4.48.0",
                "torch==2.6.0",
            ]
        ),
        compute=chains.Compute(
            gpu="L4"
        ),
        # The phi model needs a GPU and more CPUs.
        # compute=chains.Compute(cpu_count=2, gpu="T4"),
        # Cache the model weights in the image
        assets=chains.Assets(cached=[LLAMA_CACHE], secret_keys=["hf_access_token"]),
    )
    # <- Download happens before __init__ is called.
    def __init__(self, rand_int=chains.depends(RandInt, retries=3)) -> None:
        self._rand_int = rand_int
        print("loading cached llama_mini model")
        self.pipeline = pipeline(
            "text-generation",
            model=f"/app/model_cache/llama_mini",
        )

    async def run_remote(self, max_value: int = 3) -> str:
        num_repetitions = await self._rand_int.run_remote(max_value)
        print("writing poem with num_repetitions", num_repetitions)
        poem = str(self.pipeline(
            text_inputs="Write a beautiful and descriptive poem about the ocean. Focus on its vastness, movement, and colors.",
            max_new_tokens=150,
            do_sample=True,
            return_full_text=False,
            temperature=0.7,
            top_p=0.9,
        )[0]['generated_text'])
        return poem * num_repetitions
```

## `model_cache` for custom servers

If you are not using Python's `model.py` and [custom servers](/development/model/custom-server) such as [vllm](/examples/vllm), TEI or [sglang](/examples/sglang),
you are required to use the `truss-transfer-cli` command, to force population of the `/app/model_cache` location. The command will block until the weights are downloaded.

Here is an example for how to use text-embeddings-inference on a L4 to populate a jina embeddings model from huggingface into the model\_cache.

```yaml config.yaml theme={"system"}
base_image:
  image: baseten/text-embeddings-inference-mirror:89-1.6
docker_server:
  liveness_endpoint: /health
  predict_endpoint: /v1/embeddings
  readiness_endpoint: /health
  server_port: 7997
  # using `truss-transfer-cli` to download the weights to `cached_model`
  start_command: bash -c "truss-transfer-cli && text-embeddings-router --port 7997
    --model-id /app/model_cache/my_jina --max-client-batch-size 128 --max-concurrent-requests
    128 --max-batch-tokens 16384 --auto-truncate"
model_cache:
- repo_id: jinaai/jina-embeddings-v2-base-code
  revision: 516f4baf13dec4ddddda8631e019b5737c8bc250
  use_volume: true
  volume_folder: my_jina
  ignore_patterns: ["*.onnx"]
model_metadata:
  example_model_input:
    encoding_format: float
    input: text string
    model: model
model_name: TEI-jinaai-jina-embeddings-v2-base-code-truss-example
resources:
  accelerator: L4
```

## Optimizing cache hits and access time futher with b10cache enabled

<Warning>
  Requires `use_volume: true` and [b10cache](/development/model/b10cache) enabled. Without b10cache enabled, scaling the model with download the weights again.
</Warning>

To further reduce weights loading time, we can enable Baseten's Distributed Filesystem (b10cache) for your account.
You can validate that this is enabled for your account by viewing the logs of your deployment.

```
[2025-09-10 01:04:35] [INFO ] b10cache is enabled.
[2025-09-10 01:04:35] [INFO ] Symlink created successfully. Skipping download for /app/model_cache/cached_model/model.safetensors
```

<Tip>
  Once b10cache is active, we will skip downloads that are cached in the distributed filesystem of the region your deployment is running in.
  b10cache acts like a content delivery network: Initial cache misses are populating the filesystem, unused files are garbage collected 4 days after their last usage.
  Once b10cache is active, it will pull from the fastest source. If another pod is active on the same physical node, artifacts may be hot-cached, and shared among your deployments.
  Downloads are fully isolated from other organizations. Modifying downloaded artifacts inplace / without copy is not recommended.
</Tip>

If b10cache is not available for your account, we will provision the model\_cache with a optimized download from HuggingFace.co.
The download is parallellized, achieving typical download speeds of greater than 1GB/s on a 10Gbit ethernet connection.
If you want to enable b10cache, feel free to reach out to our support.
