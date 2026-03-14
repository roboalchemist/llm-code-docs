# Source: https://unsloth.ai/docs/fr/notions-de-base/inference-and-deployment/llama-server-and-openai-endpoint.md

# Source: https://unsloth.ai/docs/de/grundlagen/inference-and-deployment/llama-server-and-openai-endpoint.md

# Source: https://unsloth.ai/docs/jp/ji-ben/inference-and-deployment/llama-server-and-openai-endpoint.md

# Source: https://unsloth.ai/docs/zh/ji-chu-zhi-shi/inference-and-deployment/llama-server-and-openai-endpoint.md

# Source: https://unsloth.ai/docs/basics/inference-and-deployment/llama-server-and-openai-endpoint.md

# llama-server & OpenAI endpoint Deployment Guide

We are doing to deploy Devstral-2 - see [devstral-2](https://unsloth.ai/docs/models/tutorials/devstral-2 "mention") for more details on the model.&#x20;

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

{% hint style="info" %}
When using `--jinja` llama-server appends the following system message if tools are supported: `Respond in JSON format, either with tool_call (a request to call tools) or with response reply to the user's request` . This sometimes causes issues with fine-tunes! See the [llama.cpp repo](https://github.com/ggml-org/llama.cpp/blob/12ee1763a6f6130ce820a366d220bbadff54b818/common/chat.cpp#L849) for more details.
{% endhint %}

First download Devstral 2:

{% code overflow="wrap" %}

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/Devstral-2-123B-Instruct-2512-GGUF",
    local_dir = "Devstral-2-123B-Instruct-2512-GGUF",
    allow_patterns = ["*UD-Q2_K_XL*", "*mmproj-F16*"],
)
```

{% endcode %}

To deploy Devstral 2 for production, we use `llama-server` In a new terminal say via tmux, deploy the model via:

{% code overflow="wrap" %}

```bash
./llama.cpp/llama-server \
    --model Devstral-Small-2-24B-Instruct-2512-GGUF/Devstral-Small-2-24B-Instruct-2512-UD-Q4_K_XL.gguf \
    --mmproj Devstral-Small-2-24B-Instruct-2512-GGUF/mmproj-F16.gguf \
    --alias "unsloth/Devstral-Small-2-24B-Instruct-2512" \
    --threads -1 \
    --n-gpu-layers 999 \
    --prio 3 \
    --min_p 0.01 \
    --ctx-size 16384 \
    --port 8001 \
    --jinja
```

{% endcode %}

When you run the above, you will get:

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FJSTkWDCcHk5DI6otb72X%2Fimage.png?alt=media&#x26;token=b685008e-e9ad-4dea-8f1d-af3fdade8e3b" alt=""><figcaption></figcaption></figure>

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
    model = "unsloth/Devstral-Small-2-24B-Instruct-2512",
    messages = [{"role": "user", "content": "What is 2+2?"},],
)
print(completion.choices[0].message.content)
```

{% endcode %}

Which will simply print 4.\
\
You can go back to the llama-server screen and you might see some statistics which might be interesting:

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2F6msFgOWJEWXEEgXvLRnr%2Fimage.png?alt=media&#x26;token=25fa1784-f671-4e0d-9bad-a4534525afb6" alt=""><figcaption></figcaption></figure>

For arguments like using speculative decoding, see <https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md>

## :grey\_question:Llama-server quirks

* When using `--jinja` llama-server appends the following system message if tools are supported: `Respond in JSON format, either with tool_call (a request to call tools) or with response reply to the user's request` . This sometimes causes issues with fine-tunes! See the [llama.cpp repo](https://github.com/ggml-org/llama.cpp/blob/12ee1763a6f6130ce820a366d220bbadff54b818/common/chat.cpp#L849) for more details.\
  \
  You can stop this by using `--no-jinja` but then `tools` becomes unsupported.\
  \
  For example FunctionGemma by default uses:

  <pre class="language-notebook-python" data-overflow="wrap"><code class="lang-notebook-python">You are a model that can do function calling with the following functions
  </code></pre>

  But because of llama-server appending an extra message, we get:

  <pre class="language-notebook-python" data-overflow="wrap"><code class="lang-notebook-python">You are a model that can do function calling with the following functions\n\nRespond in JSON format, either with `tool_call` (a request to call tools) or with `response` reply to the user's request
  </code></pre>

  We reported the issue to <https://github.com/ggml-org/llama.cpp/issues/18323> and llama.cpp developers are working on a fix!\
  \
  In the meantime, for all fine-tunes, please add the prompt specifically for tool calling!

## :toolbox:Tool Calling with llama-server

See [tool-calling-guide-for-local-llms](https://unsloth.ai/docs/basics/tool-calling-guide-for-local-llms "mention") on how to do tool calling!
