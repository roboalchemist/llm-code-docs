# Source: https://huggingface.co/docs/transformers/v5.0.0/model_doc/prompt_depth_anything.md

# Prompt Depth Anything

## Overview

The Prompt Depth Anything model was introduced in [Prompting Depth Anything for 4K Resolution Accurate Metric Depth Estimation](https://huggingface.co/papers/2412.14015) by Haotong Lin, Sida Peng, Jingxiao Chen, Songyou Peng, Jiaming Sun, Minghuan Liu, Hujun Bao, Jiashi Feng, Xiaowei Zhou, Bingyi Kang.

The abstract from the paper is as follows:

*Prompts play a critical role in unleashing the power of language and vision foundation models for specific tasks. For the first time, we introduce prompting into depth foundation models, creating a new paradigm for metric depth estimation termed Prompt Depth Anything. Specifically, we use a low-cost LiDAR as the prompt to guide the Depth Anything model for accurate metric depth output, achieving up to 4K resolution. Our approach centers on a concise prompt fusion design that integrates the LiDAR at multiple scales within the depth decoder. To address training challenges posed by limited datasets containing both LiDAR depth and precise GT depth, we propose a scalable data pipeline that includes synthetic data LiDAR simulation and real data pseudo GT depth generation. Our approach sets new state-of-the-arts on the ARKitScenes and ScanNet++ datasets and benefits downstream applications, including 3D reconstruction and generalized robotic grasping.*

 Prompt Depth Anything overview. Taken from the original paper.

## Usage example

The Transformers library allows you to use the model with just a few lines of code:

```python
>>> import torch
>>> import requests
>>> import numpy as np

>>> from PIL import Image
>>> from transformers import AutoImageProcessor, AutoModelForDepthEstimation

>>> url = "https://github.com/DepthAnything/PromptDA/blob/main/assets/example_images/image.jpg?raw=true"
>>> image = Image.open(requests.get(url, stream=True).raw)

>>> image_processor = AutoImageProcessor.from_pretrained("depth-anything/prompt-depth-anything-vits-hf")
>>> model = AutoModelForDepthEstimation.from_pretrained("depth-anything/prompt-depth-anything-vits-hf")

>>> prompt_depth_url = "https://github.com/DepthAnything/PromptDA/blob/main/assets/example_images/arkit_depth.png?raw=true"
>>> prompt_depth = Image.open(requests.get(prompt_depth_url, stream=True).raw)
>>> # the prompt depth can be None, and the model will output a monocular relative depth.

>>> # prepare image for the model
>>> inputs = image_processor(images=image, return_tensors="pt", prompt_depth=prompt_depth)

>>> with torch.no_grad():
...     outputs = model(**inputs)

>>> # interpolate to original size
>>> post_processed_output = image_processor.post_process_depth_estimation(
...     outputs,
...     target_sizes=[(image.height, image.width)],
... )

>>> # visualize the prediction
>>> predicted_depth = post_processed_output[0]["predicted_depth"]
>>> depth = predicted_depth * 1000 
>>> depth = depth.detach().cpu().numpy()
>>> depth = Image.fromarray(depth.astype("uint16")) # mm
```

## Resources

A list of official Hugging Face and community (indicated by 🌎) resources to help you get started with Prompt Depth Anything.

- [Prompt Depth Anything Demo](https://huggingface.co/spaces/depth-anything/PromptDA)
- [Prompt Depth Anything Interactive Results](https://promptda.github.io/interactive.html)

If you are interested in submitting a resource to be included here, please feel free to open a Pull Request and we'll review it! The resource should ideally demonstrate something new instead of duplicating an existing resource.

## PromptDepthAnythingConfig[[transformers.PromptDepthAnythingConfig]]

#### transformers.PromptDepthAnythingConfig[[transformers.PromptDepthAnythingConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/prompt_depth_anything/configuration_prompt_depth_anything.py#L30)

This is the configuration class to store the configuration of a `PromptDepthAnythingModel`. It is used to instantiate a PromptDepthAnything
model according to the specified arguments, defining the model architecture. Instantiating a configuration with the
defaults will yield a similar configuration to that of the PromptDepthAnything
[LiheYoung/depth-anything-small-hf](https://huggingface.co/LiheYoung/depth-anything-small-hf) architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:

```python
>>> from transformers import PromptDepthAnythingConfig, PromptDepthAnythingForDepthEstimation

>>> # Initializing a PromptDepthAnything small style configuration
>>> configuration = PromptDepthAnythingConfig()

>>> # Initializing a model from the PromptDepthAnything small style configuration
>>> model = PromptDepthAnythingForDepthEstimation(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

backbone_config (`Union[dict, "PreTrainedConfig"]`, *optional*, defaults to `Dinov2Config()`) : The configuration of the backbone model.

backbone (`str`, *optional*) : Name of backbone to use when `backbone_config` is `None`. If `use_pretrained_backbone` is `True`, this will load the corresponding pretrained weights from the timm or transformers library. If `use_pretrained_backbone` is `False`, this loads the backbone's config and uses that to initialize the backbone with random weights.

use_pretrained_backbone (`bool`, *optional*, defaults to `False`) : Whether to use pretrained weights for the backbone.

use_timm_backbone (`bool`, *optional*, defaults to `False`) : Whether or not to use the `timm` library for the backbone. If set to `False`, will use the [AutoBackbone](/docs/transformers/v5.0.0/en/main_classes/backbones#transformers.AutoBackbone) API.

backbone_kwargs (`dict`, *optional*) : Keyword arguments to be passed to AutoBackbone when loading from a checkpoint e.g. `{'out_indices': (0, 1, 2, 3)}`. Cannot be specified if `backbone_config` is set.

patch_size (`int`, *optional*, defaults to 14) : The size of the patches to extract from the backbone features.

initializer_range (`float`, *optional*, defaults to 0.02) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

reassemble_hidden_size (`int`, *optional*, defaults to 384) : The number of input channels of the reassemble layers.

reassemble_factors (`list[int]`, *optional*, defaults to `[4, 2, 1, 0.5]`) : The up/downsampling factors of the reassemble layers.

neck_hidden_sizes (`list[str]`, *optional*, defaults to `[48, 96, 192, 384]`) : The hidden sizes to project to for the feature maps of the backbone.

fusion_hidden_size (`int`, *optional*, defaults to 64) : The number of channels before fusion.

head_in_index (`int`, *optional*, defaults to -1) : The index of the features to use in the depth estimation head.

head_hidden_size (`int`, *optional*, defaults to 32) : The number of output channels in the second convolution of the depth estimation head.

depth_estimation_type (`str`, *optional*, defaults to `"relative"`) : The type of depth estimation to use. Can be one of `["relative", "metric"]`.

max_depth (`float`, *optional*) : The maximum depth to use for the "metric" depth estimation head. 20 should be used for indoor models and 80 for outdoor models. For "relative" depth estimation, this value is ignored.

## PromptDepthAnythingForDepthEstimation[[transformers.PromptDepthAnythingForDepthEstimation]]

#### transformers.PromptDepthAnythingForDepthEstimation[[transformers.PromptDepthAnythingForDepthEstimation]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/prompt_depth_anything/modeling_prompt_depth_anything.py#L373)

Prompt Depth Anything Model with a depth estimation head on top (consisting of 3 convolutional layers) e.g. for KITTI, NYUv2.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.PromptDepthAnythingForDepthEstimation.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/prompt_depth_anything/modeling_prompt_depth_anything.py#L386[{"name": "pixel_values", "val": ": FloatTensor"}, {"name": "prompt_depth", "val": ": torch.FloatTensor | None = None"}, {"name": "labels", "val": ": torch.LongTensor | None = None"}, {"name": "output_attentions", "val": ": bool | None = None"}, {"name": "output_hidden_states", "val": ": bool | None = None"}, {"name": "return_dict", "val": ": bool | None = None"}, {"name": "**kwargs", "val": ""}]- **pixel_values** (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [PromptDepthAnythingImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/prompt_depth_anything#transformers.PromptDepthAnythingImageProcessorFast). See [PromptDepthAnythingImageProcessorFast.__call__()](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details (`processor_class` uses
  [PromptDepthAnythingImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/prompt_depth_anything#transformers.PromptDepthAnythingImageProcessorFast) for processing images).
- **prompt_depth** (`torch.FloatTensor` of shape `(batch_size, 1, height, width)`, *optional*) --
  Prompt depth is the sparse or low-resolution depth obtained from multi-view geometry or a
  low-resolution depth sensor. It generally has shape (height, width), where height
  and width can be smaller than those of the images. It is optional and can be None, which means no prompt depth
  will be used. If it is None, the output will be a monocular relative depth.
  The values are recommended to be in meters, but this is not necessary.
- **labels** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Labels for computing the masked language modeling loss. Indices should either be in `[0, ...,
  config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored
  (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.
- **output_attentions** (`bool`, *optional*) --
  Whether or not to return the attentions tensors of all attention layers. See `attentions` under returned
  tensors for more detail.
- **output_hidden_states** (`bool`, *optional*) --
  Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
  more detail.
- **return_dict** (`bool`, *optional*) --
  Whether or not to return a [ModelOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.utils.ModelOutput) instead of a plain tuple.0[transformers.modeling_outputs.DepthEstimatorOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.DepthEstimatorOutput) or `tuple(torch.FloatTensor)`A [transformers.modeling_outputs.DepthEstimatorOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.DepthEstimatorOutput) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([PromptDepthAnythingConfig](/docs/transformers/v5.0.0/en/model_doc/prompt_depth_anything#transformers.PromptDepthAnythingConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Classification (or regression if config.num_labels==1) loss.
- **predicted_depth** (`torch.FloatTensor` of shape `(batch_size, height, width)`) -- Predicted depth for each pixel.

- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, num_channels, height, width)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, patch_size,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
The [PromptDepthAnythingForDepthEstimation](/docs/transformers/v5.0.0/en/model_doc/prompt_depth_anything#transformers.PromptDepthAnythingForDepthEstimation) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Example:

```python
>>> from transformers import AutoImageProcessor, AutoModelForDepthEstimation
>>> import torch
>>> import numpy as np
>>> from PIL import Image
>>> import httpx
>>> from io import BytesIO

>>> url = "https://github.com/DepthAnything/PromptDA/blob/main/assets/example_images/image.jpg?raw=true"
>>> with httpx.stream("GET", url) as response:
...     image = Image.open(BytesIO(response.read()))

>>> image_processor = AutoImageProcessor.from_pretrained("depth-anything/prompt-depth-anything-vits-hf")
>>> model = AutoModelForDepthEstimation.from_pretrained("depth-anything/prompt-depth-anything-vits-hf")

>>> prompt_depth_url = "https://github.com/DepthAnything/PromptDA/blob/main/assets/example_images/arkit_depth.png?raw=true"
>>> with httpx.stream("GET", prompt_depth_url) as response:
...     prompt_depth = Image.open(BytesIO(response.read()))

>>> # prepare image for the model
>>> inputs = image_processor(images=image, return_tensors="pt", prompt_depth=prompt_depth)

>>> with torch.no_grad():
...     outputs = model(**inputs)

>>> # interpolate to original size
>>> post_processed_output = image_processor.post_process_depth_estimation(
...     outputs,
...     target_sizes=[(image.height, image.width)],
... )

>>> # visualize the prediction
>>> predicted_depth = post_processed_output[0]["predicted_depth"]
>>> depth = predicted_depth * 1000.
>>> depth = depth.detach().cpu().numpy()
>>> depth = Image.fromarray(depth.astype("uint16")) # mm
```

**Parameters:**

config ([PromptDepthAnythingForDepthEstimation](/docs/transformers/v5.0.0/en/model_doc/prompt_depth_anything#transformers.PromptDepthAnythingForDepthEstimation)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

`[transformers.modeling_outputs.DepthEstimatorOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.DepthEstimatorOutput) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.DepthEstimatorOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.DepthEstimatorOutput) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([PromptDepthAnythingConfig](/docs/transformers/v5.0.0/en/model_doc/prompt_depth_anything#transformers.PromptDepthAnythingConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Classification (or regression if config.num_labels==1) loss.
- **predicted_depth** (`torch.FloatTensor` of shape `(batch_size, height, width)`) -- Predicted depth for each pixel.

- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, num_channels, height, width)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, patch_size,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.

## PromptDepthAnythingImageProcessor[[transformers.PromptDepthAnythingImageProcessor]]

#### transformers.PromptDepthAnythingImageProcessor[[transformers.PromptDepthAnythingImageProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/prompt_depth_anything/image_processing_prompt_depth_anything.py#L114)

Constructs a PromptDepthAnything image processor.

preprocesstransformers.PromptDepthAnythingImageProcessor.preprocesshttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/prompt_depth_anything/image_processing_prompt_depth_anything.py#L292[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor']]"}, {"name": "prompt_depth", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor'], NoneType] = None"}, {"name": "do_resize", "val": ": bool | None = None"}, {"name": "size", "val": ": int | None = None"}, {"name": "keep_aspect_ratio", "val": ": bool | None = None"}, {"name": "ensure_multiple_of", "val": ": int | None = None"}, {"name": "resample", "val": ": PIL.Image.Resampling | None = None"}, {"name": "do_rescale", "val": ": bool | None = None"}, {"name": "rescale_factor", "val": ": float | None = None"}, {"name": "do_normalize", "val": ": bool | None = None"}, {"name": "image_mean", "val": ": float | list[float] | None = None"}, {"name": "image_std", "val": ": float | list[float] | None = None"}, {"name": "do_pad", "val": ": bool | None = None"}, {"name": "size_divisor", "val": ": int | None = None"}, {"name": "prompt_scale_to_meter", "val": ": float | None = None"}, {"name": "return_tensors", "val": ": str | transformers.utils.generic.TensorType | None = None"}, {"name": "data_format", "val": ": ChannelDimension = "}, {"name": "input_data_format", "val": ": str | transformers.image_utils.ChannelDimension | None = None"}]- **images** (`ImageInput`) --
  Image to preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If
  passing in images with pixel values between 0 and 1, set `do_rescale=False`.
- **prompt_depth** (`ImageInput`, *optional*) --
  Prompt depth to preprocess, which can be sparse depth obtained from multi-view geometry or
  low-resolution depth from a depth sensor. Generally has shape (height, width), where height
  and width can be smaller than those of the images. It's optional and can be None, which means no prompt depth
  is used. If it is None, the output depth will be a monocular relative depth.
  It is recommended to provide a prompt_scale_to_meter value, which is the scale factor to convert the prompt depth
  to meters. This is useful when the prompt depth is not in meters.
- **do_resize** (`bool`, *optional*, defaults to `self.do_resize`) --
  Whether to resize the image.
- **size** (`dict[str, int]`, *optional*, defaults to `self.size`) --
  Size of the image after resizing. If `keep_aspect_ratio` is `True`, the image is resized to the largest
  possible size such that the aspect ratio is preserved. If `ensure_multiple_of` is set, the image is
  resized to a size that is a multiple of this value.
- **keep_aspect_ratio** (`bool`, *optional*, defaults to `self.keep_aspect_ratio`) --
  Whether to keep the aspect ratio of the image. If False, the image will be resized to (size, size). If
  True, the image will be resized to keep the aspect ratio and the size will be the maximum possible.
- **ensure_multiple_of** (`int`, *optional*, defaults to `self.ensure_multiple_of`) --
  Ensure that the image size is a multiple of this value.
- **resample** (`int`, *optional*, defaults to `self.resample`) --
  Resampling filter to use if resizing the image. This can be one of the enum `PILImageResampling`, Only
  has an effect if `do_resize` is set to `True`.
- **do_rescale** (`bool`, *optional*, defaults to `self.do_rescale`) --
  Whether to rescale the image values between [0 - 1].
- **rescale_factor** (`float`, *optional*, defaults to `self.rescale_factor`) --
  Rescale factor to rescale the image by if `do_rescale` is set to `True`.
- **do_normalize** (`bool`, *optional*, defaults to `self.do_normalize`) --
  Whether to normalize the image.
- **image_mean** (`float` or `list[float]`, *optional*, defaults to `self.image_mean`) --
  Image mean.
- **image_std** (`float` or `list[float]`, *optional*, defaults to `self.image_std`) --
  Image standard deviation.
- **prompt_scale_to_meter** (`float`, *optional*, defaults to `self.prompt_scale_to_meter`) --
  Scale factor to convert the prompt depth to meters.
- **return_tensors** (`str` or `TensorType`, *optional*) --
  The type of tensors to return. Can be one of:
  - Unset: Return a list of `np.ndarray`.
  - `TensorType.PYTORCH` or `'pt'`: Return a batch of type `torch.Tensor`.
  - `TensorType.NUMPY` or `'np'`: Return a batch of type `np.ndarray`.
- **data_format** (`ChannelDimension` or `str`, *optional*, defaults to `ChannelDimension.FIRST`) --
  The channel dimension format for the output image. Can be one of:
  - `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
  - `ChannelDimension.LAST`: image in (height, width, num_channels) format.
- **input_data_format** (`ChannelDimension` or `str`, *optional*) --
  The channel dimension format for the input image. If unset, the channel dimension format is inferred
  from the input image. Can be one of:
  - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
  - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.
  - `"none"` or `ChannelDimension.NONE`: image in (height, width) format.0

Preprocess an image or batch of images.

**Parameters:**

do_resize (`bool`, *optional*, defaults to `True`) : Whether to resize the image's (height, width) dimensions. Can be overridden by `do_resize` in `preprocess`.

size (`dict[str, int]` *optional*, defaults to `{"height" : 384, "width": 384}`): Size of the image after resizing. Can be overridden by `size` in `preprocess`.

resample (`PILImageResampling`, *optional*, defaults to `Resampling.BICUBIC`) : Defines the resampling filter to use if resizing the image. Can be overridden by `resample` in `preprocess`.

keep_aspect_ratio (`bool`, *optional*, defaults to `False`) : If `True`, the image is resized to the largest possible size such that the aspect ratio is preserved. Can be overridden by `keep_aspect_ratio` in `preprocess`.

ensure_multiple_of (`int`, *optional*, defaults to 1) : If `do_resize` is `True`, the image is resized to a size that is a multiple of this value. Can be overridden by `ensure_multiple_of` in `preprocess`.

do_rescale (`bool`, *optional*, defaults to `True`) : Whether to rescale the image by the specified scale `rescale_factor`. Can be overridden by `do_rescale` in `preprocess`.

rescale_factor (`int` or `float`, *optional*, defaults to `1/255`) : Scale factor to use if rescaling the image. Can be overridden by `rescale_factor` in `preprocess`.

do_normalize (`bool`, *optional*, defaults to `True`) : Whether to normalize the image. Can be overridden by the `do_normalize` parameter in the `preprocess` method.

image_mean (`float` or `list[float]`, *optional*, defaults to `IMAGENET_STANDARD_MEAN`) : Mean to use if normalizing the image. This is a float or list of floats the length of the number of channels in the image. Can be overridden by the `image_mean` parameter in the `preprocess` method.

image_std (`float` or `list[float]`, *optional*, defaults to `IMAGENET_STANDARD_STD`) : Standard deviation to use if normalizing the image. This is a float or list of floats the length of the number of channels in the image. Can be overridden by the `image_std` parameter in the `preprocess` method.

do_pad (`bool`, *optional*, defaults to `False`) : Whether to apply center padding. This was introduced in the DINOv2 paper, which uses the model in combination with DPT.

size_divisor (`int`, *optional*) : If `do_pad` is `True`, pads the image dimensions to be divisible by this value. This was introduced in the DINOv2 paper, which uses the model in combination with DPT.

prompt_scale_to_meter (`float`, *optional*, defaults to 0.001) : Scale factor to convert the prompt depth to meters.
#### post_process_depth_estimation[[transformers.PromptDepthAnythingImageProcessor.post_process_depth_estimation]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/prompt_depth_anything/image_processing_prompt_depth_anything.py#L472)

Converts the raw output of `DepthEstimatorOutput` into final depth predictions and depth PIL images.
Only supports PyTorch.

**Parameters:**

outputs (`DepthEstimatorOutput`) : Raw outputs of the model.

target_sizes (`TensorType` or `list[tuple[int, int]]`, *optional*) : Tensor of shape `(batch_size, 2)` or list of tuples (`tuple[int, int]`) containing the target size (height, width) of each image in the batch. If left to None, predictions will not be resized.

**Returns:**

``list[dict[str, TensorType]]``

A list of dictionaries of tensors representing the processed depth
predictions.

## PromptDepthAnythingImageProcessorFast[[transformers.PromptDepthAnythingImageProcessorFast]]

#### transformers.PromptDepthAnythingImageProcessorFast[[transformers.PromptDepthAnythingImageProcessorFast]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/prompt_depth_anything/image_processing_prompt_depth_anything_fast.py#L92)

Constructs a fast Prompt Depth Anything image processor.

preprocesstransformers.PromptDepthAnythingImageProcessorFast.preprocesshttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/prompt_depth_anything/image_processing_prompt_depth_anything_fast.py#L112[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor']]"}, {"name": "prompt_depth", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor'], NoneType] = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.models.prompt_depth_anything.image_processing_prompt_depth_anything.PromptDepthAnythingImageProcessorKwargs]"}]- **images** (`Union[PIL.Image.Image, numpy.ndarray, torch.Tensor, list, list, list]`) --
  Image to preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If
  passing in images with pixel values between 0 and 1, set `do_rescale=False`.
- **prompt_depth** (`ImageInput`, *optional*) --
  Prompt depth to preprocess.
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
- **keep_aspect_ratio** (`bool`, *optional*) --
  If `True`, the image is resized to the largest possible size such that the aspect ratio is preserved.
- **ensure_multiple_of** (`int`, *optional*) --
  If `do_resize` is `True`, the image is resized to a size that is a multiple of this value.
- **size_divisor** (`.size_divisor`) --
  The size by which to make sure both the height and width can be divided.
- **prompt_scale_to_meter** (`float`, *optional*) --
  Scale factor to convert the prompt depth to meters.0``- **data** (`dict`) -- Dictionary of lists/arrays/tensors returned by the __call__ method ('pixel_values', etc.).
- **tensor_type** (`Union[None, str, TensorType]`, *optional*) -- You can give a tensor_type here to convert the lists of integers in PyTorch/Numpy Tensors at
  initialization.

**Parameters:**

images (`Union[PIL.Image.Image, numpy.ndarray, torch.Tensor, list, list, list]`) : Image to preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If passing in images with pixel values between 0 and 1, set `do_rescale=False`.

prompt_depth (`ImageInput`, *optional*) : Prompt depth to preprocess.

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

keep_aspect_ratio (`bool`, *optional*) : If `True`, the image is resized to the largest possible size such that the aspect ratio is preserved.

ensure_multiple_of (`int`, *optional*) : If `do_resize` is `True`, the image is resized to a size that is a multiple of this value.

size_divisor (`.size_divisor`) : The size by which to make sure both the height and width can be divided.

prompt_scale_to_meter (`float`, *optional*) : Scale factor to convert the prompt depth to meters.

**Returns:**

````

- **data** (`dict`) -- Dictionary of lists/arrays/tensors returned by the __call__ method ('pixel_values', etc.).
- **tensor_type** (`Union[None, str, TensorType]`, *optional*) -- You can give a tensor_type here to convert the lists of integers in PyTorch/Numpy Tensors at
  initialization.
#### post_process_depth_estimation[[transformers.PromptDepthAnythingImageProcessorFast.post_process_depth_estimation]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/prompt_depth_anything/image_processing_prompt_depth_anything_fast.py#L305)

Converts the raw output of `DepthEstimatorOutput` into final depth predictions and depth PIL images.
Only supports PyTorch.

**Parameters:**

outputs (`DepthEstimatorOutput`) : Raw outputs of the model.

target_sizes (`TensorType` or `list[tuple[int, int]]`, *optional*) : Tensor of shape `(batch_size, 2)` or list of tuples (`tuple[int, int]`) containing the target size (height, width) of each image in the batch. If left to None, predictions will not be resized.

**Returns:**

``list[dict[str, TensorType]]``

A list of dictionaries of tensors representing the processed depth
predictions.

