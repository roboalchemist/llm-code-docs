# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/resiliency.html.md

Title: Resiliency Features — NVIDIA NeMo Framework User Guide

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/resiliency.html

Published Time: Thu, 30 Oct 2025 07:07:34 GMT

Markdown Content:
Resiliency Features[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/resiliency.html.md#resiliency-features "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------

NeMo Framework incorporates resilient training features from the [NVIDIA Resiliency Extension](https://github.com/NVIDIA/nvidia-resiliency-ext). This extension provides fault-tolerant capabilities that help minimize downtime due to failures and interruptions during training.

The key features include:

*   Fault Tolerance: Automatically resumes training from the last checkpoint in case of interruptions.

*   Straggler Detection: Identifies and mitigates slow-performing nodes to ensure efficient training.

*   Local Checkpointing: Saves checkpoints directly to local storage on each node.

For more information on the design and use of these features, please see the Resiliency Extension’s [documentation](https://nvidia.github.io/nvidia-resiliency-ext/).

Fault Tolerance[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/resiliency.html.md#fault-tolerance "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------

The Resiliency Extension’s Fault Tolerance subpackage can detect hangs during training and automatically restart a workload due to a hang or error. This is useful if transient faults are common, for example, if training on unreliable hardware or at a very large scale.

### Use Fault Tolerance Features[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/resiliency.html.md#use-fault-tolerance-features "Link to this heading")

Warning

This plugin is currently only supported on Slurm-based clusters.

The package contains a PyTorch Lightning callback, `FaultToleranceCallback`, and the `ft_launcher`, a launcher similar to `torchrun`. To use the features mentioned above, the callback must be added to the trainer and the workload must be launched with the `ft_launcher`. We’ve provided a NeMo-Run plugin to simplify this integration to one step. Please note that [NeMo-Run](https://github.com/NVIDIA/NeMo-Run) must be installed to use this plugin.

The following example adds the plugin to the LLaMA3 8B recipe:

from nemo import lightning as nl
from nemo.collections import llm
from nemo.lightning.run.plugins import FaultTolerancePlugin

recipe = llm.llama3_8b.pretrain_recipe(name="llama3_with_fault_tolerance", ...) # fill in other recipe arguments

...

executor = # set up your NeMo-Run executor

...

run_plugins = [FaultTolerancePlugin()]
run.run(recipe, plugins=run_plugins, executor=executor)

When using this feature, if a hang is encountered, you should see log statements similar to the following:

[WARNING] [RankMonitorServer:34] Did not get subsequent heartbeat. Waited 171.92 seconds.
[WARNING] [RankMonitorServer:58] Did not get subsequent heartbeat. Waited 171.92 seconds.
torch.distributed.elastic.multiprocessing.api: [WARNING] Sending process 453152 closing signal SIGTERM
torch.distributed.elastic.multiprocessing.api: [WARNING] Sending process 453157 closing signal SIGTERM

### Default Settings[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/resiliency.html.md#default-settings "Link to this heading")

The NeMo-Run plugin will configure `FaultToleranceCallback` with `autoresume=True` and `calculate_timeout=True`. The `autoresume` setting is necessary to automatically launch another job in case of a fault or if training is not complete, which is expected to be useful for most users. This feature also makes training more hands-off when a long training session cannot complete within a single job’s time limit. The `calculate_timeout` setting automatically calculates the thresholds used to determine if the job is stuck in a hang, simplifying the user experience. Therefore, we have enabled it by default.

We’ve also limited the default maximum successive in-job restarts (`num_in_job_restarts`) to 3 and job retries (`num_job_retries_on_failure`) to 2. In our experience, when failures occur more frequently than this, there is usually a non-transient application issue that needs to be addressed. These are arguments to the plugin, so you can adjust them as needed.

Straggler Detection[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/resiliency.html.md#straggler-detection "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------

The Resiliency Extension’s Straggler Detection functionality detects slow-performing ranks and terminates the training if the performance of any rank falls below a user-specified threshold.

### Use Straggler Detection Features[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/resiliency.html.md#use-straggler-detection-features "Link to this heading")

The package provides a PyTorch Lightning callback, which makes this feature easy to use with NeMo. We’ve provided a recipe for configuration of this callback. See the following usage example:

from nemo import lightning as nl
from nemo.collections import llm
from nemo.collections.llm.recipes.callbacks import straggler_det_callback

trainer = nl.Trainer()
straggler_cb = straggler_det_callback()
trainer.callbacks.append(straggler_cb)

When using this feature, the training log should contain performance reports similar to the following:

GPU relative performance:
 Worst performing 5/512 ranks:
  Rank=76 Node=h100-001-253-012 Score=0.94
  Rank=13 Node=h100-001-010-003 Score=0.94
  Rank=45 Node=h100-001-172-026 Score=0.94
  Rank=433 Node=h100-004-141-026 Score=0.95
  Rank=308 Node=h100-003-263-012 Score=0.95
 Best performing 5/512 ranks:
  Rank=432 Node=h100-004-141-026 Score=0.99
  Rank=376 Node=h100-004-005-003 Score=0.98
  Rank=487 Node=h100-004-255-026 Score=0.98
  Rank=369 Node=h100-004-004-033 Score=0.98
  Rank=361 Node=h100-004-004-023 Score=0.98

GPU individual performance:
 Worst performing 5/512 ranks:
  Rank=76 Node=h100-001-253-012 Score=0.98
  Rank=162 Node=h100-002-042-026 Score=0.98
  Rank=79 Node=h100-001-253-012 Score=0.98
  Rank=357 Node=h100-004-004-013 Score=0.98
  Rank=85 Node=h100-001-253-026 Score=0.98
 Best performing 5/512 ranks:
  Rank=297 Node=h100-003-095-026 Score=1.00
  Rank=123 Node=h100-001-273-026 Score=1.00
  Rank=21 Node=h100-001-010-013 Score=1.00
  Rank=389 Node=h100-004-074-012 Score=1.00
  Rank=489 Node=h100-004-269-026 Score=1.00

 Straggler report processing time: 0.042 sec.

If Weights and Biases logging is configured (e.g. by using `nemo.lightning.run.plugins.WandbPlugin`), the WandB run will contain plots for the minimum, maximum, and median scores across ranks, for both individual and relative performance.

![Image 1: _images/straggler_plots.png](https://docs.nvidia.com/nemo-framework/user-guide/latest/_images/straggler_plots.png)
### Default Settings[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/resiliency.html.md#id2 "Link to this heading")

The callback recipe exposes the following arguments:

*   `straggler_report_time_interval` is the performance score reporting frequency in seconds, with a default of 300 seconds. We do not see any significant impact on training throughput while training Llama 3.1 models on up to 1,000 H100 GPUs with `straggler_det_callback` enabled and the reporting time set to 300 seconds. Feel free to increase or decrease this frequency based on your workload and any observed overheads.

*   `stop_if_detected_straggler` decides whether to stop training if a straggler is detected. This is enabled to ensure that training is stopped if there are stragglers, but can be disabled by setting to False if training should proceed even with stragglers.

When using the callback recipe, both the individual GPU performance scores and the relative GPU performance scores are calculated and the top 5 scores for each are printed in the log, which is set by `num_gpu_perf_scores_to_print=5`. Also, a score below 0.7 means that the rank is a straggler, which is determined by `gpu_relative_perf_threshold` and `gpu_individual_perf_threshold`. This value of 0.7 is set based on the defaults in the nvidia-resiliency-extension package. If you would like more control over this behavior, you can always directly configure the `StragglerDetectionCallback`.

Local Checkpointing[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/resiliency.html.md#local-checkpointing "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------

Local checkpointing saves model checkpoints directly to storage on each node (e.g., local SSDs or RAM disks), instead of relying solely on a shared network filesystem. This approach can significantly speed up the saving process and reduce the load on shared storage infrastructure.

Key features leveraged from the extension include:

*   Local Saving: Each node saves its part of the checkpoint locally.

*   Synchronous and Asynchronous Support: Saving can happen synchronously or asynchronously. In NeMo, this mirrors the configuration used for global checkpoints.

*   Automatic Cleanup: Handles the removal of outdated or incomplete local checkpoints.

*   Optional Replication: For multi-node jobs, checkpoints are replicated to other nodes (LazyCliqueReplicationStrategy) to allow recovery even if a node fails after saving. Single-node jobs do not use replication.

*   Automated Loading: When resuming, the framework automatically finds the latest valid checkpoint, comparing local and global checkpoints, and retrieves any needed parts across nodes.

### Use Local Checkpointing Features[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/resiliency.html.md#use-local-checkpointing-features "Link to this heading")

Note

This integration currently only works with Megatron Core models and requires using the MegatronStrategy.

To enable local checkpointing in NeMo, add the LocalCheckpointCallback from the Resiliency Extension to your PyTorch Lightning Trainer.

from nemo import lightning as nl
from nemo.lightning.pytorch.local_ckpt import update_trainer_local_checkpoint_io

# Define a function to extract the iteration number from a globally saved checkpoint path
def get_iteration_from_checkpoint(checkpoint_path: str) -> int:
   ...

# Define the base directory for local checkpoints on each node's filesystem
local_checkpoint_dir = "/path/to/local/node/storage/checkpoints"

# Pass any additional kwargs to the update function
# Trainer should have the local checkpoint callback added
# e.g. trainer = nl.Trainer(callbacks=[LocalCheckpointCallback(every_n_train_steps=10)], ...)
update_trainer_local_checkpoint_io(trainer, local_checkpoint_dir, get_iteration_from_checkpoint, **kwargs)

# ... rest of the training

Note

An example implementation for extracting the iteration from a checkpoint path, suitable for use as `get_iteration_from_checkpoint`, can be found in [nemo/collections/llm/recipes/log/default.py](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/recipes/log/default.py) as `get_global_step_from_global_checkpoint_path`. This function is designed to work with the default NeMo checkpoint naming convention for recipes under the LLM collection. If using a customized name format, write a corresponding implementation.

### Configuration[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/resiliency.html.md#configuration "Link to this heading")

The primary configuration needed is the local_checkpoint_base_dir argument passed to update_trainer_local_checkpoint_io. This specifies the root directory _on each node’s local filesystem_ where checkpoints will be stored. The actual path used on a node will be <base_dir>/local_ckpt/<hostname>. Ensure this path points to a fast local storage medium for best performance.

Other aspects are configured automatically:

*   Asynchronous Saving: Local checkpoint saving will be asynchronous if asynchronous saving is enabled for global checkpoints (i.e., if trainer.strategy.async_save is True).

*   Replication: Replication strategy is automatically chosen based on the number of nodes used for training. (Lazy Clique Replication for >1 node, None for 1 node).

Preemption[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/resiliency.html.md#preemption "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------

Training a foundation model can take several hours or even days to complete. In some cases, training jobs must be halted preemptively due to cluster time limits, higher priority jobs, or other reasons.

NeMo Framework provides functionality to gracefully perform a preemptive shutdown of training. This feature will listen for a user-specified signal at the end of each training step. When the signal is sent, the job will save a checkpoint and exit.

### Use Preemption Features[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/resiliency.html.md#use-preemption-features "Link to this heading")

Warning

The `PreemptionPlugin` is currently only supported on Slurm-based clusters.

To enable this feature for Slurm workloads, use the NeMo-Run plugin. Please note that [NeMo-Run](https://github.com/NVIDIA/NeMo-Run) must be installed to use this plugin.

The following example adds the plugin to the LLaMA3 8B recipe:

from nemo import lightning as nl
from nemo.collections import llm
from nemo.lightning.run.plugins import PreemptionPlugin

recipe = llm.llama3_8b.pretrain_recipe(name="llama3_with_preemption", ...) # fill in other recipe arguments

...

executor = # set up your NeMo-Run executor

...

run_plugins = [PreemptionPlugin()]
run.run(recipe, plugins=run_plugins, executor=executor)

The above plugin will configure a PyTorch Lightning callback to catch and handle a preemption signal. For non-Slurm workloads (e.g. training on a single device), you can directly configure this callback. See the following usage example:

from nemo import lightning as nl
from nemo.collections import llm

from nemo.lightning.pytorch.callbacks import PreemptionCallback

trainer = nl.Trainer()
trainer.callbacks.append(PreemptionCallback())

When the preemption signal is sent, the log should contain statements similar to the following:

Received Signals.SIGTERM death signal, shutting down workers
Sending process 404288 closing signal SIGTERM
Received signal 15, initiating graceful stop
Preemption detected, saving checkpoint and exiting

### Default Settings[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/resiliency.html.md#id3 "Link to this heading")

The default signal the `PreemptionCallback` will listen for is `SIGTERM` (set by `sig`), since this is the signal Slurm will send to all processes when the job time limit is reached. The `PreemptionPlugin` is configured to send this signal 60 seconds before the actual job time limit (set by `preempt_time`) to ensure sufficient time for saving a checkpoint. You can adjust this as needed.

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/resiliency.html.md#id3)
- [NVIDIA Resiliency Extension](https://github.com/NVIDIA/nvidia-resiliency-ext)
- [documentation](https://nvidia.github.io/nvidia-resiliency-ext/)
- [NeMo-Run](https://github.com/NVIDIA/NeMo-Run)
- [nemo/collections/llm/recipes/log/default.py](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/recipes/log/default.py)
