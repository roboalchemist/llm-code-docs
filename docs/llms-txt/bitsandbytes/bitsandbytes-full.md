# Bitsandbytes Documentation

Source: https://huggingface.co/docs/bitsandbytes/llms-full.txt

---

# Bitsandbytes

## Docs

- [Integrations](https://huggingface.co/docs/bitsandbytes/v0.49.1/integrations.md)
- [FAQs](https://huggingface.co/docs/bitsandbytes/v0.49.1/faqs.md)
- [FSDP-QLoRA](https://huggingface.co/docs/bitsandbytes/v0.49.1/fsdp_qlora.md)
- [Troubleshoot](https://huggingface.co/docs/bitsandbytes/v0.49.1/errors.md)
- [Quickstart](https://huggingface.co/docs/bitsandbytes/v0.49.1/quickstart.md)
- [bitsandbytes](https://huggingface.co/docs/bitsandbytes/v0.49.1/index.md)
- [Installation Guide](https://huggingface.co/docs/bitsandbytes/v0.49.1/installation.md)
- [8-bit optimizers](https://huggingface.co/docs/bitsandbytes/v0.49.1/optimizers.md)
- [Contribution Guide](https://huggingface.co/docs/bitsandbytes/v0.49.1/contributing.md)
- [Papers, related resources & how to cite](https://huggingface.co/docs/bitsandbytes/v0.49.1/explanations/resources.md)
- [8-bit optimizers](https://huggingface.co/docs/bitsandbytes/v0.49.1/explanations/optimizers.md)
- [Overview](https://huggingface.co/docs/bitsandbytes/v0.49.1/reference/functional.md)
- [SGD](https://huggingface.co/docs/bitsandbytes/v0.49.1/reference/optim/sgd.md)
- [Lion](https://huggingface.co/docs/bitsandbytes/v0.49.1/reference/optim/lion.md)
- [RMSprop](https://huggingface.co/docs/bitsandbytes/v0.49.1/reference/optim/rmsprop.md)
- [AdamW](https://huggingface.co/docs/bitsandbytes/v0.49.1/reference/optim/adamw.md)
- [LAMB](https://huggingface.co/docs/bitsandbytes/v0.49.1/reference/optim/lamb.md)
- [LARS](https://huggingface.co/docs/bitsandbytes/v0.49.1/reference/optim/lars.md)
- [AdEMAMix](https://huggingface.co/docs/bitsandbytes/v0.49.1/reference/optim/ademamix.md)
- [Overview](https://huggingface.co/docs/bitsandbytes/v0.49.1/reference/optim/optim_overview.md)
- [Adam](https://huggingface.co/docs/bitsandbytes/v0.49.1/reference/optim/adam.md)
- [AdaGrad](https://huggingface.co/docs/bitsandbytes/v0.49.1/reference/optim/adagrad.md)
- [Embedding](https://huggingface.co/docs/bitsandbytes/v0.49.1/reference/nn/embeddings.md)
- [4-bit quantization](https://huggingface.co/docs/bitsandbytes/v0.49.1/reference/nn/linear4bit.md)
- [LLM.int8()](https://huggingface.co/docs/bitsandbytes/v0.49.1/reference/nn/linear8bit.md)

### Integrations
https://huggingface.co/docs/bitsandbytes/v0.49.1/integrations.md

# Integrations

bitsandbytes is widely integrated with many of the libraries in the Hugging Face and wider PyTorch ecosystem. This guide provides a brief overview of the integrations and how to use bitsandbytes with them. For more details, you should refer to the linked documentation for each library.

## Transformers

> [!TIP]
> Learn more in the bitsandbytes Transformers integration [guide](https://huggingface.co/docs/transformers/quantization#bitsandbytes).

With Transformers, it's very easy to load any model in 4 or 8-bit and quantize them on the fly. To configure the quantization parameters, specify them in the [BitsAndBytesConfig](https://huggingface.co/docs/transformers/v5.0.0rc2/en/main_classes/quantization#transformers.BitsAndBytesConfig) class.

For example, to load and quantize a model to 4-bits and use the bfloat16 data type for compute:

> [!WARNING]
> bfloat16 is the ideal `compute_dtype` if your hardware supports it. While the default `compute_dtype`, float32, ensures backward compatibility (due to wide-ranging hardware support) and numerical stability, it is large and slows down computations. In contrast, float16 is smaller and faster but can lead to numerical instabilities. bfloat16 combines the best aspects of both; it offers the numerical stability of float32 and the reduced memory footprint and speed of a 16-bit data type. Check if your hardware supports bfloat16 and configure it using the `bnb_4bit_compute_dtype` parameter in [BitsAndBytesConfig](https://huggingface.co/docs/transformers/v5.0.0rc2/en/main_classes/quantization#transformers.BitsAndBytesConfig)!

```py
from transformers import AutoModelForCausalLM, BitsAndBytesConfig

quantization_config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_compute_dtype=torch.bfloat16)
model_4bit = AutoModelForCausalLM.from_pretrained(
    "bigscience/bloom-1b7",
    device_map=device_map,
    quantization_config=quantization_config,
)
```

### 8-bit optimizers

You can use any of the 8-bit or paged optimizers with Transformers by passing them to the [Trainer](https://huggingface.co/docs/transformers/v5.0.0rc2/en/main_classes/trainer#transformers.Trainer) class on initialization. All bitsandbytes optimizers are supported by passing the correct string in the [TrainingArguments](https://huggingface.co/docs/transformers/v5.0.0rc2/en/main_classes/trainer#transformers.TrainingArguments) `optim` parameter. For example, to load a [PagedAdamW32bit](/docs/bitsandbytes/v0.49.1/en/reference/optim/adamw#bitsandbytes.optim.PagedAdamW32bit) optimizer:

```py
from transformers import TrainingArguments, Trainer

training_args = TrainingArguments(
    ...,
    optim="paged_adamw_32bit",
)
trainer = Trainer(model, training_args, ...)
trainer.train()
```

## PEFT

> [!TIP]
> Learn more in the bitsandbytes PEFT integration [guide](https://huggingface.co/docs/peft/developer_guides/quantization#quantization).

PEFT builds on the bitsandbytes Transformers integration, and extends it for training with a few more steps. Let's prepare the 4-bit model from the section above for training.

Call the [prepare_model_for_kbit_training](https://huggingface.co/docs/peft/v0.18.0/en/package_reference/peft_model#peft.prepare_model_for_kbit_training) method to prepare the model for training. This only works for Transformers models!

```py
from peft import prepare_model_for_kbit_training

model_4bit = prepare_model_for_kbit_training(model_4bit)
```

Setup a [LoraConfig](https://huggingface.co/docs/peft/v0.18.0/en/package_reference/lora#peft.LoraConfig) to use QLoRA:

```py
from peft import LoraConfig

config = LoraConfig(
    r=16,
    lora_alpha=8,
    target_modules="all-linear",
    lora_dropout=0.05
    bias="none",
    task_type="CAUSAL_LM"
)
```

Now call the [get_peft_model](https://huggingface.co/docs/peft/v0.18.0/en/package_reference/peft_model#peft.get_peft_model) function on your model and config to create a trainable `PeftModel`.

```py
from peft import get_peft_model

model = get_peft_model(model_4bit, config)
```

## Accelerate

> [!TIP]
> Learn more in the bitsandbytes Accelerate integration [guide](https://huggingface.co/docs/accelerate/usage_guides/quantization).

bitsandbytes is also easily usable from Accelerate and you can quantize any PyTorch model by passing a [BnbQuantizationConfig](https://huggingface.co/docs/accelerate/v1.12.0/en/package_reference/utilities#accelerate.utils.BnbQuantizationConfig) with your desired settings, and then calling the [load_and_quantize_model](https://huggingface.co/docs/accelerate/v1.12.0/en/package_reference/utilities#accelerate.utils.load_and_quantize_model) function to quantize it.

```py
from accelerate import init_empty_weights
from accelerate.utils import BnbQuantizationConfig, load_and_quantize_model
from mingpt.model import GPT

model_config = GPT.get_default_config()
model_config.model_type = 'gpt2-xl'
model_config.vocab_size = 50257
model_config.block_size = 1024

with init_empty_weights():
    empty_model = GPT(model_config)

bnb_quantization_config = BnbQuantizationConfig(
  load_in_4bit=True,
  bnb_4bit_compute_dtype=torch.bfloat16,  # optional
  bnb_4bit_use_double_quant=True,         # optional
  bnb_4bit_quant_type="nf4"               # optional
)

quantized_model = load_and_quantize_model(
  empty_model,
  weights_location=weights_location,
  bnb_quantization_config=bnb_quantization_config,
  device_map = "auto"
)
```

## PyTorch Lightning and Lightning Fabric

bitsandbytes is available from:

- [PyTorch Lightning](https://lightning.ai/docs/pytorch/stable/), a deep learning framework for professional AI researchers and machine learning engineers who need maximal flexibility without sacrificing performance at scale.
- [Lightning Fabric](https://lightning.ai/docs/fabric/stable/), a fast and lightweight way to scale PyTorch models without boilerplate.

Learn more in the bitsandbytes PyTorch Lightning integration [guide](https://lightning.ai/docs/pytorch/stable/common/precision_intermediate.html#quantization-via-bitsandbytes).

## Lit-GPT

bitsandbytes is integrated with [Lit-GPT](https://github.com/Lightning-AI/lit-gpt), a hackable implementation of state-of-the-art open-source large language models. Lit-GPT is based on Lightning Fabric, and it can be used for quantization during training, finetuning, and inference.

Learn more in the bitsandbytes Lit-GPT integration [guide](https://github.com/Lightning-AI/lit-gpt/blob/main/tutorials/quantize.md).

## Blog posts

To learn in more detail about some of bitsandbytes integrations, take a look at the following blog posts:

- [Making LLMs even more accessible with bitsandbytes, 4-bit quantization and QLoRA](https://huggingface.co/blog/4bit-transformers-bitsandbytes)
- [A Gentle Introduction to 8-bit Matrix Multiplication for transformers at scale using Hugging Face Transformers, Accelerate and bitsandbytes](https://huggingface.co/blog/hf-bitsandbytes-integration)

### FAQs
https://huggingface.co/docs/bitsandbytes/v0.49.1/faqs.md

# FAQs

Please submit your questions in [this Github Discussion thread](https://github.com/bitsandbytes-foundation/bitsandbytes/discussions/1013) if you feel that they will likely affect a lot of other users and that they haven't been sufficiently covered in the documentation.

We'll pick the most generally applicable ones and post the QAs here or integrate them into the general documentation (also feel free to submit doc PRs, please).

### FSDP-QLoRA
https://huggingface.co/docs/bitsandbytes/v0.49.1/fsdp_qlora.md

# FSDP-QLoRA

FSDP-QLoRA combines data parallelism (FSDP enables sharding model parameters, optimizer states, and gradients across GPUs), 4-bit quantization, and LoRA to train LLMs up to 70B parameters on a dual 24GB GPU system. This technique was released by [Answer.AI](https://www.answer.ai/posts/2024-03-06-fsdp-qlora) in collaboration with bitsandbytes to make training LLMs more efficient and accessible for everyone.

This guide provides a brief guide on how bitsandbytes supports storing quantized weights to enable FSDP-QLoRA, and how to run training with the Hugging Face libraries.

> [!TIP]
> Other changes required for bitsandbytes to support FSDP-QLoRA, such as reconstructing the weights from the quantization metadata and preventing quantizing already quantized weights when they're moved from a CPU to GPU, are documented in this [Pull Request](https://github.com/bitsandbytes-foundation/bitsandbytes/pull/970) and described in the [Enabling 70B Finetuning on Consumer GPUs](https://www.answer.ai/posts/2024-03-14-fsdp-qlora-deep-dive) blog post. We highly recommend reading these resources for a better understanding of FSDP-QLoRA!

## Quantized data storage

FSDP only supports sharding float data types which can be problematic because quantized weights are typically stored as integer data types (uint8). bitsandbytes doesn't have this problem because it uses `StoreChar` to read and write quantized weights regardless of the data type storage. This makes it simple to add a `quant_storage` parameter to the [Linear4bit](/docs/bitsandbytes/v0.49.1/en/reference/nn/linear4bit#bitsandbytes.nn.Linear4bit) and [Params4bit](/docs/bitsandbytes/v0.49.1/en/reference/nn/linear4bit#bitsandbytes.nn.Params4bit) classes and set it to `torch.uint8` to maintain backward compatibility with the codebase. With the `quant_storage` parameter, you can select any of the FSDP supported data types to shard [Linear4bit](/docs/bitsandbytes/v0.49.1/en/reference/nn/linear4bit#bitsandbytes.nn.Linear4bit) with such as bfloat16, float16 or float32.

You'll typically access and configure this option from [transformers.BitsAndBytesConfig](https://huggingface.co/docs/transformers/v5.0.0rc2/en/main_classes/quantization#transformers.BitsAndBytesConfig) by setting the `bnb_4bit_quant_storage` parameter. It is very **important** the `quant_storage` data type matches the data types used throughout the model because FSDP can only wrap layers and modules that have the *same floating data type*. Making sure the data types are aligned will ensure the model is correctly sharded.

> [!TIP]
> The `compute_dtype` is the data type used for computation inside the CUDA kernel, where the 4-bit quantized weights are unpacked from the data type in `quant_storage` and dequantized to `compute_dtype`. We recommend using torch.bfloat16 (if available on your hardware) for better numerical stability.

```py
from transformers import BitsAndBytesConfig, AutoModelForCausalLM

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_quant_storage=torch.bfloat16,
)

model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-70b",
    quantization_config=bnb_config,
    torch_dtype=torch.bfloat16,
)
```

Check out this [section](https://hf.co/docs/peft/main/en/accelerate/fsdp#use-peft-qlora-and-fsdp-for-finetuning-large-models-on-multiple-gpus) of the PEFT documentation for the config file and training code to run FSDP-QLoRA training.

## Training

> [!TIP]
> FSDP is a distributed training framework that needs to be launched as a distributed training job with a library like [Accelerate](https://hf.co/docs/accelerate/index) or [torchrun](https://pytorch.org/docs/stable/elastic/run.html). The launch command provided in this section uses Accelerate to launch the training script.

bitsandbytes is deeply integrated with the Hugging Face ecosystem, making it easy to use with libraries like [Transformers](https://hf.co/docs/transformers), [PEFT](https://hf.co/docs/peft), and [TRL](https://hf.co/docs/trl).

PEFT provides a configuration file ([fsdp_config_qlora.yaml](https://github.com/huggingface/peft/blob/main/examples/sft/configs/fsdp_config_qlora.yaml)), launch command ([run_peft_qlora_fsdp.sh](https://github.com/huggingface/peft/blob/main/examples/sft/run_peft_qlora_fsdp.sh)), and training script ([train.py](https://github.com/huggingface/peft/blob/main/examples/sft/train.py)) for running FSDP-QLoRA. To learn more, check out the [Use PEFT QLoRA and FSDP for finetuning large models on multiple GPUs](https://huggingface.co/docs/peft/main/en/accelerate/fsdp#use-peft-qlora-and-fsdp-for-finetuning-large-models-on-multiple-gpus) documentation. This section briefly covers the steps to run FSDP-QLoRA training.

Before you begin, make sure you have the latest libraries installed.

```bash
pip install -U bitsandbytes accelerate transformers peft trl
```

The important change that enables FSDP-QLoRA training is the `bnb_4bit_quant_storage` parameter in the [BitsAndBytesConfig](https://huggingface.co/docs/transformers/v5.0.0rc2/en/main_classes/quantization#transformers.BitsAndBytesConfig) class. This allows you to set the storage data type of the quantized weights to a float data type.

```py
from transformers import BitsAndBytesConfig

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_storage=torch.bfloat16,
)
```

Pass the [BitsAndBytesConfig](https://huggingface.co/docs/transformers/v5.0.0rc2/en/main_classes/quantization#transformers.BitsAndBytesConfig) to a model to set it up for FSDP-QLoRA. You should set the `torch_dtype` parameter to match `bnb_4bit_quant_storage` so that the [Linear4bit](/docs/bitsandbytes/v0.49.1/en/reference/nn/linear4bit#bitsandbytes.nn.Linear4bit) layers are wrapped identically to the `Linear` layers. If the storage types do not match, then each [Linear4bit](/docs/bitsandbytes/v0.49.1/en/reference/nn/linear4bit#bitsandbytes.nn.Linear4bit) layer is wrapped individually.

```py
from transformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-70b",
    quantization_config=bnb_config,
    torch_dtype=torch.bfloat16,
)
```

Configure the [LoraConfig](https://huggingface.co/docs/peft/v0.18.0/en/package_reference/lora#peft.LoraConfig) class for QLoRA training by setting `target_modules="all-linear"`.

```py
from peft import LoraConfig

peft_config = LoraConfig(
    lora_alpha=16,
    lora_dropout=0.1,
    r=64,
    bias="none",
    task_type="CAUSAL_LM",
    target_modules="all-linear",
)
```

Now you can pass everything to the [SFTTrainer](https://huggingface.co/docs/trl/v0.26.2/en/sft_trainer#trl.SFTTrainer) for training.

```py
from trl import SFTTrainer

trainer = SFTTrainer(
    model=model,
    train_dataset=dataset,
    peft_config=peft_config,
    processing_class=tokenizer,
    args=training_arguments,
)
trainer.train()
```

## Resources

To learn more about FSDP and QLoRA, check out the following resources:

- The [AnswerDotAI/fsdp_qlora](https://github.com/AnswerDotAI/fsdp_qlora) repository.
- The introductory [You can now train a 70b language model at home](https://www.answer.ai/posts/2024-03-06-fsdp-qlora.html) blog post by Answer.AI.
- For an introduction to FSDP, read the [Introducing PyTorch Fully Sharded Data Parallel (FSDP) API](https://pytorch.org/blog/introducing-pytorch-fully-sharded-data-parallel-api) blog post.
- For more details about QLoRA, take a look at the [Making LLMs even more accessible with bitsandbytes, 4-bit quantization and QLoRA](https://huggingface.co/blog/4bit-transformers-bitsandbytes) blog post.

### Troubleshoot
https://huggingface.co/docs/bitsandbytes/v0.49.1/errors.md

# Troubleshoot

## No kernel image available

This problem arises with the cuda version loaded by bitsandbytes is not supported by your GPU, or if you pytorch CUDA version mismatches.

To solve this problem you need to debug ``$LD_LIBRARY_PATH``, ``$CUDA_HOME`` as well as ``$PATH``. You can print these via ``echo $PATH``. You should look for multiple paths to different CUDA versions. This can include versions in your anaconda path, for example ``$HOME/anaconda3/lib``. You can check those versions via ``ls -l $HOME/anaconda3/lib/*cuda*`` or equivalent paths. Look at the CUDA versions of files in these paths. Does it match with ``nvidia-smi``?

If you are feeling lucky, you can also try to compile the library from source. This can be still problematic if your PATH variables have multiple cuda versions. As such, it is recommended to figure out path conflicts before you proceed with compilation.

## `fatbinwrap`

This error occurs if there is a mismatch between CUDA versions in the C++ library and the CUDA part. Make sure you have right CUDA in your `$PATH` and `$LD_LIBRARY_PATH` variable. In the conda base environment you can find the library under:

```bash
ls $CONDA_PREFIX/lib/*cudart*
```
Make sure this path is appended to the `LD_LIBRARY_PATH` so bnb can find the CUDA runtime environment library (cudart).

If this does not fix the issue, please try compilation from source next.

If this does not work, please open an issue and paste the printed environment if you call `make` and the associated error when running bnb.

### Quickstart
https://huggingface.co/docs/bitsandbytes/v0.49.1/quickstart.md

# Quickstart

## How does it work?

... work in progress ...

(Community contributions would we very welcome!)

## Minimal examples

The following code illustrates the steps above.

```py
code examples will soon follow
```

### bitsandbytes
https://huggingface.co/docs/bitsandbytes/v0.49.1/index.md

# bitsandbytes

bitsandbytes enables accessible large language models via k-bit quantization for PyTorch. bitsandbytes provides three main features for dramatically reducing memory consumption for inference and training:

* 8-bit optimizers uses block-wise quantization to maintain 32-bit performance at a small fraction of the memory cost.
* LLM.int8() or 8-bit quantization enables large language model inference with only half the required memory and without any performance degradation. This method is based on vector-wise quantization to quantize most features to 8-bits and separately treating outliers with 16-bit matrix multiplication.
* QLoRA or 4-bit quantization enables large language model training with several memory-saving techniques that don't compromise performance. This method quantizes a model to 4-bits and inserts a small set of trainable low-rank adaptation (LoRA) weights to allow training.

# License

bitsandbytes is MIT licensed.

### Installation Guide
https://huggingface.co/docs/bitsandbytes/v0.49.1/installation.md

# Installation Guide

Welcome to the installation guide for the `bitsandbytes` library! This document provides step-by-step instructions to install `bitsandbytes` across various platforms and hardware configurations.

We provide official support for NVIDIA GPUs, CPUs, Intel XPUs, and Intel Gaudi. We also have experimental support for additional platforms such as AMD ROCm and Apple Silicon.

## Table of Contents

- [System Requirements](#requirements)
- [NVIDIA CUDA](#cuda)
  - [Installation via PyPI](#cuda-pip)
  - [Compile from Source](#cuda-compile)
- [Intel XPU](#xpu)
  - [Installation via PyPI](#xpu-pip)
- [Intel Gaudi](#gaudi)
  - [Installation via PyPI](#gaudi-pip)
- [CPU](#cpu)
  - [Installation via PyPI](#cpu-pip)
  - [Compile from Source](#cpu-compile)
- [AMD ROCm (Preview)](#rocm)
  - [Installation via PyPI](#rocm-pip)
  - [Compile from Source](#rocm-compile)
- [Preview Wheels](#preview-wheels)

## System Requirements[[requirements]]

These are the minimum requirements for `bitsandbytes` across all platforms. Please be aware that some compute platforms may impose more strict requirements.

* Python >= 3.10
* PyTorch >= 2.3

## NVIDIA CUDA[[cuda]]

`bitsandbytes` is currently supported on NVIDIA GPUs with [Compute Capability](https://developer.nvidia.com/cuda-gpus) 6.0+.
The library can be built using CUDA Toolkit versions as old as **11.8**.

| **Feature**                     | **CC Required** | **Example Hardware Requirement**            |
|---------------------------------|-----------------|---------------------------------------------|
| LLM.int8()                      | 7.5+            | Turing (RTX 20 series, T4) or newer GPUs    |
| 8-bit optimizers/quantization   | 6.0+            | Pascal (GTX 10X0 series, P100) or newer GPUs|
| NF4/FP4 quantization            | 6.0+            | Pascal (GTX 10X0 series, P100) or newer GPUs|

### Installation via PyPI[[cuda-pip]]

This is the most straightforward and recommended installation option.

The currently distributed `bitsandbytes` packages are built with the following configurations:

| **OS**             | **CUDA Toolkit** | **Host Compiler**    | **Targets**
|--------------------|------------------|----------------------|--------------
| **Linux x86-64**   | 11.8 - 12.6      | GCC 11.2             | sm60, sm70, sm75, sm80, sm86, sm89, sm90
| **Linux x86-64**   | 12.8 - 12.9      | GCC 11.2             | sm70, sm75, sm80, sm86, sm89, sm90, sm100, sm120
| **Linux x86-64**   | 13.0             | GCC 11.2             | sm75, sm80, sm86, sm89, sm90, sm100, sm120
| **Linux aarch64**  | 11.8 - 12.6      | GCC 11.2             | sm75, sm80, sm90
| **Linux aarch64**  | 12.8 - 13.0      | GCC 11.2             | sm75, sm80, sm90, sm100, sm110, sm120, sm121
| **Windows x86-64** | 11.8 - 12.6      | MSVC 19.43+ (VS2022) | sm50, sm60, sm75, sm80, sm86, sm89, sm90
| **Windows x86-64** | 12.8 - 12.9      | MSVC 19.43+ (VS2022) | sm70, sm75, sm80, sm86, sm89, sm90, sm100, sm120
| **Windows x86-64** | 13.0             | MSVC 19.43+ (VS2022) | sm75, sm80, sm86, sm89, sm90, sm100, sm120

The Linux build has a minimum glibc version of 2.24.

Use `pip` or `uv` to install the latest release:

```bash
pip install bitsandbytes
```

### Compile from Source[[cuda-compile]]

> [!TIP]
> Don't hesitate to compile from source! The process is pretty straight forward and resilient. This might be needed for older CUDA Toolkit versions or Linux distributions, or other less common configurations.

For Linux and Windows systems, compiling from source allows you to customize the build configurations. See below for detailed platform-specific instructions (see the `CMakeLists.txt` if you want to check the specifics and explore some additional options):

To compile from source, you need CMake >= **3.22.1** and Python >= **3.10** installed. Make sure you have a compiler installed to compile C++ (`gcc`, `make`, headers, etc.). It is recommended to use GCC 11 or newer.

For example, to install a compiler and CMake on Ubuntu:

```bash
apt-get install -y build-essential cmake
```

You should also install CUDA Toolkit by following the [NVIDIA CUDA Installation Guide for Linux](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html) guide. The current minimum supported CUDA Toolkit version that we support is **11.8**.

```bash
git clone https://github.com/bitsandbytes-foundation/bitsandbytes.git && cd bitsandbytes/
cmake -DCOMPUTE_BACKEND=cuda -S .
make
pip install -e .   # `-e` for "editable" install, when developing BNB (otherwise leave that out)
```

> [!TIP]
> If you have multiple versions of the CUDA Toolkit installed or it is in a non-standard location, please refer to CMake CUDA documentation for how to configure the CUDA compiler.

Compilation from source on Windows systems require Visual Studio with C++ support as well as an installation of the CUDA Toolkit.

To compile from source, you need CMake >= **3.22.1** and Python >= **3.10** installed. You should also install CUDA Toolkit by following the [CUDA Installation Guide for Windows](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html) guide from NVIDIA. The current minimum supported CUDA Toolkit version that we support is **11.8**.

```bash
git clone https://github.com/bitsandbytes-foundation/bitsandbytes.git && cd bitsandbytes/
cmake -DCOMPUTE_BACKEND=cuda -S .
cmake --build . --config Release
pip install -e .   # `-e` for "editable" install, when developing BNB (otherwise leave that out)
```

Big thanks to [wkpark](https://github.com/wkpark), [Jamezo97](https://github.com/Jamezo97), [rickardp](https://github.com/rickardp), [akx](https://github.com/akx) for their amazing contributions to make bitsandbytes compatible with Windows.

## Intel XPU[[xpu]]

* A compatible PyTorch version with Intel XPU support is required. The current minimum is **PyTorch 2.6.0**. It is recommended to use the latest stable release. See [Getting Started on Intel GPU](https://docs.pytorch.org/docs/stable/notes/get_start_xpu.html) for guidance.

### Installation via PyPI[[xpu-pip]]

This is the most straightforward and recommended installation option.

The currently distributed `bitsandbytes` packages are built with the following configurations:

| **OS**             | **oneAPI Toolkit** | **Kernel Implementation** |
|--------------------|------------------|----------------------|
| **Linux x86-64**   | 2025.1.3         | SYCL + Triton        |
| **Windows x86-64** | 2025.1.3         | SYCL + Triton        |

The Linux build has a minimum glibc version of 2.34.

Use `pip` or `uv` to install the latest release:

```bash
pip install bitsandbytes
```

## Intel Gaudi[[gaudi]]

* A compatible PyTorch version with Intel Gaudi support is required. The current minimum is **Gaudi v1.21** with **PyTorch 2.6.0**. It is recommended to use the latest stable release. See the Gaudi software [installation guide](https://docs.habana.ai/en/latest/Installation_Guide/index.html) for guidance.

### Installation from PyPI[[gaudi-pip]]

Use `pip` or `uv` to install the latest release:

```bash
pip install bitsandbytes
```

## CPU[[cpu]]

### Installation from PyPI[[cpu-pip]]

This is the most straightforward and recommended installation option.

The currently distributed `bitsandbytes` packages are built with the following configurations:

| **OS**             | **Host Compiler**    | Hardware Minimum
|--------------------|----------------------|----------------------|
| **Linux x86-64**   | GCC 11.4             | AVX2                 |
| **Linux aarch64**  | GCC 11.4             |                      |
| **Windows x86-64** | MSVC 19.43+ (VS2022) | AVX2                 |
| **macOS arm64**    | Apple Clang 17       |                      |

The Linux build has a minimum glibc version of 2.24.

Use `pip` or `uv` to install the latest release:

```bash
pip install bitsandbytes
```

### Compile from Source[[cpu-compile]]

To compile from source, simply install the package from source using `pip`. The package will be built for CPU only at this time.

```bash
git clone https://github.com/bitsandbytes-foundation/bitsandbytes.git && cd bitsandbytes/
pip install -e .
```

## AMD ROCm (Preview)[[rocm]]

* Support for AMD GPUs is currently in a preview state.
* All features are supported for consumer RDNA devices.
* The Data Center products currently lack support for the default 4bit blocksize of 64, and as such default to 128.
* A compatible PyTorch version with AMD ROCm support is required. It is recommended to use the latest stable release. See [PyTorch on ROCm](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/pytorch-install.html) for guidance.

### Installation from PyPI[[rocm-pip]]

This is the most straightforward and recommended installation option.

The currently distributed `bitsandbytes` are built with the following configurations:

| **OS**             | **ROCm** | **Targets**
|--------------------|----------|---------------------------------------------------------------------|
| **Linux x86-64**   | 6.2.4    | CDNA: gfx90a, gfx942 / RDNA: gfx1100, gfx1101
| **Linux x86-64**   | 6.3.4    | CDNA: gfx90a, gfx942 / RDNA: gfx1100, gfx1101
| **Linux x86-64**   | 6.4.4    | CDNA: gfx90a, gfx942 / RDNA: gfx1100, gfx1101, gfx1150, gfx1151, gfx1200, gfx1201
| **Linux x86-64**   | 7.0.2    | CDNA: gfx90a, gfx942, gfx950 / RDNA: gfx1100, gfx1101, gfx1150, gfx1151, gfx1200, gfx1201
| **Linux x86-64**   | 7.1.0    | CDNA: gfx90a, gfx942, gfx950 / RDNA:  gfx1100, gfx1101, gfx1150, gfx1151, gfx1200, gfx1201

**Windows is not currently supported.**

Use `pip` or `uv` to install the latest release:

```bash
pip install bitsandbytes
```

### Compile from Source[[rocm-compile]]

bitsandbytes can be compiled from ROCm 6.2 - ROCm 7.1.

To compile from source, you need CMake >= **3.31.6**.

```bash
# Install bitsandbytes from source
# Clone bitsandbytes repo
git clone https://github.com/bitsandbytes-foundation/bitsandbytes.git && cd bitsandbytes/

# Compile & install
apt-get install -y build-essential cmake  # install build tools dependencies, unless present
cmake -DCOMPUTE_BACKEND=hip -S .  # Use -DBNB_ROCM_ARCH="gfx90a;gfx942" to target specific gpu arch
make
pip install -e .   # `-e` for "editable" install, when developing BNB (otherwise leave that out)
```

## Preview Wheels[[preview-wheels]]

If you would like to use new features even before they are officially released and help us test them, feel free to install the wheel directly from our CI (*the wheel links will remain stable!*):

```bash
# Note: if you don't want to reinstall our dependencies, append the `--no-deps` flag!

# x86_64 (most users)
pip install --force-reinstall https://github.com/bitsandbytes-foundation/bitsandbytes/releases/download/continuous-release_main/bitsandbytes-1.33.7.preview-py3-none-manylinux_2_24_x86_64.whl

# ARM/aarch64
pip install --force-reinstall https://github.com/bitsandbytes-foundation/bitsandbytes/releases/download/continuous-release_main/bitsandbytes-1.33.7.preview-py3-none-manylinux_2_24_aarch64.whl
```

```bash
# Note: if you don't want to reinstall our dependencies, append the `--no-deps` flag!
pip install --force-reinstall https://github.com/bitsandbytes-foundation/bitsandbytes/releases/download/continuous-release_main/bitsandbytes-1.33.7.preview-py3-none-win_amd64.whl
```

```bash
# Note: if you don't want to reinstall our dependencies, append the `--no-deps` flag!
pip install --force-reinstall https://github.com/bitsandbytes-foundation/bitsandbytes/releases/download/continuous-release_main/bitsandbytes-1.33.7.preview-py3-none-macosx_14_0_arm64.whl
```

### 8-bit optimizers
https://huggingface.co/docs/bitsandbytes/v0.49.1/optimizers.md

# 8-bit optimizers

With 8-bit optimizers, large models can be finetuned with 75% less GPU memory without losing any accuracy compared to training with standard 32-bit optimizers. The reduced memory requirements means 8-bit optimizers are 4x faster than a standard optimizer, and no hyperparameter tuning is required.

This guide will show you how to use 8-bit optimizers.

> [!WARNING]
> 8-bit optimizers reduce memory usage and accelerate optimization on a wide range of tasks. However, since 8-bit optimizers only reduce memory proportional to the number of parameters, models that use large amounts of activation memory, such as convolutional networks, don't really benefit from 8-bit optimizers. 8-bit optimizers are most beneficial for training or finetuning models with many parameters on highly memory-constrained GPUs.

8-bit optimizers are a drop-in replacement for regular optimizers which means they also accept the same arguments as a regular optimizer. For NLP models, it is recommended to use the [StableEmbedding](/docs/bitsandbytes/v0.49.1/en/reference/nn/embeddings#bitsandbytes.nn.StableEmbedding) class to improve stability and results.

```diff
import bitsandbytes as bnb

- adam = torch.optim.Adam(...)
+ adam = bnb.optim.Adam8bit(...)

# recommended for NLP models
- before: torch.nn.Embedding(...)
+ bnb.nn.StableEmbedding(...)
```

By default, all parameter tensors with less than 4096 elements are kept at 32-bits even if you initialize those parameters with 8-bit optimizers. This is done because small tensors do not save much memory and often contain highly variable parameters (biases) or parameters that require high precision (batch norm, layer norm).

You can change this value with the `min_8bit_size` parameter. For example, if you want to optimize parameters to 8-bits only if the minimum size is 16384 values (it is recommended to use multiples of 4096):

```py
import bitsandbytes as bnb

adam = bnb.optim.Adam8bit(model.parameters(), min_8bit_size=16384)
```

Other parameters you can configure include the learning rate (`lr`), the decay rates (`betas`), the number of bits of the optimizer state (`optim_bits`), and percentile clipping (`percentile_clipping`) which can increase stability. For example, to initialize a 32-bit [Adam](/docs/bitsandbytes/v0.49.1/en/reference/optim/adam#bitsandbytes.optim.Adam) optimizer with 5th percentile clipping:

```py
import bitsandbytes as bnb

adam = bnb.optim.Adam(model.parameters(), lr=0.001, betas=(0.9, 0.995), optim_bits=32, percentile_clipping=5)
```

## Optimize unstable parameters

To optimize some unstable parameters with 32-bit Adam and others with 8-bit Adam, use the [GlobalOptimManager](/docs/bitsandbytes/v0.49.1/en/reference/optim/optim_overview#bitsandbytes.optim.GlobalOptimManager) class to override the specific hyperparameters for a particular layer. You'll need to:

1. Register the parameters while they're on the CPU.

```py
import torch
import bitsandbytes as bnb

mng = bnb.optim.GlobalOptimManager.get_instance()

model = MyModel()
mng.register_parameters(model.parameters())
```

2. Override the config with the new desired hyperparameters. For example, let's override the `model.fc1.weight` layer to use 32-bit Adam.

> [!TIP]
> Check the optimizer API documentation for more information about other hyperparameters you can override.

```py
model = model.cuda()
# use 8-bit optimizer states for all parameters
adam = bnb.optim.Adam(model.parameters(), lr=0.001, optim_bits=8)

# override the parameter model.fc1.weight now uses 32-bit Adam
mng.override_config(model.fc1.weight, "optim_bits", 32)
```

You can also override multiple layers at once by passing them as a list and the new hyperparameters as a dictionary. For example, let's override the `model.special.weight` and `model.also_special.weight` layers to use sparse optimization and a lower learning and decay rate.

```py
mng.override_config([model.special.weight, model.also_special.weight],
                    key_value_dict ={'is_sparse': True, 'lr': 1e-5, 'betas'=(0.9, 0.98)})
```

For a specific layer, we recommend overriding locally in each module. Pass the module, the parameter, and its attribute name to the [GlobalOptimManager](/docs/bitsandbytes/v0.49.1/en/reference/optim/optim_overview#bitsandbytes.optim.GlobalOptimManager):

```py
class MyModule(torch.nn.Module):
  def __init__(d_in, d_out):
    super(MyModule, self).__init__()
    self.linear = torch.nn.Linear(d_in, d_out)
    # optimization will happen in 32-bit and
    # learning rate will be set to 0.0001 independent of the main learning rate
    config = {'optim_bits': 32, 'lr' : 0.0001}
    GlobalOptimManager.get_instance().register_module_override(self, 'weight', config)

```

## Next steps

For more conceptual details and explanation about 8-bit optimizers, take a look at the [8-bit optimizers](./explanations/optimizers) guide.

### Contribution Guide
https://huggingface.co/docs/bitsandbytes/v0.49.1/contributing.md

# Contribution Guide

## Setup

### Setup pre-commit hooks
- Install pre-commit hooks with `pip install pre-commit`.
- Run `pre-commit install` once to install the hooks, so they will be run on every commit.
- If the hooks introduce changes, they'll be visible with `git diff`. Review them and `git add` them if everything is fine, then re-execute the before commit, it should pass now.
- If you want to manually trigger the hooks, you may do `pre-commit run --all-files`

Now all the pre-commit hooks will be automatically run when you try to commit and if they introduce some changes, you need to re-add the changed files before being able to commit and push.

### Ignore formatting revs
- Run `git config blame.ignoreRevsFile .git-blame-ignore-revs`. This will make it so that `git blame` is aware of commits that were logged to be solely formatting-related.

## Doc-string syntax

We're following NumPy doc-string conventions with the only notable difference being that we use Markdown instead of Rich text format (RTF) for markup within the doc-strings.

Please see the existing documentation to see how to generate autodocs.

## Documentation
- [guideline for documentation syntax](https://github.com/huggingface/doc-builder#readme)
- images shall be uploaded via PR in the `bitsandbytes/` directory [here](https://huggingface.co/datasets/huggingface/documentation-images)
- find the documentation builds for each PR in a link posted to the PR, such as https://moon-ci-docs.huggingface.co/docs/bitsandbytes/pr_1012/en/introduction

### Papers, related resources & how to cite
https://huggingface.co/docs/bitsandbytes/v0.49.1/explanations/resources.md

# Papers, related resources & how to cite

The below academic work is ordered in reverse chronological order.

## [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression (Jun 2023)](https://arxiv.org/abs/2306.03078)

Authors: Tim Dettmers, Ruslan Svirschevski, Vage Egiazarian, Denis Kuznedelev, Elias Frantar, Saleh Ashkboos, Alexander Borzunov, Torsten Hoefler, Dan Alistarh

- [Twitter summary thread](https://twitter.com/Tim_Dettmers/status/1666076553665744896)

```
@article{dettmers2023spqr,
  title={SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression},
  author={Dettmers, Tim and Svirschevski, Ruslan and Egiazarian, Vage and Kuznedelev, Denis and Frantar, Elias and Ashkboos, Saleh and Borzunov, Alexander and Hoefler, Torsten and Alistarh, Dan},
  journal={arXiv preprint arXiv:2306.03078},
  year={2023}
}
```

## [QLoRA: Efficient Finetuning of Quantized LLMs (May 2023)](https://arxiv.org/abs/2305.14314)
Authors: Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, Luke Zettlemoyer

- [Video](https://www.youtube.com/watch?v=y9PHWGOa8HA&ab_channel=LondonMachineLearningMeetup)
- [Twitter summary thread](https://twitter.com/Tim_Dettmers/status/1661379354507476994)

```
@article{dettmers2023qlora,
  title={Qlora: Efficient finetuning of quantized llms},
  author={Dettmers, Tim and Pagnoni, Artidoro and Holtzman, Ari and Zettlemoyer, Luke},
  journal={arXiv preprint arXiv:2305.14314},
  year={2023}
}
```

## [The case for 4-bit precision: k-bit Inference Scaling Laws (Dec 2022)](https://arxiv.org/abs/2212.09720)
Authors: Tim Dettmers, Luke Zettlemoyer

- [Video](https://www.youtube.com/watch?v=odlQa6AE1gY&ab_channel=TheInsideView)
- [Twitter summary thread](https://twitter.com/Tim_Dettmers/status/1605209171758284805)

```
@inproceedings{dettmers2023case,
  title={The case for 4-bit precision: k-bit inference scaling laws},
  author={Dettmers, Tim and Zettlemoyer, Luke},
  booktitle={International Conference on Machine Learning},
  pages={7750--7774},
  year={2023},
  organization={PMLR}
}
```

## [LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale (Nov 2022)](https://arxiv.org/abs/2208.07339) [[llm-int8]]
Authors: Tim Dettmers, Mike Lewis, Younes Belkada, Luke Zettlemoyer

- [LLM.int8() Blog Post](https://huggingface.co/blog/hf-bitsandbytes-integration)
- [LLM.int8() Emergent Features Blog Post](https://timdettmers.com/2022/08/17/llm-int8-and-emergent-features/)
- [Introduction to Weight Quantization](https://towardsdatascience.com/introduction-to-weight-quantization-2494701b9c0c)
- [Poster](https://twitter.com/Tim_Dettmers/status/1598351301942951937)

```
@article{dettmers2022llm,
  title={Llm. int8 (): 8-bit matrix multiplication for transformers at scale},
  author={Dettmers, Tim and Lewis, Mike and Belkada, Younes and Zettlemoyer, Luke},
  journal={arXiv preprint arXiv:2208.07339},
  year={2022}
}
```

## [8-bit Optimizers via Block-wise Quantization (Oct 2021)](https://arxiv.org/abs/2110.02861)
Authors: Tim Dettmers, Mike Lewis, Sam Shleifer, Luke Zettlemoyer

- [Video](https://www.youtube.com/watch?v=IxrlHAJtqKE)
- [Twitter summary thread](https://twitter.com/Tim_Dettmers/status/1446472128979562499)

```
@article{DBLP:journals/corr/abs-2110-02861,
  author       = {Tim Dettmers and
                  Mike Lewis and
                  Sam Shleifer and
                  Luke Zettlemoyer},
  title        = {8-bit Optimizers via Block-wise Quantization},
  journal      = {CoRR},
  volume       = {abs/2110.02861},
  year         = {2021},
  url          = {https://arxiv.org/abs/2110.02861},
  eprinttype    = {arXiv},
  eprint       = {2110.02861},
  timestamp    = {Thu, 21 Oct 2021 16:20:08 +0200},
  biburl       = {https://dblp.org/rec/journals/corr/abs-2110-02861.bib},
  bibsource    = {dblp computer science bibliography, https://dblp.org}
}
```

### 8-bit optimizers
https://huggingface.co/docs/bitsandbytes/v0.49.1/explanations/optimizers.md

# 8-bit optimizers

Stateful optimizers maintain gradient statistics over time, for example, the exponentially smoothed sum (SGD with momentum) or squared sum (Adam) of past gradient values. This state can be used to accelerate optimization compared to plain stochastic gradient descent, but uses memory that might otherwise be allocated to model parameters. As a result, this limits the maximum size of models that can be trained in practice. Now take a look at the biggest models that can be trained with 8-bit optimizers.

    
        
        Depending on your GPU size, you can train a much larger model with a 8-bit optimizer.
    

bitsandbytes optimizers use 8-bit statistics, while maintaining the performance levels of using 32-bit optimizer states.

To overcome the resulting computational, quantization and stability challenges, 8-bit optimizers have three components:

1. Block-wise quantization: divides input tensors into smaller blocks that are independently quantized, isolating outliers and distributing the error more equally over all bits. Each block is processed in parallel across cores, yielding faster optimization and high precision quantization.
2. Dynamic quantization: quantizes both small and large values with high precision.
3. Stable embedding layer: improves stability during optimization for models with word embeddings.

With these components, performing an optimizer update with 8-bit states is straightforward. The 8-bit optimizer states are dequantized to 32-bit before you perform the update, and then the states are quantized back to 8-bit for storage.

The 8-bit to 32-bit conversion happens element-by-element in registers, meaning no slow copies to GPU memory or additional temporary memory are needed to perform quantization and dequantization. For GPUs, this makes 8-bit optimizers much faster than regular 32-bit optimizers.

    
        
        A comparison of memory and time saved using 8-bit and 32-bit optimizers.
    

## Stable embedding layer

The stable embedding layer improves the training stability of the standard word embedding layer for NLP tasks. It addresses the challenge of non-uniform input distributions and mitigates extreme gradient variations. This means the stable embedding layer can support more aggressive quantization strategies without compromising training stability, and it can help achieve stable training outcomes, which is particularly important for models dealing with diverse and complex language data.

There are three features of the stable embedding layer:

- Initialization: utilizes Xavier uniform initialization to maintain consistent variance, reducing the likelihood of large gradients.
- Normalization: incorporates layer normalization before adding positional embeddings, aiding in output stability.
- Optimizer states: employs 32-bit optimizer states exclusively for this layer to enhance stability, while the rest of the model may use standard 16-bit precision.

## Paged optimizers

Paged optimizers are built on top of the [unified memory](https://developer.nvidia.com/blog/unified-memory-cuda-beginners/) feature of CUDA. Unified memory provides a single memory space the GPU and CPU can easily access. While this feature is not supported by PyTorch, it has been added to bitsandbytes.

Paged optimizers works like regular CPU paging, which means that it *only becomes active if you run out of GPU memory*. When that happens, memory is transferred page-by-page from GPU to CPU. The memory is mapped, meaning that pages are pre-allocated on the CPU but they are not updated automatically. Pages are only updated if the memory is accessed or a swapping operation is launched.

The unified memory feature is less efficient than regular asynchronous memory transfers, and you usually won't be able to get full PCIe memory bandwidth utilization. If you do a manual prefetch, transfer speeds can be high but still only about half or worse than the full PCIe memory bandwidth (tested on 16x lanes PCIe 3.0).

This means performance depends highly on the particular use-case. For example, if you evict 1 GB of memory per forward-backward-optimizer loop, then you can expect about 50% of the PCIe bandwidth as time in the best case. So, 1 GB for PCIe 3.0 with 16x lanes would run at 16 GB/s, which is `1/(16*0.5) = 1/8 = 125ms` of overhead per optimizer step. Other overhead can be estimated for the particular use-case given a PCIe interface, lanes, and the memory evicted in each iteration.

Compared to CPU offloading, a paged optimizer has zero overhead if all the memory fits onto the device and only some overhead if some of memory needs to be evicted. For offloading, you usually offload fixed parts of the model and need to off and onload all this memory with each iteration through the model (sometimes twice for both forward and backward pass).

### Overview
https://huggingface.co/docs/bitsandbytes/v0.49.1/reference/functional.md

# Overview
The `bitsandbytes.functional` API provides the low-level building blocks for the library's features.

## When to Use `bitsandbytes.functional`

* When you need direct control over quantized operations and their parameters.
* To build custom layers or operations leveraging low-bit arithmetic.
* To integrate with other ecosystem tooling.
* For experimental or research purposes requiring non-standard quantization or performance optimizations.

## LLM.int8()[[bitsandbytes.functional.int8_linear_matmul]]
#### bitsandbytes.functional.int8_linear_matmul[[bitsandbytes.functional.int8_linear_matmul]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/functional.py#L1744)

Performs an 8-bit integer matrix multiplication.

A linear transformation is applied such that `out = A @ B.T`. When possible, integer tensor core hardware is
utilized to accelerate the operation.

**Parameters:**

A (`torch.Tensor`) : The first matrix operand with the data type `torch.int8`.

B (`torch.Tensor`) : The second matrix operand with the data type `torch.int8`.

out (`torch.Tensor`, *optional*) : A pre-allocated tensor used to store the result.

dtype (`torch.dtype`, *optional*) : The expected data type of the output. Defaults to `torch.int32`.

**Returns:**

``torch.Tensor``

The result of the operation.

#### bitsandbytes.functional.int8_mm_dequant[[bitsandbytes.functional.int8_mm_dequant]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/functional.py#L1770)

Performs dequantization on the result of a quantized int8 matrix multiplication.

**Parameters:**

A (`torch.Tensor` with dtype `torch.int32`) : The result of a quantized int8 matrix multiplication.

row_stats (`torch.Tensor`) : The row-wise quantization statistics for the lhs operand of the matrix multiplication.

col_stats (`torch.Tensor`) : The column-wise quantization statistics for the rhs operand of the matrix multiplication.

out (`torch.Tensor`, *optional*) : A pre-allocated tensor to store the output of the operation.

bias (`torch.Tensor`, *optional*) : An optional bias vector to add to the result.

**Returns:**

``torch.Tensor``

The dequantized result with an optional bias, with dtype `torch.float16`.

#### bitsandbytes.functional.int8_vectorwise_dequant[[bitsandbytes.functional.int8_vectorwise_dequant]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/functional.py#L1930)

Dequantizes a tensor with dtype `torch.int8` to `torch.float32`.

**Parameters:**

A (`torch.Tensor` with dtype `torch.int8`) : The quantized int8 tensor.

stats (`torch.Tensor` with dtype `torch.float32`) : The row-wise quantization statistics.

**Returns:**

``torch.Tensor` with dtype `torch.float32``

The dequantized tensor.

#### bitsandbytes.functional.int8_vectorwise_quant[[bitsandbytes.functional.int8_vectorwise_quant]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/functional.py#L1944)

Quantizes a tensor with dtype `torch.float16` to `torch.int8` in accordance to the `LLM.int8()` algorithm.

For more information, see the [LLM.int8() paper](https://arxiv.org/abs/2208.07339).

**Parameters:**

A (`torch.Tensor` with dtype `torch.float16`) : The input tensor.

threshold (`float`, *optional*) : An optional threshold for sparse decomposition of outlier features.  No outliers are held back when 0.0. Defaults to 0.0.

**Returns:**

``Tuple[torch.Tensor, torch.Tensor, Optional[torch.Tensor]]``

A tuple containing the quantized tensor and relevant statistics.
- `torch.Tensor` with dtype `torch.int8`: The quantized data.
- `torch.Tensor` with dtype `torch.float32`: The quantization scales.
- `torch.Tensor` with dtype `torch.int32`, *optional*: A list of column indices which contain outlier features.

## 4-bit[[bitsandbytes.functional.dequantize_4bit]]
#### bitsandbytes.functional.dequantize_4bit[[bitsandbytes.functional.dequantize_4bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/functional.py#L931)

Dequantizes a packed 4-bit quantized tensor.

The input tensor is dequantized by dividing it into blocks of `blocksize` values.
The the absolute maximum value within these blocks is used for scaling
the non-linear dequantization.

**Parameters:**

A (`torch.Tensor`) : The quantized input tensor.

quant_state (`QuantState`, *optional*) : The quantization state as returned by `quantize_4bit`. Required if `absmax` is not provided.

absmax (`torch.Tensor`, *optional*) : A tensor containing the scaling values. Required if `quant_state` is not provided and ignored otherwise.

out (`torch.Tensor`, *optional*) : A tensor to use to store the result.

blocksize (`int`, *optional*) : The size of the blocks. Defaults to 128 on ROCm and 64 otherwise. Valid values are 64, 128, 256, 512, 1024, 2048, and 4096.

quant_type (`str`, *optional*) : The data type to use: `nf4` or `fp4`. Defaults to `fp4`.

**Returns:**

``torch.Tensor``

The dequantized tensor.

#### bitsandbytes.functional.dequantize_fp4[[bitsandbytes.functional.dequantize_fp4]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/functional.py#L907)

#### bitsandbytes.functional.dequantize_nf4[[bitsandbytes.functional.dequantize_nf4]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/functional.py#L919)

#### bitsandbytes.functional.gemv_4bit[[bitsandbytes.functional.gemv_4bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/functional.py#L1510)

#### bitsandbytes.functional.quantize_4bit[[bitsandbytes.functional.quantize_4bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/functional.py#L826)

Quantize tensor A in blocks of 4-bit values.

Quantizes tensor A by dividing it into blocks which are independently quantized.

**Parameters:**

A (`torch.Tensor`) : The input tensor. Supports `float16`, `bfloat16`, or `float32` datatypes.

absmax (`torch.Tensor`, *optional*) : A tensor to use to store the absmax values.

out (`torch.Tensor`, *optional*) : A tensor to use to store the result.

blocksize (`int`, *optional*) : The size of the blocks. Defaults to 128 on ROCm and 64 otherwise. Valid values are 64, 128, 256, 512, 1024, 2048, and 4096.

compress_statistics (`bool`, *optional*) : Whether to additionally quantize the absmax values. Defaults to False.

quant_type (`str`, *optional*) : The data type to use: `nf4` or `fp4`. Defaults to `fp4`.

quant_storage (`torch.dtype`, *optional*) : The dtype of the tensor used to store the result. Defaults to `torch.uint8`.

**Returns:**

`Tuple[`torch.Tensor`, `QuantState`]`

A tuple containing the quantization results.
- `torch.Tensor`: The quantized tensor with packed 4-bit values.
- `QuantState`: The state object used to undo the quantization.

#### bitsandbytes.functional.quantize_fp4[[bitsandbytes.functional.quantize_fp4]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/functional.py#L800)

#### bitsandbytes.functional.quantize_nf4[[bitsandbytes.functional.quantize_nf4]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/functional.py#L813)

#### bitsandbytes.functional.QuantState[[bitsandbytes.functional.QuantState]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/functional.py#L393)

container for quantization state components to work with Params4bit and similar classes

as_dictbitsandbytes.functional.QuantState.as_dicthttps://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/functional.py#L505[{"name": "packed", "val": " = False"}]

returns dict of tensors and strings to use in serialization via _save_to_state_dict()
param: packed -- returns dict[str, torch.Tensor] for state_dict fit for safetensors saving
#### from_dict[[bitsandbytes.functional.QuantState.from_dict]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/functional.py#L454)

unpacks components of state_dict into QuantState
where necessary, convert into strings, torch.dtype, ints, etc.

qs_dict: based on state_dict, with only relevant keys, striped of prefixes.

item with key `quant_state.bitsandbytes__[nf4/fp4]` may contain minor and non-tensor quant state items.

## Dynamic 8-bit Quantization[[bitsandbytes.functional.dequantize_blockwise]]

Primitives used in the 8-bit optimizer quantization.

For more details see [8-Bit Approximations for Parallelism in Deep Learning](https://arxiv.org/abs/1511.04561)

#### bitsandbytes.functional.dequantize_blockwise[[bitsandbytes.functional.dequantize_blockwise]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/functional.py#L641)

Dequantize a tensor in blocks of values.

The input tensor is dequantized by dividing it into blocks of `blocksize` values.
The the absolute maximum value within these blocks is used for scaling
the non-linear dequantization.

**Parameters:**

A (`torch.Tensor`) : The quantized input tensor.

quant_state (`QuantState`, *optional*) : The quantization state as returned by `quantize_blockwise`. Required if `absmax` is not provided.

absmax (`torch.Tensor`, *optional*) : A tensor containing the scaling values. Required if `quant_state` is not provided and ignored otherwise.

code (`torch.Tensor`, *optional*) : A mapping describing the low-bit data type. Defaults to a signed 8-bit dynamic type. For more details, see  (8-Bit Approximations for Parallelism in Deep Learning)[https://arxiv.org/abs/1511.04561]. Ignored when `quant_state` is provided.

out (`torch.Tensor`, *optional*) : A tensor to use to store the result.

blocksize (`int`, *optional*) : The size of the blocks. Defaults to 4096. Valid values are 64, 128, 256, 512, 1024, 2048, and 4096. Ignored when `quant_state` is provided.

**Returns:**

``torch.Tensor``

The dequantized tensor. The datatype is indicated by `quant_state.dtype` and defaults to `torch.float32`.

#### bitsandbytes.functional.quantize_blockwise[[bitsandbytes.functional.quantize_blockwise]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/functional.py#L570)

Quantize a tensor in blocks of values.

The input tensor is quantized by dividing it into blocks of `blocksize` values.
The the absolute maximum value within these blocks is calculated for scaling
the non-linear quantization.

**Parameters:**

A (`torch.Tensor`) : The input tensor. Supports `float16`, `bfloat16`, or `float32` datatypes.

code (`torch.Tensor`, *optional*) : A mapping describing the low-bit data type. Defaults to a signed 8-bit dynamic type. For more details, see  (8-Bit Approximations for Parallelism in Deep Learning)[https://arxiv.org/abs/1511.04561].

absmax (`torch.Tensor`, *optional*) : A tensor to use to store the absmax values.

out (`torch.Tensor`, *optional*) : A tensor to use to store the result.

blocksize (`int`, *optional*) : The size of the blocks. Defaults to 4096. Valid values are 64, 128, 256, 512, 1024, 2048, and 4096.

nested (`bool`, *optional*) : Whether to additionally quantize the absmax values. Defaults to False.

**Returns:**

``Tuple[torch.Tensor, QuantState]``

A tuple containing the quantization results.
- `torch.Tensor`: The quantized tensor.
- `QuantState`: The state object used to undo the quantization.

## Utility[[bitsandbytes.functional.get_ptr]]
#### bitsandbytes.functional.get_ptr[[bitsandbytes.functional.get_ptr]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/functional.py#L378)

Gets the memory address of the first element of a tenso

**Parameters:**

A (`Optional[Tensor]`) : A PyTorch tensor.

**Returns:**

``Optional[ct.c_void_p]``

A pointer to the underlying tensor data.

### SGD
https://huggingface.co/docs/bitsandbytes/v0.49.1/reference/optim/sgd.md

# SGD

Stochastic gradient descent (SGD) is a basic gradient descent optimizer to minimize loss given a set of model parameters and updates the parameters in the opposite direction of the gradient. The update is performed on a randomly sampled mini-batch of data from the dataset.

bitsandbytes also supports momentum and Nesterov momentum to accelerate SGD by adding a weighted average of past gradients to the current gradient.

## SGD[[api-class]][[bitsandbytes.optim.SGD]]

#### bitsandbytes.optim.SGD[[bitsandbytes.optim.SGD]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/sgd.py#L8)

__init__bitsandbytes.optim.SGD.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/sgd.py#L9[{"name": "params", "val": ""}, {"name": "lr", "val": ""}, {"name": "momentum", "val": " = 0"}, {"name": "dampening", "val": " = 0"}, {"name": "weight_decay", "val": " = 0"}, {"name": "nesterov", "val": " = False"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`) --
  The learning rate.
- **momentum** (`float`, defaults to 0) --
  The momentum value speeds up the optimizer by taking bigger steps.
- **dampening** (`float`, defaults to 0) --
  The dampening value reduces the momentum of the optimizer.
- **weight_decay** (`float`, defaults to 0.0) --
  The weight decay value for the optimizer.
- **nesterov** (`bool`, defaults to `False`) --
  Whether to use Nesterov momentum.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.0

Base SGD optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`) : The learning rate.

momentum (`float`, defaults to 0) : The momentum value speeds up the optimizer by taking bigger steps.

dampening (`float`, defaults to 0) : The dampening value reduces the momentum of the optimizer.

weight_decay (`float`, defaults to 0.0) : The weight decay value for the optimizer.

nesterov (`bool`, defaults to `False`) : Whether to use Nesterov momentum.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

## SGD8bit[[bitsandbytes.optim.SGD8bit]]

#### bitsandbytes.optim.SGD8bit[[bitsandbytes.optim.SGD8bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/sgd.py#L67)

__init__bitsandbytes.optim.SGD8bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/sgd.py#L68[{"name": "params", "val": ""}, {"name": "lr", "val": ""}, {"name": "momentum", "val": " = 0"}, {"name": "dampening", "val": " = 0"}, {"name": "weight_decay", "val": " = 0"}, {"name": "nesterov", "val": " = False"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`) --
  The learning rate.
- **momentum** (`float`, defaults to 0) --
  The momentum value speeds up the optimizer by taking bigger steps.
- **dampening** (`float`, defaults to 0) --
  The dampening value reduces the momentum of the optimizer.
- **weight_decay** (`float`, defaults to 0.0) --
  The weight decay value for the optimizer.
- **nesterov** (`bool`, defaults to `False`) --
  Whether to use Nesterov momentum.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.0

8-bit SGD optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`) : The learning rate.

momentum (`float`, defaults to 0) : The momentum value speeds up the optimizer by taking bigger steps.

dampening (`float`, defaults to 0) : The dampening value reduces the momentum of the optimizer.

weight_decay (`float`, defaults to 0.0) : The weight decay value for the optimizer.

nesterov (`bool`, defaults to `False`) : Whether to use Nesterov momentum.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

## SGD32bit[[bitsandbytes.optim.SGD32bit]]

#### bitsandbytes.optim.SGD32bit[[bitsandbytes.optim.SGD32bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/sgd.py#L123)

__init__bitsandbytes.optim.SGD32bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/sgd.py#L124[{"name": "params", "val": ""}, {"name": "lr", "val": ""}, {"name": "momentum", "val": " = 0"}, {"name": "dampening", "val": " = 0"}, {"name": "weight_decay", "val": " = 0"}, {"name": "nesterov", "val": " = False"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`) --
  The learning rate.
- **momentum** (`float`, defaults to 0) --
  The momentum value speeds up the optimizer by taking bigger steps.
- **dampening** (`float`, defaults to 0) --
  The dampening value reduces the momentum of the optimizer.
- **weight_decay** (`float`, defaults to 0.0) --
  The weight decay value for the optimizer.
- **nesterov** (`bool`, defaults to `False`) --
  Whether to use Nesterov momentum.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.0

32-bit SGD optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`) : The learning rate.

momentum (`float`, defaults to 0) : The momentum value speeds up the optimizer by taking bigger steps.

dampening (`float`, defaults to 0) : The dampening value reduces the momentum of the optimizer.

weight_decay (`float`, defaults to 0.0) : The weight decay value for the optimizer.

nesterov (`bool`, defaults to `False`) : Whether to use Nesterov momentum.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

### Lion
https://huggingface.co/docs/bitsandbytes/v0.49.1/reference/optim/lion.md

# Lion

[Lion (Evolved Sign Momentum)](https://hf.co/papers/2302.06675) is a unique optimizer that uses the sign of the gradient to determine the update direction of the momentum. This makes Lion more memory-efficient and faster than `AdamW` which tracks and store the first and second-order moments.

## Lion[[api-class]][[bitsandbytes.optim.Lion]]

#### bitsandbytes.optim.Lion[[bitsandbytes.optim.Lion]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/lion.py#L8)

__init__bitsandbytes.optim.Lion.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/lion.py#L9[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.0001"}, {"name": "betas", "val": " = (0.9, 0.99)"}, {"name": "weight_decay", "val": " = 0"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}, {"name": "is_paged", "val": " = False"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-4) --
  The learning rate.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **weight_decay** (`float`, defaults to 0) --
  The weight decay value for the optimizer.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.
- **is_paged** (`bool`, defaults to `False`) --
  Whether the optimizer is a paged optimizer or not.0

Base Lion optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-4) : The learning rate.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

weight_decay (`float`, defaults to 0) : The weight decay value for the optimizer.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

is_paged (`bool`, defaults to `False`) : Whether the optimizer is a paged optimizer or not.

## Lion8bit[[bitsandbytes.optim.Lion8bit]]

#### bitsandbytes.optim.Lion8bit[[bitsandbytes.optim.Lion8bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/lion.py#L63)

__init__bitsandbytes.optim.Lion8bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/lion.py#L64[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.0001"}, {"name": "betas", "val": " = (0.9, 0.99)"}, {"name": "weight_decay", "val": " = 0"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}, {"name": "is_paged", "val": " = False"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-4) --
  The learning rate.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **weight_decay** (`float`, defaults to 0) --
  The weight decay value for the optimizer.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.
- **is_paged** (`bool`, defaults to `False`) --
  Whether the optimizer is a paged optimizer or not.0

8-bit Lion optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-4) : The learning rate.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

weight_decay (`float`, defaults to 0) : The weight decay value for the optimizer.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

is_paged (`bool`, defaults to `False`) : Whether the optimizer is a paged optimizer or not.

## Lion32bit[[bitsandbytes.optim.Lion32bit]]

#### bitsandbytes.optim.Lion32bit[[bitsandbytes.optim.Lion32bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/lion.py#L115)

__init__bitsandbytes.optim.Lion32bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/lion.py#L116[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.0001"}, {"name": "betas", "val": " = (0.9, 0.99)"}, {"name": "weight_decay", "val": " = 0"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}, {"name": "is_paged", "val": " = False"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-4) --
  The learning rate.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **weight_decay** (`float`, defaults to 0) --
  The weight decay value for the optimizer.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.
- **is_paged** (`bool`, defaults to `False`) --
  Whether the optimizer is a paged optimizer or not.0

32-bit Lion optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-4) : The learning rate.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

weight_decay (`float`, defaults to 0) : The weight decay value for the optimizer.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

is_paged (`bool`, defaults to `False`) : Whether the optimizer is a paged optimizer or not.

## PagedLion[[bitsandbytes.optim.PagedLion]]

#### bitsandbytes.optim.PagedLion[[bitsandbytes.optim.PagedLion]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/lion.py#L167)

__init__bitsandbytes.optim.PagedLion.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/lion.py#L168[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.0001"}, {"name": "betas", "val": " = (0.9, 0.99)"}, {"name": "weight_decay", "val": " = 0"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-4) --
  The learning rate.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **weight_decay** (`float`, defaults to 0) --
  The weight decay value for the optimizer.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.0

Paged Lion optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-4) : The learning rate.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

weight_decay (`float`, defaults to 0) : The weight decay value for the optimizer.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

## PagedLion8bit[[bitsandbytes.optim.PagedLion8bit]]

#### bitsandbytes.optim.PagedLion8bit[[bitsandbytes.optim.PagedLion8bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/lion.py#L219)

__init__bitsandbytes.optim.PagedLion8bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/lion.py#L220[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.0001"}, {"name": "betas", "val": " = (0.9, 0.99)"}, {"name": "weight_decay", "val": " = 0"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-4) --
  The learning rate.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **weight_decay** (`float`, defaults to 0) --
  The weight decay value for the optimizer.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.0

Paged 8-bit Lion optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-4) : The learning rate.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

weight_decay (`float`, defaults to 0) : The weight decay value for the optimizer.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

## PagedLion32bit[[bitsandbytes.optim.PagedLion32bit]]

#### bitsandbytes.optim.PagedLion32bit[[bitsandbytes.optim.PagedLion32bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/lion.py#L270)

__init__bitsandbytes.optim.PagedLion32bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/lion.py#L271[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.0001"}, {"name": "betas", "val": " = (0.9, 0.99)"}, {"name": "weight_decay", "val": " = 0"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-4) --
  The learning rate.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **weight_decay** (`float`, defaults to 0) --
  The weight decay value for the optimizer.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.0

Paged 32-bit Lion optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-4) : The learning rate.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

weight_decay (`float`, defaults to 0) : The weight decay value for the optimizer.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

### RMSprop
https://huggingface.co/docs/bitsandbytes/v0.49.1/reference/optim/rmsprop.md

# RMSprop

RMSprop is an adaptive learning rate optimizer that is very similar to `Adagrad`. RMSprop stores a *weighted average* of the squared past gradients for each parameter and uses it to scale their learning rate. This allows the learning rate to be automatically lower or higher depending on the magnitude of the gradient, and it prevents the learning rate from diminishing.

## RMSprop[[api-class]][[bitsandbytes.optim.RMSprop]]

#### bitsandbytes.optim.RMSprop[[bitsandbytes.optim.RMSprop]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/rmsprop.py#L8)

## RMSprop8bit[[bitsandbytes.optim.RMSprop8bit]]

#### bitsandbytes.optim.RMSprop8bit[[bitsandbytes.optim.RMSprop8bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/rmsprop.py#L72)

## RMSprop32bit[[bitsandbytes.optim.RMSprop32bit]]

#### bitsandbytes.optim.RMSprop32bit[[bitsandbytes.optim.RMSprop32bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/rmsprop.py#L135)

### AdamW
https://huggingface.co/docs/bitsandbytes/v0.49.1/reference/optim/adamw.md

# AdamW

[AdamW](https://hf.co/papers/1711.05101) is a variant of the `Adam` optimizer that separates weight decay from the gradient update based on the observation that the weight decay formulation is different when applied to `SGD` and `Adam`.

bitsandbytes also supports paged optimizers which take advantage of CUDAs unified memory to transfer memory from the GPU to the CPU when GPU memory is exhausted.

## AdamW[[api-class]][[bitsandbytes.optim.AdamW]]

#### bitsandbytes.optim.AdamW[[bitsandbytes.optim.AdamW]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adamw.py#L9)

__init__bitsandbytes.optim.AdamW.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adamw.py#L10[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "betas", "val": " = (0.9, 0.999)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0.01"}, {"name": "amsgrad", "val": " = False"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}, {"name": "is_paged", "val": " = False"}]- **params** (`torch.Tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value prevents division by zero in the optimizer.
- **weight_decay** (`float`, defaults to 1e-2) --
  The weight decay value for the optimizer.
- **amsgrad** (`bool`, defaults to `False`) --
  Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.
- **is_paged** (`bool`, defaults to `False`) --
  Whether the optimizer is a paged optimizer or not.0

Base AdamW optimizer.

**Parameters:**

params (`torch.Tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value prevents division by zero in the optimizer.

weight_decay (`float`, defaults to 1e-2) : The weight decay value for the optimizer.

amsgrad (`bool`, defaults to `False`) : Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

is_paged (`bool`, defaults to `False`) : Whether the optimizer is a paged optimizer or not.

## AdamW8bit[[bitsandbytes.optim.AdamW8bit]]

#### bitsandbytes.optim.AdamW8bit[[bitsandbytes.optim.AdamW8bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adamw.py#L70)

__init__bitsandbytes.optim.AdamW8bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adamw.py#L71[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "betas", "val": " = (0.9, 0.999)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0.01"}, {"name": "amsgrad", "val": " = False"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}, {"name": "is_paged", "val": " = False"}]- **params** (`torch.Tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value prevents division by zero in the optimizer.
- **weight_decay** (`float`, defaults to 1e-2) --
  The weight decay value for the optimizer.
- **amsgrad** (`bool`, defaults to `False`) --
  Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.
  Note: This parameter is not supported in AdamW8bit and must be False.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
  Note: This parameter is not used in AdamW8bit as it always uses 8-bit optimization.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.
- **is_paged** (`bool`, defaults to `False`) --
  Whether the optimizer is a paged optimizer or not.0

8-bit AdamW optimizer.

**Parameters:**

params (`torch.Tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value prevents division by zero in the optimizer.

weight_decay (`float`, defaults to 1e-2) : The weight decay value for the optimizer.

amsgrad (`bool`, defaults to `False`) : Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead. Note: This parameter is not supported in AdamW8bit and must be False.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state. Note: This parameter is not used in AdamW8bit as it always uses 8-bit optimization.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

is_paged (`bool`, defaults to `False`) : Whether the optimizer is a paged optimizer or not.

## AdamW32bit[[bitsandbytes.optim.AdamW32bit]]

#### bitsandbytes.optim.AdamW32bit[[bitsandbytes.optim.AdamW32bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adamw.py#L142)

__init__bitsandbytes.optim.AdamW32bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adamw.py#L143[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "betas", "val": " = (0.9, 0.999)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0.01"}, {"name": "amsgrad", "val": " = False"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}, {"name": "is_paged", "val": " = False"}]- **params** (`torch.Tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value prevents division by zero in the optimizer.
- **weight_decay** (`float`, defaults to 1e-2) --
  The weight decay value for the optimizer.
- **amsgrad** (`bool`, defaults to `False`) --
  Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.
- **is_paged** (`bool`, defaults to `False`) --
  Whether the optimizer is a paged optimizer or not.0

32-bit AdamW optimizer.

**Parameters:**

params (`torch.Tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value prevents division by zero in the optimizer.

weight_decay (`float`, defaults to 1e-2) : The weight decay value for the optimizer.

amsgrad (`bool`, defaults to `False`) : Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

is_paged (`bool`, defaults to `False`) : Whether the optimizer is a paged optimizer or not.

## PagedAdamW[[bitsandbytes.optim.PagedAdamW]]

#### bitsandbytes.optim.PagedAdamW[[bitsandbytes.optim.PagedAdamW]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adamw.py#L203)

__init__bitsandbytes.optim.PagedAdamW.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adamw.py#L204[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "betas", "val": " = (0.9, 0.999)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0.01"}, {"name": "amsgrad", "val": " = False"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}]- **params** (`torch.Tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value prevents division by zero in the optimizer.
- **weight_decay** (`float`, defaults to 1e-2) --
  The weight decay value for the optimizer.
- **amsgrad** (`bool`, defaults to `False`) --
  Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.0

Paged AdamW optimizer.

**Parameters:**

params (`torch.Tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value prevents division by zero in the optimizer.

weight_decay (`float`, defaults to 1e-2) : The weight decay value for the optimizer.

amsgrad (`bool`, defaults to `False`) : Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

## PagedAdamW8bit[[bitsandbytes.optim.PagedAdamW8bit]]

#### bitsandbytes.optim.PagedAdamW8bit[[bitsandbytes.optim.PagedAdamW8bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adamw.py#L261)

__init__bitsandbytes.optim.PagedAdamW8bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adamw.py#L262[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "betas", "val": " = (0.9, 0.999)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0.01"}, {"name": "amsgrad", "val": " = False"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}]- **params** (`torch.Tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value prevents division by zero in the optimizer.
- **weight_decay** (`float`, defaults to 1e-2) --
  The weight decay value for the optimizer.
- **amsgrad** (`bool`, defaults to `False`) --
  Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.
  Note: This parameter is not supported in PagedAdamW8bit and must be False.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
  Note: This parameter is not used in PagedAdamW8bit as it always uses 8-bit optimization.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.0

Paged 8-bit AdamW optimizer.

**Parameters:**

params (`torch.Tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value prevents division by zero in the optimizer.

weight_decay (`float`, defaults to 1e-2) : The weight decay value for the optimizer.

amsgrad (`bool`, defaults to `False`) : Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead. Note: This parameter is not supported in PagedAdamW8bit and must be False.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state. Note: This parameter is not used in PagedAdamW8bit as it always uses 8-bit optimization.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

## PagedAdamW32bit[[bitsandbytes.optim.PagedAdamW32bit]]

#### bitsandbytes.optim.PagedAdamW32bit[[bitsandbytes.optim.PagedAdamW32bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adamw.py#L330)

__init__bitsandbytes.optim.PagedAdamW32bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adamw.py#L331[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "betas", "val": " = (0.9, 0.999)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0.01"}, {"name": "amsgrad", "val": " = False"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}]- **params** (`torch.Tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value prevents division by zero in the optimizer.
- **weight_decay** (`float`, defaults to 1e-2) --
  The weight decay value for the optimizer.
- **amsgrad** (`bool`, defaults to `False`) --
  Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.0

Paged 32-bit AdamW optimizer.

**Parameters:**

params (`torch.Tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value prevents division by zero in the optimizer.

weight_decay (`float`, defaults to 1e-2) : The weight decay value for the optimizer.

amsgrad (`bool`, defaults to `False`) : Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

### LAMB
https://huggingface.co/docs/bitsandbytes/v0.49.1/reference/optim/lamb.md

# LAMB

[LAMB (Layerwise adaptive large batch optimization)](https://hf.co/papers/1904.00962) is an adaptive optimizer designed for training with large batch sizes to accelerate training, combining ideas from `LARS` and `Adam` to automatically scale the learning rate for each layer:

- calculates a *trust ratio* between the weight and gradient norm in a layer and clips the ratio to prevent overly large or small updates
- updates weights with the first and second-moments

## LAMB[[api-class]][[bitsandbytes.optim.LAMB]]

#### bitsandbytes.optim.LAMB[[bitsandbytes.optim.LAMB]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/lamb.py#L8)

__init__bitsandbytes.optim.LAMB.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/lamb.py#L9[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "bias_correction", "val": " = True"}, {"name": "betas", "val": " = (0.9, 0.999)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0"}, {"name": "amsgrad", "val": " = False"}, {"name": "adam_w_mode", "val": " = True"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = False"}, {"name": "max_unorm", "val": " = 1.0"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **bias_correction** (`bool`, defaults to `True`) --
  Whether to apply bias correction to the first and second-order moments.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value prevents division by zero in the optimizer.
- **weight_decay** (`float`, defaults to 1e-2) --
  The weight decay value for the optimizer.
- **amsgrad** (`bool`, defaults to `False`) --
  Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.
- **adam_w_mode** (`bool`, defaults to `True`) --
  Whether to use the AdamW variant.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.
- **max_unorm** (`float`, defaults to 1.0) --
  The maximum gradient norm.0

Base LAMB optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

bias_correction (`bool`, defaults to `True`) : Whether to apply bias correction to the first and second-order moments.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value prevents division by zero in the optimizer.

weight_decay (`float`, defaults to 1e-2) : The weight decay value for the optimizer.

amsgrad (`bool`, defaults to `False`) : Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.

adam_w_mode (`bool`, defaults to `True`) : Whether to use the AdamW variant.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

max_unorm (`float`, defaults to 1.0) : The maximum gradient norm.

## LAMB8bit[[bitsandbytes.optim.LAMB8bit]]

#### bitsandbytes.optim.LAMB8bit[[bitsandbytes.optim.LAMB8bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/lamb.py#L75)

__init__bitsandbytes.optim.LAMB8bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/lamb.py#L76[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "bias_correction", "val": " = True"}, {"name": "betas", "val": " = (0.9, 0.999)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0"}, {"name": "amsgrad", "val": " = False"}, {"name": "adam_w_mode", "val": " = True"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = False"}, {"name": "max_unorm", "val": " = 1.0"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **bias_correction** (`bool`, defaults to `True`) --
  Whether to apply bias correction to the first and second-order moments.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value prevents division by zero in the optimizer.
- **weight_decay** (`float`, defaults to 1e-2) --
  The weight decay value for the optimizer.
- **amsgrad** (`bool`, defaults to `False`) --
  Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.
- **adam_w_mode** (`bool`, defaults to `True`) --
  Whether to use the AdamW variant.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.
- **max_unorm** (`float`, defaults to 1.0) --
  The maximum gradient norm.0

8-bit LAMB optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

bias_correction (`bool`, defaults to `True`) : Whether to apply bias correction to the first and second-order moments.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value prevents division by zero in the optimizer.

weight_decay (`float`, defaults to 1e-2) : The weight decay value for the optimizer.

amsgrad (`bool`, defaults to `False`) : Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.

adam_w_mode (`bool`, defaults to `True`) : Whether to use the AdamW variant.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

max_unorm (`float`, defaults to 1.0) : The maximum gradient norm.

## LAMB32bit[[bitsandbytes.optim.LAMB32bit]]

#### bitsandbytes.optim.LAMB32bit[[bitsandbytes.optim.LAMB32bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/lamb.py#L139)

__init__bitsandbytes.optim.LAMB32bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/lamb.py#L140[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "bias_correction", "val": " = True"}, {"name": "betas", "val": " = (0.9, 0.999)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0"}, {"name": "amsgrad", "val": " = False"}, {"name": "adam_w_mode", "val": " = True"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = False"}, {"name": "max_unorm", "val": " = 1.0"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **bias_correction** (`bool`, defaults to `True`) --
  Whether to apply bias correction to the first and second-order moments.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value prevents division by zero in the optimizer.
- **weight_decay** (`float`, defaults to 1e-2) --
  The weight decay value for the optimizer.
- **amsgrad** (`bool`, defaults to `False`) --
  Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.
- **adam_w_mode** (`bool`, defaults to `True`) --
  Whether to use the AdamW variant.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.
- **max_unorm** (`float`, defaults to 1.0) --
  The maximum gradient norm.0

32-bit LAMB optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

bias_correction (`bool`, defaults to `True`) : Whether to apply bias correction to the first and second-order moments.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value prevents division by zero in the optimizer.

weight_decay (`float`, defaults to 1e-2) : The weight decay value for the optimizer.

amsgrad (`bool`, defaults to `False`) : Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.

adam_w_mode (`bool`, defaults to `True`) : Whether to use the AdamW variant.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

max_unorm (`float`, defaults to 1.0) : The maximum gradient norm.

### LARS
https://huggingface.co/docs/bitsandbytes/v0.49.1/reference/optim/lars.md

# LARS

[LARS (Layer-wise Adaptive Rate Scaling)](https:/hf.co/papers/1708.03888) is an optimizer designed for training with large batch sizes to accelerate training. LARS uses a separate learning rate for each *layer* instead of each parameter. The learning rate is calculated from a *trust ratio* between the weight and gradient norm in a layer. This helps calibrate a stable update size.

## LARS[[api-class]][[bitsandbytes.optim.LARS]]

#### bitsandbytes.optim.LARS[[bitsandbytes.optim.LARS]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/lars.py#L11)

__init__bitsandbytes.optim.LARS.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/lars.py#L12[{"name": "params", "val": ""}, {"name": "lr", "val": ""}, {"name": "momentum", "val": " = 0"}, {"name": "dampening", "val": " = 0"}, {"name": "weight_decay", "val": " = 0"}, {"name": "nesterov", "val": " = False"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "max_unorm", "val": " = 0.02"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`) --
  The learning rate.
- **momentum** (`float`, defaults to 0) --
  The momentum value speeds up the optimizer by taking bigger steps.
- **dampening** (`float`, defaults to 0) --
  The dampening value reduces the momentum of the optimizer.
- **weight_decay** (`float`, defaults to 1e-2) --
  The weight decay value for the optimizer.
- **nesterov** (`bool`, defaults to `False`) --
  Whether to use Nesterov momentum.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **max_unorm** (`float`, defaults to 0.02) --
  The maximum gradient norm.0

Base LARS optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`) : The learning rate.

momentum (`float`, defaults to 0) : The momentum value speeds up the optimizer by taking bigger steps.

dampening (`float`, defaults to 0) : The dampening value reduces the momentum of the optimizer.

weight_decay (`float`, defaults to 1e-2) : The weight decay value for the optimizer.

nesterov (`bool`, defaults to `False`) : Whether to use Nesterov momentum.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

max_unorm (`float`, defaults to 0.02) : The maximum gradient norm.

## LARS8bit[[bitsandbytes.optim.LARS8bit]]

#### bitsandbytes.optim.LARS8bit[[bitsandbytes.optim.LARS8bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/lars.py#L71)

__init__bitsandbytes.optim.LARS8bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/lars.py#L72[{"name": "params", "val": ""}, {"name": "lr", "val": ""}, {"name": "momentum", "val": " = 0"}, {"name": "dampening", "val": " = 0"}, {"name": "weight_decay", "val": " = 0"}, {"name": "nesterov", "val": " = False"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "max_unorm", "val": " = 0.02"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`) --
  The learning rate.
- **momentum** (`float`, defaults to 0) --
  The momentum value speeds up the optimizer by taking bigger steps.
- **dampening** (`float`, defaults to 0) --
  The dampening value reduces the momentum of the optimizer.
- **weight_decay** (`float`, defaults to 1e-2) --
  The weight decay value for the optimizer.
- **nesterov** (`bool`, defaults to `False`) --
  Whether to use Nesterov momentum.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **max_unorm** (`float`, defaults to 0.02) --
  The maximum gradient norm.0

8-bit LARS optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`) : The learning rate.

momentum (`float`, defaults to 0) : The momentum value speeds up the optimizer by taking bigger steps.

dampening (`float`, defaults to 0) : The dampening value reduces the momentum of the optimizer.

weight_decay (`float`, defaults to 1e-2) : The weight decay value for the optimizer.

nesterov (`bool`, defaults to `False`) : Whether to use Nesterov momentum.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

max_unorm (`float`, defaults to 0.02) : The maximum gradient norm.

## LARS32bit[[bitsandbytes.optim.LARS32bit]]

#### bitsandbytes.optim.LARS32bit[[bitsandbytes.optim.LARS32bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/lars.py#L128)

__init__bitsandbytes.optim.LARS32bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/lars.py#L129[{"name": "params", "val": ""}, {"name": "lr", "val": ""}, {"name": "momentum", "val": " = 0"}, {"name": "dampening", "val": " = 0"}, {"name": "weight_decay", "val": " = 0"}, {"name": "nesterov", "val": " = False"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "max_unorm", "val": " = 0.02"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`) --
  The learning rate.
- **momentum** (`float`, defaults to 0) --
  The momentum value speeds up the optimizer by taking bigger steps.
- **dampening** (`float`, defaults to 0) --
  The dampening value reduces the momentum of the optimizer.
- **weight_decay** (`float`, defaults to 1e-2) --
  The weight decay value for the optimizer.
- **nesterov** (`bool`, defaults to `False`) --
  Whether to use Nesterov momentum.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **max_unorm** (`float`, defaults to 0.02) --
  The maximum gradient norm.0

32-bit LARS optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`) : The learning rate.

momentum (`float`, defaults to 0) : The momentum value speeds up the optimizer by taking bigger steps.

dampening (`float`, defaults to 0) : The dampening value reduces the momentum of the optimizer.

weight_decay (`float`, defaults to 1e-2) : The weight decay value for the optimizer.

nesterov (`bool`, defaults to `False`) : Whether to use Nesterov momentum.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

max_unorm (`float`, defaults to 0.02) : The maximum gradient norm.

### AdEMAMix
https://huggingface.co/docs/bitsandbytes/v0.49.1/reference/optim/ademamix.md

# AdEMAMix

[AdEMAMix](https://hf.co/papers/2409.03137) is a variant of the `Adam` optimizer.

bitsandbytes also supports paged optimizers which take advantage of CUDAs unified memory to transfer memory from the GPU to the CPU when GPU memory is exhausted.

## AdEMAMix[[api-class]][[bitsandbytes.optim.AdEMAMix]]

#### bitsandbytes.optim.AdEMAMix[[bitsandbytes.optim.AdEMAMix]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/ademamix.py#L107)

__init__bitsandbytes.optim.AdEMAMix.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/ademamix.py#L108[{"name": "params", "val": ": Iterable"}, {"name": "lr", "val": ": float = 0.001"}, {"name": "betas", "val": ": tuple = (0.9, 0.999, 0.9999)"}, {"name": "alpha", "val": ": float = 5.0"}, {"name": "t_alpha", "val": ": typing.Optional[int] = None"}, {"name": "t_beta3", "val": ": typing.Optional[int] = None"}, {"name": "eps", "val": ": float = 1e-08"}, {"name": "weight_decay", "val": ": float = 0.01"}, {"name": "optim_bits", "val": ": typing.Literal[8, 32] = 32"}, {"name": "min_8bit_size", "val": ": int = 4096"}, {"name": "is_paged", "val": ": bool = False"}]

## AdEMAMix8bit[[bitsandbytes.optim.AdEMAMix8bit]]

#### bitsandbytes.optim.AdEMAMix8bit[[bitsandbytes.optim.AdEMAMix8bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/ademamix.py#L274)

__init__bitsandbytes.optim.AdEMAMix8bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/ademamix.py#L275[{"name": "params", "val": ": Iterable"}, {"name": "lr", "val": ": float = 0.001"}, {"name": "betas", "val": ": tuple = (0.9, 0.999, 0.9999)"}, {"name": "alpha", "val": ": float = 5.0"}, {"name": "t_alpha", "val": ": typing.Optional[int] = None"}, {"name": "t_beta3", "val": ": typing.Optional[int] = None"}, {"name": "eps", "val": ": float = 1e-08"}, {"name": "weight_decay", "val": ": float = 0.01"}, {"name": "min_8bit_size", "val": ": int = 4096"}, {"name": "is_paged", "val": ": bool = False"}]

## AdEMAMix32bit[[bitsandbytes.optim.AdEMAMix32bit]]

#### bitsandbytes.optim.AdEMAMix32bit[[bitsandbytes.optim.AdEMAMix32bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/ademamix.py#L359)

__init__bitsandbytes.optim.AdEMAMix32bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/ademamix.py#L360[{"name": "params", "val": ": Iterable"}, {"name": "lr", "val": ": float = 0.001"}, {"name": "betas", "val": ": tuple = (0.9, 0.999, 0.9999)"}, {"name": "alpha", "val": ": float = 5.0"}, {"name": "t_alpha", "val": ": typing.Optional[int] = None"}, {"name": "t_beta3", "val": ": typing.Optional[int] = None"}, {"name": "eps", "val": ": float = 1e-08"}, {"name": "weight_decay", "val": ": float = 0.01"}, {"name": "min_8bit_size", "val": ": int = 4096"}, {"name": "is_paged", "val": ": bool = False"}]

## PagedAdEMAMix[[bitsandbytes.optim.PagedAdEMAMix]]

#### bitsandbytes.optim.PagedAdEMAMix[[bitsandbytes.optim.PagedAdEMAMix]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/ademamix.py#L330)

__init__bitsandbytes.optim.PagedAdEMAMix.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/ademamix.py#L331[{"name": "params", "val": ": Iterable"}, {"name": "lr", "val": ": float = 0.001"}, {"name": "betas", "val": ": tuple = (0.9, 0.999, 0.9999)"}, {"name": "alpha", "val": ": float = 5.0"}, {"name": "t_alpha", "val": ": typing.Optional[int] = None"}, {"name": "t_beta3", "val": ": typing.Optional[int] = None"}, {"name": "eps", "val": ": float = 1e-08"}, {"name": "weight_decay", "val": ": float = 0.01"}, {"name": "optim_bits", "val": ": typing.Literal[8, 32] = 32"}, {"name": "min_8bit_size", "val": ": int = 4096"}]

## PagedAdEMAMix8bit[[bitsandbytes.optim.PagedAdEMAMix8bit]]

#### bitsandbytes.optim.PagedAdEMAMix8bit[[bitsandbytes.optim.PagedAdEMAMix8bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/ademamix.py#L303)

__init__bitsandbytes.optim.PagedAdEMAMix8bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/ademamix.py#L304[{"name": "params", "val": ": Iterable"}, {"name": "lr", "val": ": float = 0.001"}, {"name": "betas", "val": ": tuple = (0.9, 0.999, 0.9999)"}, {"name": "alpha", "val": ": float = 5.0"}, {"name": "t_alpha", "val": ": typing.Optional[int] = None"}, {"name": "t_beta3", "val": ": typing.Optional[int] = None"}, {"name": "eps", "val": ": float = 1e-08"}, {"name": "weight_decay", "val": ": float = 0.01"}, {"name": "min_8bit_size", "val": ": int = 4096"}]

## PagedAdEMAMix32bit[[bitsandbytes.optim.PagedAdEMAMix32bit]]

#### bitsandbytes.optim.PagedAdEMAMix32bit[[bitsandbytes.optim.PagedAdEMAMix32bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/ademamix.py#L392)

__init__bitsandbytes.optim.PagedAdEMAMix32bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/ademamix.py#L393[{"name": "params", "val": ": Iterable"}, {"name": "lr", "val": ": float = 0.001"}, {"name": "betas", "val": ": tuple = (0.9, 0.999, 0.9999)"}, {"name": "alpha", "val": ": float = 5.0"}, {"name": "t_alpha", "val": ": typing.Optional[int] = None"}, {"name": "t_beta3", "val": ": typing.Optional[int] = None"}, {"name": "eps", "val": ": float = 1e-08"}, {"name": "weight_decay", "val": ": float = 0.01"}, {"name": "min_8bit_size", "val": ": int = 4096"}]

### Overview
https://huggingface.co/docs/bitsandbytes/v0.49.1/reference/optim/optim_overview.md

# Overview

[8-bit optimizers](https://hf.co/papers/2110.02861) reduce the memory footprint of 32-bit optimizers without any performance degradation which means you can train large models with many parameters faster. At the core of 8-bit optimizers is block-wise quantization which enables quantization accuracy, computational efficiency, and stability.

bitsandbytes provides 8-bit optimizers through the base `Optimizer8bit` class, and additionally provides `Optimizer2State` and `Optimizer1State` for 2-state (for example, `Adam`) and 1-state (for example, `Adagrad`) optimizers respectively. To provide custom optimizer hyperparameters, use the `GlobalOptimManager` class to configure the optimizer.

## Optimizer8bit[[bitsandbytes.optim.optimizer.Optimizer8bit]]

#### bitsandbytes.optim.optimizer.Optimizer8bit[[bitsandbytes.optim.optimizer.Optimizer8bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/optimizer.py#L113)

__init__bitsandbytes.optim.optimizer.Optimizer8bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/optimizer.py#L114[{"name": "params", "val": ""}, {"name": "defaults", "val": ""}, {"name": "optim_bits", "val": " = 32"}, {"name": "is_paged", "val": " = False"}]- **params** (`torch.Tensor`) --
  The input parameters to optimize.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
- **is_paged** (`bool`, defaults to `False`) --
  Whether the optimizer is a paged optimizer or not.0

Base 8-bit optimizer class.

**Parameters:**

params (`torch.Tensor`) : The input parameters to optimize.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

is_paged (`bool`, defaults to `False`) : Whether the optimizer is a paged optimizer or not.

## Optimizer2State[[bitsandbytes.optim.optimizer.Optimizer2State]]

#### bitsandbytes.optim.optimizer.Optimizer2State[[bitsandbytes.optim.optimizer.Optimizer2State]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/optimizer.py#L347)

__init__bitsandbytes.optim.optimizer.Optimizer2State.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/optimizer.py#L348[{"name": "optimizer_name", "val": ""}, {"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "betas", "val": " = (0.9, 0.999)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0.0"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}, {"name": "max_unorm", "val": " = 0.0"}, {"name": "skip_zeros", "val": " = False"}, {"name": "is_paged", "val": " = False"}, {"name": "alpha", "val": " = 0.0"}, {"name": "t_alpha", "val": ": typing.Optional[int] = None"}, {"name": "t_beta3", "val": ": typing.Optional[int] = None"}]- **optimizer_name** (`str`) --
  The name of the optimizer.
- **params** (`torch.Tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **betas** (`tuple`, defaults to (0.9, 0.999)) --
  The beta values for the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value for the optimizer.
- **weight_decay** (`float`, defaults to 0.0) --
  The weight decay value for the optimizer.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.
- **max_unorm** (`float`, defaults to 0.0) --
  The maximum value to normalize each block with.
- **skip_zeros** (`bool`, defaults to `False`) --
  Whether to skip zero values for sparse gradients and models to ensure correct updates.
- **is_paged** (`bool`, defaults to `False`) --
  Whether the optimizer is a paged optimizer or not.
- **alpha** (`float`, defaults to 0.0) --
  The alpha value for the AdEMAMix optimizer.
- **t_alpha** (`Optional[int]`, defaults to `None`) --
  Number of iterations for alpha scheduling with AdEMAMix.
- **t_beta3** (`Optional[int]`, defaults to `None`) --
  Number of iterations for beta scheduling with AdEMAMix.0

Base 2-state update optimizer class.

**Parameters:**

optimizer_name (`str`) : The name of the optimizer.

params (`torch.Tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

betas (`tuple`, defaults to (0.9, 0.999)) : The beta values for the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value for the optimizer.

weight_decay (`float`, defaults to 0.0) : The weight decay value for the optimizer.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

max_unorm (`float`, defaults to 0.0) : The maximum value to normalize each block with.

skip_zeros (`bool`, defaults to `False`) : Whether to skip zero values for sparse gradients and models to ensure correct updates.

is_paged (`bool`, defaults to `False`) : Whether the optimizer is a paged optimizer or not.

alpha (`float`, defaults to 0.0) : The alpha value for the AdEMAMix optimizer.

t_alpha (`Optional[int]`, defaults to `None`) : Number of iterations for alpha scheduling with AdEMAMix.

t_beta3 (`Optional[int]`, defaults to `None`) : Number of iterations for beta scheduling with AdEMAMix.

## Optimizer1State[[bitsandbytes.optim.optimizer.Optimizer1State]]

#### bitsandbytes.optim.optimizer.Optimizer1State[[bitsandbytes.optim.optimizer.Optimizer1State]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/optimizer.py#L591)

__init__bitsandbytes.optim.optimizer.Optimizer1State.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/optimizer.py#L592[{"name": "optimizer_name", "val": ""}, {"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "betas", "val": " = (0.9, 0.0)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0.0"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}, {"name": "max_unorm", "val": " = 0.0"}, {"name": "skip_zeros", "val": " = False"}, {"name": "is_paged", "val": " = False"}]- **optimizer_name** (`str`) --
  The name of the optimizer.
- **params** (`torch.Tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **betas** (`tuple`, defaults to (0.9, 0.0)) --
  The beta values for the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value for the optimizer.
- **weight_decay** (`float`, defaults to 0.0) --
  The weight decay value for the optimizer.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.
- **max_unorm** (`float`, defaults to 0.0) --
  The maximum value to normalize each block with.
- **skip_zeros** (`bool`, defaults to `False`) --
  Whether to skip zero values for sparse gradients and models to ensure correct updates.
- **is_paged** (`bool`, defaults to `False`) --
  Whether the optimizer is a paged optimizer or not.0

Base 1-state update optimizer class.

**Parameters:**

optimizer_name (`str`) : The name of the optimizer.

params (`torch.Tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

betas (`tuple`, defaults to (0.9, 0.0)) : The beta values for the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value for the optimizer.

weight_decay (`float`, defaults to 0.0) : The weight decay value for the optimizer.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

max_unorm (`float`, defaults to 0.0) : The maximum value to normalize each block with.

skip_zeros (`bool`, defaults to `False`) : Whether to skip zero values for sparse gradients and models to ensure correct updates.

is_paged (`bool`, defaults to `False`) : Whether the optimizer is a paged optimizer or not.

## Utilities[[bitsandbytes.optim.GlobalOptimManager]]

#### bitsandbytes.optim.GlobalOptimManager[[bitsandbytes.optim.GlobalOptimManager]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/optimizer.py#L22)

A global optimizer manager for enabling custom optimizer configs.

override_configbitsandbytes.optim.GlobalOptimManager.override_confighttps://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/optimizer.py#L56[{"name": "parameters", "val": ""}, {"name": "key", "val": " = None"}, {"name": "value", "val": " = None"}, {"name": "key_value_dict", "val": " = None"}]- **parameters** (`torch.Tensor` or `list(torch.Tensors)`) --
  The input parameters.
- **key** (`str`) --
  The hyperparameter to override.
- **value** --
  The hyperparameter value.
- **key_value_dict** (`dict`) --
  A dictionary with multiple key-values to override.0

Override initial optimizer config with specific hyperparameters.

The key-values of the optimizer config for the input parameters are overridden
This can be both, optimizer parameters like `betas` or `lr`, or it can be
8-bit specific parameters like `optim_bits` or `percentile_clipping`.

Example:

```py
import torch
import bitsandbytes as bnb

mng = bnb.optim.GlobalOptimManager.get_instance()

model = MyModel()
mng.register_parameters(model.parameters()) # 1. register parameters while still on CPU

model = model.cuda()
# use 8-bit optimizer states for all parameters
adam = bnb.optim.Adam(model.parameters(), lr=0.001, optim_bits=8)

# 2. override: the parameter model.fc1.weight now uses 32-bit Adam
mng.override_config(model.fc1.weight, 'optim_bits', 32)
```

**Parameters:**

parameters (`torch.Tensor` or `list(torch.Tensors)`) : The input parameters.

key (`str`) : The hyperparameter to override.

value : The hyperparameter value.

key_value_dict (`dict`) : A dictionary with multiple key-values to override.

### Adam
https://huggingface.co/docs/bitsandbytes/v0.49.1/reference/optim/adam.md

# Adam

[Adam (Adaptive moment estimation)](https://hf.co/papers/1412.6980) is an adaptive learning rate optimizer, combining ideas from `SGD` with momentum and `RMSprop` to automatically scale the learning rate:

- a weighted average of the past gradients to provide direction (first-moment)
- a weighted average of the *squared* past gradients to adapt the learning rate to each parameter (second-moment)

bitsandbytes also supports paged optimizers which take advantage of CUDAs unified memory to transfer memory from the GPU to the CPU when GPU memory is exhausted.

## Adam[[api-class]][[bitsandbytes.optim.Adam]]

#### bitsandbytes.optim.Adam[[bitsandbytes.optim.Adam]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adam.py#L9)

__init__bitsandbytes.optim.Adam.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adam.py#L10[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "betas", "val": " = (0.9, 0.999)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0"}, {"name": "amsgrad", "val": " = False"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}, {"name": "is_paged", "val": " = False"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value prevents division by zero in the optimizer.
- **weight_decay** (`float`, defaults to 0.0) --
  The weight decay value for the optimizer.
- **amsgrad** (`bool`, defaults to `False`) --
  Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.
- **is_paged** (`bool`, defaults to `False`) --
  Whether the optimizer is a paged optimizer or not.0

Base Adam optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value prevents division by zero in the optimizer.

weight_decay (`float`, defaults to 0.0) : The weight decay value for the optimizer.

amsgrad (`bool`, defaults to `False`) : Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

is_paged (`bool`, defaults to `False`) : Whether the optimizer is a paged optimizer or not.

## Adam8bit[[bitsandbytes.optim.Adam8bit]]

#### bitsandbytes.optim.Adam8bit[[bitsandbytes.optim.Adam8bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adam.py#L70)

__init__bitsandbytes.optim.Adam8bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adam.py#L71[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "betas", "val": " = (0.9, 0.999)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0"}, {"name": "amsgrad", "val": " = False"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}, {"name": "is_paged", "val": " = False"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value prevents division by zero in the optimizer.
- **weight_decay** (`float`, defaults to 0.0) --
  The weight decay value for the optimizer.
- **amsgrad** (`bool`, defaults to `False`) --
  Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.
  Note: This parameter is not supported in Adam8bit and must be False.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
  Note: This parameter is not used in Adam8bit as it always uses 8-bit optimization.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.
- **is_paged** (`bool`, defaults to `False`) --
  Whether the optimizer is a paged optimizer or not.0

8-bit Adam optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value prevents division by zero in the optimizer.

weight_decay (`float`, defaults to 0.0) : The weight decay value for the optimizer.

amsgrad (`bool`, defaults to `False`) : Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead. Note: This parameter is not supported in Adam8bit and must be False.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state. Note: This parameter is not used in Adam8bit as it always uses 8-bit optimization.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

is_paged (`bool`, defaults to `False`) : Whether the optimizer is a paged optimizer or not.

## Adam32bit[[bitsandbytes.optim.Adam32bit]]

#### bitsandbytes.optim.Adam32bit[[bitsandbytes.optim.Adam32bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adam.py#L142)

__init__bitsandbytes.optim.Adam32bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adam.py#L143[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "betas", "val": " = (0.9, 0.999)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0"}, {"name": "amsgrad", "val": " = False"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}, {"name": "is_paged", "val": " = False"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value prevents division by zero in the optimizer.
- **weight_decay** (`float`, defaults to 0.0) --
  The weight decay value for the optimizer.
- **amsgrad** (`bool`, defaults to `False`) --
  Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.
- **is_paged** (`bool`, defaults to `False`) --
  Whether the optimizer is a paged optimizer or not.0

32-bit Adam optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value prevents division by zero in the optimizer.

weight_decay (`float`, defaults to 0.0) : The weight decay value for the optimizer.

amsgrad (`bool`, defaults to `False`) : Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

is_paged (`bool`, defaults to `False`) : Whether the optimizer is a paged optimizer or not.

## PagedAdam[[bitsandbytes.optim.PagedAdam]]

#### bitsandbytes.optim.PagedAdam[[bitsandbytes.optim.PagedAdam]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adam.py#L203)

__init__bitsandbytes.optim.PagedAdam.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adam.py#L204[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "betas", "val": " = (0.9, 0.999)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0"}, {"name": "amsgrad", "val": " = False"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}, {"name": "is_paged", "val": " = False"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value prevents division by zero in the optimizer.
- **weight_decay** (`float`, defaults to 0.0) --
  The weight decay value for the optimizer.
- **amsgrad** (`bool`, defaults to `False`) --
  Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.
- **is_paged** (`bool`, defaults to `False`) --
  Whether the optimizer is a paged optimizer or not.0

Paged Adam optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value prevents division by zero in the optimizer.

weight_decay (`float`, defaults to 0.0) : The weight decay value for the optimizer.

amsgrad (`bool`, defaults to `False`) : Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

is_paged (`bool`, defaults to `False`) : Whether the optimizer is a paged optimizer or not.

## PagedAdam8bit[[bitsandbytes.optim.PagedAdam8bit]]

#### bitsandbytes.optim.PagedAdam8bit[[bitsandbytes.optim.PagedAdam8bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adam.py#L264)

__init__bitsandbytes.optim.PagedAdam8bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adam.py#L265[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "betas", "val": " = (0.9, 0.999)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0"}, {"name": "amsgrad", "val": " = False"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}, {"name": "is_paged", "val": " = False"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value prevents division by zero in the optimizer.
- **weight_decay** (`float`, defaults to 0.0) --
  The weight decay value for the optimizer.
- **amsgrad** (`bool`, defaults to `False`) --
  Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.
  Note: This parameter is not supported in PagedAdam8bit and must be False.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
  Note: This parameter is not used in PagedAdam8bit as it always uses 8-bit optimization.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.
- **is_paged** (`bool`, defaults to `False`) --
  Whether the optimizer is a paged optimizer or not.0

8-bit paged Adam optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value prevents division by zero in the optimizer.

weight_decay (`float`, defaults to 0.0) : The weight decay value for the optimizer.

amsgrad (`bool`, defaults to `False`) : Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead. Note: This parameter is not supported in PagedAdam8bit and must be False.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state. Note: This parameter is not used in PagedAdam8bit as it always uses 8-bit optimization.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

is_paged (`bool`, defaults to `False`) : Whether the optimizer is a paged optimizer or not.

## PagedAdam32bit[[bitsandbytes.optim.PagedAdam32bit]]

#### bitsandbytes.optim.PagedAdam32bit[[bitsandbytes.optim.PagedAdam32bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adam.py#L336)

__init__bitsandbytes.optim.PagedAdam32bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adam.py#L337[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "betas", "val": " = (0.9, 0.999)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0"}, {"name": "amsgrad", "val": " = False"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}, {"name": "is_paged", "val": " = False"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value prevents division by zero in the optimizer.
- **weight_decay** (`float`, defaults to 0.0) --
  The weight decay value for the optimizer.
- **amsgrad** (`bool`, defaults to `False`) --
  Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.
- **is_paged** (`bool`, defaults to `False`) --
  Whether the optimizer is a paged optimizer or not.0

Paged 32-bit Adam optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value prevents division by zero in the optimizer.

weight_decay (`float`, defaults to 0.0) : The weight decay value for the optimizer.

amsgrad (`bool`, defaults to `False`) : Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

is_paged (`bool`, defaults to `False`) : Whether the optimizer is a paged optimizer or not.

### AdaGrad
https://huggingface.co/docs/bitsandbytes/v0.49.1/reference/optim/adagrad.md

# AdaGrad

[AdaGrad (Adaptive Gradient)](https://jmlr.org/papers/v12/duchi11a.html) is an adaptive learning rate optimizer. AdaGrad stores a sum of the squared past gradients for each parameter and uses it to scale their learning rate. This allows the learning rate to be automatically lower or higher depending on the magnitude of the gradient, eliminating the need to manually tune the learning rate.

## Adagrad[[api-class]][[bitsandbytes.optim.Adagrad]]

#### bitsandbytes.optim.Adagrad[[bitsandbytes.optim.Adagrad]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adagrad.py#L8)

__init__bitsandbytes.optim.Adagrad.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adagrad.py#L9[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.01"}, {"name": "lr_decay", "val": " = 0"}, {"name": "weight_decay", "val": " = 0"}, {"name": "initial_accumulator_value", "val": " = 0"}, {"name": "eps", "val": " = 1e-10"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-2) --
  The learning rate.
- **lr_decay** (`int`, defaults to 0) --
  The learning rate decay.
- **weight_decay** (`float`, defaults to 0.0) --
  The weight decay value for the optimizer.
- **initial_accumulator_value** (`int`, defaults to 0) --
  The initial momemtum values.
- **eps** (`float`, defaults to 1e-10) --
  The epsilon value prevents division by zero in the optimizer.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.0

Base Adagrad optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-2) : The learning rate.

lr_decay (`int`, defaults to 0) : The learning rate decay.

weight_decay (`float`, defaults to 0.0) : The weight decay value for the optimizer.

initial_accumulator_value (`int`, defaults to 0) : The initial momemtum values.

eps (`float`, defaults to 1e-10) : The epsilon value prevents division by zero in the optimizer.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

## Adagrad8bit[[bitsandbytes.optim.Adagrad8bit]]

#### bitsandbytes.optim.Adagrad8bit[[bitsandbytes.optim.Adagrad8bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adagrad.py#L75)

__init__bitsandbytes.optim.Adagrad8bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adagrad.py#L76[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.01"}, {"name": "lr_decay", "val": " = 0"}, {"name": "weight_decay", "val": " = 0"}, {"name": "initial_accumulator_value", "val": " = 0"}, {"name": "eps", "val": " = 1e-10"}, {"name": "optim_bits", "val": " = 8"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-2) --
  The learning rate.
- **lr_decay** (`int`, defaults to 0) --
  The learning rate decay.
- **weight_decay** (`float`, defaults to 0.0) --
  The weight decay value for the optimizer.
- **initial_accumulator_value** (`int`, defaults to 0) --
  The initial momemtum values.
- **eps** (`float`, defaults to 1e-10) --
  The epsilon value prevents division by zero in the optimizer.
- **optim_bits** (`int`, defaults to 8) --
  The number of bits of the optimizer state.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.0

8-bit Adagrad optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-2) : The learning rate.

lr_decay (`int`, defaults to 0) : The learning rate decay.

weight_decay (`float`, defaults to 0.0) : The weight decay value for the optimizer.

initial_accumulator_value (`int`, defaults to 0) : The initial momemtum values.

eps (`float`, defaults to 1e-10) : The epsilon value prevents division by zero in the optimizer.

optim_bits (`int`, defaults to 8) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

## Adagrad32bit[[bitsandbytes.optim.Adagrad32bit]]

#### bitsandbytes.optim.Adagrad32bit[[bitsandbytes.optim.Adagrad32bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adagrad.py#L143)

__init__bitsandbytes.optim.Adagrad32bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adagrad.py#L144[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.01"}, {"name": "lr_decay", "val": " = 0"}, {"name": "weight_decay", "val": " = 0"}, {"name": "initial_accumulator_value", "val": " = 0"}, {"name": "eps", "val": " = 1e-10"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-2) --
  The learning rate.
- **lr_decay** (`int`, defaults to 0) --
  The learning rate decay.
- **weight_decay** (`float`, defaults to 0.0) --
  The weight decay value for the optimizer.
- **initial_accumulator_value** (`int`, defaults to 0) --
  The initial momemtum values.
- **eps** (`float`, defaults to 1e-10) --
  The epsilon value prevents division by zero in the optimizer.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.0

32-bit Adagrad optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-2) : The learning rate.

lr_decay (`int`, defaults to 0) : The learning rate decay.

weight_decay (`float`, defaults to 0.0) : The weight decay value for the optimizer.

initial_accumulator_value (`int`, defaults to 0) : The initial momemtum values.

eps (`float`, defaults to 1e-10) : The epsilon value prevents division by zero in the optimizer.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

### Embedding
https://huggingface.co/docs/bitsandbytes/v0.49.1/reference/nn/embeddings.md

# Embedding

The embedding class is used to store and retrieve word embeddings from their indices. There are two types of embeddings in bitsandbytes, the standard PyTorch `Embedding` class and the `StableEmbedding` class.

The `StableEmbedding` class was introduced in the [8-bit Optimizers via Block-wise Quantization](https://hf.co/papers/2110.02861) paper to reduce gradient variance as a result of the non-uniform distribution of input tokens. This class is designed to support quantization.

## Embedding[[bitsandbytes.nn.Embedding]]

#### bitsandbytes.nn.Embedding[[bitsandbytes.nn.Embedding]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/nn/modules.py#L133)

Embedding class to store and retrieve word embeddings from their indices.

__init__bitsandbytes.nn.Embedding.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/nn/modules.py#L138[{"name": "num_embeddings", "val": ": int"}, {"name": "embedding_dim", "val": ": int"}, {"name": "padding_idx", "val": ": typing.Optional[int] = None"}, {"name": "max_norm", "val": ": typing.Optional[float] = None"}, {"name": "norm_type", "val": ": float = 2.0"}, {"name": "scale_grad_by_freq", "val": ": bool = False"}, {"name": "sparse", "val": ": bool = False"}, {"name": "_weight", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "device", "val": ": typing.Optional[torch.device] = None"}]- **num_embeddings** (`int`) --
  The number of unique embeddings (vocabulary size).
- **embedding_dim** (`int`) --
  The dimensionality of the embedding.
- **padding_idx** (`Optional[int]`) --
  Pads the output with zeros at the given index.
- **max_norm** (`Optional[float]`) --
  Renormalizes embeddings to have a maximum L2 norm.
- **norm_type** (`float`, defaults to `2.0`) --
  The p-norm to compute for the `max_norm` option.
- **scale_grad_by_freq** (`bool`, defaults to `False`) --
  Scale gradient by frequency during backpropagation.
- **sparse** (`bool`, defaults to `False`) --
  Computes dense gradients. Set to `True` to compute sparse gradients instead.
- **_weight** (`Optional[Tensor]`) --
  Pretrained embeddings.0

**Parameters:**

num_embeddings (`int`) : The number of unique embeddings (vocabulary size).

embedding_dim (`int`) : The dimensionality of the embedding.

padding_idx (`Optional[int]`) : Pads the output with zeros at the given index.

max_norm (`Optional[float]`) : Renormalizes embeddings to have a maximum L2 norm.

norm_type (`float`, defaults to `2.0`) : The p-norm to compute for the `max_norm` option.

scale_grad_by_freq (`bool`, defaults to `False`) : Scale gradient by frequency during backpropagation.

sparse (`bool`, defaults to `False`) : Computes dense gradients. Set to `True` to compute sparse gradients instead.

_weight (`Optional[Tensor]`) : Pretrained embeddings.

## StableEmbedding[[bitsandbytes.nn.StableEmbedding]]

#### bitsandbytes.nn.StableEmbedding[[bitsandbytes.nn.StableEmbedding]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/nn/modules.py#L27)

Custom embedding layer designed to improve stability during training for NLP tasks by using 32-bit optimizer states. It is designed to reduce gradient variations that can result from quantization. This embedding layer is initialized with Xavier uniform initialization followed by layer normalization.

Example:

```
# Initialize StableEmbedding layer with vocabulary size 1000, embedding dimension 300
embedding_layer = StableEmbedding(num_embeddings=1000, embedding_dim=300)

# Reset embedding parameters
embedding_layer.reset_parameters()

# Perform a forward pass with input tensor
input_tensor = torch.tensor([1, 2, 3])
output_embedding = embedding_layer(input_tensor)
```

Methods:
reset_parameters(): Reset embedding parameters using Xavier uniform initialization.
forward(input: Tensor) -> Tensor: Forward pass through the stable embedding layer.

__init__bitsandbytes.nn.StableEmbedding.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/nn/modules.py#L53[{"name": "num_embeddings", "val": ": int"}, {"name": "embedding_dim", "val": ": int"}, {"name": "padding_idx", "val": ": typing.Optional[int] = None"}, {"name": "max_norm", "val": ": typing.Optional[float] = None"}, {"name": "norm_type", "val": ": float = 2.0"}, {"name": "scale_grad_by_freq", "val": ": bool = False"}, {"name": "sparse", "val": ": bool = False"}, {"name": "_weight", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "device", "val": " = None"}, {"name": "dtype", "val": " = None"}]- **num_embeddings** (`int`) --
  The number of unique embeddings (vocabulary size).
- **embedding_dim** (`int`) --
  The dimensionality of the embedding.
- **padding_idx** (`Optional[int]`) --
  Pads the output with zeros at the given index.
- **max_norm** (`Optional[float]`) --
  Renormalizes embeddings to have a maximum L2 norm.
- **norm_type** (`float`, defaults to `2.0`) --
  The p-norm to compute for the `max_norm` option.
- **scale_grad_by_freq** (`bool`, defaults to `False`) --
  Scale gradient by frequency during backpropagation.
- **sparse** (`bool`, defaults to `False`) --
  Computes dense gradients. Set to `True` to compute sparse gradients instead.
- **_weight** (`Optional[Tensor]`) --
  Pretrained embeddings.0

**Parameters:**

norm (`torch.nn.LayerNorm`) : Layer normalization applied after the embedding.

### 4-bit quantization
https://huggingface.co/docs/bitsandbytes/v0.49.1/reference/nn/linear4bit.md

# 4-bit quantization

[QLoRA](https://hf.co/papers/2305.14314) is a finetuning method that quantizes a model to 4-bits and adds a set of low-rank adaptation (LoRA) weights to the model and tuning them through the quantized weights. This method also introduces a new data type, 4-bit NormalFloat (`LinearNF4`) in addition to the standard Float4 data type (`LinearFP4`). `LinearNF4` is a quantization data type for normally distributed data and can improve performance.

## Linear4bit[[bitsandbytes.nn.Linear4bit]]

#### bitsandbytes.nn.Linear4bit[[bitsandbytes.nn.Linear4bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/nn/modules.py#L422)

This class is the base module for the 4-bit quantization algorithm presented in [QLoRA](https://arxiv.org/abs/2305.14314).
QLoRA 4-bit linear layers uses blockwise k-bit quantization under the hood, with the possibility of selecting various
compute datatypes such as FP4 and NF4.

In order to quantize a linear layer one should first load the original fp16 / bf16 weights into
the Linear4bit module, then call `quantized_module.to("cuda")` to quantize the fp16 / bf16 weights.

Example:

```python
import torch
import torch.nn as nn

import bitsandbytes as bnb
from bnb.nn import Linear4bit

fp16_model = nn.Sequential(
    nn.Linear(64, 64),
    nn.Linear(64, 64)
)

quantized_model = nn.Sequential(
    Linear4bit(64, 64),
    Linear4bit(64, 64)
)

quantized_model.load_state_dict(fp16_model.state_dict())
quantized_model = quantized_model.to(0) # Quantization happens here
```

__init__bitsandbytes.nn.Linear4bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/nn/modules.py#L455[{"name": "input_features", "val": ""}, {"name": "output_features", "val": ""}, {"name": "bias", "val": " = True"}, {"name": "compute_dtype", "val": " = None"}, {"name": "compress_statistics", "val": " = True"}, {"name": "quant_type", "val": " = 'fp4'"}, {"name": "quant_storage", "val": " = torch.uint8"}, {"name": "device", "val": " = None"}]- **input_features** (`str`) --
  Number of input features of the linear layer.
- **output_features** (`str`) --
  Number of output features of the linear layer.
- **bias** (`bool`, defaults to `True`) --
  Whether the linear class uses the bias term as well.0

Initialize Linear4bit class.

**Parameters:**

input_features (`str`) : Number of input features of the linear layer.

output_features (`str`) : Number of output features of the linear layer.

bias (`bool`, defaults to `True`) : Whether the linear class uses the bias term as well.

## LinearFP4[[bitsandbytes.nn.LinearFP4]]

#### bitsandbytes.nn.LinearFP4[[bitsandbytes.nn.LinearFP4]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/nn/modules.py#L560)

Implements the FP4 data type.

__init__bitsandbytes.nn.LinearFP4.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/nn/modules.py#L565[{"name": "input_features", "val": ""}, {"name": "output_features", "val": ""}, {"name": "bias", "val": " = True"}, {"name": "compute_dtype", "val": " = None"}, {"name": "compress_statistics", "val": " = True"}, {"name": "quant_storage", "val": " = torch.uint8"}, {"name": "device", "val": " = None"}]- **input_features** (`str`) --
  Number of input features of the linear layer.
- **output_features** (`str`) --
  Number of output features of the linear layer.
- **bias** (`bool`, defaults to `True`) --
  Whether the linear class uses the bias term as well.0

**Parameters:**

input_features (`str`) : Number of input features of the linear layer.

output_features (`str`) : Number of output features of the linear layer.

bias (`bool`, defaults to `True`) : Whether the linear class uses the bias term as well.

## LinearNF4[[bitsandbytes.nn.LinearNF4]]

#### bitsandbytes.nn.LinearNF4[[bitsandbytes.nn.LinearNF4]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/nn/modules.py#L596)

Implements the NF4 data type.

Constructs a quantization data type where each bin has equal area under a standard normal distribution N(0, 1) that
is normalized into the range [-1, 1].

For more information read the paper: QLoRA: Efficient Finetuning of Quantized LLMs (https://arxiv.org/abs/2305.14314)

Implementation of the NF4 data type in bitsandbytes can be found in the `create_normal_map` function in
the `functional.py` file: https://github.com/TimDettmers/bitsandbytes/blob/main/bitsandbytes/functional.py#L236.

__init__bitsandbytes.nn.LinearNF4.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/nn/modules.py#L608[{"name": "input_features", "val": ""}, {"name": "output_features", "val": ""}, {"name": "bias", "val": " = True"}, {"name": "compute_dtype", "val": " = None"}, {"name": "compress_statistics", "val": " = True"}, {"name": "quant_storage", "val": " = torch.uint8"}, {"name": "device", "val": " = None"}]- **input_features** (`str`) --
  Number of input features of the linear layer.
- **output_features** (`str`) --
  Number of output features of the linear layer.
- **bias** (`bool`, defaults to `True`) --
  Whether the linear class uses the bias term as well.0

**Parameters:**

input_features (`str`) : Number of input features of the linear layer.

output_features (`str`) : Number of output features of the linear layer.

bias (`bool`, defaults to `True`) : Whether the linear class uses the bias term as well.

## Params4bit[[bitsandbytes.nn.Params4bit]]

#### bitsandbytes.nn.Params4bit[[bitsandbytes.nn.Params4bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/nn/modules.py#L212)

__init__bitsandbytes.nn.Params4bit.__init__[{"name": "*args", "val": ""}, {"name": "**kwargs", "val": ""}]
Initialize self.  See help(type(self)) for accurate signature.

### LLM.int8()
https://huggingface.co/docs/bitsandbytes/v0.49.1/reference/nn/linear8bit.md

# LLM.int8()
[LLM.int8()](https://hf.co/papers/2208.07339) is a quantization method that aims to make large language model inference more accessible without significant degradation. Unlike naive 8-bit quantization, which can result in loss of critical information and accuracy, LLM.int8() dynamically adapts to ensure sensitive components of the computation retain higher precision when needed. The key is to extract the outliers from the inputs and weights and multiply them in 16-bit. All other values are multiplied in 8-bit before being dequantized back to 16-bits. The outputs from the 16-bit and 8-bit multiplication are combined to produce the final output.

[Further Resources](../../explanations/resources#llm-int8)

## Linear8bitLt[[bitsandbytes.nn.Linear8bitLt]]

#### bitsandbytes.nn.Linear8bitLt[[bitsandbytes.nn.Linear8bitLt]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/nn/modules.py#L937)

This class is the base module for the [LLM.int8()](https://arxiv.org/abs/2208.07339) algorithm.
To read more about it, have a look at the paper.

In order to quantize a linear layer one should first load the original fp16 / bf16 weights into
the Linear8bitLt module, then call `int8_module.to("cuda")` to quantize the fp16 weights.

Example:

```python
import torch
import torch.nn as nn

import bitsandbytes as bnb
from bnb.nn import Linear8bitLt

fp16_model = nn.Sequential(
    nn.Linear(64, 64),
    nn.Linear(64, 64)
)

int8_model = nn.Sequential(
    Linear8bitLt(64, 64, has_fp16_weights=False),
    Linear8bitLt(64, 64, has_fp16_weights=False)
)

int8_model.load_state_dict(fp16_model.state_dict())
int8_model = int8_model.to(0) # Quantization happens here
```

__init__bitsandbytes.nn.Linear8bitLt.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/nn/modules.py#L969[{"name": "input_features", "val": ": int"}, {"name": "output_features", "val": ": int"}, {"name": "bias", "val": " = True"}, {"name": "has_fp16_weights", "val": " = True"}, {"name": "threshold", "val": " = 0.0"}, {"name": "index", "val": " = None"}, {"name": "device", "val": " = None"}]- **input_features** (`int`) --
  Number of input features of the linear layer.
- **output_features** (`int`) --
  Number of output features of the linear layer.
- **bias** (`bool`, defaults to `True`) --
  Whether the linear class uses the bias term as well.0

Initialize Linear8bitLt class.

**Parameters:**

input_features (`int`) : Number of input features of the linear layer.

output_features (`int`) : Number of output features of the linear layer.

bias (`bool`, defaults to `True`) : Whether the linear class uses the bias term as well.

## Int8Params[[bitsandbytes.nn.Int8Params]]

#### bitsandbytes.nn.Int8Params[[bitsandbytes.nn.Int8Params]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/nn/modules.py#L639)

__init__bitsandbytes.nn.Int8Params.__init__[{"name": "*args", "val": ""}, {"name": "**kwargs", "val": ""}]
Initialize self.  See help(type(self)) for accurate signature.
