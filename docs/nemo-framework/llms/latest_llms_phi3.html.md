# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/phi3.html.md

Title: Phi 3 — NVIDIA NeMo Framework User Guide

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/phi3.html

Published Time: Fri, 18 Jul 2025 19:27:37 GMT

Markdown Content:
Phi 3[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/phi3.html.md#phi-3 "Link to this heading")
--------------------------------------------------------------------------------------------------------------

[Microsoft’s Phi-3-mini-4K-Instruct is a 3.8B parameters, lightweight state of the art open trained model](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct.md/) The model belongs to the Phi-3 family with the Mini version in two variants 4K and 128K which is the context length (in tokens) that it can support We provide pre-defined recipes for pretraining and finetuning a Llama 3 model in two sizes: 8B and 70B, as well as Llama 3.1 model in three sizes: 8B, 70B and 405B. The recipes use NeMo 2.0 and [NeMo-Run](https://github.com/NVIDIA/NeMo-Run.md). These recipes configure a `run.Partial` for one of the [nemo.collections.llm](https://docs.nvidia.com/nemo-framework/user-guide/nemo-2.0/index.html.md) api functions introduced in NeMo 2.0. The recipes are hosted in the following files: [llama3_8b](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/recipes/llama3_8b.py.md), [llama3_70b](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/recipes/llama3_70b.py.md), [llama31_8b](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/recipes/llama31_8b.py.md), [llama31_70b](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/recipes/llama31_70b.py.md), [llama31_405b](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/recipes/llama31_405b.py.md).

NeMo 2.0 Pretraining Recipes[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/phi3.html.md#nemo-2-0-pretraining-recipes "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------

Note

The pretraining recipes use the `MockDataModule` for the `data` argument. You are expected to replace the `MockDataModule` with your custom dataset.

We provide an example below on how to invoke the default recipe and override the data argument:

from nemo.collections import llm

pretrain = llm.phi3_mini_4k_instruct.pretrain_recipe(
    name="phi3_mini_4k_instruct_pretraining",
    dir=f"/path/to/checkpoints",
    num_nodes=1,
    num_gpus_per_node=8,
)

# # To override the data argument
# dataloader = a_function_that_configures_your_custom_dataset(
# gbs=gbs,
# mbs=mbs,
# seq_length=pretrain.model.config.seq_length,
# )
# pretrain.data = dataloader

NeMo 2.0 Finetuning Recipes[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/phi3.html.md#nemo-2-0-finetuning-recipes "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------

Note

The finetuning recipes use the `SquadDataModule` for the `data` argument. You can replace the `SquadDataModule` with your custom dataset.

To import the HF model and convert to NeMo 2.0 format, run the following command (this only needs to be done once)

from pathlib import Path
from nemo.collections.llm import import_ckpt
from nemo.collections.llm.gpt.model.phi3mini import Phi3ConfigMini, Phi3Model
import_ckpt(model=Phi3Model(Phi3ConfigMini()),source='hf://microsoft/Phi-3-mini-4k-instruct')

We provide an example below on how to invoke the default recipe and override the data argument:

from nemo.collections import llm

recipe = llm.phi3_mini_4k_instruct.pretrain_recipe(
    name="phi3_mini_4k_instruct_pretrainin",
    dir=f"/path/to/checkpoints",
    num_nodes=1,
    num_gpus_per_node=1,
    peft_scheme='lora',  # 'lora', 'none'
    packed_sequence=None,
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

The configuration in the recipes is done using the NeMo-Run `run.Config` and `run.Partial` configuration objects. Please review the NeMo-Run [documentation](https://github.com/NVIDIA/NeMo-Run/tree/main/docs/source/guides.md) to learn more about its configuration and execution system.

Once you have your final configuration ready, you can execute it on any of the NeMo-Run supported executors. The simplest is the local executor, which just runs the pretraining locally in a separate process. You can use it as follows:

import nemo_run as run

run.run(pretrain, executor=run.LocalExecutor())

Additionally, you can also run it directly in the same Python process as follows:

run.run(pretrain, direct=True)

A comprehensive list of pretraining recipes that we currently support or plan to support soon is provided below for reference:

| Recipe | Status |
| --- | --- |
| Phi 3 mini 4k instruct | Yes |
| Phi 3 mini 128k instruct | N/A |
| Phi 3 small 8k instruct | N/A |

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/phi3.html.md#nemo-2-0-finetuning-recipes)
- [Microsoft’s Phi-3-mini-4K-Instruct is a 3.8B parameters, lightweight state of the art open trained model](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct.md/)
- [NeMo-Run](https://github.com/NVIDIA/NeMo-Run.md)
- [nemo.collections.llm](https://docs.nvidia.com/nemo-framework/user-guide/nemo-2.0/index.html.md)
- [llama3_8b](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/recipes/llama3_8b.py.md)
- [llama3_70b](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/recipes/llama3_70b.py.md)
- [llama31_8b](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/recipes/llama31_8b.py.md)
- [llama31_70b](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/recipes/llama31_70b.py.md)
- [llama31_405b](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/recipes/llama31_405b.py.md)
- [documentation](https://github.com/NVIDIA/NeMo-Run/tree/main/docs/source/guides.md)
