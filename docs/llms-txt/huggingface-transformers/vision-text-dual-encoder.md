# Source: https://huggingface.co/docs/transformers/v5.0.0/model_doc/vision-text-dual-encoder.md

# VisionTextDualEncoder

## Overview

The [VisionTextDualEncoderModel](/docs/transformers/v5.0.0/en/model_doc/vision-text-dual-encoder#transformers.VisionTextDualEncoderModel) can be used to initialize a vision-text dual encoder model with
any pretrained vision autoencoding model as the vision encoder (*e.g.* [ViT](vit), [BEiT](beit), [DeiT](deit)) and any pretrained text autoencoding model as the text encoder (*e.g.* [RoBERTa](roberta), [BERT](bert)). Two projection layers are added on top of both the vision and text encoder to project the output embeddings
to a shared latent space. The projection layers are randomly initialized so the model should be fine-tuned on a
downstream task. This model can be used to align the vision-text embeddings using CLIP like contrastive image-text
training and then can be used for zero-shot vision tasks such image-classification or retrieval.

In [LiT: Zero-Shot Transfer with Locked-image Text Tuning](https://huggingface.co/papers/2111.07991) it is shown how
leveraging pre-trained (locked/frozen) image and text model for contrastive learning yields significant improvement on
new zero-shot vision tasks such as image classification or retrieval.

## VisionTextDualEncoderConfig[[transformers.VisionTextDualEncoderConfig]]

#### transformers.VisionTextDualEncoderConfig[[transformers.VisionTextDualEncoderConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/vision_text_dual_encoder/configuration_vision_text_dual_encoder.py#L33)

[VisionTextDualEncoderConfig](/docs/transformers/v5.0.0/en/model_doc/vision-text-dual-encoder#transformers.VisionTextDualEncoderConfig) is the configuration class to store the configuration of a
[VisionTextDualEncoderModel](/docs/transformers/v5.0.0/en/model_doc/vision-text-dual-encoder#transformers.VisionTextDualEncoderModel). It is used to instantiate [VisionTextDualEncoderModel](/docs/transformers/v5.0.0/en/model_doc/vision-text-dual-encoder#transformers.VisionTextDualEncoderModel) model according to the
specified arguments, defining the text model and vision model configs.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Examples:

```python
>>> from transformers import ViTConfig, BertConfig, VisionTextDualEncoderConfig, VisionTextDualEncoderModel

>>> # Initializing a BERT and ViT configuration
>>> config_vision = ViTConfig()
>>> config_text = BertConfig()

>>> config = VisionTextDualEncoderConfig.from_vision_text_configs(config_vision, config_text, projection_dim=512)

>>> # Initializing a BERT and ViT model (with random weights)
>>> model = VisionTextDualEncoderModel(config=config)

>>> # Accessing the model configuration
>>> config_vision = model.config.vision_config
>>> config_text = model.config.text_config

>>> # Saving the model, including its configuration
>>> model.save_pretrained("vit-bert")

>>> # loading model and config from pretrained folder
>>> vision_text_config = VisionTextDualEncoderConfig.from_pretrained("vit-bert")
>>> model = VisionTextDualEncoderModel.from_pretrained("vit-bert", config=vision_text_config)
```

from_vision_text_configstransformers.VisionTextDualEncoderConfig.from_vision_text_configshttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/vision_text_dual_encoder/configuration_vision_text_dual_encoder.py#L108[{"name": "vision_config", "val": ": PreTrainedConfig"}, {"name": "text_config", "val": ": PreTrainedConfig"}, {"name": "**kwargs", "val": ""}][VisionTextDualEncoderConfig](/docs/transformers/v5.0.0/en/model_doc/vision-text-dual-encoder#transformers.VisionTextDualEncoderConfig)An instance of a configuration object

Instantiate a [VisionTextDualEncoderConfig](/docs/transformers/v5.0.0/en/model_doc/vision-text-dual-encoder#transformers.VisionTextDualEncoderConfig) (or a derived class) from text model configuration and vision
model configuration.

**Parameters:**

projection_dim (`int`, *optional*, defaults to 512) : Dimensionality of text and vision projection layers.

logit_scale_init_value (`float`, *optional*, defaults to 2.6592) : The initial value of the *logit_scale* parameter. Default is used as per the original CLIP implementation.

kwargs (*optional*) : Dictionary of keyword arguments.

**Returns:**

`[VisionTextDualEncoderConfig](/docs/transformers/v5.0.0/en/model_doc/vision-text-dual-encoder#transformers.VisionTextDualEncoderConfig)`

An instance of a configuration object

## VisionTextDualEncoderProcessor[[transformers.VisionTextDualEncoderProcessor]]

#### transformers.VisionTextDualEncoderProcessor[[transformers.VisionTextDualEncoderProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/vision_text_dual_encoder/processing_vision_text_dual_encoder.py#L27)

Constructs a VisionTextDualEncoderProcessor which wraps a image processor and a tokenizer into a single processor.

[VisionTextDualEncoderProcessor](/docs/transformers/v5.0.0/en/model_doc/vision-text-dual-encoder#transformers.VisionTextDualEncoderProcessor) offers all the functionalities of `image_processor_class` and `tokenizer_class`. See the
`~image_processor_class` and `~tokenizer_class` for more information.

__call__transformers.VisionTextDualEncoderProcessor.__call__https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/processing_utils.py#L617[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor'], NoneType] = None"}, {"name": "text", "val": ": str | list[str] | list[list[str]] | None = None"}, {"name": "videos", "val": ": typing.Union[list['PIL.Image.Image'], numpy.ndarray, ForwardRef('torch.Tensor'), list[numpy.ndarray], list['torch.Tensor'], list[list['PIL.Image.Image']], list[list[numpy.ndarray]], list[list['torch.Tensor']], transformers.video_utils.URL, list[transformers.video_utils.URL], list[list[transformers.video_utils.URL]], transformers.video_utils.Path, list[transformers.video_utils.Path], list[list[transformers.video_utils.Path]], NoneType] = None"}, {"name": "audio", "val": ": typing.Union[numpy.ndarray, ForwardRef('torch.Tensor'), collections.abc.Sequence[numpy.ndarray], collections.abc.Sequence['torch.Tensor'], NoneType] = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.processing_utils.ProcessingKwargs]"}]- **images** (`PIL.Image.Image`, `np.ndarray`, `torch.Tensor`, `list[PIL.Image.Image]`, `list[np.ndarray]`, `list[torch.Tensor]`) --
  The image or batch of images to be prepared. Each image can be a PIL image, NumPy array or PyTorch
  tensor. Both channels-first and channels-last formats are supported.
- **text** (`TextInput`, `PreTokenizedInput`, `list[TextInput]`, `list[PreTokenizedInput]`, *optional*) --
  The sequence or batch of sequences to be encoded. Each sequence can be a string or a list of strings
  (pretokenized string). If the sequences are provided as list of strings (pretokenized), you must set
  `is_split_into_words=True` (to lift the ambiguity with a batch of sequences).
- **videos** (`np.ndarray`, `torch.Tensor`, `List[np.ndarray]`, `List[torch.Tensor]`) --
  The video or batch of videos to be prepared. Each video can be a 4D NumPy array or PyTorch
  tensor, or a nested list of 3D frames. Both channels-first and channels-last formats are supported.
- **audio** (`np.ndarray`, `torch.Tensor`, `list[np.ndarray]`, `list[torch.Tensor]`) --
  The audio or batch of audio to be prepared. Each audio can be a NumPy array or PyTorch
  tensor.
- **return_tensors** (`str` or [TensorType](/docs/transformers/v5.0.0/en/internal/file_utils#transformers.TensorType), *optional*) --
  If set, will return tensors of a particular framework. Acceptable values are:

  - `'pt'`: Return PyTorch `torch.Tensor` objects.
  - `'np'`: Return NumPy `np.ndarray` objects.0[BatchFeature](/docs/transformers/v5.0.0/en/main_classes/image_processor#transformers.BatchFeature)A [BatchFeature](/docs/transformers/v5.0.0/en/main_classes/image_processor#transformers.BatchFeature) object with processed inputs in a dict format.

Main method to prepare for model inputs. This method forwards the each modality argument to its own processor
along with `kwargs`. Please refer to the docstring of the each processor attributes for more information.

**Parameters:**

image_processor (`image_processor_class`) : The image processor is a required input.

tokenizer (`tokenizer_class`) : The tokenizer is a required input.

**Returns:**

`[BatchFeature](/docs/transformers/v5.0.0/en/main_classes/image_processor#transformers.BatchFeature)`

A [BatchFeature](/docs/transformers/v5.0.0/en/main_classes/image_processor#transformers.BatchFeature) object with processed inputs in a dict format.

## VisionTextDualEncoderModel[[transformers.VisionTextDualEncoderModel]]

#### transformers.VisionTextDualEncoderModel[[transformers.VisionTextDualEncoderModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/vision_text_dual_encoder/modeling_vision_text_dual_encoder.py#L45)

The bare Vision Text Dual Encoder Model outputting raw hidden-states without any specific head on top.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.VisionTextDualEncoderModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/vision_text_dual_encoder/modeling_vision_text_dual_encoder.py#L171[{"name": "input_ids", "val": ": torch.LongTensor | None = None"}, {"name": "pixel_values", "val": ": torch.FloatTensor | None = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.LongTensor | None = None"}, {"name": "return_loss", "val": ": bool | None = None"}, {"name": "token_type_ids", "val": ": torch.LongTensor | None = None"}, {"name": "output_attentions", "val": ": bool | None = None"}, {"name": "output_hidden_states", "val": ": bool | None = None"}, {"name": "return_dict", "val": ": bool | None = None"}, {"name": "**kwargs", "val": ""}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **pixel_values** (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`, *optional*) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  `image_processor_class`. See `image_processor_class.__call__` for details ([VisionTextDualEncoderProcessor](/docs/transformers/v5.0.0/en/model_doc/vision-text-dual-encoder#transformers.VisionTextDualEncoderProcessor) uses
  `image_processor_class` for processing images).
- **attention_mask** (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.

  [What are attention masks?](../glossary#attention-mask)
- **position_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of positions of each input sequence tokens in the position embeddings. Selected in the range `[0, config.n_positions - 1]`.

  [What are position IDs?](../glossary#position-ids)
- **return_loss** (`bool`, *optional*) --
  Whether or not to return the contrastive loss.
- **token_type_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Segment token indices to indicate first and second portions of the inputs. Indices are selected in `[0, 1]`:

  - 0 corresponds to a *sentence A* token,
  - 1 corresponds to a *sentence B* token.

  [What are token type IDs?](../glossary#token-type-ids)
- **output_attentions** (`bool`, *optional*) --
  Whether or not to return the attentions tensors of all attention layers. See `attentions` under returned
  tensors for more detail.
- **output_hidden_states** (`bool`, *optional*) --
  Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
  more detail.
- **return_dict** (`bool`, *optional*) --
  Whether or not to return a [ModelOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.utils.ModelOutput) instead of a plain tuple.0`transformers.models.clip.modeling_clip.CLIPOutput` or `tuple(torch.FloatTensor)`A `transformers.models.clip.modeling_clip.CLIPOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([VisionTextDualEncoderConfig](/docs/transformers/v5.0.0/en/model_doc/vision-text-dual-encoder#transformers.VisionTextDualEncoderConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `return_loss` is `True`) -- Contrastive loss for image-text similarity.
- **logits_per_image** (`torch.FloatTensor` of shape `(image_batch_size, text_batch_size)`) -- The scaled dot product scores between `image_embeds` and `text_embeds`. This represents the image-text
  similarity scores.
- **logits_per_text** (`torch.FloatTensor` of shape `(text_batch_size, image_batch_size)`) -- The scaled dot product scores between `text_embeds` and `image_embeds`. This represents the text-image
  similarity scores.
- **text_embeds** (`torch.FloatTensor` of shape `(batch_size, output_dim`) -- The text embeddings obtained by applying the projection layer to the pooled output of [CLIPTextModel](/docs/transformers/v5.0.0/en/model_doc/clip#transformers.CLIPTextModel).
- **image_embeds** (`torch.FloatTensor` of shape `(batch_size, output_dim`) -- The image embeddings obtained by applying the projection layer to the pooled output of [CLIPVisionModel](/docs/transformers/v5.0.0/en/model_doc/clip#transformers.CLIPVisionModel).
- **text_model_output** (`.text_model_output`, defaults to `None`) -- The output of the [CLIPTextModel](/docs/transformers/v5.0.0/en/model_doc/clip#transformers.CLIPTextModel).
- **vision_model_output** (`.vision_model_output`, defaults to `None`) -- The output of the [CLIPVisionModel](/docs/transformers/v5.0.0/en/model_doc/clip#transformers.CLIPVisionModel).
The [VisionTextDualEncoderModel](/docs/transformers/v5.0.0/en/model_doc/vision-text-dual-encoder#transformers.VisionTextDualEncoderModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Examples:

```python
>>> from PIL import Image
>>> import httpx
>>> from io import BytesIO
>>> from transformers import (
...     VisionTextDualEncoderModel,
...     VisionTextDualEncoderProcessor,
...     AutoImageProcessor,
...     AutoTokenizer,
... )

>>> tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-uncased")
>>> image_processor = AutoImageProcessor.from_pretrained("google/vit-base-patch16-224")
>>> processor = VisionTextDualEncoderProcessor(image_processor, tokenizer)
>>> model = VisionTextDualEncoderModel.from_vision_text_pretrained(
...     "google/vit-base-patch16-224", "google-bert/bert-base-uncased"
... )

>>> # contrastive training
>>> urls = [
...     "http://images.cocodataset.org/val2017/000000039769.jpg",
...     "https://farm3.staticflickr.com/2674/5850229113_4fe05d5265_z.jpg",
... ]
>>> with httpx.stream("GET", urls[0]) as response:
...     image1 = Image.open(BytesIO(response.read()))

>>> with httpx.stream("GET", urls[1]) as response:
...     image2 = Image.open(BytesIO(response.read()))

>>> images = [image1, image2]

>>> inputs = processor(
...     text=["a photo of a cat", "a photo of a dog"], images=images, return_tensors="pt", padding=True
... )
>>> outputs = model(
...     input_ids=inputs.input_ids,
...     attention_mask=inputs.attention_mask,
...     pixel_values=inputs.pixel_values,
...     return_loss=True,
... )
>>> loss, logits_per_image = outputs.loss, outputs.logits_per_image  # this is the image-text similarity score

>>> # save and load from pretrained
>>> model.save_pretrained("vit-bert")
>>> model = VisionTextDualEncoderModel.from_pretrained("vit-bert")

>>> # inference
>>> outputs = model(**inputs)
>>> logits_per_image = outputs.logits_per_image  # this is the image-text similarity score
>>> probs = logits_per_image.softmax(dim=1)  # we can take the softmax to get the label probabilities
```

**Parameters:**

config ([VisionTextDualEncoderConfig](/docs/transformers/v5.0.0/en/model_doc/vision-text-dual-encoder#transformers.VisionTextDualEncoderConfig), *optional*) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

vision_model (`~modeling_utils.PreTrainedModel`, *optional*) : The vision model to use.

text_model (`~modeling_utils.PreTrainedModel`, *optional*) : The text model to use.

**Returns:**

``transformers.models.clip.modeling_clip.CLIPOutput` or `tuple(torch.FloatTensor)``

A `transformers.models.clip.modeling_clip.CLIPOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([VisionTextDualEncoderConfig](/docs/transformers/v5.0.0/en/model_doc/vision-text-dual-encoder#transformers.VisionTextDualEncoderConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `return_loss` is `True`) -- Contrastive loss for image-text similarity.
- **logits_per_image** (`torch.FloatTensor` of shape `(image_batch_size, text_batch_size)`) -- The scaled dot product scores between `image_embeds` and `text_embeds`. This represents the image-text
  similarity scores.
- **logits_per_text** (`torch.FloatTensor` of shape `(text_batch_size, image_batch_size)`) -- The scaled dot product scores between `text_embeds` and `image_embeds`. This represents the text-image
  similarity scores.
- **text_embeds** (`torch.FloatTensor` of shape `(batch_size, output_dim`) -- The text embeddings obtained by applying the projection layer to the pooled output of [CLIPTextModel](/docs/transformers/v5.0.0/en/model_doc/clip#transformers.CLIPTextModel).
- **image_embeds** (`torch.FloatTensor` of shape `(batch_size, output_dim`) -- The image embeddings obtained by applying the projection layer to the pooled output of [CLIPVisionModel](/docs/transformers/v5.0.0/en/model_doc/clip#transformers.CLIPVisionModel).
- **text_model_output** (`.text_model_output`, defaults to `None`) -- The output of the [CLIPTextModel](/docs/transformers/v5.0.0/en/model_doc/clip#transformers.CLIPTextModel).
- **vision_model_output** (`.vision_model_output`, defaults to `None`) -- The output of the [CLIPVisionModel](/docs/transformers/v5.0.0/en/model_doc/clip#transformers.CLIPVisionModel).
#### get_text_features[[transformers.VisionTextDualEncoderModel.get_text_features]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/vision_text_dual_encoder/modeling_vision_text_dual_encoder.py#L105)

Examples:

```python
>>> import torch
>>> from transformers import VisionTextDualEncoderModel, AutoTokenizer

>>> model = VisionTextDualEncoderModel.from_pretrained("clip-italian/clip-italian")
>>> tokenizer = AutoTokenizer.from_pretrained("clip-italian/clip-italian")

>>> inputs = tokenizer(["una foto di un gatto", "una foto di un cane"], padding=True, return_tensors="pt")
>>> with torch.inference_mode():
...     text_features = model.get_text_features(**inputs)
```

**Parameters:**

input_ids (`torch.Tensor` of shape `(batch_size, sequence_length)`) : Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.  [What are input IDs?](../glossary#input-ids)

attention_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) : Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:  - 1 for tokens that are **not masked**, - 0 for tokens that are **masked**.  [What are attention masks?](../glossary#attention-mask)

position_ids (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) : Indices of positions of each input sequence tokens in the position embeddings. Selected in the range `[0, config.n_positions - 1]`.  [What are position IDs?](../glossary#position-ids)

token_type_ids (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) : Segment token indices to indicate first and second portions of the inputs. Indices are selected in `[0, 1]`:  - 0 corresponds to a *sentence A* token, - 1 corresponds to a *sentence B* token.  [What are token type IDs?](../glossary#token-type-ids)

**Returns:**

`[transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([VisionTextDualEncoderConfig](/docs/transformers/v5.0.0/en/model_doc/vision-text-dual-encoder#transformers.VisionTextDualEncoderConfig)) and inputs.

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
#### get_image_features[[transformers.VisionTextDualEncoderModel.get_image_features]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/vision_text_dual_encoder/modeling_vision_text_dual_encoder.py#L142)

Examples:

```python
>>> import torch
>>> from transformers import VisionTextDualEncoderModel, AutoImageProcessor
>>> from transformers.image_utils import load_image

>>> model = VisionTextDualEncoderModel.from_pretrained("clip-italian/clip-italian")
>>> image_processor = AutoImageProcessor.from_pretrained("google/vit-base-patch16-224")

>>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
>>> image = load_image(url)

>>> inputs = image_processor(images=image, return_tensors="pt")

>>> with torch.inference_mode():
...     image_features = model.get_image_features(**inputs)
```

**Parameters:**

pixel_values (`torch.Tensor` of shape `(batch_size, num_channels, image_size, image_size)`) : The tensors corresponding to the input images. Pixel values can be obtained using `image_processor_class`. See `image_processor_class.__call__` for details ([VisionTextDualEncoderProcessor](/docs/transformers/v5.0.0/en/model_doc/vision-text-dual-encoder#transformers.VisionTextDualEncoderProcessor) uses `image_processor_class` for processing images).

**Returns:**

`[transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([VisionTextDualEncoderConfig](/docs/transformers/v5.0.0/en/model_doc/vision-text-dual-encoder#transformers.VisionTextDualEncoderConfig)) and inputs.

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

