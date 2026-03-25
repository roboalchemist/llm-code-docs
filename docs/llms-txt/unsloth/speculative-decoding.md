# Source: https://unsloth.ai/docs/fr/notions-de-base/inference-and-deployment/saving-to-gguf/speculative-decoding.md

# Source: https://unsloth.ai/docs/de/grundlagen/inference-and-deployment/saving-to-gguf/speculative-decoding.md

# Source: https://unsloth.ai/docs/jp/ji-ben/inference-and-deployment/saving-to-gguf/speculative-decoding.md

# Source: https://unsloth.ai/docs/zh/ji-chu-zhi-shi/inference-and-deployment/saving-to-gguf/speculative-decoding.md

# Source: https://unsloth.ai/docs/basics/inference-and-deployment/saving-to-gguf/speculative-decoding.md

# Speculative Decoding

## :llama:Speculative Decoding in llama.cpp, llama-server

Speculative decoding in llama.cpp can be easily enabled via `llama-cli` and `llama-server` via the `--model-draft` argument. Note you must have a draft model, which generally is a smaller model, but it must have the same tokenizer&#x20;

### Spec Decoding for GLM 4.7

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "0" # Can sometimes rate limit, so set to 0 to disable
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/GLM-4.7-GGUF",
    local_dir = "unsloth/GLM-4.7-GGUF",
    allow_patterns = ["*UD-Q2_K_XL*"], # Dynamic 2bit Use "*UD-TQ1_0*" for Dynamic 1bit
)
snapshot_download(
    repo_id = "unsloth/GLM-4.5-Air-GGUF",
    local_dir = "unsloth/GLM-4.5-Air-GGUF",
    allow_patterns = ["*UD-Q4_K_XL*"], # Dynamic 4bit. Use "*UD-TQ1_0*" for Dynamic 1bit
)
```

{% code overflow="wrap" %}

```bash
./llama.cpp/llama-cli \
    --model unsloth/GLM-4.7-GGUF/UD-Q2_K_XL/GLM-4.7-UD-Q2_K_XL-00001-of-00003.gguf \
    --threads -1 \
    --fit on \
    --prio 3 \
    --temp 1.0 \
    --top-p 0.95 \
    --ctx-size 16384 \
    --jinja
```

{% endcode %}

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FI8FIkJIoIFQoJRaH1emk%2Fimage.png?alt=media&#x26;token=8c12ab2a-380f-4f3a-9b65-b0a7421f473a" alt=""><figcaption></figcaption></figure>

{% code overflow="wrap" %}

```bash
./llama.cpp/llama-cli \
    --model unsloth/GLM-4.7-GGUF/UD-Q2_K_XL/GLM-4.7-UD-Q2_K_XL-00001-of-00003.gguf \
    --model-draft unsloth/GLM-4.5-Air-GGUF/UD-Q4_K_XL/GLM-4.5-Air-UD-Q4_K_XL-00001-of-00002.gguf \
    --threads -1 \
    --fit on \
    --prio 3 \
    --temp 1.0 \
    --top-p 0.95 \
    --ctx-size 16384 \
    --ctx-size-draft 16384 \
    --jinja \
    --device CUDA0 \
    --device-draft CUDA0,CUDA1
```

{% endcode %}

{% code overflow="wrap" %}

```bash
./llama.cpp/llama-server \
    --model unsloth/GLM-4.7-GGUF/UD-Q2_K_XL/GLM-4.7-UD-Q2_K_XL-00001-of-00003.gguf \
    --alias "unsloth/GLM-4.7" \
    --threads -1 \
    --fit on \
    --prio 3 \
    --temp 1.0 \
    --top-p 0.95 \
    --ctx-size 16384 \
    --port 8001 \
    --jinja
```

{% endcode %}
