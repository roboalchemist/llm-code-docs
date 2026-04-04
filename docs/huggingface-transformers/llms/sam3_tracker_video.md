# Source: https://huggingface.co/docs/transformers/v5.0.0rc1/model_doc/sam3_tracker_video.md

# SAM3 Tracker Video

    
        
        
        
    

## Overview

SAM3 (Segment Anything Model 3) was introduced in [SAM 3: Segment Anything with Concepts](https://ai.meta.com/research/publications/sam-3-segment-anything-with-concepts/).

Sam3TrackerVideo performs **Promptable Visual Segmentation (PVS)** on videos. PVS takes interactive visual prompts (points, boxes, masks) or text inputs to track a **specific object instance** per prompt across video frames.

Sam3TrackerVideo is an updated version of SAM2 Video that maintains the same API while providing improved performance and capabilities.

The abstract from the paper is the following:

*We present Segment Anything Model (SAM) 3, a unified model that detects, segments, and tracks objects in images and videos based on concept prompts, which we define as either short noun phrases (e.g., "yellow school bus"), image exemplars, or a combination of both. Promptable Concept Segmentation (PCS) takes such prompts and returns segmentation masks and unique identities for all matching object instances. To advance PCS, we build a scalable data engine that produces a high-quality dataset with 4M unique concept labels, including hard negatives, across images and videos. Our model consists of an image-level detector and a memory-based video tracker that share a single backbone. Recognition and localization are decoupled with a presence head, which boosts detection accuracy. SAM 3 doubles the accuracy of existing systems in both image and video PCS, and improves previous SAM capabilities on visual segmentation tasks. We open source SAM 3 along with our new Segment Anything with Concepts (SA-Co) benchmark for promptable concept segmentation.*

This model was contributed by [yonigozlan](https://huggingface.co/yonigozlan) and [ronghanghu](https://huggingface.co/ronghanghu).

## Usage example

### Video Segmentation and Tracking

#### Basic Video Tracking

```python
>>> from transformers import Sam3TrackerVideoModel, Sam3TrackerVideoProcessor
from accelerate import Accelerator
>>> import torch

>>> device = Accelerator().device
>>> model = Sam3TrackerVideoModel.from_pretrained("facebook/sam3").to(device, dtype=torch.bfloat16)
>>> processor = Sam3TrackerVideoProcessor.from_pretrained("facebook/sam3")

>>> # Load video frames (example assumes you have a list of PIL Images)
>>> # video_frames = [Image.open(f"frame_{i:05d}.jpg") for i in range(num_frames)]

>>> # For this example, we'll use the video loading utility
>>> from transformers.video_utils import load_video
>>> video_url = "https://huggingface.co/datasets/hf-internal-testing/sam2-fixtures/resolve/main/bedroom.mp4"
>>> video_frames, _ = load_video(video_url)

>>> # Initialize video inference session
>>> inference_session = processor.init_video_session(
...     video=video_frames,
...     inference_device=device,
...     dtype=torch.bfloat16,
... )

>>> # Add click on first frame to select object
>>> ann_frame_idx = 0
>>> ann_obj_id = 1
>>> points = [[[[210, 350]]]]
>>> labels = [[[1]]]

>>> processor.add_inputs_to_inference_session(
...     inference_session=inference_session,
...     frame_idx=ann_frame_idx,
...     obj_ids=ann_obj_id,
...     input_points=points,
...     input_labels=labels,
... )

>>> # Segment the object on the first frame (optional, you can also propagate the masks through the video directly)
>>> outputs = model(
...     inference_session=inference_session,
...     frame_idx=ann_frame_idx,
... )
>>> video_res_masks = processor.post_process_masks(
...     [outputs.pred_masks], original_sizes=[[inference_session.video_height, inference_session.video_width]], binarize=False
... )[0]
>>> print(f"Segmentation shape: {video_res_masks.shape}")
Segmentation shape: torch.Size([1, 1, 480, 854])

>>> # Propagate through the entire video
>>> video_segments = {}
>>> for sam3_tracker_video_output in model.propagate_in_video_iterator(inference_session):
...     video_res_masks = processor.post_process_masks(
...         [sam3_tracker_video_output.pred_masks], original_sizes=[[inference_session.video_height, inference_session.video_width]], binarize=False
...     )[0]
...     video_segments[sam3_tracker_video_output.frame_idx] = video_res_masks

>>> print(f"Tracked object through {len(video_segments)} frames")
Tracked object through 180 frames
```

#### Multi-Object Video Tracking

Track multiple objects simultaneously across video frames:

```python
>>> # Reset for new tracking session
>>> inference_session.reset_inference_session()

>>> # Add multiple objects on the first frame
>>> ann_frame_idx = 0
>>> obj_ids = [2, 3]
>>> input_points = [[[[200, 300]], [[400, 150]]]]  # Points for two objects (batched)
>>> input_labels = [[[1], [1]]]

>>> processor.add_inputs_to_inference_session(
...     inference_session=inference_session,
...     frame_idx=ann_frame_idx,
...     obj_ids=obj_ids,
...     input_points=input_points,
...     input_labels=input_labels,
... )

>>> # Get masks for both objects on first frame (optional, you can also propagate the masks through the video directly)
>>> outputs = model(
...     inference_session=inference_session,
...     frame_idx=ann_frame_idx,
... )

>>> # Propagate both objects through video
>>> video_segments = {}
>>> for sam3_tracker_video_output in model.propagate_in_video_iterator(inference_session):
...     video_res_masks = processor.post_process_masks(
...         [sam3_tracker_video_output.pred_masks], original_sizes=[[inference_session.video_height, inference_session.video_width]], binarize=False
...     )[0]
...     video_segments[sam3_tracker_video_output.frame_idx] = {
...         obj_id: video_res_masks[i]
...         for i, obj_id in enumerate(inference_session.obj_ids)
...     }

>>> print(f"Tracked {len(inference_session.obj_ids)} objects through {len(video_segments)} frames")
Tracked 2 objects through 180 frames
```

#### Refining Video Segmentation

You can add additional clicks on any frame to refine the tracking:

```python
>>> # Add refinement click on a later frame
>>> refine_frame_idx = 50
>>> ann_obj_id = 2  # Refining first object
>>> points = [[[[220, 280]]]]  # Additional point
>>> labels = [[[1]]]  # Positive click

>>> processor.add_inputs_to_inference_session(
...     inference_session=inference_session,
...     frame_idx=refine_frame_idx,
...     obj_ids=ann_obj_id,
...     input_points=points,
...     input_labels=labels,
... )

>>> # Re-propagate with the additional information
>>> video_segments = {}
>>> for sam3_tracker_video_output in model.propagate_in_video_iterator(inference_session):
...     video_res_masks = processor.post_process_masks(
...         [sam3_tracker_video_output.pred_masks], original_sizes=[[inference_session.video_height, inference_session.video_width]], binarize=False
...     )[0]
...     video_segments[sam3_tracker_video_output.frame_idx] = video_res_masks
```

### Streaming Video Inference

For real-time applications, Sam3TrackerVideo supports processing video frames as they arrive:

```python
>>> # Initialize session for streaming
>>> inference_session = processor.init_video_session(
...     inference_device=device,
...     dtype=torch.bfloat16,
... )

>>> # Process frames one by one
>>> for frame_idx, frame in enumerate(video_frames[:10]):  # Process first 10 frames
...     inputs = processor(images=frame, device=device, return_tensors="pt")
...
...     if frame_idx == 0:
...         # Add point input on first frame
...         processor.add_inputs_to_inference_session(
...             inference_session=inference_session,
...             frame_idx=0,
...             obj_ids=1,
...             input_points=[[[[210, 350], [250, 220]]]],
...             input_labels=[[[1, 1]]],
...             original_size=inputs.original_sizes[0], # need to be provided when using streaming video inference
...         )
...
...     # Process current frame
...     sam3_tracker_video_output = model(inference_session=inference_session, frame=inputs.pixel_values[0])
...
...     video_res_masks = processor.post_process_masks(
...         [sam3_tracker_video_output.pred_masks], original_sizes=inputs.original_sizes, binarize=False
...     )[0]
...     print(f"Frame {frame_idx}: mask shape {video_res_masks.shape}")
```

#### Video Batch Processing for Multiple Objects

Track multiple objects simultaneously in video by adding them all at once:

```python
>>> # Initialize video session
>>> inference_session = processor.init_video_session(
...     video=video_frames,
...     inference_device=device,
...     dtype=torch.bfloat16,
... )

>>> # Add multiple objects on the first frame using batch processing
>>> ann_frame_idx = 0
>>> obj_ids = [2, 3]  # Track two different objects
>>> input_points = [
...     [[[200, 300], [230, 250], [275, 175]], [[400, 150]]]
... ]  # Object 2: 3 points (2 positive, 1 negative); Object 3: 1 point
>>> input_labels = [
...     [[1, 1, 0], [1]]
... ]  # Object 2: positive, positive, negative; Object 3: positive

>>> processor.add_inputs_to_inference_session(
...     inference_session=inference_session,
...     frame_idx=ann_frame_idx,
...     obj_ids=obj_ids,
...     input_points=input_points,
...     input_labels=input_labels,
... )

>>> # Get masks for all objects on the first frame
>>> outputs = model(
...     inference_session=inference_session,
...     frame_idx=ann_frame_idx,
... )
>>> video_res_masks = processor.post_process_masks(
...     [outputs.pred_masks], original_sizes=[[inference_session.video_height, inference_session.video_width]], binarize=False
... )[0]
>>> print(f"Generated masks for {video_res_masks.shape[0]} objects")
Generated masks for 2 objects

>>> # Propagate all objects through the video
>>> video_segments = {}
>>> for sam3_tracker_video_output in model.propagate_in_video_iterator(inference_session):
...     video_res_masks = processor.post_process_masks(
...         [sam3_tracker_video_output.pred_masks], original_sizes=[[inference_session.video_height, inference_session.video_width]], binarize=False
...     )[0]
...     video_segments[sam3_tracker_video_output.frame_idx] = {
...         obj_id: video_res_masks[i]
...         for i, obj_id in enumerate(inference_session.obj_ids)
...     }

>>> print(f"Tracked {len(inference_session.obj_ids)} objects through {len(video_segments)} frames")
Tracked 2 objects through 180 frames
```

## Sam3TrackerVideoConfig[[transformers.Sam3TrackerVideoConfig]]

#### transformers.Sam3TrackerVideoConfig[[transformers.Sam3TrackerVideoConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker_video/configuration_sam3_tracker_video.py#L152)

[Sam3TrackerVideoConfig](/docs/transformers/v5.0.0rc1/en/model_doc/sam3_tracker_video#transformers.Sam3TrackerVideoConfig) is the configuration class to store the configuration of a [Sam3TrackerVideoModel](/docs/transformers/v5.0.0rc1/en/model_doc/sam3_tracker_video#transformers.Sam3TrackerVideoModel). It is used to instantiate a
SAM3 tracker video model according to the specified arguments, defining the memory attention, memory encoder, and image encoder
configs. Instantiating a configuration defaults will yield a similar configuration to that of the SAM 3
[facebook/sam3](https://huggingface.co/facebook/sam3) architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:

```python
>>> from transformers import (
...     Sam3VisionConfig,
...     Sam3TrackerVideoPromptEncoderConfig,
...     Sam3TrackerVideoMaskDecoderConfig,
...     Sam3TrackerVideoModel,
... )

>>> # Initializing a Sam3TrackerVideoConfig with `"facebook/sam3"` style configuration
>>> configuration = Sam3TrackerVideoConfig()

>>> # Initializing a Sam3TrackerVideoModel (with random weights) from the `"facebook/sam3"` style configuration
>>> model = Sam3TrackerVideoModel(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config

>>> # We can also initialize a Sam3TrackerVideoConfig from a Sam3TrackerVideoVisionConfig, Sam3TrackerVideoPromptEncoderConfig, and Sam3TrackerVideoMaskDecoderConfig

>>> # Initializing SAM3 tracker video vision encoder, memory attention, and memory encoder configurations
>>> vision_config = Sam3TrackerVideoVisionConfig()
>>> prompt_encoder_config = Sam3TrackerVideoPromptEncoderConfig()
>>> mask_decoder_config = Sam3TrackerVideoMaskDecoderConfig()

>>> config = Sam3TrackerVideoConfig(vision_config, prompt_encoder_config, mask_decoder_config)
```

**Parameters:**

vision_config (Union[`dict`, `Sam3TrackerVideoVisionConfig`], *optional*) : Dictionary of configuration options used to initialize `Sam3TrackerVideoVisionConfig`.

prompt_encoder_config (Union[`dict`, `Sam3TrackerVideoPromptEncoderConfig`], *optional*) : Dictionary of configuration options used to initialize [Sam3TrackerVideoPromptEncoderConfig](/docs/transformers/v5.0.0rc1/en/model_doc/sam3_tracker_video#transformers.Sam3TrackerVideoPromptEncoderConfig).

mask_decoder_config (Union[`dict`, `Sam3TrackerVideoMaskDecoderConfig`], *optional*) : Dictionary of configuration options used to initialize [Sam3TrackerVideoMaskDecoderConfig](/docs/transformers/v5.0.0rc1/en/model_doc/sam3_tracker_video#transformers.Sam3TrackerVideoMaskDecoderConfig).

initializer_range (`float`, *optional*, defaults to 0.02) : Standard deviation for parameter initialization.

num_maskmem (`int`, *optional*, defaults to 7) : The number of memory slots for the mask memory.

image_size (`int`, *optional*, defaults to 1008) : The size of the input images.

sigmoid_scale_for_mem_enc (`float`, *optional*, defaults to 20.0) : Scale factor for the sigmoid function in the memory encoder.

sigmoid_bias_for_mem_enc (`float`, *optional*, defaults to -10.0) : Bias for the sigmoid function in the memory encoder.

enable_occlusion_spatial_embedding (`bool`, *optional*, defaults to `True`) : Whether to enable spatial embedding for occlusions.

multimask_output_in_sam (`bool`, *optional*, defaults to `True`) : Whether to output multiple masks from the SAM head.

multimask_min_pt_num (`int`, *optional*, defaults to 0) : The minimum number of points to trigger multimask output.

multimask_max_pt_num (`int`, *optional*, defaults to 1) : The maximum number of points to trigger multimask output.

multimask_output_for_tracking (`bool`, *optional*, defaults to `True`) : Whether to use multimask output for tracking.

max_object_pointers_in_encoder (`int`, *optional*, defaults to 16) : The maximum number of object pointers in the encoder.

max_cond_frame_num (`int`, *optional*, defaults to 4) : Maximum number of conditioning frames to use in memory attention.

enable_temporal_pos_encoding_for_object_pointers (`bool`, *optional*, defaults to `True`) : Whether to enable temporal positional encoding for object pointers.

memory_attention_hidden_size (`int`, *optional*, defaults to 256) : Dimensionality of the memory attention hidden states.

memory_attention_num_layers (`int`, *optional*, defaults to 4) : The number of layers in the memory attention module.

memory_attention_num_attention_heads (`int`, *optional*, defaults to 1) : Number of attention heads for each attention layer in the memory attention.

memory_attention_downsample_rate (`int`, *optional*, defaults to 1) : The downsample rate for the attention layers.

memory_attention_feed_forward_hidden_size (`int`, *optional*, defaults to 2048) : The dimension of the feedforward network in the memory attention module.

memory_attention_feed_forward_hidden_act (`str`, *optional*, defaults to `"relu"`) : The non-linear activation function in the feedforward network in the memory attention module.

memory_attention_dropout (`float`, *optional*, defaults to 0.1) : The dropout rate for the memory attention module.

memory_attention_rope_theta (`float`, *optional*, defaults to 10000) : The Rope theta parameter.

memory_attention_rope_feat_sizes (`list[int]`, *optional*, defaults to `[72, 72]`) : The feature sizes for the Rope positional encoding.

memory_attention_rope_dropout (`float`, *optional*, defaults to 0.1) : The dropout rate for the Rope positional encoding.

memory_encoder_hidden_size (`int`, *optional*, defaults to 256) : Dimensionality of the memory encoder hidden states.

memory_encoder_output_channels (`int`, *optional*, defaults to 64) : The number of output channels for the memory encoder.

mask_downsampler_embed_dim (`int`, *optional*, defaults to 256) : The dimension of the mask downsampler embedding.

mask_downsampler_kernel_size (`int`, *optional*, defaults to 3) : The kernel size for the mask downsampler.

mask_downsampler_stride (`int`, *optional*, defaults to 2) : The stride for the mask downsampler.

mask_downsampler_padding (`int`, *optional*, defaults to 1) : The padding for the mask downsampler.

mask_downsampler_total_stride (`int`, *optional*, defaults to 16) : The total stride for the mask downsampler.

mask_downsampler_hidden_act (`str`, *optional*, defaults to `"gelu"`) : The non-linear activation function in the mask downsampler.

memory_fuser_num_layers (`int`, *optional*, defaults to 2) : The number of layers in the memory fuser.

memory_fuser_embed_dim (`int`, *optional*, defaults to 256) : The dimension of the embedding layer in the memory fuser.

memory_fuser_intermediate_dim (`int`, *optional*, defaults to 1024) : The dimension of the intermediate layer in the memory fuser.

memory_fuser_kernel_size (`int`, *optional*, defaults to 7) : The kernel size for the memory fuser.

memory_fuser_padding (`int`, *optional*, defaults to 3) : The padding for the memory fuser.

memory_fuser_layer_scale_init_value (`float`, *optional*, defaults to 1e-06) : The initial value for the layer scale in the memory fuser.

memory_fuser_hidden_act (`str`, *optional*, defaults to `"gelu"`) : The non-linear activation function in the memory fuser.

kwargs (*optional*) : Dictionary of keyword arguments.

## Sam3TrackerVideoMaskDecoderConfig[[transformers.Sam3TrackerVideoMaskDecoderConfig]]

#### transformers.Sam3TrackerVideoMaskDecoderConfig[[transformers.Sam3TrackerVideoMaskDecoderConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker_video/configuration_sam3_tracker_video.py#L79)

This is the configuration class to store the configuration of a `Sam3TrackerVideoMaskDecoder`. It is used to instantiate a SAM3_TRACKER_VIDEO
memory encoder according to the specified arguments, defining the model architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

**Parameters:**

hidden_size (`int`, *optional*, defaults to 256) : Dimensionality of the hidden states.

hidden_act (`str`, *optional*, defaults to `"gelu"`) : The non-linear activation function in the SAM3_TRACKER_VIDEO mask decoder.

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

## Sam3TrackerVideoPromptEncoderConfig[[transformers.Sam3TrackerVideoPromptEncoderConfig]]

#### transformers.Sam3TrackerVideoPromptEncoderConfig[[transformers.Sam3TrackerVideoPromptEncoderConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker_video/configuration_sam3_tracker_video.py#L27)

This is the configuration class to store the configuration of a `Sam3TrackerVideoPromptEncoder`. The `Sam3TrackerVideoPromptEncoder`
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

## Sam3TrackerVideoProcessor[[transformers.Sam3TrackerVideoProcessor]]

#### transformers.Sam3TrackerVideoProcessor[[transformers.Sam3TrackerVideoProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker_video/processing_sam3_tracker_video.py#L38)

Constructs a SAM2 processor which wraps a SAM2 image processor and an 2D points & Bounding boxes processor into a
single processor.

[Sam3TrackerVideoProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/sam3_tracker_video#transformers.Sam3TrackerVideoProcessor) offers all the functionalities of [Sam2ImageProcessorFast](/docs/transformers/v5.0.0rc1/en/model_doc/sam2#transformers.Sam2ImageProcessorFast) and [Sam3TrackerVideoProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/sam3_tracker_video#transformers.Sam3TrackerVideoProcessor). See the docstring of
[__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) and [__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/sam3_tracker_video#transformers.Sam3TrackerVideoProcessor.__call__) for more information.

__call__transformers.Sam3TrackerVideoProcessor.__call__https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker_video/processing_sam3_tracker_video.py#L64[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor'], NoneType] = None"}, {"name": "segmentation_maps", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor'], NoneType] = None"}, {"name": "input_points", "val": ": typing.Union[list[list[list[list[float]]]], torch.Tensor, NoneType] = None"}, {"name": "input_labels", "val": ": typing.Union[list[list[list[int]]], torch.Tensor, NoneType] = None"}, {"name": "input_boxes", "val": ": typing.Union[list[list[list[float]]], torch.Tensor, NoneType] = None"}, {"name": "original_sizes", "val": ": typing.Union[list[list[float]], torch.Tensor, NoneType] = None"}, {"name": "return_tensors", "val": ": typing.Union[str, transformers.utils.generic.TensorType, NoneType] = None"}, {"name": "**kwargs", "val": ""}]- **images** (`ImageInput`, *optional*) --
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

This method uses `Sam3TrackerVideoImageProcessorFast.__call__` method to prepare image(s) for the model. It also prepares 2D
points and bounding boxes for the model if they are provided.

**Parameters:**

image_processor (`Sam2ImageProcessorFast`) : An instance of [Sam2ImageProcessorFast](/docs/transformers/v5.0.0rc1/en/model_doc/sam2#transformers.Sam2ImageProcessorFast).

video_processor (`Sam3TrackerVideoVideoProcessor`) : An instance of `Sam3TrackerVideoVideoProcessor`.

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
#### post_process_masks[[transformers.Sam3TrackerVideoProcessor.post_process_masks]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker_video/processing_sam3_tracker_video.py#L479)

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
#### init_video_session[[transformers.Sam3TrackerVideoProcessor.init_video_session]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker_video/processing_sam3_tracker_video.py#L530)

Initializes a video session for inference.
If a video is provided (async inference), the video will be processed and stored on the `video_storage_device`.

**Parameters:**

video (`VideoInput`, *optional*) : The video to process. No need to provide when streaming.

inference_device (`str` or `torch.device`, *optional*, defaults to "cpu") : The device to use for inference.

inference_state_device (`str` or `torch.device`, *optional*) : The device to store the inference state on.

processing_device (`str` or `torch.device`, *optional*) : The device to use for video processing.

video_storage_device (`str` or `torch.device`, *optional*) : The device to store the processed video frames on.

max_vision_features_cache_size (`int`, *optional*, defaults to 1) : The maximum number of vision features to cache.

dtype (`torch.dtype`, *optional*, defaults to `torch.float32`) : The torch dtype to use for the whole session.
#### add_inputs_to_inference_session[[transformers.Sam3TrackerVideoProcessor.add_inputs_to_inference_session]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker_video/processing_sam3_tracker_video.py#L583)

Process new points, boxes, or masks for a video frame and add them to the inference session.

**Parameters:**

inference_session (`Sam3TrackerVideoInferenceSession`) : The inference session for the video.

frame_idx (`int`) : The index of the frame to process.

obj_ids (`list[int]` or `int`) : The object ID(s) to associate with the points or box. These can be any integers and can be reused later on to specify an object.

input_points (`list[list[list[list[float]]]]`, `torch.Tensor`, *optional*) : The points to add to the frame.

input_labels (`list[list[list[int]]]`, `torch.Tensor`, *optional*) : The labels for the points.

input_boxes (`list[list[list[float]]]`, `torch.Tensor`, *optional*) : The bounding boxes to add to the frame.

input_masks (`np.ndarray`, `torch.Tensor`, `list[np.ndarray]`, or `list[torch.Tensor]`, *optional*) : The mask(s) to add to the frame.

original_size (`tuple[int, int]`, *optional*) : The original size of the video. Provide when streaming.

clear_old_inputs (`bool`, *optional*, defaults to `True`) : Whether to clear old inputs for the object.

## Sam3TrackerVideoInferenceSession[[transformers.Sam3TrackerVideoInferenceSession]]

#### transformers.Sam3TrackerVideoInferenceSession[[transformers.Sam3TrackerVideoInferenceSession]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker_video/modeling_sam3_tracker_video.py#L105)

Manages video inference session parameters, state and cache.

add_mask_inputstransformers.Sam3TrackerVideoInferenceSession.add_mask_inputshttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker_video/modeling_sam3_tracker_video.py#L225[{"name": "obj_idx", "val": ": int"}, {"name": "frame_idx", "val": ": int"}, {"name": "inputs", "val": ": Tensor"}]
Add mask inputs with automatic device placement.

**Parameters:**

video (`torch.FloatTensor`, *optional*) : The video to process. No need to provide when streaming.

video_height (`int`, *optional*) : The height of the video.

video_width (`int`, *optional*) : The width of the video.

inference_device (`torch.device`, *optional*, defaults to `"cpu"`) : The device to use for inference.

inference_state_device (`torch.device`, *optional*, defaults to `"cpu"`) : The device to store the inference state on.

video_storage_device (`torch.device`, *optional*, defaults to `"cpu"`) : The device to store the video on.

dtype (`torch.dtype`, *optional*, defaults to `"float32"`) : The dtype to use for the video.

max_vision_features_cache_size (`int`, *optional*, defaults to 1) : The maximum number of vision features to cache.
#### add_new_frame[[transformers.Sam3TrackerVideoInferenceSession.add_new_frame]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker_video/modeling_sam3_tracker_video.py#L300)

Add new frame with automatic device placement.
#### add_point_inputs[[transformers.Sam3TrackerVideoInferenceSession.add_point_inputs]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker_video/modeling_sam3_tracker_video.py#L211)

Add point inputs with automatic device placement.
#### get_frame[[transformers.Sam3TrackerVideoInferenceSession.get_frame]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker_video/modeling_sam3_tracker_video.py#L316)

Get frame from video.
#### get_obj_num[[transformers.Sam3TrackerVideoInferenceSession.get_obj_num]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker_video/modeling_sam3_tracker_video.py#L206)

Get the total number of unique object ids received so far in this session.
#### get_output[[transformers.Sam3TrackerVideoInferenceSession.get_output]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker_video/modeling_sam3_tracker_video.py#L273)

Get output with smart device management.

**Parameters:**

obj_idx (int) : The index of the object.

frame_idx (int) : The index of the frame.

output_key (str) : The key of the output.

is_conditioning_frame (bool) : Whether the output is for a conditioning frame.
#### obj_id_to_idx[[transformers.Sam3TrackerVideoInferenceSession.obj_id_to_idx]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker_video/modeling_sam3_tracker_video.py#L180)

Map object ID to index, creating new entry if needed.
#### obj_idx_to_id[[transformers.Sam3TrackerVideoInferenceSession.obj_idx_to_id]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker_video/modeling_sam3_tracker_video.py#L202)

Map model-side object index to client-side object id.
#### remove_mask_inputs[[transformers.Sam3TrackerVideoInferenceSession.remove_mask_inputs]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker_video/modeling_sam3_tracker_video.py#L231)

Remove mask inputs.
#### remove_point_inputs[[transformers.Sam3TrackerVideoInferenceSession.remove_point_inputs]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker_video/modeling_sam3_tracker_video.py#L221)

Remove point inputs.
#### reset_inference_session[[transformers.Sam3TrackerVideoInferenceSession.reset_inference_session]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker_video/modeling_sam3_tracker_video.py#L332)

Reset tracking data and cache.
#### reset_tracking_data[[transformers.Sam3TrackerVideoInferenceSession.reset_tracking_data]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker_video/modeling_sam3_tracker_video.py#L320)

Reset tracking data but keep cache.
#### store_output[[transformers.Sam3TrackerVideoInferenceSession.store_output]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker_video/modeling_sam3_tracker_video.py#L236)

Store output with smart device management.
If output_key is None, the output is stored as a dictionary.

**Parameters:**

obj_idx (int) : The index of the object.

frame_idx (int) : The index of the frame.

output_key (Optional[str]) : The key of the output. If None, the output is stored as a dictionary.

output_value (Optional[Union[torch.Tensor, dict]]) : The value of the output.

is_conditioning_frame (bool) : Whether the output is for a conditioning frame.

## Sam3TrackerVideoModel[[transformers.Sam3TrackerVideoModel]]

#### transformers.Sam3TrackerVideoModel[[transformers.Sam3TrackerVideoModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker_video/modeling_sam3_tracker_video.py#L1566)

The bare Sam3 Tracker Video Model outputting raw hidden-states without any specific head on top.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.Sam3TrackerVideoModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker_video/modeling_sam3_tracker_video.py#L1713[{"name": "inference_session", "val": ": Sam3TrackerVideoInferenceSession"}, {"name": "frame_idx", "val": ": typing.Optional[int] = None"}, {"name": "frame", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "reverse", "val": ": bool = False"}, {"name": "run_mem_encoder", "val": ": bool = True"}, {"name": "**kwargs", "val": ""}]- **inference_session** (`~models.sam3_tracker_video.modeling_sam3_tracker_video.Sam3TrackerVideoInferenceSession`) --
  The video inference session object.
- **frame_idx** (`int`, *optional*) --
  The index of the frame on which to run inference. No need to provide when inferring
  on a new streamed frame.
- **frame** (`torch.Tensor`, *optional*) --
  The frame to process. Provide when streaming.
- **reverse** (`bool`, *optional*, defaults to `False`) --
  Whether to propagate in reverse.
- **run_mem_encoder** (`bool`, *optional*, defaults to `True`) --
  Whether to run the memory encoder on predicted masks. The memory encoder is batched across all objects for efficiency.0`transformers.models.sam3_tracker_video.modeling_sam3_tracker_video.Sam3TrackerVideoSegmentationOutput` or `tuple(torch.FloatTensor)`A `transformers.models.sam3_tracker_video.modeling_sam3_tracker_video.Sam3TrackerVideoSegmentationOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Sam3TrackerVideoConfig](/docs/transformers/v5.0.0rc1/en/model_doc/sam3_tracker_video#transformers.Sam3TrackerVideoConfig)) and inputs.

- **object_ids** (`list[int]`, *optional*) -- List of object IDs being tracked in the current frame.
- **pred_masks** (`torch.FloatTensor` of shape `(batch_size, num_masks, height, width)`) -- The predicted masks stored at the model's resolution.
- **object_score_logits** (`torch.FloatTensor` of shape `(batch_size,)`, *optional*) -- Logits for the object scores, indicating if objects are present.
- **frame_idx** (`int`, *optional*, defaults to `None`) -- The frame index of the video.
Propagate the objects through a streamed video frame.

**Parameters:**

config ([Sam3TrackerVideoConfig](/docs/transformers/v5.0.0rc1/en/model_doc/sam3_tracker_video#transformers.Sam3TrackerVideoConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

remove_vision_encoder (`bool`, *optional*, defaults to `False`) : Whether to remove the vision encoder. If True, the vision encoder will be set to None.

**Returns:**

``transformers.models.sam3_tracker_video.modeling_sam3_tracker_video.Sam3TrackerVideoSegmentationOutput` or `tuple(torch.FloatTensor)``

A `transformers.models.sam3_tracker_video.modeling_sam3_tracker_video.Sam3TrackerVideoSegmentationOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Sam3TrackerVideoConfig](/docs/transformers/v5.0.0rc1/en/model_doc/sam3_tracker_video#transformers.Sam3TrackerVideoConfig)) and inputs.

- **object_ids** (`list[int]`, *optional*) -- List of object IDs being tracked in the current frame.
- **pred_masks** (`torch.FloatTensor` of shape `(batch_size, num_masks, height, width)`) -- The predicted masks stored at the model's resolution.
- **object_score_logits** (`torch.FloatTensor` of shape `(batch_size,)`, *optional*) -- Logits for the object scores, indicating if objects are present.
- **frame_idx** (`int`, *optional*, defaults to `None`) -- The frame index of the video.
#### propagate_in_video_iterator[[transformers.Sam3TrackerVideoModel.propagate_in_video_iterator]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam3_tracker_video/modeling_sam3_tracker_video.py#L2745)

Propagate the objects through the video frames. Used when initializing an inference session with a whole video.
Yields Sam3TrackerVideoSegmentationOutput for each frame.

**Parameters:**

inference_session (`~models.sam3_tracker_video.modeling_sam3_tracker_video.Sam3TrackerVideoInferenceSession`) : The video inference session object.

start_frame_idx (`int`, *optional*) : The starting frame index for propagation. Need to be provided if `forward` hasn't been called on new inputs yet. If not provided, the starting frame index will be the earliest frame with input points.

max_frame_num_to_track (`int`, *optional*) : The maximum number of frames to track.

reverse (`bool`, *optional*, defaults to `False`) : Whether to propagate in reverse.

show_progress_bar (`bool`, *optional*, defaults to `False`) : Whether to show a progress bar during propagation.

**Returns:**

``transformers.models.sam3_tracker_video.modeling_sam3_tracker_video.Sam3TrackerVideoSegmentationOutput` or `tuple(torch.FloatTensor)``

A `transformers.models.sam3_tracker_video.modeling_sam3_tracker_video.Sam3TrackerVideoSegmentationOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Sam3TrackerVideoConfig](/docs/transformers/v5.0.0rc1/en/model_doc/sam3_tracker_video#transformers.Sam3TrackerVideoConfig)) and inputs.

- **object_ids** (`list[int]`, *optional*) -- List of object IDs being tracked in the current frame.
- **pred_masks** (`torch.FloatTensor` of shape `(batch_size, num_masks, height, width)`) -- The predicted masks stored at the model's resolution.
- **object_score_logits** (`torch.FloatTensor` of shape `(batch_size,)`, *optional*) -- Logits for the object scores, indicating if objects are present.
- **frame_idx** (`int`, *optional*, defaults to `None`) -- The frame index of the video.

