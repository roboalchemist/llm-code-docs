# Source: https://unsloth.ai/docs/fr/notions-de-base/troubleshooting-and-faqs/hugging-face-hub-xet-debugging.md

# Source: https://unsloth.ai/docs/de/grundlagen/troubleshooting-and-faqs/hugging-face-hub-xet-debugging.md

# Source: https://unsloth.ai/docs/jp/ji-ben/troubleshooting-and-faqs/hugging-face-hub-xet-debugging.md

# Source: https://unsloth.ai/docs/zh/ji-chu-zhi-shi/troubleshooting-and-faqs/hugging-face-hub-xet-debugging.md

# Source: https://unsloth.ai/docs/basics/troubleshooting-and-faqs/hugging-face-hub-xet-debugging.md

# Hugging Face Hub, XET debugging

#### Downloads are stuck at 90% to 99%

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FAupnur7cpMvilAleA1Gp%2Fimage.png?alt=media&#x26;token=146a3d2e-6c2c-438e-9bf7-6265bc6d6cb4" alt=""><figcaption></figcaption></figure>

If you see downloads via `hf download unsloth/*` get stuck at 90% or 99% of progress for quite some time, cancel the current run, and try adding using below commands:

```bash
pip install -U huggingface_hub

HF_HOME=".cache_new/huggingface" \
HF_XET_CACHE=".cache_new/huggingface/xet" \
HF_HUB_CACHE=".cache_new/huggingface/hub" \
HF_XET_HIGH_PERFORMANCE=1 \
HF_XET_CHUNK_CACHE_SIZE_BYTES=0 \
HF_XET_RECONSTRUCT_WRITE_SEQUENTIALLY=0 \
HF_XET_NUM_CONCURRENT_RANGE_GETS=64 \
hf download unsloth/Qwen3-Coder-Next-GGUF \
    --local-dir unsloth/Qwen3-Coder-Next-GGUF \
    --include "*UD-Q6_K_XL*"
```

#### Rate limited or 429 Too Many Requests?

Try using `snapshot_download` instead, then import Unsloth which will set the correct Hugging Face variables for you:

```python
import unsloth
import os

os.environ["HF_HOME"] = ".cache_new/huggingface"
os.environ["HF_XET_CACHE"] = ".cache_new/huggingface/xet"
os.environ["HF_HUB_CACHE"] = ".cache_new/huggingface/hub"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/Qwen3-Coder-Next-GGUF",
    local_dir = "unsloth/Qwen3-Coder-Next-GGUF",
    allow_patterns = ["*UD-Q6_K_XL*"],
)
```

Or maybe try getting a Hugging Face token first via <https://huggingface.co/settings/tokens>

```bash
pip install -U huggingface_hub

HF_HOME=".cache_new/huggingface" \
HF_XET_CACHE=".cache_new/huggingface/xet" \
HF_HUB_CACHE=".cache_new/huggingface/hub" \
HF_XET_HIGH_PERFORMANCE=1 \
HF_XET_CHUNK_CACHE_SIZE_BYTES=0 \
HF_XET_RECONSTRUCT_WRITE_SEQUENTIALLY=0 \
HF_XET_NUM_CONCURRENT_RANGE_GETS=64 \
    hf download unsloth/Qwen3-Coder-Next-GGUF \
    --local-dir unsloth/Qwen3-Coder-Next-GGUF \
    --include "*UD-Q6_K_XL*" \
    --token "hf_ADD_YOUR_HUGGING_FACE_TOKEN_HERE"
```
