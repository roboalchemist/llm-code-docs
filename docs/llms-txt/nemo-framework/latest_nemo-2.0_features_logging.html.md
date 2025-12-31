# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/logging.html.md

Title: Logging and Checkpointing — NVIDIA NeMo Framework User Guide

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/logging.html

Published Time: Thu, 30 Oct 2025 07:07:29 GMT

Markdown Content:
Logging and Checkpointing[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/logging.html.md#logging-and-checkpointing "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Three main classes in NeMo 2.0 are responsible for configuring logging and checkpointing directories:

1.   `nemo.lightning.pytorch.callbacks.model_checkpoint.ModelCheckpoint`

> *   Handles the logic that determines when to save a checkpoint.
> 
>     *   Provides the ability to perform asynchronous checkpointing.

2.   `nemo.lightning.nemo_logger.NeMoLogger`

> *   Responsible for setting logging directories.
> 
>     *   Optionally configures the trainer’s loggers.

3.   `nemo.lightning.resume.AutoResume`

> *   Sets the checkpointing directory.
> 
>     *   Determines whether there is an existing checkpoint from which to resume.

ModelCheckpoint[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/logging.html.md#modelcheckpoint "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------

The `ModelCheckpoint` callback in NeMo 2.0 is a wrapper around Pytorch Lightning’s `ModelCheckpoint`. It manages when to save and clean up checkpoints during training. Additionally, it supports saving a checkpoint at the end of training and provides the necessary support for asynchronous checkpointing.

The following is an example of how to instantiate a `ModelCheckpoint` callback:

from nemo.lightning.pytorch.callbacks import ModelCheckpoint

checkpoint_callback = ModelCheckpoint(
    save_last=True,
    monitor="val_loss",
    save_top_k=2,
    every_n_train_steps=30,
    dirpath='my_model_directory',
    always_save_context=True,
)

Refer to the documentation for [NeMo Lightning](https://github.com/NVIDIA/NeMo/blob/main/nemo/lightning/pytorch/callbacks/model_checkpoint.py) and [PyTorch Lightning’s](https://github.com/Lightning-AI/pytorch-lightning/blob/master/src/lightning/pytorch/callbacks/model_checkpoint.py)`ModelCheckpoint` classes to find the complete list of supported arguments. Here, `dirpath` refers to the directory to save the checkpoints. Note that `dirpath` is optional. If not provided, it will default to `log_dir / checkpoints`, where `log_dir` is the path determined by the `NeMoLogger`, as described in detail in the subsequent section.

In addition, note that asynchronous checkpointing is set using the `ckpt_async_save` argument in [MegatronStrategy](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/megatron.html.md#design-megatron). This attribute is then accessed by the checkpoint callback to perform async checkpointing as requested.

Two options are available to pass the `ModelCheckpoint` callback instance to the trainer.

1.   Add the callback to the set of callbacks and then pass the callbacks directly to the trainer:

import nemo.lightning as nl

callbacks = [checkpoint_callback]
### add any other desired callbacks...

trainer = nl.Trainer(
    ...
    callbacks = callbacks,
    ...
) 
2.   Pass the callback to the `NeMoLogger`, as described in the `NeMoLogger` section below.

### Checkpoint Directory Structure[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/logging.html.md#checkpoint-directory-structure "Link to this heading")

By default, `ModelCheckpoint` in NeMo saves checkpoints with the following structure:

log_dir
└-checkpoints/
  └-model_name=...step=...consumed_samples=.../
    ├-context/
    | ├-io.json
    | ├-model.yaml
    | ├- ...
    ├-weights/
    | ├-common.pt
    | ├-metadata.json
    | ├-__0_0.distcp
    | ├-__1_0.distcp
    | ├-...

The `context` directory contains the artifacts needed to reinitialize the experiment’s model, trainer, and dataloader. It is present only if one of the following conditions is met:

1.   `always_save_context` is set to `True` when instantiating `ModelCheckpoint`, or

2.   `save_context_on_train_end` is set to `True` and the checkpoint is the final checkpoint of the training run.

The configuration of the model checkpoint is saved in `io.json` and displayed as a human-readable file in `model.yaml`. `io.json` is the source of truth for model configuration; modifying `model.yaml` has no effect when loading the model.

The `weights` directory consists primarily of `.distcp` files which store the distributed checkpoint. By default, there are two `.distcp` files per rank.

NeMoLogger[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/logging.html.md#nemologger "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------

The `NeMoLogger` class provides a standardized way to set up logging for NeMo experiments. It creates a new log directory (or reuses an existing one), manages experiment names and versions (optionally using timestamps), and can configure multiple loggers (e.g., TensorBoard and WandB). It also handles copying important files (like configurations) and manages checkpoint settings, ensuring all experiment artifacts are consistently organized.

Please refer to the [NeMoLogger documentation](https://github.com/NVIDIA/NeMo/blob/main/nemo/lightning/nemo_logger.py) for details on all supported arguments.

Here is an example of creating a new `NeMoLogger` instance:

from nemo.lightning import NeMoLogger

nemo_logger = NeMoLogger(
    log_dir='my_logging_dir',
    name='experiment1',
    use_datetime_version=False,
)

By default, the directory where logs are written is `log_dir / name / version`. If an explicit version is not provided and `use_datetime_version` is False, the directory will change to `log_dir / name`.

As mentioned earlier, you can optionally pass your `ModelCheckpoint` instance in here, and the logger will automatically configure the checkpoint callback in your trainer:

nemo_logger = NeMoLogger(
    ...
    ckpt=checkpoint_callback,
    ...
)

Once your trainer has been initialized, the `NeMoLogger` can be set up using the following command:

nemo_logger.setup(
    trainer,
    resume_if_exists,
)

The `resume_if_exists` boolean indicates whether to resume from the latest checkpoint, if one is available. The value of `resume_if_exists` should match the value passed into `AutoResume`, as described below.

Experiment Logging[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/logging.html.md#experiment-logging "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

NeMo 2.0 provides built-in support for logging experiments using popular tracking tools like TensorBoard and Weights & Biases (wandb).

### TensorBoard Logging[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/logging.html.md#tensorboard-logging "Link to this heading")

To use TensorBoard logging with NeMo 2.0:

1.   First, ensure you have TensorBoard installed:

pip install tensorboard 
2.   Configure the TensorBoardLogger and add it to your NeMoLogger:

from lightning.pytorch.loggers import TensorBoardLogger

# Create TensorBoard logger
tensorboard = TensorBoardLogger(
    save_dir="tb_logs",    # Directory to store TensorBoard logs
    name="my_model",       # Name of the experiment
    version=None,          # Optional version number
)

# Add TensorBoard logger to NeMoLogger
nemo_logger = NeMoLogger(
    tensorboard=tensorboard,  # Pass TensorBoard logger here
    ...
) 

In this example, The TensorBoard logs will be saved in the directory `tb_logs` as a subdirectory of the `my_model` experiment dir.

The `update_logger_directory` argument in `NeMoLogger` controls whether to update the directory of the TensorBoard logger to match the NeMo log dir. If set to `True`, the TensorBoard logger will also write to the same log directory.

### Weights & Biases (wandb) Logging[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/logging.html.md#weights-biases-wandb-logging "Link to this heading")

To use Weights & Biases (wandb) logging with NeMo 2.0:

1.   First, ensure you have wandb installed:

pip install wandb 
2.   Configure the WandbLogger and add it to your NeMoLogger:

from lightning.pytorch.loggers import WandbLogger

# Create Wandb logger
wandb_logger = WandbLogger(
    project="my_project",  # Name of the W&B project
    name="my_experiment",  # Name of this specific run
    entity="my_team",      # Optional: username or team name
    config={},             # Optional: dictionary of hyperparameters
)

# Add Wandb logger to NeMoLogger
nemo_logger = NeMoLogger(
    wandb=wandb_logger,    # Pass Wandb logger here
    ...
) 

The Weights & Biases logs will be automatically synced to your wandb account under the specified `project` and `name`. You can view your experiment metrics, system stats, and model artifacts through the wandb web interface.

Just as with the TensorBoard logger, the `update_logger_directory` argument in `NeMoLogger` controls whether to update the directory of the wandb logger to match the NeMo log dir. If set to `True`, the wandb logger will also write to the same log directory.

AutoResume[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/logging.html.md#autoresume "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------

The `AutoResume` class manages checkpoint paths and checks for existing checkpoints to restore from. Here’s an example of how it can be used:

from nemo.lightning import AutoResume

resume = AutoResume(
    resume_if_exists=True,
    resume_ignore_no_checkpoint=True,
    resume_from_directory="checkpoint_dir_to_resume_from"
)

In the script, `resume_from_directory` refers to the path of the checkpoint directory to resume from. If no `resume_from_directory` is provided, the directory to resume from will default to `log_dir / checkpoints`, where `log_dir` is determined by the `NemoLogger` instance as described in the previous section.

The `resume_ignore_no_checkpoint` boolean determines whether to proceed without error if `resume_if_exists` is set to `True` and no checkpoint is found in the checkpointing directory.

Ensure that the value of `resume_if_exists` matches the argument passed into the `NemoLogger` instance.

`AutoResume` should be set up in a similar fashion to `NeMoLogger`.

resume.setup(trainer, model)

Passing a model into the setup is optional. It is only required when importing a checkpoint from Hugging Face or other non-NeMo checkpoint formats.

Putting it All Together[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/logging.html.md#putting-it-all-together "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------

To put it all together, configuring loggers and checkpointers in NeMo 2.0 looks like this:

from lightning.pytorch.loggers import TensorBoardLogger
from lightning.pytorch.loggers import WandbLogger

checkpoint_callback = ModelCheckpoint(
    save_last=True,
    monitor="reduced_train_loss",
    save_top_k=2,
    every_n_train_steps=30,
    dirpath='my_model_directory',
)

tensorboard = TensorBoardLogger(
    save_dir="tb_logs",
    name="experiment1",
)
wandb_logger = WandbLogger(
    project="my_project",
    name="my_experiment",
    entity="my_team",
)
logger = nemo_logger = NeMoLogger(
    log_dir='my_logging_dir',
    name='experiment1',
    use_datetime_version=False,
    ckpt=checkpoint_callback,
    tensorboard=tensorboard,
    wandb=wandb_logger,
    update_logger_directory=True,
)

resume = AutoResume(
    resume_if_exists=True,
    resume_ignore_no_checkpoint=True,
)

### setup your trainer here ###

nemo_logger.setup(
    trainer,
    getattr(resume, "resume_if_exists", False),
)
resume.setup(trainer)

Note that using both `TensorBoardLogger` and `WandbLogger` at the same time is possible, as shown here, but uncommon. This example is mainly for demonstration purposes, so please adapt it to your needs.

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/logging.html.md#putting-it-all-together)
- [NeMo Lightning](https://github.com/NVIDIA/NeMo/blob/main/nemo/lightning/pytorch/callbacks/model_checkpoint.py)
- [PyTorch Lightning’s](https://github.com/Lightning-AI/pytorch-lightning/blob/master/src/lightning/pytorch/callbacks/model_checkpoint.py)
- [MegatronStrategy](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/megatron.html.md#design-megatron)
- [NeMoLogger documentation](https://github.com/NVIDIA/NeMo/blob/main/nemo/lightning/nemo_logger.py)
