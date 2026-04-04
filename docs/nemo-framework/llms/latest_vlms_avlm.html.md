# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/vlms/avlm.html.md

Title: Audio-Vision Language Model — NVIDIA NeMo Framework User Guide

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/vlms/avlm.html

Published Time: Fri, 05 Sep 2025 19:01:37 GMT

Markdown Content:
Audio-Vision Language Model[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/vlms/avlm.html.md#audio-vision-language-model "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------

AVLM (Audio-Vision Language Model) is an extension of the VLM (Vision Language Model) framework designed to handle both audio and visual modalities in a unified manner. It enables users to perform multimodal reasoning across audio and vision inputs, such as speech transcribing, video captioning, image-audio question-answering.

We have extended the NeVA model to support AVLM by providing a separate audio encoder to process input speech and sound. To migrate from NeVA to AVLM, users would: (1) replace the task encoder with AvlmTaskEncoder (which is designed to jointly encode audio and vision features while maintaining compatibility with the AVLM architecture); (2) set up AVLM model’s AVLMConfig architecture configuration, which is similar to NeVa’s NevaConfig, but now support both vision and audio encoder and projection layer.

To get started with AVLM, follow these steps, which are similar to those for NeVA, with minor adjustments to accommodate audio inputs. We provide some default training recipes for AVLM at [avlm_8b](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/avlm/recipes/avlm_8b.py). This pretraining and finetuning recipe works along with the AVLM-8B model architecture configuration defined in [avlm.py](https://github.com/NVIDIA/NeMo/tree/main/nemo/collections/avlm/model/avlm.py).

Additionally, users can also look at the example script, such as [avlm_pretrain.py](https://github.com/NVIDIA/NeMo/tree/main/scripts/avlm/avlm_pretrain.py) that contains all scripts for model configuration, data, training recipes in one file.

Configure AVLM Model[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/vlms/avlm.html.md#configure-avlm-model "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

We can configure each component of the AVLM model (language model, vision encoder, vision projector, audio encoder, audio projector), as shown in the default model architecture in configuration [avlm.py](https://github.com/NVIDIA/NeMo/tree/main/nemo/collections/avlm/model/avlm.py).

@dataclass
class AVLMConfig8B(AVLMConfig):
 """
 Configuration class for the 8B parameter variant of the AVLM model.

 """

    from transformers import PretrainedConfig

    language_transformer_config: TransformerConfig = field(default_factory=lambda: Llama3Config8B())
    vision_transformer_config: Union[TransformerConfig, PretrainedConfig] = field(
        default_factory=lambda: HFCLIPVisionConfig(
            pretrained_model_name_or_path="openai/clip-vit-large-patch14-336",
        )
    )
    vision_projection_config: TransformerConfig = field(
        default_factory=lambda: MultimodalProjectorConfig(
            projector_type="mlp2x_gelu",
            input_size=1024,
            hidden_size=4096,
            ffn_hidden_size=4096)
    )
    audio_transformer_config: TransformerConfig = field(
        default_factory=lambda: ASRModuleConfig(
             _target_ ="nemo.collections.speechlm.modules.asr_module.ASRModuleConfig",
            use_hf_auto_model=True,
            hf_trust_remote_code=False,
            hf_load_pretrained_weights=True,
            pretrained_model="openai/whisper-large-v3",
            hidden_size=1280,
        target_module="model.encoder",
        )
    )
    audio_projection_config: TransformerConfig = field(
        default_factory=lambda: MultimodalProjectorConfig(
            projector_type="mlp2x_gelu",
            input_size=1280,
            hidden_size=4096,
            ffn_hidden_size=4096)
    )

NeMo 2.0 Modalities Alignment Recipes[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/vlms/avlm.html.md#nemo-2-0-modalities-alignment-recipes "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Similar to NeVA model, the first stage of training an AVLM model is aligning the modalities embeddings with text embeddings. This includes vision alignment and audio alignment.

Vision Alignment[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/vlms/avlm.html.md#vision-alignment "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------

In this step, we only tune the vision projection layers to align vision embeddings with text embeddings. This step uses image/video-text datasets, such as image/video captioning, image question-answering, etc. The model’s components are intialized from pretrained models: Llama-3-8B for the language model, CLIP for vision encoder, Whisper-large-v3 for the audio encoder. The vision and audio projection layers are initialized from scratch. We can control which components will be training through the freeze_modules argument.

from nemo.collections import avlm

finetune = avlm.avlm_8b.pretrain_recipe(
    name="avlm_8b_pretrain",
    dir=f"/path/to/avlm_vision_alignment_checkpoints",
    num_nodes=1,
    num_gpus_per_node=8,
    language_model_from_pretrained='/root/.cache/nemo/models/meta/llama3_8b',
    # Can be None or change based on local checkpoint path
    freeze_modules={
      "freeze_language_model": True,
      "freeze_vision_model": True,
      "freeze_audio_model": True,
      "freeze_vision_projection": False,
      "freeze_audio_projection": True,
    }
)

Audio Alignment[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/vlms/avlm.html.md#audio-alignment "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------

In this step, we only tune the audio projection layers to align audio embeddings with text embeddings. This step uses audio-text datasets, such as sound captioning, speech transcribing, speech translation, etc. The model is initialized with previous step’s checkpoint.

from nemo.collections import avlm

finetune = avlm.avlm_8b.pretrain_recipe(
    name="avlm_8b_pretrain",
    dir=f"/path/to/avlm_audio_alignment_checkpoints",
    num_nodes=1,
    num_gpus_per_node=8,
    checkpoint_path=f"/path/to/avlm_vision_alignment_checkpoints",
    # Can be None or change based on local checkpoint path
    freeze_modules={
      "freeze_language_model": True,
      "freeze_vision_model": True,
      "freeze_audio_model": True,
      "freeze_vision_projection": True,
      "freeze_audio_projection": False,
    }
)

NeMo 2.0 Fine-Tuning Recipes[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/vlms/avlm.html.md#nemo-2-0-fine-tuning-recipes "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------

Here, depending on our choices, we can tune all or some components of the model (vision encoder, audio encoder, vision projector, audio projector, language model). This stage uses datasets involving both modalities in one sample, such as video (with audio) captioning, image-audio question-answering, etc.

When finetuning, we can also enable PEFT (Parameter-Efficient Fine-Tuning) for efficient tuning the large language model, avoid out-of-memory problem when training all components in the AVLM model. Users can enable this by setting peft_scheme argument to “lora”.

from nemo.collections import vlm

finetune = avlm.avlm_8b.finetune_recipe(
    name="avlm_8b_finetune",
    dir=f"/path/to/avlm_multimodals_finetune_checkpoints",
    num_nodes=1,
    num_gpus_per_node=8,
    peft_scheme='none',  # 'lora', 'none',
    checkpoint_path=f"/path/to/avlm_audio_alignment_checkpoints",
    freeze_modules={
      "freeze_language_model": False,
      "freeze_vision_model": True,
      "freeze_audio_model": True,
      "freeze_vision_projection": False,
      "freeze_audio_projection": False,
    }
)

Note

The configuration in the recipes is done using the NeMo-Run `run.Config` and `run.Partial` configuration objects. Please review the NeMo-Run [documentation](https://github.com/NVIDIA/NeMo-Run/tree/main/docs/source/guides) to learn more about its configuration and execution system.

Note

The recipes use the `MockDataModule` for the `data` argument. You are expected to replace the `MockDataModule` with your custom dataset.

Once you have your final configuration ready, you can execute it using any of the NeMo-Run supported executors. The simplest option is the local executor, which runs the pretraining locally in a separate process. You can use it as follows:

import nemo_run as run

run.run(finetune, executor=run.LocalExecutor())

Additionally, you can also run it directly in the same Python process as follows:

run.run(finetune, direct=True)

Use the Energon Dataloader[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/vlms/avlm.html.md#use-the-energon-dataloader "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

Below is an example of how to set up the [Energon](https://github.com/NVIDIA/Megatron-Energon) data module for AVLM training.

Note that, for AVLM’s Energon data module, we will provide the vision and audio encoders’s configs to AVLMSampleConfig. This is so that when processing data, we can directly calculate the exact numnber of tokens representing an image/audio, and insert their corresponding placeholders into the input tokens in advance. This helps simplify the model’s logic when using certain parallelisms, such as pipeline, context parallelisms, etc.

from nemo.collections.avlm.data.energon import AVLMSampleConfig
from nemo.collections.avlm import AVLMTaskEncoder
from nemo.collections.avlm.data.energon import AVLMDataModule
from nemo.collections.common.tokenizers.huggingface.auto_tokenizer import AutoTokenizer
from transformers import AutoProcessor

# Load the processor and tokenizer
image_processor = AutoProcessor.from_pretrained("openai/clip-vit-large-patch14")
tokenizer = AutoTokenizer("meta-llama/Meta-Llama-3-8B")

# Paths and configuration
data_path = "<path_to_dataset>"

# Define multimodal sample configuration
avlm_sample_config = AVLMSampleConfig(
    audio_encoder_config={
        "model_type": "whisper",
        "window_stride": 0.01,
        "sample_rate": 16000,
        "fixed_max_audio_length": None,
        "encoder_down_sampling": 2,
    },
    image_encoder_config={
        "model_type": "vit",
        "img_width": 336,
        "img_height": 336,
        "patch_size": 14,
        "projection_downsample_factor": None,
    },
)

# Initialize the AVLM task encoder
task_encoder = AVLMTaskEncoder(
    tokenizer=tokenizer,
    audio_processor=None,
    image_processor=image_processor,
    multimodal_sample_config=avlm_sample_config,
)

# Create the data module
data = AVLMDataModule(
    path=data_path,
    num_workers=num_workers,
    micro_batch_size=mbs,
    global_batch_size=gbs,
    seq_length=decoder_seq_length,
    tokenizer=tokenizer,
    audio_processor=None,
    image_processor=image_processor,
    multimodal_sample_config=avlm_sample_config,
    task_encoder=task_encoder,
)

Replace the `MockDataModule` in the default recipes with the above data.

from nemo.collections import vlm

# Define the fine-tuning recipe
finetune = avlm.avlm_8b.finetune_recipe(
  name="avlm_8b_finetune",
  dir=f"/path/to/checkpoints",
  num_nodes=1,
  num_gpus_per_node=8,
  peft_scheme='none',  # 'lora', 'none'
)

# Assign the above data module to the finetuning recipe
finetune.data = data

We have also included additional example scripts to further customize AVLM training:

*   **Pretraining**: [avlm_pretrain.py](https://github.com/NVIDIA/NeMo/tree/main/scripts/avlm/avlm_pretrain.py)

*   **Generation**: [avlm_generation.py](https://github.com/NVIDIA/NeMo/tree/main/scripts/avlm/avlm_generate.py)

*   **NeMo Run**: [avlm_nemo_run.py](https://github.com/NVIDIA/NeMo/tree/main/scripts/avlm/avlm_nemo_run.py)

These scripts allow for flexible and comprehensive training workflows tailored to your requirements.

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/vlms/avlm.html.md#use-the-energon-dataloader)
- [avlm_8b](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/avlm/recipes/avlm_8b.py)
- [avlm.py](https://github.com/NVIDIA/NeMo/tree/main/nemo/collections/avlm/model/avlm.py)
- [avlm_pretrain.py](https://github.com/NVIDIA/NeMo/tree/main/scripts/avlm/avlm_pretrain.py)
- [documentation](https://github.com/NVIDIA/NeMo-Run/tree/main/docs/source/guides)
- [Energon](https://github.com/NVIDIA/Megatron-Energon)
- [avlm_generation.py](https://github.com/NVIDIA/NeMo/tree/main/scripts/avlm/avlm_generate.py)
- [avlm_nemo_run.py](https://github.com/NVIDIA/NeMo/tree/main/scripts/avlm/avlm_nemo_run.py)
