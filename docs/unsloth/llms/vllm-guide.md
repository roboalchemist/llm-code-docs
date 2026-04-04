# Source: https://unsloth.ai/docs/fr/notions-de-base/inference-and-deployment/vllm-guide.md

# Source: https://unsloth.ai/docs/de/grundlagen/inference-and-deployment/vllm-guide.md

# Source: https://unsloth.ai/docs/jp/ji-ben/inference-and-deployment/vllm-guide.md

# Source: https://unsloth.ai/docs/zh/ji-chu-zhi-shi/inference-and-deployment/vllm-guide.md

# Source: https://unsloth.ai/docs/basics/inference-and-deployment/vllm-guide.md

# vLLM Deployment & Inference Guide

### :computer:Installing vLLM

For NVIDIA GPUs, use uv and run:

```bash
pip install --upgrade pip
pip install uv
uv pip install -U vllm --torch-backend=auto
```

For AMD GPUs, please use the nightly Docker image: `rocm/vllm-dev:nightly`

For the nightly branch for NVIDIA GPUs, run:

{% code overflow="wrap" %}

```bash
pip install --upgrade pip
pip install uv
uv pip install -U vllm --torch-backend=auto --extra-index-url https://wheels.vllm.ai/nightly
```

{% endcode %}

See [vLLM docs](https://docs.vllm.ai/en/stable/getting_started/installation) for more details

### :truck:Deploying vLLM models

After saving your fine-tune, you can simply do:

```bash
vllm serve unsloth/gpt-oss-120b
```

### :fire\_engine:vLLM Deployment Server Flags, Engine Arguments & Options

Some important server flags to use are at [#vllm-deployment-server-flags-engine-arguments-and-options](#vllm-deployment-server-flags-engine-arguments-and-options "mention")

### 🦥Deploying Unsloth finetunes in vLLM

After fine-tuning [fine-tuning-llms-guide](https://unsloth.ai/docs/get-started/fine-tuning-llms-guide "mention") or using our notebooks at [unsloth-notebooks](https://unsloth.ai/docs/get-started/unsloth-notebooks "mention"), you can save or deploy your models directly through vLLM within a single workflow. An example Unsloth finetuning script for eg:

```python
from unsloth import FastLanguageModel
import torch
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/gpt-oss-20b",
    max_seq_length = 2048,
    load_in_4bit = True,
)
model = FastLanguageModel.get_peft_model(model)
```

**To save to 16-bit for vLLM, use:**

{% code overflow="wrap" %}

```python
model.save_pretrained_merged("finetuned_model", tokenizer, save_method = "merged_16bit")
## OR to upload to HuggingFace:
model.push_to_hub_merged("hf/model", tokenizer, save_method = "merged_16bit", token = "")
```

{% endcode %}

**To save just the LoRA adapters**, either use:

```python
model.save_pretrained("finetuned_lora")
tokenizer.save_pretrained("finetuned_lora")
```

Or just use our builtin function to do that:

{% code overflow="wrap" %}

```python
model.save_pretrained_merged("finetuned_model", tokenizer, save_method = "lora")
## OR to upload to HuggingFace
model.push_to_hub_merged("hf/model", tokenizer, save_method = "lora", token = "")
```

{% endcode %}

To merge to 4bit to load on HuggingFace, first call `merged_4bit`. Then use `merged_4bit_forced` if you are certain you want to merge to 4bit. I highly discourage you, unless you know what you are going to do with the 4bit model (ie for DPO training for eg or for HuggingFace's online inference engine)

{% code overflow="wrap" %}

```python
model.save_pretrained_merged("finetuned_model", tokenizer, save_method = "merged_4bit")
## To upload to HuggingFace:
model.push_to_hub_merged("hf/model", tokenizer, save_method = "merged_4bit", token = "")
```

{% endcode %}

Then to load the finetuned model in vLLM in another terminal:

```bash
vllm serve finetuned_model
```

You might have to provide the full path if the above doesn't work ie:

```bash
vllm serve /mnt/disks/daniel/finetuned_model
```

See other content:

### [vllm-engine-arguments](https://unsloth.ai/docs/basics/inference-and-deployment/vllm-guide/vllm-engine-arguments "mention")

### [lora-hot-swapping-guide](https://unsloth.ai/docs/basics/inference-and-deployment/vllm-guide/lora-hot-swapping-guide "mention")
