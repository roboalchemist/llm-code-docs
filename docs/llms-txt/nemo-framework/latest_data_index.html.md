# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/data/index.html.md

Title: NeMo 2.0 Data Modules — NVIDIA NeMo Framework User Guide

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/data/index.html

Published Time: Fri, 18 Jul 2025 19:27:25 GMT

Markdown Content:
NeMo 2.0 Data Modules[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/data/index.html.md#nemo-2-0-data-modules "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------

NeMo provides two primary data modules for working with Large Language Models (LLMs):

PreTrainingDataModule[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/data/index.html.md#pretrainingdatamodule "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------

Located in `nemo.collections.llm.gpt.data.pre_training`, this module is optimized for unsupervised pre-training of LLMs from scratch on large corpora of text data. In this case, the dataset is pre-tokenized and saved as token indices on disk using the [Megatron dataset format](https://github.com/NVIDIA/Megatron-LM/blob/main/tools/preprocess_data.py.md).

It supports:

*   Training on multiple data distributions with customizable weights

*   Efficient data loading through memory mapping

*   Automatic validation and test set creation

*   Built-in data validation and accessibility checks

*   Support for distributed training with Megatron-style data parallelism

FineTuningDataModule[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/data/index.html.md#finetuningdatamodule "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------

Located in `nemo.collections.llm.gpt.data.fine_tuning`, this module is designed for supervised fine-tuning (including parameter-efficient fine-tuning) of pre-trained models on specific tasks or domains.

Key features include:

*   Support for standard fine-tuning datasets in JSONL format

*   Packed sequence training for improved efficiency

*   Automatic handling of train/validation/test splits

*   Integration with various tokenizers

*   Memory-efficient data loading

Both modules inherit from PyTorch Lightning’s `LightningDataModule`, providing a consistent interface while being optimized for their respective use cases. The separation between pre-training and fine-tuning data modules reflects the distinct requirements and optimizations needed for these two phases of LLM development.

For detailed usage of the two data modules, please see the following pages.

*   [Pre-Training Data Module](https://docs.nvidia.com/nemo-framework/user-guide/latest/data/pretrain_data.html.md)
*   [Fine-Tuning Data Module](https://docs.nvidia.com/nemo-framework/user-guide/latest/data/finetune_data.html.md)

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/data/index.html.md#finetuningdatamodule)
- [Megatron dataset format](https://github.com/NVIDIA/Megatron-LM/blob/main/tools/preprocess_data.py.md)
- [Pre-Training Data Module](https://docs.nvidia.com/nemo-framework/user-guide/latest/data/pretrain_data.html.md)
- [Fine-Tuning Data Module](https://docs.nvidia.com/nemo-framework/user-guide/latest/data/finetune_data.html.md)
