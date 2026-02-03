# Source: https://huggingface.co/docs/transformers/v5.0.0/model_doc/pe_audio.md

# PE Audio (Perception Encoder Audio)

## Overview

PE Audio (Perception Encoder Audio) is a state-of-the-art multimodal model that embeds audio and text into a shared (joint) embedding space.
The model enables cross-modal retrieval and understanding between audio and text.

**Text input**

- Produces a single embedding representing the full text.

**Audio input**

- **PeAudioFrameLevelModel**
  - Produces a sequence of embeddings, one every 40 ms of audio.
  - Suitable for audio event localization and fine-grained temporal analysis.
- **PeAudioModel**
  - Produces a single embedding for the entire audio clip.
  - Suitable for global audio-text retrieval tasks.

**The resulting embeddings can be used for:**

- Audio event localization
- Cross-modal (audio–text) retrieval and matching

## Usage

### Basic usage

```py
TODO
```

## PeAudioFeatureExtractor[[transformers.PeAudioFeatureExtractor]]

#### transformers.PeAudioFeatureExtractor[[transformers.PeAudioFeatureExtractor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/pe_audio/feature_extraction_pe_audio.py#L26)

Constructs a PeAudioFeatureExtractor feature extractor.

This feature extractor inherits from [SequenceFeatureExtractor](/docs/transformers/v5.0.0/en/main_classes/feature_extractor#transformers.SequenceFeatureExtractor) which contains
most of the main methods. Users should refer to this superclass for more information regarding those methods.

__call__transformers.PeAudioFeatureExtractor.__call__https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/pe_audio/feature_extraction_pe_audio.py#L63[{"name": "raw_audio", "val": ": numpy.ndarray | list[float] | list[numpy.ndarray] | list[list[float]] | str | list[str]"}, {"name": "padding", "val": ": bool | str | transformers.utils.generic.PaddingStrategy | None = None"}, {"name": "truncation", "val": ": bool | None = False"}, {"name": "max_length", "val": ": int | None = None"}, {"name": "return_tensors", "val": ": str | transformers.utils.generic.TensorType | None = None"}, {"name": "sampling_rate", "val": ": int | None = None"}]

**Parameters:**

feature_size (`int`, *optional*, defaults to 1) : The feature dimension of the extracted features. Use 1 for mono, 2 for stereo.

sampling_rate (`int`, *optional*, defaults to 48000) : The sampling rate at which the audio waveform should be digitalized, expressed in hertz (Hz).

padding_value (`float`, *optional*, defaults to 0.0) : The value that is used for padding.

hop_length (`int`, *optional*, defaults to 1920) : Overlap length between successive windows.

## PeAudioProcessor[[transformers.PeAudioProcessor]]

#### transformers.PeAudioProcessor[[transformers.PeAudioProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/pe_audio/processing_pe_audio.py#L17)

__call__transformers.PeAudioProcessor.__call__https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/processing_utils.py#L617[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor'], NoneType] = None"}, {"name": "text", "val": ": str | list[str] | list[list[str]] | None = None"}, {"name": "videos", "val": ": typing.Union[list['PIL.Image.Image'], numpy.ndarray, ForwardRef('torch.Tensor'), list[numpy.ndarray], list['torch.Tensor'], list[list['PIL.Image.Image']], list[list[numpy.ndarray]], list[list['torch.Tensor']], transformers.video_utils.URL, list[transformers.video_utils.URL], list[list[transformers.video_utils.URL]], transformers.video_utils.Path, list[transformers.video_utils.Path], list[list[transformers.video_utils.Path]], NoneType] = None"}, {"name": "audio", "val": ": typing.Union[numpy.ndarray, ForwardRef('torch.Tensor'), collections.abc.Sequence[numpy.ndarray], collections.abc.Sequence['torch.Tensor'], NoneType] = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.processing_utils.ProcessingKwargs]"}]- **images** (`PIL.Image.Image`, `np.ndarray`, `torch.Tensor`, `list[PIL.Image.Image]`, `list[np.ndarray]`, `list[torch.Tensor]`) --
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

## PeAudioConfig[[transformers.PeAudioConfig]]

#### transformers.PeAudioConfig[[transformers.PeAudioConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/pe_audio/configuration_pe_audio.py#L137)

This is the configuration class to store the configuration of a [PeAudioModel](/docs/transformers/v5.0.0/en/model_doc/pe_audio#transformers.PeAudioModel). It is used to instantiate a
PeAudioModel model according to the specified arguments, defining the model architecture. Instantiating a configuration
with the defaults will yield a similar configuration to that of pe-av-large.
e.g. [facebook/pe-av-large](https://huggingface.co/facebook/pe-av-large)

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

```python
>>> from transformers import PeAudioModel, PeAudioConfig

>>> # Initializing a PeAudioModel style configuration
>>> configuration = PeAudioConfig()

>>> # Initializing a model from the pe-av-large style configuration
>>> model = PeAudioModel(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

text_config (`dict` or `PreTrainedConfig`, *optional*) : Configuration for the text model component.

audio_config (`dict` or `PreTrainedConfig`, *optional*) : Configuration for the audio encoder component.

## PeAudioEncoderConfig[[transformers.PeAudioEncoderConfig]]

#### transformers.PeAudioEncoderConfig[[transformers.PeAudioEncoderConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/pe_audio/configuration_pe_audio.py#L24)

This is the configuration class to store the configuration of a [PeAudioEncoder](/docs/transformers/v5.0.0/en/model_doc/pe_audio#transformers.PeAudioEncoder). It is used to instantiate a
PeAudioEncoder model according to the specified arguments, defining the model architecture. Instantiating a configuration
with the defaults will yield a similar configuration to that of pe-av-large.
e.g. [facebook/pe-av-large](https://huggingface.co/facebook/pe-av-large)

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

```python
>>> from transformers import PeAudioEncoder, PeAudioEncoderConfig

>>> # Initializing a PeAudioEncoder style configuration
>>> configuration = PeAudioEncoderConfig()

>>> # Initializing a model from the pe-av-large style configuration
>>> model = PeAudioEncoder(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

dac_config (`Union[PreTrainedConfig, dict]`, *optional*) : Configuration for the DAC audio encoder used to tokenize the raw audio inputs. If a dictionary is passed, it will be used to instantiate a [DacConfig](/docs/transformers/v5.0.0/en/model_doc/dac#transformers.DacConfig) with default DAC hyperparameters.

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

## PeAudioEncoder[[transformers.PeAudioEncoder]]

#### transformers.PeAudioEncoder[[transformers.PeAudioEncoder]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/pe_audio/modeling_pe_audio.py#L619)

The PeAudio Encoder model.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.PeAudioEncoder.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/pe_audio/modeling_pe_audio.py#L638[{"name": "input_values", "val": ": Tensor"}, {"name": "padding_mask", "val": ": torch.Tensor | None = None"}, {"name": "**kwargs", "val": ""}]

**Parameters:**

config ([PeAudioEncoderConfig](/docs/transformers/v5.0.0/en/model_doc/pe_audio#transformers.PeAudioEncoderConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

## PeAudioFrameLevelModel[[transformers.PeAudioFrameLevelModel]]

#### transformers.PeAudioFrameLevelModel[[transformers.PeAudioFrameLevelModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/pe_audio/modeling_pe_audio.py#L768)

forwardtransformers.PeAudioFrameLevelModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/pe_audio/modeling_pe_audio.py#L779[{"name": "input_ids", "val": ": Tensor"}, {"name": "input_values", "val": ": Tensor"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "padding_mask", "val": ": torch.Tensor | None = None"}, {"name": "return_loss", "val": ": bool | None = None"}, {"name": "**kwargs", "val": ""}]

## PeAudioModel[[transformers.PeAudioModel]]

#### transformers.PeAudioModel[[transformers.PeAudioModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/pe_audio/modeling_pe_audio.py#L691)

forwardtransformers.PeAudioModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/pe_audio/modeling_pe_audio.py#L724[{"name": "input_ids", "val": ": Tensor"}, {"name": "input_values", "val": ": Tensor"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "padding_mask", "val": ": torch.Tensor | None = None"}, {"name": "return_loss", "val": ": bool | None = None"}, {"name": "**kwargs", "val": ""}]

