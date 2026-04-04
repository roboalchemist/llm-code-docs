# Source: https://huggingface.co/docs/transformers/v5.0.0/community_integrations/vllm.md

# vLLM

[vLLM](https://github.com/vllm-project/vllm) is a high-throughput inference engine for serving LLMs at scale. It continuously batches requests and keeps KV cache memory compact with PagedAttention.

Set `model_impl="transformers"` to load a model using the Transformers modeling backend.

```py
from vllm import LLM

llm = LLM(model="meta-llama/Llama-3.2-1B", model_impl="transformers")
print(llm.generate(["The capital of France is"]))
```

Pass `--model-impl transformers` to the `vllm serve` command for online serving.

```bash
vllm serve meta-llama/Llama-3.2-1B \
    --task generate \
    --model-impl transformers
```

vLLM uses [AutoConfig.from_pretrained()](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoConfig.from_pretrained) to load a model's `config.json` file from the Hub or your Hugging Face cache. It checks the `architectures` field against its internal model registry to determine which vLLM model class to load. If the model isn't in the registry, vLLM calls [AutoModel.from_config()](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoModel.from_config) to load the Transformers model implementation.

Setting `model_impl="transformers"` bypasses the vLLM model registry and loads directly from Transformers. vLLM replaces most model modules (MoE, attention, linear, etc.) with its own optimized versions.

[AutoTokenizer.from_pretrained()](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer.from_pretrained) loads tokenizer files. vLLM caches some tokenizer internals to reduce overhead during inference. Model weights download from the Hub in safetensors format.

## Resources

- [vLLM docs](https://docs.vllm.ai/en/latest/models/supported_models.html#transformers) for more usage examples and tips.
- [Integration with Hugging Face](https://docs.vllm.ai/en/latest/design/huggingface_integration/) explains how vLLM integrates with Transformers.

