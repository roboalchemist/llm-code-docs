# Source: https://huggingface.co/docs/transformers/v5.0.0/model_doc/ernie4_5_vl_moe.md

# Ernie 4.5 VL MoE

## Overview

The Ernie 4.5 VL MoE model was released in the [Ernie 4.5 Model Family](https://ernie.baidu.com/blog/posts/ernie4.5/) release by baidu.
This family of models contains multiple different architectures and model sizes. The Vision-Language series in specific is
composed of a novel multimodal heterogeneous structure, sharing paremeters across modalities and dedicating parameters
to specific modalities. This becomes especially apparent in the Mixture of Expert (MoE) which is composed of

- Dedicated Text Experts
- Dedicated Vision Experts
- Shared Experts

This architecture has the advantage to enhance multimodal understanding without compromising, and even improving, performance on text-related tasks. An more detailed breakdown is given in the [Technical Report](https://ernie.baidu.com/blog/publication/ERNIE_Technical_Report.pdf).

    

Other models from the family can be found at [Ernie 4.5](./ernie4_5) and at [Ernie 4.5 MoE](./ernie4_5_moe).

## Usage

The example below demonstrates how to generate text based on an image with [Pipeline](/docs/transformers/v5.0.0/en/main_classes/pipelines#transformers.Pipeline) or the [AutoModel](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoModel) class.

```py
from transformers import pipeline

pipe = pipeline(
    task="image-text-to-text",
    model="baidu/ERNIE-4.5-VL-28B-A3B-PT",
    device_map="auto",
    revision="refs/pr/10",
)
message = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "What kind of dog is this?"},
            {
                "type": "image",
                "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/pipeline-cat-chonk.jpeg",
            },
        ],
    }
]
print(pipe(text=message, max_new_tokens=20, return_full_text=False))
```

```py
from transformers import AutoModelForImageTextToText, AutoProcessor

model = AutoModelForImageTextToText.from_pretrained(
    "baidu/ERNIE-4.5-VL-28B-A3B-PT",
    dtype="auto",
    device_map="auto",  # Use tp_plan="auto" instead to enable Tensor Parallelism!
    revision="refs/pr/10",
)
processor = AutoProcessor.from_pretrained(
    "baidu/ERNIE-4.5-VL-28B-A3B-PT",
    # use_fast=False,  # closer to the original implementation for less speed
    revision="refs/pr/10",
)
message = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "What kind of dog is this?"},
            {
                "type": "image",
                "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/pipeline-cat-chonk.jpeg",
            },
        ],
    }
]

inputs = processor.apply_chat_template(
    message,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt"
).to(model.device)

generated_ids = model.generate(**inputs, max_new_tokens=128)
generated_ids_trimmed = [
    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
]
output_text = processor.batch_decode(
    generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
)
print(output_text)
```

Using Ernie 4.5 VL MoE with video input is similar to using it with image input.
The model can process video data and generate text based on the content of the video.

```python
from transformers import AutoModelForImageTextToText, AutoProcessor

model = AutoModelForImageTextToText.from_pretrained(
    "baidu/ERNIE-4.5-VL-28B-A3B-PT",
    dtype="auto",
    device_map="auto",  # Use tp_plan="auto" instead to enable Tensor Parallelism!
    revision="refs/pr/10",
)
processor = AutoProcessor.from_pretrained("baidu/ERNIE-4.5-VL-28B-A3B-PT", revision="refs/pr/10")
message = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "Please describe what you can see during this video."},
            {
                "type": "video",
                "url": "https://huggingface.co/datasets/raushan-testing-hf/videos-test/resolve/main/tiny_video.mp4",
            },
        ],
    }
]

inputs = processor.apply_chat_template(
    message,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt"
).to(model.device)

generated_ids = model.generate(**inputs, max_new_tokens=128)
generated_ids_trimmed = [
    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
]
output_text = processor.batch_decode(
    generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
)
print(output_text)
```

## Ernie4_5_VL_MoeConfig[[transformers.Ernie4_5_VL_MoeConfig]]

#### transformers.Ernie4_5_VL_MoeConfig[[transformers.Ernie4_5_VL_MoeConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/ernie4_5_vl_moe/configuration_ernie4_5_vl_moe.py#L255)

This is the configuration class to store the configuration of a [Ernie4_5_VL_MoeModel](/docs/transformers/v5.0.0/en/model_doc/ernie4_5_vl_moe#transformers.Ernie4_5_VL_MoeModel). It is used to instantiate a
Ernie4.5-VL MoE model according to the specified arguments, defining the model architecture. Instantiating a configuration
with the defaults will yield a similar configuration to that of
Ernie 4.5 VL 28B A3B [baidu/ERNIE-4.5-VL-28B-A3B-PT](https://huggingface.co/baidu/ERNIE-4.5-VL-28B-A3B-PT).

Configuration objects inherit from [PretrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PretrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

```python
>>> from transformers import Ernie4_5_VL_MoeForConditionalGeneration, Ernie4_5_VL_MoeConfig

>>> # Initializing a Ernie4_5_VL_Moe style configuration
>>> configuration = Ernie4_5_VL_MoeConfig()

>>> # Initializing a model from the Ernie 4.5 VL 28B A3B configuration
>>> model = Ernie4_5_VL_MoeForConditionalGeneration(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

text_config (`Union[PreTrainedConfig, dict]`, *optional*, defaults to `Ernie4_5_VL_MoeTextConfig`) : The config object or dictionary of the text backbone.

vision_config (`Union[PreTrainedConfig, dict]`,  *optional*, defaults to `Ernie4_5_VL_MoeVisionConfig`) : The config object or dictionary of the vision backbone.

image_start_token_id (`int`, *optional*, defaults to 101304) : The image token index to encode the start of image.

image_end_token_id (`int`, *optional*, defaults to 101305) : The image token index to encode the end of image.

image_token_id (`int`, *optional*, defaults to 100295) : The image token index to encode the image prompt.

video_start_token_id (`int`, *optional*, defaults to 101306) : The video token index to encode the start of video.

video_end_token_id (`int`, *optional*, defaults to 101307) : The video token index to encode the end of video.

video_token_id (`int`, *optional*, defaults to 103367) : The video token index to encode the video prompt.

tie_word_embeddings (`bool`, *optional*, defaults to `True`) : Whether the model's input and output word embeddings should be tied.

## Ernie4_5_VL_MoeTextConfig[[transformers.Ernie4_5_VL_MoeTextConfig]]

#### transformers.Ernie4_5_VL_MoeTextConfig[[transformers.Ernie4_5_VL_MoeTextConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/ernie4_5_vl_moe/configuration_ernie4_5_vl_moe.py#L98)

This is the configuration class to store the configuration of a [Ernie4_5_VL_MoeTextModel](/docs/transformers/v5.0.0/en/model_doc/ernie4_5_vl_moe#transformers.Ernie4_5_VL_MoeTextModel). It is used to instantiate a
the text model portion of the complete Ernie4.5-VL Moe model according to the specified arguments, defining the model architecture.

Configuration objects inherit from [PretrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PretrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

**Parameters:**

vocab_size (`int`, *optional*, defaults to 103424) : Vocabulary size of the Ernie 4.5 VL model. Defines the number of different tokens that can be represented by the `inputs_ids` passed when calling [Ernie4_5_VL_MoeTextModel](/docs/transformers/v5.0.0/en/model_doc/ernie4_5_vl_moe#transformers.Ernie4_5_VL_MoeTextModel)

hidden_size (`int`, *optional*, defaults to 2560) : Dimension of the hidden representations.

intermediate_size (`int`, *optional*, defaults to 12288) : Dimension of the MLP representations.

num_hidden_layers (`int`, *optional*, defaults to 28) : Number of hidden layers in the Transformer encoder.

num_attention_heads (`int`, *optional*, defaults to 20) : Number of attention heads for each attention layer in the Transformer encoder.

num_key_value_heads (`int`, *optional*, defaults to 4) : This is the number of key_value heads that should be used to implement Grouped Query Attention. If `num_key_value_heads=num_attention_heads`, the model will use Multi Head Attention (MHA), if `num_key_value_heads=1` the model will use Multi Query Attention (MQA) otherwise GQA is used. When converting a multi-head checkpoint to a GQA checkpoint, each group key and value head should be constructed by meanpooling all the original heads within that group. For more details, check out [this paper](https://huggingface.co/papers/2305.13245). If it is not specified, will default to `4`.

hidden_act (`str` or `function`, *optional*, defaults to `"silu"`) : The non-linear activation function (function or string) in the decoder.

max_position_embeddings (`int`, *optional*, defaults to 131072) : The maximum sequence length that this model might ever be used with.

initializer_range (`float`, *optional*, defaults to 0.02) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

rms_norm_eps (`float`, *optional*, defaults to 1e-05) : The epsilon used by the rms normalization layers.

use_cache (`bool`, *optional*, defaults to `True`) : Whether or not the model should return the last key/values attentions (not used by all models). Only relevant if `config.is_decoder=True`.

use_bias (`bool`, *optional*, defaults to `False`) : Whether to use a bias in any of the projections including mlp and attention for example.

rope_parameters (`RopeParameters`, *optional*) : Dictionary containing the configuration parameters for the RoPE embeddings. The dictionaty should contain a value for `rope_theta` and optionally parameters used for scaling in case you want to use RoPE with longer `max_position_embeddings`.

mlp_layer_types (`list`, *optional*) : MLP (Moe vs Dense) pattern for each layer.

moe_intermediate_size (`list[int]`, *optional*, defaults to `[1536, 512]`) : Intermediate size of the routed experts; differs between text (first) and image (second) experts.

moe_k (`int`, *optional*, defaults to 6) : Number of selected experts.

moe_num_experts (`int`, *optional*, defaults to 64) : Number of routed experts.

moe_num_shared_experts (`int`, *optional*, defaults to 2) : The number of experts that are shared for all MoE forwards.

moe_norm_min (`float`, *optional*, defaults to 1e-12) : Minimum division value during routing normalization.

output_router_logits (`bool`, *optional*, defaults to `False`) : Whether or not the router logits should be returned by the model. Enabling this will also allow the model to output the auxiliary loss, including load balancing loss and router z-loss.

router_aux_loss_coef (`float`, *optional*, defaults to 0.001) : The aux loss factor for the total loss.

pad_token_id (`int`, *optional*) : Padding token id.

eos_token_id (`int`, *optional*) : End of stream token id.

bos_token_id (`int`, *optional*) : Beginning of stream token id.

## Ernie4_5_VL_MoeVisionConfig[[transformers.Ernie4_5_VL_MoeVisionConfig]]

#### transformers.Ernie4_5_VL_MoeVisionConfig[[transformers.Ernie4_5_VL_MoeVisionConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/ernie4_5_vl_moe/configuration_ernie4_5_vl_moe.py#L23)

This is the configuration class to store the configuration of the [Ernie4_5_VL_MoeVisionTransformerPretrainedModel](/docs/transformers/v5.0.0/en/model_doc/ernie4_5_vl_moe#transformers.Ernie4_5_VL_MoeVisionTransformerPretrainedModel).
It is used to instantiate the vision models portion of the complete Ernie4.5-VL Moe model according to the specified
arguments, defining the model architecture.

Configuration objects inherit from [PretrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PretrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

**Parameters:**

depth (`int`, *optional*, defaults to 32) : Number of layers (depth) in the model.

hidden_size (`int`, *optional*, defaults to 1280) : Dimensionality of the encoder layers and the pooler layer.

hidden_act (`str` or `function`, *optional*, defaults to `"quick_gelu"`) : The non-linear activation function (function or string) in the encoder and pooler.

intermediate_size (`int`, *optional*, defaults to 5120) : Dimensionality of the "intermediate" (i.e., feed-forward) layer in the Transformer encoder.

num_heads (`int`, *optional*, defaults to 16) : Number of attention heads for each attention layer in the Transformer encoder.

in_channels (`int`, *optional*, defaults to 3) : The number of input channels.

patch_size (`int`, *optional*, defaults to 14) : The size (resolution) of each patch.

spatial_merge_size (`int`, *optional*, defaults to 2) : The size used for merging spatial dimensions.

temporal_merge_size (`int`, *optional*, defaults to 2) : The size used for merge along the temporal dimension.

rms_norm_eps (`float`, *optional*, defaults to 1e-06) : The epsilon used by the rms normalization layers.

initializer_range (`float`, *optional*, defaults to 0.02) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

## Ernie4_5_VL_MoeImageProcessor[[transformers.Ernie4_5_VL_MoeImageProcessor]]

#### transformers.Ernie4_5_VL_MoeImageProcessor[[transformers.Ernie4_5_VL_MoeImageProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/ernie4_5_vl_moe/image_processing_ernie4_5_vl_moe.py#L93)

Constructs a Ernie 4.5 VL image processor that dynamically resizes images based on the original images.

preprocesstransformers.Ernie4_5_VL_MoeImageProcessor.preprocesshttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/ernie4_5_vl_moe/image_processing_ernie4_5_vl_moe.py#L297[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor']]"}, {"name": "do_resize", "val": ": bool | None = None"}, {"name": "size", "val": ": dict[str, int] | None = None"}, {"name": "resample", "val": ": PIL.Image.Resampling | None = None"}, {"name": "do_rescale", "val": ": bool | None = None"}, {"name": "rescale_factor", "val": ": float | None = None"}, {"name": "do_normalize", "val": ": bool | None = None"}, {"name": "image_mean", "val": ": float | list[float] | None = None"}, {"name": "image_std", "val": ": float | list[float] | None = None"}, {"name": "patch_size", "val": ": int | None = None"}, {"name": "temporal_patch_size", "val": ": int | None = None"}, {"name": "merge_size", "val": ": int | None = None"}, {"name": "do_convert_rgb", "val": ": bool | None = None"}, {"name": "return_tensors", "val": ": str | transformers.utils.generic.TensorType | None = None"}, {"name": "data_format", "val": ": transformers.image_utils.ChannelDimension | None = "}, {"name": "input_data_format", "val": ": str | transformers.image_utils.ChannelDimension | None = None"}]- **images** (`ImageInput`) --
  Image to preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If
  passing in images with pixel values between 0 and 1, set `do_rescale=False`.
- **do_resize** (`bool`, *optional*, defaults to `self.do_resize`) --
  Whether to resize the image.
- **size** (`Dict[str, int]`, *optional*, defaults to `self.size`) --
  Size of the image after resizing. Shortest edge of the image is resized to size["shortest_edge"], with
  the longest edge resized to keep the input aspect ratio.
- **resample** (`int`, *optional*, defaults to `self.resample`) --
  Resampling filter to use if resizing the image. This can be one of the enum `PILImageResampling`. Only
  has an effect if `do_resize` is set to `True`.
- **do_rescale** (`bool`, *optional*, defaults to `self.do_rescale`) --
  Whether to rescale the image.
- **rescale_factor** (`float`, *optional*, defaults to `self.rescale_factor`) --
  Rescale factor to rescale the image by if `do_rescale` is set to `True`.
- **do_normalize** (`bool`, *optional*, defaults to `self.do_normalize`) --
  Whether to normalize the image.
- **image_mean** (`float` or `List[float]`, *optional*, defaults to `self.image_mean`) --
  Image mean to use for normalization. Only has an effect if `do_normalize` is set to `True`.
- **image_std** (`float` or `List[float]`, *optional*, defaults to `self.image_std`) --
  Image standard deviation to use for normalization. Only has an effect if `do_normalize` is set to
  `True`.
- **patch_size** (`int`, *optional*, defaults to `self.patch_size`) --
  The spatial patch size of the vision encoder.
- **temporal_patch_size** (`int`, *optional*, defaults to `self.temporal_patch_size`) --
  The temporal patch size of the vision encoder.
- **merge_size** (`int`, *optional*, defaults to `self.merge_size`) --
  The merge size of the vision encoder to llm encoder.
- **do_convert_rgb** (`bool`, *optional*, defaults to `self.do_convert_rgb`) --
  Whether to convert the image to RGB.
- **return_tensors** (`str` or `TensorType`, *optional*) --
  The type of tensors to return. Can be one of:
  - Unset: Return a list of `np.ndarray`.
  - `TensorType.PYTORCH` or `'pt'`: Return a batch of type `torch.Tensor`.
  - `TensorType.NUMPY` or `'np'`: Return a batch of type `np.ndarray`.
- **data_format** (`ChannelDimension` or `str`, *optional*, defaults to `ChannelDimension.FIRST`) --
  The channel dimension format for the output image. Can be one of:
  - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
  - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.
  - Unset: Use the channel dimension format of the input image.
- **input_data_format** (`ChannelDimension` or `str`, *optional*) --
  The channel dimension format for the input image. If unset, the channel dimension format is inferred
  from the input image. Can be one of:
  - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
  - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.
  - `"none"` or `ChannelDimension.NONE`: image in (height, width) format.0

**Parameters:**

do_resize (`bool`, *optional*, defaults to `True`) : Whether to resize the image's (height, width) dimensions.

size (`dict[str, int]`, *optional*, defaults to `{"shortest_edge" : 56 * 56, "longest_edge": 28 * 28 * 6177}`): Size of the image after resizing. `shortest_edge` and `longest_edge` keys must be present.

resample (`PILImageResampling`, *optional*, defaults to `Resampling.BICUBIC`) : Resampling filter to use when resizing the image.

do_rescale (`bool`, *optional*, defaults to `True`) : Whether to rescale the image by the specified scale `rescale_factor`.

rescale_factor (`int` or `float`, *optional*, defaults to `1/255`) : Scale factor to use if rescaling the image.

do_normalize (`bool`, *optional*, defaults to `True`) : Whether to normalize the image.

image_mean (`float` or `list[float]`, *optional*, defaults to `[0.48145466, 0.4578275, 0.40821073]`) : Mean to use if normalizing the image. This is a float or list of floats for each channel in the image.

image_std (`float` or `list[float]`, *optional*, defaults to `[0.26862954, 0.26130258, 0.27577711]`) : Standard deviation to use if normalizing the image. This is a float or list of floats for each channel in the image.

do_convert_rgb (`bool`, *optional*, defaults to `True`) : Whether to convert the image to RGB.

patch_size (`int`, *optional*, defaults to 14) : The spatial patch size of the vision encoder.

temporal_patch_size (`int`, *optional*) : The temporal patch size of the vision encoder. Unused in the image processor, only used for videos.

merge_size (`int`, *optional*, defaults to 2) : The merge size of the vision encoder to llm encoder.

## Ernie4_5_VL_MoeImageProcessorFast[[transformers.Ernie4_5_VL_MoeImageProcessorFast]]

#### transformers.Ernie4_5_VL_MoeImageProcessorFast[[transformers.Ernie4_5_VL_MoeImageProcessorFast]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/ernie4_5_vl_moe/image_processing_ernie4_5_vl_moe_fast.py#L64)

Constructs a fast Ernie4 5 Vl Moe image processor.

preprocesstransformers.Ernie4_5_VL_MoeImageProcessorFast.preprocesshttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/ernie4_5_vl_moe/image_processing_ernie4_5_vl_moe_fast.py#L193[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor']]"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.models.ernie4_5_vl_moe.image_processing_ernie4_5_vl_moe.Ernie4_5_VL_MoeImageProcessorKwargs]"}]- **images** (`Union[PIL.Image.Image, numpy.ndarray, torch.Tensor, list, list, list]`) --
  Image to preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If
  passing in images with pixel values between 0 and 1, set `do_rescale=False`.
- **do_convert_rgb** (`bool | None.do_convert_rgb`) --
  Whether to convert the image to RGB.
- **do_resize** (`bool | None.do_resize`) --
  Whether to resize the image.
- **size** (`Annotated[int | list[int] | tuple[int, ...] | dict[str, int] | None, None]`) --
  Describes the maximum input dimensions to the model.
- **crop_size** (`Annotated[int | list[int] | tuple[int, ...] | dict[str, int] | None, None]`) --
  Size of the output image after applying `center_crop`.
- **resample** (`Annotated[Union[PILImageResampling, int, NoneType], None]`) --
  Resampling filter to use if resizing the image. This can be one of the enum `PILImageResampling`. Only
  has an effect if `do_resize` is set to `True`.
- **do_rescale** (`bool | None.do_rescale`) --
  Whether to rescale the image.
- **rescale_factor** (`float | None.rescale_factor`) --
  Rescale factor to rescale the image by if `do_rescale` is set to `True`.
- **do_normalize** (`bool | None.do_normalize`) --
  Whether to normalize the image.
- **image_mean** (`float | list[float] | tuple[float, ...] | None.image_mean`) --
  Image mean to use for normalization. Only has an effect if `do_normalize` is set to `True`.
- **image_std** (`float | list[float] | tuple[float, ...] | None.image_std`) --
  Image standard deviation to use for normalization. Only has an effect if `do_normalize` is set to
  `True`.
- **do_pad** (`bool | None.do_pad`) --
  Whether to pad the image. Padding is done either to the largest size in the batch
  or to a fixed square size per image. The exact padding strategy depends on the model.
- **pad_size** (`Annotated[int | list[int] | tuple[int, ...] | dict[str, int] | None, None]`) --
  The size in `{"height": int, "width" int}` to pad the images to. Must be larger than any image size
  provided for preprocessing. If `pad_size` is not provided, images will be padded to the largest
  height and width in the batch. Applied only when `do_pad=True.`
- **do_center_crop** (`bool | None.do_center_crop`) --
  Whether to center crop the image.
- **data_format** (`str | ~image_utils.ChannelDimension | None.data_format`) --
  Only `ChannelDimension.FIRST` is supported. Added for compatibility with slow processors.
- **input_data_format** (`str | ~image_utils.ChannelDimension | None.input_data_format`) --
  The channel dimension format for the input image. If unset, the channel dimension format is inferred
  from the input image. Can be one of:
  - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
  - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.
  - `"none"` or `ChannelDimension.NONE`: image in (height, width) format.
- **device** (`Annotated[Union[str, torch.device, NoneType], None]`) --
  The device to process the images on. If unset, the device is inferred from the input images.
- **return_tensors** (`Annotated[str | ~utils.generic.TensorType | None, None]`) --
  Returns stacked tensors if set to `pt, otherwise returns a list of tensors.
- **disable_grouping** (`bool | None.disable_grouping`) --
  Whether to disable grouping of images by size to process them individually and not in batches.
  If None, will be set to True if the images are on CPU, and False otherwise. This choice is based on
  empirical observations, as detailed here: https://github.com/huggingface/transformers/pull/38157
- **image_seq_length** (`int | None.image_seq_length`) --
  The number of image tokens to be used for each image in the input.
  Added for backward compatibility but this should be set as a processor attribute in future models.
- **patch_size** (`int`, *optional*, defaults to 14) --
  The spatial patch size of the vision encoder.
- **temporal_patch_size** (`int`, *optional*) --
  The temporal patch size of the vision encoder. Unused in the image processor, only used for videos.
- **merge_size** (`int`, *optional*, defaults to 2) --
  The merge size of the vision encoder to llm encoder.0``- **data** (`dict`) -- Dictionary of lists/arrays/tensors returned by the __call__ method ('pixel_values', etc.).
- **tensor_type** (`Union[None, str, TensorType]`, *optional*) -- You can give a tensor_type here to convert the lists of integers in PyTorch/Numpy Tensors at
  initialization.

**Parameters:**

images (`Union[PIL.Image.Image, numpy.ndarray, torch.Tensor, list, list, list]`) : Image to preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If passing in images with pixel values between 0 and 1, set `do_rescale=False`.

do_convert_rgb (`bool | None.do_convert_rgb`) : Whether to convert the image to RGB.

do_resize (`bool | None.do_resize`) : Whether to resize the image.

size (`Annotated[int | list[int] | tuple[int, ...] | dict[str, int] | None, None]`) : Describes the maximum input dimensions to the model.

crop_size (`Annotated[int | list[int] | tuple[int, ...] | dict[str, int] | None, None]`) : Size of the output image after applying `center_crop`.

resample (`Annotated[Union[PILImageResampling, int, NoneType], None]`) : Resampling filter to use if resizing the image. This can be one of the enum `PILImageResampling`. Only has an effect if `do_resize` is set to `True`.

do_rescale (`bool | None.do_rescale`) : Whether to rescale the image.

rescale_factor (`float | None.rescale_factor`) : Rescale factor to rescale the image by if `do_rescale` is set to `True`.

do_normalize (`bool | None.do_normalize`) : Whether to normalize the image.

image_mean (`float | list[float] | tuple[float, ...] | None.image_mean`) : Image mean to use for normalization. Only has an effect if `do_normalize` is set to `True`.

image_std (`float | list[float] | tuple[float, ...] | None.image_std`) : Image standard deviation to use for normalization. Only has an effect if `do_normalize` is set to `True`.

do_pad (`bool | None.do_pad`) : Whether to pad the image. Padding is done either to the largest size in the batch or to a fixed square size per image. The exact padding strategy depends on the model.

pad_size (`Annotated[int | list[int] | tuple[int, ...] | dict[str, int] | None, None]`) : The size in `{"height": int, "width" int}` to pad the images to. Must be larger than any image size provided for preprocessing. If `pad_size` is not provided, images will be padded to the largest height and width in the batch. Applied only when `do_pad=True.`

do_center_crop (`bool | None.do_center_crop`) : Whether to center crop the image.

data_format (`str | ~image_utils.ChannelDimension | None.data_format`) : Only `ChannelDimension.FIRST` is supported. Added for compatibility with slow processors.

input_data_format (`str | ~image_utils.ChannelDimension | None.input_data_format`) : The channel dimension format for the input image. If unset, the channel dimension format is inferred from the input image. Can be one of: - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format. - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format. - `"none"` or `ChannelDimension.NONE`: image in (height, width) format.

device (`Annotated[Union[str, torch.device, NoneType], None]`) : The device to process the images on. If unset, the device is inferred from the input images.

return_tensors (`Annotated[str | ~utils.generic.TensorType | None, None]`) : Returns stacked tensors if set to `pt, otherwise returns a list of tensors.

disable_grouping (`bool | None.disable_grouping`) : Whether to disable grouping of images by size to process them individually and not in batches. If None, will be set to True if the images are on CPU, and False otherwise. This choice is based on empirical observations, as detailed here: https://github.com/huggingface/transformers/pull/38157

image_seq_length (`int | None.image_seq_length`) : The number of image tokens to be used for each image in the input. Added for backward compatibility but this should be set as a processor attribute in future models.

patch_size (`int`, *optional*, defaults to 14) : The spatial patch size of the vision encoder.

temporal_patch_size (`int`, *optional*) : The temporal patch size of the vision encoder. Unused in the image processor, only used for videos.

merge_size (`int`, *optional*, defaults to 2) : The merge size of the vision encoder to llm encoder.

**Returns:**

````

- **data** (`dict`) -- Dictionary of lists/arrays/tensors returned by the __call__ method ('pixel_values', etc.).
- **tensor_type** (`Union[None, str, TensorType]`, *optional*) -- You can give a tensor_type here to convert the lists of integers in PyTorch/Numpy Tensors at
  initialization.

## Ernie4_5_VL_MoeVideoProcessor[[transformers.Ernie4_5_VL_MoeVideoProcessor]]

#### transformers.Ernie4_5_VL_MoeVideoProcessor[[transformers.Ernie4_5_VL_MoeVideoProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/ernie4_5_vl_moe/video_processing_ernie4_5_vl_moe.py#L98)

Constructs a fast Ernie 4.5 VL image processor that dynamically resizes videos based on the original videos.

preprocesstransformers.Ernie4_5_VL_MoeVideoProcessor.preprocesshttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/ernie4_5_vl_moe/video_processing_ernie4_5_vl_moe.py#L538[{"name": "videos", "val": ": typing.Union[list['PIL.Image.Image'], numpy.ndarray, ForwardRef('torch.Tensor'), list[numpy.ndarray], list['torch.Tensor'], list[list['PIL.Image.Image']], list[list[numpy.ndarray]], list[list['torch.Tensor']], transformers.video_utils.URL, list[transformers.video_utils.URL], list[list[transformers.video_utils.URL]], transformers.video_utils.Path, list[transformers.video_utils.Path], list[list[transformers.video_utils.Path]]]"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.processing_utils.VideosKwargs]"}]- **do_resize** (`bool`, *optional*, defaults to `self.do_resize`) --
  Whether to resize the video's (height, width) dimensions to the specified `size`. Can be overridden by the
  `do_resize` parameter in the `preprocess` method.
- **size** (`dict`, *optional*, defaults to `self.size`) --
  Size of the output video after resizing. Can be overridden by the `size` parameter in the `preprocess`
  method.
- **size_divisor** (`int`, *optional*, defaults to `self.size_divisor`) --
  The size by which to make sure both the height and width can be divided.
- **default_to_square** (`bool`, *optional*, defaults to `self.default_to_square`) --
  Whether to default to a square video when resizing, if size is an int.
- **resample** (`PILImageResampling`, *optional*, defaults to `self.resample`) --
  Resampling filter to use if resizing the video. Only has an effect if `do_resize` is set to `True`. Can be
  overridden by the `resample` parameter in the `preprocess` method.
- **do_center_crop** (`bool`, *optional*, defaults to `self.do_center_crop`) --
  Whether to center crop the video to the specified `crop_size`. Can be overridden by `do_center_crop` in the
  `preprocess` method.
- **crop_size** (`dict[str, int]` *optional*, defaults to `self.crop_size`) --
  Size of the output video after applying `center_crop`. Can be overridden by `crop_size` in the `preprocess`
  method.
- **do_rescale** (`bool`, *optional*, defaults to `self.do_rescale`) --
  Whether to rescale the video by the specified scale `rescale_factor`. Can be overridden by the
  `do_rescale` parameter in the `preprocess` method.
- **rescale_factor** (`int` or `float`, *optional*, defaults to `self.rescale_factor`) --
  Scale factor to use if rescaling the video. Only has an effect if `do_rescale` is set to `True`. Can be
  overridden by the `rescale_factor` parameter in the `preprocess` method.
- **do_normalize** (`bool`, *optional*, defaults to `self.do_normalize`) --
  Whether to normalize the video. Can be overridden by the `do_normalize` parameter in the `preprocess`
  method. Can be overridden by the `do_normalize` parameter in the `preprocess` method.
- **image_mean** (`float` or `list[float]`, *optional*, defaults to `self.image_mean`) --
  Mean to use if normalizing the video. This is a float or list of floats the length of the number of
  channels in the video. Can be overridden by the `image_mean` parameter in the `preprocess` method. Can be
  overridden by the `image_mean` parameter in the `preprocess` method.
- **image_std** (`float` or `list[float]`, *optional*, defaults to `self.image_std`) --
  Standard deviation to use if normalizing the video. This is a float or list of floats the length of the
  number of channels in the video. Can be overridden by the `image_std` parameter in the `preprocess` method.
  Can be overridden by the `image_std` parameter in the `preprocess` method.
- **do_convert_rgb** (`bool`, *optional*, defaults to `self.image_std`) --
  Whether to convert the video to RGB.
- **video_metadata** (`VideoMetadata`, *optional*) --
  Metadata of the video containing information about total duration, fps and total number of frames.
- **do_sample_frames** (`int`, *optional*, defaults to `self.do_sample_frames`) --
  Whether to sample frames from the video before processing or to process the whole video.
- **num_frames** (`int`, *optional*, defaults to `self.num_frames`) --
  Maximum number of frames to sample when `do_sample_frames=True`.
- **fps** (`int` or `float`, *optional*, defaults to `self.fps`) --
  Target frames to sample per second when `do_sample_frames=True`.
- **return_tensors** (`str` or `TensorType`, *optional*) --
  Returns stacked tensors if set to `pt, otherwise returns a list of tensors.
- **data_format** (`ChannelDimension` or `str`, *optional*, defaults to `ChannelDimension.FIRST`) --
  The channel dimension format for the output video. Can be one of:
  - `"channels_first"` or `ChannelDimension.FIRST`: video in (num_channels, height, width) format.
  - `"channels_last"` or `ChannelDimension.LAST`: video in (height, width, num_channels) format.
  - Unset: Use the channel dimension format of the input video.
- **input_data_format** (`ChannelDimension` or `str`, *optional*) --
  The channel dimension format for the input video. If unset, the channel dimension format is inferred
  from the input video. Can be one of:
  - `"channels_first"` or `ChannelDimension.FIRST`: video in (num_channels, height, width) format.
  - `"channels_last"` or `ChannelDimension.LAST`: video in (height, width, num_channels) format.
  - `"none"` or `ChannelDimension.NONE`: video in (height, width) format.
- **device** (`torch.device`, *optional*) --
  The device to process the videos on. If unset, the device is inferred from the input videos.
- **return_metadata** (`bool`, *optional*) --
  Whether to return video metadata or not.0

**Parameters:**

do_resize (`bool`, *optional*, defaults to `self.do_resize`) : Whether to resize the video's (height, width) dimensions to the specified `size`. Can be overridden by the `do_resize` parameter in the `preprocess` method.

size (`dict`, *optional*, defaults to `self.size`) : Size of the output video after resizing. Can be overridden by the `size` parameter in the `preprocess` method.

size_divisor (`int`, *optional*, defaults to `self.size_divisor`) : The size by which to make sure both the height and width can be divided.

default_to_square (`bool`, *optional*, defaults to `self.default_to_square`) : Whether to default to a square video when resizing, if size is an int.

resample (`PILImageResampling`, *optional*, defaults to `self.resample`) : Resampling filter to use if resizing the video. Only has an effect if `do_resize` is set to `True`. Can be overridden by the `resample` parameter in the `preprocess` method.

do_center_crop (`bool`, *optional*, defaults to `self.do_center_crop`) : Whether to center crop the video to the specified `crop_size`. Can be overridden by `do_center_crop` in the `preprocess` method.

crop_size (`dict[str, int]` *optional*, defaults to `self.crop_size`) : Size of the output video after applying `center_crop`. Can be overridden by `crop_size` in the `preprocess` method.

do_rescale (`bool`, *optional*, defaults to `self.do_rescale`) : Whether to rescale the video by the specified scale `rescale_factor`. Can be overridden by the `do_rescale` parameter in the `preprocess` method.

rescale_factor (`int` or `float`, *optional*, defaults to `self.rescale_factor`) : Scale factor to use if rescaling the video. Only has an effect if `do_rescale` is set to `True`. Can be overridden by the `rescale_factor` parameter in the `preprocess` method.

do_normalize (`bool`, *optional*, defaults to `self.do_normalize`) : Whether to normalize the video. Can be overridden by the `do_normalize` parameter in the `preprocess` method. Can be overridden by the `do_normalize` parameter in the `preprocess` method.

image_mean (`float` or `list[float]`, *optional*, defaults to `self.image_mean`) : Mean to use if normalizing the video. This is a float or list of floats the length of the number of channels in the video. Can be overridden by the `image_mean` parameter in the `preprocess` method. Can be overridden by the `image_mean` parameter in the `preprocess` method.

image_std (`float` or `list[float]`, *optional*, defaults to `self.image_std`) : Standard deviation to use if normalizing the video. This is a float or list of floats the length of the number of channels in the video. Can be overridden by the `image_std` parameter in the `preprocess` method. Can be overridden by the `image_std` parameter in the `preprocess` method.

do_convert_rgb (`bool`, *optional*, defaults to `self.image_std`) : Whether to convert the video to RGB.

video_metadata (`VideoMetadata`, *optional*) : Metadata of the video containing information about total duration, fps and total number of frames.

do_sample_frames (`int`, *optional*, defaults to `self.do_sample_frames`) : Whether to sample frames from the video before processing or to process the whole video.

num_frames (`int`, *optional*, defaults to `self.num_frames`) : Maximum number of frames to sample when `do_sample_frames=True`.

fps (`int` or `float`, *optional*, defaults to `self.fps`) : Target frames to sample per second when `do_sample_frames=True`.

return_tensors (`str` or `TensorType`, *optional*) : Returns stacked tensors if set to `pt, otherwise returns a list of tensors.

data_format (`ChannelDimension` or `str`, *optional*, defaults to `ChannelDimension.FIRST`) : The channel dimension format for the output video. Can be one of: - `"channels_first"` or `ChannelDimension.FIRST`: video in (num_channels, height, width) format. - `"channels_last"` or `ChannelDimension.LAST`: video in (height, width, num_channels) format. - Unset: Use the channel dimension format of the input video.

input_data_format (`ChannelDimension` or `str`, *optional*) : The channel dimension format for the input video. If unset, the channel dimension format is inferred from the input video. Can be one of: - `"channels_first"` or `ChannelDimension.FIRST`: video in (num_channels, height, width) format. - `"channels_last"` or `ChannelDimension.LAST`: video in (height, width, num_channels) format. - `"none"` or `ChannelDimension.NONE`: video in (height, width) format.

device (`torch.device`, *optional*) : The device to process the videos on. If unset, the device is inferred from the input videos.

return_metadata (`bool`, *optional*) : Whether to return video metadata or not. 

patch_size (`int`, *optional*, defaults to 14) : The spacial patch size of the vision encoder.

temporal_patch_size (`int`, *optional*, defaults to 2) : The temporal patch size of the vision encoder.

merge_size (`int`, *optional*, defaults to 2) : The merge size of the vision encoder to llm encoder.

min_frames (`int`, *optional*, defaults to 16) : The minimum number of frames that can be sampled.

max_frames (`int`, *optional*, defaults to 180) : The maximum number of frames that can be sampled.

draw_on_frames (`bool`, *optional*, defaults to `True`) : Whether to draw timestamps on each frame or not. This does not work with `torch.compile` but resembles the performance of the original model.

font (`str`, *optional*, defaults to "Roboto-Regular.ttf") : The associated font name for drawing on frames. Defaults to "Roboto-Regular.ttf" and is expected to be saved along the processor as separate file.

## Ernie4_5_VL_MoeProcessor[[transformers.Ernie4_5_VL_MoeProcessor]]

#### transformers.Ernie4_5_VL_MoeProcessor[[transformers.Ernie4_5_VL_MoeProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/ernie4_5_vl_moe/processing_ernie4_5_vl_moe.py#L37)

Constructs a Ernie 4.5 VL processor which wraps a Ernie 4.5 VL image processor and a Llama tokenizer into a single processor.
[Ernie4_5_VL_MoeProcessor](/docs/transformers/v5.0.0/en/model_doc/ernie4_5_vl_moe#transformers.Ernie4_5_VL_MoeProcessor) offers all the functionalities of [Ernie4_5_VL_MoeImageProcessor](/docs/transformers/v5.0.0/en/model_doc/ernie4_5_vl_moe#transformers.Ernie4_5_VL_MoeImageProcessor) and [LlamaTokenizerFast](/docs/transformers/v5.0.0/en/model_doc/llama2#transformers.LlamaTokenizer). See the
[__call__()](/docs/transformers/v5.0.0/en/model_doc/ernie4_5_vl_moe#transformers.Ernie4_5_VL_MoeProcessor.__call__) and [decode()](/docs/transformers/v5.0.0/en/main_classes/processors#transformers.ProcessorMixin.decode) for more information.

__call__transformers.Ernie4_5_VL_MoeProcessor.__call__https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/ernie4_5_vl_moe/processing_ernie4_5_vl_moe.py#L82[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor'], NoneType] = None"}, {"name": "text", "val": ": str | list[str] | list[list[str]] = None"}, {"name": "videos", "val": ": typing.Union[list['PIL.Image.Image'], numpy.ndarray, ForwardRef('torch.Tensor'), list[numpy.ndarray], list['torch.Tensor'], list[list['PIL.Image.Image']], list[list[numpy.ndarray]], list[list['torch.Tensor']], transformers.video_utils.URL, list[transformers.video_utils.URL], list[list[transformers.video_utils.URL]], transformers.video_utils.Path, list[transformers.video_utils.Path], list[list[transformers.video_utils.Path]], NoneType] = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.models.ernie4_5_vl_moe.processing_ernie4_5_vl_moe.Ernie4_5_VL_MoeProcessorKwargs]"}]- **images** (`PIL.Image.Image`, `np.ndarray`, `torch.Tensor`, `list[PIL.Image.Image]`, `list[np.ndarray]`, `list[torch.Tensor]`) --
  The image or batch of images to be prepared. Each image can be a PIL image, NumPy array or PyTorch
  tensor. Both channels-first and channels-last formats are supported.
- **text** (`str`, `list[str]`, `list[list[str]]`) --
  The sequence or batch of sequences to be encoded. Each sequence can be a string or a list of strings
  (pretokenized string). If the sequences are provided as list of strings (pretokenized), you must set
  `is_split_into_words=True` (to lift the ambiguity with a batch of sequences).
- **videos** (`np.ndarray`, `torch.Tensor`, `list[np.ndarray]`, `list[torch.Tensor]`) --
  The image or batch of videos to be prepared. Each video can be a 4D NumPy array or PyTorch
  tensor, or a nested list of 3D frames. Both channels-first and channels-last formats are supported.
- **return_tensors** (`str` or [TensorType](/docs/transformers/v5.0.0/en/internal/file_utils#transformers.TensorType), *optional*) --
  If set, will return tensors of a particular framework. Acceptable values are:
  - `'pt'`: Return PyTorch `torch.Tensor` objects.
  - `'np'`: Return NumPy `np.ndarray` objects.0[BatchFeature](/docs/transformers/v5.0.0/en/main_classes/image_processor#transformers.BatchFeature)A [BatchFeature](/docs/transformers/v5.0.0/en/main_classes/image_processor#transformers.BatchFeature) with the following fields:

- **input_ids** -- List of token ids to be fed to a model. Returned when `text` is not `None`.
- **attention_mask** -- List of indices specifying which tokens should be attended to by the model (when
  `return_attention_mask=True` or if *"attention_mask"* is in `self.model_input_names` and if `text` is not
  `None`).
- **pixel_values** -- Pixel values to be fed to a model. Returned when `images` is not `None`.
- **pixel_values_videos** -- Pixel values of videos to be fed to a model. Returned when `videos` is not `None`.
- **image_grid_thw** -- List of image 3D grid in LLM. Returned when `images` is not `None`.
- **video_grid_thw** -- List of video 3D grid in LLM. Returned when `videos` is not `None`.
- **mm_token_type_ids** -- List of token type ids differentiating between image, video and text input.
  Returned when `text` is not `None`.

Main method to prepare for the model one or several sequences(s) and image(s). This method forwards the `text`
and `kwargs` arguments to Qwen2TokenizerFast's [__call__()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) if `text` is not `None` to encode
the text. To prepare the vision inputs, this method forwards the `vision_infos` and `kwargs` arguments to
Ernie4_5_VL_MoeImageProcessor's [__call__()](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) if `vision_infos` is not `None`.

**Parameters:**

image_processor ([Ernie4_5_VL_MoeImageProcessor](/docs/transformers/v5.0.0/en/model_doc/ernie4_5_vl_moe#transformers.Ernie4_5_VL_MoeImageProcessor), *optional*) : The image processor is a required input.

tokenizer ([LlamaTokenizerFast](/docs/transformers/v5.0.0/en/model_doc/llama2#transformers.LlamaTokenizer), *optional*) : The tokenizer is a required input.

video_processor ([Ernie4_5_VL_MoeVideoProcessor](/docs/transformers/v5.0.0/en/model_doc/ernie4_5_vl_moe#transformers.Ernie4_5_VL_MoeVideoProcessor), *optional*) : The video processor is a required input.

chat_template (`str`, *optional*) : A Jinja template which will be used to convert lists of messages in a chat into a tokenizable string.

**Returns:**

`[BatchFeature](/docs/transformers/v5.0.0/en/main_classes/image_processor#transformers.BatchFeature)`

A [BatchFeature](/docs/transformers/v5.0.0/en/main_classes/image_processor#transformers.BatchFeature) with the following fields:

- **input_ids** -- List of token ids to be fed to a model. Returned when `text` is not `None`.
- **attention_mask** -- List of indices specifying which tokens should be attended to by the model (when
  `return_attention_mask=True` or if *"attention_mask"* is in `self.model_input_names` and if `text` is not
  `None`).
- **pixel_values** -- Pixel values to be fed to a model. Returned when `images` is not `None`.
- **pixel_values_videos** -- Pixel values of videos to be fed to a model. Returned when `videos` is not `None`.
- **image_grid_thw** -- List of image 3D grid in LLM. Returned when `images` is not `None`.
- **video_grid_thw** -- List of video 3D grid in LLM. Returned when `videos` is not `None`.
- **mm_token_type_ids** -- List of token type ids differentiating between image, video and text input.
  Returned when `text` is not `None`.

## Ernie4_5_VL_MoeTextModel[[transformers.Ernie4_5_VL_MoeTextModel]]

#### transformers.Ernie4_5_VL_MoeTextModel[[transformers.Ernie4_5_VL_MoeTextModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/ernie4_5_vl_moe/modeling_ernie4_5_vl_moe.py#L725)

The bare Ernie4 5 Vl Moe Text Model outputting raw hidden-states without any specific head on to.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.Ernie4_5_VL_MoeTextModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/ernie4_5_vl_moe/modeling_ernie4_5_vl_moe.py#L744[{"name": "input_ids", "val": ": torch.LongTensor | None = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.LongTensor | None = None"}, {"name": "moe_mm_token_type_ids", "val": ": torch.IntTensor | None = None"}, {"name": "past_key_values", "val": ": transformers.cache_utils.Cache | None = None"}, {"name": "inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "cache_position", "val": ": torch.LongTensor | None = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.modeling_flash_attention_utils.FlashAttentionKwargs]"}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
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
- **moe_mm_token_type_ids** (`torch.IntTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  The same as `mm_token_type_ids` while additionally considering start/end image/video tokens as respective vision tokens.
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
- **use_cache** (`bool`, *optional*) --
  If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
  `past_key_values`).
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.0`transformers.modeling_outputs.MoeModelOutputWithPast` or `tuple(torch.FloatTensor)`A `transformers.modeling_outputs.MoeModelOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Ernie4_5_VL_MoeConfig](/docs/transformers/v5.0.0/en/model_doc/ernie4_5_vl_moe#transformers.Ernie4_5_VL_MoeConfig)) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.
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
- **router_logits** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_router_probs=True` and `config.add_router_probs=True` is passed or when `config.output_router_probs=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, sequence_length, num_experts)`.

  Raw router logtis (post-softmax) that are computed by MoE routers, these terms are used to compute the auxiliary
  loss for Mixture of Experts models.
The [Ernie4_5_VL_MoeTextModel](/docs/transformers/v5.0.0/en/model_doc/ernie4_5_vl_moe#transformers.Ernie4_5_VL_MoeTextModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

**Parameters:**

config ([Ernie4_5_VL_MoeTextConfig](/docs/transformers/v5.0.0/en/model_doc/ernie4_5_vl_moe#transformers.Ernie4_5_VL_MoeTextConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``transformers.modeling_outputs.MoeModelOutputWithPast` or `tuple(torch.FloatTensor)``

A `transformers.modeling_outputs.MoeModelOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Ernie4_5_VL_MoeConfig](/docs/transformers/v5.0.0/en/model_doc/ernie4_5_vl_moe#transformers.Ernie4_5_VL_MoeConfig)) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.
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
- **router_logits** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_router_probs=True` and `config.add_router_probs=True` is passed or when `config.output_router_probs=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, sequence_length, num_experts)`.

  Raw router logtis (post-softmax) that are computed by MoE routers, these terms are used to compute the auxiliary
  loss for Mixture of Experts models.

## Ernie4_5_VL_MoeVisionTransformerPretrainedModel[[transformers.Ernie4_5_VL_MoeVisionTransformerPretrainedModel]]

#### transformers.Ernie4_5_VL_MoeVisionTransformerPretrainedModel[[transformers.Ernie4_5_VL_MoeVisionTransformerPretrainedModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/ernie4_5_vl_moe/modeling_ernie4_5_vl_moe.py#L876)

The bare Ernie4 5 Vl Moe Model outputting raw hidden-states without any specific head on top.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.Ernie4_5_VL_MoeVisionTransformerPretrainedModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/ernie4_5_vl_moe/modeling_ernie4_5_vl_moe.py#L936[{"name": "hidden_states", "val": ": Tensor"}, {"name": "grid_thw", "val": ": Tensor"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]

grid_thw (`torch.LongTensor` of shape `(num_images, 3)`):
The temporal, height and width dimensions of feature shape for each image. Each row contains [t, h, w] values.

**Parameters:**

config ([Ernie4_5_VL_MoeVisionTransformerPretrainedModel](/docs/transformers/v5.0.0/en/model_doc/ernie4_5_vl_moe#transformers.Ernie4_5_VL_MoeVisionTransformerPretrainedModel)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

## Ernie4_5_VL_MoeVariableResolutionResamplerModel[[transformers.Ernie4_5_VL_MoeVariableResolutionResamplerModel]]

#### transformers.Ernie4_5_VL_MoeVariableResolutionResamplerModel[[transformers.Ernie4_5_VL_MoeVariableResolutionResamplerModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/ernie4_5_vl_moe/modeling_ernie4_5_vl_moe.py#L987)

forwardtransformers.Ernie4_5_VL_MoeVariableResolutionResamplerModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/ernie4_5_vl_moe/modeling_ernie4_5_vl_moe.py#L1071[{"name": "hidden_states", "val": ""}, {"name": "grid_thw", "val": ""}]

## Ernie4_5_VL_MoeModel[[transformers.Ernie4_5_VL_MoeModel]]

#### transformers.Ernie4_5_VL_MoeModel[[transformers.Ernie4_5_VL_MoeModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/ernie4_5_vl_moe/modeling_ernie4_5_vl_moe.py#L1089)

The bare Ernie4 5 Vl Moe Model outputting raw hidden-states without any specific head on top.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.Ernie4_5_VL_MoeModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/ernie4_5_vl_moe/modeling_ernie4_5_vl_moe.py#L1356[{"name": "input_ids", "val": ": LongTensor = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.LongTensor | None = None"}, {"name": "mm_token_type_ids", "val": ": torch.IntTensor | None = None"}, {"name": "moe_mm_token_type_ids", "val": ": torch.IntTensor | None = None"}, {"name": "past_key_values", "val": ": transformers.cache_utils.Cache | None = None"}, {"name": "inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "pixel_values", "val": ": torch.Tensor | None = None"}, {"name": "pixel_values_videos", "val": ": torch.FloatTensor | None = None"}, {"name": "image_grid_thw", "val": ": torch.LongTensor | None = None"}, {"name": "video_grid_thw", "val": ": torch.LongTensor | None = None"}, {"name": "rope_deltas", "val": ": torch.LongTensor | None = None"}, {"name": "cache_position", "val": ": torch.LongTensor | None = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
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
- **mm_token_type_ids** (`torch.IntTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Token type ids matching each modality to a different value in the input sequence, i.e. text (0), image (1), video (2).
- **moe_mm_token_type_ids** (`torch.IntTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  The same as `mm_token_type_ids` while additionally considering start/end image/video tokens as respective vision tokens.
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
- **use_cache** (`bool`, *optional*) --
  If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
  `past_key_values`).
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
- **rope_deltas** (`torch.LongTensor` of shape `(batch_size, )`, *optional*) --
  The rope index difference between sequence length and multimodal rope.
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.0`transformers.modeling_outputs.MoeModelOutputWithPast` or `tuple(torch.FloatTensor)`A `transformers.modeling_outputs.MoeModelOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration (`None`) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.
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
- **router_logits** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_router_probs=True` and `config.add_router_probs=True` is passed or when `config.output_router_probs=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, sequence_length, num_experts)`.

  Raw router logtis (post-softmax) that are computed by MoE routers, these terms are used to compute the auxiliary
  loss for Mixture of Experts models.
The [Ernie4_5_VL_MoeModel](/docs/transformers/v5.0.0/en/model_doc/ernie4_5_vl_moe#transformers.Ernie4_5_VL_MoeModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

**Parameters:**

config ([Ernie4_5_VL_MoeConfig](/docs/transformers/v5.0.0/en/model_doc/ernie4_5_vl_moe#transformers.Ernie4_5_VL_MoeConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``transformers.modeling_outputs.MoeModelOutputWithPast` or `tuple(torch.FloatTensor)``

A `transformers.modeling_outputs.MoeModelOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration (`None`) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.
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
- **router_logits** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_router_probs=True` and `config.add_router_probs=True` is passed or when `config.output_router_probs=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, sequence_length, num_experts)`.

  Raw router logtis (post-softmax) that are computed by MoE routers, these terms are used to compute the auxiliary
  loss for Mixture of Experts models.
#### get_video_features[[transformers.Ernie4_5_VL_MoeModel.get_video_features]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/ernie4_5_vl_moe/modeling_ernie4_5_vl_moe.py#L1269)

**Parameters:**

pixel_values_videos (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`) : The tensors corresponding to the input videos.

video_grid_thw (`torch.LongTensor` of shape `(num_videos, 3)`, *optional*) : The temporal, height and width of feature shape of each video in LLM.

**Returns:**

`[transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Ernie4_5_VL_MoeConfig](/docs/transformers/v5.0.0/en/model_doc/ernie4_5_vl_moe#transformers.Ernie4_5_VL_MoeConfig)) and inputs.

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
#### get_image_features[[transformers.Ernie4_5_VL_MoeModel.get_image_features]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/ernie4_5_vl_moe/modeling_ernie4_5_vl_moe.py#L1294)

**Parameters:**

pixel_values (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`) : The tensors corresponding to the input images.

image_grid_thw (`torch.LongTensor` of shape `(num_images, 3)`, *optional*) : The temporal, height and width of feature shape of each image in LLM.

**Returns:**

`[transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Ernie4_5_VL_MoeConfig](/docs/transformers/v5.0.0/en/model_doc/ernie4_5_vl_moe#transformers.Ernie4_5_VL_MoeConfig)) and inputs.

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

## Ernie4_5_VL_MoeForConditionalGeneration[[transformers.Ernie4_5_VL_MoeForConditionalGeneration]]

#### transformers.Ernie4_5_VL_MoeForConditionalGeneration[[transformers.Ernie4_5_VL_MoeForConditionalGeneration]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/ernie4_5_vl_moe/modeling_ernie4_5_vl_moe.py#L1589)

forwardtransformers.Ernie4_5_VL_MoeForConditionalGeneration.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/ernie4_5_vl_moe/modeling_ernie4_5_vl_moe.py#L1644[{"name": "input_ids", "val": ": LongTensor = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.LongTensor | None = None"}, {"name": "mm_token_type_ids", "val": ": torch.IntTensor | None = None"}, {"name": "moe_mm_token_type_ids", "val": ": torch.IntTensor | None = None"}, {"name": "past_key_values", "val": ": transformers.cache_utils.Cache | None = None"}, {"name": "inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "labels", "val": ": torch.LongTensor | None = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "output_router_logits", "val": ": bool | None = None"}, {"name": "pixel_values", "val": ": torch.Tensor | None = None"}, {"name": "pixel_values_videos", "val": ": torch.FloatTensor | None = None"}, {"name": "image_grid_thw", "val": ": torch.LongTensor | None = None"}, {"name": "video_grid_thw", "val": ": torch.LongTensor | None = None"}, {"name": "rope_deltas", "val": ": torch.LongTensor | None = None"}, {"name": "cache_position", "val": ": torch.LongTensor | None = None"}, {"name": "logits_to_keep", "val": ": int | torch.Tensor = 0"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
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
- **mm_token_type_ids** (`torch.IntTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Token type ids matching each modality to a different value in the input sequence, i.e. text (0), image (1), video (2).
- **moe_mm_token_type_ids** (`torch.IntTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  The same as `mm_token_type_ids` while additionally considering start/end image/video tokens as respective vision tokens.
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
- **output_router_logits** (`bool`, *optional*) --
  Whether or not to return the logits of all the routers. They are useful for computing the router loss, and
  should not be returned during inference.
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
- **rope_deltas** (`torch.LongTensor` of shape `(batch_size, )`, *optional*) --
  The rope index difference between sequence length and multimodal rope.
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.
- **logits_to_keep** (`Union[int, torch.Tensor]`, *optional*, defaults to `0`) --
  If an `int`, compute logits for the last `logits_to_keep` tokens. If `0`, calculate logits for all
  `input_ids` (special case). Only last token logits are needed for generation, and calculating them only for that
  token can save memory, which becomes pretty significant for long sequences or large vocabulary size.
  If a `torch.Tensor`, must be 1D corresponding to the indices to keep in the sequence length dimension.
  This is useful when using packed tensor format (single dimension for batch and sequence length).0`transformers.modeling_outputs.MoeCausalLMOutputWithPast` or `tuple(torch.FloatTensor)`A `transformers.modeling_outputs.MoeCausalLMOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration (`None`) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).

- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).

- **aux_loss** (`torch.FloatTensor`, *optional*, returned when `labels` is provided) -- aux_loss for the sparse modules.

- **router_logits** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_router_probs=True` and `config.add_router_probs=True` is passed or when `config.output_router_probs=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, sequence_length, num_experts)`.

  Raw router logtis (post-softmax) that are computed by MoE routers, these terms are used to compute the auxiliary
  loss for Mixture of Experts models.

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
The [Ernie4_5_VL_MoeForConditionalGeneration](/docs/transformers/v5.0.0/en/model_doc/ernie4_5_vl_moe#transformers.Ernie4_5_VL_MoeForConditionalGeneration) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

**Parameters:**

input_ids (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) : Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.  [What are input IDs?](../glossary#input-ids)

attention_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) : Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:  - 1 for tokens that are **not masked**, - 0 for tokens that are **masked**.  [What are attention masks?](../glossary#attention-mask)

position_ids (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) : Indices of positions of each input sequence tokens in the position embeddings. Selected in the range `[0, config.n_positions - 1]`.  [What are position IDs?](../glossary#position-ids)

mm_token_type_ids (`torch.IntTensor` of shape `(batch_size, sequence_length)`, *optional*) : Token type ids matching each modality to a different value in the input sequence, i.e. text (0), image (1), video (2).

moe_mm_token_type_ids (`torch.IntTensor` of shape `(batch_size, sequence_length)`, *optional*) : The same as `mm_token_type_ids` while additionally considering start/end image/video tokens as respective vision tokens.

past_key_values (`~cache_utils.Cache`, *optional*) : Pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention blocks) that can be used to speed up sequential decoding. This typically consists in the `past_key_values` returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.  Only [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache). If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.  The model will output the same cache format that is fed as input.  If `past_key_values` are used, the user is expected to input only unprocessed `input_ids` (those that don't have their past key value states given to this model) of shape `(batch_size, unprocessed_length)` instead of all `input_ids` of shape `(batch_size, sequence_length)`.

inputs_embeds (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) : Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation. This is useful if you want more control over how to convert `input_ids` indices into associated vectors than the model's internal embedding lookup matrix.

labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) : Labels for computing the masked language modeling loss. Indices should either be in `[0, ..., config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.

use_cache (`bool`, *optional*) : If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see `past_key_values`).

output_router_logits (`bool`, *optional*) : Whether or not to return the logits of all the routers. They are useful for computing the router loss, and should not be returned during inference.

pixel_values (`torch.Tensor` of shape `(batch_size, num_channels, image_size, image_size)`, *optional*) : The tensors corresponding to the input images. Pixel values can be obtained using `image_processor_class`. See `image_processor_class.__call__` for details (`processor_class` uses `image_processor_class` for processing images).

pixel_values_videos (`torch.FloatTensor` of shape `(batch_size, num_frames, num_channels, frame_size, frame_size)`, *optional*) : The tensors corresponding to the input video. Pixel values for videos can be obtained using `video_processor_class`. See `video_processor_class.__call__` for details (`processor_class` uses `video_processor_class` for processing videos).

image_grid_thw (`torch.LongTensor` of shape `(num_images, 3)`, *optional*) : The temporal, height and width of feature shape of each image in LLM.

video_grid_thw (`torch.LongTensor` of shape `(num_videos, 3)`, *optional*) : The temporal, height and width of feature shape of each video in LLM.

rope_deltas (`torch.LongTensor` of shape `(batch_size, )`, *optional*) : The rope index difference between sequence length and multimodal rope.

cache_position (`torch.LongTensor` of shape `(sequence_length)`, *optional*) : Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`, this tensor is not affected by padding. It is used to update the cache in the correct position and to infer the complete sequence length.

logits_to_keep (`Union[int, torch.Tensor]`, *optional*, defaults to `0`) : If an `int`, compute logits for the last `logits_to_keep` tokens. If `0`, calculate logits for all `input_ids` (special case). Only last token logits are needed for generation, and calculating them only for that token can save memory, which becomes pretty significant for long sequences or large vocabulary size. If a `torch.Tensor`, must be 1D corresponding to the indices to keep in the sequence length dimension. This is useful when using packed tensor format (single dimension for batch and sequence length).

**Returns:**

``transformers.modeling_outputs.MoeCausalLMOutputWithPast` or `tuple(torch.FloatTensor)``

A `transformers.modeling_outputs.MoeCausalLMOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration (`None`) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).

- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).

