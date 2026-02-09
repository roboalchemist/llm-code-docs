# Source: https://docs.baseten.co/training/concepts/checkpointing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Checkpointing

> Learn how to use Baseten's checkpointing feature to manage model checkpoints and avoid disk errors during training.

With checkpointing enabled, you can manage your model checkpoints seamlessly and avoid common training issues.

## Benefits of Checkpointing

* **Avoid catastrophic out of disk errors**: We mount additional storage at the checkpointing directory to help avoid out of disk errors during your training run.
* **Maximize GPU utilization**: When checkpointing is enabled, any data written to the checkpointing directory will be uploaded to the cloud by a separate process, allowing you to maximize GPU time spent training.
* **Seamless checkpoint management**: Checkpoints are automatically uploaded to cloud storage for easy access and management.

## Enabling Checkpointing

To enable checkpointing, add a `CheckpointingConfig` to the `Runtime` and set `enabled` to `True`:

```python  theme={"system"}
from truss_train import definitions

training_runtime = definitions.Runtime(
    # ... other configuration options
    checkpointing_config=definitions.CheckpointingConfig(enabled=True)
)
```

## Using the Checkpoint Directory

Baseten will automatically export the [`$BT_CHECKPOINT_DIR`](/reference/sdk/training#baseten-provided-environment-variables) environment variable in your job's environment.

<Danger>
  **Write your checkpoints to the `$BT_CHECKPOINT_DIR` directory so Baseten can automatically backup and preserve them.**
</Danger>

## Serving Checkpoints

Once your training is complete, you can serve your model checkpoints using Baseten's serving infrastructure. Learn more about [serving checkpoints](/training/deployment).

<Warning>
  When you delete a job or project, all undeployed checkpoints are permanently deleted with no archival or recovery option. Deployed checkpoints aren't affected. See [Management](/training/management) for details.
</Warning>
