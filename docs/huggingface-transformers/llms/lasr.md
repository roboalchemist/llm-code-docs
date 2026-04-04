# Source: https://huggingface.co/docs/transformers/v5.0.0rc1/model_doc/lasr.md

# LASR

## Overview

TODO

## Usage

### Basic usage

```py
from transformers import pipeline

pipe = pipeline("automatic-speech-recognition", model="path/to/lasr-model")
out = pipe("path/to/audio.mp3")
print(out)
```

```py
from transformers import AutoModelForCTC, AutoProcessor
from datasets import load_dataset, Audio
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

processor = AutoProcessor.from_pretrained("path/to/lasr-model")
model = AutoModelForCTC.from_pretrained("path/to/lasr-model", dtype="auto", device_map=device)

ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
ds = ds.cast_column("audio", Audio(sampling_rate=processor.feature_extractor.sampling_rate))
speech_samples = [el['array'] for el in ds["audio"][:5]]

inputs = processor(speech_samples, sampling_rate=processor.feature_extractor.sampling_rate)
inputs.to(model.device, dtype=model.dtype)
outputs = model.generate(**inputs)
print(processor.batch_decode(outputs))
```

### Making The Model Go Brrr

TODO

### Training

TODO

## LasrTokenizer[[transformers.LasrTokenizer]]

#### transformers.LasrTokenizer[[transformers.LasrTokenizer]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/lasr/tokenization_lasr.py#L35)

