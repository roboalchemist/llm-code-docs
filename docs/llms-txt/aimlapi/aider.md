# Source: https://docs.aimlapi.com/integrations/aider.md

# Aider

## About

[Aider](https://aider.chat/) is a command-line pair programming tool that connects to OpenAI-compatible APIs. It lets you chat with models to edit your codebase, auto-commit changes, and build software collaboratively from the terminal.

This guide explains how to connect **AI/ML API** to **Aider** using the **OpenAI-compatible** flow.\
You’ll get a clean setup with **one endpoint**, support for **slashes in model names**, and **full compatibility** with all chat-completion models.

***

## Quick Setup

<table><thead><tr><th width="248.13323974609375">Field</th><th>Value</th></tr></thead><tbody><tr><td><strong>Base URL</strong></td><td><code>https://api.aimlapi.com/v1</code></td></tr><tr><td><strong>API Key</strong></td><td>Your AI/ML API key (create at <a href="https://aimlapi.com/app/keys">aimlapi.com/app/keys</a>)</td></tr><tr><td><strong>Model</strong></td><td><code>openai/anthropic/claude-3.7-sonnet</code> <em>(openai/&#x3C;your_full_model_id>)</em></td></tr><tr><td><strong>Command Example</strong></td><td><code>aider --model openai/chatgpt-4o-latest</code></td></tr></tbody></table>

{% hint style="success" %}
**Tip:** Always include the `openai/` prefix (case-sensitive) before your model name.

This ensures Aider correctly routes requests to your **AI/ML API** endpoint.
{% endhint %}

***

## Installation

### ✅ Prerequisites

* AI/ML API key
* Python 3.8–3.13 installed
* Internet access to `api.aimlapi.com`
* Aider installed ([Install Guide](https://aider.chat/docs/install.html))

***

### 1️⃣ Install Aider

```bash
python -m pip install aider-install
aider-install
```

<div align="left" data-with-frame="true"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-94f550d343644dce6dfbf1ffcd7f46a3be415ffb%2F%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-22%20133803.png?alt=media" alt=""><figcaption><p><em>Install Aider via terminal</em></p></figcaption></figure></div>

***

### 2️⃣ Configure AI/ML API credentials

**Mac/Linux**

```bash
export OPENAI_API_BASE=https://api.aimlapi.com/v1
export OPENAI_API_KEY=<your_aimlapi_key>
```

**Windows (PowerShell)**

```powershell
setx OPENAI_API_BASE https://api.aimlapi.com/v1
setx OPENAI_API_KEY <your_aimlapi_key>
# restart your terminal
```

***

### 3️⃣ Run Aider with AI/ML API

Move into your project directory:

```bash
cd /to/your/project
```

Then launch Aider with your preferred model:

```bash
# GPT-4o (OpenAI)
aider --model openai/chatgpt-4o-latest

# DeepSeek Chat V3
aider --model openai/deepseek/deepseek-chat

# Claude 3.7 Sonnet
aider --model openai/anthropic/claude-3.7-sonnet

# Gemini 1.5 Pro
aider --model openai/google/gemini-1.5-pro
```

<div align="left" data-with-frame="true"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-52ea2cfbb6e264d26a05a06e29a71d30fa2b9281%2Fimage.png?alt=media" alt="Running Aider with AI/ML API model"><figcaption><p>Running Aider with AI/ML API model</p></figcaption></figure></div>

***

### 4️⃣ Model Prefix Rule

Aider automatically routes requests to your `OPENAI_API_BASE`.\
To connect to **AI/ML API**, **always prefix your model with `openai/`**.

**Pattern:**

```
openai/<provider>/<model-name>
```

**Examples:**

* `openai/chatgpt-4o-latest`
* `openai/deepseek/deepseek-chat`
* `openai/anthropic/claude-3.7-sonnet`
* `openai/google/gemini-1.5-pro`

***

## Example Aider Session

```bash
cd ~/workspace/myapp
aider --model openai/chatgpt-4o-latest
```

Aider will:

1. Load your project map.
2. Analyze the repo.
3. Apply AI-suggested edits.
4. Commit changes automatically.

<div data-with-frame="true"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-929b3459db4fbc7796e1e09cd1170ba6907899c0%2F%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-23%20125950.png?alt=media" alt="Aider researching your repo"><figcaption><p>Aider researching your repo</p></figcaption></figure></div>

<div align="left" data-with-frame="true"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-b3050367a307ad8dad35e2ca9842cd9d06445f64%2F%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-23%20130108.png?alt=media" alt="Aider working on code changes"><figcaption><p><em>Aider working on code changes</em></p></figcaption></figure></div>

***

## Common Pitfalls

* ***Bad request – check parameters*** → verify the model name and prefix
* ***Unknown model*** → confirm it exists in [AI/ML API Models](https://aimlapi.com/models?utm_source=aider\&utm_medium=github\&utm_campaign=integration)
* ***Invalid API key*** → re-copy from [AI/ML API Dashboard](https://aimlapi.com/app/keys)
* ***No response*** → check `OPENAI_API_BASE` and your internet access

***

## 📚 References

* [Dashboard & API Keys](https://aimlapi.com/app)
* [Model Catalog](https://aimlapi.com/models)
* [Aider GitHub](https://github.com/Aider-AI/aider)
* [Aider Installation Docs](https://aider.chat/docs/install.html)
