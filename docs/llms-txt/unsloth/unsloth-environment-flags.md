# Source: https://unsloth.ai/docs/fr/notions-de-base/unsloth-environment-flags.md

# Source: https://unsloth.ai/docs/de/grundlagen/unsloth-environment-flags.md

# Source: https://unsloth.ai/docs/jp/ji-ben/unsloth-environment-flags.md

# Source: https://unsloth.ai/docs/zh/ji-chu-zhi-shi/unsloth-environment-flags.md

# Source: https://unsloth.ai/docs/basics/unsloth-environment-flags.md

# Unsloth Environment Flags

<table><thead><tr><th width="397.4666748046875">Environment variable</th><th>Purpose</th><th data-hidden></th></tr></thead><tbody><tr><td><code>os.environ["UNSLOTH_RETURN_LOGITS"] = "1"</code></td><td>Forcibly returns logits - useful for evaluation if logits are needed.</td><td></td></tr><tr><td><code>os.environ["UNSLOTH_COMPILE_DISABLE"] = "1"</code></td><td>Disables auto compiler. Could be useful to debug incorrect finetune results.</td><td></td></tr><tr><td><code>os.environ["UNSLOTH_DISABLE_FAST_GENERATION"] = "1"</code></td><td>Disables fast generation for generic models.</td><td></td></tr><tr><td><code>os.environ["UNSLOTH_ENABLE_LOGGING"] = "1"</code></td><td>Enables auto compiler logging - useful to see which functions are compiled or not.</td><td></td></tr><tr><td><code>os.environ["UNSLOTH_FORCE_FLOAT32"] = "1"</code></td><td>On float16 machines, use float32 and not float16 mixed precision. Useful for Gemma 3.</td><td></td></tr><tr><td><code>os.environ["UNSLOTH_STUDIO_DISABLED"] = "1"</code></td><td>Disables extra features.</td><td></td></tr><tr><td><code>os.environ["UNSLOTH_COMPILE_DEBUG"] = "1"</code></td><td>Turns on extremely verbose <code>torch.compile</code>logs.</td><td></td></tr><tr><td><code>os.environ["UNSLOTH_COMPILE_MAXIMUM"] = "0"</code></td><td>Enables maximum <code>torch.compile</code>optimizations - not recommended.</td><td></td></tr><tr><td><code>os.environ["UNSLOTH_COMPILE_IGNORE_ERRORS"] = "1"</code></td><td>Can turn this off to enable fullgraph parsing.</td><td></td></tr><tr><td><code>os.environ["UNSLOTH_FULLGRAPH"] = "0"</code></td><td>Enable <code>torch.compile</code> fullgraph mode</td><td></td></tr><tr><td><code>os.environ["UNSLOTH_DISABLE_AUTO_UPDATES"] = "1"</code></td><td>Forces no updates to <code>unsloth-zoo</code></td><td></td></tr></tbody></table>

Another possiblity is maybe the model uploads we uploaded are corrupted, but unlikely. Try the following:

```python
model, tokenizer = FastVisionModel.from_pretrained(
    "Qwen/Qwen2-VL-7B-Instruct",
    use_exact_model_name = True,
)
```
