# Source: https://huggingface.co/docs/transformers/v5.0.0/model_doc/superglue.md

# SuperGlue

[SuperGlue](https://huggingface.co/papers/1911.11763) is a neural network that matches two sets of local features by jointly finding correspondences and rejecting non-matchable points. Assignments are estimated by solving a differentiable optimal transport problem, whose costs are predicted by a graph neural network. SuperGlue introduces a flexible context aggregation mechanism based on attention, enabling it to reason about the underlying 3D scene and feature assignments jointly. Paired with the [SuperPoint model](https://huggingface.co/magic-leap-community/superpoint), it can be used to match two images and estimate the pose between them. This model is useful for tasks such as image matching, homography estimation, etc.

You can find all the original SuperGlue checkpoints under the [Magic Leap Community](https://huggingface.co/magic-leap-community) organization.

> [!TIP]
> This model was contributed by [stevenbucaille](https://huggingface.co/stevenbucaille).
>
> Click on the SuperGlue models in the right sidebar for more examples of how to apply SuperGlue to different computer vision tasks.

The example below demonstrates how to match keypoints between two images with [Pipeline](/docs/transformers/v5.0.0/en/main_classes/pipelines#transformers.Pipeline) or the [AutoModel](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoModel) class.

```py
from transformers import pipeline

keypoint_matcher = pipeline(task="keypoint-matching", model="magic-leap-community/superglue_outdoor")

url_0 = "https://raw.githubusercontent.com/magicleap/SuperGluePretrainedNetwork/refs/heads/master/assets/phototourism_sample_images/united_states_capitol_98169888_3347710852.jpg"
url_1 = "https://raw.githubusercontent.com/magicleap/SuperGluePretrainedNetwork/refs/heads/master/assets/phototourism_sample_images/united_states_capitol_26757027_6717084061.jpg"

results = keypoint_matcher([url_0, url_1], threshold=0.9)
print(results[0])
# {'keypoint_image_0': {'x': ..., 'y': ...}, 'keypoint_image_1': {'x': ..., 'y': ...}, 'score': ...}
```

```py
from transformers import AutoImageProcessor, AutoModel
import torch
from PIL import Image
import requests

url_image1 = "https://raw.githubusercontent.com/magicleap/SuperGluePretrainedNetwork/refs/heads/master/assets/phototourism_sample_images/united_states_capitol_98169888_3347710852.jpg"
image1 = Image.open(requests.get(url_image1, stream=True).raw)
url_image2 = "https://raw.githubusercontent.com/magicleap/SuperGluePretrainedNetwork/refs/heads/master/assets/phototourism_sample_images/united_states_capitol_26757027_6717084061.jpg"
image2 = Image.open(requests.get(url_image2, stream=True).raw)

images = [image1, image2]

processor = AutoImageProcessor.from_pretrained("magic-leap-community/superglue_outdoor")
model = AutoModel.from_pretrained("magic-leap-community/superglue_outdoor")

inputs = processor(images, return_tensors="pt")
with torch.inference_mode():
    outputs = model(**inputs)

# Post-process to get keypoints and matches
image_sizes = [[(image.height, image.width) for image in images]]
processed_outputs = processor.post_process_keypoint_matching(outputs, image_sizes, threshold=0.2)
```

## Notes

- SuperGlue performs feature matching between two images simultaneously, requiring pairs of images as input.

    ```python
    from transformers import AutoImageProcessor, AutoModel
    import torch
    from PIL import Image
    import requests

    processor = AutoImageProcessor.from_pretrained("magic-leap-community/superglue_outdoor")
    model = AutoModel.from_pretrained("magic-leap-community/superglue_outdoor")

    # SuperGlue requires pairs of images
    images = [image1, image2]
    inputs = processor(images, return_tensors="pt")
    with torch.inference_mode():
        outputs = model(**inputs)

    # Extract matching information
    keypoints0 = outputs.keypoints0  # Keypoints in first image
    keypoints1 = outputs.keypoints1  # Keypoints in second image
    matches = outputs.matches        # Matching indices
    matching_scores = outputs.matching_scores  # Confidence scores
    ```

- The model outputs matching indices, keypoints, and confidence scores for each match.
- For better visualization and analysis, use the [SuperGlueImageProcessor.post_process_keypoint_matching()](/docs/transformers/v5.0.0/en/model_doc/superglue#transformers.SuperGlueImageProcessor.post_process_keypoint_matching) method to get matches in a more readable format.

    ```py
    # Process outputs for visualization
    image_sizes = [[(image.height, image.width) for image in images]]
    processed_outputs = processor.post_process_keypoint_matching(outputs, image_sizes, threshold=0.2)

    for i, output in enumerate(processed_outputs):
        print(f"For the image pair {i}")
        for keypoint0, keypoint1, matching_score in zip(
                output["keypoints0"], output["keypoints1"], output["matching_scores"]
        ):
            print(f"Keypoint at {keypoint0.numpy()} matches with keypoint at {keypoint1.numpy()} with score {matching_score}")
    ```

- Visualize the matches between the images using the built-in plotting functionality.

    ```py
    # Easy visualization using the built-in plotting method
    processor.visualize_keypoint_matching(images, processed_outputs)
    ```

    

## Resources

- Refer to the [original SuperGlue repository](https://github.com/magicleap/SuperGluePretrainedNetwork) for more examples and implementation details.

## SuperGlueConfig[[transformers.SuperGlueConfig]]

#### transformers.SuperGlueConfig[[transformers.SuperGlueConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/superglue/configuration_superglue.py#L27)

This is the configuration class to store the configuration of a `SuperGlueModel`. It is used to instantiate a
SuperGlue model according to the specified arguments, defining the model architecture. Instantiating a
configuration with the defaults will yield a similar configuration to that of the SuperGlue
[magic-leap-community/superglue_indoor](https://huggingface.co/magic-leap-community/superglue_indoor) architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Examples:
```python
>>> from transformers import SuperGlueConfig, SuperGlueModel

>>> # Initializing a SuperGlue superglue style configuration
>>> configuration = SuperGlueConfig()

>>> # Initializing a model from the superglue style configuration
>>> model = SuperGlueModel(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

keypoint_detector_config (`Union[AutoConfig, dict]`,  *optional*, defaults to `SuperPointConfig`) : The config object or dictionary of the keypoint detector.

hidden_size (`int`, *optional*, defaults to 256) : The dimension of the descriptors.

keypoint_encoder_sizes (`list[int]`, *optional*, defaults to `[32, 64, 128, 256]`) : The sizes of the keypoint encoder layers.

gnn_layers_types (`list[str]`, *optional*, defaults to `['self', 'cross', 'self', 'cross', 'self', 'cross', 'self', 'cross', 'self', 'cross', 'self', 'cross', 'self', 'cross', 'self', 'cross', 'self', 'cross']`) : The types of the GNN layers. Must be either 'self' or 'cross'.

num_attention_heads (`int`, *optional*, defaults to 4) : The number of heads in the GNN layers.

sinkhorn_iterations (`int`, *optional*, defaults to 100) : The number of Sinkhorn iterations.

matching_threshold (`float`, *optional*, defaults to 0.0) : The matching threshold.

initializer_range (`float`, *optional*, defaults to 0.02) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

is_decoder (`bool`, *optional*, defaults to `False`) : Whether to only use the decoder in an encoder-decoder architecture, otherwise it has no effect on decoder-only or encoder-only architectures.

## SuperGlueImageProcessor[[transformers.SuperGlueImageProcessor]]

#### transformers.SuperGlueImageProcessor[[transformers.SuperGlueImageProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/superglue/image_processing_superglue.py#L147)

Constructs a SuperGlue image processor.

preprocesstransformers.SuperGlueImageProcessor.preprocesshttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/superglue/image_processing_superglue.py#L233[{"name": "images", "val": ""}, {"name": "do_resize", "val": ": bool | None = None"}, {"name": "size", "val": ": dict[str, int] | None = None"}, {"name": "resample", "val": ": PIL.Image.Resampling | None = None"}, {"name": "do_rescale", "val": ": bool | None = None"}, {"name": "rescale_factor", "val": ": float | None = None"}, {"name": "do_grayscale", "val": ": bool | None = None"}, {"name": "return_tensors", "val": ": str | transformers.utils.generic.TensorType | None = None"}, {"name": "data_format", "val": ": ChannelDimension = "}, {"name": "input_data_format", "val": ": str | transformers.image_utils.ChannelDimension | None = None"}, {"name": "**kwargs", "val": ""}]- **images** (`ImageInput`) --
  Image pairs to preprocess. Expects either a list of 2 images or a list of list of 2 images list with
  pixel values ranging from 0 to 255. If passing in images with pixel values between 0 and 1, set
  `do_rescale=False`.
- **do_resize** (`bool`, *optional*, defaults to `self.do_resize`) --
  Whether to resize the image.
- **size** (`dict[str, int]`, *optional*, defaults to `self.size`) --
  Size of the output image after `resize` has been applied. If `size["shortest_edge"]` >= 384, the image
  is resized to `(size["shortest_edge"], size["shortest_edge"])`. Otherwise, the smaller edge of the
  image will be matched to `int(size["shortest_edge"]/ crop_pct)`, after which the image is cropped to
  `(size["shortest_edge"], size["shortest_edge"])`. Only has an effect if `do_resize` is set to `True`.
- **resample** (`PILImageResampling`, *optional*, defaults to `self.resample`) --
  Resampling filter to use if resizing the image. This can be one of `PILImageResampling`, filters. Only
  has an effect if `do_resize` is set to `True`.
- **do_rescale** (`bool`, *optional*, defaults to `self.do_rescale`) --
  Whether to rescale the image values between [0 - 1].
- **rescale_factor** (`float`, *optional*, defaults to `self.rescale_factor`) --
  Rescale factor to rescale the image by if `do_rescale` is set to `True`.
- **do_grayscale** (`bool`, *optional*, defaults to `self.do_grayscale`) --
  Whether to convert the image to grayscale.
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

do_resize (`bool`, *optional*, defaults to `True`) : Controls whether to resize the image's (height, width) dimensions to the specified `size`. Can be overridden by `do_resize` in the `preprocess` method.

size (`dict[str, int]` *optional*, defaults to `{"height" : 480, "width": 640}`): Resolution of the output image after `resize` is applied. Only has an effect if `do_resize` is set to `True`. Can be overridden by `size` in the `preprocess` method.

resample (`PILImageResampling`, *optional*, defaults to `Resampling.BILINEAR`) : Resampling filter to use if resizing the image. Can be overridden by `resample` in the `preprocess` method.

do_rescale (`bool`, *optional*, defaults to `True`) : Whether to rescale the image by the specified scale `rescale_factor`. Can be overridden by `do_rescale` in the `preprocess` method.

rescale_factor (`int` or `float`, *optional*, defaults to `1/255`) : Scale factor to use if rescaling the image. Can be overridden by `rescale_factor` in the `preprocess` method.

do_grayscale (`bool`, *optional*, defaults to `True`) : Whether to convert the image to grayscale. Can be overridden by `do_grayscale` in the `preprocess` method.
#### post_process_keypoint_matching[[transformers.SuperGlueImageProcessor.post_process_keypoint_matching]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/superglue/image_processing_superglue.py#L346)

Converts the raw output of `SuperGlueKeypointMatchingOutput` into lists of keypoints, scores and descriptors
with coordinates absolute to the original image sizes.

**Parameters:**

outputs (`SuperGlueKeypointMatchingOutput`) : Raw outputs of the model.

target_sizes (`torch.Tensor` or `list[tuple[tuple[int, int]]]`, *optional*) : Tensor of shape `(batch_size, 2, 2)` or list of tuples of tuples (`tuple[int, int]`) containing the target size `(height, width)` of each image in the batch. This must be the original image size (before any processing).

threshold (`float`, *optional*, defaults to 0.0) : Threshold to filter out the matches with low scores.

**Returns:**

``list[Dict]``

A list of dictionaries, each dictionary containing the keypoints in the first and second image
of the pair, the matching scores and the matching indices.
#### visualize_keypoint_matching[[transformers.SuperGlueImageProcessor.visualize_keypoint_matching]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/superglue/image_processing_superglue.py#L415)

Plots the image pairs side by side with the detected keypoints as well as the matching between them.

**Parameters:**

images (`ImageInput`) : Image pairs to plot. Same as `SuperGlueImageProcessor.preprocess`. Expects either a list of 2 images or a list of list of 2 images list with pixel values ranging from 0 to 255.

keypoint_matching_output (List[Dict[str, torch.Tensor]]]) : A post processed keypoint matching output

**Returns:**

``List[PIL.Image.Image]``

A list of PIL images, each containing the image pairs side by side with the detected
keypoints as well as the matching between them.

## SuperGlueImageProcessorFast[[transformers.SuperGlueImageProcessorFast]]

#### transformers.SuperGlueImageProcessorFast[[transformers.SuperGlueImageProcessorFast]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/superglue/image_processing_superglue_fast.py#L98)

Constructs a fast Superglue image processor.

preprocesstransformers.SuperGlueImageProcessorFast.preprocesshttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/superglue/image_processing_superglue_fast.py#L111[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor']]"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.models.superglue.image_processing_superglue.SuperGlueImageProcessorKwargs]"}]- **images** (`Union[PIL.Image.Image, numpy.ndarray, torch.Tensor, list, list, list]`) --
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
- **do_grayscale** (`bool`, *optional*, defaults to `True`) --
  Whether to convert the image to grayscale. Can be overridden by `do_grayscale` in the `preprocess` method.0``- **data** (`dict`) -- Dictionary of lists/arrays/tensors returned by the __call__ method ('pixel_values', etc.).
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

do_grayscale (`bool`, *optional*, defaults to `True`) : Whether to convert the image to grayscale. Can be overridden by `do_grayscale` in the `preprocess` method.

**Returns:**

````

- **data** (`dict`) -- Dictionary of lists/arrays/tensors returned by the __call__ method ('pixel_values', etc.).
- **tensor_type** (`Union[None, str, TensorType]`, *optional*) -- You can give a tensor_type here to convert the lists of integers in PyTorch/Numpy Tensors at
  initialization.
#### post_process_keypoint_matching[[transformers.SuperGlueImageProcessorFast.post_process_keypoint_matching]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/superglue/image_processing_superglue_fast.py#L167)

Converts the raw output of `SuperGlueKeypointMatchingOutput` into lists of keypoints, scores and descriptors
with coordinates absolute to the original image sizes.

**Parameters:**

outputs (`SuperGlueKeypointMatchingOutput`) : Raw outputs of the model.

target_sizes (`torch.Tensor` or `list[tuple[tuple[int, int]]]`, *optional*) : Tensor of shape `(batch_size, 2, 2)` or list of tuples of tuples (`tuple[int, int]`) containing the target size `(height, width)` of each image in the batch. This must be the original image size (before any processing).

threshold (`float`, *optional*, defaults to 0.0) : Threshold to filter out the matches with low scores.

**Returns:**

``list[Dict]``

A list of dictionaries, each dictionary containing the keypoints in the first and second image
of the pair, the matching scores and the matching indices.
#### visualize_keypoint_matching[[transformers.SuperGlueImageProcessorFast.visualize_keypoint_matching]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/superglue/image_processing_superglue_fast.py#L235)

Plots the image pairs side by side with the detected keypoints as well as the matching between them.

**Parameters:**

images : Image pairs to plot. Same as `EfficientLoFTRImageProcessor.preprocess`. Expects either a list of 2 images or a list of list of 2 images list with pixel values ranging from 0 to 255.

keypoint_matching_output (List[Dict[str, torch.Tensor]]]) : A post processed keypoint matching output

**Returns:**

``List[PIL.Image.Image]``

A list of PIL images, each containing the image pairs side by side with the detected
keypoints as well as the matching between them.

## SuperGlueForKeypointMatching[[transformers.SuperGlueForKeypointMatching]]

#### transformers.SuperGlueForKeypointMatching[[transformers.SuperGlueForKeypointMatching]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/superglue/modeling_superglue.py#L485)

SuperGlue model taking images as inputs and outputting the matching of them.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.SuperGlueForKeypointMatching.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/superglue/modeling_superglue.py#L664[{"name": "pixel_values", "val": ": FloatTensor"}, {"name": "labels", "val": ": torch.LongTensor | None = None"}, {"name": "output_attentions", "val": ": bool | None = None"}, {"name": "output_hidden_states", "val": ": bool | None = None"}, {"name": "return_dict", "val": ": bool | None = None"}, {"name": "**kwargs", "val": ""}]- **pixel_values** (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [SuperGlueImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/superglue#transformers.SuperGlueImageProcessorFast). See [SuperGlueImageProcessorFast.__call__()](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details (`processor_class` uses
  [SuperGlueImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/superglue#transformers.SuperGlueImageProcessorFast) for processing images).
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
  Whether or not to return a [ModelOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.utils.ModelOutput) instead of a plain tuple.0`transformers.models.superglue.modeling_superglue.SuperGlueKeypointMatchingOutput` or `tuple(torch.FloatTensor)`A `transformers.models.superglue.modeling_superglue.SuperGlueKeypointMatchingOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([SuperGlueConfig](/docs/transformers/v5.0.0/en/model_doc/superglue#transformers.SuperGlueConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*) -- Loss computed during training.
- **matches** (`torch.FloatTensor` of shape `(batch_size, 2, num_matches)`) -- Index of keypoint matched in the other image.
- **matching_scores** (`torch.FloatTensor` of shape `(batch_size, 2, num_matches)`) -- Scores of predicted matches.
- **keypoints** (`torch.FloatTensor` of shape `(batch_size, num_keypoints, 2)`) -- Absolute (x, y) coordinates of predicted keypoints in a given image.
- **mask** (`torch.IntTensor` of shape `(batch_size, num_keypoints)`) -- Mask indicating which values in matches and matching_scores are keypoint matching information.
- **hidden_states** (`tuple[torch.FloatTensor, ...]`, *optional*) -- Tuple of `torch.FloatTensor` (one for the output of each stage) of shape `(batch_size, 2, num_channels,
  num_keypoints)`, returned when `output_hidden_states=True` is passed or when
  `config.output_hidden_states=True`)
- **attentions** (`tuple[torch.FloatTensor, ...]`, *optional*) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, 2, num_heads, num_keypoints,
  num_keypoints)`, returned when `output_attentions=True` is passed or when `config.output_attentions=True`)
The [SuperGlueForKeypointMatching](/docs/transformers/v5.0.0/en/model_doc/superglue#transformers.SuperGlueForKeypointMatching) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Examples:

```python
>>> from transformers import AutoImageProcessor, AutoModel
>>> import torch
>>> from PIL import Image
>>> import httpx
>>> from io import BytesIO

>>> url = "https://github.com/magicleap/SuperGluePretrainedNetwork/blob/master/assets/phototourism_sample_images/london_bridge_78916675_4568141288.jpg?raw=true"
>>> with httpx.stream("GET", url) as response:
...     image_1 = Image.open(BytesIO(response.read()))

>>> url = "https://github.com/magicleap/SuperGluePretrainedNetwork/blob/master/assets/phototourism_sample_images/london_bridge_19481797_2295892421.jpg?raw=true"
>>> with httpx.stream("GET", url) as response:
...     image_2 = Image.open(BytesIO(response.read()))

>>> images = [image_1, image_2]

>>> processor = AutoImageProcessor.from_pretrained("magic-leap-community/superglue_outdoor")
>>> model = AutoModel.from_pretrained("magic-leap-community/superglue_outdoor")

>>> with torch.no_grad():
>>>     inputs = processor(images, return_tensors="pt")
>>>     outputs = model(**inputs)
```

**Parameters:**

config ([SuperGlueConfig](/docs/transformers/v5.0.0/en/model_doc/superglue#transformers.SuperGlueConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``transformers.models.superglue.modeling_superglue.SuperGlueKeypointMatchingOutput` or `tuple(torch.FloatTensor)``

A `transformers.models.superglue.modeling_superglue.SuperGlueKeypointMatchingOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([SuperGlueConfig](/docs/transformers/v5.0.0/en/model_doc/superglue#transformers.SuperGlueConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*) -- Loss computed during training.
- **matches** (`torch.FloatTensor` of shape `(batch_size, 2, num_matches)`) -- Index of keypoint matched in the other image.
- **matching_scores** (`torch.FloatTensor` of shape `(batch_size, 2, num_matches)`) -- Scores of predicted matches.
- **keypoints** (`torch.FloatTensor` of shape `(batch_size, num_keypoints, 2)`) -- Absolute (x, y) coordinates of predicted keypoints in a given image.
- **mask** (`torch.IntTensor` of shape `(batch_size, num_keypoints)`) -- Mask indicating which values in matches and matching_scores are keypoint matching information.
- **hidden_states** (`tuple[torch.FloatTensor, ...]`, *optional*) -- Tuple of `torch.FloatTensor` (one for the output of each stage) of shape `(batch_size, 2, num_channels,
  num_keypoints)`, returned when `output_hidden_states=True` is passed or when
  `config.output_hidden_states=True`)
- **attentions** (`tuple[torch.FloatTensor, ...]`, *optional*) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, 2, num_heads, num_keypoints,
  num_keypoints)`, returned when `output_attentions=True` is passed or when `config.output_attentions=True`)

