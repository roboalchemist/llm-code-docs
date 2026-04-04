# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/mixtral.html.md

Title: Mixtral — NVIDIA NeMo Framework User Guide

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/mixtral.html

Published Time: Thu, 30 Oct 2025 07:07:28 GMT

Markdown Content:
Mixtral[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/mixtral.html.md#mixtral "Link to this heading")
---------------------------------------------------------------------------------------------------------------------

Released in December 2023, Mistral AI’s second marquee model, Mixtral-8x7B, is one of the first performant and open-source (Apache 2.0) Sparse Mixture of Experts Model (SMoE). The key distinguishing feature of Mixtral’s SMoE implementation, compared to Mistral 7B, is the inclusion of a router network that guides tokens through a set of two groups of parameters (experts) of a possible eight. This allows the model to perform better and be significantly larger without a corresponding significant increase in cost and latency. More specific details are available in the companion paper “[Mixtral of Experts](https://arxiv.org/abs/2401.04088)”.

Released in April 2024, Mistral AI’s second SMoE model, Mixtral-8x22B sets a new standard for performance and efficiency within the AI community. It is a sparse Mixture-of-Experts (SMoE) model that uses only 39B active parameters out of 141B, offering unparalleled cost efficiency for its size “[announcement page](https://mistral.ai/news/mixtral-8x22b/)”.

In the following documentation pages we use the terms “mixtral” and “mixtral_8x22b” to refer to the Mixtral-8x7B and Mixtral-8x22B models, respectively.

We provide recipes for pretraining and finetuning Mixtral models for two sizes: 8x7B, and 8x22B. The recipes use NeMo 2.0 and [NeMo-Run](https://github.com/NVIDIA/NeMo-Run). These recipes configure a `run.Partial` for one of the [nemo.collections.llm](https://docs.nvidia.com/nemo-framework/user-guide/nemo-2.0/index.html) api functions introduced in NeMo 2.0. The recipes are hosted in [mixtral_8x7b](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/recipes/mixtral_8x7b.py#L80) and [mixtral_8x22b](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/recipes/mixtral_8x22b.py#L78) files.

NeMo 2.0 Pretraining Recipes[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/mixtral.html.md#nemo-2-0-pretraining-recipes "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------

Note

The pretraining recipes use the `MockDataModule` for the `data` argument. You are expected to replace the `MockDataModule` with your own custom dataset.

We provide an example below on how to invoke the default recipe and override the data argument:

from nemo.collections import llm

pretrain = llm.mixtral_8x7b.pretrain_recipe(
    name="mixtral_8x7b_pretraining",
    dir=f"/path/to/checkpoints",
    num_nodes=2,
    num_gpus_per_node=8,
)

# # To override the data argument
# dataloader = a_function_that_configures_your_custom_dataset(
# gbs=gbs,
# mbs=mbs,
# seq_length=pretrain.model.config.seq_length,
# )
# pretrain.data = dataloader

NeMo 2.0 Finetuning Recipes[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/mixtral.html.md#nemo-2-0-finetuning-recipes "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------

Note

The finetuning recipes use the `SquadDataModule` for the `data` argument. You can replace the `SquadDataModule` with your custom dataset.

To import the HF model and convert to NeMo 2.0 format, run the following command (this only needs to be done once)

from nemo.collections import llm

if  __name__  == "__main__":
  llm.import_ckpt(model=llm.MixtralModel(llm.MixtralConfig8x7B()), source='hf://mistralai/Mixtral-8x7B-v0.1')

By default, the non-instruct version of the model is loaded. To load a different model, set `finetune.resume.restore_config.path=nemo://<hf model id>` or `finetune.resume.restore_config.path=<local model path>`

We provide an example below on how to invoke the default recipe and override the data argument:

from nemo.collections import llm

recipe = llm.mixtral_8x7b.finetune_recipe(
    name="mixtral_8x7b_finetuning",
    dir=f"/path/to/checkpoints",
    num_nodes=1,
    num_gpus_per_node=8,
    peft_scheme='lora',  # 'lora', 'none'
    packed_sequence=False,
)

# # To override the data argument
# dataloader = a_function_that_configures_your_custom_dataset(
# gbs=gbs,
# mbs=mbs,
# seq_length=recipe.model.config.seq_length,
# )
# recipe.data = dataloader

By default, the finetuning recipe will run LoRA finetuning with LoRA applied to all linear layers in the language model. To finetune the entire model without LoRA, set `peft_scheme='none'` in the recipe argument.

To finetune with sequence packing for a higher throughput, set `packed_sequence=True`. Note that you may need to tune the global batch size in order to achieve similar convergence.

Note

The configuration in the recipes is done using the NeMo-Run `run.Config` and `run.Partial` configuration objects. Please review the NeMo-Run [documentation](https://github.com/NVIDIA/NeMo-Run/docs/source/guides) to learn more about its configuration and execution system.

Once you have your final configuration ready, you can execute it on any of the NeMo-Run supported executors. The simplest is the local executor, which just runs the pretraining locally in a separate process. You can use it as follows:

import nemo_run as run

run.run(pretrain, executor=run.LocalExecutor())

Additionally, you can also run it directly in the same Python process as follows:

run.run(pretrain, direct=True)

A comprehensive list of pretraining recipes that we currently support or plan to support soon is provided below for reference:

| Recipe | Status |
| --- | --- |
| Mixtral 8x7B | Yes |
| Mixtral 8x7B FP8 | N/A |
| Mixtral 8x7B 16k | Yes |
| Mixtral 8x7B 64k | Yes |
| Mixtral 8x22B | Yes |
| Mixtral 8x22B FP8 | N/A |
| Mixtral 8x22B 16k | N/A |
| Mixtral 8x22B 64k | N/A |

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/mixtral.html.md#nemo-2-0-finetuning-recipes)
- [Mixtral of Experts](https://arxiv.org/abs/2401.04088)
- [announcement page](https://mistral.ai/news/mixtral-8x22b/)
- [NeMo-Run](https://github.com/NVIDIA/NeMo-Run)
- [nemo.collections.llm](https://docs.nvidia.com/nemo-framework/user-guide/nemo-2.0/index.html)
- [mixtral_8x7b](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/recipes/mixtral_8x7b.py#L80)
- [mixtral_8x22b](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/recipes/mixtral_8x22b.py#L78)
- [documentation](https://github.com/NVIDIA/NeMo-Run/docs/source/guides)
