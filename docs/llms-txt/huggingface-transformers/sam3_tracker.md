# Source: https://huggingface.co/docs/transformers/v5.0.0rc1/model_doc/sam3_tracker.md

# SAM3 Tracker

    
        
        
        
    

## Overview

SAM3 (Segment Anything Model 3) was introduced in [SAM 3: Segment Anything with Concepts](https://ai.meta.com/research/publications/sam-3-segment-anything-with-concepts/).

Sam3Tracker performs **Promptable Visual Segmentation (PVS)** on images. PVS takes interactive visual prompts (points, boxes, masks) or text inputs to segment a **specific object instance** per prompt. This is the task that SAM 1 and SAM 2 focused on, and SAM 3 improves upon it.

Sam3Tracker is an updated version of SAM2 (Segment Anything Model 2) that maintains the same API while providing improved performance and capabilities.

The abstract from the paper is the following:

*We present Segment Anything Model (SAM) 3, a unified model that detects, segments, and tracks objects in images and videos based on concept prompts, which we define as either short noun phrases (e.g., "yellow school bus"), image exemplars, or a combination of both. Promptable Concept Segmentation (PCS) takes such prompts and returns segmentation masks and unique identities for all matching object instances. To advance PCS, we build a scalable data engine that produces a high-quality dataset with 4M unique concept labels, including hard negatives, across images and videos. Our model consists of an image-level detector and a memory-based video tracker that share a single backbone. Recognition and localization are decoupled with a presence head, which boosts detection accuracy. SAM 3 doubles the accuracy of existing systems in both image and video PCS, and improves previous SAM capabilities on visual segmentation tasks. We open source SAM 3 along with our new Segment Anything with Concepts (SA-Co) benchmark for promptable concept segmentation.*

This model was contributed by [yonigozlan](https://huggingface.co/yonigozlan) and [ronghanghu](https://huggingface.co/ronghanghu).

## Usage example

### Automatic Mask Generation with Pipeline

Sam3Tracker can be used for automatic mask generation to segment all objects in an image using the `mask-generation` pipeline:

```python
>>> from transformers import pipeline

>>> generator = pipeline("mask-generation", model="facebook/sam3", device=0)
>>> image_url = "https://huggingface.co/datasets/hf-internal-testing/sam2-fixtures/resolve/main/truck.jpg"
>>> outputs = generator(image_url, points_per_batch=64)

>>> len(outputs["masks"])  # Number of masks generated
39
```

### Basic Image Segmentation

#### Single Point Click

You can segment objects by providing a single point click on the object you want to segment:

```python
>>> from transformers import Sam3TrackerProcessor, Sam3TrackerModel
from accelerate import Accelerator
>>> import torch
>>> from PIL import Image
>>> import requests

>>> device = Accelerator().device

>>> model = Sam3TrackerModel.from_pretrained("facebook/sam3").to(device)
>>> processor = Sam3TrackerProcessor.from_pretrained("facebook/sam3")

>>> image_url = "https://huggingface.co/datasets/hf-internal-testing/sam2-fixtures/resolve/main/truck.jpg"
>>> raw_image = Image.open(requests.get(image_url, stream=True).raw).convert("RGB")

>>> input_points = [[[[500, 375]]]]  # Single point click, 4 dimensions (image_dim, object_dim, point_per_object_dim, coordinates)
>>> input_labels = [[[1]]]  # 1 for positive click, 0 for negative click, 3 dimensions (image_dim, object_dim, point_label)

>>> inputs = processor(images=raw_image, input_points=input_points, input_labels=input_labels, return_tensors="pt").to(model.device)

>>> with torch.no_grad():
...     outputs = model(**inputs)

>>> masks = processor.post_process_masks(outputs.pred_masks.cpu(), inputs["original_sizes"])[0]

>>> # The model outputs multiple mask predictions ranked by quality score
>>> print(f"Generated {masks.shape[1]} masks with shape {masks.shape}")
Generated 3 masks with shape torch.Size([1, 3, 1500, 2250])
```

#### Multiple Points for Refinement

You can provide multiple points to refine the segmentation:

```python
>>> # Add both positive and negative points to refine the mask
>>> input_points = [[[[500, 375], [1125, 625]]]]  # Multiple points for refinement
>>> input_labels = [[[1, 1]]]  # Both positive clicks

>>> inputs = processor(images=raw_image, input_points=input_points, input_labels=input_labels, return_tensors="pt").to(device)

>>> with torch.no_grad():
...     outputs = model(**inputs)

>>> masks = processor.post_process_masks(outputs.pred_masks.cpu(), inputs["original_sizes"])[0]
```

#### Bounding Box Input

Sam3Tracker also supports bounding box inputs for segmentation:

```python
>>> # Define bounding box as [x_min, y_min, x_max, y_max]
>>> input_boxes = [[[75, 275, 1725, 850]]]

>>> inputs = processor(images=raw_image, input_boxes=input_boxes, return_tensors="pt").to(device)

>>> with torch.no_grad():
...     outputs = model(**inputs)

>>> masks = processor.post_process_masks(outputs.pred_masks.cpu(), inputs["original_sizes"])[0]
```

#### Multiple Objects Segmentation

You can segment multiple objects simultaneously:

```python
>>> # Define points for two different objects
>>> input_points = [[[[500, 375]], [[650, 750]]]]  # Points for two objects in same image
>>> input_labels = [[[1], [1]]]  # Positive clicks for both objects

>>> inputs = processor(images=raw_image, input_points=input_points, input_labels=input_labels, return_tensors="pt").to(model.device)

>>> with torch.no_grad():
...     outputs = model(**inputs, multimask_output=False)

>>> # Each object gets its own mask
>>> masks = processor.post_process_masks(outputs.pred_masks.cpu(), inputs["original_sizes"])[0]
>>> print(f"Generated masks for {masks.shape[0]} objects")
Generated masks for 2 objects
```

### Batch Inference

#### Batched Images

Process multiple images simultaneously for improved efficiency:

```python
>>> from transformers import Sam3TrackerProcessor, Sam3TrackerModel
from accelerate import Accelerator
>>> import torch
>>> from PIL import Image
>>> import requests

>>> device = Accelerator().device

>>> model = Sam3TrackerModel.from_pretrained("facebook/sam3").to(device)
>>> processor = Sam3TrackerProcessor.from_pretrained("facebook/sam3")

>>> # Load multiple images
>>> image_urls = [
...     "https://huggingface.co/datasets/hf-internal-testing/sam2-fixtures/resolve/main/truck.jpg",
...     "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/model_doc/dog-sam.png"
... ]
>>> raw_images = [Image.open(requests.get(url, stream=True).raw).convert("RGB") for url in image_urls]

>>> # Single point per image
>>> input_points = [[[[500, 375]]], [[[770, 200]]]]  # One point for each image
>>> input_labels = [[[1]], [[1]]]  # Positive clicks for both images

>>> inputs = processor(images=raw_images, input_points=input_points, input_labels=input_labels, return_tensors="pt").to(model.device)

>>> with torch.no_grad():
...     outputs = model(**inputs, multimask_output=False)

>>> # Post-process masks for each image
>>> all_masks = processor.post_process_masks(outputs.pred_masks.cpu(), inputs["original_sizes"])
>>> print(f"Processed {len(all_masks)} images, each with {all_masks[0].shape[0]} objects")
Processed 2 images, each with 1 objects
```

#### Batched Objects per Image

Segment multiple objects within each image using batch inference:

```python
>>> # Multiple objects per image - different numbers of objects per image
>>> input_points = [
...     [[[500, 375]], [[650, 750]]],  # Truck image: 2 objects
...     [[[770, 200]]]  # Dog image: 1 object
... ]
>>> input_labels = [
...     [[1], [1]],  # Truck image: positive clicks for both objects
...     [[1]]  # Dog image: positive click for the object
... ]

>>> inputs = processor(images=raw_images, input_points=input_points, input_labels=input_labels, return_tensors="pt").to(device)

>>> with torch.no_grad():
...     outputs = model(**inputs, multimask_output=False)

>>> all_masks = processor.post_process_masks(outputs.pred_masks.cpu(), inputs["original_sizes"])
```

#### Batched Images with Batched Objects and Multiple Points

Handle complex batch scenarios with multiple points per object:

```python
>>> # Add groceries image for more complex example
>>> groceries_url = "https://huggingface.co/datasets/hf-internal-testing/sam2-fixtures/resolve/main/groceries.jpg"
>>> groceries_image = Image.open(requests.get(groceries_url, stream=True).raw).convert("RGB")
>>> raw_images = [raw_images[0], groceries_image]  # Use truck and groceries images

>>> # Complex batching: multiple images, multiple objects, multiple points per object
>>> input_points = [
...     [[[500, 375]], [[650, 750]]],  # Truck image: 2 objects with 1 point each
...     [[[400, 300]], [[630, 300], [550, 300]]]  # Groceries image: obj1 has 1 point, obj2 has 2 points
... ]
>>> input_labels = [
...     [[1], [1]],  # Truck image: positive clicks
...     [[1], [1, 1]]  # Groceries image: positive clicks for refinement
... ]

>>> inputs = processor(images=raw_images, input_points=input_points, input_labels=input_labels, return_tensors="pt").to(device)

>>> with torch.no_grad():
...     outputs = model(**inputs, multimask_output=False)

>>> all_masks = processor.post_process_masks(outputs.pred_masks.cpu(), inputs["original_sizes"])
```

#### Batched Bounding Boxes

Process multiple images with bounding box inputs:

```python
>>> # Multiple bounding boxes per image (using truck and groceries images)
>>> input_boxes = [
...     [[75, 275, 1725, 850], [425, 600, 700, 875], [1375, 550, 1650, 800], [1240, 675, 1400, 750]],  # Truck image: 4 boxes
...     [[450, 170, 520, 350], [350, 190, 450, 350], [500, 170, 580, 350], [580, 170, 640, 350]]  # Groceries image: 4 boxes
... ]

>>> # Update images for this example
>>> raw_images = [raw_images[0], groceries_image]  # truck and groceries

>>> inputs = processor(images=raw_images, input_boxes=input_boxes, return_tensors="pt").to(device)

>>> with torch.no_grad():
...     outputs = model(**inputs, multimask_output=False)

>>> all_masks = processor.post_process_masks(outputs.pred_masks.cpu(), inputs["original_sizes"])
>>> print(f"Processed {len(input_boxes)} images with {len(input_boxes[0])} and {len(input_boxes[1])} boxes respectively")
Processed 2 images with 4 and 4 boxes respectively
```

### Using Previous Masks as Input

Sam3Tracker can use masks from previous predictions as input to refine segmentation:

```python
>>> # Get initial segmentation
>>> input_points = [[[[500, 375]]]]
>>> input_labels = [[[1]]]
>>> inputs = processor(images=raw_image, input_points=input_points, input_labels=input_labels, return_tensors="pt").to(device)

>>> with torch.no_grad():
...     outputs = model(**inputs)

>>> # Use the best mask as input for refinement
>>> mask_input = outputs.pred_masks[:, :, torch.argmax(outputs.iou_scores.squeeze())]

>>> # Add additional points with the mask input
>>> new_input_points = [[[[500, 375], [450, 300]]]]
>>> new_input_labels = [[[1, 1]]]
>>> inputs = processor(
...     input_points=new_input_points,
...     input_labels=new_input_labels,
...     original_sizes=inputs["original_sizes"],
...     return_tensors="pt",
... ).to(device)

>>> with torch.no_grad():
...     refined_outputs = model(
...         **inputs,
...         input_masks=mask_input,
...         image_embeddings=outputs.image_embeddings,
...         multimask_output=False,
...     )
```

## Sam3TrackerConfig[[transformers.Sam3TrackerConfig]]

#### transformers.Sam3TrackerConfig[[transformers.Sam3TrackerConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker/configuration_sam3_tracker.py#L152)

[Sam3TrackerConfig](/docs/transformers/v5.0.0rc1/en/model_doc/sam3_tracker#transformers.Sam3TrackerConfig) is the configuration class to store the configuration of a [Sam3TrackerModel](/docs/transformers/v5.0.0rc1/en/model_doc/sam3_tracker#transformers.Sam3TrackerModel). It is used to instantiate a
SAM3_TRACKER model according to the specified arguments, defining the memory attention, memory encoder, and image encoder
configs. Instantiating a configuration defaults will yield a similar configuration to that of the SAM 2.1 Hiera-tiny
[facebook/sam3_tracker.1-hiera-tiny](https://huggingface.co/facebook/sam3_tracker.1-hiera-tiny) architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:

```python
>>> from transformers import (
...     Sam3TrackerVisionConfig,
...     Sam3TrackerPromptEncoderConfig,
...     Sam3TrackerMaskDecoderConfig,
...     Sam3TrackerModel,
... )

>>> # Initializing a Sam3TrackerConfig with `"facebook/sam3_tracker.1_hiera_tiny"` style configuration
>>> configuration = Sam3Trackerconfig()

>>> # Initializing a Sam3TrackerModel (with random weights) from the `"facebook/sam3_tracker.1_hiera_tiny"` style configuration
>>> model = Sam3TrackerModel(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config

>>> # We can also initialize a Sam3TrackerConfig from a Sam3TrackerVisionConfig, Sam3TrackerPromptEncoderConfig, and Sam3TrackerMaskDecoderConfig

>>> # Initializing SAM3_TRACKER vision encoder, memory attention, and memory encoder configurations
>>> vision_config = Sam3TrackerVisionConfig()
>>> prompt_encoder_config = Sam3TrackerPromptEncoderConfig()
>>> mask_decoder_config = Sam3TrackerMaskDecoderConfig()

>>> config = Sam3TrackerConfig(vision_config, prompt_encoder_config, mask_decoder_config)
```

**Parameters:**

vision_config (Union[`dict`, `Sam3TrackerVisionConfig`], *optional*) : Dictionary of configuration options used to initialize `Sam3TrackerVisionConfig`.

prompt_encoder_config (Union[`dict`, `Sam3TrackerPromptEncoderConfig`], *optional*) : Dictionary of configuration options used to initialize [Sam3TrackerPromptEncoderConfig](/docs/transformers/v5.0.0rc1/en/model_doc/sam3_tracker#transformers.Sam3TrackerPromptEncoderConfig).

mask_decoder_config (Union[`dict`, `Sam3TrackerMaskDecoderConfig`], *optional*) : Dictionary of configuration options used to initialize [Sam3TrackerMaskDecoderConfig](/docs/transformers/v5.0.0rc1/en/model_doc/sam3_tracker#transformers.Sam3TrackerMaskDecoderConfig).

initializer_range (`float`, *optional*, defaults to 0.02) : Standard deviation for parameter initialization.

## Sam3TrackerPromptEncoderConfig[[transformers.Sam3TrackerPromptEncoderConfig]]

#### transformers.Sam3TrackerPromptEncoderConfig[[transformers.Sam3TrackerPromptEncoderConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker/configuration_sam3_tracker.py#L27)

This is the configuration class to store the configuration of a `Sam3TrackerPromptEncoder`. The `Sam3TrackerPromptEncoder`
module is used to encode the input 2D points and bounding boxes.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

**Parameters:**

hidden_size (`int`, *optional*, defaults to 256) : Dimensionality of the hidden states.

image_size (`int`, *optional*, defaults to 1008) : The expected output resolution of the image.

patch_size (`int`, *optional*, defaults to 14) : The size (resolution) of each patch.

mask_input_channels (`int`, *optional*, defaults to 16) : The number of channels to be fed to the `MaskDecoder` module.

num_point_embeddings (`int`, *optional*, defaults to 4) : The number of point embeddings to be used.

hidden_act (`str`, *optional*, defaults to `"gelu"`) : The non-linear activation function in the encoder and pooler.

layer_norm_eps (`float`, *optional*, defaults to 1e-06) : The epsilon used by the layer normalization layers.

scale (`float`, *optional*, defaults to 1) : The scale factor for the prompt encoder.

## Sam3TrackerMaskDecoderConfig[[transformers.Sam3TrackerMaskDecoderConfig]]

#### transformers.Sam3TrackerMaskDecoderConfig[[transformers.Sam3TrackerMaskDecoderConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker/configuration_sam3_tracker.py#L79)

This is the configuration class to store the configuration of a `Sam3TrackerMaskDecoder`. It is used to instantiate a SAM3_TRACKER
memory encoder according to the specified arguments, defining the model architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

**Parameters:**

hidden_size (`int`, *optional*, defaults to 256) : Dimensionality of the hidden states.

hidden_act (`str`, *optional*, defaults to `"gelu"`) : The non-linear activation function in the SAM3_TRACKER mask decoder.

mlp_dim (`int`, *optional*, defaults to 2048) : The dimension of the MLP in the two-way transformer.

num_hidden_layers (`int`, *optional*, defaults to 2) : The number of hidden layers in the two-way transformer.

num_attention_heads (`int`, *optional*, defaults to 8) : The number of attention heads in the two-way transformer.

attention_downsample_rate (`int`, *optional*, defaults to 2) : The downsample rate for the attention layers.

num_multimask_outputs (`int`, *optional*, defaults to 3) : The number of multimask outputs.

iou_head_depth (`int`, *optional*, defaults to 3) : The depth of the IoU head.

iou_head_hidden_dim (`int`, *optional*, defaults to 256) : The hidden dimension of the IoU head.

dynamic_multimask_via_stability (`bool`, *optional*, defaults to `True`) : Whether to use dynamic multimask via stability.

dynamic_multimask_stability_delta (`float`, *optional*, defaults to 0.05) : The stability delta for the dynamic multimask.

dynamic_multimask_stability_thresh (`float`, *optional*, defaults to 0.98) : The stability threshold for the dynamic multimask.

## Sam3TrackerProcessor[[transformers.Sam3TrackerProcessor]]

#### transformers.Sam3TrackerProcessor[[transformers.Sam3TrackerProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker/processing_sam3_tracker.py#L37)

Constructs a SAM3_TRACKER processor which wraps a SAM3_TRACKER image processor and an 2D points & Bounding boxes processor into a
single processor.

[Sam3TrackerProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/sam3_tracker#transformers.Sam3TrackerProcessor) offers all the functionalities of `Sam3TrackerImageProcessorFast` and [Sam3TrackerVideoProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/sam3_tracker_video#transformers.Sam3TrackerVideoProcessor). See the docstring of
`~Sam3TrackerImageProcessorFast.__call__` and [__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/sam3_tracker_video#transformers.Sam3TrackerVideoProcessor.__call__) for more information.

__call__transformers.Sam3TrackerProcessor.__call__https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker/processing_sam3_tracker.py#L59[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor'], NoneType] = None"}, {"name": "segmentation_maps", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor'], NoneType] = None"}, {"name": "input_points", "val": ": typing.Union[list[list[list[list[float]]]], torch.Tensor, NoneType] = None"}, {"name": "input_labels", "val": ": typing.Union[list[list[list[int]]], torch.Tensor, NoneType] = None"}, {"name": "input_boxes", "val": ": typing.Union[list[list[list[float]]], torch.Tensor, NoneType] = None"}, {"name": "original_sizes", "val": ": typing.Union[list[list[float]], torch.Tensor, NoneType] = None"}, {"name": "return_tensors", "val": ": typing.Union[str, transformers.utils.generic.TensorType, NoneType] = None"}, {"name": "**kwargs", "val": ""}]- **images** (`ImageInput`, *optional*) --
  The image(s) to process.
- **segmentation_maps** (`ImageInput`, *optional*) --
  The segmentation maps to process.
- **input_points** (`list[list[list[list[float]]]]`, `torch.Tensor`, *optional*) --
  The points to add to the frame.
- **input_labels** (`list[list[list[int]]]`, `torch.Tensor`, *optional*) --
  The labels for the points.
- **input_boxes** (`list[list[list[float]]]`, `torch.Tensor`, *optional*) --
  The bounding boxes to add to the frame.
- **original_sizes** (`list[list[float]]`, `torch.Tensor`, *optional*) --
  The original sizes of the images.
- **return_tensors** (`str` or `TensorType`, *optional*) --
  The type of tensors to return.
- ****kwargs** --
  Additional keyword arguments to pass to the image processor.0A [BatchEncoding](/docs/transformers/v5.0.0rc1/en/main_classes/tokenizer#transformers.BatchEncoding) with the following fields- `pixel_values` (`torch.Tensor`): The processed image(s).
- `original_sizes` (`list[list[float]]`): The original sizes of the images.
- `labels` (`torch.Tensor`): The processed segmentation maps (if provided).
- `input_points` (`torch.Tensor`): The processed points.
- `input_labels` (`torch.Tensor`): The processed labels.
- `input_boxes` (`torch.Tensor`): The processed bounding boxes.

This method uses `Sam3TrackerImageProcessorFast.__call__` method to prepare image(s) for the model. It also prepares 2D
points and bounding boxes for the model if they are provided.

**Parameters:**

image_processor (`Sam3TrackerImageProcessorFast`) : An instance of `Sam3TrackerImageProcessorFast`.

target_size (`int`, *optional*) : The target size (target_size, target_size) to which the image will be resized.

point_pad_value (`int`, *optional*, defaults to -10) : The value used for padding input points.

**Returns:**

`A [BatchEncoding](/docs/transformers/v5.0.0rc1/en/main_classes/tokenizer#transformers.BatchEncoding) with the following fields`

- `pixel_values` (`torch.Tensor`): The processed image(s).
- `original_sizes` (`list[list[float]]`): The original sizes of the images.
- `labels` (`torch.Tensor`): The processed segmentation maps (if provided).
- `input_points` (`torch.Tensor`): The processed points.
- `input_labels` (`torch.Tensor`): The processed labels.
- `input_boxes` (`torch.Tensor`): The processed bounding boxes.
#### post_process_masks[[transformers.Sam3TrackerProcessor.post_process_masks]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker/processing_sam3_tracker.py#L474)

Remove padding and upscale masks to the original image size.

**Parameters:**

masks (`Union[List[torch.Tensor], List[np.ndarray]]`) : Batched masks from the mask_decoder in (batch_size, num_channels, height, width) format.

original_sizes (`Union[torch.Tensor, List[Tuple[int,int]]]`) : The original sizes of each image before it was resized to the model's expected input shape, in (height, width) format.

mask_threshold (`float`, *optional*, defaults to 0.0) : Threshold for binarization and post-processing operations.

binarize (`bool`, *optional*, defaults to `True`) : Whether to binarize the masks.

max_hole_area (`float`, *optional*, defaults to 0.0) : The maximum area of a hole to fill.

max_sprinkle_area (`float`, *optional*, defaults to 0.0) : The maximum area of a sprinkle to fill.

apply_non_overlapping_constraints (`bool`, *optional*, defaults to `False`) : Whether to apply non-overlapping constraints to the masks.

**Returns:**

`(`torch.Tensor`)`

Batched masks in batch_size, num_channels, height, width) format, where (height, width)
is given by original_size.

## Sam3TrackerModel[[transformers.Sam3TrackerModel]]

#### transformers.Sam3TrackerModel[[transformers.Sam3TrackerModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker/modeling_sam3_tracker.py#L762)

Segment Anything Model 2 (SAM 2) for generating segmentation masks, given an input image and
input points and labels, boxes, or masks.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.Sam3TrackerModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker/modeling_sam3_tracker.py#L878[{"name": "pixel_values", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "input_points", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "input_labels", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "input_boxes", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "input_masks", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "image_embeddings", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "multimask_output", "val": ": bool = True"}, {"name": "attention_similarity", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "target_embedding", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **pixel_values** (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`, *optional*) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  `image_processor_class`. See `image_processor_class.__call__` for details (`processor_class` uses
  `image_processor_class` for processing images).
- **input_points** (`torch.FloatTensor` of shape `(batch_size, num_points, 2)`) --
  Input 2D spatial points, this is used by the prompt encoder to encode the prompt. Generally yields to much
  better results. The points can be obtained by passing a list of list of list to the processor that will
  create corresponding `torch` tensors of dimension 4. The first dimension is the image batch size, the
  second dimension is the point batch size (i.e. how many segmentation masks do we want the model to predict
  per input point), the third dimension is the number of points per segmentation mask (it is possible to pass
  multiple points for a single mask), and the last dimension is the x (vertical) and y (horizontal)
  coordinates of the point. If a different number of points is passed either for each image, or for each
  mask, the processor will create "PAD" points that will correspond to the (0, 0) coordinate, and the
  computation of the embedding will be skipped for these points using the labels.
- **input_labels** (`torch.LongTensor` of shape `(batch_size, point_batch_size, num_points)`) --
  Input labels for the points, this is used by the prompt encoder to encode the prompt. According to the
  official implementation, there are 3 types of labels

  - `1`: the point is a point that contains the object of interest
  - `0`: the point is a point that does not contain the object of interest
  - `-1`: the point corresponds to the background

  We added the label:

  - `-10`: the point is a padding point, thus should be ignored by the prompt encoder

  The padding labels should be automatically done by the processor.
- **input_boxes** (`torch.FloatTensor` of shape `(batch_size, num_boxes, 4)`) --
  Input boxes for the points, this is used by the prompt encoder to encode the prompt. Generally yields to
  much better generated masks. The boxes can be obtained by passing a list of list of list to the processor,
  that will generate a `torch` tensor, with each dimension corresponding respectively to the image batch
  size, the number of boxes per image and the coordinates of the top left and bottom right point of the box.
  In the order (`x1`, `y1`, `x2`, `y2`):

  - `x1`: the x coordinate of the top left point of the input box
  - `y1`: the y coordinate of the top left point of the input box
  - `x2`: the x coordinate of the bottom right point of the input box
  - `y2`: the y coordinate of the bottom right point of the input box
- **input_masks** (`torch.FloatTensor` of shape `(batch_size, image_size, image_size)`) --
  SAM model also accepts segmentation masks as input. The mask will be embedded by the prompt encoder to
  generate a corresponding embedding, that will be fed later on to the mask decoder. These masks needs to be
  manually fed by the user, and they need to be of shape (`batch_size`, `image_size`, `image_size`).
- **image_embeddings** (`torch.FloatTensor` of shape `(batch_size, output_channels, window_size, window_size)`) --
  Image embeddings, this is used by the mask decoder to generate masks and iou scores. For more memory
  efficient computation, users can first retrieve the image embeddings using the `get_image_embeddings`
  method, and then feed them to the `forward` method instead of feeding the `pixel_values`.
- **multimask_output** (`bool`, *optional*) --
  In the original implementation and paper, the model always outputs 3 masks per image (or per point / per
  bounding box if relevant). However, it is possible to just output a single mask, that corresponds to the
  "best" mask, by specifying `multimask_output=False`.
- **attention_similarity** (`torch.FloatTensor`, *optional*) --
  Attention similarity tensor, to be provided to the mask decoder for target-guided attention in case the
  model is used for personalization as introduced in [PerSAM](https://huggingface.co/papers/2305.03048).
- **target_embedding** (`torch.FloatTensor`, *optional*) --
  Embedding of the target concept, to be provided to the mask decoder for target-semantic prompting in case
  the model is used for personalization as introduced in [PerSAM](https://huggingface.co/papers/2305.03048).0`transformers.models.sam3_tracker.modeling_sam3_tracker.Sam3TrackerImageSegmentationOutput` or `tuple(torch.FloatTensor)`A `transformers.models.sam3_tracker.modeling_sam3_tracker.Sam3TrackerImageSegmentationOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Sam3TrackerConfig](/docs/transformers/v5.0.0rc1/en/model_doc/sam3_tracker#transformers.Sam3TrackerConfig)) and inputs.

- **iou_scores** (`torch.FloatTensor` of shape `(batch_size, point_batch_size, num_masks)`) -- The Intersection over Union (IoU) scores of the predicted masks.
- **pred_masks** (`torch.FloatTensor` of shape `(batch_size, point_batch_size, num_masks, height, width)`) -- The predicted low-resolution masks. This is an alias for `low_res_masks`. These masks need to be post-processed
  by the processor to be brought to the original image size.
- **object_score_logits** (`torch.FloatTensor` of shape `(batch_size, point_batch_size, 1)`) -- Logits for the object score, indicating if an object is present.
- **image_embeddings** (`tuple(torch.FloatTensor)`) -- The features from the FPN, which are used by the mask decoder. This is a tuple of `torch.FloatTensor` where each
  tensor has shape `(batch_size, channels, height, width)`.
- **vision_hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of each stage) of shape `(batch_size, height, width, hidden_size)`.
  Hidden-states of the vision model at the output of each stage.
- **vision_attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length, sequence_length)`.
  Attentions weights of the vision model.
- **mask_decoder_attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length, sequence_length)`.
  Attentions weights of the mask decoder.
The [Sam3TrackerModel](/docs/transformers/v5.0.0rc1/en/model_doc/sam3_tracker#transformers.Sam3TrackerModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Example:

```python
>>> from PIL import Image
>>> import requests
>>> from transformers import AutoModel, AutoProcessor

>>> model = AutoModel.from_pretrained("danelcsb/sam3_tracker.1_hiera_tiny")
>>> processor = AutoProcessor.from_pretrained("danelcsb/sam3_tracker.1_hiera_tiny")

>>> img_url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/model_doc/sam-car.png"
>>> raw_image = Image.open(requests.get(img_url, stream=True).raw).convert("RGB")
>>> input_points = [[[400, 650]]]  # 2D location of a window on the car
>>> inputs = processor(images=raw_image, input_points=input_points, return_tensors="pt")

>>> # Get segmentation mask
>>> outputs = model(**inputs)

>>> # Postprocess masks
>>> masks = processor.post_process_masks(
...     outputs.pred_masks, inputs["original_sizes"]
... )
```

**Parameters:**

config ([Sam3TrackerConfig](/docs/transformers/v5.0.0rc1/en/model_doc/sam3_tracker#transformers.Sam3TrackerConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``transformers.models.sam3_tracker.modeling_sam3_tracker.Sam3TrackerImageSegmentationOutput` or `tuple(torch.FloatTensor)``

A `transformers.models.sam3_tracker.modeling_sam3_tracker.Sam3TrackerImageSegmentationOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Sam3TrackerConfig](/docs/transformers/v5.0.0rc1/en/model_doc/sam3_tracker#transformers.Sam3TrackerConfig)) and inputs.

- **iou_scores** (`torch.FloatTensor` of shape `(batch_size, point_batch_size, num_masks)`) -- The Intersection over Union (IoU) scores of the predicted masks.
- **pred_masks** (`torch.FloatTensor` of shape `(batch_size, point_batch_size, num_masks, height, width)`) -- The predicted low-resolution masks. This is an alias for `low_res_masks`. These masks need to be post-processed
  by the processor to be brought to the original image size.
- **object_score_logits** (`torch.FloatTensor` of shape `(batch_size, point_batch_size, 1)`) -- Logits for the object score, indicating if an object is present.
- **image_embeddings** (`tuple(torch.FloatTensor)`) -- The features from the FPN, which are used by the mask decoder. This is a tuple of `torch.FloatTensor` where each
  tensor has shape `(batch_size, channels, height, width)`.
- **vision_hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of each stage) of shape `(batch_size, height, width, hidden_size)`.
  Hidden-states of the vision model at the output of each stage.
- **vision_attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length, sequence_length)`.
  Attentions weights of the vision model.
- **mask_decoder_attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length, sequence_length)`.
  Attentions weights of the mask decoder.

## Sam3TrackerPreTrainedModel[[transformers.Sam3TrackerPreTrainedModel]]

#### transformers.Sam3TrackerPreTrainedModel[[transformers.Sam3TrackerPreTrainedModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker/modeling_sam3_tracker.py#L116)

Segment Anything Model 3 (SAM 3) for generating segmentation masks, given an input image and
input points and labels, boxes, or masks.

_forward_unimplementedtransformers.Sam3TrackerPreTrainedModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/torch/nn/modules/module.py#L388[{"name": "*input", "val": ": typing.Any"}]
Define the computation performed at every call.

Should be overridden by all subclasses.

Although the recipe for forward pass needs to be defined within
this function, one should call the `Module` instance afterwards
instead of this since the former takes care of running the
registered hooks while the latter silently ignores them.

**Parameters:**

config ([PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