- **aux_loss** (`torch.FloatTensor`, *optional*, returned when `labels` is provided) -- aux_loss for the sparse modules.

- **router_logits** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_router_probs=True` and `config.add_router_probs=True` is passed or when `config.output_router_probs=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, sequence_length, num_experts)`.

  Raw router logtis (post-softmax) that are computed by MoE routers, these terms are used to compute the auxiliary
  loss for Mixture of Experts models.

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
#### get_video_features[[transformers.Ernie4_5_VL_MoeForConditionalGeneration.get_video_features]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/ernie4_5_vl_moe/modeling_ernie4_5_vl_moe.py#L1612)

Example:

```python
>>> from PIL import Image
>>> from transformers import AutoProcessor, Ernie4_5_VL_MoeForConditionalGeneration

>>> model = Ernie4_5_VL_MoeForConditionalGeneration.from_pretrained("baidu/ERNIE-4.5-VL-28B-A3B-PT")
>>> processor = AutoProcessor.from_pretrained("baidu/ERNIE-4.5-VL-28B-A3B-PT")

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

pixel_values_videos (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`) : The tensors corresponding to the input videos.

video_grid_thw (`torch.LongTensor` of shape `(num_videos, 3)`, *optional*) : The temporal, height and width of feature shape of each video in LLM.

**Returns:**

`[transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Ernie4_5_VL_MoeConfig](/docs/transformers/v5.0.0/en/model_doc/ernie4_5_vl_moe#transformers.Ernie4_5_VL_MoeConfig)) and inputs.

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
#### get_image_features[[transformers.Ernie4_5_VL_MoeForConditionalGeneration.get_image_features]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/ernie4_5_vl_moe/modeling_ernie4_5_vl_moe.py#L1629)

Example:

```python
>>> from PIL import Image
>>> from transformers import AutoProcessor, Ernie4_5_VL_MoeForConditionalGeneration

>>> model = Ernie4_5_VL_MoeForConditionalGeneration.from_pretrained("baidu/ERNIE-4.5-VL-28B-A3B-PT")
>>> processor = AutoProcessor.from_pretrained("baidu/ERNIE-4.5-VL-28B-A3B-PT")

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

pixel_values (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`) : The tensors corresponding to the input images.

image_grid_thw (`torch.LongTensor` of shape `(num_images, 3)`, *optional*) : The temporal, height and width of feature shape of each image in LLM.

**Returns:**

`[transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Ernie4_5_VL_MoeConfig](/docs/transformers/v5.0.0/en/model_doc/ernie4_5_vl_moe#transformers.Ernie4_5_VL_MoeConfig)) and inputs.

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

