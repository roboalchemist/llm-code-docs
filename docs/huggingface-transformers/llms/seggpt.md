# Source: https://huggingface.co/docs/transformers/v5.0.0rc1/model_doc/seggpt.md

# SegGPT

## Overview

The SegGPT model was proposed in [SegGPT: Segmenting Everything In Context](https://huggingface.co/papers/2304.03284) by Xinlong Wang, Xiaosong Zhang, Yue Cao, Wen Wang, Chunhua Shen, Tiejun Huang. SegGPT employs a decoder-only Transformer that can generate a segmentation mask given an input image, a prompt image and its corresponding prompt mask. The model achieves remarkable one-shot results with 56.1 mIoU on COCO-20 and 85.6 mIoU on FSS-1000.

The abstract from the paper is the following:

*We present SegGPT, a generalist model for segmenting everything in context. We unify various segmentation tasks into a generalist in-context learning framework that accommodates different kinds of segmentation data by transforming them into the same format of images. The training of SegGPT is formulated as an in-context coloring problem with random color mapping for each data sample. The objective is to accomplish diverse tasks according to the context, rather than relying on specific colors. After training, SegGPT can perform arbitrary segmentation tasks in images or videos via in-context inference, such as object instance, stuff, part, contour, and text. SegGPT is evaluated on a broad range of tasks, including few-shot semantic segmentation, video object segmentation, semantic segmentation, and panoptic segmentation. Our results show strong capabilities in segmenting in-domain and out-of*

Tips:

- One can use [SegGptImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/seggpt#transformers.SegGptImageProcessor) to prepare image input, prompt and mask to the model.
- One can either use segmentation maps or RGB images as prompt masks. If using the latter make sure to set `do_convert_rgb=False` in the `preprocess` method.
- It's highly advisable to pass `num_labels` when using `segmentation_maps` (not considering background) during preprocessing and postprocessing with [SegGptImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/seggpt#transformers.SegGptImageProcessor) for your use case.
- When doing inference with [SegGptForImageSegmentation](/docs/transformers/v5.0.0rc1/en/model_doc/seggpt#transformers.SegGptForImageSegmentation) if your `batch_size` is greater than 1 you can use feature ensemble across your images by passing `feature_ensemble=True` in the forward method.

Here's how to use the model for one-shot semantic segmentation:

```python
import torch
from datasets import load_dataset
from transformers import SegGptImageProcessor, SegGptForImageSegmentation

checkpoint = "BAAI/seggpt-vit-large"
image_processor = SegGptImageProcessor.from_pretrained(checkpoint)
model = SegGptForImageSegmentation.from_pretrained(checkpoint)

dataset_id = "EduardoPacheco/FoodSeg103"
ds = load_dataset(dataset_id, split="train")
# Number of labels in FoodSeg103 (not including background)
num_labels = 103

image_input = ds[4]["image"]
ground_truth = ds[4]["label"]
image_prompt = ds[29]["image"]
mask_prompt = ds[29]["label"]

inputs = image_processor(
    images=image_input, 
    prompt_images=image_prompt,
    segmentation_maps=mask_prompt, 
    num_labels=num_labels,
    return_tensors="pt"
)

with torch.no_grad():
    outputs = model(**inputs)

target_sizes = [image_input.size[::-1]]
mask = image_processor.post_process_semantic_segmentation(outputs, target_sizes, num_labels=num_labels)[0]
```

This model was contributed by [EduardoPacheco](https://huggingface.co/EduardoPacheco).
The original code can be found [here]([(https://github.com/baaivision/Painter/tree/main)).

## SegGptConfig[[transformers.SegGptConfig]]

#### transformers.SegGptConfig[[transformers.SegGptConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/seggpt/configuration_seggpt.py#L24)

This is the configuration class to store the configuration of a [SegGptModel](/docs/transformers/v5.0.0rc1/en/model_doc/seggpt#transformers.SegGptModel). It is used to instantiate a SegGPT
model according to the specified arguments, defining the model architecture. Instantiating a configuration with the
defaults will yield a similar configuration to that of the SegGPT
[BAAI/seggpt-vit-large](https://huggingface.co/BAAI/seggpt-vit-large) architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:

```python
>>> from transformers import SegGptConfig, SegGptModel

>>> # Initializing a SegGPT seggpt-vit-large style configuration
>>> configuration = SegGptConfig()

>>> # Initializing a model (with random weights) from the seggpt-vit-large style configuration
>>> model = SegGptModel(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

hidden_size (`int`, *optional*, defaults to 1024) : Dimensionality of the encoder layers and the pooler layer.

num_hidden_layers (`int`, *optional*, defaults to 24) : Number of hidden layers in the Transformer encoder.

num_attention_heads (`int`, *optional*, defaults to 16) : Number of attention heads for each attention layer in the Transformer encoder.

hidden_act (`str` or `function`, *optional*, defaults to `"gelu"`) : The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`, `"relu"`, `"selu"` and `"gelu_new"` are supported.

hidden_dropout_prob (`float`, *optional*, defaults to 0.0) : The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.

initializer_range (`float`, *optional*, defaults to 0.02) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

layer_norm_eps (`float`, *optional*, defaults to 1e-06) : The epsilon used by the layer normalization layers.

image_size (`list[int]`, *optional*, defaults to `[896, 448]`) : The size (resolution) of each image.

patch_size (`int`, *optional*, defaults to 16) : The size (resolution) of each patch.

num_channels (`int`, *optional*, defaults to 3) : The number of input channels.

qkv_bias (`bool`, *optional*, defaults to `True`) : Whether to add a bias to the queries, keys and values.

mlp_dim (`int`, *optional*) : The dimensionality of the MLP layer in the Transformer encoder. If unset, defaults to `hidden_size` * 4.

drop_path_rate (`float`, *optional*, defaults to 0.1) : The drop path rate for the dropout layers.

pretrain_image_size (`int`, *optional*, defaults to 224) : The pretrained size of the absolute position embeddings.

decoder_hidden_size (`int`, *optional*, defaults to 64) : Hidden size for decoder.

use_relative_position_embeddings (`bool`, *optional*, defaults to `True`) : Whether to use relative position embeddings in the attention layers.

merge_index (`int`, *optional*, defaults to 2) : The index of the encoder layer to merge the embeddings.

intermediate_hidden_state_indices (`list[int]`, *optional*, defaults to `[5, 11, 17, 23]`) : The indices of the encoder layers which we store as features for the decoder.

beta (`float`, *optional*, defaults to 0.01) : Regularization factor for SegGptLoss (smooth-l1 loss).

## SegGptImageProcessor[[transformers.SegGptImageProcessor]]

#### transformers.SegGptImageProcessor[[transformers.SegGptImageProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/seggpt/image_processing_seggpt.py#L95)

Constructs a SegGpt image processor.

preprocesstransformers.SegGptImageProcessor.preprocesshttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/seggpt/image_processing_seggpt.py#L383[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor'], NoneType] = None"}, {"name": "prompt_images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor'], NoneType] = None"}, {"name": "prompt_masks", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor'], NoneType] = None"}, {"name": "do_resize", "val": ": typing.Optional[bool] = None"}, {"name": "size", "val": ": typing.Optional[dict[str, int]] = None"}, {"name": "resample", "val": ": typing.Optional[PIL.Image.Resampling] = None"}, {"name": "do_rescale", "val": ": typing.Optional[bool] = None"}, {"name": "rescale_factor", "val": ": typing.Optional[float] = None"}, {"name": "do_normalize", "val": ": typing.Optional[bool] = None"}, {"name": "image_mean", "val": ": typing.Union[float, list[float], NoneType] = None"}, {"name": "image_std", "val": ": typing.Union[float, list[float], NoneType] = None"}, {"name": "do_convert_rgb", "val": ": typing.Optional[bool] = None"}, {"name": "num_labels", "val": ": typing.Optional[int] = None"}, {"name": "return_tensors", "val": ": typing.Union[str, transformers.utils.generic.TensorType, NoneType] = None"}, {"name": "data_format", "val": ": typing.Union[str, transformers.image_utils.ChannelDimension] = "}, {"name": "input_data_format", "val": ": typing.Union[str, transformers.image_utils.ChannelDimension, NoneType] = None"}, {"name": "**kwargs", "val": ""}]- **images** (`ImageInput`) --
  Image to _preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If
  passing in images with pixel values between 0 and 1, set `do_rescale=False`.
- **prompt_images** (`ImageInput`) --
  Prompt image to _preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If
  passing in images with pixel values between 0 and 1, set `do_rescale=False`.
- **prompt_masks** (`ImageInput`) --
  Prompt mask from prompt image to _preprocess that specify prompt_masks value in the preprocessed output.
  Can either be in the format of segmentation maps (no channels) or RGB images. If in the format of
  RGB images, `do_convert_rgb` should be set to `False`. If in the format of segmentation maps, `num_labels`
  specifying `num_labels` is recommended to build a palette to map the prompt mask from a single channel to
  a 3 channel RGB. If `num_labels` is not specified, the prompt mask will be duplicated across the channel
  dimension.
- **do_resize** (`bool`, *optional*, defaults to `self.do_resize`) --
  Whether to resize the image.
- **size** (`dict[str, int]`, *optional*, defaults to `self.size`) --
  Dictionary in the format `{"height": h, "width": w}` specifying the size of the output image after
  resizing.
- **resample** (`PILImageResampling` filter, *optional*, defaults to `self.resample`) --
  `PILImageResampling` filter to use if resizing the image e.g. `PILImageResampling.BICUBIC`. Only has
  an effect if `do_resize` is set to `True`. Doesn't apply to prompt mask as it is resized using nearest.
- **do_rescale** (`bool`, *optional*, defaults to `self.do_rescale`) --
  Whether to rescale the image values between [0 - 1].
- **rescale_factor** (`float`, *optional*, defaults to `self.rescale_factor`) --
  Rescale factor to rescale the image by if `do_rescale` is set to `True`.
- **do_normalize** (`bool`, *optional*, defaults to `self.do_normalize`) --
  Whether to normalize the image.
- **image_mean** (`float` or `list[float]`, *optional*, defaults to `self.image_mean`) --
  Image mean to use if `do_normalize` is set to `True`.
- **image_std** (`float` or `list[float]`, *optional*, defaults to `self.image_std`) --
  Image standard deviation to use if `do_normalize` is set to `True`.
- **do_convert_rgb** (`bool`, *optional*, defaults to `self.do_convert_rgb`) --
  Whether to convert the prompt mask to RGB format. If `num_labels` is specified, a palette will be built
  to map the prompt mask from a single channel to a 3 channel RGB. If unset, the prompt mask is duplicated
  across the channel dimension. Must be set to `False` if the prompt mask is already in RGB format.
- **num_labels** -- (`int`, *optional*):
  Number of classes in the segmentation task (excluding the background). If specified, a palette will be
  built, assuming that class_idx 0 is the background, to map the prompt mask from a plain segmentation map
  with no channels to a 3 channel RGB. Not specifying this will result in the prompt mask either being passed
  through as is if it is already in RGB format (if `do_convert_rgb` is false) or being duplicated
  across the channel dimension.
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

Preprocess an image or batch of images.

**Parameters:**

do_resize (`bool`, *optional*, defaults to `True`) : Whether to resize the image's (height, width) dimensions to the specified `(size["height"], size["width"])`. Can be overridden by the `do_resize` parameter in the `preprocess` method.

size (`dict`, *optional*, defaults to `{"height" : 448, "width": 448}`): Size of the output image after resizing. Can be overridden by the `size` parameter in the `preprocess` method.

resample (`PILImageResampling`, *optional*, defaults to `Resampling.BICUBIC`) : Resampling filter to use if resizing the image. Can be overridden by the `resample` parameter in the `preprocess` method.

do_rescale (`bool`, *optional*, defaults to `True`) : Whether to rescale the image by the specified scale `rescale_factor`. Can be overridden by the `do_rescale` parameter in the `preprocess` method.

rescale_factor (`int` or `float`, *optional*, defaults to `1/255`) : Scale factor to use if rescaling the image. Can be overridden by the `rescale_factor` parameter in the `preprocess` method.

do_normalize (`bool`, *optional*, defaults to `True`) : Whether to normalize the image. Can be overridden by the `do_normalize` parameter in the `preprocess` method.

image_mean (`float` or `list[float]`, *optional*, defaults to `IMAGENET_DEFAULT_MEAN`) : Mean to use if normalizing the image. This is a float or list of floats the length of the number of channels in the image. Can be overridden by the `image_mean` parameter in the `preprocess` method.

image_std (`float` or `list[float]`, *optional*, defaults to `IMAGENET_DEFAULT_STD`) : Standard deviation to use if normalizing the image. This is a float or list of floats the length of the number of channels in the image. Can be overridden by the `image_std` parameter in the `preprocess` method.

do_convert_rgb (`bool`, *optional*, defaults to `True`) : Whether to convert the prompt mask to RGB format. Can be overridden by the `do_convert_rgb` parameter in the `preprocess` method.
#### post_process_semantic_segmentation[[transformers.SegGptImageProcessor.post_process_semantic_segmentation]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/seggpt/image_processing_seggpt.py#L532)

Converts the output of `SegGptImageSegmentationOutput` into segmentation maps. Only supports
PyTorch.

**Parameters:**

outputs (`SegGptImageSegmentationOutput`) : Raw outputs of the model.

target_sizes (`list[tuple[int, int]]`, *optional*) : List of length (batch_size), where each list item (`tuple[int, int]`) corresponds to the requested final size (height, width) of each prediction. If left to None, predictions will not be resized.

num_labels (`int`, *optional*) : Number of classes in the segmentation task (excluding the background). If specified, a palette will be built, assuming that class_idx 0 is the background, to map prediction masks from RGB values to class indices. This value should be the same used when preprocessing inputs.

**Returns:**

`semantic_segmentation`

`list[torch.Tensor]` of length `batch_size`, where each item is a semantic
segmentation map of shape (height, width) corresponding to the target_sizes entry (if `target_sizes` is
specified). Each entry of each `torch.Tensor` correspond to a semantic class id.

## SegGptModel[[transformers.SegGptModel]]

#### transformers.SegGptModel[[transformers.SegGptModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/seggpt/modeling_seggpt.py#L623)

The bare Seggpt Model outputting raw hidden-states without any specific head on top.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.SegGptModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/seggpt/modeling_seggpt.py#L637[{"name": "pixel_values", "val": ": Tensor"}, {"name": "prompt_pixel_values", "val": ": Tensor"}, {"name": "prompt_masks", "val": ": Tensor"}, {"name": "bool_masked_pos", "val": ": typing.Optional[torch.BoolTensor] = None"}, {"name": "feature_ensemble", "val": ": typing.Optional[bool] = None"}, {"name": "embedding_type", "val": ": typing.Optional[str] = None"}, {"name": "labels", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "output_attentions", "val": ": typing.Optional[bool] = None"}, {"name": "output_hidden_states", "val": ": typing.Optional[bool] = None"}, {"name": "return_dict", "val": ": typing.Optional[bool] = None"}, {"name": "**kwargs", "val": ""}]- **pixel_values** (`torch.Tensor` of shape `(batch_size, num_channels, image_size, image_size)`) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [SegGptImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/seggpt#transformers.SegGptImageProcessor). See [SegGptImageProcessor.__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details (`processor_class` uses
  [SegGptImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/seggpt#transformers.SegGptImageProcessor) for processing images).
- **prompt_pixel_values** (`torch.FloatTensor` of shape `(batch_size, num_channels, height, width)`) --
  Prompt pixel values. Prompt pixel values can be obtained using [AutoImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoImageProcessor). See
  [SegGptImageProcessor.__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details.
- **prompt_masks** (`torch.FloatTensor` of shape `(batch_size, num_channels, height, width)`) --
  Prompt mask. Prompt mask can be obtained using [AutoImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoImageProcessor). See [SegGptImageProcessor.__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for
  details.
- **bool_masked_pos** (`torch.BoolTensor` of shape `(batch_size, num_patches)`, *optional*) --
  Boolean masked positions. Indicates which patches are masked (1) and which aren't (0).
- **feature_ensemble** (`bool`, *optional*) --
  Boolean indicating whether to use feature ensemble or not. If `True`, the model will use feature ensemble
  if we have at least two prompts. If `False`, the model will not use feature ensemble. This argument should
  be considered when doing few-shot inference on an input image i.e. more than one prompt for the same image.
- **embedding_type** (`str`, *optional*) --
  Embedding type. Indicates whether the prompt is a semantic or instance embedding. Can be either
  instance or semantic.
- **labels** (`torch.FloatTensor` of shape `(batch_size, num_channels, height, width)`, `optional`) --
  Ground truth mask for input images.
- **output_attentions** (`bool`, *optional*) --
  Whether or not to return the attentions tensors of all attention layers. See `attentions` under returned
  tensors for more detail.
- **output_hidden_states** (`bool`, *optional*) --
  Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
  more detail.
- **return_dict** (`bool`, *optional*) --
  Whether or not to return a [ModelOutput](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.utils.ModelOutput) instead of a plain tuple.0`transformers.models.seggpt.modeling_seggpt.SegGptEncoderOutput` or `tuple(torch.FloatTensor)`A `transformers.models.seggpt.modeling_seggpt.SegGptEncoderOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([SegGptConfig](/docs/transformers/v5.0.0rc1/en/model_doc/seggpt#transformers.SegGptConfig)) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, patch_height, patch_width, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.
- **hidden_states** (`tuple[torch.FloatTensor]`, `optional`, returned when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer)
  of shape `(batch_size, patch_height, patch_width, hidden_size)`.
- **attentions** (`tuple[torch.FloatTensor]`, `optional`, returned when `config.output_attentions=True`) -- Tuple of *torch.FloatTensor* (one for each layer) of shape
  `(batch_size, num_heads, seq_len, seq_len)`.
- **intermediate_hidden_states** (`tuple[torch.FloatTensor]`, *optional*, returned when `config.intermediate_hidden_state_indices` is set) -- Tuple of `torch.FloatTensor` of shape `(batch_size, patch_height, patch_width, hidden_size)`.
  Each element in the Tuple corresponds to the output of the layer specified in `config.intermediate_hidden_state_indices`.
  Additionally, each feature passes through a LayerNorm.
The [SegGptModel](/docs/transformers/v5.0.0rc1/en/model_doc/seggpt#transformers.SegGptModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Examples:

```python
>>> from transformers import SegGptImageProcessor, SegGptModel
>>> from PIL import Image
>>> import requests

>>> image_input_url = "https://raw.githubusercontent.com/baaivision/Painter/main/SegGPT/SegGPT_inference/examples/hmbb_2.jpg"
>>> image_prompt_url = "https://raw.githubusercontent.com/baaivision/Painter/main/SegGPT/SegGPT_inference/examples/hmbb_1.jpg"
>>> mask_prompt_url = "https://raw.githubusercontent.com/baaivision/Painter/main/SegGPT/SegGPT_inference/examples/hmbb_1_target.png"

>>> image_input = Image.open(requests.get(image_input_url, stream=True).raw)
>>> image_prompt = Image.open(requests.get(image_prompt_url, stream=True).raw)
>>> mask_prompt = Image.open(requests.get(mask_prompt_url, stream=True).raw).convert("L")

>>> checkpoint = "BAAI/seggpt-vit-large"
>>> model = SegGptModel.from_pretrained(checkpoint)
>>> image_processor = SegGptImageProcessor.from_pretrained(checkpoint)

>>> inputs = image_processor(images=image_input, prompt_images=image_prompt, prompt_masks=mask_prompt, return_tensors="pt")

>>> outputs = model(**inputs)
>>> list(outputs.last_hidden_state.shape)
[1, 56, 28, 1024]
```

**Parameters:**

config ([SegGptConfig](/docs/transformers/v5.0.0rc1/en/model_doc/seggpt#transformers.SegGptConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``transformers.models.seggpt.modeling_seggpt.SegGptEncoderOutput` or `tuple(torch.FloatTensor)``

A `transformers.models.seggpt.modeling_seggpt.SegGptEncoderOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([SegGptConfig](/docs/transformers/v5.0.0rc1/en/model_doc/seggpt#transformers.SegGptConfig)) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, patch_height, patch_width, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.
- **hidden_states** (`tuple[torch.FloatTensor]`, `optional`, returned when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer)
  of shape `(batch_size, patch_height, patch_width, hidden_size)`.
- **attentions** (`tuple[torch.FloatTensor]`, `optional`, returned when `config.output_attentions=True`) -- Tuple of *torch.FloatTensor* (one for each layer) of shape
  `(batch_size, num_heads, seq_len, seq_len)`.
- **intermediate_hidden_states** (`tuple[torch.FloatTensor]`, *optional*, returned when `config.intermediate_hidden_state_indices` is set) -- Tuple of `torch.FloatTensor` of shape `(batch_size, patch_height, patch_width, hidden_size)`.
  Each element in the Tuple corresponds to the output of the layer specified in `config.intermediate_hidden_state_indices`.
  Additionally, each feature passes through a LayerNorm.

## SegGptForImageSegmentation[[transformers.SegGptForImageSegmentation]]

#### transformers.SegGptForImageSegmentation[[transformers.SegGptForImageSegmentation]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/seggpt/modeling_seggpt.py#L823)

SegGpt model with a decoder on top for one-shot image segmentation.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.SegGptForImageSegmentation.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/seggpt/modeling_seggpt.py#L834[{"name": "pixel_values", "val": ": Tensor"}, {"name": "prompt_pixel_values", "val": ": Tensor"}, {"name": "prompt_masks", "val": ": Tensor"}, {"name": "bool_masked_pos", "val": ": typing.Optional[torch.BoolTensor] = None"}, {"name": "feature_ensemble", "val": ": typing.Optional[bool] = None"}, {"name": "embedding_type", "val": ": typing.Optional[str] = None"}, {"name": "labels", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "output_attentions", "val": ": typing.Optional[bool] = None"}, {"name": "output_hidden_states", "val": ": typing.Optional[bool] = None"}, {"name": "return_dict", "val": ": typing.Optional[bool] = None"}, {"name": "**kwargs", "val": ""}]- **pixel_values** (`torch.Tensor` of shape `(batch_size, num_channels, image_size, image_size)`) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [SegGptImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/seggpt#transformers.SegGptImageProcessor). See [SegGptImageProcessor.__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details (`processor_class` uses
  [SegGptImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/seggpt#transformers.SegGptImageProcessor) for processing images).
- **prompt_pixel_values** (`torch.FloatTensor` of shape `(batch_size, num_channels, height, width)`) --
  Prompt pixel values. Prompt pixel values can be obtained using [AutoImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoImageProcessor). See
  [SegGptImageProcessor.__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details.
- **prompt_masks** (`torch.FloatTensor` of shape `(batch_size, num_channels, height, width)`) --
  Prompt mask. Prompt mask can be obtained using [AutoImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoImageProcessor). See [SegGptImageProcessor.__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for
  details.
- **bool_masked_pos** (`torch.BoolTensor` of shape `(batch_size, num_patches)`, *optional*) --
  Boolean masked positions. Indicates which patches are masked (1) and which aren't (0).
- **feature_ensemble** (`bool`, *optional*) --
  Boolean indicating whether to use feature ensemble or not. If `True`, the model will use feature ensemble
  if we have at least two prompts. If `False`, the model will not use feature ensemble. This argument should
  be considered when doing few-shot inference on an input image i.e. more than one prompt for the same image.
- **embedding_type** (`str`, *optional*) --
  Embedding type. Indicates whether the prompt is a semantic or instance embedding. Can be either
  instance or semantic.
- **labels** (`torch.FloatTensor` of shape `(batch_size, num_channels, height, width)`, `optional`) --
  Ground truth mask for input images.
- **output_attentions** (`bool`, *optional*) --
  Whether or not to return the attentions tensors of all attention layers. See `attentions` under returned
  tensors for more detail.
- **output_hidden_states** (`bool`, *optional*) --
  Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
  more detail.
- **return_dict** (`bool`, *optional*) --
  Whether or not to return a [ModelOutput](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.utils.ModelOutput) instead of a plain tuple.0`transformers.models.seggpt.modeling_seggpt.SegGptImageSegmentationOutput` or `tuple(torch.FloatTensor)`A `transformers.models.seggpt.modeling_seggpt.SegGptImageSegmentationOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([SegGptConfig](/docs/transformers/v5.0.0rc1/en/model_doc/seggpt#transformers.SegGptConfig)) and inputs.

- **loss** (`torch.FloatTensor`, *optional*, returned when `labels` is provided) -- The loss value.
- **pred_masks** (`torch.FloatTensor` of shape `(batch_size, num_channels, height, width)`) -- The predicted masks.
- **hidden_states** (`tuple[torch.FloatTensor]`, `optional`, returned when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer)
  of shape `(batch_size, patch_height, patch_width, hidden_size)`.
- **attentions** (`tuple[torch.FloatTensor]`, `optional`, returned when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape
  `(batch_size, num_heads, seq_len, seq_len)`.
The [SegGptForImageSegmentation](/docs/transformers/v5.0.0rc1/en/model_doc/seggpt#transformers.SegGptForImageSegmentation) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Examples:

```python
>>> from transformers import SegGptImageProcessor, SegGptForImageSegmentation
>>> from PIL import Image
>>> import requests

>>> image_input_url = "https://raw.githubusercontent.com/baaivision/Painter/main/SegGPT/SegGPT_inference/examples/hmbb_2.jpg"
>>> image_prompt_url = "https://raw.githubusercontent.com/baaivision/Painter/main/SegGPT/SegGPT_inference/examples/hmbb_1.jpg"
>>> mask_prompt_url = "https://raw.githubusercontent.com/baaivision/Painter/main/SegGPT/SegGPT_inference/examples/hmbb_1_target.png"

>>> image_input = Image.open(requests.get(image_input_url, stream=True).raw)
>>> image_prompt = Image.open(requests.get(image_prompt_url, stream=True).raw)
>>> mask_prompt = Image.open(requests.get(mask_prompt_url, stream=True).raw).convert("L")

>>> checkpoint = "BAAI/seggpt-vit-large"
>>> model = SegGptForImageSegmentation.from_pretrained(checkpoint)
>>> image_processor = SegGptImageProcessor.from_pretrained(checkpoint)

>>> inputs = image_processor(images=image_input, prompt_images=image_prompt, prompt_masks=mask_prompt, return_tensors="pt")
>>> outputs = model(**inputs)
>>> result = image_processor.post_process_semantic_segmentation(outputs, target_sizes=[(image_input.height, image_input.width)])[0]
>>> print(list(result.shape))
[170, 297]
```

**Parameters:**

config ([SegGptConfig](/docs/transformers/v5.0.0rc1/en/model_doc/seggpt#transformers.SegGptConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``transformers.models.seggpt.modeling_seggpt.SegGptImageSegmentationOutput` or `tuple(torch.FloatTensor)``

A `transformers.models.seggpt.modeling_seggpt.SegGptImageSegmentationOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([SegGptConfig](/docs/transformers/v5.0.0rc1/en/model_doc/seggpt#transformers.SegGptConfig)) and inputs.

- **loss** (`torch.FloatTensor`, *optional*, returned when `labels` is provided) -- The loss value.
- **pred_masks** (`torch.FloatTensor` of shape `(batch_size, num_channels, height, width)`) -- The predicted masks.
- **hidden_states** (`tuple[torch.FloatTensor]`, `optional`, returned when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer)
  of shape `(batch_size, patch_height, patch_width, hidden_size)`.
- **attentions** (`tuple[torch.FloatTensor]`, `optional`, returned when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape
  `(batch_size, num_heads, seq_len, seq_len)`.

