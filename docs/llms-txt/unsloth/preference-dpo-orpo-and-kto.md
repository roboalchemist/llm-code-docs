# Source: https://unsloth.ai/docs/fr/commencer/reinforcement-learning-rl-guide/preference-dpo-orpo-and-kto.md

# Source: https://unsloth.ai/docs/de/loslegen/reinforcement-learning-rl-guide/preference-dpo-orpo-and-kto.md

# Source: https://unsloth.ai/docs/jp/hajimeni/reinforcement-learning-rl-guide/preference-dpo-orpo-and-kto.md

# Source: https://unsloth.ai/docs/zh/kai-shi-shi-yong/reinforcement-learning-rl-guide/preference-dpo-orpo-and-kto.md

# Source: https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/preference-dpo-orpo-and-kto.md

# Preference Optimization Training - DPO, ORPO & KTO

DPO (Direct Preference Optimization), ORPO (Odds Ratio Preference Optimization), PPO, KTO Reward Modelling all work with Unsloth.

We have Google Colab notebooks for reproducing GRPO, ORPO, DPO Zephyr, KTO and SimPO:

* [GRPO notebooks](https://unsloth.ai/docs/unsloth-notebooks#grpo-reasoning-rl-notebooks)
* [ORPO notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3_\(8B\)-ORPO.ipynb)
* [DPO Zephyr notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Zephyr_\(7B\)-DPO.ipynb)
* [KTO notebook](https://colab.research.google.com/drive/1MRgGtLWuZX4ypSfGguFgC-IblTvO2ivM?usp=sharing)
* [SimPO notebook](https://colab.research.google.com/drive/1Hs5oQDovOay4mFA6Y9lQhVJ8TnbFLFh2?usp=sharing)

We're also in 🤗Hugging Face's official docs! We're on the [SFT docs](https://huggingface.co/docs/trl/main/en/sft_trainer#accelerate-fine-tuning-2x-using-unsloth) and the [DPO docs](https://huggingface.co/docs/trl/main/en/dpo_trainer#accelerate-dpo-fine-tuning-using-unsloth).

## DPO Code

```python
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0" # Optional set GPU device ID

from unsloth import FastLanguageModel, PatchDPOTrainer
from unsloth import is_bfloat16_supported
PatchDPOTrainer()
import torch
from trl import DPOTrainer, DPOConfig  # Changed from TrainingArguments

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/zephyr-sft-bnb-4bit",
    max_seq_length = max_seq_length,
    dtype = None,
    load_in_4bit = True,
)

# Do model patching and add fast LoRA weights
model = FastLanguageModel.get_peft_model(
    model,
    r = 64,
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj",],
    lora_alpha = 64,
    lora_dropout = 0, # Supports any, but = 0 is optimized
    bias = "none",    # Supports any, but = "none" is optimized
    # [NEW] "unsloth" uses 30% less VRAM, fits 2x larger batch sizes!
    use_gradient_checkpointing = "unsloth", # True or "unsloth" for very long context
    random_state = 3407,
    max_seq_length = max_seq_length,
)

dpo_trainer = DPOTrainer(
    model = model,
    ref_model = None,
    args = DPOConfig( # Use DPOConfig
        per_device_train_batch_size = 4,
        gradient_accumulation_steps = 8,
        warmup_ratio = 0.1,
        num_train_epochs = 3,
        fp16 = not is_bfloat16_supported(),
        bf16 = is_bfloat16_supported(),
        logging_steps = 1,
        optim = "adamw_8bit",
        seed = 42,
        output_dir = "outputs",
    ),
    beta = 0.1,
    train_dataset = YOUR_DATASET_HERE,
    # eval_dataset = YOUR_DATASET_HERE,
    tokenizer = tokenizer,
    max_length = 1024,
    max_prompt_length = 512,
)

dpo_trainer.train()
```
