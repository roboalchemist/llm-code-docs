# Source: https://unsloth.ai/docs/fr/notions-de-base/inference-and-deployment/vllm-guide/lora-hot-swapping-guide.md

# Source: https://unsloth.ai/docs/de/grundlagen/inference-and-deployment/vllm-guide/lora-hot-swapping-guide.md

# Source: https://unsloth.ai/docs/jp/ji-ben/inference-and-deployment/vllm-guide/lora-hot-swapping-guide.md

# Source: https://unsloth.ai/docs/zh/ji-chu-zhi-shi/inference-and-deployment/vllm-guide/lora-hot-swapping-guide.md

# Source: https://unsloth.ai/docs/basics/inference-and-deployment/vllm-guide/lora-hot-swapping-guide.md

# LoRA Hot Swapping Guide

### :shaved\_ice: vLLM LoRA Hot Swapping / Dynamic LoRAs

To enable LoRA serving for at most 4 LoRAs at 1 time (these are hot swapped / changed), first set the environment flag to allow hot swapping:

```bash
export VLLM_ALLOW_RUNTIME_LORA_UPDATING=True
```

Then, serve it with LoRA support:

```bash
export VLLM_ALLOW_RUNTIME_LORA_UPDATING=True
vllm serve unsloth/Llama-3.1-8B-Instruct \
    --quantization fp8 \
    --kv-cache-dtype fp8
    --gpu-memory-utilization 0.8 \
    --max-model-len 65536 \
    --enable-lora \
    --max-loras 4 \
    --max-lora-rank 64
```

To load a LoRA dynamically (set the lora name as well), do:

```bash
curl -X POST http://localhost:8000/v1/load_lora_adapter \
    -H "Content-Type: application/json" \
    -d '{
        "lora_name": "LORA_NAME",
        "lora_path": "/path/to/LORA"
    }'
```

To remove it from the pool:

```bash
curl -X POST http://localhost:8000/v1/unload_lora_adapter \
    -H "Content-Type: application/json" \
    -d '{
        "lora_name": "LORA_NAME"
    }'
```

For example when finetuning with Unsloth:

{% code overflow="wrap" %}

```python
from unsloth import FastLanguageModel
import torch
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/Llama-3.1-8B-Instruct",
    max_seq_length = 2048,
    load_in_4bit = True,
)
model = FastLanguageModel.get_peft_model(model)
```

{% endcode %}

Then after training, we save the LoRAs:

```python
model.save_pretrained("finetuned_lora")
tokenizer.save_pretrained("finetuned_lora")
```

We can then load the LoRA:

{% code overflow="wrap" %}

```bash
curl -X POST http://localhost:8000/v1/load_lora_adapter \
    -H "Content-Type: application/json" \
    -d '{
        "lora_name": "LORA_NAME_finetuned_lora",
        "lora_path": "finetuned_lora"
    }'
```

{% endcode %}
