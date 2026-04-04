# Source: https://huggingface.co/docs/transformers/v5.0.0/model_doc/deepseek_vl.md

# DeepseekVL

[Deepseek-VL](https://huggingface.co/papers/2403.05525) was introduced by the DeepSeek AI team. It is a vision-language model (VLM) designed to process both text and images for generating contextually relevant responses. The model leverages [LLaMA](./llama) as its text encoder, while [SigLip](./siglip) is used for encoding images.

You can find all the original Deepseek-VL checkpoints under the [DeepSeek-community](https://huggingface.co/deepseek-community) organization.

> [!TIP]
> Click on the Deepseek-VL models in the right sidebar for more examples of how to apply Deepseek-VL to different vision and language tasks.

The example below demonstrates how to generate text based on an image with [Pipeline](/docs/transformers/v5.0.0/en/main_classes/pipelines#transformers.Pipeline) or the [AutoModel](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoModel) class.

```py
import torch
from transformers import pipeline

pipe = pipeline(
    task="image-text-to-text",
    model="deepseek-community/deepseek-vl-1.3b-chat",
    device=0,
    dtype=torch.float16
)

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/pipeline-cat-chonk.jpeg",
            },
            { "type": "text", "text": "Describe this image."},
        ]
    }
]

pipe(text=messages, max_new_tokens=20, return_full_text=False)
```

```py
import torch
from transformers import DeepseekVLForConditionalGeneration, AutoProcessor

model = DeepseekVLForConditionalGeneration.from_pretrained(
    "deepseek-community/deepseek-vl-1.3b-chat",
    dtype=torch.float16,
    device_map="auto",
    attn_implementation="sdpa"
)

processor = AutoProcessor.from_pretrained("deepseek-community/deepseek-vl-1.3b-chat")

messages = [
    {
        "role":"user",
        "content":[
            {
                "type":"image",
                "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/pipeline-cat-chonk.jpeg"
            },
            {
                "type":"text",
                "text":"Describe this image."
            }
        ]
    }

]

inputs = processor.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt"
).to(model.device, dtype=model.dtype)

generated_ids = model.generate(**inputs, max_new_tokens=128)
generated_ids_trimmed = [
    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
]
output_text = processor.batch_decode(
    generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
)

print(output_text)
```

Quantization reduces the memory burden of large models by representing the weights in a lower precision. Refer to the [Quantization](../quantization/overview) overview for more available quantization backends.

The example below uses [torchao](../quantization/torchao) to only quantize the weights to int4.

```python
import torch
from transformers import TorchAoConfig, DeepseekVLForConditionalGeneration, AutoProcessor

quantization_config = TorchAoConfig(
    "int4_weight_only",
    group_size=128
)

model = DeepseekVLForConditionalGeneration.from_pretrained(
    "deepseek-community/deepseek-vl-1.3b-chat",
    dtype=torch.bfloat16,
    device_map="auto",
    quantization_config=quantization_config
)
```

### Notes

- Do inference with multiple images in a single conversation.

    ```py
    import torch
    from transformers import DeepseekVLForConditionalGeneration, AutoProcessor

    model = DeepseekVLForConditionalGeneration.from_pretrained(
        "deepseek-community/deepseek-vl-1.3b-chat",
        dtype=torch.float16,
        device_map="auto",
        attn_implementation="sdpa"
    )

    processor = AutoProcessor.from_pretrained("deepseek-community/deepseek-vl-1.3b-chat")

    messages = [
        [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What’s the difference between"},
                    {"type": "image", "url": "http://images.cocodataset.org/val2017/000000039769.jpg"},
                    {"type": "text", "text": " and "},
                    {"type": "image", "url": "https://www.ilankelman.org/stopsigns/australia.jpg"}
                ]
            }
        ],
        [
            {
                "role": "user",
                "content": [
                    {"type": "image", "url": "https://huggingface.co/microsoft/kosmos-2-patch14-224/resolve/main/snowman.jpg"},
                    {"type": "text", "text": "What do you see in this image?"}
                ]
            }
        ]
    ]

    inputs = processor.apply_chat_template(
        messages,
        add_generation_prompt=True,
        padding=True,
        truncation=True,
        tokenize=True,
        return_dict=True,
        return_tensors="pt"
    ).to(model.device, dtype=model.dtype)

    generated_ids = model.generate(**inputs, max_new_tokens=128)
    generated_ids_trimmed = [
        out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
    ]
    output_text = processor.batch_decode(
        generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
    )

    print(output_text)
    ```

## DeepseekVLConfig[[transformers.DeepseekVLConfig]]

#### transformers.DeepseekVLConfig[[transformers.DeepseekVLConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/deepseek_vl/configuration_deepseek_vl.py#L30)

This is the configuration class to store the configuration of a [DeepseekVLModel](/docs/transformers/v5.0.0/en/model_doc/deepseek_vl#transformers.DeepseekVLModel). It is used to instantiate a
DeepseekVL model according to the specified arguments, defining the model architecture. Instantiating a configuration
with the defaults will yield a similar configuration to that of the DeepseekVL
[deepseek-community/deepseek-vl-1.3b-chat](https://huggingface.co/deepseek-community/deepseek-vl-1.3b-chat) architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:

```python
>>> from transformers import DeepseekVLConfig, DeepseekVLModel

>>> # Initializing a DeepseekVL deepseek-community/deepseek-vl-1.3b-chat style configuration
>>> configuration = DeepseekVLConfig()

>>> # Initializing a model (with random weights) from the deepseek-community/deepseek-vl-1.3b-chat style configuration
>>> model = DeepseekVLModel(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

text_config (`Union[AutoConfig, dict]`, *optional*, defaults to `LlamaConfig`) : The config object or dictionary of the text backbone.

vision_config (`Union[AutoConfig, dict]`,  *optional*, defaults to `SiglipVisionConfig`) : The config object or dictionary of the vision backbone.

image_token_id (`int`, *optional*, defaults to 100015) : The index representing image tokens in the model's token vocabulary.

## DeepseekVLProcessor[[transformers.DeepseekVLProcessor]]

#### transformers.DeepseekVLProcessor[[transformers.DeepseekVLProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/deepseek_vl/processing_deepseek_vl.py#L37)

Constructs a DeepseekVLProcessor which wraps a image processor and a tokenizer into a single processor.

[DeepseekVLProcessor](/docs/transformers/v5.0.0/en/model_doc/deepseek_vl#transformers.DeepseekVLProcessor) offers all the functionalities of [DeepseekVLImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/deepseek_vl#transformers.DeepseekVLImageProcessorFast) and `tokenizer_class`. See the
[~DeepseekVLImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/deepseek_vl#transformers.DeepseekVLImageProcessorFast) and `~tokenizer_class` for more information.

__call__transformers.DeepseekVLProcessor.__call__https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/deepseek_vl/processing_deepseek_vl.py#L54[{"name": "text", "val": ": str | list[str] | list[list[str]] = None"}, {"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor'], NoneType] = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.models.deepseek_vl.processing_deepseek_vl.DeepseekVLProcessorKwargs]"}]- **text** (`Union[str, list, list]`, *optional*) --
  The sequence or batch of sequences to be encoded. Each sequence can be a string or a list of strings
  (pretokenized string). If you pass a pretokenized input, set `is_split_into_words=True` to avoid ambiguity with batched inputs.
- **images** (`Union[PIL.Image.Image, numpy.ndarray, torch.Tensor, list, list, list]`, *optional*) --
  Image to preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If
  passing in images with pixel values between 0 and 1, set `do_rescale=False`.
- **return_tensors** (`str` or [TensorType](/docs/transformers/v5.0.0/en/internal/file_utils#transformers.TensorType), *optional*) --
  If set, will return tensors of a particular framework. Acceptable values are:

  - `'pt'`: Return PyTorch `torch.Tensor` objects.
  - `'np'`: Return NumPy `np.ndarray` objects.0[BatchFeature](/docs/transformers/v5.0.0/en/main_classes/image_processor#transformers.BatchFeature)A [BatchFeature](/docs/transformers/v5.0.0/en/main_classes/image_processor#transformers.BatchFeature) with the following fields:

- **input_ids** -- List of token ids to be fed to a model. Returned when `text` is not `None`.
- **attention_mask** -- List of indices specifying which tokens should be attended to by the model (when
  `return_attention_mask=True` or if *"attention_mask"* is in `self.model_input_names` and if `text` is not
  `None`).
- **pixel_values** -- Pixel values to be fed to a model. Returned when `images` is not `None`.

**Parameters:**

image_processor (`DeepseekVLImageProcessorFast`) : The image processor is a required input.

tokenizer (`tokenizer_class`) : The tokenizer is a required input.

chat_template (`str`) : A Jinja template to convert lists of messages in a chat into a tokenizable string.

num_image_tokens (`int`, *optional*, defaults to 576) : The number of special image tokens used as placeholders for visual content in text sequences.

**Returns:**

`[BatchFeature](/docs/transformers/v5.0.0/en/main_classes/image_processor#transformers.BatchFeature)`

A [BatchFeature](/docs/transformers/v5.0.0/en/main_classes/image_processor#transformers.BatchFeature) with the following fields:

- **input_ids** -- List of token ids to be fed to a model. Returned when `text` is not `None`.
- **attention_mask** -- List of indices specifying which tokens should be attended to by the model (when
  `return_attention_mask=True` or if *"attention_mask"* is in `self.model_input_names` and if `text` is not
  `None`).
- **pixel_values** -- Pixel values to be fed to a model. Returned when `images` is not `None`.

## DeepseekVLImageProcessor[[transformers.DeepseekVLImageProcessor]]

#### transformers.DeepseekVLImageProcessor[[transformers.DeepseekVLImageProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/deepseek_vl/image_processing_deepseek_vl.py#L61)

Constructs a DEEPSEEK_VL image processor.

pad_to_squaretransformers.DeepseekVLImageProcessor.pad_to_squarehttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/deepseek_vl/image_processing_deepseek_vl.py#L357[{"name": "image", "val": ": ndarray"}, {"name": "background_color", "val": ": int | tuple[int, int, int] = 0"}, {"name": "data_format", "val": ": str | transformers.image_utils.ChannelDimension | None = None"}, {"name": "input_data_format", "val": ": str | transformers.image_utils.ChannelDimension | None = None"}]- **image** (`np.ndarray`) --
  The image to pad.
- **background_color** (`int` or `tuple[int, int, int]`, *optional*, defaults to 0) --
  The color to use for the padding. Can be an integer for single channel or a
  tuple of integers representing for multi-channel images. If passed as integer
  in multi-channel mode, it will default to `0` in subsequent channels.
- **data_format** (`str` or `ChannelDimension`, *optional*) --
  The channel dimension format for the output image. Can be one of:
  - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
  - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.
  If unset, will use same as the input image.
- **input_data_format** (`str` or `ChannelDimension`, *optional*) --
  The channel dimension format for the input image. Can be one of:
  - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
  - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.0`np.ndarray`The padded image.

Pads an image to a square based on the longest edge.

**Parameters:**

do_resize (`bool`, *optional*, defaults to `True`) : Whether to resize the image's (height, width) dimensions to the specified `size`. Can be overridden by the `do_resize` parameter in the `preprocess` method.

size (`dict`, *optional*, defaults to `{"height" : 384, "width": 384}`): Size of the output image after resizing. Can be overridden by the `size` parameter in the `preprocess` method.

min_size (`int`, *optional*, defaults to 14) : The minimum allowed size for the resized image. Ensures that neither the height nor width falls below this value after resizing.

resample (`PILImageResampling`, *optional*, defaults to `Resampling.BICUBIC`) : Resampling filter to use if resizing the image. Only has an effect if `do_resize` is set to `True`. Can be overridden by the `resample` parameter in the `preprocess` method.

do_rescale (`bool`, *optional*, defaults to `True`) : Whether to rescale the image by the specified scale `rescale_factor`. Can be overridden by the `do_rescale` parameter in the `preprocess` method.

rescale_factor (`int` or `float`, *optional*, defaults to `1/255`) : Scale factor to use if rescaling the image. Only has an effect if `do_rescale` is set to `True`. Can be overridden by the `rescale_factor` parameter in the `preprocess` method.

do_normalize (`bool`, *optional*, defaults to `True`) : Whether to normalize the image. Can be overridden by the `do_normalize` parameter in the `preprocess` method. Can be overridden by the `do_normalize` parameter in the `preprocess` method.

image_mean (`float` or `list[float]`, *optional*, defaults to `IMAGENET_STANDARD_MEAN`) : Mean to use if normalizing the image. This is a float or list of floats the length of the number of channels in the image. Can be overridden by the `image_mean` parameter in the `preprocess` method. Can be overridden by the `image_mean` parameter in the `preprocess` method.

image_std (`float` or `list[float]`, *optional*, defaults to `IMAGENET_STANDARD_STD`) : Standard deviation to use if normalizing the image. This is a float or list of floats the length of the number of channels in the image. Can be overridden by the `image_std` parameter in the `preprocess` method. Can be overridden by the `image_std` parameter in the `preprocess` method.

do_convert_rgb (`bool`, *optional*, defaults to `True`) : Whether to convert the image to RGB.

do_pad (`bool`, *optional*, defaults to `True`) : Whether to pad the image to square or not.

**Returns:**

``np.ndarray``

The padded image.
#### preprocess[[transformers.DeepseekVLImageProcessor.preprocess]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/deepseek_vl/image_processing_deepseek_vl.py#L206)

Preprocess an image or batch of images.

**Parameters:**

images (`ImageInput`) : Image to preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If passing in images with pixel values between 0 and 1, set `do_rescale=False`.

do_resize (`bool`, *optional*, defaults to `self.do_resize`) : Whether to resize the image.

size (`dict[str, int]`, *optional*, defaults to `self.size`) : Controls the size of the image after `resize`. The shortest edge of the image is resized to `size["shortest_edge"]` whilst preserving the aspect ratio. If the longest edge of this resized image is > `int(size["shortest_edge"] * (1333 / 800))`, then the image is resized again to make the longest edge equal to `int(size["shortest_edge"] * (1333 / 800))`.

resample (`PILImageResampling`, *optional*, defaults to `self.resample`) : Resampling filter to use if resizing the image. Only has an effect if `do_resize` is set to `True`.

do_rescale (`bool`, *optional*, defaults to `self.do_rescale`) : Whether to rescale the image values between [0 - 1].

rescale_factor (`float`, *optional*, defaults to `self.rescale_factor`) : Rescale factor to rescale the image by if `do_rescale` is set to `True`.

do_normalize (`bool`, *optional*, defaults to `self.do_normalize`) : Whether to normalize the image.

image_mean (`float` or `list[float]`, *optional*, defaults to `self.image_mean`) : Image mean to normalize the image by if `do_normalize` is set to `True`.

image_std (`float` or `list[float]`, *optional*, defaults to `self.image_std`) : Image standard deviation to normalize the image by if `do_normalize` is set to `True`.

do_convert_rgb (`bool`, *optional*, defaults to `self.do_convert_rgb`) : Whether to convert the image to RGB.

background_color (`tuple[int, int, int]`) : The background color to use for the padding.

do_pad (`bool`, *optional*, defaults to `self.do_pad`) : Whether to pad the image to square or not.

return_tensors (`str` or `TensorType`, *optional*) : The type of tensors to return. Can be one of: - Unset: Return a list of `np.ndarray`. - `TensorType.PYTORCH` or `'pt'`: Return a batch of type `torch.Tensor`. - `TensorType.NUMPY` or `'np'`: Return a batch of type `np.ndarray`.

data_format (`ChannelDimension` or `str`, *optional*, defaults to `ChannelDimension.FIRST`) : The channel dimension format for the output image. Can be one of: - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format. - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format. - Unset: Use the channel dimension format of the input image.

input_data_format (`ChannelDimension` or `str`, *optional*) : The channel dimension format for the input image. If unset, the channel dimension format is inferred from the input image. Can be one of: - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format. - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format. - `"none"` or `ChannelDimension.NONE`: image in (height, width) format.
#### resize[[transformers.DeepseekVLImageProcessor.resize]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/deepseek_vl/image_processing_deepseek_vl.py#L141)

Resize an image to dynamically calculated size.

**Parameters:**

image (`np.ndarray`) : Image to resize.

size (`dict[str, int]` or `int`) : The size to resize the image to. If a dictionary, it should have the keys `"height"` and `"width"`.

resample (`PILImageResampling`, *optional*, defaults to `PILImageResampling.BICUBIC`) : `PILImageResampling` filter to use when resizing the image e.g. `PILImageResampling.BICUBIC`.

data_format (`ChannelDimension` or `str`, *optional*) : The channel dimension format for the output image. If unset, the channel dimension format of the input image is used. Can be one of: - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format. - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format. - `None`: will be inferred from input

input_data_format (`ChannelDimension` or `str`, *optional*) : The channel dimension format for the input image. If unset, the channel dimension format is inferred from the input image. Can be one of: - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format. - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format. - `"none"` or `ChannelDimension.NONE`: image in (height, width) format.

**Returns:**

``np.ndarray``

The resized image.

## DeepseekVLImageProcessorFast[[transformers.DeepseekVLImageProcessorFast]]

#### transformers.DeepseekVLImageProcessorFast[[transformers.DeepseekVLImageProcessorFast]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/deepseek_vl/image_processing_deepseek_vl_fast.py#L36)

Constructs a fast Deepseek Vl image processor.

pad_to_squaretransformers.DeepseekVLImageProcessorFast.pad_to_squarehttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/deepseek_vl/image_processing_deepseek_vl_fast.py#L83[{"name": "images", "val": ": torch.Tensor"}, {"name": "background_color", "val": ": int | tuple[int, int, int] = 0"}]- **images** (`torch.Tensor`) --
  The images to pad.
- **background_color** (`int` or `tuple[int, int, int]`, *optional*, defaults to 0) --
  The color to use for the padding. Can be an integer for single channel or a
  tuple of integers representing for multi-channel images. If passed as integer
  in multi-channel mode, it will default to `0` in subsequent channels.0`torch.Tensor`The padded images.

Pads an image to a square based on the longest edge.

**Parameters:**

images (`torch.Tensor`) : The images to pad.

background_color (`int` or `tuple[int, int, int]`, *optional*, defaults to 0) : The color to use for the padding. Can be an integer for single channel or a tuple of integers representing for multi-channel images. If passed as integer in multi-channel mode, it will default to `0` in subsequent channels.

**Returns:**

``torch.Tensor``

The padded images.

## DeepseekVLModel[[transformers.DeepseekVLModel]]

#### transformers.DeepseekVLModel[[transformers.DeepseekVLModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/deepseek_vl/modeling_deepseek_vl.py#L136)

The bare Deepseek Vl Model outputting raw hidden-states without any specific head on top.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.DeepseekVLModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/deepseek_vl/modeling_deepseek_vl.py#L190[{"name": "input_ids", "val": ": torch.LongTensor | None = None"}, {"name": "pixel_values", "val": ": torch.FloatTensor | None = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.LongTensor | None = None"}, {"name": "past_key_values", "val": ": transformers.cache_utils.Cache | None = None"}, {"name": "cache_position", "val": ": torch.LongTensor | None = None"}, {"name": "inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "logits_to_keep", "val": ": int | torch.Tensor = 0"}, {"name": "**kwargs", "val": ""}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **pixel_values** (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`, *optional*) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [DeepseekVLImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/deepseek_vl#transformers.DeepseekVLImageProcessorFast). See [DeepseekVLImageProcessorFast.__call__()](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details ([DeepseekVLProcessor](/docs/transformers/v5.0.0/en/model_doc/deepseek_vl#transformers.DeepseekVLProcessor) uses
  [DeepseekVLImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/deepseek_vl#transformers.DeepseekVLImageProcessorFast) for processing images).
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
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.
- **inputs_embeds** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) --
  Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation. This
  is useful if you want more control over how to convert `input_ids` indices into associated vectors than the
  model's internal embedding lookup matrix.
- **use_cache** (`bool`, *optional*) --
  If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
  `past_key_values`).
- **logits_to_keep** (`Union[int, torch.Tensor]`, *optional*, defaults to `0`) --
  If an `int`, compute logits for the last `logits_to_keep` tokens. If `0`, calculate logits for all
  `input_ids` (special case). Only last token logits are needed for generation, and calculating them only for that
  token can save memory, which becomes pretty significant for long sequences or large vocabulary size.
  If a `torch.Tensor`, must be 1D corresponding to the indices to keep in the sequence length dimension.
  This is useful when using packed tensor format (single dimension for batch and sequence length).0`transformers.models.deepseek_vl.modeling_deepseek_vl.DeepseekVLBaseModelOutputWithPast` or `tuple(torch.FloatTensor)`A `transformers.models.deepseek_vl.modeling_deepseek_vl.DeepseekVLBaseModelOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([DeepseekVLConfig](/docs/transformers/v5.0.0/en/model_doc/deepseek_vl#transformers.DeepseekVLConfig)) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.

  If `past_key_values` is used only the last hidden-state of the sequences of shape `(batch_size, 1,
  hidden_size)` is output.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks and optionally if
  `config.is_encoder_decoder=True` in the cross-attention blocks) that can be used (see `past_key_values`
  input) to speed up sequential decoding.
- **hidden_states** (`tuple[torch.FloatTensor] | None.hidden_states`, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple[torch.FloatTensor] | None.attentions`, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
- **image_hidden_states** (`tuple(torch.FloatTensor)`, *optional*) -- Tuple of `torch.FloatTensor` (one for the output of the image embeddings, `(batch_size, num_images,
  sequence_length, hidden_size)`.

  image_hidden_states of the model produced by the vision encoder, and optionally by the perceiver
The [DeepseekVLModel](/docs/transformers/v5.0.0/en/model_doc/deepseek_vl#transformers.DeepseekVLModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

**Parameters:**

config ([DeepseekVLModel](/docs/transformers/v5.0.0/en/model_doc/deepseek_vl#transformers.DeepseekVLModel)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``transformers.models.deepseek_vl.modeling_deepseek_vl.DeepseekVLBaseModelOutputWithPast` or `tuple(torch.FloatTensor)``

A `transformers.models.deepseek_vl.modeling_deepseek_vl.DeepseekVLBaseModelOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([DeepseekVLConfig](/docs/transformers/v5.0.0/en/model_doc/deepseek_vl#transformers.DeepseekVLConfig)) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.

  If `past_key_values` is used only the last hidden-state of the sequences of shape `(batch_size, 1,
  hidden_size)` is output.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks and optionally if
  `config.is_encoder_decoder=True` in the cross-attention blocks) that can be used (see `past_key_values`
  input) to speed up sequential decoding.
- **hidden_states** (`tuple[torch.FloatTensor] | None.hidden_states`, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple[torch.FloatTensor] | None.attentions`, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
- **image_hidden_states** (`tuple(torch.FloatTensor)`, *optional*) -- Tuple of `torch.FloatTensor` (one for the output of the image embeddings, `(batch_size, num_images,
  sequence_length, hidden_size)`.

  image_hidden_states of the model produced by the vision encoder, and optionally by the perceiver
#### get_image_features[[transformers.DeepseekVLModel.get_image_features]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/deepseek_vl/modeling_deepseek_vl.py#L156)

**Parameters:**

pixel_values (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`) : The tensors corresponding to the input images. Pixel values can be obtained using [DeepseekVLImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/deepseek_vl#transformers.DeepseekVLImageProcessorFast). See [DeepseekVLImageProcessorFast.__call__()](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details ([DeepseekVLProcessor](/docs/transformers/v5.0.0/en/model_doc/deepseek_vl#transformers.DeepseekVLProcessor) uses [DeepseekVLImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/deepseek_vl#transformers.DeepseekVLImageProcessorFast) for processing images).

**Returns:**

`[transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([DeepseekVLConfig](/docs/transformers/v5.0.0/en/model_doc/deepseek_vl#transformers.DeepseekVLConfig)) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.
- **pooler_output** (`torch.FloatTensor` of shape `(batch_size, hidden_size)`) -- Last layer hidden-state of the first token of the sequence (classification token) after further processing
  through the layers used for the auxiliary pretraining task. E.g. for BERT-family of models, this returns
  the classification token after processing through a linear layer and a tanh activation function. The linear
  layer weights are trained from the next sentence prediction (classification) objective during pretraining.
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.

## DeepseekVLForConditionalGeneration[[transformers.DeepseekVLForConditionalGeneration]]

#### transformers.DeepseekVLForConditionalGeneration[[transformers.DeepseekVLForConditionalGeneration]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/deepseek_vl/modeling_deepseek_vl.py#L241)

forwardtransformers.DeepseekVLForConditionalGeneration.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/deepseek_vl/modeling_deepseek_vl.py#L261[{"name": "input_ids", "val": ": torch.LongTensor | None = None"}, {"name": "pixel_values", "val": ": torch.FloatTensor | None = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.LongTensor | None = None"}, {"name": "past_key_values", "val": ": transformers.cache_utils.Cache | None = None"}, {"name": "cache_position", "val": ": torch.LongTensor | None = None"}, {"name": "inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "labels", "val": ": torch.LongTensor | None = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "logits_to_keep", "val": ": int | torch.Tensor = 0"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **pixel_values** (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`, *optional*) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [DeepseekVLImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/deepseek_vl#transformers.DeepseekVLImageProcessorFast). See [DeepseekVLImageProcessorFast.__call__()](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details ([DeepseekVLProcessor](/docs/transformers/v5.0.0/en/model_doc/deepseek_vl#transformers.DeepseekVLProcessor) uses
  [DeepseekVLImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/deepseek_vl#transformers.DeepseekVLImageProcessorFast) for processing images).
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
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.
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
- **logits_to_keep** (`Union[int, torch.Tensor]`, *optional*, defaults to `0`) --
  If an `int`, compute logits for the last `logits_to_keep` tokens. If `0`, calculate logits for all
  `input_ids` (special case). Only last token logits are needed for generation, and calculating them only for that
  token can save memory, which becomes pretty significant for long sequences or large vocabulary size.
  If a `torch.Tensor`, must be 1D corresponding to the indices to keep in the sequence length dimension.
  This is useful when using packed tensor format (single dimension for batch and sequence length).0`transformers.models.deepseek_vl.modeling_deepseek_vl.DeepseekVLCausalLMOutputWithPast` or `tuple(torch.FloatTensor)`A `transformers.models.deepseek_vl.modeling_deepseek_vl.DeepseekVLCausalLMOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([DeepseekVLConfig](/docs/transformers/v5.0.0/en/model_doc/deepseek_vl#transformers.DeepseekVLConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
  `past_key_values` input) to speed up sequential decoding.
- **hidden_states** (`tuple[torch.FloatTensor] | None.hidden_states`, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple[torch.FloatTensor] | None.attentions`, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
- **image_hidden_states** (`tuple(torch.FloatTensor)`, *optional*) -- Tuple of `torch.FloatTensor` (one for the output of the image embeddings, `(batch_size, num_images,
  sequence_length, hidden_size)`.

  image_hidden_states of the model produced by the vision encoder, and optionally by the perceiver
The [DeepseekVLForConditionalGeneration](/docs/transformers/v5.0.0/en/model_doc/deepseek_vl#transformers.DeepseekVLForConditionalGeneration) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Example:

```python
>>> from PIL import Image
>>> from transformers import AutoProcessor, DeepseekVLForConditionalGeneration

>>> model = DeepseekVLForConditionalGeneration.from_pretrained("deepseek-community/deepseek-vl-1.3b-chat")
>>> processor = AutoProcessor.from_pretrained("deepseek-community/deepseek-vl-1.3b-chat")

>>> messages = [
...     {
...         "role": "user", "content": [
...             {"type": "image", "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/pipeline-cat-chonk.jpeg"},
...             {"type": "text", "text": "Where is the cat standing?"},
...         ]
...     },
... ]

>>> inputs = processor.apply_chat_template(
...     messages,
...     tokenize=True,
...     return_dict=True,
...     return_tensors="pt",
...     add_generation_prompt=True
... )
>>> # Generate
>>> generate_ids = model.generate(**inputs)
>>> processor.batch_decode(generate_ids, skip_special_tokens=True)[0]
```

**Parameters:**

input_ids (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) : Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.  [What are input IDs?](../glossary#input-ids)

pixel_values (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`, *optional*) : The tensors corresponding to the input images. Pixel values can be obtained using [DeepseekVLImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/deepseek_vl#transformers.DeepseekVLImageProcessorFast). See [DeepseekVLImageProcessorFast.__call__()](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details ([DeepseekVLProcessor](/docs/transformers/v5.0.0/en/model_doc/deepseek_vl#transformers.DeepseekVLProcessor) uses [DeepseekVLImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/deepseek_vl#transformers.DeepseekVLImageProcessorFast) for processing images).

attention_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) : Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:  - 1 for tokens that are **not masked**, - 0 for tokens that are **masked**.  [What are attention masks?](../glossary#attention-mask)

position_ids (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) : Indices of positions of each input sequence tokens in the position embeddings. Selected in the range `[0, config.n_positions - 1]`.  [What are position IDs?](../glossary#position-ids)

past_key_values (`~cache_utils.Cache`, *optional*) : Pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention blocks) that can be used to speed up sequential decoding. This typically consists in the `past_key_values` returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.  Only [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache). If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.  The model will output the same cache format that is fed as input.  If `past_key_values` are used, the user is expected to input only unprocessed `input_ids` (those that don't have their past key value states given to this model) of shape `(batch_size, unprocessed_length)` instead of all `input_ids` of shape `(batch_size, sequence_length)`.

cache_position (`torch.LongTensor` of shape `(sequence_length)`, *optional*) : Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`, this tensor is not affected by padding. It is used to update the cache in the correct position and to infer the complete sequence length.

inputs_embeds (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) : Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation. This is useful if you want more control over how to convert `input_ids` indices into associated vectors than the model's internal embedding lookup matrix.

labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) : Labels for computing the masked language modeling loss. Indices should either be in `[0, ..., config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.

use_cache (`bool`, *optional*) : If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see `past_key_values`).

logits_to_keep (`Union[int, torch.Tensor]`, *optional*, defaults to `0`) : If an `int`, compute logits for the last `logits_to_keep` tokens. If `0`, calculate logits for all `input_ids` (special case). Only last token logits are needed for generation, and calculating them only for that token can save memory, which becomes pretty significant for long sequences or large vocabulary size. If a `torch.Tensor`, must be 1D corresponding to the indices to keep in the sequence length dimension. This is useful when using packed tensor format (single dimension for batch and sequence length).

**Returns:**

``transformers.models.deepseek_vl.modeling_deepseek_vl.DeepseekVLCausalLMOutputWithPast` or `tuple(torch.FloatTensor)``

A `transformers.models.deepseek_vl.modeling_deepseek_vl.DeepseekVLCausalLMOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([DeepseekVLConfig](/docs/transformers/v5.0.0/en/model_doc/deepseek_vl#transformers.DeepseekVLConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
  `past_key_values` input) to speed up sequential decoding.
- **hidden_states** (`tuple[torch.FloatTensor] | None.hidden_states`, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple[torch.FloatTensor] | None.attentions`, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
- **image_hidden_states** (`tuple(torch.FloatTensor)`, *optional*) -- Tuple of `torch.FloatTensor` (one for the output of the image embeddings, `(batch_size, num_images,
  sequence_length, hidden_size)`.

  image_hidden_states of the model produced by the vision encoder, and optionally by the perceiver

