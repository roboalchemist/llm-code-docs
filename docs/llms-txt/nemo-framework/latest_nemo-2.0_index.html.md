# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/index.html.md

Title: NeMo 2.0 — NVIDIA NeMo Framework User Guide

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/index.html

Published Time: Thu, 30 Oct 2025 07:07:29 GMT

Markdown Content:
NeMo 2.0[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/index.html.md#nemo-2-0 "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------

In NeMo 1.0, the main interface for configuring experiments is through YAML files. This approach allows for a declarative way to set up experiments, but it has limitations in terms of flexibility and programmatic control. NeMo 2.0 shifts to a Python-based configuration, which offers several advantages:

*   More flexibility and control over the configuration.

*   Better integration with IDEs for code completion and type checking.

*   Easier to extend and customize configurations programmatically.

By adopting PyTorch Lightning’s modular abstractions, NeMo 2.0 makes it easy for users to adapt the framework to their specific use cases and experiment with various configurations. This section offers an overview of the new features in NeMo 2.0 and includes a migration guide with step-by-step instructions for transitioning your models from NeMo 1.0 to NeMo 2.0.

Install NeMo 2.0[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/index.html.md#install-nemo-2-0 "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------

NeMo 2.0 installation instructions can be found in the [Getting Started guide](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/quickstart.html.md#nemo-2-quickstart-nemo-run).

Quickstart[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/index.html.md#quickstart "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------

Important

In any script you write, please make sure you wrap your code in an `if __name__ == "__main__":` block. See [Working with scripts in NeMo 2.0](https://docs.nvidia.com/nemo-framework/user-guide/latest/best-practices.html.md#main-block-best-practice) for details.

The following is an example of running a simple training loop using NeMo 2.0. This example uses the [train API](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/api.py) from the NeMo Framework LLM collection. Once you have set up your environment using the instructions above, you’re ready to run this simple train script.

import torch
from nemo import lightning as nl
from nemo.collections import llm
from megatron.core.optimizer import OptimizerConfig

if  __name__  == "__main__":
    seq_length = 2048
    global_batch_size = 16

    ## setup the dummy dataset
    data = llm.MockDataModule(seq_length=seq_length, global_batch_size=global_batch_size)

    ## initialize a small GPT model
    gpt_config = llm.GPTConfig(
        num_layers=6,
        hidden_size=384,
        ffn_hidden_size=1536,
        num_attention_heads=6,
        seq_length=seq_length,
        init_method_std=0.023,
        hidden_dropout=0.1,
        attention_dropout=0.1,
        layernorm_epsilon=1e-5,
        make_vocab_size_divisible_by=128,
    )
    model = llm.GPTModel(gpt_config, tokenizer=data.tokenizer)

    ## initialize the strategy
    strategy = nl.MegatronStrategy(
        tensor_model_parallel_size=1,
        pipeline_model_parallel_size=1,
        pipeline_dtype=torch.bfloat16,
    )

    ## setup the optimizer
    opt_config = OptimizerConfig(
        optimizer='adam',
        lr=6e-4,
        bf16=True,
    )
    opt = nl.MegatronOptimizerModule(config=opt_config)

    trainer = nl.Trainer(
        devices=1, ## you can change the number of devices to suit your setup
        max_steps=50,
        accelerator="gpu",
        strategy=strategy,
        plugins=nl.MegatronMixedPrecision(precision="bf16-mixed"),
    )

    nemo_logger = nl.NeMoLogger(
        log_dir="test_logdir", ## logs and checkpoints will be written here
    )

    llm.train(
        model=model,
        data=data,
        trainer=trainer,
        log=nemo_logger,
        tokenizer='data',
        optim=opt,
    )

CLI Quickstart[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/index.html.md#cli-quickstart "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------

NeMo comes equipped with a CLI that allows you to launch experiments locally or on a remote cluster. Every command has a help flag that you can use to get more information about the command.

To list all the commands inside the llm-collection, you can use the following command:

$ nemo llm --help
Usage: nemo llm [OPTIONS] COMMAND [ARGS]...

[Module] llm

╭─ Options ────────────────────────────────────────────────────────────────╮
│ --help Show this message and exit. │
╰──────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────╮
│ train [Entrypoint] train │
│ pretrain [Entrypoint] pretrain │
│ finetune [Entrypoint] finetune │
│ validate [Entrypoint] validate │
│ prune [Entrypoint] prune │
│ distill [Entrypoint] distill │
│ ptq [Entrypoint] ptq │
│ deploy [Entrypoint] deploy │
│ import [Entrypoint] import │
│ export [Entrypoint] export │
│ generate [Entrypoint] generate │
╰──────────────────────────────────────────────────────────────────────────╯

Most commands come with various pre-configured recipes. To list all the recipes for a given command, you can use the following command:

$ nemo llm finetune --help
Usage: nemo llm finetune [OPTIONS] [ARGUMENTS]

[Entrypoint] finetune
Finetunes a model using the specified data and trainer, with optional logging, resuming, and PEFT.

╭─ Pre-loaded entrypoint factories, run with --factory ──────────────────────────────────╮
│ baichuan2_7b nemo.collections.llm.recipes.baichuan2_7b.fi… line 236 │
│ chatglm3_6b nemo.collections.llm.recipes.chatglm3_6b.fin… line 236 │
│ deepseek_v2 nemo.collections.llm.recipes.deepseek_v2.fin… line 108 │
│ deepseek_v2_lite nemo.collections.llm.recipes.deepseek_v2_lit… line 107 │
│ gemma2_2b nemo.collections.llm.recipes.gemma2_2b.finet… line 173 │
│ gemma2_9b nemo.collections.llm.recipes.gemma2_9b.finet… line 173 │
│ llama2_7b nemo.collections.llm.recipes.llama2_7b.finet… line 230 │
│ llama3_8b nemo.collections.llm.recipes.llama3_8b.finet… line 245 │
│ mixtral_8x7b nemo.collections.llm.recipes.mixtral_8x7b.fi… line 240 │
│ nemotron3_8b nemo.collections.llm.recipes.nemotron3_8b.fi… line 253 │
│ nemotron4_15b nemo.collections.llm.recipes.nemotron4_15b.f… line 227 │
│ ... (output truncated) │
╰────────────────────────────────────────────────────────────────────────────────────────╯

You can also use the `--factory` flag to run a specific recipe. For example, to run the `llama32_1b` recipe, you can use the following command:

$ nemo llm finetune --factory llama32_1b

NeMo CLI supports overriding any configuration parameter using Hydra-style dot notation. This powerful feature allows you to customize any aspect of the recipe without modifying the source code. For example, to change the number of GPUs used for training from the default to just 1 device:

$ nemo llm finetune --factory llama32_1b trainer.devices=1

Configuring global options
Dry run for task nemo.collections.llm.api:finetune
Resolved Arguments
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Argument Name ┃ Resolved Value ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ trainer │ Trainer( │
│ │ ... │
│ │ devices='1', │
│ │ ... │
└──────────────────────┴──────────────────────────────────────────────────────────────┘
Continue? [y/N]:

This syntax follows the pattern `component.parameter=value`, allowing you to navigate nested configurations. You can override multiple parameters at once by adding more space-separated overrides:

$ nemo llm finetune --factory llama32_1b trainer.devices=1 trainer.max_steps=500 optim.config.lr=5e-5

The command prints a preview of the resolved configuration values so you can verify your changes before starting the training run.

NeMo 2.0 also seamlessly supports scaling to thousands of GPUs using [NeMo-Run](https://github.com/NVIDIA/NeMo-Run). For examples of launching large-scale experiments using NeMo-Run, refer to [Quickstart with NeMo-Run](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/quickstart.html.md#nemo-2-quickstart-nemo-run).

Note

If you are an existing user of NeMo 1.0 and would like to use a NeMo 1.0 dataset in place of the `MockDataModule` in the example, refer to the [data migration guide](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/data.html.md#migration-data) for instructions.

Extend Quickstart with NeMo-Run[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/index.html.md#extend-quickstart-with-nemo-run "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

While [Quickstart with NeMo-Run](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/quickstart.html.md#nemo-2-quickstart-nemo-run) covers how to configure your NeMo 2.0 experiment using NeMo-Run, it is not mandatory to use the configuration system from NeMo-Run. In fact, you can take the Python script from the [Quickstart](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/index.html.md#nemo-2-quickstart-python) above and launch it on remote clusters directly using NeMo-Run. For more details about NeMo-Run, refer to [NeMo-Run Github](https://github.com/NVIDIA/NeMo-Run) and the [hello_scripts example](https://github.com/NVIDIA/NeMo-Run/blob/main/examples/hello-world/hello_scripts.py). Below, we will walk through how to do this.

### Prerequisites[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/index.html.md#prerequisites "Link to this heading")

1.   Save the script above as `train.py` in your working directory.

2.   Install NeMo-Run using the following command:

pip install git+https://github.com/NVIDIA/NeMo-Run.git

Let’s assume that you have the above script saved as `train.py` in your current working directory.

### Launch the Experiment Locally[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/index.html.md#launch-the-experiment-locally "Link to this heading")

Locally here means from your local workstation. It can be a `venv` in your workstation or an interactive NeMo Docker container.

1.   Write a new file called `run.py` with the following contents:

import os
import nemo_run as run

if  __name__  == "__main__":
    training_job = run.Script(
        inline="""
# This string will get saved to a sh file and executed with bash
# Run any preprocessing commands

# Run the training command
python train.py

# Run any post processing commands
"""
    )

    # Run it locally
    executor = run.LocalExecutor()

    with run.Experiment("nemo_2.0_training_experiment", log_level="INFO") as exp:
        exp.add(training_job, executor=executor, tail_logs=True, name="training")
        # Add more jobs as needed

        # Run the experiment
        exp.run(detach=False)

1.   Launch the experiment using the following command:

python run.py

### Launch the Experiment on Slurm[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/index.html.md#launch-the-experiment-on-slurm "Link to this heading")

Writing an extra script to just launch locally is not very useful. So let’s see how we can extend `run.py` to launch the job on any supported [NeMo-Run executors](https://github.com/NVIDIA/NeMo-Run/blob/main/docs/source/guides/execution.md). For this tutorial, we will use the slurm executor.

Note

Each cluster might have different settings. It is recommended that you reach out to the cluster administrators for specific details.

1.   Define a function to configure your slurm executor as follows:

def slurm_executor(
    user: str,
    host: str,
    remote_job_dir: str,
    account: str,
    partition: str,
    nodes: int,
    devices: int,
    time: str = "01:00:00",
    custom_mounts: Optional[list[str]] = None,
    custom_env_vars: Optional[dict[str, str]] = None,
    container_image: str = "nvcr.io/nvidia/nemo:dev",
    retries: int = 0,
) -> run.SlurmExecutor:
    if not (user and host and remote_job_dir and account and partition and nodes and devices):
        raise RuntimeError(
            "Please set user, host, remote_job_dir, account, partition, nodes, and devices args for using this function."
        )

    mounts = []
    # Custom mounts are defined here.
    if custom_mounts:
        mounts.extend(custom_mounts)

    # Env vars for jobs are configured here
    env_vars = {
        "TORCH_NCCL_AVOID_RECORD_STREAMS": "1",
        "NCCL_NVLS_ENABLE": "0",
        "NVTE_DP_AMAX_REDUCE_INTERVAL": "0",
        "NVTE_ASYNC_AMAX_REDUCTION": "1",
    }
    if custom_env_vars:
        env_vars |= custom_env_vars

    # This will package the train.py script in the current working directory to the remote cluster.
    # If you are inside a git repo, you can also use https://github.com/NVIDIA/NeMo-Run/blob/main/src/nemo_run/core/packaging/git.py.
    # If the script already exists on your container and you call it with the absolute path, you can also just use `run.Packager()`.
    packager = run.PatternPackager(include_pattern="train.py", relative_path=os.getcwd())

    # This defines the slurm executor.
    # We connect to the executor via the tunnel defined by user, host and remote_job_dir.
    executor = run.SlurmExecutor(
        account=account,
        partition=partition,
        tunnel=run.SSHTunnel(
            user=user,
            host=host,
            job_dir=remote_job_dir, # This is where the results of the run will be stored by default.
            # identity="/path/to/identity/file" OPTIONAL: Provide path to the private key that can be used to establish the SSH connection without entering your password.
        ),
        nodes=nodes,
        ntasks_per_node=devices,
        gpus_per_node=devices,
        mem="0",
        exclusive=True,
        gres="gpu:8",
        packager=packager,
    )

    executor.container_image = container_image
    executor.container_mounts = mounts
    executor.env_vars = env_vars
    executor.retries = retries
    executor.time = time

    return executor

1.   Replace the executor in `run.py` as follows:

executor = slurm_executor(...) # pass in args relevant to your cluster

1.   Run the file with the same command and it will launch your job on the cluster. Similarly, you can define multiple slurm executors for multiple Slurm clusters and use them interchangeably, or use any of the supported executors in NeMo-Run.

Where to Find NeMo 2.0[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/index.html.md#where-to-find-nemo-2-0 "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

Currently, the code for NeMo 2.0 can be found in two main locations within the [NeMo GitHub](https://github.com/NVIDIA/NeMo/tree/main) repository:

1.   [LLM collection](https://github.com/NVIDIA/NeMo/tree/main/nemo/collections/llm): This is the first collection to adopt the NeMo 2.0 APIs. This collection provides implementations of common language models using NeMo 2.0. Currently, the collection supports the following models:

> *   GPT
> 
>     *   [LLama](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/llama3.html.md#llama)
> 
>     *   [Mixtral](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/mixtral.html.md#mixtral)
> 
>     *   [Nemotron](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/nemotron.html.md#nemotron)
> 
>     *   [Mamba2 and Hybrid Models](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/mamba.html.md#mamba)
> 
>     *   [T5](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/t5.html.md#t5)

2.   [NeMo 2.0 LLM Recipes](https://github.com/NVIDIA/NeMo/tree/main/nemo/collections/llm/recipes): Provides comprehensive recipes for pretraining and fine-tuning large language models. Recipes can be easily configured and modified for specific use-cases with the help of [NeMo-Run](https://github.com/NVIDIA/NeMo-Run).

3.   [NeMo Lightning](https://github.com/NVIDIA/NeMo/tree/main/nemo/lightning): Provides custom PyTorch Lightning-compatible objects that make it possible to train Megatron Core-based models using PTL in a modular fashion. NeMo 2.0 employs these objects to train models in a simple and efficient manner.

Pretraining, Supervised Fine-Tuning (SFT), and Parameter-Efficient Fine-Tuning (PEFT) are all supported by the LLM collection. More information about each model can be found in the model-specific documentation linked above.

Long context recipes are also supported with the help of context parallelism. For more information on the available long conext recipes, refer to the [long context documentation](https://docs.nvidia.com/nemo-framework/user-guide/latest/longcontext/index.html.md#long-context-recipes).

Inference via TensorRT-LLM supported in NeMo 2.0. For more information, refer to the TRT-LLM deployment documentation.

Additional Resources[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/index.html.md#additional-resources "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------

*   The [Feature Guide](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/index.html.md#nemo-2-design) provides an in-depth exploration of the main features of NeMo 2.0. Refer to this guide for information on:

> *   [The interaction between NeMo Lightning and Megatron](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/megatron.html.md#design-megatron)
> 
>     *   [Logging and checkpointing](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/logging.html.md#design-logging)
> 
>     *   [Parameter-efficient fine-tuning](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/peft.html.md#design-peft)
> 
>     *   [Serialization](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/serialization.html.md#design-serialization)
> 
>     *   [Hugging Face integration](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/hf-integration.html.md#design-hf)

*   For users familiar with NeMo 1.0, the [Migration Guide](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/index.html.md#nemo-2-migration) explains how to migrate your experiments from NeMo 1.0 to NeMo 2.0. To convert your existing NeMo 1.0 checkpoint to NeMo 2.0, follow the guide [here](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/checkpointing.html.md#migration-checkpointing).

*   [NeMo 2.0 Recipes](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/recipes) contains additional examples of launching large-scale runs using NeMo 2.0 and NeMo-Run.

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/index.html.md#additional-resources)
- [Getting Started guide](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/quickstart.html.md#nemo-2-quickstart-nemo-run)
- [Working with scripts in NeMo 2.0](https://docs.nvidia.com/nemo-framework/user-guide/latest/best-practices.html.md#main-block-best-practice)
- [train API](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/api.py)
- [NeMo-Run](https://github.com/NVIDIA/NeMo-Run)
- [data migration guide](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/data.html.md#migration-data)
- [Quickstart](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/index.html.md#nemo-2-quickstart-python)
- [hello_scripts example](https://github.com/NVIDIA/NeMo-Run/blob/main/examples/hello-world/hello_scripts.py)
- [NeMo-Run executors](https://github.com/NVIDIA/NeMo-Run/blob/main/docs/source/guides/execution.md)
- [NeMo GitHub](https://github.com/NVIDIA/NeMo/tree/main)
- [LLM collection](https://github.com/NVIDIA/NeMo/tree/main/nemo/collections/llm)
- [LLama](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/llama3.html.md#llama)
- [Mixtral](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/mixtral.html.md#mixtral)
- [Nemotron](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/nemotron.html.md#nemotron)
- [Mamba2 and Hybrid Models](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/mamba.html.md#mamba)
- [T5](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/t5.html.md#t5)
- [NeMo 2.0 LLM Recipes](https://github.com/NVIDIA/NeMo/tree/main/nemo/collections/llm/recipes)
- [NeMo Lightning](https://github.com/NVIDIA/NeMo/tree/main/nemo/lightning)
- [long context documentation](https://docs.nvidia.com/nemo-framework/user-guide/latest/longcontext/index.html.md#long-context-recipes)
- [Feature Guide](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/index.html.md#nemo-2-design)
- [The interaction between NeMo Lightning and Megatron](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/megatron.html.md#design-megatron)
- [Logging and checkpointing](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/logging.html.md#design-logging)
- [Parameter-efficient fine-tuning](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/peft.html.md#design-peft)
- [Serialization](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/serialization.html.md#design-serialization)
- [Hugging Face integration](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/hf-integration.html.md#design-hf)
- [Migration Guide](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/index.html.md#nemo-2-migration)
- [here](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/checkpointing.html.md#migration-checkpointing)
- [NeMo 2.0 Recipes](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/recipes)
