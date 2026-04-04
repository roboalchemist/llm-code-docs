# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/data/finetune_data.html.md

Title: Fine-tuning with Custom Datasets — NVIDIA NeMo Framework User Guide

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/data/finetune_data.html

Published Time: Fri, 05 Sep 2025 18:59:46 GMT

Markdown Content:
Fine-tuning with Custom Datasets[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/data/finetune_data.html.md#fine-tuning-with-custom-datasets "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Overview[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/data/finetune_data.html.md#overview "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------

The `FineTuningDataModule` is a base class in NeMo 2 for fine-tuning Large Language Models (LLMs) for supervised tasks, such as question answering, instruction tuning, function calling, etc. It handles data loading, preprocessing, and batch creation for training, validation, and testing phases. This class integrates with PyTorch Lightning’s `LightningDataModule` and NeMo’s SFT dataset classes (`GPTSFTDataset`, `GPTSFTChatDataset`, and `GPTSFTPackedDataset`).

NeMo’s fine-tuning datasets are formatted as jsonl files. Each file contains lines of json-formatted text, and each line should contain a minimum of two keys, “input” and “output”. Additional keys can be added, and are returned by the data loader as is. This is useful, for example, if you want to filter or modify any data on-the-fly.

{"input": "This is the input/prompt/context/question for sample 1. Escape any double quotes like \"this\".", "output": "This is the output/answer/completion part of sample 1"}
{"input": "This is the input/prompt/context/question for sample 2. Escape any double quotes like \"this\".", "output": "This is the output/answer/completion part of sample 2"}
...

During training, by default, “input” and “output” are naively concatenated to be passed into the transformer model. Moreover, loss is only computed on the “output” tokens by default. These two behaviors can be customized with the `dataset_kwargs` field in the data module.

FineTuningDataModule(
    ...,
    dataset_kwargs={
        "prompt_template": "Question: {input} Answer: {output}",  # default is "{input} {output}" (naive concatenation)
        "answer_only_loss": False,  # default is True (only calculate loss on answer/output)
    }
)

NeMo 2 comes with a few pre-defined dataset-specific data modules which subclass `FineTuningDataModule`, so that users can get started with fine-tuning in NeMo 2 easily. See the list of pre-defined data modules [here](https://github.com/NVIDIA/NeMo/tree/main/nemo/collections/llm/gpt/data). When you are ready to use your own datasets, this guide provides you with two options to prepare the datasets for training in NeMo 2.

Option 1: Create a Custom DataModule[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/data/finetune_data.html.md#option-1-create-a-custom-datamodule "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To create your own DataModule, subclass `FineTuningDataModule` and implement the necessary preprocessing logic, similar to the pre-defined data modules [here](https://github.com/NVIDIA/NeMo/tree/main/nemo/collections/llm/gpt/data).

*   `_download_data()` defines the logic to download the raw dataset from the internet. If you dataset is locally hosted, you can load it in this function and return the loaded dataset.

*   `_preprocess_and_split_data()` defines the logic to preprocess the raw data into the jsonl format specified above, as well as splitting the dataset into training, validation, and test sets. The function should save three files:

> dataset_root/
>     ├── training.jsonl
>     ├── validation.jsonl
>     └── test.jsonl

Note: Both of these functions are called by the `prepare_data()` hook in Pytorch Lightning, which runs this function in a single process.

You can find an end-to-end tutorial utilizing a custom data module here: [🔗 Create a Distillation Pipeline to Distill DeepSeek-R1 into Qwen model with NeNo 2.0 Framework](https://github.com/NVIDIA/NeMo/blob/main/tutorials/llm/distill_deepseek_r1/qwen2_distill_nemo.ipynb).

Option 2: Use FineTuningDataModule with Preprocessed Data[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/data/finetune_data.html.md#option-2-use-finetuningdatamodule-with-preprocessed-data "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you prefer preprocessing the dataset offline, you can also use `FineTuningDataModule` directly by specifying the location of preprocessed data.

1.   Create training, validation and test files by preprocessing your raw data into the format specified above:

> your_dataset_root/
>     ├── training.jsonl
>     ├── validation.jsonl
>     └── test.jsonl

2.   Set up FineTuningDataModule to point to `dataset_root`, as well as any additional kwargs, if needed.

> FineTuningDataModule(
>     dataset_root="your_dataset_root",
>     seq_length=512,
>     micro_batch_size=1,
>     global_batch_size=128,
>     dataset_kwargs={},
> )

You can find an end-to-end tutorial utilizing data prepared offline here: [🔗 Fine-Tuning LLMs for Function Calling](https://github.com/NVIDIA/NeMo/blob/main/tutorials/llm/function_calling/nemo2-chat-sft-function-calling.ipynb). This tutorial uses `ChatDataModule`, which sets a few default arguments on top of `FineTuningDataModule`, but is otherwise the same.

Advanced Features[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/data/finetune_data.html.md#advanced-features "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------

1.   **Packed Sequence Training**: To minimize the impact of padding for uneven sequence lengths, you can enable packed sequence training by providing `packed_sequence_specs`. Read more here: [Sequence Packing](https://docs.nvidia.com/nemo-framework/user-guide/latest/sft_peft/packed_sequence.html.md#packed-seq).

2.   **Sequence Length Truncation**: You can customize how a sequence is truncated when it is longer than `seq_length` using the following two dataset_kwargs: `truncation_field` and `truncation_method`.

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/data/finetune_data.html.md#advanced-features)
- [here](https://github.com/NVIDIA/NeMo/tree/main/nemo/collections/llm/gpt/data)
- [🔗 Create a Distillation Pipeline to Distill DeepSeek-R1 into Qwen model with NeNo 2.0 Framework](https://github.com/NVIDIA/NeMo/blob/main/tutorials/llm/distill_deepseek_r1/qwen2_distill_nemo.ipynb)
- [🔗 Fine-Tuning LLMs for Function Calling](https://github.com/NVIDIA/NeMo/blob/main/tutorials/llm/function_calling/nemo2-chat-sft-function-calling.ipynb)
- [Sequence Packing](https://docs.nvidia.com/nemo-framework/user-guide/latest/sft_peft/packed_sequence.html.md#packed-seq)
