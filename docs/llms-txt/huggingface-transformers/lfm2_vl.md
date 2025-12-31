# Source: https://huggingface.co/docs/transformers/v5.0.0rc1/model_doc/lfm2_vl.md

# LFM2-VL

## Overview

[LFM2-VL](https://www.liquid.ai/blog/lfm2-vl-efficient-vision-language-models) first series of vision-language foundation models developed by [Liquid AI](https://liquid.ai/). These multimodal models are designed for low-latency and device-aware deployment. LFM2-VL extends the LFM2 family of open-weight Liquid Foundation Models (LFMs) into the vision-language space, supporting both text and image inputs with variable resolutions.

## Architecture

LFM2-VL consists of three main components: a language model backbone, a vision encoder, and a multimodal projector. LFM2-VL builds upon the LFM2 backbone, inheriting from either LFM2-1.2B (for LFM2-VL-1.6B) or LFM2-350M (for LFM2-VL-450M). For the vision tower, LFM2-VL uses SigLIP2 NaFlex encoders to convert input images into token sequences. Two variants are implemented:

* Shape-optimized (400M) for more fine-grained vision capabilities for LFM2-VL-1.6B
* Base (86M) for fast image processing for LFM2-VL-450M

The encoder processes images at their native resolution up to 512×512 pixels, efficiently handling smaller images without upscaling and supporting non-standard aspect ratios without distortion. Larger images are split into non-overlapping square patches of 512×512 each, preserving detail. In LFM2-VL-1.6B, the model also receives a thumbnail (a small, downscaled version of the original image capturing the overall scene) to enhance global context understanding and alignment. Special tokens mark each patch’s position and indicate the thumbnail’s start. The multimodal connector is a 2-layer MLP connector with pixel unshuffle to reduce image token count.

## Example

The following example shows how to generate an answer using the `AutoModelForImageTextToText` class.

```python
from transformers import AutoProcessor, AutoModelForImageTextToText
\
# Load model and processor
model_id = "LiquidAI/LFM2-VL-1.6B"
model = AutoModelForImageTextToText.from_pretrained(
    model_id,
    device_map="auto",
    dtype="bfloat16",
)
processor = AutoProcessor.from_pretrained(model_id)

# Load image and create conversation
conversation = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": "https://www.ilankelman.org/stopsigns/australia.jpg"},
            {"type": "text", "text": "What is in this image?"},
        ],
    },
]

# Generate snswer
inputs = processor.apply_chat_template(
    conversation,
    add_generation_prompt=True,
    return_tensors="pt",
    return_dict=True,
    tokenize=True,
).to(model.device)

outputs = model.generate(**inputs, max_new_tokens=64)
processor.batch_decode(outputs, skip_special_tokens=True)[0]

```

## Lfm2VlImageProcessorFast[[transformers.Lfm2VlImageProcessorFast]]

#### transformers.Lfm2VlImageProcessorFast[[transformers.Lfm2VlImageProcessorFast]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/lfm2_vl/image_processing_lfm2_vl_fast.py#L193)

Constructs a fast Lfm2 Vl image processor.

crop_image_to_patchestransformers.Lfm2VlImageProcessorFast.crop_image_to_patcheshttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/lfm2_vl/image_processing_lfm2_vl_fast.py#L258[{"name": "image", "val": ": torch.Tensor"}, {"name": "min_tiles", "val": ": int"}, {"name": "max_tiles", "val": ": int"}, {"name": "tile_size", "val": ": int"}, {"name": "use_thumbnail", "val": ": bool"}, {"name": "thumbnail_size", "val": ": tuple"}, {"name": "interpolation", "val": ": F.InterpolationMode = None"}, {"name": "antialias", "val": ": bool = True"}, {"name": "**kwargs", "val": ""}]

Processes a high resolution image into patches.
This method splits a high resolution image into a grid of smaller patches while trying to maintain
the original aspect ratio. It finds the optimal grid configuration within the specified tile constraints.
#### smart_resize[[transformers.Lfm2VlImageProcessorFast.smart_resize]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/lfm2_vl/image_processing_lfm2_vl_fast.py#L307)

Rescales the image so that the following conditions are met:
1. Both dimensions (height and width) are divisible by 'encoder_patch_size' * 'downsample_factor'.
   This ensures no padding is needed in the downsampling step.
2. The total number of pixels is within the range ['smart_resize_min_pixels', 'smart_resize_max_pixels'].
3. The aspect ratio of the image is maintained as closely as possible.

## Lfm2VlProcessor[[transformers.Lfm2VlProcessor]]

#### transformers.Lfm2VlProcessor[[transformers.Lfm2VlProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/lfm2_vl/processing_lfm2_vl.py#L52)

Constructs a Lfm2Vl processor which wraps a Lfm2Tokenizer tokenizer and Lfm2VlImageProcessor into a single processor.

[Lfm2VlProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/lfm2_vl#transformers.Lfm2VlProcessor) offers all the functionalities of `Lfm2ImageProcessor` and `Lfm2Tokenizer`.

batch_decodetransformers.Lfm2VlProcessor.batch_decodehttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/lfm2_vl/processing_lfm2_vl.py#L226[{"name": "*args", "val": ""}, {"name": "**kwargs", "val": ""}]

This method forwards all its arguments to LFM2Tokeniser's [batch_decode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.batch_decode). Please
refer to the docstring of this method for more information.

**Parameters:**

image_processor (`Lfm2VlImageProcessor`) : An instance of `Lfm2VlImageProcessor`. The image processor is a required input.

tokenizer (`PreTrainedTokenizerBase`) : An instance of [PreTrainedTokenizerBase](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase). This should correspond with the model's text model. The tokenizer is a required input.

chat_template (`str`, *optional*) : A Jinja template which will be used to convert lists of messages in a chat into a tokenizable string.
#### decode[[transformers.Lfm2VlProcessor.decode]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/lfm2_vl/processing_lfm2_vl.py#L234)

This method forwards all its arguments to LFM2Tokeniser's [decode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.decode). Please refer to
the docstring of this method for more information.

## Lfm2VlConfig[[transformers.Lfm2VlConfig]]

#### transformers.Lfm2VlConfig[[transformers.Lfm2VlConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/lfm2_vl/configuration_lfm2_vl.py#L25)

This is the configuration class to store the configuration of a [Lfm2VlForConditionalGeneration](/docs/transformers/v5.0.0rc1/en/model_doc/lfm2_vl#transformers.Lfm2VlForConditionalGeneration). It is used to instantiate an
Lfm2Vl model according to the specified arguments, defining the model architecture. Instantiating a configuration
with the defaults will yield a similar configuration to that of the Lfm2-VL-1.6B.

e.g. [LiquidAI/LFM2-VL-1.6B](https://huggingface.co/LiquidAI/LFM2-VL-1.6B)

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

**Parameters:**

vision_config (`AutoConfig | dict`,  *optional*, defaults to `Siglip2ImageConfig`) : The config object or dictionary of the vision backbone.

text_config (`AutoConfig | dict`, *optional*, defaults to `Lfm2Config`) : The config object or dictionary of the text backbone.

image_token_id (`int`, *optional*, defaults to 396) : The image token index to encode the image prompt.

projector_hidden_act (`str`, *optional*, defaults to `"gelu"`) : The activation function used by the multimodal projector.

projector_hidden_size (`int`, *optional*, defaults to 2560) : The hidden size of the multimodal projector.

projector_bias (`bool`, *optional*, defaults to `True`) : Whether to use bias in the multimodal projector.

downsample_factor (`int`, *optional*, defaults to 2) : The downsample_factor factor of the vision backbone.

## Lfm2VlModel[[transformers.Lfm2VlModel]]

#### transformers.Lfm2VlModel[[transformers.Lfm2VlModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/lfm2_vl/modeling_lfm2_vl.py#L147)

The Lfm2Vl model which consists of a vision backbone and a language model, without a language modeling head.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.Lfm2VlModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/lfm2_vl/modeling_lfm2_vl.py#L235[{"name": "input_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "attention_mask", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "position_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "pixel_values", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "spatial_shapes", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "pixel_attention_mask", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "past_key_values", "val": ": typing.Optional[transformers.cache_utils.Cache] = None"}, {"name": "inputs_embeds", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "use_cache", "val": ": typing.Optional[bool] = None"}, {"name": "cache_position", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **attention_mask** (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.

  [What are attention masks?](../glossary#attention-mask)
- **position_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of positions of each input sequence tokens in the position embeddings. Selected in the range `[0, config.n_positions - 1]`.

  [What are position IDs?](../glossary#position-ids)
- **pixel_values** (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`, *optional*) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  `image_processor_class`. See `image_processor_class.__call__` for details ([Lfm2VlProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/lfm2_vl#transformers.Lfm2VlProcessor) uses
  `image_processor_class` for processing images).
- **spatial_shapes** (`torch.Tensor` of shape `(batch_size, 2)`, *optional*) --
  The spatial shapes of the input images.
- **pixel_attention_mask** (`torch.Tensor` of shape `(batch_size, height, width)`, *optional*) --
  The pixel attention mask of the input images.
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
- **use_cache** (`bool`, *optional*) --
  If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
  `past_key_values`).
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.0`transformers.models.lfm2_vl.modeling_lfm2_vl.Lfm2VlModelOutputWithPast` or `tuple(torch.FloatTensor)`A `transformers.models.lfm2_vl.modeling_lfm2_vl.Lfm2VlModelOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Lfm2VlConfig](/docs/transformers/v5.0.0rc1/en/model_doc/lfm2_vl#transformers.Lfm2VlConfig)) and inputs.

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
The [Lfm2VlModel](/docs/transformers/v5.0.0rc1/en/model_doc/lfm2_vl#transformers.Lfm2VlModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

**Parameters:**

config ([Lfm2VlConfig](/docs/transformers/v5.0.0rc1/en/model_doc/lfm2_vl#transformers.Lfm2VlConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``transformers.models.lfm2_vl.modeling_lfm2_vl.Lfm2VlModelOutputWithPast` or `tuple(torch.FloatTensor)``

A `transformers.models.lfm2_vl.modeling_lfm2_vl.Lfm2VlModelOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Lfm2VlConfig](/docs/transformers/v5.0.0rc1/en/model_doc/lfm2_vl#transformers.Lfm2VlConfig)) and inputs.

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

## Lfm2VlForConditionalGeneration[[transformers.Lfm2VlForConditionalGeneration]]

#### transformers.Lfm2VlForConditionalGeneration[[transformers.Lfm2VlForConditionalGeneration]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/lfm2_vl/modeling_lfm2_vl.py#L302)

The LFM2_VL model which consists of a vision backbone and a language model.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.Lfm2VlForConditionalGeneration.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/lfm2_vl/modeling_lfm2_vl.py#L335[{"name": "input_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "pixel_values", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "spatial_shapes", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "pixel_attention_mask", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "attention_mask", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "position_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "past_key_values", "val": ": typing.Optional[transformers.cache_utils.Cache] = None"}, {"name": "inputs_embeds", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "labels", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "use_cache", "val": ": typing.Optional[bool] = None"}, {"name": "cache_position", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "logits_to_keep", "val": ": typing.Union[int, torch.Tensor] = 0"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]

pixel_values (`torch.FloatTensor` of shape `(batch_size, channels, height, width)`, *optional*):
The input image tensors.
spatial_shapes (`torch.Tensor` of shape `(batch_size, 2)`, *optional*):
The spatial shapes of the input images.
pixel_attention_mask (`torch.Tensor` of shape `(batch_size, height, width)`, *optional*):
The pixel attention mask of the input images.
labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
Labels for computing the masked language modeling loss. Indices should either be in `[0, ...,
config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored
(masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.

Example:

```python
>>> from PIL import Image
>>> import requests
>>> from transformers import AutoProcessor, AutoModelForImageTextToText
>>> from transformers.image_utils import load_image

>>> model = AutoModelForImageTextToText.from_pretrained(
...     "LiquidAI/LFM2-VL-1.6B",
... )
>>> processor = AutoProcessor.from_pretrained(
...     "LiquidAI/LFM2-VL-1.6B",
... )

>>> url = "https://www.ilankelman.org/stopsigns/australia.jpg"
>>> image = load_image(url)

>>> conversation = [
...     {
...         "role": "user",
...         "content": [
...             {"type": "image", "image": image},
...             {"type": "text", "text": "What is in this image?"},
...         ],
...     },
... ]

>>> inputs = processor.apply_chat_template(
...     conversation,
...     add_generation_prompt=True,
...     tokenize=True,
...     return_dict=True,
...     return_tensors="pt"
... )

>>> # Generate
>>> outputs = model.generate(**inputs, max_new_tokens=45)
>>> processor.batch_decode(outputs, skip_special_tokens=True)[0]
'This image depicts a vibrant street scene in what appears to be a Chinatown or similar cultural area. The focal point is a large red stop sign with white lettering, mounted on a pole.'
```

**Parameters:**

config ([Lfm2VlConfig](/docs/transformers/v5.0.0rc1/en/model_doc/lfm2_vl#transformers.Lfm2VlConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

