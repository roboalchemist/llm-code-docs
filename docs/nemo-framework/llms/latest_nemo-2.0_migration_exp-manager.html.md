# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/exp-manager.html.md

Title: Migrate exp_manager to NeMoLogger and AutoResume#

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/exp-manager.html

Published Time: Thu, 30 Oct 2025 07:07:29 GMT

Markdown Content:
In NeMo 2.0, the `exp_manager` configuration has been replaced with [NeMoLogger](https://github.com/NVIDIA/NeMo/blob/main/nemo/lightning/nemo_logger.py) and [AutoResume](https://github.com/NVIDIA/NeMo/blob/main/nemo/lightning/resume.py) objects. This guide will help you migrate your experiment management setup.

NeMo 1.0 (Previous Release)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/exp-manager.html.md#nemo-1-0-previous-release "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In NeMo 1.0, experiment management was configured in the YAML configuration file.

exp_manager:
 explicit_log_dir: null
 exp_dir: null
 name: megatron_gpt
 create_wandb_logger: False
 wandb_logger_kwargs:
 project: null
 name: null
 resume_if_exists: True
 resume_ignore_no_checkpoint: True
 resume_from_checkpoint: ${model.resume_from_checkpoint}
 create_checkpoint_callback: True
 checkpoint_callback_params:
 dirpath: null # to use S3 checkpointing, set the dirpath in format s3://bucket/key
 monitor: val_loss
 save_top_k: 10
 mode: min
 always_save_nemo: False # saves nemo file during validation, not implemented for model parallel
 save_nemo_on_train_end: False # not recommended when training large models on clusters with short time limits
 filename: 'megatron_gpt--{val_loss:.2f}-{step}-{consumed_samples}'
 model_parallel_size: ${multiply:${model.tensor_model_parallel_size}, ${model.pipeline_model_parallel_size}}
 async_save: False # Set to True to enable async checkpoint save. Currently works only with distributed checkpoints

NeMo 2.0 (New Release)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/exp-manager.html.md#nemo-2-0-new-release "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

In NeMo 2.0, experiment management is configured using the `NeMoLogger` and `AutoResume` classes.

from nemo.collections import llm
from nemo import lightning as nl
from pytorch_lightning.loggers import WandbLogger

log = nl.NeMoLogger(
    name="megatron_gpt",
    log_dir=None,  # This will default to ./nemo_experiments
    explicit_log_dir=None,
    version=None,
    use_datetime_version=True,
    log_local_rank_0_only=False,
    log_global_rank_0_only=False,
    files_to_copy=None,
    update_logger_directory=True,
    wandb=WandbLogger(project=None, name=None),
    ckpt=nl.ModelCheckpoint(
        dirpath=None,  # to use S3 checkpointing, set the dirpath in format s3://bucket/key
        monitor="val_loss",
        save_top_k=10,
        mode="min",
        always_save_nemo=False,
        save_nemo_on_train_end=False,
        filename='megatron_gpt--{val_loss:.2f}-{step}-{consumed_samples}',
    )
)

resume = nl.AutoResume(
    path=None,  # Equivalent to resume_from_checkpoint
    dirpath=None,
    import_path=None,
    resume_if_exists=True,
    resume_past_end=False,
    resume_ignore_no_checkpoint=True,
)

llm.train(..., log=log, resume=resume)

Additionally, the NeMo 1.0 experiment manager provided the option to add some callbacks to the trainer. In NeMo 2.0, those callbacks can be passed directly to your trainer. Notably, the `TimingCallback()` was used in NeMo 1.0 to log step times.

To add the `TimingCallback` in NeMo 2.0, add the callback directly to the trainer:

import nemo.lightning as nl
from nemo.utils.exp_manager import TimingCallback

trainer = nl.Trainer(
    ...
    callbacks=[TimingCallback()],
    ...
)

Migration Steps[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/exp-manager.html.md#migration-steps "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------

1.   Remove the `exp_manager` section from your YAML config file.

2.   Add the following imports to your Python script:

from nemo import lightning as nl
from pytorch_lightning.loggers import WandbLogger 
3.   Create a `NeMoLogger` object with the appropriate parameters:

log = nl.NeMoLogger(
    name="megatron_gpt",
    log_dir=None,  # This will default to ./nemo_experiments
    explicit_log_dir=None,
    version=None,
    use_datetime_version=True,
    log_local_rank_0_only=False,
    log_global_rank_0_only=False,
    files_to_copy=None,
    update_logger_directory=True,
    wandb=WandbLogger(project=None, name=None),
    ckpt=nl.ModelCheckpoint(
        dirpath=None,
        monitor="val_loss",
        save_top_k=10,
        mode="min",
        always_save_nemo=False,
        save_nemo_on_train_end=False,
        filename='megatron_gpt--{val_loss:.2f}-{step}-{consumed_samples}',
        async_save=False,
    )
) 
4.   Create an `AutoResume` object with the appropriate parameters:

resume = nl.AutoResume(
    path=None,  # Equivalent to resume_from_checkpoint
    dirpath=None,
    import_path=None,
    resume_if_exists=True,
    resume_past_end=False,
    resume_ignore_no_checkpoint=True,
) 
5.   Add any callbacks you want to the trainer:

import nemo.lightning as nl
from nemo.lightning.python.callbacks import PreemptionCallback
from nemo.utils.exp_manager import TimingCallback

callback = [TimingCallback(), PreemptionCallback()]
trainer = nl.Trainer(
    ...
    callbacks=callbacks,
    ...
) 
6.   Pass the `trainer`, `log`, and `resume` objects to the `llm.train()` function:

llm.train(..., trainer=trainer, log=log, resume=resume) 

1.   Adjust the parameters in `NeMoLogger` and `AutoResume` to match your previous YAML configuration.

Note

*   The `model_parallel_size` parameter is no longer needed in the checkpoint configuration.

*   For S3 checkpointing, set the `dirpath` in the `ModelCheckpoint` to the format `s3://bucket/key`.

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/exp-manager.html.md#migration-steps)
- [NeMoLogger](https://github.com/NVIDIA/NeMo/blob/main/nemo/lightning/nemo_logger.py)
- [AutoResume](https://github.com/NVIDIA/NeMo/blob/main/nemo/lightning/resume.py)
