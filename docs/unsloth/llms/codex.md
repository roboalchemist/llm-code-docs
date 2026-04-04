# Source: https://unsloth.ai/docs/fr/notions-de-base/codex.md

# Source: https://unsloth.ai/docs/de/grundlagen/codex.md

# Source: https://unsloth.ai/docs/jp/ji-ben/codex.md

# Source: https://unsloth.ai/docs/zh/ji-chu-zhi-shi/codex.md

# Source: https://unsloth.ai/docs/basics/codex.md

# How to Run Local LLMs with OpenAI Codex

This guide will walk you through connecting open LLMs to the Codex CLI **entirely locally**. It works with any OpenAI or API compatible local model setup including: DeepSeek, Qwen, Gemma, and more.

In this tutorial, we’ll use [GLM-4.7-Flash](https://open-2v.gitbook.com/url/preview/site_mXXTe/~/revisions/NYG3pIjIP3JF6zgJgfjl/models/glm-4.7-flash) (a 30B MoE, agentic + coding model) which fits nicely on a 24GB RAM/unified memory device to autonomously fine-tune an LLM using [Unsloth](https://github.com/unslothai/unsloth). Prefer a different model? Swap in [any other model](https://open-2v.gitbook.com/url/preview/site_mXXTe/~/revisions/NYG3pIjIP3JF6zgJgfjl/models/tutorials) by updating the model names in the scripts.

<a href="#openai-codex-cli-tutorial" class="button primary" data-icon="openai">OpenAI Codex Tutorial</a>

For model quants, we’ll use Unsloth [Dynamic GGUFs](https://open-2v.gitbook.com/url/preview/site_mXXTe/~/revisions/NYG3pIjIP3JF6zgJgfjl/basics/unsloth-dynamic-2.0-ggufs) so you can run quantized GGUF models while preserving as much quality as possible.

We’ll use [`llama.cpp`](https://github.com/ggml-org/llama.cpp), an open-source runtime for running LLMs on macOS, Linux, and Windows. Its `llama-server` component lets you serve models efficiently via a single **OpenAI-compatible** HTTP endpoint. In this setup, the model is served on **port 8001**, and all agent tool calls are routed through that one endpoint.

### 📖 #1: Setup Tutorial

{% stepper %}
{% step %}

#### Install llama.cpp

We need to install `llama.cpp` to deploy/serve local LLMs to use in Codex etc. We follow the official build instructions for correct GPU bindings and maximum performance. Change `-DGGML_CUDA=ON` to `-DGGML_CUDA=OFF` if you don't have a GPU or just want CPU inference. **For Apple Mac / Metal devices**, set `-DGGML_CUDA=OFF` then continue as usual - Metal support is on by default.

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev git-all -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2F4DmycqgjxOz6TOQd9PLJ%2Fimage.png?alt=media&#x26;token=c94db0b5-8e4a-4043-b2a3-c68bad93213e" alt="" width="563"><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Download and use models locally

Download the model via `huggingface_hub` in Python (after installing via `pip install huggingface_hub hf_transfer`). We use the **UD-Q4\_K\_XL** quant for the best size/accuracy balance. You can find all Unsloth GGUF uploads in our [Collection here](https://unsloth.ai/docs/get-started/unsloth-model-catalog). If downloads get stuck, see [hugging-face-hub-xet-debugging](https://unsloth.ai/docs/basics/troubleshooting-and-faqs/hugging-face-hub-xet-debugging "mention")

{% hint style="success" %}
We used `unsloth/GLM-4.7-Flash-GGUF` , but you can use anything like `unsloth/Qwen3-Coder-Next-GGUF` - see [qwen3-coder-next](https://unsloth.ai/docs/models/qwen3-coder-next "mention")
{% endhint %}

```python
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download

snapshot_download(
    repo_id = "unsloth/GLM-4.7-Flash-GGUF",
    local_dir = "unsloth/GLM-4.7-Flash-GGUF",
    allow_patterns = ["*UD-Q4_K_XL*"],
)
```

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FxlIrQGQ0cevb1ckkSFy5%2Fimage.png?alt=media&#x26;token=b1a42562-927a-4ad2-85f8-29c2993c46aa" alt="" width="563"><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Start the Llama-server

To deploy GLM-4.7-Flash for agentic workloads, we use `llama-server`. We apply Z.ai's recommended sampling parameters (`temp 1.0`, `top_p 0.95`) and enable `--jinja` for proper tool calling support.

Run this command in a new terminal (use `tmux` or open a new terminal). The below should **fit perfectly in a 24GB GPU (RTX 4090) (uses 23GB)** `--fit on` will also auto offload, but if you see bad performance, reduce `--ctx-size` . We used `--cache-type-k q8_0 --cache-type-v q8_0` for KV cache quantization to reduce VRAM usage.

```bash
./llama.cpp/llama-server \
    --model unsloth/GLM-4.7-Flash-GGUF/GLM-4.7-Flash-UD-Q4_K_XL.gguf \
    --alias "unsloth/GLM-4.7-Flash" \
    --temp 1.0 \
    --top-p 0.95 \
    --min-p 0.01 \
    --port 8001 \
    --kv-unified \
    --cache-type-k q8_0 --cache-type-v q8_0 \
    --flash-attn on \
    --batch-size 4096 --ubatch-size 1024 \
    --ctx-size 131072
```

{% hint style="success" %}
You can also disable thinking for GLM-4.7-Flash which can improve performance for agentic coding stuff. To disable thinking with llama.cpp add this to the llama-server command:

`--chat-template-kwargs "{\"enable_thinking\": false}"`

<img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FyKf6guCV8snRaAV16Zxc%2FG_16XLgXUAEnSWH.jpg?alt=media&#x26;token=3b557c6d-3f6f-4515-ba9f-4cc8b50bcef1" alt="" data-size="original">
{% endhint %}
{% endstep %}
{% endstepper %}

## <i class="fa-openai">:openai:</i> OpenAI Codex CLI Tutorial

[Codex ](https://github.com/openai/codex)is OpenAI's official coding agent that runs locally. While designed for ChatGPT, it supports custom API endpoints, making it perfect for local LLMs. For installing on [Windows](https://developers.openai.com/codex/windows/) - it's best to use WSL.

#### **Install**

**Mac (Homebrew):**

```bash
brew install --cask codex
```

**Universal (NPM) for Linux**

```bash
apt update
apt install nodejs npm -y
npm install -g @openai/codex
```

**Configure**

First run `codex` to login and setup things, then create or edit the configuration file at `~/.codex/config.toml` (Mac/Linux) or `%USERPROFILE%\.codex\config.toml` (Windows).

Use `cat > ~/.codex/config.toml` for Linux / Mac:

```toml
[model_providers.llama_cpp]
name = "llama_cpp API"
base_url = "http://localhost:8001/v1"
wire_api = "responses"
stream_idle_timeout_ms = 10000000
```

Navigate to your project folder (`mkdir project ; cd project`) and run:

```bash
codex --model unsloth/GLM-4.7-Flash -c model_provider=llama_cpp --search
```

Or to allow any code to execute. **(BEWARE this will make Codex do and execute code however it likes without any approvals!)**

{% code overflow="wrap" %}

```bash
codex --model unsloth/GLM-4.7-Flash -c model_provider=llama_cpp --search --dangerously-bypass-approvals-and-sandbox
```

{% endcode %}

And you will see:

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FiTjL7DtyNg0GREwR7p54%2Fimage.png?alt=media&#x26;token=9f793df2-e91b-4631-a7c8-00e659fd1a07" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
OpenAI's Codex is removing `wire_api = "chat"` support it seems - it still works as of January 29th 2026. We should switch to `wire_api = "responses"` but it keeps error-ing out with: `{"error":{"code":400,"message":"'type' of tool must be 'function'","type":"invalid_request_error"}}`
{% endhint %}

Try this prompt to install and run a simple Unsloth finetune:

{% code overflow="wrap" %}

```
You can only work in the cwd project/. Do not search for AGENTS.md - this is it. Install Unsloth via a virtual environment via uv. See https://unsloth.ai/docs/get-started/install/pip-install on how (get it and read). Then do a simple Unsloth finetuning run described in https://github.com/unslothai/unsloth. You have access to 1 GPU.
```

{% endcode %}

and you will see:

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fg2R9WPuNRNUUFnPRXE2F%2Fimage.png?alt=media&#x26;token=686f4be8-7a50-4f6b-86cb-327cec36de81" alt=""><figcaption></figcaption></figure>

and if we wait a little longer, we finally get:

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FHTKt5sGFpkYzS8DlM9E7%2Fimage.png?alt=media&#x26;token=f4fa2e27-10d7-4c4e-8af0-448170336af9" alt=""><figcaption></figcaption></figure>
