# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/sft.html.md

Title: Migrate SFT Training and Inference from NeMo 1.0 to NeMo 2.0#

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/sft.html

Published Time: Thu, 30 Oct 2025 07:07:30 GMT

Markdown Content:
NeMo 1.0 (Previous Release)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/sft.html.md#nemo-1-0-previous-release "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

In NeMo 1.0, SFT is configured using [megatron_gpt_finetuning_config.yaml](https://github.com/NVIDIA/NeMo/blob/main/examples/nlp/language_modeling/tuning/conf/megatron_gpt_finetuning_config.yaml), and launched with [megatron_gpt_finetuning.py](https://github.com/NVIDIA/NeMo/blob/main/examples/nlp/language_modeling/tuning/megatron_gpt_finetuning.py), which are both completely separate from the pretraining scripts. Internally, this script instantiates a different model class (`MegatronGPTSFTModel`), even though the only difference from pretraining is the data pipeline. This design has been a point of confusion for many users of NeMo 1.0.

NeMo 2.0 (New Release)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/sft.html.md#nemo-2-0-new-release "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------

In NeMo 2.0, the design has been improved to address this problem. The data module and model class are now independent building blocks which can be combined intuitively to improve versatility and minimize redundancy. For SFT, the data module is [FineTuningDataModule](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/gpt/data/fine_tuning.py), and the rest of the pipeline is shared with pretraining.

In addition, we provide dataset-specific data modules for the convenience of users to start training without having to worry about data downloading and preprocessing. Supported datasets can be found [here](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/gpt/data/api.py).

Warning

When using `import_ckpt` in NeMo 2.0, ensure your script includes `if __name__ == "__main__":`. Without this, Python’s multiprocessing won’t initialize threads properly, causing a “Failure to acquire lock” error.

In NeMo 2.0, a fine-tuning workload can be run like this:

from nemo import lightning as nl
from nemo.collections import llm

if  __name__  == "__main__":
   trainer = nl.Trainer(...)
   model = llm.LlamaModel(...)
   ckpt_path = model.import_ckpt("hf://meta-llama/Meta-Llama-3-8B")

   # Option 1: custom dataset
   data = llm.FineTuningDataModule(dataset_root, seq_length=2048, micro_batch_size=1, global_batch_size=128, ...)
   # Option 2: provided dataset
   data = llm.SquadDataModule(seq_length=2048, micro_batch_size=1, global_batch_size=128, ...)

   trainer.fit(model, data, ckpt_path=ckpt_path)

Using the [llm.finetune](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/api.py) API with NeMo-Run:

import nemo_run as run
sft = run.Partial(
     llm.finetune,
     model=llm.mistral,
     data=llm.squad,
     trainer=trainer,
     log=logger,
     optim=adam_with_cosine_annealing,
)
run.run(sft, name="mistral-sft", direct=True)

Migration Steps[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/sft.html.md#migration-steps "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------

1.   Create a `FineTuningDataModule` using arguments from the `data` field in the YAML file. The jsonl files should be processed in the same way as in NeMo 1.0. Alternatively, use one of the provided datasets and have it processed automatically for you.

2.   Initialize the trainer, model, optimizer, logger in the same way as pretraining.

3.   Instead of `MegatronGPTSFTModel.restore_from`, use `trainer.fit(..., ckpt_path=model.import_ckpt(...))`

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/sft.html.md#migration-steps)
- [megatron_gpt_finetuning_config.yaml](https://github.com/NVIDIA/NeMo/blob/main/examples/nlp/language_modeling/tuning/conf/megatron_gpt_finetuning_config.yaml)
- [megatron_gpt_finetuning.py](https://github.com/NVIDIA/NeMo/blob/main/examples/nlp/language_modeling/tuning/megatron_gpt_finetuning.py)
- [FineTuningDataModule](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/gpt/data/fine_tuning.py)
- [here](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/gpt/data/api.py)
- [llm.finetune](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/api.py)
