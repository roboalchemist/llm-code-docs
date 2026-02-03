# Source: https://huggingface.co/docs/transformers/v5.0.0/model_doc/longcat_flash.md

# LongCatFlash

## Overview

The LongCatFlash model was proposed in [LongCat-Flash Technical Report](https://huggingface.co/papers/2509.01322) by the Meituan LongCat Team.
LongCat-Flash is a 560B parameter Mixture-of-Experts (MoE) model that activates 18.6B-31.3B parameters dynamically (average ~27B). The model features a shortcut-connected architecture enabling high inference speed (>100 tokens/second) and advanced reasoning capabilities.

The abstract from the paper is the following:

*We present LongCat-Flash, a 560 billion parameter Mixture-of-Experts (MoE) language model featuring a dynamic computation mechanism that activates 18.6B-31.3B parameters based on context (average ~27B). The model incorporates a shortcut-connected architecture enabling high inference speed (>100 tokens/second) and demonstrates strong performance across multiple benchmarks including 89.71% accuracy on MMLU and exceptional agentic tool use capabilities.*

Tips:

- LongCat-Flash uses a unique shortcut-connected MoE architecture that enables faster inference compared to traditional MoE models
- The model supports up to 128k context length for long-form tasks
- Dynamic parameter activation makes it computationally efficient while maintaining high performance
- Best suited for applications requiring strong reasoning, coding, and tool-calling capabilities
- The MoE architecture includes zero experts (nn.Identity modules) which act as skip connections, allowing tokens to bypass expert computation when appropriate

This model was contributed by [Molbap](https://huggingface.co/Molbap).
The original code can be found [here](https://huggingface.co/meituan-longcat/LongCat-Flash-Chat).

## Usage examples

The model is large: you will need 2x8 H100 to run inference.

```python
# launch_longcat.py
from transformers import LongcatFlashForCausalLM, AutoTokenizer
import torch

model_id = "meituan-longcat/LongCat-Flash-Chat"

tokenizer = AutoTokenizer.from_pretrained(model_id)

chat = [
      {"role": "user", "content": "Hello! What is the capital of France? What can you tell me about it?"},
]

model = LongcatFlashForCausalLM.from_pretrained(
      model_id,
      tp_plan="auto",
      dtype=torch.bfloat16,
      )

inputs = tokenizer.apply_chat_template(
      chat, tokenize=True, add_generation_prompt=True, return_tensors="pt").to(model.device)

outputs = model.generate(inputs, max_new_tokens=30)
print(tokenizer.batch_decode(outputs))
```

To run with TP, you will need torchrun:

```bash
torchrun  --nproc_per_node=8 --nnodes=2 --node_rank=0 | 1  --rdzv-id  --rdzv-backend c10d --rdzv-endpoint $NODE_ID:$NODE_PORT  --log-dir ./logs_longcat launch_longcat.py
```

And you'll get a nice generation:

```json
[Round 0] USER:Hello! What is the capital of France? What can you tell me about it? ASSISTANT:Hello! 😊 The capital of France is Paris, one of the most famous and beloved cities in the world. Here’s a quick overview of what makes Paris special:
1. Iconic Landmarks

    Eiffel Tower – The global symbol of France, built in 1889 for the World's Fair.
    Notre-Dame Cathedral – A masterpiece of Gothic architecture (currently under restoration after the 2019 fire).
    Louvre Museum – The world’s largest art museum, home to the Mona Lisa and Venus de Milo.
    Sacré-Cœur Basilica – A stunning white church atop Montmartre with panoramic views.
    Arc de Triomphe – Honors French military victories, with the Tomb of the Unknown Soldier beneath it.
    Champs-Élysées – A glamorous avenue leading to the Arc de Triomphe, lined with shops and cafés.

2. Culture & Arts

    Paris is the "City of Light" (La Ville Lumière), a nickname from its early adoption of street lighting and its role as a center of enlightenment.
    It’s a global hub for fashion (haute couture, Paris Fashion Week) and art (Impressionism, Picasso, Dali).
    Famous literary figures like Hemingway, Fitzgerald, and Sartre lived and wrote here.

3. Food & Cuisine

    Croissants, baguettes, macarons, and crème brûlée are just a few of its culinary delights.
    Paris has over 100 Michelin-starred restaurants and countless cozy bistros.
    The Marché d’Aligre and Rue Mouffetard are great for fresh produce and local flavors.

4. History & Politics

    Founded in the 3rd century BC by the Parisii tribe, it became a major European city under the Romans.
    The French Revolution (1789–1799) began here, leading to the fall of the monarchy.
    Today, it’s the political and economic heart of France, housing the French President’s residence (Élysée Palace) and the National Assembly.

**
```

## LongcatFlashConfig[[transformers.LongcatFlashConfig]]

#### transformers.LongcatFlashConfig[[transformers.LongcatFlashConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/longcat_flash/configuration_longcat_flash.py#L21)

This is the configuration class to store the configuration of a [LongcatFlashModel](/docs/transformers/v5.0.0/en/model_doc/longcat_flash#transformers.LongcatFlashModel). It is used to instantiate
a LongCat Flash model according to the specified arguments, defining the model architecture. Instantiating a
configuration with the defaults will yield a similar configuration to that of the LongCat Flash architecture.
e.g. [meituan-longcat/LongCat-Flash-Chat](https://huggingface.co/meituan-longcat/LongCat-Flash-Chat)
Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

```python
>>> from transformers import LongcatFlashModel, LongcatFlashConfig

>>> # Initializing a LongCat Flash style configuration
>>> configuration = LongcatFlashConfig()

>>> # Initializing a model from the configuration
>>> model = LongcatFlashModel(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

vocab_size (`int`, *optional*, defaults to 131072) : Vocabulary size of the LongCat Flash model. Defines the number of different tokens that can be represented by the `input_ids` passed when calling [LongcatFlashModel](/docs/transformers/v5.0.0/en/model_doc/longcat_flash#transformers.LongcatFlashModel)

hidden_size (`int`, *optional*, defaults to 6144) : Dimension of the hidden representations.

num_hidden_layers (`int`, *optional*, defaults to 56) : Number of hidden layers in the Transformer decoder.

num_layers (`int`, *optional*, defaults to 28) : number of layers, each with 2 sublayers.

num_attention_heads (`int`, *optional*, defaults to 64) : Number of attention heads for each attention layer in the Transformer decoder.

num_key_value_heads (`int`, *optional*) : This is the number of key_value heads that should be used to implement Grouped Query Attention. If `num_key_value_heads=num_attention_heads`, the model will use Multi Head Attention (MHA), if `num_key_value_heads=1` the model will use Multi Query Attention (MQA) otherwise GQA is used. When converting from a multi-head checkpoint to a GQA checkpoint, each group key and value head should be constructed by meanpooling all the original heads within that group. For more details checkout [this paper](https://arxiv.org/pdf/2305.13245.pdf). If it is not specified, will default to `num_attention_heads`.

hidden_act (`str` or `function`, *optional*, defaults to `"silu"`) : The non-linear activation function (function or string) in the decoder.

max_position_embeddings (`int`, *optional*, defaults to 131072) : The maximum sequence length that this model might ever be used with. Typically set this to something large just in case (e.g., 512 or 1024 or 2048).

initializer_range (`float`, *optional*, defaults to 0.02) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

rms_norm_eps (`float`, *optional*, defaults to 1e-05) : The epsilon value used by the RMS normalization layers.

use_cache (`bool`, *optional*, defaults to `True`) : Whether or not the model should return the last key/values attentions (not used by all models). Only relevant if `config.is_decoder=True`.

pad_token_id (`int`, *optional*) : Padding token id.

bos_token_id (`int`, *optional*, defaults to 1) : Beginning of stream token id.

eos_token_id (`int`, *optional*, defaults to 2) : End of stream token id.

tie_word_embeddings (`bool`, *optional*, defaults to `False`) : Whether to tie input and output embeddings.

rope_parameters (`RopeParameters`, *optional*) : Dictionary containing the scaling configuration for the RoPE embeddings. Currently supports two scaling strategies: linear and dynamic. Their scaling factor must be a float greater than 1. The expected format is `{"type": strategy name, "factor": scaling factor}`. When using this flag, don't update `max_position_embeddings` to the expected new maximum.

attention_bias (`bool`, *optional*, defaults to `False`) : Whether to use a bias in the query, key, value and output projection layers during self-attention.

attention_dropout (`float`, *optional*, defaults to 0.0) : The dropout ratio for the attention probabilities.

ffn_hidden_size (`int`, *optional*, defaults to 12288) : Dimension of the MLP representations.

q_lora_rank (`int`, *optional*, defaults to 1536) : The rank of the query LoRA projection in MLA (Multi-head Latent Attention).

kv_lora_rank (`int`, *optional*, defaults to 512) : The rank of the key-value LoRA projection in MLA.

qk_nope_head_dim (`int`, *optional*, defaults to 128) : The dimension of the non-position encoding part of query/key heads.

qk_rope_head_dim (`int`, *optional*, defaults to 64) : The dimension of the RoPE part of query/key heads.

head_dim (`int`, *optional*, defaults to 64) : Standard dimension of qk heads, unused except for CI.

v_head_dim (`int`, *optional*, defaults to 128) : The dimension of value heads.

qk_head_dim (`int`, *optional*) : The total dimension of query/key heads. If not specified, set to `qk_nope_head_dim + qk_rope_head_dim`.

moe_topk (`int`, *optional*, defaults to 12) : Number of experts to route to for each token in the MoE layer.

n_routed_experts (`int`, *optional*, defaults to 512) : Number of routed experts in the MoE layer.

zero_expert_num (`int`, *optional*, defaults to 256) : Number of zero experts (identity function) to add to the expert pool.

expert_ffn_hidden_size (`int`, *optional*, defaults to 2048) : Hidden size of individual expert FFN layers.

routed_scaling_factor (`float`, *optional*, defaults to 6.0) : Scaling factor applied to the routing weights.

## LongcatFlashPreTrainedModel[[transformers.LongcatFlashPreTrainedModel]]

#### transformers.LongcatFlashPreTrainedModel[[transformers.LongcatFlashPreTrainedModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/longcat_flash/modeling_longcat_flash.py#L544)

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

_forward_unimplementedtransformers.LongcatFlashPreTrainedModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/torch/nn/modules/module.py#L391[{"name": "*input", "val": ": typing.Any"}]
Define the computation performed at every call.

Should be overridden by all subclasses.

Although the recipe for forward pass needs to be defined within
this function, one should call the `Module` instance afterwards
instead of this since the former takes care of running the
registered hooks while the latter silently ignores them.

**Parameters:**

config ([PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

## LongcatFlashModel[[transformers.LongcatFlashModel]]

#### transformers.LongcatFlashModel[[transformers.LongcatFlashModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/longcat_flash/modeling_longcat_flash.py#L573)

The bare Longcat Flash Model outputting raw hidden-states without any specific head on top.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.LongcatFlashModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/longcat_flash/modeling_longcat_flash.py#L596[{"name": "input_ids", "val": ": torch.LongTensor | None = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.LongTensor | None = None"}, {"name": "past_key_values", "val": ": transformers.cache_utils.Cache | None = None"}, {"name": "inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "cache_position", "val": ": torch.LongTensor | None = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **attention_mask** (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.

  [What are attention masks?](../glossary#attention-mask)
- **position_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of positions of each input sequence tokens in the position embeddings. Selected in the range `[0, config.n_positions - 1]`.

  [What are position IDs?](../glossary#position-ids)
- **past_key_values** (`~cache_utils.Cache`, *optional*) --
  Pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention
  blocks) that can be used to speed up sequential decoding. This typically consists in the `past_key_values`
  returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.

  Only [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).
  If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.

  The model will output the same cache format that is fed as input.

  If `past_key_values` are used, the user is expected to input only unprocessed `input_ids` (those that don't
  have their past key value states given to this model) of shape `(batch_size, unprocessed_length)` instead of all `input_ids`
  of shape `(batch_size, sequence_length)`.
- **inputs_embeds** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) --
  Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation. This
  is useful if you want more control over how to convert `input_ids` indices into associated vectors than the
  model's internal embedding lookup matrix.
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.
- **use_cache** (`bool`, *optional*) --
  If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
  `past_key_values`).0[transformers.modeling_outputs.BaseModelOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or `tuple(torch.FloatTensor)`A [transformers.modeling_outputs.BaseModelOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([LongcatFlashConfig](/docs/transformers/v5.0.0/en/model_doc/longcat_flash#transformers.LongcatFlashConfig)) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.

  If `past_key_values` is used only the last hidden-state of the sequences of shape `(batch_size, 1,
  hidden_size)` is output.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks and optionally if
  `config.is_encoder_decoder=True` in the cross-attention blocks) that can be used (see `past_key_values`
  input) to speed up sequential decoding.
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
The [LongcatFlashModel](/docs/transformers/v5.0.0/en/model_doc/longcat_flash#transformers.LongcatFlashModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

**Parameters:**

config ([LongcatFlashModel](/docs/transformers/v5.0.0/en/model_doc/longcat_flash#transformers.LongcatFlashModel)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

`[transformers.modeling_outputs.BaseModelOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([LongcatFlashConfig](/docs/transformers/v5.0.0/en/model_doc/longcat_flash#transformers.LongcatFlashConfig)) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.

  If `past_key_values` is used only the last hidden-state of the sequences of shape `(batch_size, 1,
  hidden_size)` is output.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks and optionally if
  `config.is_encoder_decoder=True` in the cross-attention blocks) that can be used (see `past_key_values`
  input) to speed up sequential decoding.
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.

## LongcatFlashForCausalLM[[transformers.LongcatFlashForCausalLM]]

#### transformers.LongcatFlashForCausalLM[[transformers.LongcatFlashForCausalLM]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/longcat_flash/modeling_longcat_flash.py#L660)

The Longcat Flash Model for causal language modeling.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.LongcatFlashForCausalLM.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/longcat_flash/modeling_longcat_flash.py#L675[{"name": "input_ids", "val": ": torch.LongTensor | None = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.LongTensor | None = None"}, {"name": "past_key_values", "val": ": transformers.cache_utils.Cache | None = None"}, {"name": "inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "labels", "val": ": torch.LongTensor | None = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "cache_position", "val": ": torch.LongTensor | None = None"}, {"name": "logits_to_keep", "val": ": int | torch.Tensor = 0"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **attention_mask** (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.

  [What are attention masks?](../glossary#attention-mask)
- **position_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of positions of each input sequence tokens in the position embeddings. Selected in the range `[0, config.n_positions - 1]`.

  [What are position IDs?](../glossary#position-ids)
- **past_key_values** (`~cache_utils.Cache`, *optional*) --
  Pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention
  blocks) that can be used to speed up sequential decoding. This typically consists in the `past_key_values`
  returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.

  Only [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).
  If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.

  The model will output the same cache format that is fed as input.

  If `past_key_values` are used, the user is expected to input only unprocessed `input_ids` (those that don't
  have their past key value states given to this model) of shape `(batch_size, unprocessed_length)` instead of all `input_ids`
  of shape `(batch_size, sequence_length)`.
- **inputs_embeds** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) --
  Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation. This
  is useful if you want more control over how to convert `input_ids` indices into associated vectors than the
  model's internal embedding lookup matrix.
- **labels** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Labels for computing the masked language modeling loss. Indices should either be in `[0, ...,
  config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored
  (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.
- **use_cache** (`bool`, *optional*) --
  If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
  `past_key_values`).
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.
- **logits_to_keep** (`Union[int, torch.Tensor]`, *optional*, defaults to `0`) --
  If an `int`, compute logits for the last `logits_to_keep` tokens. If `0`, calculate logits for all
  `input_ids` (special case). Only last token logits are needed for generation, and calculating them only for that
  token can save memory, which becomes pretty significant for long sequences or large vocabulary size.
  If a `torch.Tensor`, must be 1D corresponding to the indices to keep in the sequence length dimension.
  This is useful when using packed tensor format (single dimension for batch and sequence length).0[transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or `tuple(torch.FloatTensor)`A [transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([LongcatFlashConfig](/docs/transformers/v5.0.0/en/model_doc/longcat_flash#transformers.LongcatFlashConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
  `past_key_values` input) to speed up sequential decoding.
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
The [LongcatFlashForCausalLM](/docs/transformers/v5.0.0/en/model_doc/longcat_flash#transformers.LongcatFlashForCausalLM) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Example:

```python
>>> from transformers import AutoTokenizer, LongcatFlashForCausalLM

>>> model = LongcatFlashForCausalLM.from_pretrained("meta-longcat_flash/LongcatFlash-2-7b-hf")
>>> tokenizer = AutoTokenizer.from_pretrained("meta-longcat_flash/LongcatFlash-2-7b-hf")

>>> prompt = "Hey, are you conscious? Can you talk to me?"
>>> inputs = tokenizer(prompt, return_tensors="pt")

>>> # Generate
>>> generate_ids = model.generate(inputs.input_ids, max_length=30)
>>> tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
"Hey, are you conscious? Can you talk to me?\nI'm not conscious, but I can talk to you."
```

**Parameters:**

config ([LongcatFlashForCausalLM](/docs/transformers/v5.0.0/en/model_doc/longcat_flash#transformers.LongcatFlashForCausalLM)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

`[transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([LongcatFlashConfig](/docs/transformers/v5.0.0/en/model_doc/longcat_flash#transformers.LongcatFlashConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
  `past_key_values` input) to speed up sequential decoding.
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.

