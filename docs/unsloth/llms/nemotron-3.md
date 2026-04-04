# Source: https://unsloth.ai/docs/fr/modeles/tutorials/nemotron-3.md

# Source: https://unsloth.ai/docs/de/modelle/tutorials/nemotron-3.md

# Source: https://unsloth.ai/docs/jp/moderu/tutorials/nemotron-3.md

# Source: https://unsloth.ai/docs/zh/mo-xing/tutorials/nemotron-3.md

# Source: https://unsloth.ai/docs/models/tutorials/nemotron-3.md

# NVIDIA Nemotron 3 Nano - How To Run Guide

NVIDIA releases Nemotron 3 Nano, a 30B parameter hybrid reasoning MoE model with \~3.6B active parameters - built for fast, accurate coding, math and agentic tasks. It has a **1M context window** and is best amongst its size class on SWE-Bench, GPQA Diamond, reasoning, chat and throughput.

Nemotron 3 Nano runs on **24GB RAM**/VRAM (or unified memory) and you can now **fine-tune** it locally. Thanks NVIDIA for providing Unsloth with day-zero support.

<a href="#run-nemotron-3-nano-30b-a3b" class="button primary">Running Tutorial</a><a href="https://docs.unsloth.ai/models/nemotron-3#fine-tuning-nemotron-3-nano-and-rl" class="button secondary">Fine-tuning Nano 3</a>

