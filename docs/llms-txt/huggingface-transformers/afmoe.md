# Source: https://huggingface.co/docs/transformers/v5.0.0rc1/model_doc/afmoe.md

# AFMoE

AFMoE (Arcee Foundational Mixture of Experts) is a decoder-only transformer model that extends the Llama architecture with a sparse Mixture of Experts (MoE) approach. The model combines token-choice routing with shared experts and employs several architectural innovations for efficient inference and improved performance.

## Key Architecture Features

AFMoE introduces several key modifications to the standard transformer architecture:

- **Mixture of Experts with Shared Experts**: Combines routed experts (activated per-token via learned routing) with always-active shared experts for stable base computation
- **Token-Choice Routing**: Uses sigmoid or softmax-based routing with normalization and scaling for expert selection
- **Q/K Normalization and Gating**: Applies RMSNorm to query and key projections and uses sigmoid gating on attention outputs for improved stability
- **Hybrid Attention Patterns**: Alternates between sliding window attention and full attention across layers for efficiency with long contexts
- **Dual Normalization**: Uses pre- and post-normalization around both attention and MLP blocks for training stability
- **Configurable Dense Layers**: Allows initial layers to use dense MLPs before transitioning to sparse MoE layers

The model supports extended context lengths with RoPE embeddings and includes all standard Transformers features including Flash Attention 2, SDPA, gradient checkpointing, and quantization support.

> [!TIP]
> AFMoE is particularly well-suited for scenarios requiring efficient scaling through sparsity while maintaining strong performance. The shared experts provide a stable computation baseline while routed experts enable model capacity scaling.

The example below demonstrates how to generate text with AFMoE using [Pipeline](/docs/transformers/v5.0.0rc1/en/main_classes/pipelines#transformers.Pipeline) or the [AutoModel](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoModel).

```py
import torch
from transformers import pipeline

pipeline = pipeline(
    task="text-generation",
    model="arcee-ai/Trinity-Mini",
    torch_dtype=torch.bfloat16,
    device=0
)

output = pipeline("The key innovation in mixture of experts is")
print(output[0]["generated_text"])
```

```py
import torch
from transformers import AutoTokenizer, AfmoeForCausalLM

tokenizer = AutoTokenizer.from_pretrained("arcee-ai/Trinity-Mini")
model = AfmoeForCausalLM.from_pretrained(
    "arcee-ai/Trinity-Mini",
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

inputs = tokenizer("The key innovation in mixture of experts is", return_tensors="pt")
with torch.no_grad():
    outputs = model.generate(**inputs, max_new_tokens=50)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## Model Architecture Details

### Expert Routing

AFMoE uses token-choice routing where each token independently selects top-k experts based on router logits. The routing mechanism includes:

- Configurable scoring function (sigmoid or softmax)
- Optional route normalization for balanced expert utilization
- Route scaling to control expert contribution strength
- Bias correction for expert selection

### Shared Experts

Unlike standard MoE models, AFMoE includes shared experts that are always activated for every token, providing:

- A stable computation baseline across all tokens
- Reduced variance in model outputs
- Better handling of out-of-distribution inputs

### Attention Mechanism

The hybrid attention pattern alternates between:

- **Sliding Window Attention**: For efficiency on long sequences, with configurable window size
- **Full Attention**: Applied every N layers (configurable via `global_attn_every_n_layers`) for global context

All attention layers include Q/K normalization and output gating for improved training dynamics.

## AfmoeConfig[[transformers.AfmoeConfig]]

#### transformers.AfmoeConfig[[transformers.AfmoeConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/afmoe/configuration_afmoe.py#L27)

This is the configuration class to store the configuration of a [AfmoeModel](/docs/transformers/v5.0.0rc1/en/model_doc/afmoe#transformers.AfmoeModel). It is used to instantiate an
AFMoE model according to the specified arguments, defining the model architecture. Instantiating a configuration
with the defaults will yield a similar configuration to that of [arcee-ai/Trinity-Mini](https://huggingface.co/arcee-ai/Trinity-Mini).

AFMoE is an Adaptive Feedforward MoE (Mixture of Experts) model with token-choice routing, shared experts, and a
hybrid attention mechanism combining sliding window and full attention patterns.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:
```python
>>> from transformers import AfmoeModel, AfmoeConfig

>>> # Initializing an AFMoE configuration
>>> configuration = AfmoeConfig()

>>> # Initializing a model from the afmoe-small-sft-v1 style configuration
>>> model = AfmoeModel(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

vocab_size (`int`, *optional*, defaults to 200192) : Vocabulary size of the AFMoE model. Defines the number of different tokens that can be represented by the `inputs_ids` passed when calling [AfmoeModel](/docs/transformers/v5.0.0rc1/en/model_doc/afmoe#transformers.AfmoeModel).

hidden_size (`int`, *optional*, defaults to 2048) : Dimension of the hidden representations.

intermediate_size (`int`, *optional*, defaults to 6144) : Dimension of the dense MLP representations.

moe_intermediate_size (`int`, *optional*, defaults to 1408) : Intermediate size of the routed expert MLPs.

num_hidden_layers (`int`, *optional*, defaults to 32) : Number of hidden layers in the Transformer decoder.

num_dense_layers (`int`, *optional*, defaults to 1) : Number of initial dense layers before MoE layers begin. Layers with index >> from transformers import AutoTokenizer, AfmoeForCausalLM

>>> model = AfmoeForCausalLM.from_pretrained("meta-afmoe/Afmoe-2-7b-hf")
>>> tokenizer = AutoTokenizer.from_pretrained("meta-afmoe/Afmoe-2-7b-hf")

>>> prompt = "Hey, are you conscious? Can you talk to me?"
>>> inputs = tokenizer(prompt, return_tensors="pt")

>>> # Generate
>>> generate_ids = model.generate(inputs.input_ids, max_length=30)
>>> tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
"Hey, are you conscious? Can you talk to me?\nI'm not conscious, but I can talk to you."
```

**Parameters:**

config ([AfmoeForCausalLM](/docs/transformers/v5.0.0rc1/en/model_doc/afmoe#transformers.AfmoeForCausalLM)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

`[transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([AfmoeConfig](/docs/transformers/v5.0.0rc1/en/model_doc/afmoe#transformers.AfmoeConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
  `past_key_values` input) to speed up sequential decoding.
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.

