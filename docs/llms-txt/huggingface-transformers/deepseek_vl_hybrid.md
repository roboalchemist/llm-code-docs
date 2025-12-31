# Source: https://huggingface.co/docs/transformers/v5.0.0rc1/model_doc/deepseek_vl_hybrid.md

# DeepseekVLHybrid

[Deepseek-VL-Hybrid](https://huggingface.co/papers/2403.05525) was introduced by the DeepSeek AI team. It is a vision-language model (VLM) designed to process both text and images for generating contextually relevant responses. The model leverages [LLaMA](./llama) as its text encoder, while [SigLip](./siglip) is used for encoding low-resolution images and [SAM (Segment Anything Model)](./sam) is incorporated to handle high-resolution image encoding, enhancing the model's ability to process fine-grained visual details. Deepseek-VL-Hybrid is a variant of Deepseek-VL that uses [SAM (Segment Anything Model)](./sam) to handle high-resolution image encoding.

You can find all the original Deepseek-VL-Hybrid checkpoints under the [DeepSeek-community](https://huggingface.co/deepseek-community) organization.

> [!TIP]
> Click on the Deepseek-VL-Hybrid models in the right sidebar for more examples of how to apply Deepseek-VL-Hybrid to different vision and language tasks.

The example below demonstrates how to generate text based on an image with [Pipeline](/docs/transformers/v5.0.0rc1/en/main_classes/pipelines#transformers.Pipeline) or the [AutoModel](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoModel) class.

```py
import torch
from transformers import pipeline

pipe = pipeline(
    task="image-text-to-text",
    model="deepseek-community/deepseek-vl-7b-chat",
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
from transformers import DeepseekVLHybridForConditionalGeneration, AutoProcessor

model = DeepseekVLHybridForConditionalGeneration.from_pretrained(
    "deepseek-community/deepseek-vl-7b-chat",
    dtype=torch.float16,
    device_map="auto",
    attn_implementation="sdpa"
)

processor = AutoProcessor.from_pretrained("deepseek-community/deepseek-vl-7b-chat")

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
from transformers import TorchAoConfig, DeepseekVLHybridForConditionalGeneration, AutoProcessor

quantization_config = TorchAoConfig(
    "int4_weight_only",
    group_size=128
)

model = DeepseekVLHybridForConditionalGeneration.from_pretrained(
    "deepseek-community/deepseek-vl-7b-chat",
    dtype=torch.bfloat16,
    device_map="auto",
    quantization_config=quantization_config
)
```

### Notes

- Do inference with multiple images in a single conversation.

    ```py
    import torch
    from transformers import DeepseekVLHybridForConditionalGeneration, AutoProcessor

    model = DeepseekVLHybridForConditionalGeneration.from_pretrained(
        "deepseek-community/deepseek-vl-7b-chat",
        dtype=torch.float16,
        device_map="auto",
        attn_implementation="sdpa"
    )

    processor = AutoProcessor.from_pretrained("deepseek-community/deepseek-vl-7b-chat")

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

## DeepseekVLHybridConfig[[transformers.DeepseekVLHybridConfig]]

#### transformers.DeepseekVLHybridConfig[[transformers.DeepseekVLHybridConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/deepseek_vl_hybrid/configuration_deepseek_vl_hybrid.py#L31)

This is the configuration class to store the configuration of a [DeepseekVLHybridModel](/docs/transformers/v5.0.0rc1/en/model_doc/deepseek_vl_hybrid#transformers.DeepseekVLHybridModel). It is used to instantiate a
DeepseekVLHybrid model according to the specified arguments, defining the model architecture. Instantiating a configuration
with the defaults will yield a similar configuration to that of the DeepseekVLHybrid
[deepseek-community/deepseek-vl-7b-chat](https://huggingface.co/deepseek-community/deepseek-vl-7b-chat) architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:

```python
>>> from transformers import DeepseekVLHybridConfig, DeepseekVLHybridModel

>>> # Initializing a DeepseekVLHybrid deepseek-community/deepseek-vl-7b-chat style configuration
>>> configuration = DeepseekVLHybridConfig()

>>> # Initializing a model (with random weights) from the deepseek-community/deepseek-vl-7b-chat style configuration
>>> model = DeepseekVLHybridModel(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

text_config (`Union[AutoConfig, dict]`, *optional*, defaults to `LlamaConfig`) : The config object or dictionary of the text backbone.

vision_config (`Union[AutoConfig, dict]`,  *optional*, defaults to `SiglipVisionConfig`) : The config object or dictionary of the vision backbone.

high_res_vision_config (`Union[AutoConfig, dict]`,  *optional*, defaults to `SamVisionConfig`) : The config object or dictionary of the high resolution vision backbone.

image_token_id (`int`, *optional*, defaults to 100015) : The index representing image tokens in the model's token vocabulary.

## DeepseekVLHybridProcessor[[transformers.DeepseekVLHybridProcessor]]

#### transformers.DeepseekVLHybridProcessor[[transformers.DeepseekVLHybridProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/deepseek_vl_hybrid/processing_deepseek_vl_hybrid.py#L36)

Constructs a DeepseekVLHybrid processor which wraps a DeepseekVLHybrid Image Processor and a Llama tokenizer into a single processor.

[DeepseekVLHybridProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/deepseek_vl_hybrid#transformers.DeepseekVLHybridProcessor) offers all the functionalities of [DeepseekVLHybridImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/deepseek_vl_hybrid#transformers.DeepseekVLHybridImageProcessor) and [LlamaTokenizerFast](/docs/transformers/v5.0.0rc1/en/model_doc/llama2#transformers.LlamaTokenizer). See the
`__call__()` and [decode()](/docs/transformers/v5.0.0rc1/en/model_doc/deepseek_vl_hybrid#transformers.DeepseekVLHybridProcessor.decode) for more information.

batch_decodetransformers.DeepseekVLHybridProcessor.batch_decodehttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/deepseek_vl_hybrid/processing_deepseek_vl_hybrid.py#L130[{"name": "*args", "val": ""}, {"name": "**kwargs", "val": ""}]

This method forwards all its arguments to LlamaTokenizerFast's [batch_decode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.batch_decode). Please
refer to the docstring of this method for more information.

**Parameters:**

image_processor ([DeepseekVLHybridImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/deepseek_vl_hybrid#transformers.DeepseekVLHybridImageProcessor)) : The image processor is a required input.

tokenizer ([LlamaTokenizerFast](/docs/transformers/v5.0.0rc1/en/model_doc/llama2#transformers.LlamaTokenizer)) : The tokenizer is a required input.

chat_template (`str`, *optional*) : A Jinja template which will be used to convert lists of messages in a chat into a tokenizable string.

num_image_tokens (`int`, *optional*, defaults to 576) : The number of special image tokens used as placeholders for visual content in text sequences.
#### decode[[transformers.DeepseekVLHybridProcessor.decode]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/deepseek_vl_hybrid/processing_deepseek_vl_hybrid.py#L137)

This method forwards all its arguments to LlamaTokenizerFast's [decode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.decode). Please refer to
the docstring of this method for more information.

## DeepseekVLHybridImageProcessor[[transformers.DeepseekVLHybridImageProcessor]]

#### transformers.DeepseekVLHybridImageProcessor[[transformers.DeepseekVLHybridImageProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/deepseek_vl_hybrid/image_processing_deepseek_vl_hybrid.py#L79)

Constructs a DEEPSEEK_VL_HYBRID image processor.

pad_to_squaretransformers.DeepseekVLHybridImageProcessor.pad_to_squarehttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/deepseek_vl_hybrid/image_processing_deepseek_vl_hybrid.py#L446[{"name": "image", "val": ": ndarray"}, {"name": "background_color", "val": ": typing.Union[int, tuple[int, int, int]] = 0"}, {"name": "data_format", "val": ": typing.Union[str, transformers.image_utils.ChannelDimension, NoneType] = None"}, {"name": "input_data_format", "val": ": typing.Union[str, transformers.image_utils.ChannelDimension, NoneType] = None"}]- **image** (`np.ndarray`) --
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

high_res_size (`dict`, *optional*, defaults to `{"height" : 1024, "width": 1024}`): Size of the high resolution output image after resizing. Can be overridden by the `high_res_size` parameter in the `preprocess` method.

min_size (`int`, *optional*, defaults to 14) : The minimum allowed size for the resized image. Ensures that neither the height nor width falls below this value after resizing.

resample (`PILImageResampling`, *optional*, defaults to `Resampling.BICUBIC`) : Resampling filter to use if resizing the image. Only has an effect if `do_resize` is set to `True`. Can be overridden by the `resample` parameter in the `preprocess` method.

high_res_resample (`PILImageResampling`, *optional*, defaults to `Resampling.BICUBIC`) : Resampling filter to use if resizing the image. Only has an effect if `do_resize` is set to `True`. Can be overridden by the `high_res_resample` parameter in the `preprocess` method.

do_rescale (`bool`, *optional*, defaults to `True`) : Whether to rescale the image by the specified scale `rescale_factor`. Can be overridden by the `do_rescale` parameter in the `preprocess` method.

rescale_factor (`int` or `float`, *optional*, defaults to `1/255`) : Scale factor to use if rescaling the image. Only has an effect if `do_rescale` is set to `True`. Can be overridden by the `rescale_factor` parameter in the `preprocess` method.

do_normalize (`bool`, *optional*, defaults to `True`) : Whether to normalize the image. Can be overridden by the `do_normalize` parameter in the `preprocess` method. Can be overridden by the `do_normalize` parameter in the `preprocess` method.

image_mean (`float` or `list[float]`, *optional*, defaults to `IMAGENET_STANDARD_MEAN`) : Mean to use if normalizing the image. This is a float or list of floats the length of the number of channels in the image. Can be overridden by the `image_mean` parameter in the `preprocess` method. Can be overridden by the `image_mean` parameter in the `preprocess` method.

image_std (`float` or `list[float]`, *optional*, defaults to `IMAGENET_STANDARD_STD`) : Standard deviation to use if normalizing the image. This is a float or list of floats the length of the number of channels in the image. Can be overridden by the `image_std` parameter in the `preprocess` method. Can be overridden by the `image_std` parameter in the `preprocess` method.

high_res_image_mean (`float` or `list[float]`, *optional*, defaults to `OPENAI_CLIP_MEAN`) : Mean to use if normalizing the high resolution image. This is a float or list of floats the length of the number of channels in the image. Can be overridden by the `high_res_image_mean` parameter in the `preprocess` method.

high_res_image_std (`float` or `list[float]`, *optional*, defaults to `OPENAI_CLIP_STD`) : Standard deviation to use if normalizing the high resolution image. This is a float or list of floats the length of the number of channels in the image. Can be overridden by the `high_res_image_std` parameter in the `preprocess` method.

do_convert_rgb (`bool`, *optional*, defaults to `True`) : Whether to convert the image to RGB.

do_pad (`bool`, *optional*, defaults to `True`) : Whether to pad the image to square or not.

**Returns:**

``np.ndarray``

The padded image.
#### preprocess[[transformers.DeepseekVLHybridImageProcessor.preprocess]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/deepseek_vl_hybrid/image_processing_deepseek_vl_hybrid.py#L253)

Preprocess an image or batch of images.

**Parameters:**

images (`ImageInput`) : Image to preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If passing in images with pixel values between 0 and 1, set `do_rescale=False`.

do_resize (`bool`, *optional*, defaults to `self.do_resize`) : Whether to resize the image.

size (`Dict[str, int]`, *optional*, defaults to `self.size`) : Dictionary in the format `{"height": h, "width": w}` specifying the size of the output image after resizing.

high_res_size (`Dict[str, int]`, *optional*, defaults to `self.high_res_size`) : Dictionary in the format `{"height": h, "width": w}` specifying the size of the high resolution output image after resizing.

resample (`PILImageResampling` filter, *optional*, defaults to `self.resample`) : `PILImageResampling` filter to use if resizing the image e.g. `PILImageResampling.BILINEAR`. Only has an effect if `do_resize` is set to `True`.

high_res_resample (`PILImageResampling` filter, *optional*, defaults to `self.resample`) : `PILImageResampling` filter to use if resizing the image e.g. `PILImageResampling.BICUBIC`. Only has an effect if `do_resize` is set to `True`.

do_rescale (`bool`, *optional*, defaults to `self.do_rescale`) : Whether to rescale the image values between [0 - 1].

rescale_factor (`float`, *optional*, defaults to `self.rescale_factor`) : Rescale factor to rescale the image by if `do_rescale` is set to `True`.

do_normalize (`bool`, *optional*, defaults to `self.do_normalize`) : Whether to normalize the image.

image_mean (`float` or `List[float]`, *optional*, defaults to `self.image_mean`) : Image mean to use if `do_normalize` is set to `True`.

image_std (`float` or `List[float]`, *optional*, defaults to `self.image_std`) : Image standard deviation to use if `do_normalize` is set to `True`.

high_res_image_mean (`float` or `List[float]`, *optional*, defaults to `self.high_res_image_mean`) : Image mean to use if `do_normalize` is set to `True`.

high_res_image_std (`float` or `List[float]`, *optional*, defaults to `self.high_res_image_std`) : Image standard deviation to use if `do_normalize` is set to `True`.

return_tensors (`str` or `TensorType`, *optional*) : The type of tensors to return. Can be one of: - Unset: Return a list of `np.ndarray`. - `TensorType.PYTORCH` or `'pt'`: Return a batch of type `torch.Tensor`. - `TensorType.NUMPY` or `'np'`: Return a batch of type `np.ndarray`.

data_format (`ChannelDimension` or `str`, *optional*, defaults to `ChannelDimension.FIRST`) : The channel dimension format for the output image. Can be one of: - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format. - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format. - Unset: Use the channel dimension format of the input image.

input_data_format (`ChannelDimension` or `str`, *optional*) : The channel dimension format for the input image. If unset, the channel dimension format is inferred from the input image. Can be one of: - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format. - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format. - `"none"` or `ChannelDimension.NONE`: image in (height, width) format.

do_convert_rgb (`bool`, *optional*, defaults to `self.do_convert_rgb`) : Whether to convert the image to RGB.

do_pad (`bool`, *optional*, defaults to `self.do_pad`) : Whether to pad the image to square or not.

background_color (`tuple[int, int, int]`) : The background color to use for the padding.
#### resize[[transformers.DeepseekVLHybridImageProcessor.resize]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/deepseek_vl_hybrid/image_processing_deepseek_vl_hybrid.py#L188)

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

## DeepseekVLHybridImageProcessorFast[[transformers.DeepseekVLHybridImageProcessorFast]]

#### transformers.DeepseekVLHybridImageProcessorFast[[transformers.DeepseekVLHybridImageProcessorFast]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/deepseek_vl_hybrid/image_processing_deepseek_vl_hybrid_fast.py#L47)

Constructs a fast Deepseek Vl Hybrid image processor.

pad_to_squaretransformers.DeepseekVLHybridImageProcessorFast.pad_to_squarehttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/deepseek_vl_hybrid/image_processing_deepseek_vl_hybrid_fast.py#L104[{"name": "images", "val": ": torch.Tensor"}, {"name": "background_color", "val": ": typing.Union[int, tuple[int, int, int]] = 0"}]- **images** (`torch.Tensor`) --
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

## DeepseekVLHybridModel[[transformers.DeepseekVLHybridModel]]

#### transformers.DeepseekVLHybridModel[[transformers.DeepseekVLHybridModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/deepseek_vl_hybrid/modeling_deepseek_vl_hybrid.py#L243)

The bare Deepseek Vl Hybrid Model outputting raw hidden-states without any specific head on top.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.DeepseekVLHybridModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/deepseek_vl_hybrid/modeling_deepseek_vl_hybrid.py#L302[{"name": "input_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "pixel_values", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "high_res_pixel_values", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "attention_mask", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "position_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "past_key_values", "val": ": typing.Optional[transformers.cache_utils.Cache] = None"}, {"name": "cache_position", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "inputs_embeds", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "use_cache", "val": ": typing.Optional[bool] = None"}, {"name": "logits_to_keep", "val": ": typing.Union[int, torch.Tensor] = 0"}, {"name": "**kwargs", "val": ""}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **pixel_values** (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`, *optional*) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [DeepseekVLHybridImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/deepseek_vl_hybrid#transformers.DeepseekVLHybridImageProcessor). See [DeepseekVLHybridImageProcessor.__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details ([DeepseekVLHybridProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/deepseek_vl_hybrid#transformers.DeepseekVLHybridProcessor) uses
  [DeepseekVLHybridImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/deepseek_vl_hybrid#transformers.DeepseekVLHybridImageProcessor) for processing images).
- **high_res_pixel_values** (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size), *optional*) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [AutoImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoImageProcessor).
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
- **logits_to_keep** (`Union[int, torch.Tensor]`, defaults to `0`) --
  If an `int`, compute logits for the last `logits_to_keep` tokens. If `0`, calculate logits for all
  `input_ids` (special case). Only last token logits are needed for generation, and calculating them only for that
  token can save memory, which becomes pretty significant for long sequences or large vocabulary size.
  If a `torch.Tensor`, must be 1D corresponding to the indices to keep in the sequence length dimension.
  This is useful when using packed tensor format (single dimension for batch and sequence length).0
The [DeepseekVLHybridModel](/docs/transformers/v5.0.0rc1/en/model_doc/deepseek_vl_hybrid#transformers.DeepseekVLHybridModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

**Parameters:**

config ([DeepseekVLHybridModel](/docs/transformers/v5.0.0rc1/en/model_doc/deepseek_vl_hybrid#transformers.DeepseekVLHybridModel)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

## DeepseekVLHybridForConditionalGeneration[[transformers.DeepseekVLHybridForConditionalGeneration]]

#### transformers.DeepseekVLHybridForConditionalGeneration[[transformers.DeepseekVLHybridForConditionalGeneration]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/deepseek_vl_hybrid/modeling_deepseek_vl_hybrid.py#L391)

forwardtransformers.DeepseekVLHybridForConditionalGeneration.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/deepseek_vl_hybrid/modeling_deepseek_vl_hybrid.py#L411[{"name": "input_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "pixel_values", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "high_res_pixel_values", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "attention_mask", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "position_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "past_key_values", "val": ": typing.Optional[transformers.cache_utils.Cache] = None"}, {"name": "cache_position", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "inputs_embeds", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "labels", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "use_cache", "val": ": typing.Optional[bool] = None"}, {"name": "logits_to_keep", "val": ": typing.Union[int, torch.Tensor] = 0"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **pixel_values** (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`, *optional*) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [DeepseekVLHybridImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/deepseek_vl_hybrid#transformers.DeepseekVLHybridImageProcessor). See [DeepseekVLHybridImageProcessor.__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details ([DeepseekVLHybridProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/deepseek_vl_hybrid#transformers.DeepseekVLHybridProcessor) uses
  [DeepseekVLHybridImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/deepseek_vl_hybrid#transformers.DeepseekVLHybridImageProcessor) for processing images).
- **high_res_pixel_values** (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size), *optional*) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [AutoImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoImageProcessor).

  labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
  Labels for computing the masked language modeling loss. Indices should either be in `[0, ...,
  config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored
  (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.
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
- **logits_to_keep** (`Union[int, torch.Tensor]`, defaults to `0`) --
  If an `int`, compute logits for the last `logits_to_keep` tokens. If `0`, calculate logits for all
  `input_ids` (special case). Only last token logits are needed for generation, and calculating them only for that
  token can save memory, which becomes pretty significant for long sequences or large vocabulary size.
  If a `torch.Tensor`, must be 1D corresponding to the indices to keep in the sequence length dimension.
  This is useful when using packed tensor format (single dimension for batch and sequence length).0
The [DeepseekVLHybridForConditionalGeneration](/docs/transformers/v5.0.0rc1/en/model_doc/deepseek_vl_hybrid#transformers.DeepseekVLHybridForConditionalGeneration) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Example:

```python
>>> from PIL import Image
>>> import requests
>>> from transformers import AutoProcessor, DeepseekVLHybridForConditionalGeneration

>>> model = DeepseekVLHybridForConditionalGeneration.from_pretrained("deepseek-community/deepseek-vl-7b-chat")
>>> processor = AutoProcessor.from_pretrained("deepseek-community/deepseek-vl-7b-chat")

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

input_ids (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) : Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.  [What are input IDs?](../glossary#input-ids)

pixel_values (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`, *optional*) : The tensors corresponding to the input images. Pixel values can be obtained using [DeepseekVLHybridImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/deepseek_vl_hybrid#transformers.DeepseekVLHybridImageProcessor). See [DeepseekVLHybridImageProcessor.__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details ([DeepseekVLHybridProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/deepseek_vl_hybrid#transformers.DeepseekVLHybridProcessor) uses [DeepseekVLHybridImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/deepseek_vl_hybrid#transformers.DeepseekVLHybridImageProcessor) for processing images).

high_res_pixel_values (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size), *optional*) : The tensors corresponding to the input images. Pixel values can be obtained using [AutoImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoImageProcessor).  labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*): Labels for computing the masked language modeling loss. Indices should either be in `[0, ..., config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.

attention_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) : Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:  - 1 for tokens that are **not masked**, - 0 for tokens that are **masked**.  [What are attention masks?](../glossary#attention-mask)

position_ids (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) : Indices of positions of each input sequence tokens in the position embeddings. Selected in the range `[0, config.n_positions - 1]`.  [What are position IDs?](../glossary#position-ids)

past_key_values (`~cache_utils.Cache`, *optional*) : Pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention blocks) that can be used to speed up sequential decoding. This typically consists in the `past_key_values` returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.  Only [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache). If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.  The model will output the same cache format that is fed as input.  If `past_key_values` are used, the user is expected to input only unprocessed `input_ids` (those that don't have their past key value states given to this model) of shape `(batch_size, unprocessed_length)` instead of all `input_ids` of shape `(batch_size, sequence_length)`.

cache_position (`torch.LongTensor` of shape `(sequence_length)`, *optional*) : Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`, this tensor is not affected by padding. It is used to update the cache in the correct position and to infer the complete sequence length.

inputs_embeds (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) : Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation. This is useful if you want more control over how to convert `input_ids` indices into associated vectors than the model's internal embedding lookup matrix.

labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) : Labels for computing the masked language modeling loss. Indices should either be in `[0, ..., config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.

use_cache (`bool`, *optional*) : If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see `past_key_values`).

logits_to_keep (`Union[int, torch.Tensor]`, defaults to `0`) : If an `int`, compute logits for the last `logits_to_keep` tokens. If `0`, calculate logits for all `input_ids` (special case). Only last token logits are needed for generation, and calculating them only for that token can save memory, which becomes pretty significant for long sequences or large vocabulary size. If a `torch.Tensor`, must be 1D corresponding to the indices to keep in the sequence length dimension. This is useful when using packed tensor format (single dimension for batch and sequence length).

