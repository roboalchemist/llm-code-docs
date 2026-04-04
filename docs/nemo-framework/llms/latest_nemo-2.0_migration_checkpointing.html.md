# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/checkpointing.html.md

Title: Migrate Checkpointing Configurations from NeMo 1.0 to NeMo 2.0#

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/checkpointing.html

Published Time: Thu, 30 Oct 2025 07:07:29 GMT

Markdown Content:
NeMo 1.0 (Previous Release)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/checkpointing.html.md#nemo-1-0-previous-release "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In NeMo 1.0, [distributed checkpointing](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/checkpoints/dist_ckpt.html.md?highlight=distributed%2520checkpointing#) was configured in the YAML configuration file.

# Distributed checkpoint setup
dist_ckpt_format: 'zarr' # Set to 'torch_dist' to use PyTorch distributed checkpoint format.
dist_ckpt_load_on_device: True # whether to load checkpoint weights directly on GPU or to CPU
dist_ckpt_parallel_save: False # if true, each worker will write its own part of the dist checkpoint
dist_ckpt_parallel_load: False # if true, each worker will load part of the dist checkpoint and exchange with NCCL. Might use some extra GPU memory
dist_ckpt_torch_dist_multiproc: 2 # number of extra processes per rank used during ckpt save with PyTorch distributed format
dist_ckpt_assume_constant_structure: False # set to True only if the state dict structure doesn't change within a single job. Allows caching some computation across checkpoint saves.
dist_ckpt_parallel_dist_opt: True # parallel save/load of a DistributedOptimizer. 'True' allows performant save and reshardable checkpoints. Set to 'False' only in order to minimize the number of checkpoint files.

NeMo 2.0 (New Release)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/checkpointing.html.md#nemo-2-0-new-release "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

In NeMo 2.0, these settings are controlled from the `MegatronStrategy`.

from nemo.collections import llm
from nemo import lightning as nl

strategy = nl.MegatronStrategy(
   save_ckpt_format='zarr',
   ckpt_load_on_device=True,
   ckpt_parallel_save=False,
   ckpt_parallel_load=False,
   ckpt_assume_constant_structure=False,
   ckpt_parallel_save_optim=False,
)

nl.Trainer(
   strategy=strategy,
   ...
)

