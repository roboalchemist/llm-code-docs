# Source: https://huggingface.co/docs/transformers/v5.0.0rc1/model_doc/ovis2.md

# Ovis2

## Overview

The [Ovis2](https://github.com/AIDC-AI/Ovis) is an updated version of the [Ovis](https://huggingface.co/papers/2405.20797) model developed by the AIDC-AI team at Alibaba International Digital Commerce Group.

Ovis2 is the latest advancement in multi-modal large language models (MLLMs), succeeding Ovis1.6. It retains the architectural design of the Ovis series, which focuses on aligning visual and textual embeddings, and introduces major improvements in data curation and training methods.

 Ovis2 architecture.

This model was contributed by [thisisiron](https://huggingface.co/thisisiron).

## Usage example

```python

from PIL import Image
import requests
import torch
from torchvision import io
from typing import Dict
from transformers.image_utils import load_images, load_video
from transformers import AutoModelForImageTextToText, AutoTokenizer, AutoProcessor
from accelerate import Accelerator

device = Accelerator().device

model = AutoModelForImageTextToText.from_pretrained(
    "thisisiron/Ovis2-2B-hf",
    dtype=torch.bfloat16,
).eval().to(device)
processor = AutoProcessor.from_pretrained("thisisiron/Ovis2-2B-hf")

messages = [
    {
        "role": "user",
        "content": [
            {"type": "image"},
            {"type": "text", "text": "Describe the image."},
        ],
    },
]
url = "http://images.cocodataset.org/val2014/COCO_val2014_000000537955.jpg"
image = Image.open(requests.get(url, stream=True).raw)
messages = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
print(messages)

inputs = processor(
    images=[image],
    text=messages,
    return_tensors="pt",
)
inputs = inputs.to(model.device)
inputs['pixel_values'] = inputs['pixel_values'].to(torch.bfloat16)

with torch.inference_mode():
    output_ids = model.generate(**inputs, max_new_tokens=128, do_sample=False)
    generated_ids = [output_ids[len(input_ids):] for input_ids, output_ids in zip(inputs.input_ids, output_ids)]
    output_text = processor.batch_decode(generated_ids, skip_special_tokens=True)
    print(output_text)
```

## Ovis2Config[[transformers.Ovis2Config]]

#### transformers.Ovis2Config[[transformers.Ovis2Config]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/ovis2/configuration_ovis2.py#L109)

This is the configuration class to store the configuration of a [Ovis2ForConditionalGeneration](/docs/transformers/v5.0.0rc1/en/model_doc/ovis2#transformers.Ovis2ForConditionalGeneration). It is used to instantiate a
Ovis2 model according to the specified arguments, defining the model architecture. Instantiating a configuration
with the defaults will yield a similar configuration to that of Ovis2.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

e.g. [thisisiron/Ovis2-1B-hf](https://huggingface.co/thisisiron/Ovis2-1B-hf)

```python
>>> from transformers import Ovis2ForConditionalGeneration, Ovis2Config

>>> # Initializing a Ovis2 style configuration
>>> configuration = Ovis2Config()

>>> # Initializing a model from the Ovis2-2B style configuration
>>> model = Ovis2ForConditionalGeneration(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

vision_config (`Union[AutoConfig, dict]`,  *optional*, defaults to `Ovis2VisionConfig`) : The config object or dictionary of the vision backbone.

text_config (`Union[AutoConfig, dict]`, *optional*, defaults to `Qwen2Config`) : The config object or dictionary of the text backbone.

image_token_id (`int`, *optional*, defaults to 151665) : The image token id to encode the image prompt.

visual_indicator_token_ids (`List[int]`, *optional*, defaults to `[151666, 151667, 151668, 151669, 151670]`) : The visual indicator token ids to encode the image prompt.

vocab_size (`int`, *optional*, defaults to 151643) : Vocabulary size of the text model.

hidden_size (`int`, *optional*, defaults to 1536) : Dimensionality of the encoder layers and the pooler layer.

## Ovis2VisionConfig[[transformers.Ovis2VisionConfig]]

#### transformers.Ovis2VisionConfig[[transformers.Ovis2VisionConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/ovis2/configuration_ovis2.py#L20)

This is the configuration class to store the configuration of a `Ovis2VisionModel`. It is used to instantiate a
Ovis2VisionModel model according to the specified arguments, defining the model architecture. Instantiating a configuration
with the defaults will yield a similar configuration to that of Ovis2.

**Parameters:**

hidden_size (`int`, *optional*, defaults to 1024) : Dimensionality of the encoder layers and the pooler layer.

intermediate_size (`int`, *optional*, defaults to 2816) : Dimensionality of the "intermediate" (i.e., feed-forward) layer in the Transformer encoder.

num_hidden_layers (`int`, *optional*, defaults to 24) : Number of hidden layers in the Transformer encoder.

num_attention_heads (`int`, *optional*, defaults to 8) : Number of attention heads for each attention layer in the Transformer encoder.

num_channels (`int`, *optional*, defaults to 3) : Number of channels in the input images.

image_size (`int`, *optional*, defaults to 224) : The size (resolution) of each image.

patch_size (`int`, *optional*, defaults to 14) : The size (resolution) of each patch.

rms_norm_eps (`float`, *optional*, defaults to 1e-05) : The epsilon used by the RMSNorm layers.

attention_dropout (`float`, *optional*, defaults to 0.0) : The dropout ratio for the attention probabilities.

qkv_bias (`bool`, *optional*, defaults to `False`) : Whether to add a learnable bias to the query, key, and value sequences at each attention head.

mlp_bias (`bool`, *optional*, defaults to `False`) : Whether to add a learnable bias to the MLP layers.

hidden_act (`str` or `function`, *optional*, defaults to `"silu"`) : The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`, `"relu"`, `"selu"` and `"gelu_new"` `"quick_gelu"` are supported.

vocab_size (`int`, *optional*, defaults to 16384) : Vocabulary size of the Vision Transformer.

hidden_stride (`int`, *optional*, defaults to 1) : The stride of the hidden layer in the Vision Transformer.

num_visual_indicator_tokens (`int`, *optional*, defaults to 5) : Number of visual indicator tokens.

initializer_range (`float`, *optional*, defaults to 0.02) : The standard deviation of the truncated normal initializer for initializing all weight matrices.

tokenize_function (`str`, *optional*, defaults to `"softmax"`) : The function used to tokenize the visual indicator tokens.

## Ovis2Model[[transformers.Ovis2Model]]

#### transformers.Ovis2Model[[transformers.Ovis2Model]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/ovis2/modeling_ovis2.py#L501)

The Ovis2 model which consists of a vision backbone and a language model, without a language modeling head.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.Ovis2Model.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/ovis2/modeling_ovis2.py#L586[{"name": "input_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "pixel_values", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "attention_mask", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "position_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "past_key_values", "val": ": typing.Optional[transformers.cache_utils.Cache] = None"}, {"name": "inputs_embeds", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "labels", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "use_cache", "val": ": typing.Optional[bool] = None"}, {"name": "output_attentions", "val": ": typing.Optional[bool] = None"}, {"name": "output_hidden_states", "val": ": typing.Optional[bool] = None"}, {"name": "return_dict", "val": ": typing.Optional[bool] = None"}, {"name": "cache_position", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "logits_to_keep", "val": ": typing.Union[int, torch.Tensor] = 0"}, {"name": "**kwargs", "val": ""}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **pixel_values** (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`, *optional*) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [Ovis2ImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/ovis2#transformers.Ovis2ImageProcessor). See [Ovis2ImageProcessor.__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details ([Ovis2Processor](/docs/transformers/v5.0.0rc1/en/model_doc/ovis2#transformers.Ovis2Processor) uses
  [Ovis2ImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/ovis2#transformers.Ovis2ImageProcessor) for processing images).
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

  Only [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).
  If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.

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
- **output_attentions** (`bool`, *optional*) --
  Whether or not to return the attentions tensors of all attention layers. See `attentions` under returned
  tensors for more detail.
- **output_hidden_states** (`bool`, *optional*) --
  Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
  more detail.
- **return_dict** (`bool`, *optional*) --
  Whether or not to return a [ModelOutput](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.utils.ModelOutput) instead of a plain tuple.
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.
- **logits_to_keep** (`Union[int, torch.Tensor]`, defaults to `0`) --
  If an `int`, compute logits for the last `logits_to_keep` tokens. If `0`, calculate logits for all
  `input_ids` (special case). Only last token logits are needed for generation, and calculating them only for that
  token can save memory, which becomes pretty significant for long sequences or large vocabulary size.
  If a `torch.Tensor`, must be 1D corresponding to the indices to keep in the sequence length dimension.
  This is useful when using packed tensor format (single dimension for batch and sequence length).0`transformers.models.ovis2.modeling_ovis2.Ovis2ModelOutputWithPast` or `tuple(torch.FloatTensor)`A `transformers.models.ovis2.modeling_ovis2.Ovis2ModelOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Ovis2Config](/docs/transformers/v5.0.0rc1/en/model_doc/ovis2#transformers.Ovis2Config)) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) -- Sequence of hidden-states at the output of the last layer of the model.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
  `past_key_values` input) to speed up sequential decoding.
- **hidden_states** (`tuple[torch.FloatTensor, ...]`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple[torch.FloatTensor, ...]`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
- **image_hidden_states** (`torch.FloatTensor`, *optional*) -- A `torch.FloatTensor` of size `(batch_size, num_images, sequence_length, hidden_size)`.
  image_hidden_states of the model produced by the vision encoder and after projecting the last hidden state.
The [Ovis2Model](/docs/transformers/v5.0.0rc1/en/model_doc/ovis2#transformers.Ovis2Model) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

**Parameters:**

config ([Ovis2Config](/docs/transformers/v5.0.0rc1/en/model_doc/ovis2#transformers.Ovis2Config)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``transformers.models.ovis2.modeling_ovis2.Ovis2ModelOutputWithPast` or `tuple(torch.FloatTensor)``

A `transformers.models.ovis2.modeling_ovis2.Ovis2ModelOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Ovis2Config](/docs/transformers/v5.0.0rc1/en/model_doc/ovis2#transformers.Ovis2Config)) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) -- Sequence of hidden-states at the output of the last layer of the model.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
  `past_key_values` input) to speed up sequential decoding.
- **hidden_states** (`tuple[torch.FloatTensor, ...]`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple[torch.FloatTensor, ...]`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
- **image_hidden_states** (`torch.FloatTensor`, *optional*) -- A `torch.FloatTensor` of size `(batch_size, num_images, sequence_length, hidden_size)`.
  image_hidden_states of the model produced by the vision encoder and after projecting the last hidden state.
#### get_image_features[[transformers.Ovis2Model.get_image_features]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/ovis2/modeling_ovis2.py#L521)

Obtains image last hidden states from the vision tower and apply multimodal projection.

**Parameters:**

pixel_values (`torch.FloatTensor]` of shape `(batch_size, channels, height, width)`) : The tensors corresponding to the input images.

vision_feature_layer (`Union[int, list[int]]`, *optional*) : The index of the layer to select the vision feature. If multiple indices are provided, the vision feature of the corresponding indices will be concatenated to form the vision features.

vision_feature_select_strategy (`str`, *optional*) : The feature selection strategy used to select the vision feature from the vision backbone. Can be one of `"default"` or `"full"`

**Returns:**

`image_features (`torch.Tensor`)`

Image feature tensor of shape `(num_images, image_length, embed_dim)`).
#### get_placeholder_mask[[transformers.Ovis2Model.get_placeholder_mask]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/ovis2/modeling_ovis2.py#L562)

Obtains multimodal placeholder mask from `input_ids` or `inputs_embeds`, and checks that the placeholder token count is
equal to the length of multimodal features. If the lengths are different, an error is raised.

## Ovis2ForConditionalGeneration[[transformers.Ovis2ForConditionalGeneration]]

#### transformers.Ovis2ForConditionalGeneration[[transformers.Ovis2ForConditionalGeneration]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/ovis2/modeling_ovis2.py#L666)

The Ovis2 Model for token generation conditioned on other modalities (e.g. image-text-to-text generation).

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.Ovis2ForConditionalGeneration.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/ovis2/modeling_ovis2.py#L688[{"name": "input_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "pixel_values", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "attention_mask", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "position_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "past_key_values", "val": ": typing.Optional[transformers.cache_utils.Cache] = None"}, {"name": "inputs_embeds", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "labels", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "use_cache", "val": ": typing.Optional[bool] = None"}, {"name": "output_attentions", "val": ": typing.Optional[bool] = None"}, {"name": "output_hidden_states", "val": ": typing.Optional[bool] = None"}, {"name": "return_dict", "val": ": typing.Optional[bool] = None"}, {"name": "cache_position", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "logits_to_keep", "val": ": typing.Union[int, torch.Tensor] = 0"}, {"name": "**kwargs", "val": ""}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **pixel_values** (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`, *optional*) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [Ovis2ImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/ovis2#transformers.Ovis2ImageProcessor). See [Ovis2ImageProcessor.__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details ([Ovis2Processor](/docs/transformers/v5.0.0rc1/en/model_doc/ovis2#transformers.Ovis2Processor) uses
  [Ovis2ImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/ovis2#transformers.Ovis2ImageProcessor) for processing images).
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

  Only [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).
  If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.

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
- **output_attentions** (`bool`, *optional*) --
  Whether or not to return the attentions tensors of all attention layers. See `attentions` under returned
  tensors for more detail.
- **output_hidden_states** (`bool`, *optional*) --
  Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
  more detail.
- **return_dict** (`bool`, *optional*) --
  Whether or not to return a [ModelOutput](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.utils.ModelOutput) instead of a plain tuple.
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.
- **logits_to_keep** (`Union[int, torch.Tensor]`, defaults to `0`) --
  If an `int`, compute logits for the last `logits_to_keep` tokens. If `0`, calculate logits for all
  `input_ids` (special case). Only last token logits are needed for generation, and calculating them only for that
  token can save memory, which becomes pretty significant for long sequences or large vocabulary size.
  If a `torch.Tensor`, must be 1D corresponding to the indices to keep in the sequence length dimension.
  This is useful when using packed tensor format (single dimension for batch and sequence length).0`transformers.models.ovis2.modeling_ovis2.Ovis2CausalLMOutputWithPast` or `tuple(torch.FloatTensor)`A `transformers.models.ovis2.modeling_ovis2.Ovis2CausalLMOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Ovis2Config](/docs/transformers/v5.0.0rc1/en/model_doc/ovis2#transformers.Ovis2Config)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
  `past_key_values` input) to speed up sequential decoding.
- **hidden_states** (`tuple[torch.FloatTensor]`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple[torch.FloatTensor]`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
- **image_hidden_states** (`torch.FloatTensor`, *optional*) -- A `torch.FloatTensor` of size (batch_size * num_patches, num_images, sequence_length, hidden_size)`.
  image_hidden_states of the model produced by the vision encoder and after projecting the last hidden state.
The [Ovis2ForConditionalGeneration](/docs/transformers/v5.0.0rc1/en/model_doc/ovis2#transformers.Ovis2ForConditionalGeneration) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Example:

```python
>>> from PIL import Image
>>> import requests
>>> from transformers import AutoProcessor, Ovis2ForConditionalGeneration

>>> model = Ovis2ForConditionalGeneration.from_pretrained("thisisiron/Ovis2-2B-hf")
>>> processor = AutoProcessor.from_pretrained("thisisiron/Ovis2-2B-hf")

>>> prompt = "user\n\nDescribe the image.\nassistant\n"
>>> url = "http://images.cocodataset.org/val2014/COCO_val2014_000000537955.jpg"
>>> image = Image.open(requests.get(url, stream=True).raw)

>>> inputs = processor(images=image, text=prompt, return_tensors="pt")

>>> # Generate
>>> generate_ids = model.generate(**inputs, max_new_tokens=15)
>>> processor.batch_decode(generate_ids, skip_special_tokens=True)[0]
"user\n\nDescribe the image.\nassistant\nThe image features a brown dog standing on a wooden floor, looking up with"
```

**Parameters:**

config ([Ovis2Config](/docs/transformers/v5.0.0rc1/en/model_doc/ovis2#transformers.Ovis2Config)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``transformers.models.ovis2.modeling_ovis2.Ovis2CausalLMOutputWithPast` or `tuple(torch.FloatTensor)``

A `transformers.models.ovis2.modeling_ovis2.Ovis2CausalLMOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Ovis2Config](/docs/transformers/v5.0.0rc1/en/model_doc/ovis2#transformers.Ovis2Config)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
  `past_key_values` input) to speed up sequential decoding.
- **hidden_states** (`tuple[torch.FloatTensor]`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple[torch.FloatTensor]`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
- **image_hidden_states** (`torch.FloatTensor`, *optional*) -- A `torch.FloatTensor` of size (batch_size * num_patches, num_images, sequence_length, hidden_size)`.
  image_hidden_states of the model produced by the vision encoder and after projecting the last hidden state.

## Ovis2ImageProcessor[[transformers.Ovis2ImageProcessor]]

#### transformers.Ovis2ImageProcessor[[transformers.Ovis2ImageProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/ovis2/image_processing_ovis2.py#L202)

Constructs a Ovis2 image processor.

crop_image_to_patchestransformers.Ovis2ImageProcessor.crop_image_to_patcheshttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/ovis2/image_processing_ovis2.py#L497[{"name": "images", "val": ": ndarray"}, {"name": "min_patches", "val": ": int"}, {"name": "max_patches", "val": ": int"}, {"name": "use_covering_area_grid", "val": ": bool = True"}, {"name": "patch_size", "val": ": typing.Union[tuple, int, dict, NoneType] = None"}, {"name": "data_format", "val": ": typing.Optional[transformers.image_utils.ChannelDimension] = None"}, {"name": "covering_threshold", "val": ": float = 0.9"}]- **images** (`np.ndarray`) --
  The image to be cropped.
- **min_patches** (`int`) --
  The minimum number of patches to be extracted from the image.
- **max_patches** (`int`) --
  The maximum number of patches to be extracted from the image.
- **use_covering_area_grid** (`bool`, *optional*, defaults to `True`) --
  Whether to use the covering area grid to determine the number of patches.
- **patch_size** (`int`, `Tuple[int, int]`, `dict`, *optional*) --
  The size of the output patches.
- **data_format** (`ChannelDimension`, *optional*) --
  The format of the image data. If `None`, the format is inferred from the input image.
- **covering_threshold** (`float`, *optional*, defaults to `0.9`) --
  The threshold for the covering area grid. If the covering area is less than this value, the grid is
  considered invalid.0List`PIL.Image.Image` or List[np.ndarray]The list of cropped images.

Crop the image to patches and return a list of cropped images.
The number of patches and their grid arrangement are determined by the original image size,
the target patch size and the minimum and maximum number of patches.
The aspect ratio of the patches grid is chosen to be the closest to the original image aspect ratio.

**Parameters:**

do_resize (`bool`, *optional*, defaults to `True`) : Whether to resize the image's (height, width) dimensions to the specified `size`. Can be overridden by the `do_resize` parameter in the `preprocess` method.

size (`dict`, *optional*, defaults to `{"height" : 384, "width": 384}`): Size of the output image after resizing. Can be overridden by the `size` parameter in the `preprocess` method.

crop_to_patches (`bool`, *optional*, defaults to `False`) : Whether to crop the image to patches. Can be overridden by the `crop_to_patches` parameter in the `preprocess` method.

min_patches (`int`, *optional*, defaults to 1) : The minimum number of patches to be extracted from the image. Only has an effect if `crop_to_patches` is set to `True`. Can be overridden by the `min_patches` parameter in the `preprocess` method.

max_patches (`int`, *optional*, defaults to 12) : The maximum number of patches to be extracted from the image. Only has an effect if `crop_to_patches` is set to `True`. Can be overridden by the `max_patches` parameter in the `preprocess` method.

resample (`PILImageResampling`, *optional*, defaults to `Resampling.BICUBIC`) : Resampling filter to use if resizing the image. Only has an effect if `do_resize` is set to `True`. Can be overridden by the `resample` parameter in the `preprocess` method.

do_rescale (`bool`, *optional*, defaults to `True`) : Whether to rescale the image by the specified scale `rescale_factor`. Can be overridden by the `do_rescale` parameter in the `preprocess` method.

rescale_factor (`int` or `float`, *optional*, defaults to `1/255`) : Scale factor to use if rescaling the image. Only has an effect if `do_rescale` is set to `True`. Can be overridden by the `rescale_factor` parameter in the `preprocess` method.

do_normalize (`bool`, *optional*, defaults to `True`) : Whether to normalize the image. Can be overridden by the `do_normalize` parameter in the `preprocess` method. Can be overridden by the `do_normalize` parameter in the `preprocess` method.

image_mean (`float` or `List[float]`, *optional*, defaults to `IMAGENET_STANDARD_MEAN`) : Mean to use if normalizing the image. This is a float or list of floats the length of the number of channels in the image. Can be overridden by the `image_mean` parameter in the `preprocess` method. Can be overridden by the `image_mean` parameter in the `preprocess` method.

image_std (`float` or `List[float]`, *optional*, defaults to `IMAGENET_STANDARD_STD`) : Standard deviation to use if normalizing the image. This is a float or list of floats the length of the number of channels in the image. Can be overridden by the `image_std` parameter in the `preprocess` method. Can be overridden by the `image_std` parameter in the `preprocess` method.

do_convert_rgb (`bool`, *optional*, defaults to `True`) : Whether to convert the image to RGB.

use_covering_area_grid (`bool`, *optional*, defaults to `True`) : Whether to use the covering area grid to determine the number of patches. Only has an effect if `crop_to_patches` is set to `True`. Can be overridden by the `use_covering_area_grid` parameter in the `preprocess` method.

**Returns:**

`List`PIL.Image.Image` or List[np.ndarray]`

The list of cropped images.
#### preprocess[[transformers.Ovis2ImageProcessor.preprocess]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/ovis2/image_processing_ovis2.py#L335)

Preprocess an image or batch of images.

**Parameters:**

images (`ImageInput`) : Image to preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If passing in images with pixel values between 0 and 1, set `do_rescale=False`.

do_resize (`bool`, *optional*, defaults to `self.do_resize`) : Whether to resize the image.

size (`Dict[str, int]`, *optional*, defaults to `self.size`) : Controls the size of the image after `resize`. The shortest edge of the image is resized to `size["shortest_edge"]` whilst preserving the aspect ratio. If the longest edge of this resized image is > `int(size["shortest_edge"] * (1333 / 800))`, then the image is resized again to make the longest edge equal to `int(size["shortest_edge"] * (1333 / 800))`.

crop_to_patches (`bool`, *optional*, defaults to `self.crop_to_patches`) : Whether to crop the image to patches.

min_patches (`int`, *optional*, defaults to `self.min_patches`) : The minimum number of patches to be extracted from the image. Only has an effect if `crop_to_patches` is set to `True`.

max_patches (`int`, *optional*, defaults to `self.max_patches`) : The maximum number of patches to be extracted from the image. Only has an effect if `crop_to_patches` is set to `True`.

resample (`PILImageResampling`, *optional*, defaults to `self.resample`) : Resampling filter to use if resizing the image. Only has an effect if `do_resize` is set to `True`.

do_rescale (`bool`, *optional*, defaults to `self.do_rescale`) : Whether to rescale the image values between [0 - 1].

rescale_factor (`float`, *optional*, defaults to `self.rescale_factor`) : Rescale factor to rescale the image by if `do_rescale` is set to `True`.

do_normalize (`bool`, *optional*, defaults to `self.do_normalize`) : Whether to normalize the image.

image_mean (`float` or `List[float]`, *optional*, defaults to `self.image_mean`) : Image mean to normalize the image by if `do_normalize` is set to `True`.

image_std (`float` or `List[float]`, *optional*, defaults to `self.image_std`) : Image standard deviation to normalize the image by if `do_normalize` is set to `True`.

do_convert_rgb (`bool`, *optional*, defaults to `self.do_convert_rgb`) : Whether to convert the image to RGB.

return_tensors (`str` or `TensorType`, *optional*) : The type of tensors to return. Can be one of: - Unset: Return a list of `np.ndarray`. - `TensorType.PYTORCH` or `'pt'`: Return a batch of type `torch.Tensor`. - `TensorType.NUMPY` or `'np'`: Return a batch of type `np.ndarray`.

data_format (`ChannelDimension` or `str`, *optional*, defaults to `ChannelDimension.FIRST`) : The channel dimension format for the output image. Can be one of: - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format. - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format. - Unset: Use the channel dimension format of the input image.

input_data_format (`ChannelDimension` or `str`, *optional*) : The channel dimension format for the input image. If unset, the channel dimension format is inferred from the input image. Can be one of: - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format. - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format. - `"none"` or `ChannelDimension.NONE`: image in (height, width) format.

use_covering_area_grid (`bool`, *optional*, defaults to `True`) : Whether to use the covering area grid to determine the number of patches. Only has an effect if `crop_to_patches` is set to `True`.
#### resize[[transformers.Ovis2ImageProcessor.resize]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/ovis2/image_processing_ovis2.py#L287)

Resize an image to `(size["height"], size["width"])`.

**Parameters:**

image (`np.ndarray`) : Image to resize.

size (`Dict[str, int]`) : Dictionary in the format `{"height": int, "width": int}` specifying the size of the output image.

resample (`PILImageResampling`, *optional*, defaults to `PILImageResampling.BICUBIC`) : `PILImageResampling` filter to use when resizing the image e.g. `PILImageResampling.BICUBIC`.

data_format (`ChannelDimension` or `str`, *optional*) : The channel dimension format for the output image. If unset, the channel dimension format of the input image is used. Can be one of: - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format. - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format. - `"none"` or `ChannelDimension.NONE`: image in (height, width) format.

input_data_format (`ChannelDimension` or `str`, *optional*) : The channel dimension format for the input image. If unset, the channel dimension format is inferred from the input image. Can be one of: - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format. - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format. - `"none"` or `ChannelDimension.NONE`: image in (height, width) format.

**Returns:**

``np.ndarray``

The resized image.

## Ovis2ImageProcessorFast[[transformers.Ovis2ImageProcessorFast]]

#### transformers.Ovis2ImageProcessorFast[[transformers.Ovis2ImageProcessorFast]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/ovis2/image_processing_ovis2_fast.py#L43)

Constructs a fast Ovis2 image processor.

crop_image_to_patchestransformers.Ovis2ImageProcessorFast.crop_image_to_patcheshttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/ovis2/image_processing_ovis2_fast.py#L63[{"name": "images", "val": ": torch.Tensor"}, {"name": "min_patches", "val": ": int"}, {"name": "max_patches", "val": ": int"}, {"name": "use_covering_area_grid", "val": ": bool = True"}, {"name": "covering_threshold", "val": ": float = 0.9"}, {"name": "patch_size", "val": ": typing.Union[tuple, int, dict, NoneType] = None"}, {"name": "interpolation", "val": ": typing.Optional[ForwardRef('F.InterpolationMode')] = None"}]- **images** (`torch.Tensor`) --
  The images to be cropped.
- **min_patches** (`int`) --
  The minimum number of patches to be extracted from the image.
- **max_patches** (`int`) --
  The maximum number of patches to be extracted from the image.
- **use_covering_area_grid** (`bool`, *optional*, defaults to `True`) --
  Whether to use the original OVIS2 approach: compute the minimal number of tiles that cover at least 90%
  of the image area. If `False`, the closest aspect ratio to the target is used.
- **covering_threshold** (`float`, *optional*, defaults to `0.9`) --
  The threshold for the covering area. Only has an effect if `use_covering_area_grid` is set to `True`.
- **patch_size** (`int`, `Tuple[int, int]`, `dict`, *optional*) --
  The size of the output patches.
  The format of the image data. If `None`, the format is inferred from the input image.
- **interpolation** (`InterpolationMode`) --
  Resampling filter to use if resizing the image.0List`PIL.Image.Image` or List[np.ndarray]The list of cropped images.

Crop the images to patches and return a list of cropped images.
The number of patches and their grid arrangement are determined by the original image size,
the target patch size and the minimum and maximum number of patches.
The aspect ratio of the patches grid is chosen to be the closest to the original image aspect ratio.

**Parameters:**

images (`torch.Tensor`) : The images to be cropped.

min_patches (`int`) : The minimum number of patches to be extracted from the image.

max_patches (`int`) : The maximum number of patches to be extracted from the image.

use_covering_area_grid (`bool`, *optional*, defaults to `True`) : Whether to use the original OVIS2 approach: compute the minimal number of tiles that cover at least 90% of the image area. If `False`, the closest aspect ratio to the target is used.

covering_threshold (`float`, *optional*, defaults to `0.9`) : The threshold for the covering area. Only has an effect if `use_covering_area_grid` is set to `True`.

patch_size (`int`, `Tuple[int, int]`, `dict`, *optional*) : The size of the output patches. The format of the image data. If `None`, the format is inferred from the input image.

interpolation (`InterpolationMode`) : Resampling filter to use if resizing the image.

**Returns:**

`List`PIL.Image.Image` or List[np.ndarray]`

The list of cropped images.
#### preprocess[[transformers.Ovis2ImageProcessorFast.preprocess]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/ovis2/image_processing_ovis2_fast.py#L59)

**Parameters:**

images (`Union[PIL.Image.Image, numpy.ndarray, torch.Tensor, list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor']]`) : Image to preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If passing in images with pixel values between 0 and 1, set `do_rescale=False`.

do_convert_rgb (`bool`, *optional*) : Whether to convert the image to RGB.

do_resize (`bool`, *optional*) : Whether to resize the image.

size (`Annotated[Union[int, list[int], tuple[int, ...], dict[str, int], NoneType], None]`) : Describes the maximum input dimensions to the model.

crop_size (`Annotated[Union[int, list[int], tuple[int, ...], dict[str, int], NoneType], None]`) : Size of the output image after applying `center_crop`.

resample (`Annotated[Union[PILImageResampling, int, NoneType], None]`) : Resampling filter to use if resizing the image. This can be one of the enum `PILImageResampling`. Only has an effect if `do_resize` is set to `True`.

do_rescale (`bool`, *optional*) : Whether to rescale the image.

rescale_factor (`float`, *optional*) : Rescale factor to rescale the image by if `do_rescale` is set to `True`.

do_normalize (`bool`, *optional*) : Whether to normalize the image.

image_mean (`Union[float, list[float], tuple[float, ...], NoneType]`) : Image mean to use for normalization. Only has an effect if `do_normalize` is set to `True`.

image_std (`Union[float, list[float], tuple[float, ...], NoneType]`) : Image standard deviation to use for normalization. Only has an effect if `do_normalize` is set to `True`.

do_pad (`bool`, *optional*) : Whether to pad the image. Padding is done either to the largest size in the batch or to a fixed square size per image. The exact padding strategy depends on the model.

pad_size (`Annotated[Union[int, list[int], tuple[int, ...], dict[str, int], NoneType], None]`) : The size in `{"height": int, "width" int}` to pad the images to. Must be larger than any image size provided for preprocessing. If `pad_size` is not provided, images will be padded to the largest height and width in the batch. Applied only when `do_pad=True.`

do_center_crop (`bool`, *optional*) : Whether to center crop the image.

data_format (`Union[~image_utils.ChannelDimension, str, NoneType]`) : Only `ChannelDimension.FIRST` is supported. Added for compatibility with slow processors.

input_data_format (`Union[~image_utils.ChannelDimension, str, NoneType]`) : The channel dimension format for the input image. If unset, the channel dimension format is inferred from the input image. Can be one of: - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format. - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format. - `"none"` or `ChannelDimension.NONE`: image in (height, width) format.

device (`Annotated[Union[str, torch.device, NoneType], None]`) : The device to process the images on. If unset, the device is inferred from the input images.

return_tensors (`Annotated[Union[str, ~utils.generic.TensorType, NoneType], None]`) : Returns stacked tensors if set to `pt, otherwise returns a list of tensors.

disable_grouping (`bool`, *optional*) : Whether to disable grouping of images by size to process them individually and not in batches. If None, will be set to True if the images are on CPU, and False otherwise. This choice is based on empirical observations, as detailed here: https://github.com/huggingface/transformers/pull/38157

image_seq_length (`int`, *optional*) : The number of image tokens to be used for each image in the input. Added for backward compatibility but this should be set as a processor attribute in future models.

crop_to_patches (`bool`, *optional*, defaults to `False`) : Whether to crop the image to patches. Can be overridden by the `crop_to_patches` parameter in the `preprocess` method.

min_patches (`int`, *optional*, defaults to 1) : The minimum number of patches to be extracted from the image. Only has an effect if `crop_to_patches` is set to `True`. Can be overridden by the `min_patches` parameter in the `preprocess` method.

max_patches (`int`, *optional*, defaults to 12) : The maximum number of patches to be extracted from the image. Only has an effect if `crop_to_patches` is set to `True`. Can be overridden by the `max_patches` parameter in the `preprocess` method.

use_covering_area_grid (`bool`, *optional*, defaults to `True`) : Whether to use the covering area grid to determine the number of patches. Only has an effect if `crop_to_patches` is set to `True`. Can be overridden by the `use_covering_area_grid` parameter in the `preprocess` method.

**Returns:**

````

- **data** (`dict`) -- Dictionary of lists/arrays/tensors returned by the __call__ method ('pixel_values', etc.).
- **tensor_type** (`Union[None, str, TensorType]`, *optional*) -- You can give a tensor_type here to convert the lists of integers in PyTorch/Numpy Tensors at
  initialization.

## Ovis2Processor[[transformers.Ovis2Processor]]

#### transformers.Ovis2Processor[[transformers.Ovis2Processor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/ovis2/processing_ovis2.py#L37)

Constructs a Ovis2 processor which wraps Ovis2 image processor and a Qwen2 tokenizer into a single processor.

[Ovis2Processor](/docs/transformers/v5.0.0rc1/en/model_doc/ovis2#transformers.Ovis2Processor) offers all the functionalities of `Ovis2VideoProcessor`, [Ovis2ImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/ovis2#transformers.Ovis2ImageProcessor) and [Qwen2TokenizerFast](/docs/transformers/v5.0.0rc1/en/model_doc/qwen2#transformers.Qwen2Tokenizer). See the
`__call__()` and [decode()](/docs/transformers/v5.0.0rc1/en/model_doc/ovis2#transformers.Ovis2Processor.decode) for more information.

batch_decodetransformers.Ovis2Processor.batch_decodehttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/ovis2/processing_ovis2.py#L156[{"name": "*args", "val": ""}, {"name": "**kwargs", "val": ""}]

This method forwards all its arguments to Qwen2TokenizerFast's [batch_decode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.batch_decode). Please
refer to the docstring of this method for more information.

**Parameters:**

image_processor ([Ovis2ImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/ovis2#transformers.Ovis2ImageProcessor), *optional*) : The image processor is a required input.

tokenizer ([Qwen2TokenizerFast](/docs/transformers/v5.0.0rc1/en/model_doc/qwen2#transformers.Qwen2Tokenizer), *optional*) : The tokenizer is a required input.

chat_template (`str`, *optional*) : A Jinja template which will be used to convert lists of messages in a chat into a tokenizable string.

image_token (`str`, *optional*, defaults to `""`) : Special token used to denote image location.

image_seq_length (`int`, *optional*, defaults to 256) : The number of image tokens to be used for each image in the input.
#### decode[[transformers.Ovis2Processor.decode]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/ovis2/processing_ovis2.py#L163)

This method forwards all its arguments to Qwen2TokenizerFast's [decode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.decode). Please refer to
the docstring of this method for more information.

