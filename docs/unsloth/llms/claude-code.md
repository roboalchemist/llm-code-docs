# Source: https://unsloth.ai/docs/fr/notions-de-base/claude-code.md

# Source: https://unsloth.ai/docs/de/grundlagen/claude-code.md

# Source: https://unsloth.ai/docs/jp/ji-ben/claude-code.md

# Source: https://unsloth.ai/docs/zh/ji-chu-zhi-shi/claude-code.md

# Source: https://unsloth.ai/docs/basics/claude-code.md

# How to Run Local LLMs with Claude Code

This step-by-step guide shows you how to connect open LLMs and APIs to Claude Code entirely locally, complete with screenshots. Run using any open model like Qwen3.5, DeepSeek and Gemma.

For this tutorial, we’ll use [**Qwen3.5**](https://unsloth.ai/docs/models/qwen3.5) and [GLM-4.7-Flash](https://unsloth.ai/docs/models/glm-4.7-flash). Both are the strongest 35B MoE agentic & coding model as of Mar 2026 (which works great on a 24GB RAM/unified mem device) to autonomously fine-tune an LLM with [Unsloth](https://github.com/unslothai/unsloth). You can swap in [any other model](https://unsloth.ai/docs/models/tutorials), just update the model names in your scripts.

<a href="#qwen3.5-tutorial" class="button secondary">Qwen3.5 Tutorial</a><a href="#glm-4.7-flash-tutorial" class="button secondary">GLM-4.7-Flash Tutorial</a><a href="#claude-code-tutorial" class="button primary" data-icon="claude">Claude Code Tutorial</a>

For model quants, we will utilize Unsloth [Dynamic GGUFs](https://unsloth.ai/docs/basics/unsloth-dynamic-2.0-ggufs) to run any LLM quantized, while retaining as much accuracy as possible.

{% hint style="info" %}
Claude Code has changed quite a lot since Jan 2026. There are lots more settings and necessary features you will need to toggle.
{% endhint %}

## 📖 LLM Setup Tutorials

Before we begin, we firstly need to complete setup for the specific model you're going to use. We use `llama.cpp` which is an open-source framework for running LLMs on your Mac, Linux, Windows etc. devices. Llama.cpp contains `llama-server` which allows you to serve and deploy LLMs efficiently. The model will be served on port 8001, with all agent tools routed through a single OpenAI-compatible endpoint.&#x20;

### Qwen3.5 Tutorial

We'll be using [Qwen3.5](https://unsloth.ai/docs/models/qwen3.5)-35B-A3B and specific settings for fast accurate coding tasks. If you don't have enough VRAM and want a **smarter** model, **Qwen3.5-27B** is a great choice, but it will be \~2x slower, or you can use other Qwen3.5 variants like 9B, 4B or 2B.

{% hint style="info" %}
Use Qwen3.5-27B if you want a **smarter** model or if you don't have enough VRAM. It will be \~2x slower than 35B-A3B however. Or you can use [**Qwen3-Coder-Next**](https://unsloth.ai/docs/models/qwen3-coder-next) which is fantastic if you have enough VRAM.
{% endhint %}

{% stepper %}
{% step %}

#### Install llama.cpp

We need to install `llama.cpp` to deploy/serve local LLMs to use in Claude Code etc. We follow the official build instructions for correct GPU bindings and maximum performance. Change `-DGGML_CUDA=ON` to `-DGGML_CUDA=OFF` if you don't have a GPU or just want CPU inference. **For Apple Mac / Metal devices**, set `-DGGML_CUDA=OFF` then continue as usual - Metal support is on by default.

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

```bash
hf download unsloth/Qwen3.5-35B-A3B-GGUF \
    --local-dir unsloth/Qwen3.5-35B-A3B-GGUF \
    --include "*UD-Q4_K_XL*" # Use "*UD-Q2_K_XL*" for Dynamic 2bit
```

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FRfXofrNzl1ypjfMTz15o%2Fimage.png?alt=media&#x26;token=8009de90-cd11-46ed-85b5-fca5c07b66fc" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
We used `unsloth/Qwen3.5-35B-A3B-GGUF` , but you can use another variant like 27B or any other model like `unsloth/`[`Qwen3-Coder-Next`](https://unsloth.ai/docs/models/qwen3-coder-next)`-GGUF`.
{% endhint %}

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FxlIrQGQ0cevb1ckkSFy5%2Fimage.png?alt=media&#x26;token=b1a42562-927a-4ad2-85f8-29c2993c46aa" alt="" width="563"><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Start the Llama-server

To deploy Qwen3.5 for agentic workloads, we use `llama-server`. We apply [Qwen's recommended sampling parameters](https://unsloth.ai/docs/models/qwen3.5#recommended-settings) for thinking mode: `temp 0.6`, `top_p 0.95` , `top-k 20`. Keep in mind these numbers change if you use non-thinking mode or other tasks.

Run this command in a new terminal (use `tmux` or open a new terminal). The below should **fit perfectly in a 24GB GPU (RTX 4090) (uses 23GB)** `--fit on` will also auto offload, but if you see bad performance, reduce `--ctx-size` .

{% hint style="danger" %}
We used `--cache-type-k q8_0 --cache-type-v q8_0` for KV cache quantization for less VRAM usage. For full precision, use `--cache-type-k bf16 --cache-type-v bf16` According to multiple reports, Qwen3.5 degrades accuracy with `f16` KV cache, so do not use `--cache-type-k f16 --cache-type-v f16` which is also on by default in llama.cpp. Note bf16 KV Cache might be slightly slower on some machines.
{% endhint %}

```bash
./llama.cpp/llama-server \
    --model unsloth/Qwen3.5-35B-A3B-GGUF/Qwen3.5-35B-A3B-UD-Q4_K_XL.gguf \
    --alias "unsloth/Qwen3.5-35B-A3B" \
    --temp 0.6 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.00 \
    --port 8001 \
    --kv-unified \
    --cache-type-k q8_0 --cache-type-v q8_0 \
    --flash-attn on --fit on \
    --ctx-size 131072 # change as required
```

{% hint style="success" %}
You can also disable thinking for Qwen3.5 which can improve performance for agentic coding stuff. To disable thinking with llama.cpp add this to the llama-server command:

`--chat-template-kwargs "{\"enable_thinking\": false}"`

<img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2F373wtRRbMcobtjV5e6xf%2Fkerkekke.png?alt=media&#x26;token=2cd3b8c7-93b6-41cb-8bce-41f1aee819eb" alt="" data-size="original">
{% endhint %}
{% endstep %}
{% endstepper %}

### GLM-4.7-Flash Tutorial

{% stepper %}
{% step %}

#### Install llama.cpp

We need to install `llama.cpp` to deploy/serve local LLMs to use in Claude Code etc. We follow the official build instructions for correct GPU bindings and maximum performance. Change `-DGGML_CUDA=ON` to `-DGGML_CUDA=OFF` if you don't have a GPU or just want CPU inference. **For Apple Mac / Metal devices**, set `-DGGML_CUDA=OFF` then continue as usual - Metal support is on by default.

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

To deploy GLM-4.7-Flash for agentic workloads, we use `llama-server`. We apply Z.ai's recommended sampling parameters (`temp 1.0`, `top_p 0.95`).

Run this command in a new terminal (use `tmux` or open a new terminal). The below should **fit perfectly in a 24GB GPU (RTX 4090) (uses 23GB)** `--fit on` will also auto offload, but if you see bad performance, reduce `--ctx-size` .

{% hint style="danger" %}
We used `--cache-type-k q8_0 --cache-type-v q8_0` for KV cache quantization to reduce VRAM usage. If you see reduced quality, instead you can use `bf16` but it will increase VRAM use by twice: `--cache-type-k bf16 --cache-type-v bf16`
{% endhint %}

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
    --flash-attn on --fit on \
    --batch-size 4096 --ubatch-size 1024 \
    --ctx-size 131072 #change as required
```

{% hint style="success" %}
You can also disable thinking for GLM-4.7-Flash which can improve performance for agentic coding stuff. To disable thinking with llama.cpp add this to the llama-server command:

`--chat-template-kwargs "{\"enable_thinking\": false}"`

<img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FyKf6guCV8snRaAV16Zxc%2FG_16XLgXUAEnSWH.jpg?alt=media&#x26;token=3b557c6d-3f6f-4515-ba9f-4cc8b50bcef1" alt="" data-size="original">
{% endhint %}
{% endstep %}
{% endstepper %}

## <i class="fa-claude">:claude:</i> Claude Code Tutorial

{% hint style="danger" %}
See [#fixing-90-slower-inference-in-claude-code](#fixing-90-slower-inference-in-claude-code "mention") after installing Claude Code to fix open models being 90% slower due to KV Cache invalidation.
{% endhint %}

Once you are done doing the first steps of setting up your local LLM, it's time to setup Claude Code. Claude Code is Anthropic's agentic coding tool that lives in your terminal, understands your codebase, and handles complex Git workflows via natural language.

#### **Install Claude Code and run it locally**

{% tabs %}
{% tab title="Mac / Linux Setups" %}

```bash
curl -fsSL https://claude.ai/install.sh | bash
# Or via Homebrew: brew install --cask claude-code
```

**Configure**

Set the `ANTHROPIC_BASE_URL` environment variable to redirect Claude Code to your local `llama.cpp` server.

```bash
export ANTHROPIC_BASE_URL="http://localhost:8001"
```

Also you might need to set `ANTHROPIC_API_KEY` depending on the server. For example:

```bash
export ANTHROPIC_API_KEY='sk-no-key-required' ## or 'sk-1234'
```

**Session vs Persistent:** The commands above apply to the current terminal only. To persist across new terminals:

Add the `export` line to `~/.bashrc` (bash) or `~/.zshrc` (zsh).

{% hint style="warning" %}
If you see `Unable to connect to API (ConnectionRefused)` , remember to unset `ANTHROPIC_BASE_URL`  via `unset ANTHROPIC_BASE_URL`
{% endhint %}

**Missing API key**

If you see this, set `export ANTHROPIC_API_KEY='sk-no-key-required' ## or 'sk-1234'`

{% hint style="info" %}
If Claude Code still asks you to sign in on first run, add `"hasCompletedOnboarding": true` and `"primaryApiKey": "sk-dummy-key"` to `~/.claude.json`. For the VS Code extension, also enable **Disable Login Prompt** in settings (or add `"claudeCode.disableLoginPrompt": true` to `settings.json`).
{% endhint %}
{% endtab %}

{% tab title="Windows Setups" %}
Use Powershell for all commands below:

```powershell
irm https://claude.ai/install.ps1 | iex
```

**Configure**

Set the `ANTHROPIC_BASE_URL` environment variable to redirect Claude Code to your local `llama.cpp` server.  Also you must use `$env:CLAUDE_CODE_ATTRIBUTION_HEADER=0` see below.

```powershell
$env:ANTHROPIC_BASE_URL="http://localhost:8001"
```

{% hint style="danger" %}
Claude Code recently prepends and changes a Claude Code Attribution header, which invalidates the KV Cache. See this [LocalLlama discussion](https://www.reddit.com/r/LocalLLaMA/comments/1r47fz0/claude_code_with_local_models_full_prompt/).

To solve this, do `$env:CLAUDE_CODE_ATTRIBUTION_HEADER=0` or edit `~/.claude/settings.json` with:

```
{
    ...
    "env": {
        "CLAUDE_CODE_ATTRIBUTION_HEADER" : "0",
        ...
    }
}
```

{% endhint %}

**Session vs Persistent:** The commands above apply to the current terminal only. To persist across new terminals:

Run `setx ANTHROPIC_BASE_URL "http://localhost:8001"` once, or add the `$env:` line to your `$PROFILE`.

{% hint style="info" %}
If Claude Code still asks you to sign in on first run, add `"hasCompletedOnboarding": true` and `"primaryApiKey": "sk-dummy-key"` to `~/.claude.json`. For the VS Code extension, also enable **Disable Login Prompt** in settings (or add `"claudeCode.disableLoginPrompt": true` to `settings.json`).
{% endhint %}
{% endtab %}
{% endtabs %}

### :detective:Fixing 90% slower inference in Claude Code

{% hint style="danger" %}
Claude Code recently prepends and adds a Claude Code Attribution header, which **invalidates the KV Cache, making inference 90% slower with local models**. See this [LocalLlama discussion](https://www.reddit.com/r/LocalLLaMA/comments/1r47fz0/claude_code_with_local_models_full_prompt/).
{% endhint %}

To solve this, edit `~/.claude/settings.json` to include `CLAUDE_CODE_ATTRIBUTION_HEADER` and set it to 0 within `"env"`

{% hint style="info" %}
Using `export CLAUDE_CODE_ATTRIBUTION_HEADER=0` **DOES NOT** work!
{% endhint %}

For example do `cat > ~/.claude/settings.json` then add the below (when pasted, do ENTER then CTRL+D to save it). If you have a previous `~/.claude/settings.json` file, just add `"CLAUDE_CODE_ATTRIBUTION_HEADER" : "0"` to the "env" section, and leave the rest of the settings file unchanged.

<pre><code>{
  "promptSuggestionEnabled": false,
  "env": {
    "CLAUDE_CODE_ENABLE_TELEMETRY": "0",
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
    <a data-footnote-ref href="#user-content-fn-1">"CLAUDE_CODE_ATTRIBUTION_HEADER" : "0"</a>
  },
  "attribution": {
    "commit": "",
    "pr": ""
  },
  "plansDirectory" : "./plans",
  "prefersReducedMotion" : true,
  "terminalProgressBarEnabled" : false,
  "effortLevel" : "high"
}
</code></pre>

#### :star2:Running Claude Code locally on Linux / Mac / Windows

{% hint style="success" %}
We used `unsloth/GLM-4.7-Flash-GGUF` , but you can use anything like `unsloth/Qwen3.5-35B-A3B-GGUF`.
{% endhint %}

{% hint style="danger" %}
See [#fixing-90-slower-inference-in-claude-code](#fixing-90-slower-inference-in-claude-code "mention") first to fix open models being 90% slower due to KV Cache invalidation.
{% endhint %}

Navigate to your project folder (`mkdir project ; cd project`) and run:

```bash
claude --model unsloth/GLM-4.7-Flash
```

To use Qwen3.5-35B-A3B, simply change it to:

```bash
claude --model unsloth/Qwen3.5-35B-A3B
```

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fnyc5BnXQiXPRZnyuYZt3%2Fimage.png?alt=media&#x26;token=72011cb6-abed-4a41-99b0-104ef5d0111f" alt=""><figcaption></figcaption></figure>

To set Claude Code to execute commands without any approvals do **(BEWARE this will make Claude Code do and execute code however it likes without any approvals!)**

{% code overflow="wrap" %}

```bash
claude --model unsloth/GLM-4.7-Flash --dangerously-skip-permissions
```

{% endcode %}

Try this prompt to install and run a simple Unsloth finetune:

{% code overflow="wrap" %}

```
You can only work in the cwd project/. Do not search for CLAUDE.md - this is it. Install Unsloth via a virtual environment via uv. Use `python -m venv unsloth_env` then `source unsloth_env/bin/activate` if possible. See https://unsloth.ai/docs/get-started/install/pip-install on how (get it and read). Then do a simple Unsloth finetuning run described in https://github.com/unslothai/unsloth. You have access to 1 GPU.
```

{% endcode %}

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FBkpEsVssYZG9wHvvWMRH%2Fimage.png?alt=media&#x26;token=e1a8283f-49ed-4b78-8052-d8970f069d5b" alt=""><figcaption></figcaption></figure>

After waiting a bit, Unsloth will be installed in a venv via uv, and loaded up:

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FHATFwDrR1gP44XFbzWcv%2Fimage.png?alt=media&#x26;token=6ff63733-686d-4b08-bdd5-66a6fa4aa34c" alt=""><figcaption></figcaption></figure>

and finally you will see a successfully finetuned model with Unsloth!

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FZjQ6askaixcYOMrr2qMi%2Fimage.png?alt=media&#x26;token=e0e0047d-b6a2-421f-a86b-68e093a3a17a" alt=""><figcaption></figcaption></figure>

**IDE Extension (VS Code / Cursor)**

You can also use Claude Code directly inside your editor via the official extension:

* [Install for VS Code](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)
* [Install for Cursor](cursor:extension/anthropic.claude-code)
* [Claude Code in VS Code docs](https://code.claude.com/docs/en/vs-code)

Alternatively, press `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (Mac), search for **Claude Code**, and click **Install**.

{% hint style="warning" %}
If you see `Unable to connect to API (ConnectionRefused)` , remember to unset `ANTHROPIC_BASE_URL`  via `unset ANTHROPIC_BASE_URL`
{% endhint %}

{% hint style="danger" %}
If you find open models to be 90% slower, see [#claude-code-90-slower-inference](#claude-code-90-slower-inference "mention") first to fix KV cache being invalidated.
{% endhint %}

[^1]: Must use this!
