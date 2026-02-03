# Source: https://huggingface.co/docs/transformers/v5.0.0/model_doc/pe_audio_video.md

# PE Audio Video (Perception Encoder Audio-Video)

## Overview

TODO

## Usage

### Basic usage

```py
TODO
```

## PeAudioVideoProcessor[[transformers.PeAudioVideoProcessor]]

#### transformers.PeAudioVideoProcessor[[transformers.PeAudioVideoProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/pe_audio_video/processing_pe_audio_video.py#L17)

__call__transformers.PeAudioVideoProcessor.__call__https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/processing_utils.py#L617[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor'], NoneType] = None"}, {"name": "text", "val": ": str | list[str] | list[list[str]] | None = None"}, {"name": "videos", "val": ": typing.Union[list['PIL.Image.Image'], numpy.ndarray, ForwardRef('torch.Tensor'), list[numpy.ndarray], list['torch.Tensor'], list[list['PIL.Image.Image']], list[list[numpy.ndarray]], list[list['torch.Tensor']], transformers.video_utils.URL, list[transformers.video_utils.URL], list[list[transformers.video_utils.URL]], transformers.video_utils.Path, list[transformers.video_utils.Path], list[list[transformers.video_utils.Path]], NoneType] = None"}, {"name": "audio", "val": ": typing.Union[numpy.ndarray, ForwardRef('torch.Tensor'), collections.abc.Sequence[numpy.ndarray], collections.abc.Sequence['torch.Tensor'], NoneType] = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.processing_utils.ProcessingKwargs]"}]- **images** (`PIL.Image.Image`, `np.ndarray`, `torch.Tensor`, `list[PIL.Image.Image]`, `list[np.ndarray]`, `list[torch.Tensor]`) --
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

images (`PIL.Image.Image`, `np.ndarray`, `torch.Tensor`, `list[PIL.Image.Image]`, `list[np.ndarray]`, `list[torch.Tensor]`) : The image or batch of images to be prepared. Each image can be a PIL image, NumPy array or PyTorch tensor. Both channels-first and channels-last formats are supported.

text (`TextInput`, `PreTokenizedInput`, `list[TextInput]`, `list[PreTokenizedInput]`, *optional*) : The sequence or batch of sequences to be encoded. Each sequence can be a string or a list of strings (pretokenized string). If the sequences are provided as list of strings (pretokenized), you must set `is_split_into_words=True` (to lift the ambiguity with a batch of sequences).

videos (`np.ndarray`, `torch.Tensor`, `List[np.ndarray]`, `List[torch.Tensor]`) : The video or batch of videos to be prepared. Each video can be a 4D NumPy array or PyTorch tensor, or a nested list of 3D frames. Both channels-first and channels-last formats are supported.

audio (`np.ndarray`, `torch.Tensor`, `list[np.ndarray]`, `list[torch.Tensor]`) : The audio or batch of audio to be prepared. Each audio can be a NumPy array or PyTorch tensor.

