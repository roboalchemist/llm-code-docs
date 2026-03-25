# Source: https://unsloth.ai/docs/fr/notions-de-base/multi-gpu-training-with-unsloth.md

# Source: https://unsloth.ai/docs/de/grundlagen/multi-gpu-training-with-unsloth.md

# Source: https://unsloth.ai/docs/jp/ji-ben/multi-gpu-training-with-unsloth.md

# Source: https://unsloth.ai/docs/zh/ji-chu-zhi-shi/multi-gpu-training-with-unsloth.md

# Source: https://unsloth.ai/docs/basics/multi-gpu-training-with-unsloth.md

# Multi-GPU Fine-tuning with Unsloth

Unsloth currently supports multi-GPU setups through libraries like Accelerate and DeepSpeed. This means you can already leverage parallelism methods such as **FSDP** and **DDP** with Unsloth.

#### **See our new Distributed Data Parallel** [**(DDP) multi-GPU Guide here**](https://unsloth.ai/docs/basics/multi-gpu-training-with-unsloth/ddp)**.**

We know that the process can be complex and requires manual setup. We’re working hard to make multi-GPU support much simpler and more user-friendly, and we’ll be announcing official multi-GPU support for Unsloth soon.

For now, you can use our [Magistral-2509 Kaggle notebook](https://unsloth.ai/docs/models/tutorials/magistral-how-to-run-and-fine-tune#fine-tuning-magistral-with-unsloth) as an example which utilizes multi-GPU Unsloth to fit the 24B parameter model or our [DDP guide](https://unsloth.ai/docs/basics/multi-gpu-training-with-unsloth/ddp).

**In the meantime**, to enable multi GPU for DDP, do the following:

1. Create your training script as `train.py` (or similar). For example, you can use one of our [training scripts](https://github.com/unslothai/notebooks/tree/main/python_scripts) created from our various notebooks!
2. Run `accelerate launch train.py` or `torchrun --nproc_per_node N_GPUS train.py` where `N_GPUS` is the number of GPUs you have.

#### **Pipeline / model splitting loading**

If you do not have enough VRAM for 1 GPU to load say Llama 70B, no worries - we will split the model for you on each GPU! To enable this, use the `device_map = "balanced"` flag:

```python
from unsloth import FastLanguageModel
model, tokenizer = FastLanguageModel.from_pretrained(
    "unsloth/Llama-3.3-70B-Instruct",
    load_in_4bit = True,
    device_map = "balanced",
)
```

**Stay tuned for our official announcement!**\
For more details, check out our ongoing [Pull Request](https://github.com/unslothai/unsloth/issues/2435) discussing multi-GPU support.
