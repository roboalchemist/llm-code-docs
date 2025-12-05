# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/gemma2.html.md

Title: Gemma 2 — NVIDIA NeMo Framework User Guide

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/gemma2.html

Published Time: Fri, 05 Sep 2025 18:59:52 GMT

Markdown Content:
Gemma 2[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/gemma2.html.md#gemma-2 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------

Gemma 2 offers three new, powerful, and efficient models available in 2, 9, and 27 billion parameter sizes, all with built-in safety advancements. It adopts the transformer decoder framework while adding multi-query attention, RoPE, GeGLU activations, and more. More information is available in Google’s release blog.

Note

Currently, Gemma 2 does not support CuDNN Fused Attention. The recipes disable CuDNN attention and use Flash Attention instead.

We provide pre-defined recipes for finetuning Gemma 2 models using NeMo 2.0 and [NeMo-Run](https://github.com/NVIDIA/NeMo-Run). These recipes configure a `run.Partial` for one of the [nemo.collections.llm](https://docs.nvidia.com/nemo-framework/user-guide/nemo-2.0/index.html) api functions introduced in NeMo 2.0. The recipes are hosted in [gemma_2_2b](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/recipes/gemma2_2b.py), [gemma_2_9b](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/recipes/gemma2_9b.py), and [gemma_2_27b](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/recipes/gemma2_27b.py).

NeMo 2.0 Finetuning Recipes[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/gemma2.html.md#nemo-2-0-finetuning-recipes "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------

Note

The finetuning recipes use the `SquadDataModule` for the `data` argument. You can replace the `SquadDataModule` with your custom dataset.

To import the HF model and convert to NeMo 2.0 format, run the following command (this only needs to be done once)

from nemo.collections import llm
llm.import_ckpt(model=llm.Gemma2Model(llm.Gemma2Config2B()), source='hf://google/gemma-2-2b')

By default, the non-instruct version of the model is loaded. To load a different model, set `finetune.resume.restore_config.path=nemo://<hf model id>` or `finetune.resume.restore_config.path=<local model path>`

We provide an example below on how to invoke the default recipe and override the data argument:

from nemo.collections import llm

recipe = llm.gemma2_2b.finetune_recipe(
    name="gemma2_2b_finetuning",
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

The configuration in the recipes is done using the NeMo-Run `run.Config` and `run.Partial` configuration objects. Please review the NeMo-Run [documentation](https://github.com/NVIDIA/NeMo-Run/tree/main/docs/source/guides) to learn more about its configuration and execution system.

Once you have your final configuration ready, you can execute it on any of the NeMo-Run supported executors. The simplest is the local executor, which just runs the pretraining locally in a separate process. You can use it as follows:

import nemo_run as run

run.run(recipe, executor=run.LocalExecutor())

Additionally, you can also run it directly in the same Python process as follows:

run.run(recipe, direct=True)

| Recipe | Status |
| --- | --- |
| Gemma 2 2B | Yes |
| Gemma 2 9B | Yes |
| Gemma 2 27B | Yes |

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/gemma2.html.md#nemo-2-0-finetuning-recipes)
- [NeMo-Run](https://github.com/NVIDIA/NeMo-Run)
- [nemo.collections.llm](https://docs.nvidia.com/nemo-framework/user-guide/nemo-2.0/index.html)
- [gemma_2_2b](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/recipes/gemma2_2b.py)
- [gemma_2_9b](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/recipes/gemma2_9b.py)
- [gemma_2_27b](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/recipes/gemma2_27b.py)
- [documentation](https://github.com/NVIDIA/NeMo-Run/tree/main/docs/source/guides)