NVIDIA Nemotron 3 Nano GGUF to run: [unsloth/Nemotron-3-Nano-30B-A3B-GGUF](https://huggingface.co/unsloth/Nemotron-3-Nano-30B-A3B-GGUF)\
We also uploaded [BF16](https://huggingface.co/unsloth/Nemotron-3-Nano-30B-A3B) and [FP8](https://huggingface.co/unsloth/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8) variants.

### ⚙️ Usage Guide

NVIDIA recommends these settings for inference:

{% columns %}
{% column %}
**General chat/instruction (default):**

* `temperature = 1.0`
* `top_p = 1.0`
  {% endcolumn %}

{% column %}
**Tool calling use-cases:**

* `temperature = 0.6`
* `top_p = 0.95`
  {% endcolumn %}
  {% endcolumns %}

**For most local use, set:**

* `max_new_tokens` = `32,768` to `262,144` for standard prompts with a max of 1M tokens
* Increase for deep reasoning or long-form generation as your RAM/VRAM allows.

The chat template format is found when we use the below:

{% code overflow="wrap" %}

```python
tokenizer.apply_chat_template([
    {"role" : "user", "content" : "What is 1+1?"},
    {"role" : "assistant", "content" : "2"},
    {"role" : "user", "content" : "What is 2+2?"}
    ], add_generation_prompt = True, tokenize = False,
)
```

{% endcode %}

{% hint style="success" %}
Because the model was trained with NoPE, you only need to change `max_position_embeddings`. The model doesn’t use explicit positional embeddings, so YaRN isn’t needed.
{% endhint %}

#### Nemotron 3 chat template format:

{% hint style="info" %}
Nemotron 3 uses `<think>` with token ID 12 and `</think>` with token ID 13 for reasoning. Use `--special` to see the tokens for llama.cpp. You might also need `--verbose-prompt` to see `<think>` since it's prepended.
{% endhint %}

{% code overflow="wrap" lineNumbers="true" %}

```
<|im_start|>system\n<|im_end|>\n<|im_start|>user\nWhat is 1+1?<|im_end|>\n<|im_start|>assistant\n<think></think>2<|im_end|>\n<|im_start|>user\nWhat is 2+2?<|im_end|>\n<|im_start|>assistant\n<think>\n
```

{% endcode %}

### 🖥️ Run Nemotron-3-Nano-30B-A3B

Depending on your use-case you will need to use different settings. Some GGUFs end up similar in size because the model architecture (like [gpt-oss](https://unsloth.ai/docs/models/gpt-oss-how-to-run-and-fine-tune)) has dimensions not divisible by 128, so parts can’t be quantized to lower bits.

The 4-bit versions of the model requires \~24GB RAM. 8-bit requires 36GB.

#### Llama.cpp Tutorial (GGUF):

Instructions to run in llama.cpp (note we will be using 4-bit to fit most devices):

{% stepper %}
{% step %}
Obtain the latest `llama.cpp` on [GitHub here](https://github.com/ggml-org/llama.cpp). You can follow the build instructions below as well. Change `-DGGML_CUDA=ON` to `-DGGML_CUDA=OFF` if you don't have a GPU or just want CPU inference. **For Apple Mac / Metal devices**, set `-DGGML_CUDA=OFF` then continue as usual - Metal support is on by default.

{% code overflow="wrap" %}

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

{% endcode %}
{% endstep %}

{% step %}
You can directly pull from Hugging Face. You can increase the context to 1M as your RAM/VRAM allows.

Follow this for **general instruction** use-cases:

```bash
./llama.cpp/llama-cli \
    -hf unsloth/Nemotron-3-Nano-30B-A3B-GGUF:UD-Q4_K_XL \
    --ctx-size 32768 \
    --temp 1.0 --top-p 1.0
```

Follow this for **tool-calling** use-cases:

```bash
./llama.cpp/llama-cli \
    -hf unsloth/Nemotron-3-Nano-30B-A3B-GGUF:UD-Q4_K_XL \
    --ctx-size 32768 \
    --temp 0.6 --top-p 0.95
```

{% endstep %}

{% step %}
Download the model via (after installing `pip install huggingface_hub hf_transfer` ). You can choose `UD-Q4_K_XL` or other quantized versions.

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/Nemotron-3-Nano-30B-A3B-GGUF",
    local_dir = "unsloth/Nemotron-3-Nano-30B-A3B-GGUF",
    allow_patterns = ["*UD-Q4_K_XL*"],
)
```

{% endstep %}

{% step %}
Then run the model in conversation mode:

{% code overflow="wrap" %}

```bash
./llama.cpp/llama-cli \
    --model unsloth/Nemotron-3-Nano-30B-A3B-GGUF/Nemotron-3-Nano-30B-A3B-UD-Q4_K_XL.gguf \
    --ctx-size 16384 \
    --seed 3407 \
    --prio 2 \
    --temp 0.6 \
    --top-p 0.95
```

{% endcode %}

Also, adjust **context window** as required. Ensure your hardware can handle more than a 256K context window. Setting it to 1M may trigger CUDA OOM and crash, which is why the default is 262,144.

{% hint style="info" %}
Nemotron 3 uses `<think>` with token ID 12 and `</think>` with token ID 13 for reasoning. Use `--special` to see the tokens for llama.cpp. You might also need `--verbose-prompt` to see `<think>` since it's prepended.
{% endhint %}
{% endstep %}
{% endstepper %}

{% hint style="success" %}
Because the model was trained with **NoPE**, you only need to change `max_position_embeddings`. The model doesn’t use explicit positional embeddings, so **YaRN isn’t needed**.
{% endhint %}

### 🦥 Fine-tuning Nemotron 3 Nano and RL

Unsloth now supports fine-tuning of all Nemotron models, including Nemotron 3 Nano. The 30B model does not fit on a free Colab GPU; however, we still made an 80GB A100 Colab notebook for you to fine-tune with. 16-bit LoRA fine-tuning of Nemotron 3 Nano will use around **60GB VRAM**:

* [Nemotron-3-Nano-30B-A3B SFT LoRA notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Nemotron-3-Nano-30B-A3B_A100.ipynb)

{% embed url="<https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Nemotron-3-Nano-30B-A3B_A100.ipynb>" %}

On fine-tuning MoE's - it's probably not a good idea to fine-tune the router layer so we disabled it by default. If you want to maintain its reasoning capabilities (optional), you can use a mix of direct answers and chain-of-thought examples. Use at least <mark style="background-color:green;">75% reasoning</mark> and <mark style="background-color:green;">25% non-reasoning</mark> in your dataset to make the model retain its reasoning capabilities.

#### :sparkles:Reinforcement Learning + NeMo Gym

We worked with the open-source NVIDIA [NeMo Gym](https://github.com/NVIDIA-NeMo/Gym/pull/492) team to enable the democratization of RL environments. Our collab enables single-turn rollout RL training for many domains of interest, including math, coding, tool-use, etc, using training environments and datasets from NeMo Gym:

* [NeMo Gym Sudoku Reinforcement Learning notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/nemo_gym_sudoku.ipynb)

{% embed url="<https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/NeMo-Gym-Sudoku.ipynb>" %}

* [NeMo Gym Multi Environments for Reinforcement Learning notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/NeMo-Gym-Multi-Environment.ipynb)

{% embed url="<https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/NeMo-Gym-Multi-Environment.ipynb>" %}

{% hint style="success" %}
**Also check out our latest collab guide published on NVIDIA’s official Developer blog:**

#### [How to Fine-Tune an LLM on NVIDIA GPUs With Unsloth](https://blogs.nvidia.com/blog/rtx-ai-garage-fine-tuning-unsloth-dgx-spark/)

{% endhint %}

{% embed url="<https://blogs.nvidia.com/blog/rtx-ai-garage-fine-tuning-unsloth-dgx-spark/>" %}

### :tada:Llama-server serving & deployment

To deploy Nemotron 3 for production, we use `llama-server` In a new terminal say via tmux, deploy the model via:

{% code overflow="wrap" %}

```bash
./llama.cpp/llama-server \
    --model unsloth/Nemotron-3-Nano-30B-A3B-GGUF/Nemotron-3-Nano-30B-A3B-UD-Q4_K_XL.gguf \
    --alias "unsloth/Nemotron-3-Nano-30B-A3B" \
    --prio 3 \
    --min_p 0.01 \
    --temp 0.6 \
    --top-p 0.95 \
    --ctx-size 16384 \
    --port 8001
```

{% endcode %}

When you run the above, you will get:

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2F93hcq5qYJi4BNnkOqgC4%2Fimage.png?alt=media&#x26;token=901aa339-4b1f-4e43-9793-f224edcdb024" alt="" width="563"><figcaption></figcaption></figure>

Then in a new terminal, after doing `pip install openai`, do:

{% code overflow="wrap" %}

```python
from openai import OpenAI
import json
openai_client = OpenAI(
    base_url = "http://127.0.0.1:8001/v1",
    api_key = "sk-no-key-required",
)
completion = openai_client.chat.completions.create(
    model = "unsloth/Nemotron-3-Nano-30B-A3B",
    messages = [{"role": "user", "content": "What is 2+2?"},],
)
print(completion.choices[0].message.content)
```

{% endcode %}

Which will print

{% code overflow="wrap" %}

```
User asks a simple question: "What is 2+2?" The answer is 4. Provide answer.

2 + 2 = 4.
```

{% endcode %}

### Benchmarks

Nemotron-3-Nano-30B-A3B is the best performing model across all benchmarks, including throughput.

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FOVAJmRGUC982jLoOivii%2Faccuracy_chart.png?alt=media&#x26;token=5c090424-087e-46ab-ac03-d3e82d3c2c87" alt=""><figcaption></figcaption></figure>
