# Source: https://huggingface.co/docs/transformers/v5.3.0/model_doc/qwen3_5_moe.md

# Qwen3.5 Moe

[Qwen3.5 Moe](https://huggingface.co/papers/2502.13923) TODO @shuaibai @bozheng

Model usage

```py
TODO
```

## Qwen3_5MoeConfig[[transformers.Qwen3_5MoeConfig]]

#### transformers.Qwen3_5MoeConfig[[transformers.Qwen3_5MoeConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/qwen3_5_moe/configuration_qwen3_5_moe.py#L260)

This is the configuration class to store the configuration of a [Qwen3_5MoeModel](/docs/transformers/v5.3.0/en/model_doc/qwen3_5_moe#transformers.Qwen3_5MoeModel). It is used to instantiate a
Qwen3.5-MoE model according to the specified arguments, defining the model architecture. Instantiating a configuration
with the defaults will yield a similar configuration to that of
Qwen3.5-35B-A3B-Instruct [Qwen/Qwen3.5-35B-A3B-Instruct](https://huggingface.co/Qwen/Qwen3.5-35B-A3B-Instruct).

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.3.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.3.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

```python
>>> from transformers import Qwen3_5MoeForConditionalGeneration, Qwen3_5MoeConfig

>>> # Initializing a Qwen3.5-MoE style configuration
>>> configuration = Qwen3_5MoeConfig()

>>> # Initializing a model from the Qwen3.5-35B-A3B style configuration
>>> model = Qwen3_5MoeForConditionalGeneration(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

text_config (`Union[PreTrainedConfig, dict]`, *optional*, defaults to `Qwen3_5TextConfig`) : The config object or dictionary of the text backbone.

vision_config (`Union[PreTrainedConfig, dict]`,  *optional*, defaults to `Qwen3_5VisionConfig`) : The config object or dictionary of the vision backbone.

image_token_id (`int`, *optional*, defaults to 248056) : The image token index to encode the image prompt.

video_token_id (`int`, *optional*, defaults to 248057) : The video token index to encode the image prompt.

vision_start_token_id (`int`, *optional*, defaults to 248053) : The start token index to encode the image prompt.

vision_end_token_id (`int`, *optional*, defaults to 248054) : The end token index to encode the image prompt.

tie_word_embeddings (`bool`, *optional*, defaults to `False`) : Whether to tie the word embeddings.

## Qwen3_5MoeTextConfig[[transformers.Qwen3_5MoeTextConfig]]

#### transformers.Qwen3_5MoeTextConfig[[transformers.Qwen3_5MoeTextConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/qwen3_5_moe/configuration_qwen3_5_moe.py#L24)

This is the configuration class to store the configuration of a [Qwen3_5MoeTextModel](/docs/transformers/v5.3.0/en/model_doc/qwen3_5_moe#transformers.Qwen3_5MoeTextModel). It is used to instantiate a
Qwen3.5-MoE model according to the specified arguments, defining the model architecture.
Instantiating a configuration with the defaults will yield a similar configuration to that of
Qwen3.5-35B-A3B-Instruct [Qwen/Qwen3.5-35B-A3B-Instruct](https://huggingface.co/Qwen/Qwen3.5-35B-A3B-Instruct).

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.3.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.3.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

```python
>>> from transformers import Qwen3_5MoeTextModel, Qwen3_5MoeTextConfig

>>> # Initializing a Qwen3.5-MoE style configuration
>>> configuration =  Qwen3_5MoeTextConfig()

>>> # Initializing a model from the Qwen3.5-35B-A3B style configuration
>>> model = Qwen3_5MoeTextModel(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

vocab_size (`int`, *optional*, defaults to 248320) : Vocabulary size of the model. Defines the number of different tokens that can be represented by the `inputs_ids`.

hidden_size (`int`, *optional*, defaults to 2048) : Dimension of the hidden representations.

num_hidden_layers (`int`, *optional*, defaults to 40) : Number of hidden layers in the Transformer encoder.

num_attention_heads (`int`, *optional*, defaults to 16) : Number of attention heads for each attention layer in the Transformer encoder.

num_key_value_heads (`int`, *optional*, defaults to 2) : This is the number of key_value heads that should be used to implement Grouped Query Attention. If `num_key_value_heads=num_attention_heads`, the model will use Multi Head Attention (MHA), if `num_key_value_heads=1` the model will use Multi Query Attention (MQA) otherwise GQA is used. When converting a multi-head checkpoint to a GQA checkpoint, each group key and value head should be constructed by meanpooling all the original heads within that group. For more details checkout [this paper](https://arxiv.org/pdf/2305.13245.pdf). If it is not specified, will default to `32`.

hidden_act (`str`, *optional*, defaults to `"silu"`) : The non-linear activation function in the decoder.

max_position_embeddings (`int`, *optional*, defaults to 32768) : The maximum sequence length that this model might ever be used with.

initializer_range (`float`, *optional*, defaults to 0.02) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

rms_norm_eps (`float`, *optional*, defaults to 1e-06) : The epsilon used by the rms normalization layers.

use_cache (`bool`, *optional*, defaults to `True`) : Whether or not the model should return the last key/values attentions (not used by all models). Only relevant if `config.is_decoder=True`.

tie_word_embeddings (`bool`, *optional*, defaults to `False`) : Whether the model's input and output word embeddings should be tied.

rope_parameters (`RopeParameters`, *optional*) : Dictionary containing the configuration parameters for the RoPE embeddings. The dictionary should contain a value for `rope_theta` and optionally parameters used for scaling in case you want to use RoPE with longer `max_position_embeddings`.

attention_bias (`bool`, *optional*, defaults to `False`) : Whether to use a bias in the query, key, value and output projection layers during self-attention.

attention_dropout (`float`, *optional*, defaults to 0.0) : The dropout ratio for the attention probabilities.

head_dim (`int`, *optional*, defaults to 256) : Projection weights dimension in multi-head attention.

linear_conv_kernel_dim (`int`, *optional*, defaults to 4) : Kernel size of the convolution used in linear attention layers.

linear_key_head_dim (`int`, *optional*, defaults to 128) : Dimension of each key head in linear attention.

linear_value_head_dim (`int`, *optional*, defaults to 128) : Dimension of each value head in linear attention.

linear_num_key_heads (`int`, *optional*, defaults to 16) : Number of key heads used in linear attention layers.

linear_num_value_heads (`int`, *optional*, defaults to 32) : Number of value heads used in linear attention layers.

moe_intermediate_size (`int`, *optional*, defaults to 512) : Intermediate size of the routed expert.

shared_expert_intermediate_size (`int`, *optional*, defaults to 512) : Intermediate size of the shared expert.

num_experts_per_tok (`int`, *optional*, defaults to 8) : Number of selected experts.

num_experts (`int`, *optional*, defaults to 256) : Number of routed experts.

output_router_logits (`bool`, *optional*, defaults to `False`) : Whether or not the router logits should be returned by the model. Enabling this will also allow the model to output the auxiliary loss, including load balancing loss and router z-loss.

router_aux_loss_coef (`float`, *optional*, defaults to 0.001) : The aux loss factor for the total loss.

layer_types (`list[str]`, *optional*) : Types of each layer (attention or linear).

pad_token_id (`int`, *optional*) : Padding token id.

bos_token_id (`int`, *optional*) : Beginning of stream token id.

eos_token_id (`int`, *optional*) : End of stream token id.

## Qwen3_5MoeVisionModel[[transformers.Qwen3_5MoeVisionModel]]

#### transformers.Qwen3_5MoeVisionModel[[transformers.Qwen3_5MoeVisionModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/qwen3_5_moe/modeling_qwen3_5_moe.py#L1181)

forwardtransformers.Qwen3_5MoeVisionModel.forwardhttps://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/qwen3_5_moe/modeling_qwen3_5_moe.py#L1319[{"name": "hidden_states", "val": ": Tensor"}, {"name": "grid_thw", "val": ": Tensor"}, {"name": "**kwargs", "val": ""}]- **hidden_states** (`torch.Tensor` of shape `(seq_len, hidden_size)`) --
  The final hidden states of the model.
- **grid_thw** (`torch.Tensor` of shape `(num_images_or_videos, 3)`) --
  The temporal, height and width of feature shape of each image in LLM.0`torch.Tensor`hidden_states.

**Parameters:**

hidden_states (`torch.Tensor` of shape `(seq_len, hidden_size)`) : The final hidden states of the model.

grid_thw (`torch.Tensor` of shape `(num_images_or_videos, 3)`) : The temporal, height and width of feature shape of each image in LLM.

**Returns:**

``torch.Tensor``

hidden_states.

## Qwen3_5MoeTextModel[[transformers.Qwen3_5MoeTextModel]]

#### transformers.Qwen3_5MoeTextModel[[transformers.Qwen3_5MoeTextModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/qwen3_5_moe/modeling_qwen3_5_moe.py#L1427)

forwardtransformers.Qwen3_5MoeTextModel.forwardhttps://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/qwen3_5_moe/modeling_qwen3_5_moe.py#L1440[{"name": "input_ids", "val": ": torch.LongTensor | None = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.LongTensor | None = None"}, {"name": "past_key_values", "val": ": transformers.cache_utils.Cache | None = None"}, {"name": "inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "cache_position", "val": ": torch.LongTensor | None = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.3.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.3.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.3.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

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

  Only [Cache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).
  If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.

  The model will output the same cache format that is fed as input.

  If `past_key_values` are used, the user is expected to input only unprocessed `input_ids` (those that don't
  have their past key value states given to this model) of shape `(batch_size, unprocessed_length)` instead of all `input_ids`
  of shape `(batch_size, sequence_length)`.
- **inputs_embeds** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) --
  Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation. This
  is useful if you want more control over how to convert `input_ids` indices into associated vectors than the
  model's internal embedding lookup matrix.
- **use_cache** (`bool`, *optional*) --
  If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
  `past_key_values`).
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.0[BaseModelOutputWithPast](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or `tuple(torch.FloatTensor)`A [BaseModelOutputWithPast](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Qwen3_5MoeConfig](/docs/transformers/v5.3.0/en/model_doc/qwen3_5_moe#transformers.Qwen3_5MoeConfig)) and inputs.
The [Qwen3_5MoeTextModel](/docs/transformers/v5.3.0/en/model_doc/qwen3_5_moe#transformers.Qwen3_5MoeTextModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.

  If `past_key_values` is used only the last hidden-state of the sequences of shape `(batch_size, 1,
  hidden_size)` is output.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

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

**Parameters:**

input_ids (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) : Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.3.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.3.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and [PreTrainedTokenizer.__call__()](/docs/transformers/v5.3.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.  [What are input IDs?](../glossary#input-ids)

attention_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) : Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:  - 1 for tokens that are **not masked**, - 0 for tokens that are **masked**.  [What are attention masks?](../glossary#attention-mask)

position_ids (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) : Indices of positions of each input sequence tokens in the position embeddings. Selected in the range `[0, config.n_positions - 1]`.  [What are position IDs?](../glossary#position-ids)

past_key_values (`~cache_utils.Cache`, *optional*) : Pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention blocks) that can be used to speed up sequential decoding. This typically consists in the `past_key_values` returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.  Only [Cache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache). If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.  The model will output the same cache format that is fed as input.  If `past_key_values` are used, the user is expected to input only unprocessed `input_ids` (those that don't have their past key value states given to this model) of shape `(batch_size, unprocessed_length)` instead of all `input_ids` of shape `(batch_size, sequence_length)`.

inputs_embeds (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) : Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation. This is useful if you want more control over how to convert `input_ids` indices into associated vectors than the model's internal embedding lookup matrix.

use_cache (`bool`, *optional*) : If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see `past_key_values`).

cache_position (`torch.LongTensor` of shape `(sequence_length)`, *optional*) : Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`, this tensor is not affected by padding. It is used to update the cache in the correct position and to infer the complete sequence length.

**Returns:**

`[BaseModelOutputWithPast](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or `tuple(torch.FloatTensor)``

A [BaseModelOutputWithPast](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Qwen3_5MoeConfig](/docs/transformers/v5.3.0/en/model_doc/qwen3_5_moe#transformers.Qwen3_5MoeConfig)) and inputs.

## Qwen3_5MoeModel[[transformers.Qwen3_5MoeModel]]

#### transformers.Qwen3_5MoeModel[[transformers.Qwen3_5MoeModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/qwen3_5_moe/modeling_qwen3_5_moe.py#L1529)

The bare Qwen3 5 Moe Model outputting raw hidden-states without any specific head on top.

This model inherits from [PreTrainedModel](/docs/transformers/v5.3.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.Qwen3_5MoeModel.forwardhttps://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/qwen3_5_moe/modeling_qwen3_5_moe.py#L1838[{"name": "input_ids", "val": ": LongTensor = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.LongTensor | None = None"}, {"name": "past_key_values", "val": ": transformers.cache_utils.Cache | None = None"}, {"name": "inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "pixel_values", "val": ": torch.Tensor | None = None"}, {"name": "pixel_values_videos", "val": ": torch.FloatTensor | None = None"}, {"name": "image_grid_thw", "val": ": torch.LongTensor | None = None"}, {"name": "video_grid_thw", "val": ": torch.LongTensor | None = None"}, {"name": "mm_token_type_ids", "val": ": torch.IntTensor | None = None"}, {"name": "cache_position", "val": ": torch.LongTensor | None = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.3.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.3.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.3.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

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

  Only [Cache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).
  If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.

  The model will output the same cache format that is fed as input.

  If `past_key_values` are used, the user is expected to input only unprocessed `input_ids` (those that don't
  have their past key value states given to this model) of shape `(batch_size, unprocessed_length)` instead of all `input_ids`
  of shape `(batch_size, sequence_length)`.
- **inputs_embeds** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) --
  Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation. This
  is useful if you want more control over how to convert `input_ids` indices into associated vectors than the
  model's internal embedding lookup matrix.
- **pixel_values** (`torch.Tensor` of shape `(batch_size, num_channels, image_size, image_size)`, *optional*) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  `image_processor_class`. See `image_processor_class.__call__` for details (`processor_class` uses
  `image_processor_class` for processing images).
- **pixel_values_videos** (`torch.FloatTensor` of shape `(batch_size, num_frames, num_channels, frame_size, frame_size)`, *optional*) --
  The tensors corresponding to the input video. Pixel values for videos can be obtained using
  `video_processor_class`. See `video_processor_class.__call__` for details (`processor_class` uses
  `video_processor_class` for processing videos).
- **image_grid_thw** (`torch.LongTensor` of shape `(num_images, 3)`, *optional*) --
  The temporal, height and width of feature shape of each image in LLM.
- **video_grid_thw** (`torch.LongTensor` of shape `(num_videos, 3)`, *optional*) --
  The temporal, height and width of feature shape of each video in LLM.
- **mm_token_type_ids** (`torch.IntTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens matching each modality. For example text (0), image (1), video (2).
  Multimodal token type ids can be obtained using [AutoProcessor](/docs/transformers/v5.3.0/en/model_doc/auto#transformers.AutoProcessor). See [ProcessorMixin.__call__()](/docs/transformers/v5.3.0/en/model_doc/vilt#transformers.ViltProcessor.__call__) for details.

- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.0`Qwen3_5MoeModelOutputWithPast` or `tuple(torch.FloatTensor)`A `Qwen3_5MoeModelOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration (`None`) and inputs.
The [Qwen3_5MoeModel](/docs/transformers/v5.3.0/en/model_doc/qwen3_5_moe#transformers.Qwen3_5MoeModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*, defaults to `None`) -- Sequence of hidden-states at the output of the last layer of the model.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
  `past_key_values` input) to speed up sequential decoding.
- **hidden_states** (`tuple[torch.FloatTensor]`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple[torch.FloatTensor]`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
- **rope_deltas** (`torch.LongTensor` of shape `(batch_size, )`, *optional*) -- The rope index difference between sequence length and multimodal rope.
- **router_logits** (`tuple[torch.FloatTensor]`, *optional*, returned when `output_router_logits=True` is passed or when `config.add_router_probs=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, sequence_length, num_experts)`.

  Router logits of the model, useful to compute the auxiliary loss for Mixture of Experts models.

**Parameters:**

config ([Qwen3_5MoeModel](/docs/transformers/v5.3.0/en/model_doc/qwen3_5_moe#transformers.Qwen3_5MoeModel)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.3.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``Qwen3_5MoeModelOutputWithPast` or `tuple(torch.FloatTensor)``

A `Qwen3_5MoeModelOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration (`None`) and inputs.

## Qwen3_5MoeForCausalLM[[transformers.Qwen3_5MoeForCausalLM]]

#### transformers.Qwen3_5MoeForCausalLM[[transformers.Qwen3_5MoeForCausalLM]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/qwen3_5_moe/modeling_qwen3_5_moe.py#L1999)

The Qwen3 5 Moe Model for causal language modeling.

This model inherits from [PreTrainedModel](/docs/transformers/v5.3.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.Qwen3_5MoeForCausalLM.forwardhttps://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/qwen3_5_moe/modeling_qwen3_5_moe.py#L2018[{"name": "input_ids", "val": ": torch.LongTensor | None = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.LongTensor | None = None"}, {"name": "past_key_values", "val": ": transformers.models.qwen3_5_moe.modeling_qwen3_5_moe.Qwen3_5MoeDynamicCache | None = None"}, {"name": "inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "labels", "val": ": torch.LongTensor | None = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "output_router_logits", "val": ": bool | None = None"}, {"name": "cache_position", "val": ": torch.LongTensor | None = None"}, {"name": "logits_to_keep", "val": ": int | torch.Tensor = 0"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.3.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.3.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.3.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **attention_mask** (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.

  [What are attention masks?](../glossary#attention-mask)
- **position_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of positions of each input sequence tokens in the position embeddings. Selected in the range `[0, config.n_positions - 1]`.

  [What are position IDs?](../glossary#position-ids)
- **past_key_values** (`~models.qwen3_5_moe.modeling_qwen3_5_moe.Qwen3_5MoeDynamicCache`, *optional*) --
  Pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention
  blocks) that can be used to speed up sequential decoding. This typically consists in the `past_key_values`
  returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.

  Only [Cache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).
  If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.

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
- **output_router_logits** (`bool`, *optional*) --
  Whether or not to return the logits of all the routers. They are useful for computing the router loss, and
  should not be returned during inference.
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.
- **logits_to_keep** (`Union[int, torch.Tensor]`, *optional*, defaults to `0`) --
  If an `int`, compute logits for the last `logits_to_keep` tokens. If `0`, calculate logits for all
  `input_ids` (special case). Only last token logits are needed for generation, and calculating them only for that
  token can save memory, which becomes pretty significant for long sequences or large vocabulary size.
  If a `torch.Tensor`, must be 1D corresponding to the indices to keep in the sequence length dimension.
  This is useful when using packed tensor format (single dimension for batch and sequence length).0`MoeCausalLMOutputWithPast` or `tuple(torch.FloatTensor)`A `MoeCausalLMOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Qwen3_5MoeConfig](/docs/transformers/v5.3.0/en/model_doc/qwen3_5_moe#transformers.Qwen3_5MoeConfig)) and inputs.
The [Qwen3_5MoeForCausalLM](/docs/transformers/v5.3.0/en/model_doc/qwen3_5_moe#transformers.Qwen3_5MoeForCausalLM) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **aux_loss** (`torch.FloatTensor`, *optional*, returned when `labels` is provided) -- aux_loss for the sparse modules.
- **router_logits** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_router_probs=True` and `config.add_router_probs=True` is passed or when `config.output_router_probs=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, sequence_length, num_experts)`.

  Raw router logtis (post-softmax) that are computed by MoE routers, these terms are used to compute the auxiliary
  loss for Mixture of Experts models.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
  `past_key_values` input) to speed up sequential decoding.
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.

Example:

```python
>>> from transformers import AutoTokenizer, Qwen3_5MoeForCausalLM

>>> model = Qwen3_5MoeForCausalLM.from_pretrained("Qwen/Qwen3-Next-80B-A3B-Instruct")
>>> tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-Next-80B-A3B-Instruct")

>>> prompt = "Hey, are you conscious? Can you talk to me?"
>>> inputs = tokenizer(prompt, return_tensors="pt")

>>> # Generate
>>> generate_ids = model.generate(inputs.input_ids, max_length=30)
>>> tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
"Hey, are you conscious? Can you talk to me?\nI'm not conscious, but I can talk to you."
```

**Parameters:**

config ([Qwen3_5MoeForCausalLM](/docs/transformers/v5.3.0/en/model_doc/qwen3_5_moe#transformers.Qwen3_5MoeForCausalLM)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.3.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``MoeCausalLMOutputWithPast` or `tuple(torch.FloatTensor)``

A `MoeCausalLMOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Qwen3_5MoeConfig](/docs/transformers/v5.3.0/en/model_doc/qwen3_5_moe#transformers.Qwen3_5MoeConfig)) and inputs.

## Qwen3_5MoeForConditionalGeneration[[transformers.Qwen3_5MoeForConditionalGeneration]]

#### transformers.Qwen3_5MoeForConditionalGeneration[[transformers.Qwen3_5MoeForConditionalGeneration]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/qwen3_5_moe/modeling_qwen3_5_moe.py#L2105)

forwardtransformers.Qwen3_5MoeForConditionalGeneration.forwardhttps://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/qwen3_5_moe/modeling_qwen3_5_moe.py#L2157[{"name": "input_ids", "val": ": LongTensor = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.LongTensor | None = None"}, {"name": "past_key_values", "val": ": transformers.cache_utils.Cache | None = None"}, {"name": "inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "labels", "val": ": torch.LongTensor | None = None"}, {"name": "pixel_values", "val": ": torch.Tensor | None = None"}, {"name": "pixel_values_videos", "val": ": torch.FloatTensor | None = None"}, {"name": "image_grid_thw", "val": ": torch.LongTensor | None = None"}, {"name": "video_grid_thw", "val": ": torch.LongTensor | None = None"}, {"name": "mm_token_type_ids", "val": ": torch.IntTensor | None = None"}, {"name": "cache_position", "val": ": torch.LongTensor | None = None"}, {"name": "logits_to_keep", "val": ": int | torch.Tensor = 0"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]

labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
Labels for computing the masked language modeling loss. Indices should either be in `[0, ...,
config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored
(masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.
image_grid_thw (`torch.LongTensor` of shape `(num_images, 3)`, *optional*):
The temporal, height and width of feature shape of each image in LLM.
video_grid_thw (`torch.LongTensor` of shape `(num_videos, 3)`, *optional*):
The temporal, height and width of feature shape of each video in LLM.

Example:
```python
>>> from PIL import Image
>>> import requests
>>> from transformers import AutoProcessor, Qwen3_5MoeForConditionalGeneration

>>> model = Qwen3_5MoeForConditionalGeneration.from_pretrained("Qwen/Qwen3.5-35B-A3B-Instruct", dtype="auto", device_map="auto")
>>> processor = AutoProcessor.from_pretrained("Qwen/Qwen3.5-35B-A3B-Instruct")

>>> messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "image": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg",
            },
            {"type": "text", "text": "Describe this image in short."},
        ],
    }
]

>>> # Preparation for inference
>>> inputs = processor.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_dict=True,
    return_tensors="pt"
)
>>> inputs = inputs.to(model.device)

>>> # Generate
>>> generated_ids = model.generate(**inputs, max_new_tokens=128)
>>> generated_ids_trimmed = [
    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
]
>>> processor.batch_decode(generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
"A woman in a plaid shirt sits on a sandy beach at sunset, smiling as she gives a high-five to a yellow Labrador Retriever wearing a harness. The ocean waves roll in the background."
```

