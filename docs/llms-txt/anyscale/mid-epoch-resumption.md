# Source: https://docs.anyscale.com/runtime/mid-epoch-resumption.md

# Mid-epoch training resumption

[View Markdown](/runtime/mid-epoch-resumption.md)

# Mid-epoch training resumption

note

This feature is available as a beta release. This feature requires Ray 2.50.0 or later.

Ray Train in the Anyscale Runtime supports mid-epoch training resumption, enabling training jobs to resume from their previous dataset iteration state after interruption. This feature ensures your training job processes each data sample exactly once per epoch, even when failures, preemptions, or manual stops interrupt training.

This feature addresses the following issues:

* If you reload model weights but restart data iteration from the beginning of the epoch, you experience data imbalance due to processing some samples multiple times.
* Configurations that let you skip batches until you reach the restored batch index waste computation. For example, see [Hugging Face docs](https://huggingface.co/docs/transformers/v4.56.2/en/main_classes/trainer#transformers.TrainingArguments.set_dataloader.ignore_data_skip).

You enable checkpointing at the dataset level. Mid-epoch resumption integrates seamlessly with PyTorch Lightning, Hugging Face Transformers, and custom training loops. During training, the feature has minimal performance overhead through asynchronous checkpoint writes. During restoration, there's some overhead to read the data checkpoint files and filter out seen rows, but this overhead is still less than the baseline of skipping batches.

## Requirements[​](#requirements "Direct link to Requirements")

Your data and workloads must fulfill the following requirements:

* **Row identifiers**: Your dataset must include a column with unique row IDs, or use Parquet datasets with `generate_id_column=True`.
* **Supported operations**: Use only map-based transformations that don't increase the number of rows, such as `map`, `map_batches`, and `filter`.
  <!-- -->
  * Map transformations must pass along the ID column to the end of the pipeline.
* **Storage**: Store data iteration checkpoint metadata alongside model checkpoints to ensure atomicity of the model and data iteration state.

## Enable mid-epoch resumption[​](#enable-mid-epoch-resumption "Direct link to Enable mid-epoch resumption")

To enable mid-epoch resumption, you must do the following:

* Configure your training function to look for checkpoint information on initialization and load it when present.
* Save your dataset iterator state alongside your model checkpoints.
* Specify an ID column for your training dataset to `DataConfig.dataset_checkpoint_configs`.
* Set a storage path for your trainer to a shared storage location available to all workers for checkpointing.
* Enable Ray Train fault tolerance.

This allows `ray.train.report()` to save model and data iterator states atomically. On restart, Ray Train restores the iterator and skips forward to the saved position.

## Mid-epoch resumption example[​](#mid-epoch-resumption-example "Direct link to Mid-epoch resumption example")

The following code example demonstrates patterns for configuring checkpointing and resumption:

```
import os
os.environ["RAY_TRAIN_V2_ENABLED"] = "1"

import time
import tempfile

import ray
import ray.train
from ray.train.torch import TorchTrainer
import torch


def train_fn_per_worker(config):
    model_state = {"steps": 0}  # Dummy model state

    data_state_dict = None
    checkpoint = ray.train.get_checkpoint()
    restored = bool(checkpoint)
    if checkpoint:
        with checkpoint.as_directory() as temp_checkpoint_dir:
            model_path = os.path.join(temp_checkpoint_dir, "model.pt")
            data_path = os.path.join(temp_checkpoint_dir, "data.pt")
            model_state = torch.load(model_path)
            data_state_dict = torch.load(data_path)
            print(f"Loaded checkpoint:", model_state)

    # =============================================================
    # Change 1: Load the data state dict from the latest checkpoint
    # if one exists.
    # =============================================================
    ds_shard = ray.train.get_dataset_shard("train", state_dict=data_state_dict)

    checkpoint_every_n_batches = 10
    num_epochs = 2

    def save_checkpoint(model_state, ds_state):
        with tempfile.TemporaryDirectory() as temp_checkpoint_dir:
            checkpoint = None

            if ray.train.get_context().get_world_rank() == 0:
                torch.save(model_state, os.path.join(temp_checkpoint_dir, "model.pt"))
                torch.save(ds_state, os.path.join(temp_checkpoint_dir, "data.pt"))
                checkpoint = ray.train.Checkpoint.from_directory(temp_checkpoint_dir)

            print(f"Saved checkpoint:", model_state)
            ray.train.report(
                {"epoch": epoch, "batch_idx": batch_idx},
                checkpoint=checkpoint
            )

    for epoch in range(num_epochs):
        print(f"Starting {epoch=}")

        for batch_idx, batch in enumerate(ds_shard.iter_batches(batch_size=100)):
            if epoch == 0 and batch_idx == 50 and not restored:
                raise RuntimeError("Mid-epoch error to demonstrate resumption:", model_state)

            # Simulate training work
            time.sleep(0.01)
            model_state["steps"] += 1

            # Mid-epoch checkpoint
            if (batch_idx + 1) % checkpoint_every_n_batches == 0:
                # =============================================================
                # Change 2: During your mid-epoch checkpoints, save the dataset
                # iterator state dict alongside your model checkpoint.
                # =============================================================
                save_checkpoint(model_state, ds_shard.state_dict())

        # End-of-epoch checkpoint
        save_checkpoint(model_state, ds_shard.state_dict())


if __name__ == "__main__":
    # =============================================================
    # Change 3: Configure the DataConfig(dataset_checkpoint_configs)
    # for the training dataset.
    # =============================================================
    data_config = ray.train.DataConfig(
        dataset_checkpoint_configs={
            "train": ray.train.DatasetCheckpointConfig(
                id_column="id", generate_id_column=True,
            )
        }
    )

    ds = ray.data.read_parquet("s3://anonymous@air-example-data/cifar-10/parquet/train/")

    trainer = TorchTrainer(
        train_fn_per_worker,
        scaling_config=ray.train.ScalingConfig(num_workers=4),
        datasets={"train": ds},
        dataset_config=data_config,
        run_config=ray.train.RunConfig(
            # =============================================================
            # Change 4: Set storage_path to a shared storage location where
            # all workers can write checkpoint files (such as S3 or NFS).
            # =============================================================
            storage_path="/mnt/cluster_storage",

            # =============================================================
            # Change 5: Enable Ray Train fault tolerance by setting
            # max_failures > 0
            # =============================================================
            failure_config=ray.train.FailureConfig(max_failures=1),
        )
    )

    result = trainer.fit()
```

## API reference[​](#api-reference "Direct link to API reference")

```
ray.train.get_dataset_shard(dataset_name: str, state_dict: Optional[Dict] = None) -> DataIterator
```

Arguments:

* `dataset_name`: The key of the dataset in the dict passed into the trainer's datasets argument.
* `state_dict`: A state dictionary produced by `DataIterator.state_dict()` when resuming from a mid-epoch checkpoint. Only rank 0 should pass this value—Ray Train ignores state dicts from other ranks. If not provided, iteration starts from the beginning.

Returns:

* `DataIterator`: An iterator yielding batches from the specified dataset shard, aligned to the current worker.

```
DataIterator.state_dict() -> Dict
```

Returns:

* `Dict`: A state dictionary capturing information needed to resume iteration from the current point. You should save this dict alongside the model checkpoint and later pass it back into get\_dataset\_shard.

Notes:

* You **must call this method on every rank at the same time** to synchronize global batch iteration state.

```
DatasetCheckpointConfig(
    id_column: str
    generate_id_column: bool = False
    checkpoint_path: Optional[str] = None
    override_filesystem: Optional[pyarrow.fs.FileSystem] = None
    delete_checkpoints_after_epoch: bool = True
)
```

Arguments:

* `id_column`: Name of the ID column in the input dataset. ID values must be unique across all rows in the dataset and must persist during all operators.
* `generate_id_column`: Whether to generate the `id_column` for each row. Use this when you don't have a pre-existing `id_column` in the input dataset. Ray Train only supports Parquet files based data sources for auto-generated row IDs feature.
* `checkpoint_path`: Path to store the checkpoint data. It can be a path to a cloud object storage (for example, `s3://bucket/path`) or a file system path. If the latter, the path must be a network-mounted file system (for example, `/mnt/cluster_storage/`) that's accessible to the entire cluster. If not set, defaults to `{RunConfig.storage_path}/{RunConfig.name}` configured on the `ray.train` trainer.
* `override_filesystem`: Override the [`pyarrow.fs.FileSystem`](https://arrow.apache.org/docs/python/generated/pyarrow.fs.FileSystem.html) object used to read or write checkpoint data. Use this when you want to use custom credentials. If unset, this defaults to the filesystem configured in the `ray.train.RunConfig` passed to the trainer.
* `delete_checkpoints_after_epoch`: If True, automatically delete checkpoint data after each epoch completes. This allows for fault tolerance from the latest checkpoint. If you intend to resume from a checkpoint prior to the latest epoch, set this to False. Defaults to True.
