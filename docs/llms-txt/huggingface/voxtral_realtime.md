# Source: https://huggingface.co/docs/transformers/v5.3.0/model_doc/voxtral_realtime.md

# VoxtralRealtime

VoxtralRealtime is a streaming speech-to-text model from [Mistral AI](https://mistral.ai), designed for real-time automatic speech recognition (ASR). Unlike the offline [Voxtral](./voxtral) model which processes complete audio files, VoxtralRealtime is architected for low-latency, incremental transcription by processing audio in chunks as they arrive.

The model combines an audio encoder with a Mistral-based language model decoder, using time conditioning embeddings and causal convolutions with padding caches to enable efficient streaming inference.

## Usage

### Offline Transcription

For transcribing complete audio files, use the processor and model directly. The generation length is automatically determined from the audio length.

```python
import torch
from transformers import VoxtralRealtimeForConditionalGeneration, AutoProcessor
from datasets import load_dataset

repo_id = "mistralai/Voxtral-Mini-4B-Realtime-2602"

processor = AutoProcessor.from_pretrained(repo_id)
model = VoxtralRealtimeForConditionalGeneration.from_pretrained(repo_id, device_map="auto")

ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
audio = ds[0]["audio"]["array"]

inputs = processor(audio, return_tensors="pt")
inputs = inputs.to(model.device, dtype=model.dtype)

outputs = model.generate(**inputs)
decoded_outputs = processor.batch_decode(outputs, skip_special_tokens=True)

print(decoded_outputs[0])
```

### Batched Offline Transcription

Multiple audio samples can be transcribed in a single forward pass:

```python
import torch
from transformers import VoxtralRealtimeForConditionalGeneration, AutoProcessor
from datasets import load_dataset

repo_id = "mistralai/Voxtral-Mini-4B-Realtime-2602"

processor = AutoProcessor.from_pretrained(repo_id)
model = VoxtralRealtimeForConditionalGeneration.from_pretrained(repo_id, device_map="auto")

ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
audio = [ds[i]["audio"]["array"] for i in range(2)]

inputs = processor(audio, return_tensors="pt")
inputs = inputs.to(model.device, dtype=model.dtype)

outputs = model.generate(**inputs)
decoded_outputs = processor.batch_decode(outputs, skip_special_tokens=True)

for decoded_output in decoded_outputs:
    print(decoded_output)
```

### Streaming Transcription
> [!NOTE]
> This is an experimental feature and the API is subject to change.

For real-time transcription, audio is split into chunks following:

```python
from transformers import (
    VoxtralRealtimeProcessor,
    VoxtralRealtimeForConditionalGeneration,
    TextIteratorStreamer,
)
from datasets import load_dataset
from threading import Thread
import numpy as np

model_id = "mistralai/Voxtral-Mini-4B-Realtime-2602"
processor = VoxtralRealtimeProcessor.from_pretrained(model_id)
model = VoxtralRealtimeForConditionalGeneration.from_pretrained(model_id, device_map="cuda:0")

ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
audio = ds[0]["audio"]["array"]
# Manually pad the audio to account for right padding tokens required by the model
xaudio = np.pad(audio, (0, processor.num_right_pad_tokens * processor.raw_audio_length_per_tok))

first_chunk_inputs = processor(
    audio[:processor.num_samples_first_audio_chunk],
    is_streaming=True,
    is_first_audio_chunk=True,
    return_tensors="pt"
)
first_chunk_inputs.to(model.device, dtype=model.dtype)

def input_features_generator():
    yield first_chunk_inputs.input_features

    mel_frame_idx = processor.num_mel_frames_first_audio_chunk
    hop_length = processor.feature_extractor.hop_length
    win_length = processor.feature_extractor.win_length
    
    start_idx = mel_frame_idx * hop_length - win_length // 2
    end_idx = start_idx + processor.num_samples_per_audio_chunk

    while (end_idx:=start_idx + processor.num_samples_per_audio_chunk) >> from transformers import VoxtralRealtimeForConditionalGeneration, VoxtralRealtimeConfig

>>> # Initializing a VoxtralRealtime configuration
>>> configuration = VoxtralRealtimeConfig()

>>> # Initializing a model with random weights
>>> model = VoxtralRealtimeForConditionalGeneration(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

audio_config (`Union[AutoConfig, dict]`, *optional*) : The config object or dictionary of the audio encoder.

text_config (`Union[AutoConfig, dict]`, *optional*) : The config object or dictionary of the text model.

projector_hidden_act (`str`, *optional*, defaults to `"gelu"`) : The activation function (function or string) in the multi-modal projector.

audio_length_per_tok (`int`, *optional*, defaults to 8) : The number of audio frames corresponding to each text token.

default_num_delay_tokens (`int`, *optional*, defaults to 6) : The default number of delay tokens used for streaming.

downsample_factor (`int`, *optional*, defaults to 4) : The downsampling factor applied to audio features before projection.

## VoxtralRealtimeEncoderConfig[[transformers.VoxtralRealtimeEncoderConfig]]

#### transformers.VoxtralRealtimeEncoderConfig[[transformers.VoxtralRealtimeEncoderConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/voxtral_realtime/configuration_voxtral_realtime.py#L34)

This is the configuration class to store the configuration of a [VoxtralRealtimeEncoder](/docs/transformers/v5.3.0/en/model_doc/voxtral_realtime#transformers.VoxtralRealtimeEncoder). It is used to instantiate a
Voxtral Realtime audio encoder according to the specified arguments, defining the model architecture. Instantiating a
configuration with the defaults will yield a similar configuration to that of the audio encoder of the Voxtral Realtime
architecture.

e.g. [mistralai/Voxtral-Mini-4B-Realtime-2602](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602)

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.3.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.3.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

```python
>>> from transformers import VoxtralRealtimeEncoderConfig, VoxtralRealtimeEncoder

>>> # Initializing a VoxtralRealtimeEncoderConfig
>>> configuration = VoxtralRealtimeEncoderConfig()

>>> # Initializing a VoxtralRealtimeEncoder (with random weights)
>>> model = VoxtralRealtimeEncoder(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

vocab_size (`int`, *optional*, defaults to 131072) : Vocabulary size of the model.

hidden_size (`int`, *optional*, defaults to 1280) : Dimensionality of the hidden representations.

intermediate_size (`int`, *optional*, defaults to 5120) : Dimension of the MLP representations.

num_hidden_layers (`int`, *optional*, defaults to 32) : Number of hidden layers in the Transformer encoder.

num_attention_heads (`int`, *optional*, defaults to 32) : Number of attention heads for each attention layer in the Transformer encoder.

activation_function (`str`, *optional*, defaults to `"gelu"`) : The non-linear activation function (function or string) in the encoder and pooler.

num_mel_bins (`int`, *optional*, defaults to 128) : Number of mel features used per input features. Should correspond to the value used in the `VoxtralRealtimeProcessor` class.

initializer_range (`float`, *optional*, defaults to 0.02) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

attention_dropout (`float`, *optional*, defaults to 0.0) : The dropout ratio for the attention probabilities.

hidden_act (`str`, *optional*, defaults to `"silu"`) : The activation function used in the MLP layers.

max_position_embeddings (`int`, *optional*, defaults to 1500) : The maximum sequence length that this model might ever be used with.

rms_norm_eps (`float`, *optional*, defaults to 1e-05) : The epsilon used by the RMS normalization layers.

rope_parameters (`Union[RopeParameters, dict]`, *optional*) : The parameters for the rotary position embeddings.

sliding_window (`int`, *optional*, defaults to 750) : The sliding window size for local attention.

head_dim (`int`, *optional*, defaults to 64) : The dimension of each attention head.

## VoxtralRealtimeTextConfig[[transformers.VoxtralRealtimeTextConfig]]

#### transformers.VoxtralRealtimeTextConfig[[transformers.VoxtralRealtimeTextConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/voxtral_realtime/configuration_voxtral_realtime.py#L21)

This is the configuration class to store the configuration of a `VoxtralRealtimeText`. It is used to instantiate a
Voxtral Realtime text decoder according to the specified arguments, defining the model architecture. Instantiating a
configuration with the defaults will yield a similar configuration to that of the text decoder of the Voxtral Realtime
architecture.

e.g. [mistralai/Voxtral-Mini-4B-Realtime-2602](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602)

## VoxtralRealtimeFeatureExtractor[[transformers.VoxtralRealtimeFeatureExtractor]]

#### transformers.VoxtralRealtimeFeatureExtractor[[transformers.VoxtralRealtimeFeatureExtractor]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/voxtral_realtime/feature_extraction_voxtral_realtime.py#L29)

Constructs a VOXTRAL_REALTIME feature extractor.

This feature extractor inherits from [SequenceFeatureExtractor](/docs/transformers/v5.3.0/en/main_classes/feature_extractor#transformers.SequenceFeatureExtractor) which contains
most of the main methods. Users should refer to this superclass for more information regarding those methods.

This class extracts mel-filter bank features from raw speech using a custom numpy implementation of the `Short Time
Fourier Transform` which should match pytorch's `torch.stft` equivalent.

**Parameters:**

feature_size (`int`, *optional*, defaults to 128) : The feature dimension of the extracted features.

sampling_rate (`int`, *optional*, defaults to 16000) : The sampling rate at which the audio files should be digitalized expressed in hertz (Hz).

hop_length (`int`, *optional*, defaults to 160) : Length of the overlapping windows for the STFT used to obtain the Mel Frequency coefficients.

n_fft (`int`, *optional*, defaults to 512) : Size of the Fourier transform.

win_length (`int`, *optional*, defaults to 400) : The window length for the STFT computation.

padding_value (`float`, *optional*, defaults to 0.0) : Padding value used to pad the audio. Should correspond to silences.

## VoxtralRealtimeProcessor[[transformers.VoxtralRealtimeProcessor]]

#### transformers.VoxtralRealtimeProcessor[[transformers.VoxtralRealtimeProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/voxtral_realtime/processing_voxtral_realtime.py#L55)

Constructs a VoxtralRealtimeProcessor which wraps a feature extractor and a tokenizer into a single processor.

[VoxtralRealtimeProcessor](/docs/transformers/v5.3.0/en/model_doc/voxtral_realtime#transformers.VoxtralRealtimeProcessor) offers all the functionalities of [VoxtralRealtimeFeatureExtractor](/docs/transformers/v5.3.0/en/model_doc/voxtral_realtime#transformers.VoxtralRealtimeFeatureExtractor) and [MistralCommonBackend](/docs/transformers/v5.3.0/en/model_doc/mixtral#transformers.MistralCommonBackend). See the
[~VoxtralRealtimeFeatureExtractor](/docs/transformers/v5.3.0/en/model_doc/voxtral_realtime#transformers.VoxtralRealtimeFeatureExtractor) and [~MistralCommonBackend](/docs/transformers/v5.3.0/en/model_doc/mixtral#transformers.MistralCommonBackend) for more information.

__call__transformers.VoxtralRealtimeProcessor.__call__https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/voxtral_realtime/processing_voxtral_realtime.py#L131[{"name": "audio", "val": ": typing.Union[numpy.ndarray, ForwardRef('torch.Tensor'), collections.abc.Sequence[numpy.ndarray], collections.abc.Sequence['torch.Tensor'], NoneType] = None"}, {"name": "is_streaming", "val": ": bool = False"}, {"name": "is_first_audio_chunk", "val": ": bool | None = True"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.models.voxtral_realtime.processing_voxtral_realtime.VoxtralRealtimeProcessorKwargs]"}]- **audio** (`AudioInput`, *optional*) --
  Input audio or batch of audios as NumPy arrays or PyTorch tensors.
- **is_streaming** (`bool`, *optional*, defaults to `False`) --
  Whether to process audio in streaming mode. When `True`, audio can be passed in chunks
  using `is_first_audio_chunk` to distinguish the first chunk from subsequent ones.
- **is_first_audio_chunk** (`bool`, *optional*, defaults to `True`) --
  Whether the current audio is the first chunk in a streaming session. When `True`, the audio
  is encoded into a full transcription request with tokenized text. When `False`, only audio
  features are extracted (text encoding is skipped). Must be `True` when `is_streaming=False`.0[BatchFeature](/docs/transformers/v5.3.0/en/main_classes/feature_extractor#transformers.BatchFeature)A [BatchFeature](/docs/transformers/v5.3.0/en/main_classes/feature_extractor#transformers.BatchFeature) with the following fields:

- **input_ids** -- List of token ids to be fed to the model. Returned when `is_first_audio_chunk=True`.
- **attention_mask** -- List of indices specifying which tokens should be attended to by the model.
  Returned when `is_first_audio_chunk=True`.
- **input_features** -- Mel spectrogram features extracted from the audio input.
- **num_delay_tokens** -- The number of delay tokens used for streaming.

Main method to prepare audio input for the Voxtral Realtime model. This method encodes the audio into
a transcription request using `mistral_common`, tokenizes the resulting text, and extracts mel spectrogram
features using the feature extractor. Supports both streaming and non-streaming modes.

**Parameters:**

feature_extractor (`VoxtralRealtimeFeatureExtractor`) : The feature extractor is a required input.

tokenizer (`MistralCommonBackend`) : The tokenizer is a required input.

**Returns:**

`[BatchFeature](/docs/transformers/v5.3.0/en/main_classes/feature_extractor#transformers.BatchFeature)`

A [BatchFeature](/docs/transformers/v5.3.0/en/main_classes/feature_extractor#transformers.BatchFeature) with the following fields:

- **input_ids** -- List of token ids to be fed to the model. Returned when `is_first_audio_chunk=True`.
- **attention_mask** -- List of indices specifying which tokens should be attended to by the model.
  Returned when `is_first_audio_chunk=True`.
- **input_features** -- Mel spectrogram features extracted from the audio input.
- **num_delay_tokens** -- The number of delay tokens used for streaming.

## VoxtralRealtimeEncoder[[transformers.VoxtralRealtimeEncoder]]

#### transformers.VoxtralRealtimeEncoder[[transformers.VoxtralRealtimeEncoder]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/voxtral_realtime/modeling_voxtral_realtime.py#L502)

The VoxtralRealtime encoder, which is a Whisper encoder.

This model inherits from [PreTrainedModel](/docs/transformers/v5.3.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.VoxtralRealtimeEncoder.forwardhttps://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/voxtral_realtime/modeling_voxtral_realtime.py#L533[{"name": "input_features", "val": ": torch.FloatTensor | None = None"}, {"name": "position_ids", "val": ": torch.LongTensor | None = None"}, {"name": "past_key_values", "val": ": transformers.cache_utils.Cache | None = None"}, {"name": "padding_cache", "val": ": transformers.models.voxtral_realtime.modeling_voxtral_realtime.VoxtralRealtimeConv1dPaddingCache | None = None"}, {"name": "inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "cache_position", "val": ": torch.LongTensor | None = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "use_padding_cache", "val": ": bool | None = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_features** (`torch.FloatTensor` of shape `(batch_size, sequence_length, feature_dim)`, *optional*) --
  The tensors corresponding to the input audio features. Audio features can be obtained using
  [VoxtralRealtimeFeatureExtractor](/docs/transformers/v5.3.0/en/model_doc/voxtral_realtime#transformers.VoxtralRealtimeFeatureExtractor). See `VoxtralRealtimeFeatureExtractor.__call__()` for details ([VoxtralRealtimeProcessor](/docs/transformers/v5.3.0/en/model_doc/voxtral_realtime#transformers.VoxtralRealtimeProcessor) uses
  [VoxtralRealtimeFeatureExtractor](/docs/transformers/v5.3.0/en/model_doc/voxtral_realtime#transformers.VoxtralRealtimeFeatureExtractor) for processing audios).
- **position_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of positions of each input sequence tokens in the position embeddings. Selected in the range `[0, config.n_positions - 1]`.

  [What are position IDs?](../glossary#position-ids)
- **past_key_values** (`~cache_utils.Cache`, *optional*) --
  Pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention
  blocks) that can be used to speed up sequential decoding. This typically consists in the `past_key_values`
  returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.

  Only [Cache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).
  If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.

  The model will output the same cache format that is fed as input.

  If `past_key_values` are used, the user is expected to input only unprocessed `input_ids` (those that don't
  have their past key value states given to this model) of shape `(batch_size, unprocessed_length)` instead of all `input_ids`
  of shape `(batch_size, sequence_length)`.
- **padding_cache** (`VoxtralRealtimeConv1dPaddingCache`, *optional*) --
  Cache for padding in convolutional layers to maintain state across streaming chunks.
- **inputs_embeds** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) --
  Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation. This
  is useful if you want more control over how to convert `input_ids` indices into associated vectors than the
  model's internal embedding lookup matrix.
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.
- **use_cache** (`bool`, *optional*) --
  If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
  `past_key_values`).
- **use_padding_cache** (`bool`, *optional*) --
  Whether to use the padding cache.
- **attention_mask** (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.

  [What are attention masks?](../glossary#attention-mask)0[BaseModelOutputWithPooling](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)`A [BaseModelOutputWithPooling](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([VoxtralRealtimeConfig](/docs/transformers/v5.3.0/en/model_doc/voxtral_realtime#transformers.VoxtralRealtimeConfig)) and inputs.
The [VoxtralRealtimeEncoder](/docs/transformers/v5.3.0/en/model_doc/voxtral_realtime#transformers.VoxtralRealtimeEncoder) forward method, overrides the `__call__` special method.

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

**Parameters:**

config ([VoxtralRealtimeEncoder](/docs/transformers/v5.3.0/en/model_doc/voxtral_realtime#transformers.VoxtralRealtimeEncoder)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.3.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

`[BaseModelOutputWithPooling](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)``

A [BaseModelOutputWithPooling](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([VoxtralRealtimeConfig](/docs/transformers/v5.3.0/en/model_doc/voxtral_realtime#transformers.VoxtralRealtimeConfig)) and inputs.

## VoxtralRealtimeForConditionalGeneration[[transformers.VoxtralRealtimeForConditionalGeneration]]

#### transformers.VoxtralRealtimeForConditionalGeneration[[transformers.VoxtralRealtimeForConditionalGeneration]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/voxtral_realtime/modeling_voxtral_realtime.py#L959)

The VoxtralRealtime model, which consists of Whisper encoder, a multi-modal projector and a LLama language model.

This model inherits from [PreTrainedModel](/docs/transformers/v5.3.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.VoxtralRealtimeForConditionalGeneration.forwardhttps://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/voxtral_realtime/modeling_voxtral_realtime.py#L1037[{"name": "input_ids", "val": ": torch.LongTensor | None = None"}, {"name": "input_features", "val": ": torch.FloatTensor | None = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.LongTensor | None = None"}, {"name": "past_key_values", "val": ": transformers.cache_utils.Cache | None = None"}, {"name": "encoder_past_key_values", "val": ": transformers.cache_utils.Cache | None = None"}, {"name": "padding_cache", "val": ": transformers.models.voxtral_realtime.modeling_voxtral_realtime.VoxtralRealtimeConv1dPaddingCache | None = None"}, {"name": "inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "encoder_inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "labels", "val": ": torch.LongTensor | None = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "cache_position", "val": ": torch.LongTensor | None = None"}, {"name": "logits_to_keep", "val": ": int | torch.Tensor = 0"}, {"name": "num_delay_tokens", "val": ": int | torch.Tensor = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.3.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.3.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.3.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **input_features** (`torch.FloatTensor` of shape `(batch_size, sequence_length, feature_dim)`, *optional*) --
  The tensors corresponding to the input audio features. Audio features can be obtained using
  [VoxtralRealtimeFeatureExtractor](/docs/transformers/v5.3.0/en/model_doc/voxtral_realtime#transformers.VoxtralRealtimeFeatureExtractor). See `VoxtralRealtimeFeatureExtractor.__call__()` for details ([VoxtralRealtimeProcessor](/docs/transformers/v5.3.0/en/model_doc/voxtral_realtime#transformers.VoxtralRealtimeProcessor) uses
  [VoxtralRealtimeFeatureExtractor](/docs/transformers/v5.3.0/en/model_doc/voxtral_realtime#transformers.VoxtralRealtimeFeatureExtractor) for processing audios).
- **attention_mask** (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.

  [What are attention masks?](../glossary#attention-mask)
- **position_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of positions of each input sequence tokens in the position embeddings. Selected in the range `[0, config.n_positions - 1]`.

  [What are position IDs?](../glossary#position-ids)
- **past_key_values** (`~cache_utils.Cache`, *optional*) --
  Pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention
  blocks) that can be used to speed up sequential decoding. This typically consists in the `past_key_values`
  returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.

  Only [Cache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).
  If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.

  The model will output the same cache format that is fed as input.

  If `past_key_values` are used, the user is expected to input only unprocessed `input_ids` (those that don't
  have their past key value states given to this model) of shape `(batch_size, unprocessed_length)` instead of all `input_ids`
  of shape `(batch_size, sequence_length)`.
- **encoder_past_key_values** (`Cache`, *optional*) --
  Pre-computed hidden-states (key and value in the self-attention blocks) for the encoder that can be used to speed up sequential decoding.
- **padding_cache** (`VoxtralRealtimeConv1dPaddingCache`, *optional*) --
  Cache for padding in convolutional layers to maintain state across streaming chunks.
- **inputs_embeds** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) --
  Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation. This
  is useful if you want more control over how to convert `input_ids` indices into associated vectors than the
  model's internal embedding lookup matrix.
- **encoder_inputs_embeds** (`torch.FloatTensor`, *optional*) --
  Optionally, instead of passing `input_features` you can choose to directly pass an embedded representation for the encoder.
- **labels** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Labels for computing the masked language modeling loss. Indices should either be in `[0, ...,
  config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored
  (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.
- **use_cache** (`bool`, *optional*) --
  If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
  `past_key_values`).
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.
- **logits_to_keep** (`Union[int, torch.Tensor]`, *optional*, defaults to `0`) --
  If an `int`, compute logits for the last `logits_to_keep` tokens. If `0`, calculate logits for all
  `input_ids` (special case). Only last token logits are needed for generation, and calculating them only for that
  token can save memory, which becomes pretty significant for long sequences or large vocabulary size.
  If a `torch.Tensor`, must be 1D corresponding to the indices to keep in the sequence length dimension.
  This is useful when using packed tensor format (single dimension for batch and sequence length).
- **num_delay_tokens** (`int` or `torch.Tensor`, *optional*) --
  Number of delay tokens used when preparing inputs, see [~VoxtralRealtimeProcessor](/docs/transformers/v5.3.0/en/model_doc/voxtral_realtime#transformers.VoxtralRealtimeProcessor) for more details.0`VoxtralRealtimeCausalLMOutputWithPast` or `tuple(torch.FloatTensor)`A `VoxtralRealtimeCausalLMOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([VoxtralRealtimeConfig](/docs/transformers/v5.3.0/en/model_doc/voxtral_realtime#transformers.VoxtralRealtimeConfig)) and inputs.
The [VoxtralRealtimeForConditionalGeneration](/docs/transformers/v5.3.0/en/model_doc/voxtral_realtime#transformers.VoxtralRealtimeForConditionalGeneration) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

- **encoder_past_key_values** (`Cache`, *optional*) -- Pre-computed hidden-states (key and value in the self-attention blocks) for the audio encoder
  that can be used to speed up sequential decoding.
- **padding_cache** (`VoxtralRealtimeConv1dPaddingCache`, *optional*) -- Cache for padding in convolutional layers to maintain state across streaming chunks.

Example:

```python
>>> import torch
>>> from transformers import VoxtralRealtimeForConditionalGeneration, AutoProcessor
>>> from datasets import load_dataset

>>> repo_id = "mistralai/Voxtral-Mini-4B-Realtime-2602"

>>> processor = AutoProcessor.from_pretrained(repo_id)
>>> model = VoxtralRealtimeForConditionalGeneration.from_pretrained(repo_id, dtype=torch.bfloat16, device_map="auto")

>>> ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
>>> audio = ds[0]["audio"]["array"]

>>> inputs = processor(audio, return_tensors="pt")
>>> inputs = inputs.to(model.device, dtype=model.dtype)

>>> outputs = model.generate(**inputs)
>>> processor.batch_decode(outputs, skip_special_tokens=True)
```

**Parameters:**

config ([VoxtralRealtimeForConditionalGeneration](/docs/transformers/v5.3.0/en/model_doc/voxtral_realtime#transformers.VoxtralRealtimeForConditionalGeneration)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.3.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``VoxtralRealtimeCausalLMOutputWithPast` or `tuple(torch.FloatTensor)``

A `VoxtralRealtimeCausalLMOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([VoxtralRealtimeConfig](/docs/transformers/v5.3.0/en/model_doc/voxtral_realtime#transformers.VoxtralRealtimeConfig)) and inputs.
#### get_audio_features[[transformers.VoxtralRealtimeForConditionalGeneration.get_audio_features]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/voxtral_realtime/modeling_voxtral_realtime.py#L991)

This method is used to get the audio embeddings from input features (a log mel spectrogram), meaning inferring the audio encoder and the multi-modal projector.

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
>>> from transformers import AutoProcessor, VoxtralRealtimeForConditionalGeneration
>>> from datasets import load_dataset
>>> import torch

>>> dataset = load_dataset("hf-internal-testing/librispeech_asr_demo", "clean", split="validation")
>>> dataset = dataset.sort("id")
>>> sampling_rate = dataset.features["audio"].sampling_rate

>>> processor = AutoProcessor.from_pretrained("mistralai/Voxtral-Mini-4B-Realtime-2602")
>>> model = VoxtralRealtimeForConditionalGeneration.from_pretrained("mistralai/Voxtral-Mini-4B-Realtime-2602")

>>> # audio file is decoded on the fly
>>> inputs = processor(dataset[0]["audio"]["array"], sampling_rate=sampling_rate, return_tensors="pt")
>>> with torch.no_grad():
...     logits = model(**inputs).logits
>>> predicted_ids = torch.argmax(logits, dim=-1)

>>> # transcribe speech
>>> transcription = processor.batch_decode(predicted_ids)
>>> transcription[0]
...

>>> inputs["labels"] = processor(text=dataset[0]["text"], return_tensors="pt").input_ids

>>> # compute loss
>>> loss = model(**inputs).loss
>>> round(loss.item(), 2)
...
```

**Parameters:**

input_features (`torch.FloatTensor`, *optional*) : Float values of mel features extracted from the raw speech waveform. Raw speech waveform can be obtained by loading a `.flac` or `.wav` audio file into an array of type `list[float]` or a `numpy.ndarray`, *e.g.* via the soundfile library (`pip install soundfile`). To prepare the array into `input_features`, the [AutoFeatureExtractor](/docs/transformers/v5.3.0/en/model_doc/auto#transformers.AutoFeatureExtractor) should be used for extracting the mel features, padding and conversion into a tensor of type `torch.FloatTensor`. See `__call__()`

padding_cache (`VoxtralRealtimeConv1dPaddingCache`, *optional*) : Cache for padding in convolutional layers to maintain state across streaming chunks.

encoder_inputs_embeds (`torch.FloatTensor`, *optional*) : Optionally, instead of passing `input_features` you can choose to directly pass an embedded representation for the encoder.

past_key_values (`~cache_utils.Cache`, *optional*) : Pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention blocks) that can be used to speed up sequential decoding. This typically consists in the `past_key_values` returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.  Only [Cache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache). If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.  The model will output the same cache format that is fed as input.  If `past_key_values` are used, the user is expected to input only unprocessed `input_ids` (those that don't have their past key value states given to this model) of shape `(batch_size, unprocessed_length)` instead of all `input_ids` of shape `(batch_size, sequence_length)`.

use_cache (`bool`, *optional*) : If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see `past_key_values`).

**Returns:**

`[BaseModelOutputWithPooling](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)``

A [BaseModelOutputWithPooling](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([VoxtralRealtimeConfig](/docs/transformers/v5.3.0/en/model_doc/voxtral_realtime#transformers.VoxtralRealtimeConfig)) and inputs.

