# Source: https://docs.baseten.co/training/concepts/cache.md

# Cache

> Learn how to use the training cache to speed up your training iterations by persisting data between jobs.

The training cache enables you to persist data between training jobs. This can significantly improve iteration speed by skipping expensive downloads and data transformations.

## How to Use the Training Cache

Set the cache configuration in your `Runtime`:

```python  theme={"system"}
from truss_train import definitions

training_runtime = definitions.Runtime(
    # ... other configuration options
    cache_config=definitions.CacheConfig(enabled=True)
)
```

## Cache Directory

The cache will be mounted at `/root/.cache/user_artifacts`, which can be accessed via the [`$BT_RW_CACHE_DIR`](/reference/sdk/training#baseten-provided-environment-variables) environment variable.

## Legacy HF Cache

We recommend using the new cache directory at `/root/.cache/user_artifacts` instead. However, if you need to access data mounted to `/root/.cache/huggingface` for compatibility reasons, you can set `enable_legacy_hf_mount=True` in your `CacheConfig`. Note that this legacy option is not recommended for new projects.

## Seeding Your Data

For multi-gpu training, you should ensure that your data is seeded before running multi-process training jobs. You can do this by separating your training script into training script and data loading script.

## Performance Benefits

For a 400 GB HF Dataset, you can expect to save *nearly an hour* of compute time for each job - data download and preparation have been done already!

## Cache Management

You can inspect the contents of the cache through CLI with `truss train cache summarize <project_name or project_id>`. This visibility into what's in the cache can help you verify your code is working as expected, and additionally manage files and artifacts you no longer need.
