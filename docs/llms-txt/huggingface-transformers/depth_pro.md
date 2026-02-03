# Source: https://huggingface.co/docs/transformers/v5.0.0/model_doc/depth_pro.md

# DepthPro

## Overview

The DepthPro model was proposed in [Depth Pro: Sharp Monocular Metric Depth in Less Than a Second](https://huggingface.co/papers/2410.02073) by Aleksei Bochkovskii, Amaël Delaunoy, Hugo Germain, Marcel Santos, Yichao Zhou, Stephan R. Richter, Vladlen Koltun.

DepthPro is a foundation model for zero-shot metric monocular depth estimation, designed to generate high-resolution depth maps with remarkable sharpness and fine-grained details. It employs a multi-scale Vision Transformer (ViT)-based architecture, where images are downsampled, divided into patches, and processed using a shared Dinov2 encoder. The extracted patch-level features are merged, upsampled, and refined using a DPT-like fusion stage, enabling precise depth estimation.

The abstract from the paper is the following:

*We present a foundation model for zero-shot metric monocular depth estimation. Our model, Depth Pro, synthesizes high-resolution depth maps with unparalleled sharpness and high-frequency details. The predictions are metric, with absolute scale, without relying on the availability of metadata such as camera intrinsics. And the model is fast, producing a 2.25-megapixel depth map in 0.3 seconds on a standard GPU. These characteristics are enabled by a number of technical contributions, including an efficient multi-scale vision transformer for dense prediction, a training protocol that combines real and synthetic datasets to achieve high metric accuracy alongside fine boundary tracing, dedicated evaluation metrics for boundary accuracy in estimated depth maps, and state-of-the-art focal length estimation from a single image. Extensive experiments analyze specific design choices and demonstrate that Depth Pro outperforms prior work along multiple dimensions.*

 DepthPro Outputs. Taken from the official code. 

This model was contributed by [geetu040](https://github.com/geetu040). The original code can be found [here](https://github.com/apple/ml-depth-pro).

## Usage Tips

The DepthPro model processes an input image by first downsampling it at multiple scales and splitting each scaled version into patches. These patches are then encoded using a shared Vision Transformer (ViT)-based Dinov2 patch encoder, while the full image is processed by a separate image encoder. The extracted patch features are merged into feature maps, upsampled, and fused using a DPT-like decoder to generate the final depth estimation. If enabled, an additional Field of View (FOV) encoder processes the image for estimating the camera's field of view, aiding in depth accuracy.

```py
>>> import requests
>>> from PIL import Image
>>> import torch
>>> from transformers import DepthProImageProcessorFast, DepthProForDepthEstimation
from accelerate import Accelerator

>>> device = Accelerator().device

>>> url = 'http://images.cocodataset.org/val2017/000000039769.jpg'
>>> image = Image.open(requests.get(url, stream=True).raw)

>>> image_processor = DepthProImageProcessorFast.from_pretrained("apple/DepthPro-hf")
>>> model = DepthProForDepthEstimation.from_pretrained("apple/DepthPro-hf").to(device)

>>> inputs = image_processor(images=image, return_tensors="pt").to(model.device)

>>> with torch.no_grad():
...     outputs = model(**inputs)

>>> post_processed_output = image_processor.post_process_depth_estimation(
...     outputs, target_sizes=[(image.height, image.width)],
... )

>>> field_of_view = post_processed_output[0]["field_of_view"]
>>> focal_length = post_processed_output[0]["focal_length"]
>>> depth = post_processed_output[0]["predicted_depth"]
>>> depth = (depth - depth.min()) / depth.max()
>>> depth = depth * 255.
>>> depth = depth.detach().cpu().numpy()
>>> depth = Image.fromarray(depth.astype("uint8"))
```

### Architecture and Configuration

 DepthPro architecture. Taken from the original paper. 

The `DepthProForDepthEstimation` model uses a `DepthProEncoder`, for encoding the input image and a `FeatureFusionStage` for fusing the output features from encoder.

The `DepthProEncoder` further uses two encoders:

- `patch_encoder`
  - Input image is scaled with multiple ratios, as specified in the `scaled_images_ratios` configuration.
  - Each scaled image is split into smaller **patches** of size `patch_size` with overlapping areas determined by `scaled_images_overlap_ratios`.
  - These patches are processed by the **`patch_encoder`**
- `image_encoder`
  - Input image is also rescaled to `patch_size` and processed by the **`image_encoder`**

Both these encoders can be configured via `patch_model_config` and `image_model_config` respectively, both of which are separate `Dinov2Model` by default.

Outputs from both encoders (`last_hidden_state`) and selected intermediate states (`hidden_states`) from **`patch_encoder`** are fused by a `DPT`-based `FeatureFusionStage` for depth estimation.

### Field-of-View (FOV) Prediction

The network is supplemented with a focal length estimation head. A small convolutional head ingests frozen features from the depth estimation network and task-specific features from a separate ViT image encoder to predict the horizontal angular field-of-view.

The `use_fov_model` parameter in `DepthProConfig` controls whether **FOV prediction** is enabled. By default, it is set to `False` to conserve memory and computation. When enabled, the **FOV encoder** is instantiated based on the `fov_model_config` parameter, which defaults to a `Dinov2Model`. The `use_fov_model` parameter can also be passed when initializing the `DepthProForDepthEstimation` model.

The pretrained model at checkpoint `apple/DepthPro-hf` uses the FOV encoder. To use the pretrained-model without FOV encoder, set `use_fov_model=False` when loading the model, which saves computation.

```py
>>> from transformers import DepthProForDepthEstimation
>>> model = DepthProForDepthEstimation.from_pretrained("apple/DepthPro-hf", use_fov_model=False)
```

To instantiate a new model with FOV encoder, set `use_fov_model=True` in the config.

```py
>>> from transformers import DepthProConfig, DepthProForDepthEstimation
>>> config = DepthProConfig(use_fov_model=True)
>>> model = DepthProForDepthEstimation(config)
```

Or set `use_fov_model=True` when initializing the model, which overrides the value in config.

```py
>>> from transformers import DepthProConfig, DepthProForDepthEstimation
>>> config = DepthProConfig()
>>> model = DepthProForDepthEstimation(config, use_fov_model=True)
```

### Using Scaled Dot Product Attention (SDPA)

PyTorch includes a native scaled dot-product attention (SDPA) operator as part of `torch.nn.functional`. This function
encompasses several implementations that can be applied depending on the inputs and the hardware in use. See the
[official documentation](https://pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html)
or the [GPU Inference](https://huggingface.co/docs/transformers/main/en/perf_infer_gpu_one#pytorch-scaled-dot-product-attention)
page for more information.

SDPA is used by default for `torch>=2.1.1` when an implementation is available, but you may also set
`attn_implementation="sdpa"` in `from_pretrained()` to explicitly request SDPA to be used.

```py
from transformers import DepthProForDepthEstimation
model = DepthProForDepthEstimation.from_pretrained("apple/DepthPro-hf", attn_implementation="sdpa", dtype=torch.float16)
```

For the best speedups, we recommend loading the model in half-precision (e.g. `torch.float16` or `torch.bfloat16`).

On a local benchmark (A100-40GB, PyTorch 2.3.0, OS Ubuntu 22.04) with `float32` and `google/vit-base-patch16-224` model, we saw the following speedups during inference.

|   Batch size |   Average inference time (ms), eager mode |   Average inference time (ms), sdpa model |   Speed up, Sdpa / Eager (x) |
|--------------|-------------------------------------------|-------------------------------------------|------------------------------|
|            1 |                                         7 |                                         6 |                      1.17 |
|            2 |                                         8 |                                         6 |                      1.33 |
|            4 |                                         8 |                                         6 |                      1.33 |
|            8 |                                         8 |                                         6 |                      1.33 |

## Resources

A list of official Hugging Face and community (indicated by 🌎) resources to help you get started with DepthPro:

- Research Paper: [Depth Pro: Sharp Monocular Metric Depth in Less Than a Second](https://huggingface.co/papers/2410.02073)
- Official Implementation: [apple/ml-depth-pro](https://github.com/apple/ml-depth-pro)
- DepthPro Inference Notebook: [DepthPro Inference](https://github.com/qubvel/transformers-notebooks/blob/main/notebooks/DepthPro_inference.ipynb)
- DepthPro for Super Resolution and Image Segmentation
  - Read blog on Medium: [Depth Pro: Beyond Depth](https://medium.com/@raoarmaghanshakir040/depth-pro-beyond-depth-9d822fc557ba)
  - Code on Github: [geetu040/depthpro-beyond-depth](https://github.com/geetu040/depthpro-beyond-depth)

If you're interested in submitting a resource to be included here, please feel free to open a Pull Request and we'll review it! The resource should ideally demonstrate something new instead of duplicating an existing resource.

## DepthProConfig[[transformers.DepthProConfig]]

#### transformers.DepthProConfig[[transformers.DepthProConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/depth_pro/configuration_depth_pro.py#L26)

This is the configuration class to store the configuration of a [DepthProModel](/docs/transformers/v5.0.0/en/model_doc/depth_pro#transformers.DepthProModel). It is used to instantiate a
DepthPro model according to the specified arguments, defining the model architecture. Instantiating a configuration
with the defaults will yield a similar configuration to that of the DepthPro
[apple/DepthPro](https://huggingface.co/apple/DepthPro) architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:

```python
>>> from transformers import DepthProConfig, DepthProModel

>>> # Initializing a DepthPro apple/DepthPro style configuration
>>> configuration = DepthProConfig()

>>> # Initializing a model (with random weights) from the apple/DepthPro style configuration
>>> model = DepthProModel(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

fusion_hidden_size (`int`, *optional*, defaults to 256) : The number of channels before fusion.

patch_size (`int`, *optional*, defaults to 384) : The size (resolution) of each patch. This is also the image_size for backbone model.

initializer_range (`float`, *optional*, defaults to 0.02) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

intermediate_hook_ids (`list[int]`, *optional*, defaults to `[11, 5]`) : Indices of the intermediate hidden states from the patch encoder to use for fusion.

intermediate_feature_dims (`list[int]`, *optional*, defaults to `[256, 256]`) : Hidden state dimensions during upsampling for each intermediate hidden state in `intermediate_hook_ids`.

scaled_images_ratios (`list[float]`, *optional*, defaults to `[0.25, 0.5, 1]`) : Ratios of scaled images to be used by the patch encoder.

scaled_images_overlap_ratios (`list[float]`, *optional*, defaults to `[0.0, 0.5, 0.25]`) : Overlap ratios between patches for each scaled image in `scaled_images_ratios`.

scaled_images_feature_dims (`list[int]`, *optional*, defaults to `[1024, 1024, 512]`) : Hidden state dimensions during upsampling for each scaled image in `scaled_images_ratios`.

merge_padding_value (`int`, *optional*, defaults to 3) : When merging smaller patches back to the image size, overlapping sections of this size are removed.

use_batch_norm_in_fusion_residual (`bool`, *optional*, defaults to `False`) : Whether to use batch normalization in the pre-activate residual units of the fusion blocks.

use_bias_in_fusion_residual (`bool`, *optional*, defaults to `True`) : Whether to use bias in the pre-activate residual units of the fusion blocks.

use_fov_model (`bool`, *optional*, defaults to `False`) : Whether to use `DepthProFovModel` to generate the field of view.

num_fov_head_layers (`int`, *optional*, defaults to 2) : Number of convolution layers in the head of `DepthProFovModel`.

image_model_config (`Union[dict[str, Any], PreTrainedConfig]`, *optional*) : The configuration of the image encoder model, which is loaded using the [AutoModel](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoModel) API. By default, Dinov2 model is used as backbone.

patch_model_config (`Union[dict[str, Any], PreTrainedConfig]`, *optional*) : The configuration of the patch encoder model, which is loaded using the [AutoModel](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoModel) API. By default, Dinov2 model is used as backbone.

fov_model_config (`Union[dict[str, Any], PreTrainedConfig]`, *optional*) : The configuration of the fov encoder model, which is loaded using the [AutoModel](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoModel) API. By default, Dinov2 model is used as backbone.

## DepthProImageProcessor[[transformers.DepthProImageProcessor]]

#### transformers.DepthProImageProcessor[[transformers.DepthProImageProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/depth_pro/image_processing_depth_pro.py#L55)

Constructs a DepthPro image processor.

preprocesstransformers.DepthProImageProcessor.preprocesshttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/depth_pro/image_processing_depth_pro.py#L190[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor']]"}, {"name": "do_resize", "val": ": bool | None = None"}, {"name": "size", "val": ": dict[str, int] | None = None"}, {"name": "resample", "val": ": PIL.Image.Resampling | None = None"}, {"name": "do_rescale", "val": ": bool | None = None"}, {"name": "rescale_factor", "val": ": float | None = None"}, {"name": "do_normalize", "val": ": bool | None = None"}, {"name": "image_mean", "val": ": float | list[float] | None = None"}, {"name": "image_std", "val": ": float | list[float] | None = None"}, {"name": "return_tensors", "val": ": str | transformers.utils.generic.TensorType | None = None"}, {"name": "data_format", "val": ": str | transformers.image_utils.ChannelDimension = "}, {"name": "input_data_format", "val": ": str | transformers.image_utils.ChannelDimension | None = None"}]- **images** (`ImageInput`) --
  Image to preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If
  passing in images with pixel values between 0 and 1, set `do_rescale=False`.
- **do_resize** (`bool`, *optional*, defaults to `self.do_resize`) --
  Whether to resize the image.
- **size** (`dict[str, int]`, *optional*, defaults to `self.size`) --
  Dictionary in the format `{"height": h, "width": w}` specifying the size of the output image after
  resizing.
- **resample** (`PILImageResampling` filter, *optional*, defaults to `self.resample`) --
  `PILImageResampling` filter to use if resizing the image e.g. `PILImageResampling.BILINEAR`. Only has
  an effect if `do_resize` is set to `True`.
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

size (`dict`, *optional*, defaults to `{"height" : 1536, "width": 1536}`): Size of the output image after resizing. Can be overridden by the `size` parameter in the `preprocess` method.

resample (`PILImageResampling`, *optional*, defaults to `Resampling.BILINEAR`) : Resampling filter to use if resizing the image. Can be overridden by the `resample` parameter in the `preprocess` method.

do_rescale (`bool`, *optional*, defaults to `True`) : Whether to rescale the image by the specified scale `rescale_factor`. Can be overridden by the `do_rescale` parameter in the `preprocess` method.

rescale_factor (`int` or `float`, *optional*, defaults to `1/255`) : Scale factor to use if rescaling the image. Can be overridden by the `rescale_factor` parameter in the `preprocess` method.

do_normalize (`bool`, *optional*, defaults to `True`) : Whether to normalize the image. Can be overridden by the `do_normalize` parameter in the `preprocess` method.

image_mean (`float` or `list[float]`, *optional*, defaults to `IMAGENET_STANDARD_MEAN`) : Mean to use if normalizing the image. This is a float or list of floats the length of the number of channels in the image. Can be overridden by the `image_mean` parameter in the `preprocess` method.

image_std (`float` or `list[float]`, *optional*, defaults to `IMAGENET_STANDARD_STD`) : Standard deviation to use if normalizing the image. This is a float or list of floats the length of the number of channels in the image. Can be overridden by the `image_std` parameter in the `preprocess` method.
#### post_process_depth_estimation[[transformers.DepthProImageProcessor.post_process_depth_estimation]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/depth_pro/image_processing_depth_pro.py#L311)

Post-processes the raw depth predictions from the model to generate
final depth predictions which is caliberated using the field of view if provided
and resized to specified target sizes if provided.

**Parameters:**

outputs (`DepthProDepthEstimatorOutput`) : Raw outputs of the model.

target_sizes (`Optional[Union[TensorType, list[tuple[int, int]], None]]`, *optional*, defaults to `None`) : Target sizes to resize the depth predictions. Can be a tensor of shape `(batch_size, 2)` or a list of tuples `(height, width)` for each image in the batch. If `None`, no resizing is performed.

**Returns:**

``list[dict[str, TensorType]]``

A list of dictionaries of tensors representing the processed depth
predictions, and field of view (degrees) and focal length (pixels) if `field_of_view` is given in `outputs`.

## DepthProImageProcessorFast[[transformers.DepthProImageProcessorFast]]

#### transformers.DepthProImageProcessorFast[[transformers.DepthProImageProcessorFast]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/depth_pro/image_processing_depth_pro_fast.py#L50)

Constructs a fast Depth Pro image processor.

preprocesstransformers.DepthProImageProcessorFast.preprocesshttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/image_processing_utils_fast.py#L838[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor']]"}, {"name": "*args", "val": ""}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.processing_utils.ImagesKwargs]"}]- **images** (`Union[PIL.Image.Image, numpy.ndarray, torch.Tensor, list, list, list]`) --
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
  Added for backward compatibility but this should be set as a processor attribute in future models.0``- **data** (`dict`) -- Dictionary of lists/arrays/tensors returned by the __call__ method ('pixel_values', etc.).
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

**Returns:**

````

- **data** (`dict`) -- Dictionary of lists/arrays/tensors returned by the __call__ method ('pixel_values', etc.).
- **tensor_type** (`Union[None, str, TensorType]`, *optional*) -- You can give a tensor_type here to convert the lists of integers in PyTorch/Numpy Tensors at
  initialization.
#### post_process_depth_estimation[[transformers.DepthProImageProcessorFast.post_process_depth_estimation]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/depth_pro/image_processing_depth_pro_fast.py#L100)

Post-processes the raw depth predictions from the model to generate
final depth predictions which is caliberated using the field of view if provided
and resized to specified target sizes if provided.

**Parameters:**

outputs (`DepthProDepthEstimatorOutput`) : Raw outputs of the model.

target_sizes (`Optional[Union[TensorType, list[tuple[int, int]], None]]`, *optional*, defaults to `None`) : Target sizes to resize the depth predictions. Can be a tensor of shape `(batch_size, 2)` or a list of tuples `(height, width)` for each image in the batch. If `None`, no resizing is performed.

**Returns:**

``list[dict[str, TensorType]]``

A list of dictionaries of tensors representing the processed depth
predictions, and field of view (degrees) and focal length (pixels) if `field_of_view` is given in `outputs`.

## DepthProModel[[transformers.DepthProModel]]

#### transformers.DepthProModel[[transformers.DepthProModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/depth_pro/modeling_depth_pro.py#L627)

The bare Depth Pro Model outputting raw hidden-states without any specific head on top.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.DepthProModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/depth_pro/modeling_depth_pro.py#L639[{"name": "pixel_values", "val": ": FloatTensor"}, {"name": "output_attentions", "val": ": bool | None = None"}, {"name": "output_hidden_states", "val": ": bool | None = None"}, {"name": "return_dict", "val": ": bool | None = None"}, {"name": "**kwargs", "val": ""}]- **pixel_values** (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [DepthProImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/depth_pro#transformers.DepthProImageProcessorFast). See [DepthProImageProcessorFast.__call__()](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details (`processor_class` uses
  [DepthProImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/depth_pro#transformers.DepthProImageProcessorFast) for processing images).
- **output_attentions** (`bool`, *optional*) --
  Whether or not to return the attentions tensors of all attention layers. See `attentions` under returned
  tensors for more detail.
- **output_hidden_states** (`bool`, *optional*) --
  Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
  more detail.
- **return_dict** (`bool`, *optional*) --
  Whether or not to return a [ModelOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.utils.ModelOutput) instead of a plain tuple.0`transformers.models.depth_pro.modeling_depth_pro.DepthProOutput` or `tuple(torch.FloatTensor)`A `transformers.models.depth_pro.modeling_depth_pro.DepthProOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([DepthProConfig](/docs/transformers/v5.0.0/en/model_doc/depth_pro#transformers.DepthProConfig)) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, n_patches_per_batch, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.
- **features** (`Union[torch.FloatTensor, List[torch.FloatTensor]]`, *optional*) -- Features from encoders. Can be a single feature or a list of features.
- **hidden_states** (`tuple[torch.FloatTensor, ...] | None.hidden_states`, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple[torch.FloatTensor, ...] | None.attentions`, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
The [DepthProModel](/docs/transformers/v5.0.0/en/model_doc/depth_pro#transformers.DepthProModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Examples:

```python
>>> import torch
>>> from PIL import Image
>>> import httpx
>>> from io import BytesIO
>>> from transformers import AutoProcessor, DepthProModel

>>> url = "https://www.ilankelman.org/stopsigns/australia.jpg"
>>> with httpx.stream("GET", url) as response:
...     image = Image.open(BytesIO(response.read()))

>>> checkpoint = "apple/DepthPro-hf"
>>> processor = AutoProcessor.from_pretrained(checkpoint)
>>> model = DepthProModel.from_pretrained(checkpoint)

>>> # prepare image for the model
>>> inputs = processor(images=image, return_tensors="pt")

>>> with torch.no_grad():
...     output = model(**inputs)

>>> output.last_hidden_state.shape
torch.Size([1, 35, 577, 1024])
```

**Parameters:**

config ([DepthProModel](/docs/transformers/v5.0.0/en/model_doc/depth_pro#transformers.DepthProModel)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``transformers.models.depth_pro.modeling_depth_pro.DepthProOutput` or `tuple(torch.FloatTensor)``

A `transformers.models.depth_pro.modeling_depth_pro.DepthProOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([DepthProConfig](/docs/transformers/v5.0.0/en/model_doc/depth_pro#transformers.DepthProConfig)) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, n_patches_per_batch, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.
- **features** (`Union[torch.FloatTensor, List[torch.FloatTensor]]`, *optional*) -- Features from encoders. Can be a single feature or a list of features.
- **hidden_states** (`tuple[torch.FloatTensor, ...] | None.hidden_states`, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple[torch.FloatTensor, ...] | None.attentions`, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.

## DepthProForDepthEstimation[[transformers.DepthProForDepthEstimation]]

#### transformers.DepthProForDepthEstimation[[transformers.DepthProForDepthEstimation]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/depth_pro/modeling_depth_pro.py#L998)

DepthPro Model with a depth estimation head on top (consisting of 3 convolutional layers).

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.DepthProForDepthEstimation.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/depth_pro/modeling_depth_pro.py#L1023[{"name": "pixel_values", "val": ": FloatTensor"}, {"name": "labels", "val": ": torch.LongTensor | None = None"}, {"name": "output_attentions", "val": ": bool | None = None"}, {"name": "output_hidden_states", "val": ": bool | None = None"}, {"name": "return_dict", "val": ": bool | None = None"}, {"name": "**kwargs", "val": ""}]- **pixel_values** (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [DepthProImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/depth_pro#transformers.DepthProImageProcessorFast). See [DepthProImageProcessorFast.__call__()](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details (`processor_class` uses
  [DepthProImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/depth_pro#transformers.DepthProImageProcessorFast) for processing images).
- **labels** (`torch.LongTensor` of shape `(batch_size, height, width)`, *optional*) --
  Ground truth depth estimation maps for computing the loss.
- **output_attentions** (`bool`, *optional*) --
  Whether or not to return the attentions tensors of all attention layers. See `attentions` under returned
  tensors for more detail.
- **output_hidden_states** (`bool`, *optional*) --
  Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
  more detail.
- **return_dict** (`bool`, *optional*) --
  Whether or not to return a [ModelOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.utils.ModelOutput) instead of a plain tuple.0`transformers.models.depth_pro.modeling_depth_pro.DepthProDepthEstimatorOutput` or `tuple(torch.FloatTensor)`A `transformers.models.depth_pro.modeling_depth_pro.DepthProDepthEstimatorOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([DepthProConfig](/docs/transformers/v5.0.0/en/model_doc/depth_pro#transformers.DepthProConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Classification (or regression if config.num_labels==1) loss.
- **predicted_depth** (`torch.FloatTensor | None.predicted_depth` of shape `(batch_size, height, width)`, defaults to `None`) -- Predicted depth for each pixel.
- **field_of_view** (`torch.FloatTensor` of shape `(batch_size,)`, *optional*, returned when `use_fov_model` is provided) -- Field of View Scaler.
- **hidden_states** (`tuple[torch.FloatTensor, ...] | None.hidden_states`, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple[torch.FloatTensor, ...] | None.attentions`, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
The [DepthProForDepthEstimation](/docs/transformers/v5.0.0/en/model_doc/depth_pro#transformers.DepthProForDepthEstimation) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Examples:

```python
>>> from transformers import AutoImageProcessor, DepthProForDepthEstimation
>>> import torch
>>> from PIL import Image
>>> import httpx
>>> from io import BytesIO

>>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
>>> with httpx.stream("GET", url) as response:
...     image = Image.open(BytesIO(response.read()))

>>> checkpoint = "apple/DepthPro-hf"
>>> processor = AutoImageProcessor.from_pretrained(checkpoint)
>>> model = DepthProForDepthEstimation.from_pretrained(checkpoint)

>>> device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
>>> model.to(device)

>>> # prepare image for the model
>>> inputs = processor(images=image, return_tensors="pt").to(device)

>>> with torch.no_grad():
...     outputs = model(**inputs)

>>> # interpolate to original size
>>> post_processed_output = processor.post_process_depth_estimation(
...     outputs, target_sizes=[(image.height, image.width)],
... )

>>> # get the field of view (fov) predictions
>>> field_of_view = post_processed_output[0]["field_of_view"]
>>> focal_length = post_processed_output[0]["focal_length"]

>>> # visualize the prediction
>>> predicted_depth = post_processed_output[0]["predicted_depth"]
>>> depth = predicted_depth * 255 / predicted_depth.max()
>>> depth = depth.detach().cpu().numpy()
>>> depth = Image.fromarray(depth.astype("uint8"))
```

**Parameters:**

config ([DepthProForDepthEstimation](/docs/transformers/v5.0.0/en/model_doc/depth_pro#transformers.DepthProForDepthEstimation)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

use_fov_model (`bool`, *optional*) : Whether to use the field of view model.

**Returns:**

``transformers.models.depth_pro.modeling_depth_pro.DepthProDepthEstimatorOutput` or `tuple(torch.FloatTensor)``

A `transformers.models.depth_pro.modeling_depth_pro.DepthProDepthEstimatorOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([DepthProConfig](/docs/transformers/v5.0.0/en/model_doc/depth_pro#transformers.DepthProConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Classification (or regression if config.num_labels==1) loss.
- **predicted_depth** (`torch.FloatTensor | None.predicted_depth` of shape `(batch_size, height, width)`, defaults to `None`) -- Predicted depth for each pixel.
- **field_of_view** (`torch.FloatTensor` of shape `(batch_size,)`, *optional*, returned when `use_fov_model` is provided) -- Field of View Scaler.
- **hidden_states** (`tuple[torch.FloatTensor, ...] | None.hidden_states`, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple[torch.FloatTensor, ...] | None.attentions`, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.

