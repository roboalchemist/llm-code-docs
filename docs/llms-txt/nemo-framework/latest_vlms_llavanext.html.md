# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/vlms/llavanext.html.md

Title: LLaVA-Next — NVIDIA NeMo Framework User Guide

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/vlms/llavanext.html

Published Time: Thu, 30 Oct 2025 07:07:34 GMT

Markdown Content:
LLaVA-Next[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/vlms/llavanext.html.md#llava-next "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------

LLaVA-Next is an extension of the LLaVA model designed to handle high-resolution images efficiently through tiling. This enables users to work with larger image sizes for improved accuracy in various VL tasks. For more details about LLaVA-Next, refer to the [LLaVA-Next blog](https://llava-vl.github.io/blog/2024-01-30-llava-next/).

We have extended the NeVA model to support LLaVA-Next. Users can easily switch to LLaVA-Next for high-resolution image tiling support with minimal configuration changes. To switch to LLaVA-Next from NeVA (LLaVA), replace the task encoder with LlavaNextTaskEncoder. It is designed to handle image tiling, supporting the LLaVA-Next architecture.

To get started with LLaVA-Next, follow these steps, which are similar to NeVA but with minor modifications.

Import from Hugging Face to NeMo 2.0[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/vlms/llavanext.html.md#import-from-hugging-face-to-nemo-2-0 "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following script downloads the checkpoint for LLM (vicuna - 7b) and converts it to NeMo format. The converted checkpoint is stored in the NeMo cache folder at: `~/.cache/nemo`. For example, when used with the NeMo container, the full path is `/root/.cache/nemo/models/lmsys/vicuna-7b-v1.5/`. The checkpoint can be used to initialize the LLM for pretraining LlaVa-Next.

from nemo.collections.llm import import_ckpt
from nemo.collections.llm import Llama2Config7B, LlamaModel

if  __name__  == "__main__":
    # Specify the Hugging Face model ID
    hf_model_id = "lmsys/vicuna-7b-v1.5"

    # Import the model and convert to NeMo 2.0 format
    import_ckpt(
        model=LlamaModel(Llama2Config7B()),
        source=f"hf://{hf_model_id}",
    )

This step is optional and is intended for users who want to fine-tune the LLaVA-Next model starting from a pretrained checkpoint from Hugging Face.

To run the script, save it as import_llava_next.py and then execute it:

python import_llava_next.py

from nemo.collections.llm import import_ckpt
from nemo.collections import vlm

if  __name__  == '__main__':
    # Specify the Hugging Face model ID
    hf_model_id = "llava-hf/llava-v1.6-vicuna-7b-hf"

    # Import the model and convert to NeMo 2.0 format
    import_ckpt(
        model=vlm.LlavaNextModel(vlm.LlavaNextConfig7B()),  # Model configuration
        source=f"hf://{hf_model_id}",  # Hugging Face model source
    )

NeMo 2.0 Pretraining Recipes[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/vlms/llavanext.html.md#nemo-2-0-pretraining-recipes "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Similar to the NeVA model, we provide some default recipes for pretraining LLaVA-NEXT [llava_next_7b](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/vlm/recipes/llava_next_7b.py).

from nemo.collections import vlm

finetune = vlm.llava_next_7b.pretrain_recipe(
    name="llava_next_7b_pretrain",
    dir=f"/path/to/checkpoints",
    num_nodes=1,
    num_gpus_per_node=8,
    language_model_from_pretrained='/root/.cache/nemo/models/lmsys/vicuna-7b-v1.5/',
    # Can be None or change based on local checkpoint path
)

NeMo 2.0 Fine-Tuning Recipes[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/vlms/llavanext.html.md#nemo-2-0-fine-tuning-recipes "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

We also provide a fine-tuning recipe - [llava_next_7b](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/vlm/recipes/llava_next_7b.py) that you can use.

from nemo.collections import vlm

finetune = vlm.llava_next_7b.finetune_recipe(
    name="llava_next_7b_finetune",
    dir=f"/path/to/checkpoints",
    num_nodes=1,
    num_gpus_per_node=8,
    peft_scheme='none',  # 'lora', 'none'
)

Note

The configuration in the recipes is done using the NeMo-Run `run.Config` and `run.Partial` configuration objects. Please review the NeMo-Run [documentation](https://docs.nvidia.com/nemo/run/latest/guides/) to learn more about its configuration and execution system.

Note

The recipes use the `MockDataModule` for the `data` argument. You are expected to replace the `MockDataModule` with your custom dataset.

Once you have your final configuration ready, you can execute it using any of the NeMo-Run supported executors. The simplest option is the local executor, which runs the pretraining locally in a separate process. You can use it as follows:

import nemo_run as run

run.run(finetune, executor=run.LocalExecutor())

Additionally, you can also run it directly in the same Python process as follows:

run.run(finetune, direct=True)

Use the Energon Dataloader[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/vlms/llavanext.html.md#use-the-energon-dataloader "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------

Below is an example of how to set up the [Energon](https://github.com/NVIDIA/Megatron-Energon) data module for LLaVA-Next training:

from nemo.collections.multimodal.data.energon.config import MultiModalSampleConfig
from nemo.collections.vlm import LlavaNextTaskEncoder
from nemo.collections.multimodal.data.energon import EnergonMultiModalDataModule
from transformers import AutoProcessor

# Load the processor from the pretrained LLaVA-Next model
processor = AutoProcessor.from_pretrained("llava-hf/llava-v1.6-mistral-7b-hf")

# Paths and configuration
data_path = "<path_to_dataset>"
image_processor = processor.image_processor
tokenizer = processor.tokenizer

# Define multimodal sample configuration
multimodal_sample_config = MultiModalSampleConfig()

# Initialize the LLaVA-Next task encoder
task_encoder = LlavaNextTaskEncoder(
    tokenizer=tokenizer,
    image_processor=image_processor,
    multimodal_sample_config=multimodal_sample_config,
)

# Create the data module
data = EnergonMultiModalDataModule(
    path=data_path,
    tokenizer=tokenizer,
    image_processor=image_processor,
    num_workers=8,
    micro_batch_size=4,
    global_batch_size=32,
    multimodal_sample_config=multimodal_sample_config,
    task_encoder=task_encoder,
)

Replace the `MockDataModule` in the default recipes with the above data.

from nemo.collections import vlm

# Define the fine-tuning recipe
finetune = vlm.llava_next_7b.finetune_recipe(
  name="llava_next_7b_finetune",
  dir=f"/path/to/checkpoints",
  num_nodes=1,
  num_gpus_per_node=8,
  peft_scheme='none',  # 'lora', 'none'
)

# Assign the above data module to the finetuning recipe
finetune.data = data

We have also included additional example scripts to further customize LLaVA-NeXT training:

*   **Pretraining**: [llava_next_pretrain.py](https://github.com/NVIDIA/NeMo/tree/main/scripts/vlm/llava_next_pretrain.py)

*   **Finetuning**: [llava_next_finetune.py](https://github.com/NVIDIA/NeMo/tree/main/scripts/vlm/llava_next_finetune.py)

*   **Generation**: [llava_next_generation.py](https://github.com/NVIDIA/NeMo/tree/main/scripts/vlm/llava_next_generation.py)

*   **NeMo Run**: [llava_next_nemo_run.py](https://github.com/NVIDIA/NeMo/tree/main/scripts/vlm/llava_next_nemo_run.py)

These scripts allow for flexible and comprehensive training workflows tailored to your requirements.

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/vlms/llavanext.html.md#use-the-energon-dataloader)
- [LLaVA-Next blog](https://llava-vl.github.io/blog/2024-01-30-llava-next/)
- [llava_next_7b](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/vlm/recipes/llava_next_7b.py)
- [documentation](https://docs.nvidia.com/nemo/run/latest/guides/)
- [Energon](https://github.com/NVIDIA/Megatron-Energon)
- [llava_next_pretrain.py](https://github.com/NVIDIA/NeMo/tree/main/scripts/vlm/llava_next_pretrain.py)
- [llava_next_finetune.py](https://github.com/NVIDIA/NeMo/tree/main/scripts/vlm/llava_next_finetune.py)
- [llava_next_generation.py](https://github.com/NVIDIA/NeMo/tree/main/scripts/vlm/llava_next_generation.py)
- [llava_next_nemo_run.py](https://github.com/NVIDIA/NeMo/tree/main/scripts/vlm/llava_next_nemo_run.py)
