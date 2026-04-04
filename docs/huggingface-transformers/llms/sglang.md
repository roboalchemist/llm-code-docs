# Source: https://huggingface.co/docs/transformers/v5.0.0/community_integrations/sglang.md

# SGLang

[SGLang](https://docs.sglang.ai) is a low-latency, high-throughput inference engine for large language models (LLMs). It also includes a frontend language for building agentic workflows.

Set `model-impl="transformers"` to load a Transformers modeling backend.

```py
import sglang as sgl

llm = sgl.Engine("meta-llama/Llama-3.2-1B-Instruct", model-impl="transformers")
print(llm.generate(["The capital of France is"], {"max_new_tokens": 20})[0])
```

Pass `--model-impl transformers` to the `sglang.launch_server` command for online serving.

```bash
python3 -m sglang.launch_server \
  --model-path meta-llama/Llama-3.2-1B-Instruct \
  --model-impl transformers \
  --host 0.0.0.0 \
  --port 30000
```

Setting `model-impl="transformers"` tells SGLang to skip its native model matching and use the `TransformersModel` backend instead. [PretrainedConfig.from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig.from_pretrained) loads the config and `AutoModel.config` resolves the model class.

During loading, `_attn_implementation` is set to `"sglang"`. This routes attention calls through SGLang. RadixAttention kernels replace standard attention layers. SGLang's parallel linear class replaces linear layers to support tensor parallelism. The model benefits from all SGLang optimizations.

> [!WARNING]
> Compatible models require `_supports_attention_backend=True` so SGLang can control attention execution. See the [Building a compatible model backend for inference](./transformers_as_backend#model-implementation) guide for details.

The [load_weights](https://github.com/sgl-project/sglang/blob/main/python/sglang/srt/models/transformers.py#L277) function populates the model with weights.

## Resources

- [SGLang docs](https://docs.sglang.ai/supported_models/transformers_fallback.html) has more usage examples and tips for using Transformers as a backend.
- [Transformers backend integration in SGLang](https://huggingface.co/blog/transformers-backend-sglang) blog post explains what this integration enables.

