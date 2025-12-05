# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/exp_manager.html.md

Title: Experiment Manager — NVIDIA NeMo Framework User Guide

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/exp_manager.html

Published Time: Fri, 05 Sep 2025 19:01:33 GMT

Markdown Content:
Experiment Manager[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/exp_manager.html.md#experiment-manager "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------

The NeMo Framework Experiment Manager leverages PyTorch Lightning for model checkpointing, TensorBoard Logging, Weights and Biases, DLLogger and MLFlow logging. The Experiment Manager is included by default in all NeMo example scripts.

To use the Experiment Manager, call [`exp_manager`](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.utils.exp_manager.exp_manager "nemo.utils.exp_manager.exp_manager") and pass in the PyTorch Lightning `Trainer`.

exp_dir = exp_manager(trainer, cfg.get("exp_manager", None))

The Experiment Manager is configurable using YAML with Hydra.

exp_manager:
 exp_dir: /path/to/my/experiments
 name: my_experiment_name
 create_tensorboard_logger: True
 create_checkpoint_callback: True

Optionally, launch TensorBoard to view the training results in `exp_dir`, which by default is set to `./nemo_experiments`.

tensorboard --bind_all --logdir nemo_experiments

If `create_checkpoint_callback` is set to `True`, then NeMo automatically creates checkpoints during training using PyTorch Lightning’s [ModelCheckpoint](https://lightning.ai/docs/pytorch/stable/api/lightning.pytorch.callbacks.ModelCheckpoint.html). We can configure the `ModelCheckpoint` via YAML or CLI:

exp_manager:
 ...
 # configure the PyTorch Lightning ModelCheckpoint using checkpoint_call_back_params
 # any ModelCheckpoint argument can be set here

 # save the best checkpoints based on this metric
 checkpoint_callback_params.monitor=val_loss

 # choose how many total checkpoints to save
 checkpoint_callback_params.save_top_k=5

Resume Training[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/exp_manager.html.md#resume-training "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

To auto-resume training, configure the `exp_manager`. This feature is important for long training runs that might be interrupted or shut down before the procedure has completed. To auto-resume training, set the following parameters via YAML or CLI:

exp_manager:
 ...
 # resume training if checkpoints already exist
 resume_if_exists: True

 # to start training with no existing checkpoints
 resume_ignore_no_checkpoint: True

 # by default experiments will be versioned by datetime
 # we can set our own version with
 exp_manager.version: my_experiment_version

Experiment Loggers[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/exp_manager.html.md#experiment-loggers "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------

Alongside Tensorboard, NeMo also supports Weights and Biases, MLFlow, DLLogger, ClearML and NeptuneLogger. To use these loggers, set the following via YAML or [`ExpManagerConfig`](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.utils.exp_manager.ExpManagerConfig "nemo.utils.exp_manager.ExpManagerConfig").

### Weights and Biases (WandB)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/exp_manager.html.md#weights-and-biases-wandb "Link to this heading")

exp_manager:
 ...
 create_checkpoint_callback: True
 create_wandb_logger: True
 wandb_logger_kwargs:
 name: ${name}
 project: ${project}
 entity: ${entity}
 <Add any other arguments supported by WandB logger here>

### MLFlow[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/exp_manager.html.md#mlflow "Link to this heading")

exp_manager:
 ...
 create_checkpoint_callback: True
 create_mlflow_logger: True
 mlflow_logger_kwargs:
 experiment_name: ${name}
 tags:
 <Any key:value pairs>
 save_dir: './mlruns'
 prefix: ''
 artifact_location: None
 # provide run_id if resuming a previously started run
 run_id: Optional[str] = None

### DLLogger[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/exp_manager.html.md#dllogger "Link to this heading")

exp_manager:
 ...
 create_checkpoint_callback: True
 create_dllogger_logger: True
 dllogger_logger_kwargs:
 verbose: False
 stdout: False
 json_file: "./dllogger.json"

### ClearML[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/exp_manager.html.md#clearml "Link to this heading")

exp_manager:
 ...
 create_checkpoint_callback: True
 create_clearml_logger: True
 clearml_logger_kwargs:
 project: None # name of the project
 task: None # optional name of task
 connect_pytorch: False
 model_name: None # optional name of model
 tags: None # Should be a list of str
 log_model: False # log model to clearml server
 log_cfg: False # log config to clearml server
 log_metrics: False # log metrics to clearml server

### Neptune[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/exp_manager.html.md#neptune "Link to this heading")

exp_manager:
 ...
 create_checkpoint_callback: True
 create_neptune_logger: false
 neptune_logger_kwargs:
 project: ${project}
 name: ${name}
 prefix: train
 log_model_checkpoints: false # set to True if checkpoints need to be pushed to Neptune
 tags: null # can specify as an array of strings in yaml array format
 description: null
 <Add any other arguments supported by Neptune logger here>

Exponential Moving Average[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/exp_manager.html.md#exponential-moving-average "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

NeMo supports using exponential moving average (EMA) for model parameters. This can be useful for improving model generalization and stability. To use EMA, set the following parameters via YAML or [`ExpManagerConfig`](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.utils.exp_manager.ExpManagerConfig "nemo.utils.exp_manager.ExpManagerConfig").

exp_manager:
 ...
 # use exponential moving average for model parameters
 ema:
 enabled: True # False by default
 decay: 0.999 # decay rate
 cpu_offload: False # If EMA parameters should be offloaded to CPU to save GPU memory
 every_n_steps: 1 # How often to update EMA weights
 validate_original_weights: False # Whether to use original weights for validation calculation or EMA weights

Hydra Multi-Run with NeMo[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/exp_manager.html.md#hydra-multi-run-with-nemo "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When training neural networks, it is common to perform a hyperparameter search to improve the model’s performance on validation data. However, manually preparing a grid of experiments and managing all checkpoints and their metrics can be tedious. To simplify these tasks, NeMo integrates with [Hydra Multi-Run support](https://hydra.cc/docs/tutorials/basic/running_your_app/multi-run/), providing a unified way to run a set of experiments directly from the configuration.

There are certain limitations to this framework, which we list below:

*   All experiments are assumed to be run on a single GPU, and multi GPU for single run (model parallel models are not supported as of now).

*   NeMo Multi-Run currently supports only grid search over a set of hyperparameters. Support for advanced hyperparameter search strategies will be added in the future.

*   **NeMo Multi-Run requires one or more GPUs** to function and will not work without GPU devices.

### Config Setup[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/exp_manager.html.md#config-setup "Link to this heading")

In order to enable NeMo Multi-Run, we first update our YAML configs with some information to let Hydra know we expect to run multiple experiments from this one config -

# Required for Hydra launch of hyperparameter search via multirun
defaults:
 - override hydra/launcher: nemo_launcher

# Hydra arguments necessary for hyperparameter optimization
hydra:
 # Helper arguments to ensure all hyper parameter runs are from the directory that launches the script.
 sweep:
 dir: "."
 subdir: "."

 # Define all the hyper parameters here
 sweeper:
 params:
 # Place all the parameters you wish to search over here (corresponding to the rest of the config)
 # NOTE: Make sure that there are no spaces between the commas that separate the config params !
 model.optim.lr: 0.001,0.0001
 model.encoder.dim: 32,64,96,128
 model.decoder.dropout: 0.0,0.1,0.2

 # Arguments to the process launcher
 launcher:
 num_gpus: -1 # Number of gpus to use. Each run works on a single GPU.
 jobs_per_gpu: 1 # If each GPU has large memory, you can run multiple jobs on the same GPU for faster results (until OOM).

Next, we will setup the config for `Experiment Manager`. When we perform hyper parameter search, each run may take some time to complete. We want to therefore avoid the case where a run ends (say due to OOM or timeout on the machine) and we need to redo all experiments. We therefore setup the experiment manager config such that every experiment has a unique “key”, whose value corresponds to a single resumable experiment.

Let us see how to setup such a unique “key” via the experiment name. Simply attach all the hyper parameter arguments to the experiment name as shown below -

exp_manager:
 exp_dir: null # Can be set by the user.

 # Add a unique name for all hyper parameter arguments to allow continued training.
 # NOTE: It is necessary to add all hyperparameter arguments to the name !
 # This ensures successful restoration of model runs in case HP search crashes.
 name: ${name}-lr-${model.optim.lr}-adim-${model.adapter.dim}-sd-${model.adapter.adapter_strategy.stochastic_depth}

 ...
 checkpoint_callback_params:
 ...
 save_top_k: 1 # Dont save too many .ckpt files during HP search
 always_save_nemo: True # saves the checkpoints as nemo files for fast checking of results later
 ...

 # We highly recommend use of any experiment tracking took to gather all the experiments in one location
 create_wandb_logger: True
 wandb_logger_kwargs:
 project: "<Add some project name here>"

 # HP Search may crash due to various reasons, best to attempt continuation in order to
 # resume from where the last failure case occurred.
 resume_if_exists: true
 resume_ignore_no_checkpoint: true

### Run a NeMo Multi-Run Configuration[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/exp_manager.html.md#run-a-nemo-multi-run-configuration "Link to this heading")

Once the config has been updated, we can now run it just like any normal Hydra script, with one special flag (`-m`).

python script.py --config-path=ABC --config-name=XYZ -m \
 trainer.max_steps=5000 \  # Any additional arg after -m will be passed to all the runs generated from the config !
 ...

Tips and Tricks[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/exp_manager.html.md#tips-and-tricks "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

This section provides recommendations for using the Experiment Manager.

### Preserving disk space for a large number of experiments[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/exp_manager.html.md#preserving-disk-space-for-a-large-number-of-experiments "Link to this heading")

Some models may have a large number of parameters, making it very expensive to save numerous checkpoints on physical storage drives. For example, if you use the Adam optimizer, each PyTorch Lightning “.ckpt” file will be three times the size of just the model parameters. This can become exorbitant if you have multiple runs.

In the above configuration, we explicitly set `save_top_k: 1` and `always_save_nemo: True`. This limits the number of “.ckpt” files to just one and also saves a NeMo file, which contains only the model parameters without the optimizer state. This NeMo file can be restored immediately for further work.

We can further save storage space by using NeMo’s utility functions to automatically delete either “.ckpt” or NeMo files after a training run has finished. This is sufficient if you are collecting results in an experiment tracking tool and can simply rerun the best configuration after the search is completed.

# Import `clean_exp_ckpt` along with exp_manager
from nemo.utils.exp_manager import clean_exp_ckpt, exp_manager

@hydra_runner(...)
def main(cfg):
    ...

    # Keep track of the experiment directory
    exp_log_dir = exp_manager(trainer, cfg.get("exp_manager", None))

    ... add any training code here as needed ...

    # Add following line to end of the training script
    # Remove PTL ckpt file, and potentially also remove .nemo file to conserve storage space.
    clean_exp_ckpt(exp_log_dir, remove_ckpt=True, remove_nemo=False)

### Debugging Multi-Run Scripts[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/exp_manager.html.md#debugging-multi-run-scripts "Link to this heading")

When running Hydra scripts, you may encounter configuration issues that crash the program. In NeMo Multi-Run, a crash in any single run will not crash the entire program. Instead, we will note the error and proceed to the next job. Once all jobs are completed, we will raise the errors in the order they occurred, crashing the program with the first error’s stack trace.

To debug NeMo Multi-Run, we recommend commenting out the entire hyperparameter configuration set inside `sweep.params`. Instead, run a single experiment with the configuration, which will immediately raise the error.

### Experiment name cannot be parsed by Hydra[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/exp_manager.html.md#experiment-name-cannot-be-parsed-by-hydra "Link to this heading")

Sometimes our hyperparameters include PyTorch Lightning `trainer` arguments, such as the number of steps, number of epochs, and whether to use gradient accumulation. When we attempt to add these as keys to the experiment manager’s `name`, Hydra may complain that `trainer.xyz` cannot be resolved.

A simple solution is to finalize the Hydra config before you call `exp_manager()` as follows:

@hydra_runner(...)
def main(cfg):
    # Make any changes as necessary to the config
    cfg.xyz.abc = uvw

    # Finalize the config
    cfg = OmegaConf.resolve(cfg)

    # Carry on as normal by calling trainer and exp_manager
    trainer = pl.Trainer(**cfg.trainer)
    exp_log_dir = exp_manager(trainer, cfg.get("exp_manager", None))
    ...

ExpManagerConfig[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/exp_manager.html.md#expmanagerconfig "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ nemo.utils.exp_manager.ExpManagerConfig(_explicit\_log\_dir:str|None=None_,_exp\_dir:str|None=None_,_name:str|None=None_,_version:str|None=None_,_use\_datetime\_version:bool|None=True_,_resume\_if\_exists:bool|None=False_,_resume\_past\_end:bool|None=False_,_resume\_ignore\_no\_checkpoint:bool|None=False_,_resume\_from\_checkpoint:str|None=None_,_create\_tensorboard\_logger:bool|None=True_,_summary\_writer\_kwargs:~typing.Dict[~typing.Any_,_~typing.Any]|None=None_,_create\_wandb\_logger:bool|None=False_,_wandb\_logger\_kwargs:~typing.Dict[~typing.Any_,_~typing.Any]|None=None_,_create\_mlflow\_logger:bool|None=False_,_mlflow\_logger\_kwargs:~nemo.utils.loggers.mlflow\_logger.MLFlowParams|None=<factory>_,_create\_dllogger\_logger:bool|None=False_,_dllogger\_logger\_kwargs:~nemo.utils.loggers.dllogger.DLLoggerParams|None=<factory>_,_create\_clearml\_logger:bool|None=False_,_clearml\_logger\_kwargs:~nemo.utils.loggers.clearml\_logger.ClearMLParams|None=<factory>_,_create\_neptune\_logger:bool|None=False_,_neptune\_logger\_kwargs:~typing.Dict[~typing.Any_,_~typing.Any]|None=None_,_create\_checkpoint\_callback:bool|None=True_,_checkpoint\_callback\_params:~nemo.utils.exp\_manager.CallbackParams|None=<factory>_,_create\_early\_stopping\_callback:bool|None=False_,_early\_stopping\_callback\_params:~nemo.utils.exp\_manager.EarlyStoppingParams|None=<factory>_,_create\_preemption\_callback:bool|None=True_,_files\_to\_copy:~typing.List[str]|None=None_,_log\_step\_timing:bool|None=True_,_log\_delta\_step\_timing:bool|None=False_,_step\_timing\_kwargs:~nemo.utils.exp\_manager.StepTimingParams|None=<factory>_,_log\_local\_rank\_0\_only:bool|None=False_,_log\_global\_rank\_0\_only:bool|None=False_,_disable\_validation\_on\_resume:bool|None=True_,_ema:~nemo.utils.exp\_manager.EMAParams|None=<factory>_,_max\_time\_per\_run:str|None=None_,_seconds\_to\_sleep:float=5_,_create\_straggler\_detection\_callback:bool|None=False_,_straggler\_detection\_params:~nemo.utils.exp\_manager.StragglerDetectionParams|None=<factory>_,_create\_fault\_tolerance\_callback:bool|None=False_,_fault\_tolerance:~nemo.utils.exp\_manager.FaultToleranceParams|None=<factory>_,_log\_tflops\_per\_sec\_per\_gpu:bool|None=True_,)
Bases: `object`

Experiment Manager config for validation of passed arguments.

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/exp_manager.html.md#expmanagerconfig)
- [exp_manager](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.utils.exp_manager.exp_manager)
- [ModelCheckpoint](https://lightning.ai/docs/pytorch/stable/api/lightning.pytorch.callbacks.ModelCheckpoint.html)
- [ExpManagerConfig](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.utils.exp_manager.ExpManagerConfig)
- [Hydra Multi-Run support](https://hydra.cc/docs/tutorials/basic/running_your_app/multi-run/)
