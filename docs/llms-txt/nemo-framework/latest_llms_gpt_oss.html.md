# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/gpt_oss.html.md

Title: GPT-OSS — NVIDIA NeMo Framework User Guide

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/gpt_oss.html

Published Time: Thu, 30 Oct 2025 07:07:28 GMT

Markdown Content:
GPT-OSS[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/gpt_oss.html.md#gpt-oss "Link to this heading")
---------------------------------------------------------------------------------------------------------------------

GPT-OSS is an open-weight model released by OpenAI, providing transparent and accessible large language models. GPT-OSS models are built on the Mixture-of-Experts (MoE) transformer decoder architecture with Sink Attention and alternating Sliding-Window Attention (SWA). The model family includes two variants: GPT-OSS 20B and GPT-OSS 120B, designed to serve different computational requirements while maintaining high-quality text generation capabilities. The models are designed to be used within agentic workflows with strong instruction following, tool use like web search and Python code execution, and reasoning capabilities—including the ability to adjust the reasoning effort for tasks that don’t require complex reasoning.

We provide pre-defined recipes for finetuning GPT-OSS models in two sizes: 20B and 120B using NeMo 2.0 and [NeMo-Run](https://github.com/NVIDIA/NeMo-Run). These recipes configure a `run.Partial` for one of the [nemo.collections.llm](https://docs.nvidia.com/nemo-framework/user-guide/nemo-2.0/index.html) api functions introduced in NeMo 2.0.

Note

Please use the custom container `nvcr.io/nvidia/nemo:25.07.gpt_oss` when working with GPT-OSS. Please make sure you update to the latest version of `transformers`.

NeMo 2.0 Finetuning Recipes[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/gpt_oss.html.md#nemo-2-0-finetuning-recipes "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------

Note

The finetuning recipes use the `SquadDataModule` for the `data` argument. You can replace the `SquadDataModule` with your custom dataset. Note that this model is a reasoning model with a specific chat template, so it is best to use a chat dataset with the `use_hf_tokenizer_chat_template=True` argument when finetuning.

To import the HF model and convert to NeMo 2.0 format, run the following command (this only needs to be done once):

cd <HF_MODEL_DIR>
apt-get update && apt-get install git-lfs
git lfs install
git clone https://huggingface.co/openai/gpt-oss-20b
git clone https://huggingface.co/openai/gpt-oss-120b

from nemo.collections import llm

if  __name__  == "__main__":
    # For GPT-OSS 20B
    llm.import_ckpt(model=llm.GPTOSSModel(llm.GPTOSSConfig20B()), source='hf:///<HF_MODEL_DIR>/gpt-oss-20b')

    # For GPT-OSS 120B
    # llm.import_ckpt(model=llm.GPTOSSModel(llm.GPTOSSConfig120B()), source='hf:///<HF_MODEL_DIR>/gpt-oss-120b')

To import the original OpenAI checkpoint and convert to NeMo 2.0 format, run the following command (this only needs to be done once):

from nemo.collections import llm

if  __name__  == "__main__":
    # For GPT-OSS 20B
    llm.import_ckpt(model=llm.GPTOSSModel(llm.GPTOSSConfig20B()), source='openai:///path/to/gpt-oss-20b')

    # For GPT-OSS 120B
    # llm.import_ckpt(model=llm.GPTOSSModel(llm.GPTOSSConfig120B()), source='openai:///path/to/gpt-oss-120b')

We provide an example below on how to invoke the default recipe and override the data argument:

from nemo.collections import llm

# For GPT-OSS 20B
recipe = llm.gpt_oss_20b.finetune_recipe(
    name="gpt_oss_20b_finetuning",
    dir=f"/path/to/checkpoints",
    num_nodes=1,
    num_gpus_per_node=8,
    peft_scheme='lora',  # 'lora', 'none'
)

# For GPT-OSS 120B
# recipe = llm.gpt_oss_120b.finetune_recipe(
# name="gpt_oss_120b_finetuning",
# dir=f"/path/to/checkpoints",
# num_nodes=4,
# num_gpus_per_node=8,
# peft_scheme='lora', # 'lora', 'none'
# )

# # To override the data argument
# dataloader = a_function_that_configures_your_custom_dataset(
# gbs=gbs,
# mbs=mbs,
# seq_length=recipe.model.config.seq_length,
# use_hf_tokenizer_chat_template=True,
# )
# recipe.data = dataloader

By default, the finetuning recipe will run LoRA finetuning with LoRA applied to linear layers in the attention block in the language model. To finetune the entire model without LoRA, set `peft_scheme='none'` in the recipe argument.

Note

The configuration in the recipes is done using the NeMo-Run `run.Config` and `run.Partial` configuration objects. Please review the NeMo-Run [documentation](https://docs.nvidia.com/nemo/run/latest/guides/) to learn more about its configuration and execution system.

Once you have your final configuration ready, you can execute it on any of the NeMo-Run supported executors. The simplest is the local executor, which just runs the pretraining locally in a separate process. You can use it as follows:

import nemo_run as run

run.run(recipe, executor=run.LocalExecutor())

Additionally, you can also run it directly in the same Python process as follows:

run.run(recipe, direct=True)

Inference[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/gpt_oss.html.md#inference "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------

To run inference with GPT-OSS models, you can use the following command:

# For GPT-OSS 20B
torchrun --nproc-per-node=1 /opt/NeMo/scripts/llm/generate.py \
 --model_path=<PATH_TO_NEMO2_MODEL> \
 --devices=1 \
 --num_tokens_to_generate=512 \
 --temperature=0.0 \
 --top_p=0.0 \
 --top_k=1 \
 --disable_flash_decode

# For GPT-OSS 120B
# torchrun --nproc-per-node=8 /opt/NeMo/scripts/llm/generate.py \
# --model_path=<PATH_TO_NEMO2_MODEL> \
# --ep=4 \
# --pp=2 \
# --devices=8 \
# --num_tokens_to_generate=512 \
# --temperature=0.0 \
# --top_p=0.0 \
# --top_k=1 \
# --disable_flash_decode

Export to HF[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/gpt_oss.html.md#export-to-hf "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------

After training or finetuning your GPT-OSS model, you can export it to Hugging Face format for easy sharing and deployment:

from nemo.collections import llm

# Export NeMo checkpoint to Hugging Face format
llm.export_ckpt(
    target="hf",
    path=Path("<path_to_nemo_checkpoint>"),
    output_path=Path("<path_to_output_hf_model>"),
)

Note

Ensure you have sufficient disk space and appropriate permissions when exporting large models. The export process may take some time depending on the model size and your storage setup.

Deployment[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/gpt_oss.html.md#deployment "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------

### Install TensorRT-LLM in NeMo GPT-OSS container[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/gpt_oss.html.md#install-tensorrt-llm-in-nemo-gpt-oss-container "Link to this heading")

The NeMo Framework container does not have TensorRT-LLM pre-installed. To expoert gpt-oss to TRT-LLM, run the following commands inside the container `nvcr.io/nvidia/nemo:25.07.gpt_oss`.

1.   Reinstall NeMo Export-Deploy package

rm -r /opt/Export-Deploy && pip install git+https://github.com/NVIDIA-NeMo/Export-Deploy.git 
2.   Install prerequisites for TensorRT-LLM

curl -sL https://github.com/NVIDIA/TensorRT-LLM/raw/refs/heads/feat/gpt-oss/docker/common/install_tensorrt.sh | bash 
3.   Install TensorRT-LLM with GPT-OSS branch

git clone -b feat/gpt-oss --single-branch https://github.com/NVIDIA/TensorRT-LLM.git
cd TensorRT-LLM
python scripts/build_wheel.py --clean --trt_root /usr/local/tensorrt --benchmark --job_count $(nproc)
pip install ./build/tensorrt_llm*.whl 

### Export and Deploy Hugging Face checkpoint to TensorRT-LLM and Triton Inference Server[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/gpt_oss.html.md#export-and-deploy-hugging-face-checkpoint-to-tensorrt-llm-and-triton-inference-server "Link to this heading")

from nemo_deploy.nlp.trtllm_api_deployable import TensorRTLLMAPIDeployable
from nemo_deploy import DeployPyTriton

deployable = TensorRTLLMAPIDeployable(
    hf_model_id_path="openai/gpt-oss-120b",
    tensor_parallel_size=2,
)

output = deployable.generate(
    prompts=["What is the color of a banana?"],
    max_length=20,
)
print("output: ", output)

# Deploy to Triton
nm = DeployPyTriton(model=deployable, triton_model_name="gpt-oss", http_port=8000)
nm.deploy()
nm.serve()

### Query Triton Inference Server[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/gpt_oss.html.md#query-triton-inference-server "Link to this heading")

from nemo_deploy.nlp import NemoQueryTRTLLMAPI

nq = NemoQueryTRTLLMAPI(url="localhost:8000", model_name="gpt-oss")
output = nq.query_llm(
    prompts=["What is the capital of France?"],
    max_length=100,
)
print(output)

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/gpt_oss.html.md#query-triton-inference-server)
- [NeMo-Run](https://github.com/NVIDIA/NeMo-Run)
- [nemo.collections.llm](https://docs.nvidia.com/nemo-framework/user-guide/nemo-2.0/index.html)
- [documentation](https://docs.nvidia.com/nemo/run/latest/guides/)
