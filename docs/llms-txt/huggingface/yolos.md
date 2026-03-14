# Source: https://huggingface.co/docs/transformers/v5.3.0/model_doc/yolos.md

# YOLOS

[YOLOS](https://huggingface.co/papers/2106.00666) uses a [Vision Transformer (ViT)](./vit) for object detection with minimal modifications and region priors. It can achieve performance comparable to specialized object detection models and frameworks with knowledge about 2D spatial structures.

You can find all the original YOLOS checkpoints under the [HUST Vision Lab](https://huggingface.co/hustvl/models?search=yolos) organization.

 YOLOS architecture. Taken from the original paper.

> [!TIP]
> This model wasa contributed by [nielsr](https://huggingface.co/nielsr).
> Click on the YOLOS models in the right sidebar for more examples of how to apply YOLOS to different object detection tasks.

The example below demonstrates how to detect objects with [Pipeline](/docs/transformers/v5.3.0/en/main_classes/pipelines#transformers.Pipeline) or the [AutoModel](/docs/transformers/v5.3.0/en/model_doc/auto#transformers.AutoModel) class.

```py
import torch
from transformers import pipeline

detector = pipeline(
    task="object-detection",
    model="hustvl/yolos-base",
    dtype=torch.float16,
    device=0
)
detector("https://huggingface.co/datasets/Narsil/image_dummy/raw/main/parrots.png")
```

```py
import torch
from PIL import Image
import requests
from transformers import AutoImageProcessor, AutoModelForObjectDetection
from accelerate import Accelerator

device = Accelerator().device

processor = AutoImageProcessor.from_pretrained("hustvl/yolos-base")
model = AutoModelForObjectDetection.from_pretrained("hustvl/yolos-base", dtype=torch.float16, attn_implementation="sdpa").to(device)

url = "https://huggingface.co/datasets/Narsil/image_dummy/raw/main/parrots.png"
image = Image.open(requests.get(url, stream=True).raw).convert("RGB")
inputs = processor(images=image, return_tensors="pt").to(model.device)

with torch.no_grad():
    outputs = model(**inputs)
logits = outputs.logits.softmax(-1)
scores, labels = logits[..., :-1].max(-1)
boxes = outputs.pred_boxes

threshold = 0.3
keep = scores[0] > threshold

filtered_scores = scores[0][keep]
filtered_labels = labels[0][keep]
filtered_boxes  = boxes[0][keep]

width, height = image.size
pixel_boxes = filtered_boxes * torch.tensor([width, height, width, height], device=boxes.device)

for score, label, box in zip(filtered_scores, filtered_labels, pixel_boxes):
    x0, y0, x1, y1 = box.tolist()
    print(f"Label {model.config.id2label[label.item()]}: {score:.2f} at [{x0:.0f}, {y0:.0f}, {x1:.0f}, {y1:.0f}]")
```

## Notes

- Use [YolosImageProcessor](/docs/transformers/v5.3.0/en/model_doc/yolos#transformers.YolosImageProcessor) for preparing images (and optional targets) for the model. Contrary to [DETR](./detr), YOLOS doesn't require a `pixel_mask`.

## Resources

- Refer to these [notebooks](https://github.com/NielsRogge/Transformers-Tutorials/tree/master/YOLOS) for inference and fine-tuning with [YolosForObjectDetection](/docs/transformers/v5.3.0/en/model_doc/yolos#transformers.YolosForObjectDetection) on a custom dataset.

## YolosConfig[[transformers.YolosConfig]]

#### transformers.YolosConfig[[transformers.YolosConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/yolos/configuration_yolos.py#L23)

This is the configuration class to store the configuration of a [YolosModel](/docs/transformers/v5.3.0/en/model_doc/yolos#transformers.YolosModel). It is used to instantiate a YOLOS
model according to the specified arguments, defining the model architecture. Instantiating a configuration with the
defaults will yield a similar configuration to that of the YOLOS
[hustvl/yolos-base](https://huggingface.co/hustvl/yolos-base) architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.3.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.3.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:

```python
>>> from transformers import YolosConfig, YolosModel

>>> # Initializing a YOLOS hustvl/yolos-base style configuration
>>> configuration = YolosConfig()

>>> # Initializing a model (with random weights) from the hustvl/yolos-base style configuration
>>> model = YolosModel(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

hidden_size (`int`, *optional*, defaults to 768) : Dimensionality of the encoder layers and the pooler layer.

num_hidden_layers (`int`, *optional*, defaults to 12) : Number of hidden layers in the Transformer encoder.

num_attention_heads (`int`, *optional*, defaults to 12) : Number of attention heads for each attention layer in the Transformer encoder.

intermediate_size (`int`, *optional*, defaults to 3072) : Dimensionality of the "intermediate" (i.e., feed-forward) layer in the Transformer encoder.

hidden_act (`str` or `function`, *optional*, defaults to `"gelu"`) : The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`, `"relu"`, `"selu"` and `"gelu_new"` are supported.

hidden_dropout_prob (`float`, *optional*, defaults to 0.0) : The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.

attention_probs_dropout_prob (`float`, *optional*, defaults to 0.0) : The dropout ratio for the attention probabilities.

initializer_range (`float`, *optional*, defaults to 0.02) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

layer_norm_eps (`float`, *optional*, defaults to 1e-12) : The epsilon used by the layer normalization layers.

image_size (`list[int]`, *optional*, defaults to `[512, 864]`) : The size (resolution) of each image.

patch_size (`int`, *optional*, defaults to 16) : The size (resolution) of each patch.

num_channels (`int`, *optional*, defaults to 3) : The number of input channels.

qkv_bias (`bool`, *optional*, defaults to `True`) : Whether to add a bias to the queries, keys and values.

num_detection_tokens (`int`, *optional*, defaults to 100) : The number of detection tokens.

use_mid_position_embeddings (`bool`, *optional*, defaults to `True`) : Whether to use the mid-layer position encodings.

auxiliary_loss (`bool`, *optional*, defaults to `False`) : Whether auxiliary decoding losses (loss at each decoder layer) are to be used.

class_cost (`float`, *optional*, defaults to 1) : Relative weight of the classification error in the Hungarian matching cost.

bbox_cost (`float`, *optional*, defaults to 5) : Relative weight of the L1 error of the bounding box coordinates in the Hungarian matching cost.

giou_cost (`float`, *optional*, defaults to 2) : Relative weight of the generalized IoU loss of the bounding box in the Hungarian matching cost.

bbox_loss_coefficient (`float`, *optional*, defaults to 5) : Relative weight of the L1 bounding box loss in the object detection loss.

giou_loss_coefficient (`float`, *optional*, defaults to 2) : Relative weight of the generalized IoU loss in the object detection loss.

eos_coefficient (`float`, *optional*, defaults to 0.1) : Relative classification weight of the 'no-object' class in the object detection loss.

## YolosImageProcessor[[transformers.YolosImageProcessor]]

#### transformers.YolosImageProcessor[[transformers.YolosImageProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/yolos/image_processing_yolos.py#L719)

Constructs a Detr image processor.

preprocesstransformers.YolosImageProcessor.preprocesshttps://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/yolos/image_processing_yolos.py#L1137[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor']]"}, {"name": "annotations", "val": ": dict[str, int | str | list[dict]] | list[dict[str, int | str | list[dict]]] | None = None"}, {"name": "return_segmentation_masks", "val": ": bool | None = None"}, {"name": "masks_path", "val": ": str | pathlib.Path | None = None"}, {"name": "do_resize", "val": ": bool | None = None"}, {"name": "size", "val": ": dict[str, int] | None = None"}, {"name": "resample", "val": " = None"}, {"name": "do_rescale", "val": ": bool | None = None"}, {"name": "rescale_factor", "val": ": int | float | None = None"}, {"name": "do_normalize", "val": ": bool | None = None"}, {"name": "image_mean", "val": ": float | list[float] | None = None"}, {"name": "image_std", "val": ": float | list[float] | None = None"}, {"name": "do_convert_annotations", "val": ": bool | None = None"}, {"name": "do_pad", "val": ": bool | None = None"}, {"name": "format", "val": ": str | transformers.image_utils.AnnotationFormat | None = None"}, {"name": "return_tensors", "val": ": transformers.utils.generic.TensorType | str | None = None"}, {"name": "data_format", "val": ": str | transformers.image_utils.ChannelDimension = "}, {"name": "input_data_format", "val": ": str | transformers.image_utils.ChannelDimension | None = None"}, {"name": "pad_size", "val": ": dict[str, int] | None = None"}, {"name": "**kwargs", "val": ""}]- **images** (`ImageInput`) --
  Image or batch of images to preprocess. Expects a single or batch of images with pixel values ranging
  from 0 to 255. If passing in images with pixel values between 0 and 1, set `do_rescale=False`.
- **annotations** (`AnnotationType` or `list[AnnotationType]`, *optional*) --
  List of annotations associated with the image or batch of images. If annotation is for object
  detection, the annotations should be a dictionary with the following keys:
  - "image_id" (`int`): The image id.
  - "annotations" (`list[Dict]`): List of annotations for an image. Each annotation should be a
    dictionary. An image can have no annotations, in which case the list should be empty.
  If annotation is for segmentation, the annotations should be a dictionary with the following keys:
  - "image_id" (`int`): The image id.
  - "segments_info" (`list[Dict]`): List of segments for an image. Each segment should be a dictionary.
    An image can have no segments, in which case the list should be empty.
  - "file_name" (`str`): The file name of the image.
- **return_segmentation_masks** (`bool`, *optional*, defaults to self.return_segmentation_masks) --
  Whether to return segmentation masks.
- **masks_path** (`str` or `pathlib.Path`, *optional*) --
  Path to the directory containing the segmentation masks.
- **do_resize** (`bool`, *optional*, defaults to self.do_resize) --
  Whether to resize the image.
- **size** (`dict[str, int]`, *optional*, defaults to self.size) --
  Size of the image's `(height, width)` dimensions after resizing. Available options are:
  - `{"height": int, "width": int}`: The image will be resized to the exact size `(height, width)`.
    Do NOT keep the aspect ratio.
  - `{"shortest_edge": int, "longest_edge": int}`: The image will be resized to a maximum size respecting
    the aspect ratio and keeping the shortest edge less or equal to `shortest_edge` and the longest edge
    less or equal to `longest_edge`.
  - `{"max_height": int, "max_width": int}`: The image will be resized to the maximum size respecting the
    aspect ratio and keeping the height less or equal to `max_height` and the width less or equal to
    `max_width`.
- **resample** (`PILImageResampling`, *optional*, defaults to self.resample) --
  Resampling filter to use when resizing the image.
- **do_rescale** (`bool`, *optional*, defaults to self.do_rescale) --
  Whether to rescale the image.
- **rescale_factor** (`float`, *optional*, defaults to self.rescale_factor) --
  Rescale factor to use when rescaling the image.
- **do_normalize** (`bool`, *optional*, defaults to self.do_normalize) --
  Whether to normalize the image.
- **image_mean** (`float` or `list[float]`, *optional*, defaults to self.image_mean) --
  Mean to use when normalizing the image.
- **image_std** (`float` or `list[float]`, *optional*, defaults to self.image_std) --
  Standard deviation to use when normalizing the image.
- **do_convert_annotations** (`bool`, *optional*, defaults to self.do_convert_annotations) --
  Whether to convert the annotations to the format expected by the model. Converts the bounding
  boxes from the format `(top_left_x, top_left_y, width, height)` to `(center_x, center_y, width, height)`
  and in relative coordinates.
- **do_pad** (`bool`, *optional*, defaults to self.do_pad) --
  Whether to pad the image. If `True`, padding will be applied to the bottom and right of
  the image with zeros. If `pad_size` is provided, the image will be padded to the specified
  dimensions. Otherwise, the image will be padded to the maximum height and width of the batch.
- **format** (`str` or `AnnotationFormat`, *optional*, defaults to self.format) --
  Format of the annotations.
- **return_tensors** (`str` or `TensorType`, *optional*, defaults to self.return_tensors) --
  Type of tensors to return. If `None`, will return the list of images.
- **data_format** (`str` or `ChannelDimension`, *optional*, defaults to self.data_format) --
  The channel dimension format of the image. If not provided, it will be the same as the input image.
- **input_data_format** (`ChannelDimension` or `str`, *optional*) --
  The channel dimension format for the input image. If unset, the channel dimension format is inferred
  from the input image. Can be one of:
  - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
  - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.
  - `"none"` or `ChannelDimension.NONE`: image in (height, width) format.
- **pad_size** (`dict[str, int]`, *optional*) --
  The size `{"height": int, "width" int}` to pad the images to. Must be larger than any image size
  provided for preprocessing. If `pad_size` is not provided, images will be padded to the largest
  height and width in the batch.0

Preprocess an image or a batch of images so that it can be used by the model.

**Parameters:**

format (`str`, *optional*, defaults to `"coco_detection"`) : Data format of the annotations. One of "coco_detection" or "coco_panoptic".

do_resize (`bool`, *optional*, defaults to `True`) : Controls whether to resize the image's (height, width) dimensions to the specified `size`. Can be overridden by the `do_resize` parameter in the `preprocess` method.

size (`dict[str, int]` *optional*, defaults to `{"shortest_edge" : 800, "longest_edge": 1333}`): Size of the image's `(height, width)` dimensions after resizing. Can be overridden by the `size` parameter in the `preprocess` method. Available options are: - `{"height": int, "width": int}`: The image will be resized to the exact size `(height, width)`. Do NOT keep the aspect ratio. - `{"shortest_edge": int, "longest_edge": int}`: The image will be resized to a maximum size respecting the aspect ratio and keeping the shortest edge less or equal to `shortest_edge` and the longest edge less or equal to `longest_edge`. - `{"max_height": int, "max_width": int}`: The image will be resized to the maximum size respecting the aspect ratio and keeping the height less or equal to `max_height` and the width less or equal to `max_width`.

resample (`PILImageResampling`, *optional*, defaults to `PILImageResampling.BILINEAR`) : Resampling filter to use if resizing the image.

do_rescale (`bool`, *optional*, defaults to `True`) : Controls whether to rescale the image by the specified scale `rescale_factor`. Can be overridden by the `do_rescale` parameter in the `preprocess` method.

rescale_factor (`int` or `float`, *optional*, defaults to `1/255`) : Scale factor to use if rescaling the image. Can be overridden by the `rescale_factor` parameter in the `preprocess` method.

do_normalize : Controls whether to normalize the image. Can be overridden by the `do_normalize` parameter in the `preprocess` method.

image_mean (`float` or `list[float]`, *optional*, defaults to `IMAGENET_DEFAULT_MEAN`) : Mean values to use when normalizing the image. Can be a single value or a list of values, one for each channel. Can be overridden by the `image_mean` parameter in the `preprocess` method.

image_std (`float` or `list[float]`, *optional*, defaults to `IMAGENET_DEFAULT_STD`) : Standard deviation values to use when normalizing the image. Can be a single value or a list of values, one for each channel. Can be overridden by the `image_std` parameter in the `preprocess` method.

do_pad (`bool`, *optional*, defaults to `True`) : Controls whether to pad the image. Can be overridden by the `do_pad` parameter in the `preprocess` method. If `True`, padding will be applied to the bottom and right of the image with zeros. If `pad_size` is provided, the image will be padded to the specified dimensions. Otherwise, the image will be padded to the maximum height and width of the batch.

pad_size (`dict[str, int]`, *optional*) : The size `{"height": int, "width" int}` to pad the images to. Must be larger than any image size provided for preprocessing. If `pad_size` is not provided, images will be padded to the largest height and width in the batch.

## YolosImageProcessorFast[[transformers.YolosImageProcessorFast]]

#### transformers.YolosImageProcessorFast[[transformers.YolosImageProcessorFast]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/yolos/image_processing_yolos_fast.py#L293)

Constructs a YolosImageProcessorFast image processor.

preprocesstransformers.YolosImageProcessorFast.preprocesshttps://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/image_processing_utils_fast.py#L838[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor']]"}, {"name": "*args", "val": ""}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.processing_utils.ImagesKwargs]"}]- **images** (`Union[PIL.Image.Image, numpy.ndarray, torch.Tensor, list[PIL.Image.Image], list[numpy.ndarray], list[torch.Tensor]]`) --
  Image to preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If
  passing in images with pixel values between 0 and 1, set `do_rescale=False`.
- **return_tensors** (`str` or [TensorType](/docs/transformers/v5.3.0/en/internal/file_utils#transformers.TensorType), *optional*) --
  Returns stacked tensors if set to `'pt'`, otherwise returns a list of tensors.
- ****kwargs** ([ImagesKwargs](/docs/transformers/v5.3.0/en/main_classes/processors#transformers.ImagesKwargs), *optional*) --
  Additional image preprocessing options. Model-specific kwargs are listed above; see the TypedDict class
  for the complete list of supported arguments.0`~image_processing_base.BatchFeature`- **data** (`dict`) -- Dictionary of lists/arrays/tensors returned by the __call__ method ('pixel_values', etc.).
- **tensor_type** (`Union[None, str, TensorType]`, *optional*) -- You can give a tensor_type here to convert the lists of integers in PyTorch/Numpy Tensors at
  initialization.

**Parameters:**

format (`str`, *kwargs*, *optional*, defaults to `AnnotationFormat.COCO_DETECTION`) : Data format of the annotations. One of "coco_detection" or "coco_panoptic".

do_convert_annotations (`bool`, *kwargs*, *optional*, defaults to `True`) : Controls whether to convert the annotations to the format expected by the YOLOS model. Converts the bounding boxes to the format `(center_x, center_y, width, height)` and in the range `[0, 1]`. Can be overridden by the `do_convert_annotations` parameter in the `preprocess` method.

return_segmentation_masks (`bool`, *kwargs*, *optional*, defaults to `False`) : Whether to return segmentation masks.

annotations (`AnnotationType`, *kwargs* or `list[AnnotationType]`, *optional*) : Annotations to transform according to the padding that is applied to the images.

masks_path (`str`, *kwargs* or `pathlib.Path`, *optional*) : Path to the directory containing the segmentation masks.

- ****kwargs** ([ImagesKwargs](/docs/transformers/v5.3.0/en/main_classes/processors#transformers.ImagesKwargs), *optional*) : Additional image preprocessing options. Model-specific kwargs are listed above; see the TypedDict class for the complete list of supported arguments.

**Returns:**

``~image_processing_base.BatchFeature``

- **data** (`dict`) -- Dictionary of lists/arrays/tensors returned by the __call__ method ('pixel_values', etc.).
- **tensor_type** (`Union[None, str, TensorType]`, *optional*) -- You can give a tensor_type here to convert the lists of integers in PyTorch/Numpy Tensors at
  initialization.
#### pad[[transformers.YolosImageProcessorFast.pad]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/yolos/image_processing_yolos_fast.py#L512)
#### post_process_object_detection[[transformers.YolosImageProcessorFast.post_process_object_detection]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/yolos/image_processing_yolos_fast.py#L658)

Converts the raw output of [YolosForObjectDetection](/docs/transformers/v5.3.0/en/model_doc/yolos#transformers.YolosForObjectDetection) into final bounding boxes in (top_left_x, top_left_y,
bottom_right_x, bottom_right_y) format. Only supports PyTorch.

**Parameters:**

outputs (`YolosObjectDetectionOutput`) : Raw outputs of the model.

threshold (`float`, *optional*) : Score threshold to keep object detection predictions.

target_sizes (`torch.Tensor` or `list[tuple[int, int]]`, *optional*) : Tensor of shape `(batch_size, 2)` or list of tuples (`tuple[int, int]`) containing the target size `(height, width)` of each image in the batch. If unset, predictions will not be resized.

**Returns:**

``list[Dict]``

A list of dictionaries, each dictionary containing the scores, labels and boxes for an image
in the batch as predicted by the model.

## YolosModel[[transformers.YolosModel]]

#### transformers.YolosModel[[transformers.YolosModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/yolos/modeling_yolos.py#L448)

The bare Yolos Model outputting raw hidden-states without any specific head on top.

This model inherits from [PreTrainedModel](/docs/transformers/v5.3.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.YolosModel.forwardhttps://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/yolos/modeling_yolos.py#L469[{"name": "pixel_values", "val": ": torch.Tensor | None = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **pixel_values** (`torch.Tensor` of shape `(batch_size, num_channels, image_size, image_size)`, *optional*) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [YolosImageProcessorFast](/docs/transformers/v5.3.0/en/model_doc/yolos#transformers.YolosImageProcessorFast). See [YolosImageProcessorFast.__call__()](/docs/transformers/v5.3.0/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details (`processor_class` uses
  [YolosImageProcessorFast](/docs/transformers/v5.3.0/en/model_doc/yolos#transformers.YolosImageProcessorFast) for processing images).0[BaseModelOutputWithPooling](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)`A [BaseModelOutputWithPooling](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([YolosConfig](/docs/transformers/v5.3.0/en/model_doc/yolos#transformers.YolosConfig)) and inputs.
The [YolosModel](/docs/transformers/v5.3.0/en/model_doc/yolos#transformers.YolosModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

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

Example:

```python
```

**Parameters:**

config ([YolosConfig](/docs/transformers/v5.3.0/en/model_doc/yolos#transformers.YolosConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.3.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

add_pooling_layer (`bool`, *optional*, defaults to `True`) : Whether to add a pooling layer

**Returns:**

`[BaseModelOutputWithPooling](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)``

A [BaseModelOutputWithPooling](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([YolosConfig](/docs/transformers/v5.3.0/en/model_doc/yolos#transformers.YolosConfig)) and inputs.

## YolosForObjectDetection[[transformers.YolosForObjectDetection]]

#### transformers.YolosForObjectDetection[[transformers.YolosForObjectDetection]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/yolos/modeling_yolos.py#L531)

YOLOS Model (consisting of a ViT encoder) with object detection heads on top, for tasks such as COCO detection.

This model inherits from [PreTrainedModel](/docs/transformers/v5.3.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.YolosForObjectDetection.forwardhttps://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/yolos/modeling_yolos.py#L554[{"name": "pixel_values", "val": ": FloatTensor"}, {"name": "labels", "val": ": list[dict] | None = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **pixel_values** (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [YolosImageProcessorFast](/docs/transformers/v5.3.0/en/model_doc/yolos#transformers.YolosImageProcessorFast). See [YolosImageProcessorFast.__call__()](/docs/transformers/v5.3.0/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details (`processor_class` uses
  [YolosImageProcessorFast](/docs/transformers/v5.3.0/en/model_doc/yolos#transformers.YolosImageProcessorFast) for processing images).
- **labels** (`list[Dict]` of len `(batch_size,)`, *optional*) --
  Labels for computing the bipartite matching loss. List of dicts, each dictionary containing at least the
  following 2 keys: `'class_labels'` and `'boxes'` (the class labels and bounding boxes of an image in the
  batch respectively). The class labels themselves should be a `torch.LongTensor` of len `(number of bounding
  boxes in the image,)` and the boxes a `torch.FloatTensor` of shape `(number of bounding boxes in the image,
  4)`.0`YolosObjectDetectionOutput` or `tuple(torch.FloatTensor)`A `YolosObjectDetectionOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([YolosConfig](/docs/transformers/v5.3.0/en/model_doc/yolos#transformers.YolosConfig)) and inputs.
The [YolosForObjectDetection](/docs/transformers/v5.3.0/en/model_doc/yolos#transformers.YolosForObjectDetection) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` are provided)) -- Total loss as a linear combination of a negative log-likehood (cross-entropy) for class prediction and a
  bounding box loss. The latter is defined as a linear combination of the L1 loss and the generalized
  scale-invariant IoU loss.
- **loss_dict** (`Dict`, *optional*) -- A dictionary containing the individual losses. Useful for logging.
- **logits** (`torch.FloatTensor` of shape `(batch_size, num_queries, num_classes + 1)`) -- Classification logits (including no-object) for all queries.
- **pred_boxes** (`torch.FloatTensor` of shape `(batch_size, num_queries, 4)`) -- Normalized boxes coordinates for all queries, represented as (center_x, center_y, width, height). These
  values are normalized in [0, 1], relative to the size of each individual image in the batch (disregarding
  possible padding). You can use `~YolosImageProcessor.post_process` to retrieve the unnormalized bounding
  boxes.
- **auxiliary_outputs** (`list[Dict]`, *optional*) -- Optional, only returned when auxiliary losses are activated (i.e. `config.auxiliary_loss` is set to `True`)
  and labels are provided. It is a list of dictionaries containing the two above keys (`logits` and
  `pred_boxes`) for each decoder layer.
- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) -- Sequence of hidden-states at the output of the last layer of the decoder of the model.
- **hidden_states** (`tuple[torch.FloatTensor]`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple[torch.FloatTensor]`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.

Examples:

```python
>>> from transformers import AutoImageProcessor, AutoModelForObjectDetection
>>> import torch
>>> from PIL import Image
>>> import httpx
>>> from io import BytesIO

>>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
>>> with httpx.stream("GET", url) as response:
...     image = Image.open(BytesIO(response.read()))

>>> image_processor = AutoImageProcessor.from_pretrained("hustvl/yolos-tiny")
>>> model = AutoModelForObjectDetection.from_pretrained("hustvl/yolos-tiny")

>>> inputs = image_processor(images=image, return_tensors="pt")
>>> outputs = model(**inputs)

>>> # convert outputs (bounding boxes and class logits) to Pascal VOC format (xmin, ymin, xmax, ymax)
>>> target_sizes = torch.tensor([image.size[::-1]])
>>> results = image_processor.post_process_object_detection(outputs, threshold=0.9, target_sizes=target_sizes)[
...     0
... ]

>>> for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
...     box = [round(i, 2) for i in box.tolist()]
...     print(
...         f"Detected {model.config.id2label[label.item()]} with confidence "
...         f"{round(score.item(), 3)} at location {box}"
...     )
Detected remote with confidence 0.991 at location [46.48, 72.78, 178.98, 119.3]
Detected remote with confidence 0.908 at location [336.48, 79.27, 368.23, 192.36]
Detected cat with confidence 0.934 at location [337.18, 18.06, 638.14, 373.09]
Detected cat with confidence 0.979 at location [10.93, 53.74, 313.41, 470.67]
Detected remote with confidence 0.974 at location [41.63, 72.23, 178.09, 119.99]
```

**Parameters:**

config ([YolosConfig](/docs/transformers/v5.3.0/en/model_doc/yolos#transformers.YolosConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.3.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``YolosObjectDetectionOutput` or `tuple(torch.FloatTensor)``

A `YolosObjectDetectionOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([YolosConfig](/docs/transformers/v5.3.0/en/model_doc/yolos#transformers.YolosConfig)) and inputs.

