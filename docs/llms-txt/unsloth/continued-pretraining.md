# Source: https://unsloth.ai/docs/fr/notions-de-base/continued-pretraining.md

# Source: https://unsloth.ai/docs/de/grundlagen/continued-pretraining.md

# Source: https://unsloth.ai/docs/jp/ji-ben/continued-pretraining.md

# Source: https://unsloth.ai/docs/zh/ji-chu-zhi-shi/continued-pretraining.md

# Source: https://unsloth.ai/docs/basics/continued-pretraining.md

# Continued Pretraining

* The [text completion notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Mistral_\(7B\)-Text_Completion.ipynb) is for continued pretraining/raw text.
* The [continued pretraining notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Mistral_v0.3_\(7B\)-CPT.ipynb) is for learning another language.

You can read more about continued pretraining and our release in our [blog post](https://unsloth.ai/blog/contpretraining).

## What is Continued Pretraining?

Continued or continual pretraining (CPT) is necessary to “steer” the language model to understand new domains of knowledge, or out of distribution domains. Base models like Llama-3 8b or Mistral 7b are first pretrained on gigantic datasets of trillions of tokens (Llama-3 for e.g. is 15 trillion).

But sometimes these models have not been well trained on other languages, or text specific domains, like law, medicine or other areas. So continued pretraining (CPT) is necessary to make the language model learn new tokens or datasets.

## Advanced Features:

### Loading LoRA adapters for continued finetuning

If you saved a LoRA adapter through Unsloth, you can also continue training using your LoRA weights. The optimizer state will be reset as well. To load even optimizer states to continue finetuning, see the next section.

```python
from unsloth import FastLanguageModel
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "LORA_MODEL_NAME",
    max_seq_length = max_seq_length,
    dtype = dtype,
    load_in_4bit = load_in_4bit,
)
trainer = Trainer(...)
trainer.train()
```

### Continued Pretraining & Finetuning the `lm_head` and `embed_tokens` matrices

Add `lm_head` and `embed_tokens`. For Colab, sometimes you will go out of memory for Llama-3 8b. If so, just add `lm_head`.

```python
model = FastLanguageModel.get_peft_model(
    model,
    r = 16,
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj",
                      "lm_head", "embed_tokens",],
    lora_alpha = 16,
)
```

Then use 2 different learning rates - a 2-10x smaller one for the `lm_head` or `embed_tokens` like so:

```python
from unsloth import UnslothTrainer, UnslothTrainingArguments

trainer = UnslothTrainer(
    ....
    args = UnslothTrainingArguments(
        ....
        learning_rate = 5e-5,
        embedding_learning_rate = 5e-6, # 2-10x smaller than learning_rate
    ),
)
```
