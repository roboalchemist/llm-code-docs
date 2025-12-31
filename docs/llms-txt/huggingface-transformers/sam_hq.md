# Source: https://huggingface.co/docs/transformers/v5.0.0rc1/model_doc/sam_hq.md

# SAM-HQ

## Overview

SAM-HQ (High-Quality Segment Anything Model) was proposed in [Segment Anything in High Quality](https://huggingface.co/papers/2306.01567) by Lei Ke, Mingqiao Ye, Martin Danelljan, Yifan Liu, Yu-Wing Tai, Chi-Keung Tang, Fisher Yu.

The model is an enhancement to the original SAM model that produces significantly higher quality segmentation masks while maintaining SAM's original promptable design, efficiency, and zero-shot generalizability.

![example image](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/model_doc/sam-output.png)

SAM-HQ introduces several key improvements over the original SAM model:

1. High-Quality Output Token: A learnable token injected into SAM's mask decoder for higher quality mask prediction
2. Global-local Feature Fusion: Combines features from different stages of the model for improved mask details
3. Training Data: Uses a carefully curated dataset of 44K high-quality masks instead of SA-1B
4. Efficiency: Adds only 0.5% additional parameters while significantly improving mask quality
5. Zero-shot Capability: Maintains SAM's strong zero-shot performance while improving accuracy

The abstract from the paper is the following:

*The recent Segment Anything Model (SAM) represents a big leap in scaling up segmentation models, allowing for powerful zero-shot capabilities and flexible prompting. Despite being trained with 1.1 billion masks, SAM's mask prediction quality falls short in many cases, particularly when dealing with objects that have intricate structures. We propose HQ-SAM, equipping SAM with the ability to accurately segment any object, while maintaining SAM's original promptable design, efficiency, and zero-shot generalizability. Our careful design reuses and preserves the pre-trained model weights of SAM, while only introducing minimal additional parameters and computation. We design a learnable High-Quality Output Token, which is injected into SAM's mask decoder and is responsible for predicting the high-quality mask. Instead of only applying it on mask-decoder features, we first fuse them with early and final ViT features for improved mask details. To train our introduced learnable parameters, we compose a dataset of 44K fine-grained masks from several sources. HQ-SAM is only trained on the introduced dataset of 44k masks, which takes only 4 hours on 8 GPUs.*

Tips:

- SAM-HQ produces higher quality masks than the original SAM model, particularly for objects with intricate structures and fine details
- The model predicts binary masks with more accurate boundaries and better handling of thin structures
- Like SAM, the model performs better with input 2D points and/or input bounding boxes
- You can prompt multiple points for the same image and predict a single high-quality mask
- The model maintains SAM's zero-shot generalization capabilities
- SAM-HQ only adds ~0.5% additional parameters compared to SAM
- Fine-tuning the model is not supported yet

This model was contributed by [sushmanth](https://huggingface.co/sushmanth).
The original code can be found [here](https://github.com/SysCV/SAM-HQ).

Below is an example on how to run mask generation given an image and a 2D point:

```python
import torch
from PIL import Image
import requests
from transformers import SamHQModel, SamHQProcessor
from accelerate import Accelerator

device = Accelerator().device
model = SamHQModel.from_pretrained("syscv-community/sam-hq-vit-base").to(device)
processor = SamHQProcessor.from_pretrained("syscv-community/sam-hq-vit-base")

img_url = "https://huggingface.co/ybelkada/segment-anything/resolve/main/assets/car.png"
raw_image = Image.open(requests.get(img_url, stream=True).raw).convert("RGB")
input_points = [[[450, 600]]]  # 2D location of a window in the image

inputs = processor(raw_image, input_points=input_points, return_tensors="pt").to(model.device)
with torch.no_grad():
    outputs = model(**inputs)

masks = processor.image_processor.post_process_masks(
    outputs.pred_masks.cpu(), inputs["original_sizes"].cpu(), inputs["reshaped_input_sizes"].cpu()
)
scores = outputs.iou_scores
```

You can also process your own masks alongside the input images in the processor to be passed to the model:

```python
import torch
from PIL import Image
import requests
from transformers import SamHQModel, SamHQProcessor
from accelerate import Accelerator

device = Accelerator().device
model = SamHQModel.from_pretrained("syscv-community/sam-hq-vit-base").to(device)
processor = SamHQProcessor.from_pretrained("syscv-community/sam-hq-vit-base")

img_url = "https://huggingface.co/ybelkada/segment-anything/resolve/main/assets/car.png"
raw_image = Image.open(requests.get(img_url, stream=True).raw).convert("RGB")
mask_url = "https://huggingface.co/ybelkada/segment-anything/resolve/main/assets/car.png"
segmentation_map = Image.open(requests.get(mask_url, stream=True).raw).convert("1")
input_points = [[[450, 600]]]  # 2D location of a window in the image

inputs = processor(raw_image, input_points=input_points, segmentation_maps=segmentation_map, return_tensors="pt").to(model.device)
with torch.no_grad():
    outputs = model(**inputs)

masks = processor.image_processor.post_process_masks(
    outputs.pred_masks.cpu(), inputs["original_sizes"].cpu(), inputs["reshaped_input_sizes"].cpu()
)
scores = outputs.iou_scores
```

## Resources

A list of official Hugging Face and community (indicated by 🌎) resources to help you get started with SAM-HQ:

- Demo notebook for using the model (coming soon)
- Paper implementation and code: [SAM-HQ GitHub Repository](https://github.com/SysCV/SAM-HQ)

## SamHQConfig[[transformers.SamHQConfig]]

#### transformers.SamHQConfig[[transformers.SamHQConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam_hq/configuration_sam_hq.py#L259)

[SamHQConfig](/docs/transformers/v5.0.0rc1/en/model_doc/sam_hq#transformers.SamHQConfig) is the configuration class to store the configuration of a [SamHQModel](/docs/transformers/v5.0.0rc1/en/model_doc/sam_hq#transformers.SamHQModel). It is used to instantiate a
SAM-HQ model according to the specified arguments, defining the vision model, prompt-encoder model and mask decoder
configs. Instantiating a configuration with the defaults will yield a similar configuration to that of the
SAM-HQ-ViT-H [sushmanth/sam_hq_vit_h](https://huggingface.co/sushmanth/sam_hq_vit_h) architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

**Parameters:**

vision_config (Union[`dict`, `SamHQVisionConfig`], *optional*) : Dictionary of configuration options used to initialize [SamHQVisionConfig](/docs/transformers/v5.0.0rc1/en/model_doc/sam_hq#transformers.SamHQVisionConfig).

prompt_encoder_config (Union[`dict`, `SamHQPromptEncoderConfig`], *optional*) : Dictionary of configuration options used to initialize [SamHQPromptEncoderConfig](/docs/transformers/v5.0.0rc1/en/model_doc/sam_hq#transformers.SamHQPromptEncoderConfig).

mask_decoder_config (Union[`dict`, `SamHQMaskDecoderConfig`], *optional*) : Dictionary of configuration options used to initialize [SamHQMaskDecoderConfig](/docs/transformers/v5.0.0rc1/en/model_doc/sam_hq#transformers.SamHQMaskDecoderConfig).

kwargs (*optional*) : Dictionary of keyword arguments.

## SamHQVisionConfig[[transformers.SamHQVisionConfig]]

#### transformers.SamHQVisionConfig[[transformers.SamHQVisionConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam_hq/configuration_sam_hq.py#L75)

This is the configuration class to store the configuration of a [SamHQVisionModel](/docs/transformers/v5.0.0rc1/en/model_doc/sam_hq#transformers.SamHQVisionModel). It is used to instantiate a SAM_HQ
vision encoder according to the specified arguments, defining the model architecture. Instantiating a configuration
defaults will yield a similar configuration to that of the SAM_HQ ViT-h
[facebook/sam_hq-vit-huge](https://huggingface.co/facebook/sam_hq-vit-huge) architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:

```python
>>> from transformers import (
...     SamHQVisionConfig,
...     SamHQVisionModel,
... )

>>> # Initializing a SamHQVisionConfig with `"facebook/sam_hq-vit-huge"` style configuration
>>> configuration = SamHQVisionConfig()

>>> # Initializing a SamHQVisionModel (with random weights) from the `"facebook/sam_hq-vit-huge"` style configuration
>>> model = SamHQVisionModel(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

hidden_size (`int`, *optional*, defaults to 768) : Dimensionality of the encoder layers and the pooler layer.

output_channels (`int`, *optional*, defaults to 256) : Dimensionality of the output channels in the Patch Encoder.

num_hidden_layers (`int`, *optional*, defaults to 12) : Number of hidden layers in the Transformer encoder.

num_attention_heads (`int`, *optional*, defaults to 12) : Number of attention heads for each attention layer in the Transformer encoder.

num_channels (`int`, *optional*, defaults to 3) : Number of channels in the input image.

image_size (`int`, *optional*, defaults to 1024) : Expected resolution. Target size of the resized input image.

patch_size (`int`, *optional*, defaults to 16) : Size of the patches to be extracted from the input image.

hidden_act (`str`, *optional*, defaults to `"gelu"`) : The non-linear activation function (function or string)

layer_norm_eps (`float`, *optional*, defaults to 1e-06) : The epsilon used by the layer normalization layers.

attention_dropout (`float`, *optional*, defaults to 0.0) : The dropout ratio for the attention probabilities.

initializer_range (`float`, *optional*, defaults to 1e-10) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

qkv_bias (`bool`, *optional*, defaults to `True`) : Whether to add a bias to query, key, value projections.

mlp_ratio (`float`, *optional*, defaults to 4.0) : Ratio of mlp hidden dim to embedding dim.

use_abs_pos (`bool`, *optional*, defaults to `True`) : Whether to use absolute position embedding.

use_rel_pos (`bool`, *optional*, defaults to `True`) : Whether to use relative position embedding.

window_size (`int`, *optional*, defaults to 14) : Window size for relative position.

global_attn_indexes (`list[int]`, *optional*, defaults to `[2, 5, 8, 11]`) : The indexes of the global attention layers.

num_pos_feats (`int`, *optional*, defaults to 128) : The dimensionality of the position embedding.

mlp_dim (`int`, *optional*) : The dimensionality of the MLP layer in the Transformer encoder. If `None`, defaults to `mlp_ratio * hidden_size`.

## SamHQMaskDecoderConfig[[transformers.SamHQMaskDecoderConfig]]

#### transformers.SamHQMaskDecoderConfig[[transformers.SamHQMaskDecoderConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam_hq/configuration_sam_hq.py#L193)

This is the configuration class to store the configuration of a `SamHQMaskDecoder`. It is used to instantiate a SAM_HQ
mask decoder to the specified arguments, defining the model architecture. Instantiating a configuration defaults
will yield a similar configuration to that of the SAM_HQ-vit-h
[facebook/sam_hq-vit-huge](https://huggingface.co/facebook/sam_hq-vit-huge) architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

**Parameters:**

hidden_size (`int`, *optional*, defaults to 256) : Dimensionality of the hidden states.

hidden_act (`str`, *optional*, defaults to `"relu"`) : The non-linear activation function used inside the `SamHQMaskDecoder` module.

mlp_dim (`int`, *optional*, defaults to 2048) : Dimensionality of the "intermediate" (i.e., feed-forward) layer in the Transformer encoder.

num_hidden_layers (`int`, *optional*, defaults to 2) : Number of hidden layers in the Transformer encoder.

num_attention_heads (`int`, *optional*, defaults to 8) : Number of attention heads for each attention layer in the Transformer encoder.

attention_downsample_rate (`int`, *optional*, defaults to 2) : The downsampling rate of the attention layer.

num_multimask_outputs (`int`, *optional*, defaults to 3) : The number of outputs from the `SamHQMaskDecoder` module. In the Segment Anything paper, this is set to 3.

iou_head_depth (`int`, *optional*, defaults to 3) : The number of layers in the IoU head module.

iou_head_hidden_dim (`int`, *optional*, defaults to 256) : The dimensionality of the hidden states in the IoU head module.

layer_norm_eps (`float`, *optional*, defaults to 1e-06) : The epsilon used by the layer normalization layers.

vit_dim (`int`, *optional*, defaults to 768) : Dimensionality of the Vision Transformer (ViT) used in the `SamHQMaskDecoder` module.

## SamHQPromptEncoderConfig[[transformers.SamHQPromptEncoderConfig]]

#### transformers.SamHQPromptEncoderConfig[[transformers.SamHQPromptEncoderConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam_hq/configuration_sam_hq.py#L26)

This is the configuration class to store the configuration of a `SamHQPromptEncoderModel`.The `SamHQPromptEncoderModel`
module is used to encode the input 2D points and bounding boxes. Instantiating a configuration defaults will yield a
similar configuration to that of the SAM_HQ model. The configuration is used to store the configuration of the model.
[Uminosachi/sam-hq](https://huggingface.co/Uminosachi/sam-hq) architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model's output.Read the documentation from
[PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

**Parameters:**

hidden_size (`int`, *optional*, defaults to 256) : Dimensionality of the hidden states.

image_size (`int`, *optional*, defaults to 1024) : The expected output resolution of the image.

patch_size (`int`, *optional*, defaults to 16) : The size (resolution) of each patch.

mask_input_channels (`int`, *optional*, defaults to 16) : The number of channels to be fed to the `MaskDecoder` module.

num_point_embeddings (`int`, *optional*, defaults to 4) : The number of point embeddings to be used.

hidden_act (`str`, *optional*, defaults to `"gelu"`) : The non-linear activation function in the encoder and pooler.

## SamHQProcessor[[transformers.SamHQProcessor]]

#### transformers.SamHQProcessor[[transformers.SamHQProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam_hq/processing_samhq.py#L55)

Constructs a SAM HQ processor which wraps a SAM  image processor and an 2D points & Bounding boxes processor into a
single processor.

[SamHQProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/sam_hq#transformers.SamHQProcessor) offers all the functionalities of [SamImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/sam#transformers.SamImageProcessor). See the docstring of
`__call__()` for more information.

**Parameters:**

image_processor (`SamImageProcessor`) : An instance of [SamImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/sam#transformers.SamImageProcessor). The image processor is a required input.

## SamHQVisionModel[[transformers.SamHQVisionModel]]

#### transformers.SamHQVisionModel[[transformers.SamHQVisionModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam_hq/modeling_sam_hq.py#L1051)

The vision model from SamHQ without any head or projection on top.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.SamHQVisionModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam_hq/modeling_sam_hq.py#L1063[{"name": "pixel_values", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **pixel_values** (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`, *optional*) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [SamImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/sam#transformers.SamImageProcessor). See `SamImageProcessor.__call__()` for details ([SamHQProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/sam_hq#transformers.SamHQProcessor) uses
  [SamImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/sam#transformers.SamImageProcessor) for processing images).0`transformers.models.sam_hq.modeling_sam_hq.SamHQVisionEncoderOutput` or `tuple(torch.FloatTensor)`A `transformers.models.sam_hq.modeling_sam_hq.SamHQVisionEncoderOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([SamHQConfig](/docs/transformers/v5.0.0rc1/en/model_doc/sam_hq#transformers.SamHQConfig)) and inputs.

- **image_embeds** (`torch.FloatTensor` of shape `(batch_size, output_dim)` *optional* returned when model is initialized with `with_projection=True`) -- The image embeddings obtained by applying the projection layer to the pooler_output.
- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*, defaults to `None`) -- Sequence of hidden-states at the output of the last layer of the model.
- **hidden_states** (`tuple[torch.FloatTensor, ...]`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple[torch.FloatTensor, ...]`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
- **intermediate_embeddings** (`list(torch.FloatTensor)`, *optional*) -- A list of intermediate embeddings collected from certain blocks within the model, typically those without
  windowed attention. Each element in the list is of shape `(batch_size, sequence_length, hidden_size)`.
  This is specific to SAM-HQ and not present in base SAM.
The [SamHQVisionModel](/docs/transformers/v5.0.0rc1/en/model_doc/sam_hq#transformers.SamHQVisionModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

**Parameters:**

config ([SamHQVisionConfig](/docs/transformers/v5.0.0rc1/en/model_doc/sam_hq#transformers.SamHQVisionConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``transformers.models.sam_hq.modeling_sam_hq.SamHQVisionEncoderOutput` or `tuple(torch.FloatTensor)``

A `transformers.models.sam_hq.modeling_sam_hq.SamHQVisionEncoderOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([SamHQConfig](/docs/transformers/v5.0.0rc1/en/model_doc/sam_hq#transformers.SamHQConfig)) and inputs.

- **image_embeds** (`torch.FloatTensor` of shape `(batch_size, output_dim)` *optional* returned when model is initialized with `with_projection=True`) -- The image embeddings obtained by applying the projection layer to the pooler_output.
- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*, defaults to `None`) -- Sequence of hidden-states at the output of the last layer of the model.
- **hidden_states** (`tuple[torch.FloatTensor, ...]`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple[torch.FloatTensor, ...]`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
- **intermediate_embeddings** (`list(torch.FloatTensor)`, *optional*) -- A list of intermediate embeddings collected from certain blocks within the model, typically those without
  windowed attention. Each element in the list is of shape `(batch_size, sequence_length, hidden_size)`.
  This is specific to SAM-HQ and not present in base SAM.

## SamHQModel[[transformers.SamHQModel]]

#### transformers.SamHQModel[[transformers.SamHQModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam_hq/modeling_sam_hq.py#L1232)

Segment Anything Model HQ (SAM-HQ) for generating masks, given an input image and optional 2D location and bounding boxes.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.SamHQModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/sam_hq/modeling_sam_hq.py#L1314[{"name": "pixel_values", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "input_points", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "input_labels", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "input_boxes", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "input_masks", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "image_embeddings", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "multimask_output", "val": ": bool = True"}, {"name": "hq_token_only", "val": ": bool = False"}, {"name": "attention_similarity", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "target_embedding", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "intermediate_embeddings", "val": ": typing.Optional[list[torch.FloatTensor]] = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **pixel_values** (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`, *optional*) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [SamImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/sam#transformers.SamImageProcessor). See `SamImageProcessor.__call__()` for details ([SamHQProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/sam_hq#transformers.SamHQProcessor) uses
  [SamImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/sam#transformers.SamImageProcessor) for processing images).
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
  SAM_HQ model also accepts segmentation masks as input. The mask will be embedded by the prompt encoder to
  generate a corresponding embedding, that will be fed later on to the mask decoder. These masks needs to be
  manually fed by the user, and they need to be of shape (`batch_size`, `image_size`, `image_size`).
- **image_embeddings** (`torch.FloatTensor` of shape `(batch_size, output_channels, window_size, window_size)`) --
  Image embeddings, this is used by the mask decder to generate masks and iou scores. For more memory
  efficient computation, users can first retrieve the image embeddings using the `get_image_embeddings`
  method, and then feed them to the `forward` method instead of feeding the `pixel_values`.
- **multimask_output** (`bool`, *optional*) --
  In the original implementation and paper, the model always outputs 3 masks per image (or per point / per
  bounding box if relevant). However, it is possible to just output a single mask, that corresponds to the
  "best" mask, by specifying `multimask_output=False`.
- **hq_token_only** (`bool`, *optional*, defaults to `False`) --
  Whether to use only the HQ token path for mask generation. When False, combines both standard and HQ paths.
  This is specific to SAM-HQ's architecture.
- **attention_similarity** (`torch.FloatTensor`, *optional*) --
  Attention similarity tensor, to be provided to the mask decoder for target-guided attention in case the
  model is used for personalization as introduced in [PerSAM](https://huggingface.co/papers/2305.03048).
- **target_embedding** (`torch.FloatTensor`, *optional*) --
  Embedding of the target concept, to be provided to the mask decoder for target-semantic prompting in case
  the model is used for personalization as introduced in [PerSAM](https://huggingface.co/papers/2305.03048).
- **intermediate_embeddings** (`List[torch.FloatTensor]`, *optional*) --
  Intermediate embeddings from vision encoder's non-windowed blocks, used by SAM-HQ for enhanced mask quality.
  Required when providing pre-computed image_embeddings instead of pixel_values.0`list[dict[str, torch.Tensor]]`
The [SamHQModel](/docs/transformers/v5.0.0rc1/en/model_doc/sam_hq#transformers.SamHQModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Example:

```python
>>> from PIL import Image
>>> import requests
>>> from transformers import AutoModel, AutoProcessor

>>> model = AutoModel.from_pretrained("sushmanth/sam_hq_vit_b")
>>> processor = AutoProcessor.from_pretrained("sushmanth/sam_hq_vit_b")

>>> img_url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/model_doc/sam-car.png"
>>> raw_image = Image.open(requests.get(img_url, stream=True).raw).convert("RGB")
>>> input_points = [[[400, 650]]]  # 2D location of a window on the car
>>> inputs = processor(images=raw_image, input_points=input_points, return_tensors="pt")

>>> # Get high-quality segmentation mask
>>> outputs = model(**inputs)

>>> # For high-quality mask only
>>> outputs = model(**inputs, hq_token_only=True)

>>> # Postprocess masks
>>> masks = processor.post_process_masks(
...     outputs.pred_masks, inputs["original_sizes"], inputs["reshaped_input_sizes"]
... )
```

**Parameters:**

config ([SamHQModel](/docs/transformers/v5.0.0rc1/en/model_doc/sam_hq#transformers.SamHQModel)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

`list[dict[str, torch.Tensor]]`