Migrate Distributed Checkpoint Setup Settings[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/checkpointing.html.md#migrate-distributed-checkpoint-setup-settings "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1.   Locate the [distributed checkpoint setup](https://github.com/NVIDIA/NeMo/blob/00fe96f01baff193418e3d71e78acf3748907b6e/examples/nlp/language_modeling/conf/megatron_gpt_config.yaml#L176-L185) section in your NeMo 1.0 YAML config file.

2.   Pass the `distributed checkpoint setup` settings into `MegatronStrategy`:

strategy = nl.MegatronStrategy(
    save_ckpt_format='zarr',
    ckpt_load_on_device=True,
    ckpt_parallel_save=False,
    ckpt_parallel_load=False,
    ckpt_torch_dist_multiproc=2,
    ckpt_assume_constant_structure=False,
    ckpt_parallel_save_optim=False,
) 

Note

Non-distributed checkpointing is not supported by NeMo 2.0.

Convert NeMo 1.0 Checkpoint to NeMo 2.0 Checkpoint[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/checkpointing.html.md#convert-nemo-1-0-checkpoint-to-nemo-2-0-checkpoint "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We provide a script to convert NeMo 1.0 checkpoints to NeMo 2.0 checkpoints. The script is available at `scripts/checkpoint_converters/convert_nemo1_to_nemo2.py`.

1.   The NeMo 1.0 checkpoint is in the `model_name.nemo` tarball format. After you extract the tarball you will see the following structure:

model_name.nemo
├── model_config.yaml
├── model_weights
│ ├── distributed checkpointing directories/files in zarr or torch_dist format
│ ├── metadata.json
│ └── common.pt 
2.   The NeMo 2.0 checkpoint is a directory with the following structure. The content in the context directory may be optional:

model_name
├── context
│ ├── model_config.yaml
│ ├── io.json
│ └── tokenizer
├── weights
│ ├── distributed checkpointing directories/files in zarr or torch_dist format
│ ├── metadata.json
│ └── common.pt 
3.   The conversion script needs the NeMo 1.0 weights, NeMo 1.0 model ID (that specifis the model structure and configurations) and NeMo 1.0 tokenizer information (either sentencepiece tokenizer.model or Hugging Face tokenizer ID) to convert the checkpoint to NeMo 2.0 format. The script will create a new directory with the NeMo 2.0 checkpoint structure.

The script utilizes CPU and CPU memory for checkpoint conversion. When your NeMo 1.0 checkpoint uses Hugging Face tokenizer, the conversion script will download the tokenizer from Hugging Face. If the tokenizer comes from a gated repo, you will need to first log in to Hugging Face:

huggingface-cli login 
Currently, only sentencepice and Hugging Face tokenizers are supported.

The following commands should be used inside a NeMo container.

    *   You can pass the `model_name.nemo` tarball, which contains weights and tokenizer info, to the script. We take `meta-llama/Meta-Llama-3-8B` as an example:

python /opt/NeMo/scripts/checkpoint_converters/convert_nemo1_to_nemo2.py \
--input_path=Meta-Llama-3-8B.nemo \
--output_path=your_output_dir \
--model_id=meta-llama/Meta-Llama-3-8B

    *   If you have a model weight directory (whose structure is similar to the `model_weights` directory in the NeMo 1.0 checkpoint), you can pass the weight directory to the script. In this case, the script will also need the tokenizer info since the weights directory doesn’t contain this information. We take nemotron-3-8b-base-4k` as an example:

python /opt/NeMo/scripts/checkpoint_converters/convert_nemo1_to_nemo2.py \
--input_path=nemotron3-8b-extracted/model_weights \
--tokenizer_path=path_to_your_tokenizer_model.model \
--tokenizer_library=sentencepiece \
--output_path=your_output_dir \
--model_id=nvidia/nemotron-3-8b-base-4k

4.   Supported models: Currently, we have validated for the following models:

    *   `meta-llama/Meta-Llama-3-8B`

    *   `mistralai/Mixtral-8x7B-v0.1`

    *   `nvidia/nemotron-3-8b-base-4k`

Models of same family/structure and different sizes should work, but have not been validated. The model conversion will only work for models supported by NeMo 2.0. We will add validation for more models in the future. The list of available model IDs can be find in the script `scripts/checkpoint_converters/convert_nemo1_to_nemo2.py`. The `--model_id` argument should be one of the following:

    *   `meta-llama/Llama-2-7b-hf`

    *   `meta-llama/Llama-2-13b-hf`

    *   `meta-llama/Llama-2-70b-hf`

    *   `meta-llama/Meta-Llama-3-8B`

    *   `meta-llama/Meta-Llama-3-70B`

    *   `mistralai/Mixtral-8x7B-v0.1`

    *   `mistralai/Mixtral-8x22B-v0.1`

    *   `mistralai/Mistral-7B-v0.1`

    *   `nvidia/nemotron-3-8b-base-4k`

    *   `nemotron4-22b`

    *   `nemotron4-15b`

    *   `nemotron4-340b`

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/checkpointing.html.md#convert-nemo-1-0-checkpoint-to-nemo-2-0-checkpoint)
- [distributed checkpointing](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/checkpoints/dist_ckpt.html.md?highlight=distributed%2520checkpointing#)
- [distributed checkpoint setup](https://github.com/NVIDIA/NeMo/blob/00fe96f01baff193418e3d71e78acf3748907b6e/examples/nlp/language_modeling/conf/megatron_gpt_config.yaml#L176-L185)
