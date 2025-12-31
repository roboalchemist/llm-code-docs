# Source: https://huggingface.co/docs/transformers/v5.0.0rc1/model_doc/hiera.md

# Hiera

## Overview

Hiera was proposed in [Hiera: A Hierarchical Vision Transformer without the Bells-and-Whistles](https://huggingface.co/papers/2306.00989) by Chaitanya Ryali, Yuan-Ting Hu, Daniel Bolya, Chen Wei, Haoqi Fan, Po-Yao Huang, Vaibhav Aggarwal, Arkabandhu Chowdhury, Omid Poursaeed, Judy Hoffman, Jitendra Malik, Yanghao Li, Christoph Feichtenhofer

The paper introduces "Hiera," a hierarchical Vision Transformer that simplifies the architecture of modern hierarchical vision transformers by removing unnecessary components without compromising on accuracy or efficiency. Unlike traditional transformers that add complex vision-specific components to improve supervised classification performance, Hiera demonstrates that such additions, often termed "bells-and-whistles," are not essential for high accuracy. By leveraging a strong visual pretext task (MAE) for pretraining, Hiera retains simplicity and achieves superior accuracy and speed both in inference and training across various image and video recognition tasks. The approach suggests that spatial biases required for vision tasks can be effectively learned through proper pretraining, eliminating the need for added architectural complexity.

The abstract from the paper is the following:

*Modern hierarchical vision transformers have added several vision-specific components in the pursuit of supervised classification performance. While these components lead to effective accuracies and attractive FLOP counts, the added complexity actually makes these transformers slower than their vanilla ViT counterparts. In this paper, we argue that this additional bulk is unnecessary. By pretraining with a strong visual pretext task (MAE), we can strip out all the bells-and-whistles from a state-of-the-art multi-stage vision transformer without losing accuracy. In the process, we create Hiera, an extremely simple hierarchical vision transformer that is more accurate than previous models while being significantly faster both at inference and during training. We evaluate Hiera on a variety of tasks for image and video recognition. Our code and models are available at https://github.com/facebookresearch/hiera.*

 Hiera architecture. Taken from the original paper. 

This model was a joint contribution by [EduardoPacheco](https://huggingface.co/EduardoPacheco) and [namangarg110](https://huggingface.co/namangarg110). The original code can be found [here] (https://github.com/facebookresearch/hiera).

## Resources

A list of official Hugging Face and community (indicated by 🌎) resources to help you get started with Hiera. If you're interested in submitting a resource to be included here, please feel free to open a Pull Request and we'll review it! The resource should ideally demonstrate something new instead of duplicating an existing resource.

- [HieraForImageClassification](/docs/transformers/v5.0.0rc1/en/model_doc/hiera#transformers.HieraForImageClassification) is supported by this [example script](https://github.com/huggingface/transformers/tree/main/examples/pytorch/image-classification) and [notebook](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/image_classification.ipynb).
- See also: [Image classification task guide](../tasks/image_classification)

## HieraConfig[[transformers.HieraConfig]]

#### transformers.HieraConfig[[transformers.HieraConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/hiera/configuration_hiera.py#L25)

This is the configuration class to store the configuration of a [HieraModel](/docs/transformers/v5.0.0rc1/en/model_doc/hiera#transformers.HieraModel). It is used to instantiate a Hiera
model according to the specified arguments, defining the model architecture. Instantiating a configuration with the
defaults will yield a similar configuration to that of the Hiera
[facebook/hiera-base-224](https://huggingface.co/facebook/hiera-base-224) architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:

```python
>>> from transformers import HieraConfig, HieraModel

>>> # Initializing a Hiera hiera-base-patch16-224 style configuration
>>> configuration = HieraConfig()

>>> # Initializing a model (with random weights) from the hiera-base-patch16-224 style configuration
>>> model = HieraModel(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

embed_dim (`int`, *optional*, defaults to 96) : Dimensionality of patch embedding.

image_size (`list(int)`, *optional*, defaults to `[224, 224]`) : The size (resolution) of input in the format (height, width) for images and (frames, height, width) for videos.

patch_size (`list(int)`, *optional*, defaults to `[7, 7]`) : The size (resolution) of each patch.

patch_stride (`list(int)`, *optional*, defaults to `[4, 4]`) : The stride of the patch.

patch_padding (`list(int)`, *optional*, defaults to `[3, 3]`) : The padding of the patch.

mlp_ratio (`float`, *optional*, defaults to 4.0) : The ratio of mlp hidden dim to embedding dim.

depths (`list(int)`, *optional*, defaults to `[2, 3, 16, 3]`) : Depth of each layer in the Transformer encoder.

num_heads (`list(int)`, *optional*, defaults to `[1, 2, 4, 8]`) : Number of attention heads in each layer of the Transformer encoder.

embed_dim_multiplier (`float`, *optional*, defaults to 2.0) : The multiplier to the dimensionality of patch embedding in each layer of the Transformer encoder.

num_query_pool (`int`, *optional*, defaults to 3) : The number of query pool stages.

query_stride (`list(int)`, *optional*, defaults to `[2, 2]`) : The stride of the query pool.

masked_unit_size (`list(int)`, *optional*, defaults to `[8, 8]`) : The size of the masked unit.

masked_unit_attention (`list(bool)`, *optional*, defaults to `[True, True, False, False]`) : Whether to use masked unit attention in each layer of the Transformer encoder.

drop_path_rate (`float`, *optional*, defaults to 0.0) : The drop path rate.

num_channels (`int`, *optional*, defaults to 3) : The number of input channels.

hidden_act (`str`, *optional*, defaults to `"gelu"`) : The non-linear activation function (function or string) in the encoder. If string, `"gelu"`, `"relu"`, `"selu"` and `"gelu_new"` are supported.

initializer_range (`float`, *optional*, defaults to 0.02) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices and the zero_initializer for initializing all bias vectors.

layer_norm_init (`float`, *optional*, defaults to 1.0) : The initial weight value for layer normalization layers.

layer_norm_eps (`float`, *optional*, defaults to 1e-06) : The epsilon used by the layer normalization layers.

decoder_hidden_size (`int`, *optional*) : Dimensionality of decoder embeddings for MAE pretraining.

decoder_depth (`int`, *optional*) : Depth of the decoder for MAE pretraining.

decoder_num_heads (`int`, *optional*) : Number of attention heads in each layer of the decoder for MAE pretraining.

normalize_pixel_loss (`bool`, *optional*, defaults to `True`) : Whether to normalize the pixel loss by the number of pixels.

mask_ratio (`float`, *optional*, defaults to 0.6) : The ratio of masked tokens in the input.

out_features (`list[str]`, *optional*) : If used as backbone, list of features to output. Can be any of `"stem"`, `"stage1"`, `"stage2"`, etc. (depending on how many stages the model has). If unset and `out_indices` is set, will default to the corresponding stages. If unset and `out_indices` is unset, will default to the last stage. Must be in the same order as defined in the `stage_names` attribute.

out_indices (`list[int]`, *optional*) : If used as backbone, list of indices of features to output. Can be any of 0, 1, 2, etc. (depending on how many stages the model has). If unset and `out_features` is set, will default to the corresponding stages. If unset and `out_features` is unset, will default to the last stage. Must be in the same order as defined in the `stage_names` attribute.

## HieraModel[[transformers.HieraModel]]

#### transformers.HieraModel[[transformers.HieraModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/hiera/modeling_hiera.py#L818)

The bare Hiera Model outputting raw hidden-states without any specific head on top.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.HieraModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/hiera/modeling_hiera.py#L842[{"name": "pixel_values", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "noise", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "output_attentions", "val": ": typing.Optional[bool] = None"}, {"name": "output_hidden_states", "val": ": typing.Optional[bool] = None"}, {"name": "interpolate_pos_encoding", "val": ": typing.Optional[bool] = None"}, {"name": "return_dict", "val": ": typing.Optional[bool] = None"}, {"name": "**kwargs", "val": ""}]- **pixel_values** (`torch.Tensor` of shape `(batch_size, num_channels, image_size, image_size)`, *optional*) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [BitImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/bit#transformers.BitImageProcessor). See [BitImageProcessor.__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details (`processor_class` uses
  [BitImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/bit#transformers.BitImageProcessor) for processing images).
- **noise** (`torch.FloatTensor` of shape `(batch_size, num_mask_units)`, *optional*) --
  Mainly used for testing purposes to control randomness and maintain the reproducibility
- **output_attentions** (`bool`, *optional*) --
  Whether or not to return the attentions tensors of all attention layers. See `attentions` under returned
  tensors for more detail.
- **output_hidden_states** (`bool`, *optional*) --
  Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
  more detail.
- **interpolate_pos_encoding** (`bool`, *optional*) --
  Whether to interpolate the pre-trained position encodings.
- **return_dict** (`bool`, *optional*) --
  Whether or not to return a [ModelOutput](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.utils.ModelOutput) instead of a plain tuple.0[transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)`A [transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([HieraConfig](/docs/transformers/v5.0.0rc1/en/model_doc/hiera#transformers.HieraConfig)) and inputs.

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
The [HieraModel](/docs/transformers/v5.0.0rc1/en/model_doc/hiera#transformers.HieraModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Example:

```python
```

**Parameters:**

config ([HieraConfig](/docs/transformers/v5.0.0rc1/en/model_doc/hiera#transformers.HieraConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

add_pooling_layer (`bool`, *optional*, defaults to `True`) : Whether or not to apply pooling layer.

is_mae (`bool`, *optional*, defaults to `False`) : Whether or not to run the model on MAE mode.

**Returns:**

`[transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([HieraConfig](/docs/transformers/v5.0.0rc1/en/model_doc/hiera#transformers.HieraConfig)) and inputs.

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

## HieraForPreTraining[[transformers.HieraForPreTraining]]

#### transformers.HieraForPreTraining[[transformers.HieraForPreTraining]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/hiera/modeling_hiera.py#L1086)

The Hiera Model transformer with the decoder on top for self-supervised pre-training.

Note that we provide a script to pre-train this model on custom data in our [examples
directory](https://github.com/huggingface/transformers/tree/main/examples/pytorch/image-pretraining).

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.HieraForPreTraining.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/hiera/modeling_hiera.py#L1127[{"name": "pixel_values", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "noise", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "output_attentions", "val": ": typing.Optional[bool] = None"}, {"name": "output_hidden_states", "val": ": typing.Optional[bool] = None"}, {"name": "interpolate_pos_encoding", "val": ": typing.Optional[bool] = None"}, {"name": "return_dict", "val": ": typing.Optional[bool] = None"}, {"name": "**kwargs", "val": ""}]- **pixel_values** (`torch.Tensor` of shape `(batch_size, num_channels, image_size, image_size)`, *optional*) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [BitImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/bit#transformers.BitImageProcessor). See [BitImageProcessor.__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details (`processor_class` uses
  [BitImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/bit#transformers.BitImageProcessor) for processing images).
- **noise** (`torch.FloatTensor` of shape `(batch_size, num_mask_units)`, *optional*) --
  Mainly used for testing purposes to control randomness and maintain the reproducibility
- **output_attentions** (`bool`, *optional*) --
  Whether or not to return the attentions tensors of all attention layers. See `attentions` under returned
  tensors for more detail.
- **output_hidden_states** (`bool`, *optional*) --
  Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
  more detail.
- **interpolate_pos_encoding** (`bool`, *optional*) --
  Whether to interpolate the pre-trained position encodings.
- **return_dict** (`bool`, *optional*) --
  Whether or not to return a [ModelOutput](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.utils.ModelOutput) instead of a plain tuple.0`transformers.models.hiera.modeling_hiera.HieraForPreTrainingOutput` or `tuple(torch.FloatTensor)`A `transformers.models.hiera.modeling_hiera.HieraForPreTrainingOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([HieraConfig](/docs/transformers/v5.0.0rc1/en/model_doc/hiera#transformers.HieraConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`) -- Pixel reconstruction loss.
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, patch_size ** 2 * num_channels)`) -- Pixel reconstruction logits.
- **bool_masked_pos** (`torch.BoolTensor` of shape `(batch_size, sequence_length)`) -- Tensor indicating which patches are masked (0) and which are not (1).
- **ids_restore** (`torch.LongTensor` of shape `(batch_size, sequence_length)`) -- Tensor containing the original index of the (shuffled) masked patches.
- **hidden_states** (`tuple[torch.FloatTensor]`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple[torch.FloatTensor]`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
- **reshaped_hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
  shape `(batch_size, height, width, hidden_size)`. Hidden-states of the model at the output of each layer
  plus the initial embedding outputs reshaped to include the spatial dimensions.
The [HieraForPreTraining](/docs/transformers/v5.0.0rc1/en/model_doc/hiera#transformers.HieraForPreTraining) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Examples:
```python
>>> from transformers import AutoImageProcessor, HieraForPreTraining
>>> import torch
>>> from PIL import Image
>>> import requests

>>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
>>> image = Image.open(requests.get(url, stream=True).raw)

>>> image_processor = AutoImageProcessor.from_pretrained("facebook/hiera-tiny-224-mae-hf")
>>> model = HieraForPreTraining.from_pretrained("facebook/hiera-tiny-224-mae-hf")

>>> inputs = image_processor(images=image, return_tensors="pt")

>>> outputs = model(**inputs)
>>> logits = outputs.logits
>>> loss = outputs.loss
>>> print(list(logits.shape))
[1, 196, 768]
```

**Parameters:**

config ([HieraConfig](/docs/transformers/v5.0.0rc1/en/model_doc/hiera#transformers.HieraConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``transformers.models.hiera.modeling_hiera.HieraForPreTrainingOutput` or `tuple(torch.FloatTensor)``

A `transformers.models.hiera.modeling_hiera.HieraForPreTrainingOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([HieraConfig](/docs/transformers/v5.0.0rc1/en/model_doc/hiera#transformers.HieraConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`) -- Pixel reconstruction loss.
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, patch_size ** 2 * num_channels)`) -- Pixel reconstruction logits.
- **bool_masked_pos** (`torch.BoolTensor` of shape `(batch_size, sequence_length)`) -- Tensor indicating which patches are masked (0) and which are not (1).
- **ids_restore** (`torch.LongTensor` of shape `(batch_size, sequence_length)`) -- Tensor containing the original index of the (shuffled) masked patches.
- **hidden_states** (`tuple[torch.FloatTensor]`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple[torch.FloatTensor]`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
- **reshaped_hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
  shape `(batch_size, height, width, hidden_size)`. Hidden-states of the model at the output of each layer
  plus the initial embedding outputs reshaped to include the spatial dimensions.

## HieraForImageClassification[[transformers.HieraForImageClassification]]

#### transformers.HieraForImageClassification[[transformers.HieraForImageClassification]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/hiera/modeling_hiera.py#L1230)

Hiera Model transformer with an image classification head on top (a linear layer on top of the final hidden state with
average pooling) e.g. for ImageNet.

Note that it's possible to fine-tune Hiera on higher resolution images than the ones it has been trained on, by
setting `interpolate_pos_encoding` to `True` in the forward of the model. This will interpolate the pre-trained
position embeddings to the higher resolution.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.HieraForImageClassification.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/hiera/modeling_hiera.py#L1245[{"name": "pixel_values", "val": ""}, {"name": "labels", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "output_attentions", "val": ": typing.Optional[bool] = None"}, {"name": "output_hidden_states", "val": ": typing.Optional[bool] = None"}, {"name": "interpolate_pos_encoding", "val": ": typing.Optional[bool] = None"}, {"name": "return_dict", "val": ": typing.Optional[bool] = None"}, {"name": "**kwargs", "val": ""}]- **pixel_values** (`` of shape `(batch_size, num_channels, image_size, image_size)`) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [BitImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/bit#transformers.BitImageProcessor). See [BitImageProcessor.__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details (`processor_class` uses
  [BitImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/bit#transformers.BitImageProcessor) for processing images).
- **labels** (`torch.LongTensor` of shape `(batch_size,)`, *optional*) --
  Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
  config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
  `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
- **output_attentions** (`bool`, *optional*) --
  Whether or not to return the attentions tensors of all attention layers. See `attentions` under returned
  tensors for more detail.
- **output_hidden_states** (`bool`, *optional*) --
  Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
  more detail.
- **interpolate_pos_encoding** (`bool`, *optional*) --
  Whether to interpolate the pre-trained position encodings.
- **return_dict** (`bool`, *optional*) --
  Whether or not to return a [ModelOutput](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.utils.ModelOutput) instead of a plain tuple.0`transformers.models.hiera.modeling_hiera.HieraForImageClassificationOutput` or `tuple(torch.FloatTensor)`A `transformers.models.hiera.modeling_hiera.HieraForImageClassificationOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([HieraConfig](/docs/transformers/v5.0.0rc1/en/model_doc/hiera#transformers.HieraConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, `optional`) -- Loss value for the training task.
- **logits** (`torch.FloatTensor` of shape `(batch_size, num_labels)`) -- Prediction scores of the classification head (logits of the output layer).
- **hidden_states** (`tuple(torch.FloatTensor)`, `optional`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each stage) of
  shape `(batch_size, sequence_length, hidden_size)`. These are the unrolled hidden states of the model.

  Hidden-states of the model at the output of each layer plus the initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, `optional`) -- Tuple of `torch.FloatTensor` (one for each stage) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
- **loss** (`torch.FloatTensor` of shape `(1,)`, `optional`) -- Loss value for the training task.
- **logits** (`torch.FloatTensor` of shape `(batch_size, num_labels)`) -- Prediction scores of the classification head (logits of the output layer).
- **hidden_states** (`tuple(torch.FloatTensor)`, `optional`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each stage) of
  shape `(batch_size, sequence_length, hidden_size)`. These are the unrolled hidden states of the model.

  Hidden-states of the model at the output of each layer plus the initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, `optional`) -- Tuple of `torch.FloatTensor` (one for each stage) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
- **reshaped_hidden_states** (`tuple(torch.FloatTensor)`, `optional`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each stage) of
  shape `(batch_size, height, width, hidden_size)`. These are the reshaped and re-rolled hidden states of the model.

  Hidden-states of the model at the output of each layer plus the initial embedding outputs reshaped to
  include the spatial dimensions.
The [HieraForImageClassification](/docs/transformers/v5.0.0rc1/en/model_doc/hiera#transformers.HieraForImageClassification) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Example:

```python
>>> from transformers import AutoImageProcessor, HieraForImageClassification
>>> import torch
>>> from datasets import load_dataset

>>> dataset = load_dataset("huggingface/cats-image")
>>> image = dataset["test"]["image"][0]

>>> image_processor = AutoImageProcessor.from_pretrained("facebook/hiera-base-224")
>>> model = HieraForImageClassification.from_pretrained("facebook/hiera-base-224")

>>> inputs = image_processor(image, return_tensors="pt")

>>> with torch.no_grad():
...     logits = model(**inputs).logits

>>> # model predicts one of the 1000 ImageNet classes
>>> predicted_label = logits.argmax(-1).item()
>>> print(model.config.id2label[predicted_label])
...
```

**Parameters:**

config ([HieraConfig](/docs/transformers/v5.0.0rc1/en/model_doc/hiera#transformers.HieraConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``transformers.models.hiera.modeling_hiera.HieraForImageClassificationOutput` or `tuple(torch.FloatTensor)``

A `transformers.models.hiera.modeling_hiera.HieraForImageClassificationOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([HieraConfig](/docs/transformers/v5.0.0rc1/en/model_doc/hiera#transformers.HieraConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, `optional`) -- Loss value for the training task.
- **logits** (`torch.FloatTensor` of shape `(batch_size, num_labels)`) -- Prediction scores of the classification head (logits of the output layer).
- **hidden_states** (`tuple(torch.FloatTensor)`, `optional`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each stage) of
  shape `(batch_size, sequence_length, hidden_size)`. These are the unrolled hidden states of the model.

  Hidden-states of the model at the output of each layer plus the initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, `optional`) -- Tuple of `torch.FloatTensor` (one for each stage) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
- **loss** (`torch.FloatTensor` of shape `(1,)`, `optional`) -- Loss value for the training task.
- **logits** (`torch.FloatTensor` of shape `(batch_size, num_labels)`) -- Prediction scores of the classification head (logits of the output layer).
- **hidden_states** (`tuple(torch.FloatTensor)`, `optional`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each stage) of
  shape `(batch_size, sequence_length, hidden_size)`. These are the unrolled hidden states of the model.

  Hidden-states of the model at the output of each layer plus the initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, `optional`) -- Tuple of `torch.FloatTensor` (one for each stage) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
- **reshaped_hidden_states** (`tuple(torch.FloatTensor)`, `optional`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each stage) of
  shape `(batch_size, height, width, hidden_size)`. These are the reshaped and re-rolled hidden states of the model.

  Hidden-states of the model at the output of each layer plus the initial embedding outputs reshaped to
  include the spatial dimensions.