return_tensors (`str` or [TensorType](/docs/transformers/v5.0.0/en/internal/file_utils#transformers.TensorType), *optional*) : If set, will return tensors of a particular framework. Acceptable values are:  - `'pt'`: Return PyTorch `torch.Tensor` objects. - `'np'`: Return NumPy `np.ndarray` objects.

**Returns:**

`[BatchFeature](/docs/transformers/v5.0.0/en/main_classes/image_processor#transformers.BatchFeature)`

A [BatchFeature](/docs/transformers/v5.0.0/en/main_classes/image_processor#transformers.BatchFeature) object with processed inputs in a dict format.

## PeAudioVideoConfig[[transformers.PeAudioVideoConfig]]

#### transformers.PeAudioVideoConfig[[transformers.PeAudioVideoConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/pe_audio_video/configuration_pe_audio_video.py#L143)

This is the configuration class to store the configuration of a [PeAudioVideoModel](/docs/transformers/v5.0.0/en/model_doc/pe_audio_video#transformers.PeAudioVideoModel). It is used to instantiate a
PeAudioVideoModel model according to the specified arguments, defining the model architecture. Instantiating a configuration
with the defaults will yield a similar configuration to that of pe-av-large.
e.g. [facebook/pe-av-large](https://huggingface.co/facebook/pe-av-large)

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

```python
>>> from transformers import PeAudioVideoModel, PeAudioVideoConfig

>>> # Initializing a PeAudioVideoModel style configuration
>>> configuration = PeAudioVideoConfig()

>>> # Initializing a model from the pe-av-large style configuration
>>> model = PeAudioModel(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

text_config (`dict` or `PreTrainedConfig`, *optional*) : Configuration for the text model component.

audio_video_config (`dict` or `PreTrainedConfig`, *optional*) : Configuration for the audio-video encoder component.

## PeAudioVideoEncoderConfig[[transformers.PeAudioVideoEncoderConfig]]

#### transformers.PeAudioVideoEncoderConfig[[transformers.PeAudioVideoEncoderConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/pe_audio_video/configuration_pe_audio_video.py#L25)

This is the configuration class to store the configuration of a `PeAudioVideoEncoderModel`. It is used to instantiate a
PeAudioVideoEncoder model according to the specified arguments, defining the model architecture. Instantiating a configuration
with the defaults will yield a similar configuration to that of pe-av-large.
e.g. [facebook/pe-av-large](https://huggingface.co/facebook/pe-av-large)

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

```python
>>> from transformers import PeAudioVideoEncoder, PeAudioVideoEncoderConfig

>>> # Initializing a PeAudioVideoEncoder style configuration
>>> configuration = PeAudioVideoEncoderConfig()

>>> # Initializing a model from the pe-av-large style configuration
>>> model = PeAudioVideoEncoder(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

audio_config (`Union[PreTrainedConfig, dict]`, *optional*) : Configuration for the audio encoder. If a dictionary is provided, it is used to instantiate [PeAudioEncoderConfig](/docs/transformers/v5.0.0/en/model_doc/pe_audio#transformers.PeAudioEncoderConfig).

video_config (`Union[PreTrainedConfig, dict]`, *optional*) : Configuration for the video encoder. If a dictionary is provided, it is used to instantiate [PeVideoEncoderConfig](/docs/transformers/v5.0.0/en/model_doc/pe_video#transformers.PeVideoEncoderConfig).

hidden_size (`int`, *optional*, defaults to 1792) : Dimension of the hidden representations.

intermediate_size (`int`, *optional*, defaults to 4800) : Dimension of the feedforward layers in the Transformer blocks.

num_hidden_layers (`int`, *optional*, defaults to 6) : Number of Transformer encoder blocks.

num_attention_heads (`int`, *optional*, defaults to 14) : Number of attention heads used in each attention layer.

num_key_value_heads (`int`, *optional*) : Number of key and value heads for grouped-query attention. If unset, this defaults to `num_attention_heads`.

head_dim (`int`, *optional*, defaults to 128) : Dimension of each attention head for query, key, and value projections.

hidden_act (`str`, *optional*, defaults to `"silu"`) : The non-linear activation function (function or string) in the Transformer blocks.

max_position_embeddings (`int`, *optional*, defaults to 10000) : Maximum sequence length supported by the rotary position embeddings.

initializer_range (`float`, *optional*, defaults to 0.02) : Standard deviation of the truncated normal initializer for weight matrices.

rms_norm_eps (`float`, *optional*, defaults to 1e-05) : Epsilon used by the RMS normalization layers.

rope_parameters (`Union[RopeParameters, dict]`, *optional*, defaults to `{'rope_theta' : 20000}`): Parameters for the rotary position embeddings, such as the base `rope_theta`.

attention_bias (`bool`, *optional*, defaults to `False`) : Whether to use bias terms in the query, key, value, and output projections.

attention_dropout (`float`, *optional*, defaults to 0.0) : Dropout ratio applied to attention probabilities.

## PeAudioVideoModel[[transformers.PeAudioVideoModel]]

#### transformers.PeAudioVideoModel[[transformers.PeAudioVideoModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/pe_audio_video/modeling_pe_audio_video.py#L678)

forwardtransformers.PeAudioVideoModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/pe_audio_video/modeling_pe_audio_video.py#L816[{"name": "input_ids", "val": ": torch.Tensor | None = None"}, {"name": "pixel_values_videos", "val": ": torch.Tensor | None = None"}, {"name": "input_values", "val": ": torch.Tensor | None = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "padding_mask_videos", "val": ": torch.Tensor | None = None"}, {"name": "padding_mask", "val": ": torch.Tensor | None = None"}, {"name": "return_loss", "val": " = False"}, {"name": "**kwargs", "val": ""}]

## PeAudioVideoEncoder[[transformers.PeAudioVideoEncoder]]

#### transformers.PeAudioVideoEncoder[[transformers.PeAudioVideoEncoder]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/pe_audio_video/modeling_pe_audio_video.py#L564)

The PeAudioVideo Encoder model.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.PeAudioVideoEncoder.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/pe_audio_video/modeling_pe_audio_video.py#L583[{"name": "input_values", "val": ": torch.Tensor | None = None"}, {"name": "pixel_values_videos", "val": ": torch.Tensor | None = None"}, {"name": "padding_mask", "val": ": torch.Tensor | None = None"}, {"name": "padding_mask_videos", "val": ": torch.Tensor | None = None"}, {"name": "**kwargs", "val": ""}]

**Parameters:**

config ([PeAudioVideoEncoderConfig](/docs/transformers/v5.0.0/en/model_doc/pe_audio_video#transformers.PeAudioVideoEncoderConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

