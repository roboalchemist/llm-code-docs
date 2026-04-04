# Source: https://unsloth.ai/docs/fr/modeles/nemotron-3-super.md

# Source: https://unsloth.ai/docs/de/modelle/nemotron-3-super.md

# Source: https://unsloth.ai/docs/jp/moderu/nemotron-3-super.md

# Source: https://unsloth.ai/docs/zh/mo-xing/nemotron-3-super.md

# Source: https://unsloth.ai/docs/models/nemotron-3-super.md

# NVIDIA Nemotron-3-Super: How To Run Guide

NVIDIA releases **Nemotron-3-Super-120B-A12B**, a 120B open hybrid reasoning MoE model with 12B active parameters, following the earlier launch of [Nemotron-3-Nano](https://unsloth.ai/docs/models/tutorials/nemotron-3), its 30B counterpart. Nemotron-3-Super is designed for high efficiency and accuracy for multi-agent AI. With a **1M-token** context window, it leads its size class on AIME 2025, Terminal Bench and SWE-Bench Verified benchmarks, while achieving the highest throughput.

Nemotron-3-Super runs on a device with **64GB** of RAM, VRAM, or unified memory and can now be fine-tuned locally. Thanks NVIDIA for giving Unsloth day-zero support.

<a href="../tutorials/nemotron-3#run-nemotron-3-super-120b" class="button primary">Nemotron 3 Super</a><a href="tutorials/nemotron-3" class="button secondary">Nemotron 3 Nano</a>

GGUF: [NVIDIA-Nemotron-3-Super-**120B-A12B**-GGUF](https://huggingface.co/unsloth/NVIDIA-Nemotron-3-Super-120B-A12B-GGUF)

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

### 🖥️ Run Nemotron-3-Super-120B-A12B

Depending on your use-case you will need to use different settings. Some GGUFs end up similar in size because the model architecture (like [gpt-oss](https://unsloth.ai/docs/models/gpt-oss-how-to-run-and-fine-tune)) has dimensions not divisible by 128, so parts can’t be quantized to lower bits. Access GGUFs [here](https://huggingface.co/unsloth/NVIDIA-Nemotron-3-Super-120B-A12B-GGUF).

The 4-bit versions of the model requires \~64GB RAM - 72GB RAM. 8-bit requires 128GB.

#### Llama.cpp Tutorial (GGUF):

Instructions to run in llama.cpp (note we will be using 4-bit to fit most devices):

{% stepper %}
{% step %}
Obtain the latest `llama.cpp` on [GitHub here](https://github.com/ggml-org/llama.cpp). You can follow the build instructions below as well. Change `-DGGML_CUDA=ON` to `-DGGML_CUDA=OFF` if you don't have a GPU or just want CPU inference.

{% hint style="warning" %}
We will need to install Unsloth's llama.cpp branch for Nemotron-3-Super! This is not necessary for LM Studio, as it'll work with an update.
{% endhint %}

{% code overflow="wrap" %}

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/unslothai/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON
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
    -hf unsloth/NVIDIA-Nemotron-3-Super-120B-A12B-GGUF:UD-Q3_K_XL \
    --ctx-size 16384 \
    --temp 1.0 --top-p 1.0
```

Follow this for **tool-calling** use-cases:

```bash
./llama.cpp/llama-cli \
    -hf unsloth/NVIDIA-Nemotron-3-Super-120B-A12B-GGUF:UD-Q3_K_XL \
    --ctx-size 32768 \
    --temp 0.6 --top-p 0.95
```

{% endstep %}

{% step %}
Download the model via (after installing `pip install huggingface_hub hf_transfer` ). You can choose Q4\_K\_M or other quantized versions like `UD-Q4_K_XL` . We recommend using at least 2-bit dynamic quant `UD-Q2_K_XL` to balance size and accuracy. If downloads get stuck, see: [hugging-face-hub-xet-debugging](https://unsloth.ai/docs/basics/troubleshooting-and-faqs/hugging-face-hub-xet-debugging "mention")

```bash
hf download unsloth/NVIDIA-Nemotron-3-Super-120B-A12B-GGUF \
    --local-dir unsloth/NVIDIA-Nemotron-3-Super-120B-A12B-GGUF \
    --include "*UD-Q3_K_XL*" # Use "*UD-Q2_K_XL*" for Dynamic 2bit
```

{% endstep %}

{% step %}
Then run the model in conversation mode:

{% code overflow="wrap" %}

```bash
/llama.cpp/llama-cli \
    --model unsloth/NVIDIA-Nemotron-3-Super-120B-A12B-GGUF/UD-Q3_K_XL/NVIDIA-Nemotron-3-Super-120B-A12B-UD-Q3_K_XL-00001-of-00003.gguf \
    --ctx-size 16384 \
    --seed 3407 \
    --prio 2 \
    --temp 0.6 \
    --top-p 0.95
```

{% endcode %}

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FiGf05CCDNnMGE9g7KtqE%2Fimage.png?alt=media&#x26;token=24cd05c6-4fd5-4e9b-9057-822fe27bf255" alt=""><figcaption></figcaption></figure>

Also, adjust **context window** as required. Ensure your hardware can handle more than a 256K context window. Setting it to 1M may trigger CUDA OOM and crash, which is why the default is 262,144.
{% endstep %}
{% endstepper %}

### 🦥 Fine-tuning Nemotron 3 and RL

Unsloth now supports fine-tuning of all Nemotron models, including Nemotron 3 Super and Nano. For notebook examples of Nano, see our Nemotron 3 [Nano fine-tuning guide](https://unsloth.ai/docs/models/tutorials/nemotron-3).

#### Nemotron 3 Super

* Router-layer fine-tuning is disabled by default for stability.
* Nemotron-3-Super-120B - bf16 LoRA works on 256GB VRAM. If you're using multiGPUs, add     `device_map = "balanced"` or follow our [multiGPU Guide](https://unsloth.ai/docs/basics/multi-gpu-training-with-unsloth).

### 🦙Llama-server serving & deployment

To deploy Nemotron 3 for production, we use `llama-server` In a new terminal say via tmux, deploy the model via:

{% code overflow="wrap" %}

```bash
./llama.cpp/llama-server \
    --model unsloth/NVIDIA-Nemotron-3-Super-120B-A12B-GGUF/UD-Q3_K_XL/NVIDIA-Nemotron-3-Super-120B-A12B-UD-Q3_K_XL-00001-of-00003.gguf \
    --alias "unsloth/NVIDIA-Nemotron-3-Super-120B-A12B" \
    --prio 3 \
    --min_p 0.01 \
    --temp 0.6 \
    --top-p 0.95 \
    --ctx-size 16384 \
    --port 8001
```

{% endcode %}

When you run the above, you will get:

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FfEwDrf2FRCuWV7t7i7L6%2Fimage.png?alt=media&#x26;token=e2449552-27f5-4238-9e09-c708377a4e61" alt=""><figcaption></figcaption></figure>

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
    model = "unsloth/NVIDIA-Nemotron-3-Super-120B-A12B",
    messages = [{"role": "user", "content": "What is 2+2?"},],
)
print(completion.choices[0].message.reasoning_content)
print(completion.choices[0].message.content)
```

{% endcode %}

Which will print

{% code overflow="wrap" %}

```
Okay, the user asked "What is 2+2?" This seems like a very basic arithmetic question.

Hmm, maybe they're testing if I'm paying attention, or perhaps they're a young child learning math. Could also be someone checking if I'll overcomplicate a simple question.

I should keep it straightforward since there's no indication of trickery in the query. The answer is definitely 4 - no need to second-guess basic addition.

Though part of me wonders if they're setting up for a joke (like "2+2=5 for large values of 2"), but since they didn't suggest any context, I'll assume genuine inquiry.

Better to answer clearly and warmly - might encourage them to ask more questions if they're learning. No need for fluff though; just state the fact helpfully.

2 + 2 equals **4**.

This is a fundamental arithmetic fact in base-10 (decimal) notation. If you're asking in a different context (like modular arithmetic, binary, or a joke/reference), feel free to clarify—I'm happy to adapt! 😊
```

{% endcode %}

### Benchmarks

Compared to similar sized models, Nemotron 3 Super performs competitively, while providing highest throughput.

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fe2p2jCqKu7D9pTtJpOQN%2Faccuracy_chart(1).png?alt=media&#x26;token=df1805ab-f005-4a7f-bd77-b91f84a2c76f" alt=""><figcaption></figcaption></figure>