Construct a LASR tokenizer (backed by HuggingFace's *tokenizers* library). Based on
[Unigram](https://huggingface.co/docs/tokenizers/python/latest/components.html?highlight=unigram#models).

This tokenizer inherits from [TokenizersBackend](/docs/transformers/v5.0.0rc1/en/main_classes/tokenizer#transformers.TokenizersBackend) which contains most of the main methods. Users should
refer to this superclass for more information regarding those methods.

get_sentinel_token_idstransformers.LasrTokenizer.get_sentinel_token_idshttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/lasr/tokenization_lasr.py#L158[]
Get the token IDs for sentinel tokens.

**Parameters:**

vocab_file (`str`, *optional*) : [SentencePiece](https://github.com/google/sentencepiece) file (generally has a *.spm* extension) that contains the vocabulary necessary to instantiate a tokenizer.

eos_token (`str`, *optional*, defaults to `""`) : The end of sequence token.    When building a sequence using special tokens, this is not the token that is used for the end of sequence. The token used is the `sep_token`.   

unk_token (`str`, *optional*, defaults to `""`) : The unknown token. A token that is not in the vocabulary cannot be converted to an ID and is set to be this token instead.

pad_token (`str`, *optional*, defaults to `""`) : The token used for padding, for example when batching sequences of different lengths.

extra_ids (`int`, *optional*, defaults to 100) : Add a number of extra ids added to the vocabulary for use as sentinels. These tokens are accessible as "" where "{%d}" is a number between 0 and extra_ids-1. These tokens can be retrieved by calling get_sentinel_tokens method and token ids can be by calling get_sentinel_token_ids method

additional_special_tokens (`list[str]`, *optional*) : Additional special tokens used by the tokenizer.

vocab (`str`, `dict` or `list`, *optional*) : Custom vocabulary dict. If not provided, a minimal vocabulary is created using the special tokens.
#### get_sentinel_tokens[[transformers.LasrTokenizer.get_sentinel_tokens]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/lasr/tokenization_lasr.py#L152)

Get the list of sentinel tokens (extra_id tokens) from additional_special_tokens.

## LasrFeatureExtractor[[transformers.LasrFeatureExtractor]]

#### transformers.LasrFeatureExtractor[[transformers.LasrFeatureExtractor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/lasr/feature_extraction_lasr.py#L69)

Constructs a LASR feature extractor.

This feature extractor inherits from [SequenceFeatureExtractor](/docs/transformers/v5.0.0rc1/en/main_classes/feature_extractor#transformers.SequenceFeatureExtractor) which contains
most of the main methods. Users should refer to this superclass for more information regarding those methods.

This class extracts mel-filter bank features from raw speech using a custom numpy implementation of the `Short Time
Fourier Transform` which should match pytorch's `torch.stft` equivalent.

__call__transformers.LasrFeatureExtractor.__call__https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/lasr/feature_extraction_lasr.py#L141[{"name": "raw_speech", "val": ": typing.Union[numpy.ndarray, list[float], list[numpy.ndarray], list[list[float]]]"}, {"name": "truncation", "val": ": bool = False"}, {"name": "pad_to_multiple_of", "val": ": typing.Optional[int] = None"}, {"name": "return_tensors", "val": ": typing.Union[str, transformers.utils.generic.TensorType, NoneType] = None"}, {"name": "return_attention_mask", "val": ": typing.Optional[bool] = None"}, {"name": "padding", "val": ": typing.Optional[str] = 'longest'"}, {"name": "max_length", "val": ": typing.Optional[int] = None"}, {"name": "sampling_rate", "val": ": typing.Optional[int] = None"}, {"name": "do_normalize", "val": ": typing.Optional[bool] = None"}, {"name": "device", "val": ": typing.Optional[str] = 'cpu'"}, {"name": "return_token_timestamps", "val": ": typing.Optional[bool] = None"}, {"name": "**kwargs", "val": ""}]- **raw_speech** (`np.ndarray`, `list[float]`, `list[np.ndarray]`, `list[list[float]]`) --
  The sequence or batch of sequences to be padded. Each sequence can be a numpy array, a list of float
  values, a list of numpy arrays or a list of list of float values. Must be mono channel audio, not
  stereo, i.e. single float per timestep.
- **truncation** (`bool`, *optional*, default to `True`) --
  Activates truncation to cut input sequences longer than *max_length* to *max_length*.
- **pad_to_multiple_of** (`int`, *optional*, defaults to None) --
  If set will pad the sequence to a multiple of the provided value.

  This is especially useful to enable the use of Tensor Cores on NVIDIA hardware with compute capability
  `>= 7.5` (Volta), or on TPUs which benefit from having sequence lengths be a multiple of 128.
- **return_attention_mask** (`bool`, *optional*) --
  Whether to return the attention mask. If left to the default, will return the attention mask according
  to the specific feature_extractor's default.

  [What are attention masks?](../glossary#attention-mask)

  

  For Parakeet models, `attention_mask` should always be passed for batched inference, to avoid subtle
  bugs.

  

- **return_tensors** (`str` or [TensorType](/docs/transformers/v5.0.0rc1/en/internal/file_utils#transformers.TensorType), *optional*) --
  If set, will return tensors instead of list of python integers. Acceptable values are:

  - `'tf'`: Return TensorFlow `tf.constant` objects.
  - `'pt'`: Return PyTorch `torch.Tensor` objects.
  - `'np'`: Return Numpy `np.ndarray` objects.
- **sampling_rate** (`int`, *optional*) --
  The sampling rate at which the `raw_speech` input was sampled. It is strongly recommended to pass
  `sampling_rate` at the forward call to prevent silent errors and allow automatic speech recognition
  pipeline.
- **padding_value** (`float`, *optional*, defaults to 0.0) --
  The value that is used to fill the padding values / vectors.
- **do_normalize** (`bool`, *optional*, defaults to `False`) --
  Whether or not to zero-mean unit-variance normalize the input. Normalizing can help to significantly
  improve the performance of the model.
- **device** (`str`, *optional*, defaults to `'cpu'`) --
  Specifies the device for computation of the log-mel spectrogram of audio signals in the
  `_torch_extract_fbank_features` method. (e.g., "cpu", "cuda")
- **return_token_timestamps** (`bool`, *optional*, defaults to `None`) --
  Deprecated. Use `return_attention_mask` instead from which the number of frames can be inferred.

  Whether or not to return the number of frames of the input raw_speech.
  These num_frames can be used by the model to compute word level timestamps.0

Main method to featurize and prepare for the model one or several sequence(s). Implementation uses PyTorch for
the STFT computation if available, otherwise a slower NumPy based one.

**Parameters:**

feature_size (`int`, *optional*, defaults to 128) : The feature dimension of the extracted features.

sampling_rate (`int`, *optional*, defaults to 16000) : The sampling rate at which the audio files should be digitalized expressed in hertz (Hz).

hop_length (`int`, *optional*, defaults to 160) : Length of the overlapping windows for the STFT used to obtain the Mel Frequency coefficients.

n_fft (`int`, *optional*, defaults to 512) : Size of the Fourier transform.

win_length (`int`, *optional*, defaults to 400) : The window length for the STFT computation.

padding_value (`float`, *optional*, defaults to 0.0) : Padding value used to pad the audio. Should correspond to silences.

## LasrProcessor[[transformers.LasrProcessor]]

#### transformers.LasrProcessor[[transformers.LasrProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/lasr/processing_lasr.py#L49)

__call__transformers.LasrProcessor.__call__https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/lasr/processing_lasr.py#L55[{"name": "audio", "val": ": typing.Union[numpy.ndarray, ForwardRef('torch.Tensor'), collections.abc.Sequence[numpy.ndarray], collections.abc.Sequence['torch.Tensor']]"}, {"name": "text", "val": ": typing.Union[str, list[str], list[list[str]], NoneType] = None"}, {"name": "sampling_rate", "val": ": typing.Optional[int] = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.models.lasr.processing_lasr.LasrProcessorKwargs]"}]
#### batch_decode[[transformers.LasrProcessor.batch_decode]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/processing_utils.py#L1520)

This method forwards all its arguments to PreTrainedTokenizer's [batch_decode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.batch_decode). Please
refer to the docstring of this method for more information.
#### decode[[transformers.LasrProcessor.decode]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/processing_utils.py#L1529)

This method forwards all its arguments to PreTrainedTokenizer's [decode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.decode). Please refer to
the docstring of this method for more information.

## LasrEncoderConfig[[transformers.LasrEncoderConfig]]

#### transformers.LasrEncoderConfig[[transformers.LasrEncoderConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/lasr/configuration_lasr.py#L27)

This is the configuration class to store the configuration of a [LasrEncoder](/docs/transformers/v5.0.0rc1/en/model_doc/lasr#transformers.LasrEncoder). It is used to instantiate a
`LasrEncoder` model according to the specified arguments, defining the model architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:
```python
>>> from transformers import LasrEncoderModel, LasrEncoderConfig

>>> # Initializing a `LasrEncoder` configuration
>>> configuration = LasrEncoderConfig()

>>> # Initializing a model from the configuration
>>> model = LasrEncoderModel(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

This configuration class is based on the LasrEncoder architecture from Google Health AI. You can find more details
and pre-trained models at [TODO/TODO](https://huggingface.co/TODO/TODO).

**Parameters:**

hidden_size (`int`, *optional*, defaults to 512) : Dimension of the layers and the hidden states.

num_hidden_layers (`int`, *optional*, defaults to 17) : Number of hidden layers in the Transformer encoder.

num_attention_heads (`int`, *optional*, defaults to 8) : Number of attention heads for each attention layer in the Transformer encoder.

intermediate_size (`int`, *optional*, defaults to 2048) : Dimension of the "intermediate" (often named feed-forward) layer in the Transformer encoder.

hidden_act (`str` or `function`, *optional*, defaults to `"silu"`) : The non-linear activation function (function or string) in the encoder and pooler.

attention_bias (`bool`, *optional*, defaults to `False`) : Whether to use bias in the attention layers.

convolution_bias (`bool`, *optional*, defaults to `False`) : Whether to use bias in convolutions of the conformer's convolution module.

conv_kernel_size (`int`, *optional*, defaults to 32) : The kernel size of the convolution layers in the Conformer block.

subsampling_conv_channels (`int`, *optional*, defaults to 256) : The number of channels in the subsampling convolution layers.

subsampling_conv_kernel_size (`int`, *optional*, defaults to 5) : The kernel size of the subsampling convolution layers.

subsampling_conv_stride (`int`, *optional*, defaults to 2) : The stride of the subsampling convolution layers.

num_mel_bins (`int`, *optional*, defaults to 128) : Number of mel features.

dropout (`float`, *optional*, defaults to 0.1) : The dropout ratio for all fully connected layers in the embeddings, encoder, and pooler.

dropout_positions (`float`, *optional*, defaults to 0.0) : The dropout ratio for the positions in the input sequence.

layerdrop (`float`, *optional*, defaults to 0.1) : The dropout ratio for the layers in the encoder.

activation_dropout (`float`, *optional*, defaults to 0.1) : The dropout ratio for activations inside the fully connected layer.

attention_dropout (`float`, *optional*, defaults to 0.1) : The dropout ratio for the attention layers.

max_position_embeddings (`int`, *optional*, defaults to 10000) : The maximum sequence length that this model might ever be used with.

initializer_range (`float`, *optional*, defaults to 0.02) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

layer_norm_eps (`float`, *optional*, defaults to 1e-06) : The epsilon used by the layer normalization layers.

feed_forward_residual_weights (`tuple[float, float]`, *optional*, defaults to `[1.5, 0.5]`) : The residual weights for the feed forward layers.

conv_residual_weights (`tuple[float, float]`, *optional*, defaults to `[2.0, 1.0]`) : The residual weights for the convolution layers.

batch_norm_momentum (`float`, *optional*, defaults to 0.01) : The momentum for the batch normalization layers.

rope_parameters (`RopeParameters`, *optional*) : Dictionary containing the configuration parameters for the RoPE embeddings. The dictionary should contain a value for `rope_theta` and optionally parameters used for scaling in case you want to use RoPE with longer `max_position_embeddings`.

## LasrCTCConfig[[transformers.LasrCTCConfig]]

#### transformers.LasrCTCConfig[[transformers.LasrCTCConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/lasr/configuration_lasr.py#L169)

This is the configuration class to store the configuration of a [LasrForCTC](/docs/transformers/v5.0.0rc1/en/model_doc/lasr#transformers.LasrForCTC). It is used to instantiate a
Lasr CTC model according to the specified arguments, defining the model architecture.
Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:
```python
>>> from transformers import LasrForCTC, LasrCTCConfig
>>> # Initializing a Lasr configuration
>>> configuration = LasrCTCConfig()
>>> # Initializing a model from the configuration
>>> model = LasrForCTC(configuration)
>>> # Accessing the model configuration
>>> configuration = model.config
```

This configuration class is based on the Lasr CTC architecture from Google Health AI. You can find more details
and pre-trained models at [TODO/TODO](https://huggingface.co/TODO/TODO).

from_encoder_configtransformers.LasrCTCConfig.from_encoder_confighttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/lasr/configuration_lasr.py#L232[{"name": "encoder_config", "val": ": LasrEncoderConfig"}, {"name": "**kwargs", "val": ""}][LasrCTCConfig](/docs/transformers/v5.0.0rc1/en/model_doc/lasr#transformers.LasrCTCConfig)An instance of a configuration object

Instantiate a [LasrCTCConfig](/docs/transformers/v5.0.0rc1/en/model_doc/lasr#transformers.LasrCTCConfig) (or a derived class) from lasr encoder model configuration.

**Parameters:**

vocab_size (`int`, *optional*, defaults to 512) : Vocabulary size of the model.

ctc_loss_reduction (`str`, *optional*, defaults to `"mean"`) : Specifies the reduction to apply to the output of `torch.nn.CTCLoss`. Only relevant when training an instance of [LasrForCTC](/docs/transformers/v5.0.0rc1/en/model_doc/lasr#transformers.LasrForCTC).

ctc_zero_infinity (`bool`, *optional*, defaults to `True`) : Whether to zero infinite losses and the associated gradients of `torch.nn.CTCLoss`. Infinite losses mainly occur when the inputs are too short to be aligned to the targets. Only relevant when training an instance of [LasrForCTC](/docs/transformers/v5.0.0rc1/en/model_doc/lasr#transformers.LasrForCTC).

encoder_config (`Union[dict, LasrEncoderConfig]`, *optional*) : The config object or dictionary of the encoder.

pad_token_id (`int`, *optional*, defaults to 0) : Padding token id. Also used as blank token id.

**Returns:**

`[LasrCTCConfig](/docs/transformers/v5.0.0rc1/en/model_doc/lasr#transformers.LasrCTCConfig)`

An instance of a configuration object

## LasrEncoder[[transformers.LasrEncoder]]

#### transformers.LasrEncoder[[transformers.LasrEncoder]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/lasr/modeling_lasr.py#L468)

The LasrEncoder model, based on the Conformer architecture](https://arxiv.org/abs/2005.08100).

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.LasrEncoder.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/lasr/modeling_lasr.py#L489[{"name": "input_features", "val": ": Tensor"}, {"name": "attention_mask", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_features** (`torch.Tensor` of shape `(batch_size, sequence_length, feature_dim)`) --
  The tensors corresponding to the input audio features. Audio features can be obtained using
  `feature_extractor_class`. See `feature_extractor_class.__call__` for details (`processor_class` uses
  `feature_extractor_class` for processing audios).
- **attention_mask** (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.

  [What are attention masks?](../glossary#attention-mask)0[transformers.modeling_outputs.BaseModelOutput](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutput) or `tuple(torch.FloatTensor)`A [transformers.modeling_outputs.BaseModelOutput](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutput) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration (`None`) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
The [LasrEncoder](/docs/transformers/v5.0.0rc1/en/model_doc/lasr#transformers.LasrEncoder) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Example:

```python
>>> from transformers import AutoProcessor, LasrEncoder
>>> from datasets import load_dataset, Audio

>>> model_id = TODO
>>> processor = AutoProcessor.from_pretrained(model_id)
>>> encoder = ParakeetEncoder.from_pretrained(model_id)

>>> ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
>>> ds = ds.cast_column("audio", Audio(sampling_rate=processor.feature_extractor.sampling_rate))

>>> inputs = processor(ds[0]["audio"]["array"])
>>> encoder_outputs = encoder(**inputs)

>>> print(encoder_outputs.last_hidden_state.shape)
```

**Parameters:**

config ([LasrEncoderConfig](/docs/transformers/v5.0.0rc1/en/model_doc/lasr#transformers.LasrEncoderConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

`[transformers.modeling_outputs.BaseModelOutput](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutput) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutput](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutput) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration (`None`) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.

## LasrForCTC[[transformers.LasrForCTC]]

#### transformers.LasrForCTC[[transformers.LasrForCTC]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/lasr/modeling_lasr.py#L590)

Lasr Encoder with a Connectionist Temporal Classification (CTC) head.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.LasrForCTC.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/lasr/modeling_lasr.py#L601[{"name": "input_features", "val": ": Tensor"}, {"name": "attention_mask", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "labels", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_features** (`torch.Tensor` of shape `(batch_size, sequence_length, feature_dim)`) --
  The tensors corresponding to the input audio features. Audio features can be obtained using
  `feature_extractor_class`. See `feature_extractor_class.__call__` for details (`processor_class` uses
  `feature_extractor_class` for processing audios).
- **attention_mask** (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.

  [What are attention masks?](../glossary#attention-mask)
- **labels** (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Labels for computing the masked language modeling loss. Indices should either be in `[0, ...,
  config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored
  (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.0[transformers.modeling_outputs.CausalLMOutput](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.CausalLMOutput) or `tuple(torch.FloatTensor)`A [transformers.modeling_outputs.CausalLMOutput](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.CausalLMOutput) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration (`None`) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
The [LasrForCTC](/docs/transformers/v5.0.0rc1/en/model_doc/lasr#transformers.LasrForCTC) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Example:

```python
>>> from transformers import AutoProcessor, LasrForCTC
>>> from datasets import load_dataset, Audio

>>> model_id = "nvidia/lasr-ctc-1.1b"
>>> processor = AutoProcessor.from_pretrained(model_id)
>>> model = LasrForCTC.from_pretrained(model_id)

>>> ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
>>> ds = ds.cast_column("audio", Audio(sampling_rate=processor.feature_extractor.sampling_rate))

>>> inputs = processor(ds[0]["audio"]["array"], text=ds[0]["text"])
>>> outputs = model(**inputs)

>>> print(outputs.loss)
```

**Parameters:**

config ([LasrCTCConfig](/docs/transformers/v5.0.0rc1/en/model_doc/lasr#transformers.LasrCTCConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

`[transformers.modeling_outputs.CausalLMOutput](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.CausalLMOutput) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.CausalLMOutput](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.CausalLMOutput) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration (`None`) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
#### generate[[transformers.LasrForCTC.generate]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/lasr/modeling_lasr.py#L674)

Example:

```python
>>> from transformers import AutoProcessor, LasrForCTC
>>> from datasets import load_dataset, Audio

>>> model_id = TODO
>>> processor = AutoProcessor.from_pretrained(model_id)
>>> model = LasrForCTC.from_pretrained(model_id)

>>> ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
>>> ds = ds.cast_column("audio", Audio(sampling_rate=processor.feature_extractor.sampling_rate))

>>> inputs = processor(ds[0]["audio"]["array"], text=ds[0]["text"])
>>> predicted_ids = model.generate(**inputs)
>>> transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)

>>> print(transcription)
```

