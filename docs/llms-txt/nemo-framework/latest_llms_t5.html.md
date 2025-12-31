# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/t5.html.md

Title: T5 — NVIDIA NeMo Framework User Guide

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/t5.html

Published Time: Fri, 18 Jul 2025 19:27:39 GMT

Markdown Content:
T5[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/t5.html.md#t5 "Link to this heading")
------------------------------------------------------------------------------------------------------

T5, or Text-to-Text Transfer Transformer, is a versatile language model that frames all natural language processing (NLP) tasks as text-to-text problems. This means that every task, whether it’s translation, summarization, or question answering, is treated uniformly by converting input text into output text. T5 employs a transformer architecture, utilizing both encoder and decoder components to effectively process and generate language.

We provide pre-defined recipes for pretraining and finetuning a T5 model in sizes: 220M, 3B and 11B. The recipes use NeMo 2.0 and [NeMo-Run](https://github.com/NVIDIA/NeMo-Run.md). These recipes configure a `run.Partial` for one of the [nemo.collections.llm](https://docs.nvidia.com/nemo-framework/user-guide/nemo-2.0/index.html.md) api functions introduced in NeMo 2.0. The recipes are hosted in [t5_220m](https://github.com/NVIDIA/NeMo/tree/main/nemo/collections/llm/recipes/t5_220m.py.md), [t5_3b](https://github.com/NVIDIA/NeMo/tree/main/nemo/collections/llm/recipes/t5_3b.py.md) and [t5_11b](https://github.com/NVIDIA/NeMo/tree/main/nemo/collections/llm/recipes/t5_11b.py.md) files.

NeMo 2.0 Pretraining Recipes[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/t5.html.md#nemo-2-0-pretraining-recipes "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------

Note

The pretraining recipes use the `MockDataModule` for the `data` argument. You are expected to replace the `MockDataModule` with your custom dataset.

We provide an example below on how to invoke the default recipe and override the data argument:

from nemo.collections import llm

pretrain = llm.t5_220m.pretrain_recipe(
    name="t5_220m_pretraining",
    dir=f"/path/to/checkpoints",
    num_nodes=1,
    num_gpus_per_node=8,
)

# # To override the data argument
# dataloader = a_function_that_configures_your_custom_dataset(
# global_batch_size=global_batch_size,
# micro_batch_size=micro_batch_size,
# seq_length=pretrain.model.config.seq_length,
# seq_length_dec=recipe.model.config.seq_length_dec,
# )
# pretrain.data = dataloader

NeMo 2.0 Finetuning Recipes[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/t5.html.md#nemo-2-0-finetuning-recipes "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

Note

The finetuning recipes use the `SquadDataModule` for the `data` argument. You can replace the `SquadDataModule` with your custom dataset.

We provide an example below on how to invoke the default recipe and override the data argument:

from nemo.collections import llm

recipe = llm.t5_220m.finetune_recipe(
    name="t5_220m_finetuning",
    checkpoint_path=f"/path/to/pretrained_checkpoints",
    dir=f"/path/to/checkpoints",
    num_nodes=1,
    num_gpus_per_node=8,
    peft_scheme='lora',  # 'lora', 'none'
)

# # To override the data argument
# dataloader = a_function_that_configures_your_custom_dataset(
# global_batch_size=global_batch_size,
# micro_batch_size=micro_batch_size,
# seq_length=recipe.model.config.seq_length,
# seq_length_dec=recipe.model.config.seq_length_dec,
# )
# recipe.data = dataloader

By default, the finetuning recipe will run LoRA finetuning with LoRA applied to all linear layers in the language model. To finetune the entire model without LoRA, set `peft_scheme='none'` in the recipe argument.

Note

The configuration in the recipes is done using the NeMo-Run `run.Config` and `run.Partial` configuration objects. Please review the NeMo-Run [documentation](https://github.com/NVIDIA/NeMo-Run/tree/main/docs/source/guides.md) to learn more about its configuration and execution system.

Once you have your final configuration ready, you can execute it on any of the NeMo-Run supported executors. The simplest is the local executor, which just runs the pretraining locally in a separate process. You can use it as follows:

import nemo_run as run

run.run(pretrain, executor=run.LocalExecutor())

Additionally, you can also run it directly in the same Python process as follows:

run.run(pretrain, direct=True)

A list of pretraining recipes that we currently support or plan to support soon is provided below for reference:

| Recipe | Status |
| --- | --- |
| T5 220M | Yes |
| T5 3B | Yes |
| T5 11B | Yes |

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/t5.html.md#nemo-2-0-finetuning-recipes)
- [NeMo-Run](https://github.com/NVIDIA/NeMo-Run.md)
- [nemo.collections.llm](https://docs.nvidia.com/nemo-framework/user-guide/nemo-2.0/index.html.md)
- [t5_220m](https://github.com/NVIDIA/NeMo/tree/main/nemo/collections/llm/recipes/t5_220m.py.md)
- [t5_3b](https://github.com/NVIDIA/NeMo/tree/main/nemo/collections/llm/recipes/t5_3b.py.md)
- [t5_11b](https://github.com/NVIDIA/NeMo/tree/main/nemo/collections/llm/recipes/t5_11b.py.md)
- [documentation](https://github.com/NVIDIA/NeMo-Run/tree/main/docs/source/guides.md)
