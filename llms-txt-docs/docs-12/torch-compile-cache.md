# Source: https://docs.baseten.co/development/model/torch-compile-cache.md

# Torch Compile Caching 🆕

> Accelerate cold starts by loading in previous compilation artifacts.

<Warning>
  ### Requires [b10cache](/development/model/b10cache) enabled
</Warning>

## Overview

PyTorch's `torch.compile` feature offers significant performance improvements for inference workloads, reducing inference time by up to 40%. However, this optimization comes with a trade-off: the initial compilation process adds considerable latency to cold starts, as the model must be compiled before serving its first inference request.

This compilation overhead becomes particularly problematic in production environments where:

* Models frequently scale up and down based on demand
* New pods are regularly spawned to handle traffic spikes
* Each new instance must repeat the compilation process from scratch

## Solution

Persist compilation artifacts across deployments and pod restarts, by storing them in [b10cache](/development/model/b10cache). When a new pod starts up, it can load previously compiled artifacts instead of recompiling from scratch. The library gracefully handles large scale ups, managing race conditions and ensuring fault-tolerance in the shared b10cache.

In practice, this strategy slashes compilation latencies to just around 5-20 seconds, depending on the model.

***

## Implementation Options

There are two different deployment patterns that benefit from torch compile caching:

<Tip>
  * **Truss Models**: `model.py` calling `torch.compile` ([Jump to](#truss-models-model-py))
  * **vLLM Servers**: vLLM custom server ([Jump to](#vllm-servers-cli-tool))
</Tip>

***

## Truss Models (`model.py`)

### API Reference

We expose two API calls that return an `OperationStatus` object to help you control program flow based on the result.

<Accordion title="load_compile_cache()">
  If you have previously saved compilation cache for this model, load it to speed up the compilation for the model on this pod.

  **Returns:**

  * `OperationStatus.SUCCESS` → successful load
  * `OperationStatus.SKIPPED` → if torch compilation artifacts already exist on the pod
  * `OperationStatus.ERROR` → general catch-all errors
  * `OperationStatus.DOES_NOT_EXIST` → if no cache file was found
</Accordion>

<Accordion title="save_compile_cache()">
  Save your model's torch compilation cache for future use. This should be called after running prompts to warm up your model and trigger compilation.

  **Returns:**

  * `OperationStatus.SUCCESS` → successful save
  * `OperationStatus.SKIPPED` → skipped because compile cache already exists in shared directory
  * `OperationStatus.ERROR` → general catch-all errors
</Accordion>

### Implementation Example

Here is an example of compile caching for Flux, an image generation model. Note how we save the result of `load_compile_cache` to inform on whether to `save_compile_cache`.

#### Step 1: Update `config.yaml`

Under requirements, add `b10-transfer`:

```yaml  theme={"system"}
requirements:
  - b10-transfer
```

#### Step 2: Update `model.py`

Import the library and use the two functions to speed up torch compilation time:

```python  theme={"system"}
from b10_transfer import load_compile_cache, save_compile_cache, OperationStatus

class Model:
    def load(self):
        self.pipe = FluxPipeline.from_pretrained(
            self.model_name, torch_dtype=torch.bfloat16, token=self.hf_access_token
        ).to("cuda")

        # Try to load compile cache
        cache_loaded: OperationStatus = load_compile_cache()

        if cache_loaded == OperationStatus.ERROR:
            logging.info("Run in eager mode, skipping torch compile")
        else:
            logging.info("Compiling the model for performance optimization")
            self.pipe.transformer = torch.compile(
                self.pipe.transformer, mode="max-autotune-no-cudagraphs", dynamic=False
            )

            self.pipe.vae.decode = torch.compile(
                self.pipe.vae.decode, mode="max-autotune-no-cudagraphs", dynamic=False
            )

            seed = random.randint(0, MAX_SEED)
            generator = torch.Generator().manual_seed(seed)
            start_time = time.time()
            # Warmup the model with dummy prompts, also triggering compilation
            self.pipe(
                prompt="dummy prompt",
                prompt_2=None,
                guidance_scale=0.0,
                max_sequence_length=256,
                num_inference_steps=4,
                width=1024,
                height=1024,
                output_type="pil",
                generator=generator
            )

            end_time = time.time()

            logging.info(
                f"Warmup completed in {(end_time - start_time)} seconds. "
                "This is expected to take a few minutes on the first run."
            )

            if cache_loaded != OperationStatus.SUCCESS:
                # Save compile cache for future runs
                outcome: OperationStatus = save_compile_cache()
```

<Note>
  See the [full example](https://github.com/basetenlabs/truss-examples/tree/main/flux/schnell).
</Note>

***

## vLLM Servers (CLI Tool)

### Overview

This should be used whenever using compile options with vLLM. On vLLM V1, compiling is the default behavior. This command line tool spawns a process that is completely automatic—it loads the compile cache if you have saved it before, and if not, it will save the compile cache.

### Implementation

There are two changes to make in `config.yaml`:

#### Step 1: Add Requirements

Under requirements, add `b10-transfer`:

```yaml  theme={"system"}
requirements:
  - b10-transfer
```

#### Step 2: Update Start Command

Under start command, add `b10-compile-cache &` right before the `vllm serve` call:

```yaml  theme={"system"}
start_command: "... b10-compile-cache & vllm serve ..."
```

<Note>
  See the [full example](https://github.com/basetenlabs/truss-examples/tree/main/mistral/mistral-small-3.1).
</Note>

***

## Advanced Configuration

<Accordion title="Parameter Overrides">
  The torch compile caching library supports several environment variables for fine-tuning behavior in production environments:

  ### Cache Directory Configuration

  **`TORCHINDUCTOR_CACHE_DIR`** (optional)

  * **Default**: `/tmp/torchinductor_<username>`
  * **Description**: Directory where PyTorch stores compilation artifacts locally
  * **Allowed prefixes**: `/tmp/`, `/cache/`, `~/.cache`
  * **Usage**: Set this if you need to customize where torch compilation artifacts are stored on the local filesystem

  **`B10FS_CACHE_DIR`** (optional)

  * **Default**: Derived from b10cache mount point + `/compile_cache`
  * **Description**: Directory in b10cache where compilation artifacts are persisted across deployments
  * **Usage**: Typically doesn't need to be changed as it's automatically configured based on your b10cache setup

  **`LOCAL_WORK_DIR`** (optional)

  * **Default**: `/app`
  * **Description**: Local working directory for temporary operations
  * **Allowed prefixes**: `/app/`, `/tmp/`, `/cache/`

  ### Performance and Resource Limits

  **`MAX_CACHE_SIZE_MB`** (optional)

  * **Default**: `1024` (1GB)
  * **Cap**: Limited by `MAX_CACHE_SIZE_CAP_MB` for safety
  * **Description**: Maximum size of a single cache archive in megabytes
  * **Usage**: Increase for larger models with extensive compilation artifacts, decrease to save storage

  **`MAX_CONCURRENT_SAVES`** (optional)

  * **Default**: `50`
  * **Cap**: Limited by `MAX_CONCURRENT_SAVES_CAP` for safety
  * **Description**: Maximum number of concurrent save operations allowed
  * **Usage**: Tune based on your deployment's concurrency requirements and storage performance

  ### Cleanup and Maintenance

  **`CLEANUP_LOCK_TIMEOUT_SECONDS`** (optional)

  * **Default**: `30`
  * **Cap**: Limited by `LOCK_TIMEOUT_CAP_SECONDS`
  * **Description**: Timeout for cleaning up stale lock files, to prevent deadlocks. They may occur when a replica holding the lock crashes.
  * **Usage**: Decrease if you're experiencing deadlocks in high-load scenarios

  **`CLEANUP_INCOMPLETE_TIMEOUT_SECONDS`** (optional)

  * **Default**: `60`
  * **Cap**: Limited by `INCOMPLETE_TIMEOUT_CAP_SECONDS`
  * **Description**: Timeout for cleaning up incomplete cache files
  * **Usage**: Increase for slower storage systems or larger cache files

  ### Example Configuration

  ```yaml  theme={"system"}
  # config.yaml
  environment_variables:
    MAX_CACHE_SIZE_MB: "2048"
    MAX_CONCURRENT_SAVES: "25"
    CLEANUP_LOCK_TIMEOUT_SECONDS: "45"
  ```

  <Note>
    Most users won't need to modify these settings. The defaults are optimized for typical production workloads. Only adjust these values if you're experiencing specific performance issues or have unusual deployment requirements.
  </Note>
</Accordion>

***

## Further Reading

To understand implementation details, read more [here](https://docs.pytorch.org/tutorials/recipes/torch_compile_caching_tutorial.html).
