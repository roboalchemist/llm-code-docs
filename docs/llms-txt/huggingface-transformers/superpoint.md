# Source: https://huggingface.co/docs/transformers/v5.0.0/model_doc/superpoint.md

# SuperPoint

[SuperPoint](https://huggingface.co/papers/1712.07629) is the result of self-supervised training of a fully-convolutional network for interest point detection and description. The model is able to detect interest points that are repeatable under homographic transformations and provide a descriptor for each point. Usage on it's own is limited, but it can be used as a feature extractor for other tasks such as homography estimation and image matching.

You can find all the original SuperPoint checkpoints under the [Magic Leap Community](https://huggingface.co/magic-leap-community) organization.

> [!TIP]
> This model was contributed by [stevenbucaille](https://huggingface.co/stevenbucaille).
>
> Click on the SuperPoint models in the right sidebar for more examples of how to apply SuperPoint to different computer vision tasks.

The example below demonstrates how to detect interest points in an image with the [AutoModel](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoModel) class.

```py
from transformers import AutoImageProcessor, SuperPointForKeypointDetection
import torch
from PIL import Image
import requests

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)

processor = AutoImageProcessor.from_pretrained("magic-leap-community/superpoint")
model = SuperPointForKeypointDetection.from_pretrained("magic-leap-community/superpoint")

inputs = processor(image, return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)

# Post-process to get keypoints, scores, and descriptors
image_size = (image.height, image.width)
processed_outputs = processor.post_process_keypoint_detection(outputs, [image_size])
```

## Notes

- SuperPoint outputs a dynamic number of keypoints per image, which makes it suitable for tasks requiring variable-length feature representations.

    ```py
    from transformers import AutoImageProcessor, SuperPointForKeypointDetection
    import torch
    from PIL import Image
    import requests
    processor = AutoImageProcessor.from_pretrained("magic-leap-community/superpoint")
    model = SuperPointForKeypointDetection.from_pretrained("magic-leap-community/superpoint")
    url_image_1 = "http://images.cocodataset.org/val2017/000000039769.jpg"
    image_1 = Image.open(requests.get(url_image_1, stream=True).raw)
    url_image_2 = "http://images.cocodataset.org/test-stuff2017/000000000568.jpg"
    image_2 = Image.open(requests.get(url_image_2, stream=True).raw)
    images = [image_1, image_2]
    inputs = processor(images, return_tensors="pt")
    # Example of handling dynamic keypoint output
    outputs = model(**inputs)
    keypoints = outputs.keypoints  # Shape varies per image
    scores = outputs.scores        # Confidence scores for each keypoint
    descriptors = outputs.descriptors  # 256-dimensional descriptors
    mask = outputs.mask # Value of 1 corresponds to a keypoint detection
    ```

- The model provides both keypoint coordinates and their corresponding descriptors (256-dimensional vectors) in a single forward pass.
- For batch processing with multiple images, you need to use the mask attribute to retrieve the respective information for each image. You can use the `post_process_keypoint_detection` from the `SuperPointImageProcessor` to retrieve the each image information.

    ```py
    # Batch processing example
    images = [image1, image2, image3]
    inputs = processor(images, return_tensors="pt")
    outputs = model(**inputs)
    image_sizes = [(img.height, img.width) for img in images]
    processed_outputs = processor.post_process_keypoint_detection(outputs, image_sizes)
    ```

- You can then print the keypoints on the image of your choice to visualize the result:

    ```py
    import matplotlib.pyplot as plt
    plt.axis("off")
    plt.imshow(image_1)
    plt.scatter(
        outputs[0]["keypoints"][:, 0],
        outputs[0]["keypoints"][:, 1],
        c=outputs[0]["scores"] * 100,
        s=outputs[0]["scores"] * 50,
        alpha=0.8
    )
    plt.savefig(f"output_image.png")
    ```

    

## Resources

- Refer to this [notebook](https://github.com/NielsRogge/Transformers-Tutorials/blob/master/SuperPoint/Inference_with_SuperPoint_to_detect_interest_points_in_an_image.ipynb) for an inference and visualization example.

## SuperPointConfig[[transformers.SuperPointConfig]]

#### transformers.SuperPointConfig[[transformers.SuperPointConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/superpoint/configuration_superpoint.py#L22)

This is the configuration class to store the configuration of a [SuperPointForKeypointDetection](/docs/transformers/v5.0.0/en/model_doc/superpoint#transformers.SuperPointForKeypointDetection). It is used to instantiate a
SuperPoint model according to the specified arguments, defining the model architecture. Instantiating a
configuration with the defaults will yield a similar configuration to that of the SuperPoint
[magic-leap-community/superpoint](https://huggingface.co/magic-leap-community/superpoint) architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:
```python
>>> from transformers import SuperPointConfig, SuperPointForKeypointDetection

>>> # Initializing a SuperPoint superpoint style configuration
>>> configuration = SuperPointConfig()
>>> # Initializing a model from the superpoint style configuration
>>> model = SuperPointForKeypointDetection(configuration)
>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

encoder_hidden_sizes (`List`, *optional*, defaults to `[64, 64, 128, 128]`) : The number of channels in each convolutional layer in the encoder.

decoder_hidden_size (`int`, *optional*, defaults to 256) : The hidden size of the decoder.

keypoint_decoder_dim (`int`, *optional*, defaults to 65) : The output dimension of the keypoint decoder.

descriptor_decoder_dim (`int`, *optional*, defaults to 256) : The output dimension of the descriptor decoder.

keypoint_threshold (`float`, *optional*, defaults to 0.005) : The threshold to use for extracting keypoints.

max_keypoints (`int`, *optional*, defaults to -1) : The maximum number of keypoints to extract. If `-1`, will extract all keypoints.

nms_radius (`int`, *optional*, defaults to 4) : The radius for non-maximum suppression.

border_removal_distance (`int`, *optional*, defaults to 4) : The distance from the border to remove keypoints.

initializer_range (`float`, *optional*, defaults to 0.02) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

## SuperPointImageProcessor[[transformers.SuperPointImageProcessor]]

#### transformers.SuperPointImageProcessor[[transformers.SuperPointImageProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/superpoint/image_processing_superpoint.py#L109)

Constructs a SuperPoint image processor.

preprocesstransformers.SuperPointImageProcessor.preprocesshttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/superpoint/image_processing_superpoint.py#L195[{"name": "images", "val": ""}, {"name": "do_resize", "val": ": bool | None = None"}, {"name": "size", "val": ": dict[str, int] | None = None"}, {"name": "resample", "val": ": PIL.Image.Resampling | None = None"}, {"name": "do_rescale", "val": ": bool | None = None"}, {"name": "rescale_factor", "val": ": float | None = None"}, {"name": "do_grayscale", "val": ": bool | None = None"}, {"name": "return_tensors", "val": ": str | transformers.utils.generic.TensorType | None = None"}, {"name": "data_format", "val": ": ChannelDimension = "}, {"name": "input_data_format", "val": ": str | transformers.image_utils.ChannelDimension | None = None"}, {"name": "**kwargs", "val": ""}]- **images** (`ImageInput`) --
  Image to preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If
  passing in images with pixel values between 0 and 1, set `do_rescale=False`.
- **do_resize** (`bool`, *optional*, defaults to `self.do_resize`) --
  Whether to resize the image.
- **size** (`dict[str, int]`, *optional*, defaults to `self.size`) --
  Size of the output image after `resize` has been applied. If `size["shortest_edge"]` >= 384, the image
  is resized to `(size["shortest_edge"], size["shortest_edge"])`. Otherwise, the smaller edge of the
  image will be matched to `int(size["shortest_edge"]/ crop_pct)`, after which the image is cropped to
  `(size["shortest_edge"], size["shortest_edge"])`. Only has an effect if `do_resize` is set to `True`.
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

resample (`Resampling`, *optional*, defaults to `2`) : Resampling filter to use if resizing the image. Can be overridden by `resample` in the `preprocess` method.

do_rescale (`bool`, *optional*, defaults to `True`) : Whether to rescale the image by the specified scale `rescale_factor`. Can be overridden by `do_rescale` in the `preprocess` method.

rescale_factor (`int` or `float`, *optional*, defaults to `1/255`) : Scale factor to use if rescaling the image. Can be overridden by `rescale_factor` in the `preprocess` method.

do_grayscale (`bool`, *optional*, defaults to `False`) : Whether to convert the image to grayscale. Can be overridden by `do_grayscale` in the `preprocess` method.

## SuperPointImageProcessorFast[[transformers.SuperPointImageProcessorFast]]

#### transformers.SuperPointImageProcessorFast[[transformers.SuperPointImageProcessorFast]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/superpoint/image_processing_superpoint_fast.py#L74)

Constructs a fast Superpoint image processor.

preprocesstransformers.SuperPointImageProcessorFast.preprocesshttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/image_processing_utils_fast.py#L838[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor']]"}, {"name": "*args", "val": ""}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.processing_utils.ImagesKwargs]"}]- **images** (`Union[PIL.Image.Image, numpy.ndarray, torch.Tensor, list, list, list]`) --
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
#### post_process_keypoint_detection[[transformers.SuperPointImageProcessorFast.post_process_keypoint_detection]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/superpoint/image_processing_superpoint_fast.py#L113)

Converts the raw output of [SuperPointForKeypointDetection](/docs/transformers/v5.0.0/en/model_doc/superpoint#transformers.SuperPointForKeypointDetection) into lists of keypoints, scores and descriptors
with coordinates absolute to the original image sizes.

**Parameters:**

outputs (`SuperPointKeypointDescriptionOutput`) : Raw outputs of the model containing keypoints in a relative (x, y) format, with scores and descriptors.

target_sizes (`torch.Tensor` or `List[Tuple[int, int]]`) : Tensor of shape `(batch_size, 2)` or list of tuples (`Tuple[int, int]`) containing the target size `(height, width)` of each image in the batch. This must be the original image size (before any processing).

**Returns:**

``List[Dict]``

A list of dictionaries, each dictionary containing the keypoints in absolute format according
to target_sizes, scores and descriptors for an image in the batch as predicted by the model.

## SuperPointForKeypointDetection[[transformers.SuperPointForKeypointDetection]]

#### transformers.SuperPointForKeypointDetection[[transformers.SuperPointForKeypointDetection]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/superpoint/modeling_superpoint.py#L352)

SuperPoint model outputting keypoints and descriptors.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.SuperPointForKeypointDetection.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/superpoint/modeling_superpoint.py#L373[{"name": "pixel_values", "val": ": FloatTensor"}, {"name": "labels", "val": ": torch.LongTensor | None = None"}, {"name": "output_hidden_states", "val": ": bool | None = None"}, {"name": "return_dict", "val": ": bool | None = None"}, {"name": "**kwargs", "val": ""}]- **pixel_values** (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [SuperPointImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/superpoint#transformers.SuperPointImageProcessorFast). See [SuperPointImageProcessorFast.__call__()](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details (`processor_class` uses
  [SuperPointImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/superpoint#transformers.SuperPointImageProcessorFast) for processing images).
- **labels** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Labels for computing the masked language modeling loss. Indices should either be in `[0, ...,
  config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored
  (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.
- **output_hidden_states** (`bool`, *optional*) --
  Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
  more detail.
- **return_dict** (`bool`, *optional*) --
  Whether or not to return a [ModelOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.utils.ModelOutput) instead of a plain tuple.0`transformers.models.superpoint.modeling_superpoint.SuperPointKeypointDescriptionOutput` or `tuple(torch.FloatTensor)`A `transformers.models.superpoint.modeling_superpoint.SuperPointKeypointDescriptionOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([SuperPointConfig](/docs/transformers/v5.0.0/en/model_doc/superpoint#transformers.SuperPointConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*) -- Loss computed during training.
- **keypoints** (`torch.FloatTensor` of shape `(batch_size, num_keypoints, 2)`) -- Relative (x, y) coordinates of predicted keypoints in a given image.
- **scores** (`torch.FloatTensor` of shape `(batch_size, num_keypoints)`) -- Scores of predicted keypoints.
- **descriptors** (`torch.FloatTensor` of shape `(batch_size, num_keypoints, descriptor_size)`) -- Descriptors of predicted keypoints.
- **mask** (`torch.BoolTensor` of shape `(batch_size, num_keypoints)`) -- Mask indicating which values in keypoints, scores and descriptors are keypoint information.
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or
- **when** `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each stage) of shape `(batch_size, sequence_length, hidden_size)`. Hidden-states
  (also called feature maps) of the model at the output of each stage.
The [SuperPointForKeypointDetection](/docs/transformers/v5.0.0/en/model_doc/superpoint#transformers.SuperPointForKeypointDetection) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Examples:

```python
>>> from transformers import AutoImageProcessor, SuperPointForKeypointDetection
>>> import torch
>>> from PIL import Image
>>> import httpx
>>> from io import BytesIO

>>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
>>> with httpx.stream("GET", url) as response:
...     image = Image.open(BytesIO(response.read()))

>>> processor = AutoImageProcessor.from_pretrained("magic-leap-community/superpoint")
>>> model = SuperPointForKeypointDetection.from_pretrained("magic-leap-community/superpoint")

>>> inputs = processor(image, return_tensors="pt")
>>> outputs = model(**inputs)
```

**Parameters:**

config ([SuperPointConfig](/docs/transformers/v5.0.0/en/model_doc/superpoint#transformers.SuperPointConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``transformers.models.superpoint.modeling_superpoint.SuperPointKeypointDescriptionOutput` or `tuple(torch.FloatTensor)``

A `transformers.models.superpoint.modeling_superpoint.SuperPointKeypointDescriptionOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([SuperPointConfig](/docs/transformers/v5.0.0/en/model_doc/superpoint#transformers.SuperPointConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*) -- Loss computed during training.
- **keypoints** (`torch.FloatTensor` of shape `(batch_size, num_keypoints, 2)`) -- Relative (x, y) coordinates of predicted keypoints in a given image.
- **scores** (`torch.FloatTensor` of shape `(batch_size, num_keypoints)`) -- Scores of predicted keypoints.
- **descriptors** (`torch.FloatTensor` of shape `(batch_size, num_keypoints, descriptor_size)`) -- Descriptors of predicted keypoints.
- **mask** (`torch.BoolTensor` of shape `(batch_size, num_keypoints)`) -- Mask indicating which values in keypoints, scores and descriptors are keypoint information.
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or
- **when** `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each stage) of shape `(batch_size, sequence_length, hidden_size)`. Hidden-states
  (also called feature maps) of the model at the output of each stage.

