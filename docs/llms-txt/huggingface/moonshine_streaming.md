# Source: https://huggingface.co/docs/transformers/v5.3.0/model_doc/moonshine_streaming.md

# Moonshine Streaming

Moonshine Streaming is a streaming variant of the [Moonshine](https://huggingface.co/papers/2410.15608) speech recognition model, optimized for real-time transcription with low latency. Like the original Moonshine, it is an encoder-decoder model that uses Rotary Position Embedding (RoPE) for handling variable-length speech efficiently. The streaming architecture includes sliding window attention in the encoder and a context adapter that enables incremental processing of audio chunks.

Moonshine Streaming is available in three sizes: tiny, small, and medium, offering a trade-off between speed and accuracy. It is particularly well-suited for on-device streaming transcription and voice command applications.

You can find all the original Moonshine Streaming checkpoints under the [Useful Sensors](https://huggingface.co/UsefulSensors) organization.

> [!TIP]
> Moonshine Streaming processes raw audio waveforms directly without requiring mel-spectrogram preprocessing, making it efficient for real-time applications.

The example below demonstrates how to transcribe speech into text with [Pipeline](/docs/transformers/v5.3.0/en/main_classes/pipelines#transformers.Pipeline) or the [AutoModel](/docs/transformers/v5.3.0/en/model_doc/auto#transformers.AutoModel) class.

```py
import torch
from transformers import pipeline

pipe = pipeline(
    task="automatic-speech-recognition",
    model="UsefulSensors/moonshine-streaming-tiny",
    dtype=torch.float16,
    device=0
)
pipe("https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/mlk.flac")
```

```py
import torch
from datasets import load_dataset
from transformers import AutoProcessor, MoonshineStreamingForConditionalGeneration

processor = AutoProcessor.from_pretrained("UsefulSensors/moonshine-streaming-tiny")
model = MoonshineStreamingForConditionalGeneration.from_pretrained(
    "UsefulSensors/moonshine-streaming-tiny",
    dtype=torch.float16,
    device_map="auto",
    attn_implementation="sdpa"
)

ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
audio_sample = ds[0]["audio"]

inputs = processor(audio_sample["array"], return_tensors="pt")
inputs = inputs.to(model.device)

generated_ids = model.generate(**inputs, max_new_tokens=100)
transcription = processor.decode(generated_ids[0], skip_special_tokens=True)
transcription
```

## MoonshineStreamingProcessor[[transformers.MoonshineStreamingProcessor]]

#### transformers.MoonshineStreamingProcessor[[transformers.MoonshineStreamingProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/moonshine_streaming/processing_moonshine_streaming.py#L37)

Constructs a MoonshineStreamingProcessor which wraps a feature extractor and a tokenizer into a single processor.

[MoonshineStreamingProcessor](/docs/transformers/v5.3.0/en/model_doc/moonshine_streaming#transformers.MoonshineStreamingProcessor) offers all the functionalities of `feature_extractor_class` and `tokenizer_class`. See the
`~feature_extractor_class` and `~tokenizer_class` for more information.

padtransformers.MoonshineStreamingProcessor.padhttps://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/moonshine_streaming/processing_moonshine_streaming.py#L74[{"name": "*args", "val": ""}, {"name": "**kwargs", "val": ""}]- **input_features** --
  When the first argument is a dictionary containing a batch of tensors, or the `input_features` argument is present, it is passed to `MoonshineStreamingFeatureExtractor.pad`.
- **labels** --
  When the `label` argument is present, it is passed to [PreTrainedTokenizer.pad()](/docs/transformers/v5.3.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.pad).0This method returns the results of each `pad` method. If both are used, the output is a dictionary containing the results of both.

This method operates on batches of extracted features and/or tokenized text. It forwards all arguments to
`MoonshineStreamingFeatureExtractor.pad` and/or [PreTrainedTokenizer.pad()](/docs/transformers/v5.3.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.pad) depending on the input modality and returns their outputs. If both modalities are passed, `MoonshineStreamingFeatureExtractor.pad` and [PreTrainedTokenizer.pad()](/docs/transformers/v5.3.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.pad) are called.

**Parameters:**

feature_extractor (`feature_extractor_class`) : The feature extractor is a required input.

tokenizer (`tokenizer_class`) : The tokenizer is a required input.

**Returns:**

This method returns the results of each `pad` method. If both are used, the output is a dictionary containing the results of both.

## MoonshineStreamingEncoderConfig[[transformers.MoonshineStreamingEncoderConfig]]

#### transformers.MoonshineStreamingEncoderConfig[[transformers.MoonshineStreamingEncoderConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/moonshine_streaming/configuration_moonshine_streaming.py#L21)

This is the configuration class to store the configuration of a `MoonshineStreamingEncoder`. It is used to
instantiate a Moonshine Streaming encoder according to the specified arguments, defining the encoder architecture.
Instantiating a configuration with the defaults will yield a similar configuration to that of the Moonshine Streaming tiny model.
e.g. [UsefulSensors/moonshine-streaming-tiny](https://huggingface.co/UsefulSensors/moonshine-streaming-tiny)

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.3.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.3.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

```python
>>> from transformers import MoonshineStreamingEncoder, MoonshineStreamingEncoderConfig

>>> # Initializing a Moonshine Streaming encoder configuration
>>> configuration = MoonshineStreamingEncoderConfig()

>>> # Initializing a model from the configuration
>>> model = MoonshineStreamingEncoder(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

hidden_size (`int`, *optional*, defaults to 320) : Dimension of the hidden representations.

intermediate_size (`int`, *optional*, defaults to 1280) : Dimension of the MLP representations.

hidden_act (`str`, *optional*, defaults to `"gelu"`) : The non-linear activation function (function or string) in the encoder.

num_hidden_layers (`int`, *optional*, defaults to 6) : Number of hidden layers in the Transformer encoder.

num_attention_heads (`int`, *optional*, defaults to 8) : Number of attention heads for each attention layer in the Transformer encoder.

num_key_value_heads (`int`, *optional*, defaults to 8) : This is the number of key_value heads that should be used to implement Grouped Query Attention. If `num_key_value_heads=num_attention_heads`, the model will use Multi Head Attention (MHA), if `num_key_value_heads=1` the model will use Multi Query Attention (MQA) otherwise GQA is used.

max_position_embeddings (`int`, *optional*, defaults to 4096) : The maximum sequence length that this model might ever be used with.

attention_dropout (`float`, *optional*, defaults to 0.0) : The dropout ratio for the attention probabilities.

attention_bias (`bool`, *optional*, defaults to `False`) : Whether to use a bias in the query, key, value and output projection layers during self-attention.

sample_rate (`int`, *optional*, defaults to 16000) : The sample rate of the audio input in Hz.

frame_ms (`float`, *optional*, defaults to 5.0) : The frame duration in milliseconds for audio processing.

sliding_windows (`list[tuple[int, int]]`, *optional*, defaults to `[(16, 4), (16, 4), (16, 0), (16, 0), (16, 4), (16, 4)]`) : List of sliding window configurations for each encoder layer. Each tuple contains (window_size, shift).

head_dim (`int`, *optional*) : The attention head dimension. If None, it will default to hidden_size // num_attention_heads.

## MoonshineStreamingConfig[[transformers.MoonshineStreamingConfig]]

#### transformers.MoonshineStreamingConfig[[transformers.MoonshineStreamingConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/moonshine_streaming/configuration_moonshine_streaming.py#L110)

This is the configuration class to store the configuration of a [MoonshineStreamingModel](/docs/transformers/v5.3.0/en/model_doc/moonshine_streaming#transformers.MoonshineStreamingModel). It is used to
instantiate a Moonshine Streaming model according to the specified arguments, defining the model architecture.
Instantiating a configuration with the defaults will yield a similar configuration to that of the Moonshine
Streaming tiny model.
e.g. [UsefulSensors/moonshine-streaming-tiny](https://huggingface.co/UsefulSensors/moonshine-streaming-tiny)

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.3.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.3.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

```python
>>> from transformers import MoonshineStreamingModel, MoonshineStreamingConfig

>>> # Initializing a Moonshine Streaming configuration
>>> configuration = MoonshineStreamingConfig()

>>> # Initializing a model from the configuration
>>> model = MoonshineStreamingModel(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

encoder_config (`MoonshineStreamingEncoderConfig`, *optional*) : Configuration of the encoder. If not provided, a default `MoonshineStreamingEncoderConfig` will be instantiated.

vocab_size (`int`, *optional*, defaults to 32768) : Vocabulary size of the Moonshine Streaming decoder model. Defines the number of different tokens that can be represented by the `inputs_ids` passed when calling [MoonshineStreamingModel](/docs/transformers/v5.3.0/en/model_doc/moonshine_streaming#transformers.MoonshineStreamingModel).

hidden_size (`int`, *optional*, defaults to 320) : Dimension of the hidden representations.

intermediate_size (`int`, *optional*, defaults to 1280) : Dimension of the MLP representations.

num_hidden_layers (`int`, *optional*, defaults to 6) : Number of hidden layers in the Transformer decoder.

num_attention_heads (`int`, *optional*, defaults to 8) : Number of attention heads for each attention layer in the Transformer decoder.

hidden_act (`str`, *optional*, defaults to `"silu"`) : The non-linear activation function (function or string) in the decoder.

max_position_embeddings (`int`, *optional*, defaults to 4096) : The maximum sequence length that this model might ever be used with.

use_cache (`bool`, *optional*, defaults to `True`) : Whether or not the model should return the last key/values attentions (not used by all models). Only relevant if `config.is_decoder=True`.

pad_token_id (`int`, *optional*, defaults to 0) : Padding token id.

bos_token_id (`int`, *optional*, defaults to 1) : Beginning of stream token id.

eos_token_id (`int`, *optional*, defaults to 2) : End of stream token id.

rope_parameters (`RopeParameters` or `dict`, *optional*, defaults to `{'rope_type' : 'default', 'rope_theta': 10000.0, 'partial_rotary_factor': 0.8}`): Dictionary containing the configuration parameters for the RoPE embeddings. The dictionary should contain a value for `rope_theta`, `rope_type`, and optionally `partial_rotary_factor` for partial RoPE application.

attention_bias (`bool`, *optional*, defaults to `False`) : Whether to use a bias in the query, key, value and output projection layers during self-attention.

attention_dropout (`float`, *optional*, defaults to 0.0) : The dropout ratio for the attention probabilities.

decoder_start_token_id (`int`, *optional*) : The decoder start token id. If not specified, it will default to `bos_token_id`.

head_dim (`int`, *optional*) : The attention head dimension. If None, it will default to hidden_size // num_attention_heads.

pad_head_dim_to_multiple_of (`int`, *optional*) : If set, the head dimension will be padded to a multiple of this value.

tie_word_embeddings (`bool`, *optional*, defaults to `False`) : Whether to tie weight embeddings

is_encoder_decoder (`bool`, *optional*, defaults to `True`) : Whether the model is used as an encoder/decoder or not.

## MoonshineStreamingModel[[transformers.MoonshineStreamingModel]]

#### transformers.MoonshineStreamingModel[[transformers.MoonshineStreamingModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/moonshine_streaming/modeling_moonshine_streaming.py#L897)

The bare Moonshine Streaming Model outputting raw hidden-states without any specific head on top.

This model inherits from [PreTrainedModel](/docs/transformers/v5.3.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.MoonshineStreamingModel.forwardhttps://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/moonshine_streaming/modeling_moonshine_streaming.py#L925[{"name": "input_values", "val": ": torch.FloatTensor | None = None"}, {"name": "attention_mask", "val": ": torch.LongTensor | None = None"}, {"name": "decoder_input_ids", "val": ": torch.LongTensor | None = None"}, {"name": "decoder_attention_mask", "val": ": torch.LongTensor | None = None"}, {"name": "encoder_outputs", "val": ": tuple[tuple[torch.FloatTensor]] | None = None"}, {"name": "past_key_values", "val": ": transformers.cache_utils.EncoderDecoderCache | None = None"}, {"name": "decoder_inputs_embeds", "val": ": tuple[torch.FloatTensor] | None = None"}, {"name": "decoder_position_ids", "val": ": tuple[torch.LongTensor] | None = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "cache_position", "val": ": torch.LongTensor | None = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_values** (`torch.FloatTensor` of shape `(batch_size, audio_length)`) --
  Float values of the raw speech waveform. Raw speech waveform can be
  obtained by loading a `.flac` or `.wav` audio file into an array of type `list[float]`, a
  `numpy.ndarray` or a `torch.Tensor`, *e.g.* via the torchcodec library (`pip install torchcodec`) or
  the soundfile library (`pip install soundfile`). To prepare the array into
  `input_values`, the [AutoFeatureExtractor](/docs/transformers/v5.3.0/en/model_doc/auto#transformers.AutoFeatureExtractor) should be used for padding
  and conversion into a tensor of type `torch.FloatTensor`.
- **attention_mask** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.

  [What are attention masks?](../glossary#attention-mask)
- **decoder_input_ids** (`torch.LongTensor` of shape `(batch_size, target_sequence_length)`, *optional*) --
  Indices of decoder input sequence tokens in the vocabulary.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.3.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.3.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.3.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are decoder input IDs?](../glossary#decoder-input-ids)
- **decoder_attention_mask** (`torch.LongTensor` of shape `(batch_size, target_sequence_length)`, *optional*) --
  Mask to avoid performing attention on certain token indices. By default, a causal mask will be used, to
  make sure the model can only look at previous inputs in order to predict the future.
- **encoder_outputs** (`tuple[tuple[torch.FloatTensor]]`, *optional*) --
  Tuple consists of (`last_hidden_state`, *optional*: `hidden_states`, *optional*: `attentions`)
  `last_hidden_state` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) is a sequence of
  hidden-states at the output of the last layer of the encoder. Used in the cross-attention of the decoder.
- **past_key_values** (`~cache_utils.EncoderDecoderCache`, *optional*) --
  Pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention
  blocks) that can be used to speed up sequential decoding. This typically consists in the `past_key_values`
  returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.

  Only [Cache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).
  If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.

  The model will output the same cache format that is fed as input.

  If `past_key_values` are used, the user is expected to input only unprocessed `input_ids` (those that don't
  have their past key value states given to this model) of shape `(batch_size, unprocessed_length)` instead of all `input_ids`
  of shape `(batch_size, sequence_length)`.
- **decoder_inputs_embeds** (`tuple[torch.FloatTensor]` of shape `(batch_size, target_sequence_length, hidden_size)`, *optional*) --
  Optionally, instead of passing `decoder_input_ids` you can choose to directly pass an embedded
  representation. If `past_key_values` is used, optionally only the last `decoder_inputs_embeds` have to be
  input (see `past_key_values`). This is useful if you want more control over how to convert
  `decoder_input_ids` indices into associated vectors than the model's internal embedding lookup matrix.

  If `decoder_input_ids` and `decoder_inputs_embeds` are both unset, `decoder_inputs_embeds` takes the value
  of `inputs_embeds`.
- **decoder_position_ids** (`torch.LongTensor` of shape `(batch_size, target_sequence_length)`) --
  Indices of positions of each input sequence tokens in the position embeddings.
  Used to calculate the position embeddings up to `config.decoder_config.max_position_embeddings`
- **use_cache** (`bool`, *optional*) --
  If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
  `past_key_values`).
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.0[Seq2SeqModelOutput](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.Seq2SeqModelOutput) or `tuple(torch.FloatTensor)`A [Seq2SeqModelOutput](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.Seq2SeqModelOutput) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([MoonshineStreamingConfig](/docs/transformers/v5.3.0/en/model_doc/moonshine_streaming#transformers.MoonshineStreamingConfig)) and inputs.
The [MoonshineStreamingModel](/docs/transformers/v5.3.0/en/model_doc/moonshine_streaming#transformers.MoonshineStreamingModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the decoder of the model.

  If `past_key_values` is used only the last hidden-state of the sequences of shape `(batch_size, 1,
  hidden_size)` is output.
- **past_key_values** (`EncoderDecoderCache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [EncoderDecoderCache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.EncoderDecoderCache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention
  blocks) that can be used (see `past_key_values` input) to speed up sequential decoding.
- **decoder_hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the decoder at the output of each layer plus the optional initial embedding outputs.
- **decoder_attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights of the decoder, after the attention softmax, used to compute the weighted average in the
  self-attention heads.
- **cross_attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights of the decoder's cross-attention layer, after the attention softmax, used to compute the
  weighted average in the cross-attention heads.
- **encoder_last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) -- Sequence of hidden-states at the output of the last layer of the encoder of the model.
- **encoder_hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the encoder at the output of each layer plus the optional initial embedding outputs.
- **encoder_attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights of the encoder, after the attention softmax, used to compute the weighted average in the
  self-attention heads.

Example:

```python
>>> import torch
>>> from transformers import AutoFeatureExtractor, MoonshineStreamingModel
>>> from datasets import load_dataset

>>> model = MoonshineStreamingModel.from_pretrained("UsefulSensors/moonshine_streaming-tiny")
>>> feature_extractor = AutoFeatureExtractor.from_pretrained("UsefulSensors/moonshine_streaming-tiny")
>>> ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
>>> inputs = feature_extractor(ds[0]["audio"]["array"], return_tensors="pt")
>>> input_values = inputs.input_values
>>> decoder_input_ids = torch.tensor([[1, 1]]) * model.config.decoder_start_token_id
>>> last_hidden_state = model(input_values, decoder_input_ids=decoder_input_ids).last_hidden_state
>>> list(last_hidden_state.shape)
[1, 2, 288]
```

**Parameters:**

config ([MoonshineStreamingModel](/docs/transformers/v5.3.0/en/model_doc/moonshine_streaming#transformers.MoonshineStreamingModel)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.3.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

`[Seq2SeqModelOutput](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.Seq2SeqModelOutput) or `tuple(torch.FloatTensor)``

A [Seq2SeqModelOutput](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.Seq2SeqModelOutput) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([MoonshineStreamingConfig](/docs/transformers/v5.3.0/en/model_doc/moonshine_streaming#transformers.MoonshineStreamingConfig)) and inputs.

## MoonshineStreamingForConditionalGeneration[[transformers.MoonshineStreamingForConditionalGeneration]]

#### transformers.MoonshineStreamingForConditionalGeneration[[transformers.MoonshineStreamingForConditionalGeneration]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/moonshine_streaming/modeling_moonshine_streaming.py#L1020)

The MoonshineStreaming Model with a language modeling head. Can be used for automatic speech recognition.

This model inherits from [PreTrainedModel](/docs/transformers/v5.3.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.MoonshineStreamingForConditionalGeneration.forwardhttps://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/models/moonshine_streaming/modeling_moonshine_streaming.py#L1040[{"name": "input_values", "val": ": torch.FloatTensor | None = None"}, {"name": "attention_mask", "val": ": torch.LongTensor | None = None"}, {"name": "decoder_input_ids", "val": ": torch.LongTensor | None = None"}, {"name": "decoder_attention_mask", "val": ": torch.LongTensor | None = None"}, {"name": "encoder_outputs", "val": ": tuple[tuple[torch.FloatTensor]] | None = None"}, {"name": "past_key_values", "val": ": transformers.cache_utils.EncoderDecoderCache | None = None"}, {"name": "decoder_inputs_embeds", "val": ": tuple[torch.FloatTensor] | None = None"}, {"name": "decoder_position_ids", "val": ": tuple[torch.LongTensor] | None = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "cache_position", "val": ": torch.LongTensor | None = None"}, {"name": "labels", "val": ": torch.LongTensor | None = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_values** (`torch.FloatTensor` of shape `(batch_size, audio_length)`) --
  Float values of the raw speech waveform. Raw speech waveform can be
  obtained by loading a `.flac` or `.wav` audio file into an array of type `list[float]`, a
  `numpy.ndarray` or a `torch.Tensor`, *e.g.* via the torchcodec library (`pip install torchcodec`) or
  the soundfile library (`pip install soundfile`). To prepare the array into
  `input_values`, the [AutoFeatureExtractor](/docs/transformers/v5.3.0/en/model_doc/auto#transformers.AutoFeatureExtractor) should be used for padding
  and conversion into a tensor of type `torch.FloatTensor`.
- **attention_mask** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.

  [What are attention masks?](../glossary#attention-mask)
- **decoder_input_ids** (`torch.LongTensor` of shape `(batch_size, target_sequence_length)`, *optional*) --
  Indices of decoder input sequence tokens in the vocabulary.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.3.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.3.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.3.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are decoder input IDs?](../glossary#decoder-input-ids)
- **decoder_attention_mask** (`torch.LongTensor` of shape `(batch_size, target_sequence_length)`, *optional*) --
  Mask to avoid performing attention on certain token indices. By default, a causal mask will be used, to
  make sure the model can only look at previous inputs in order to predict the future.
- **encoder_outputs** (`tuple[tuple[torch.FloatTensor]]`, *optional*) --
  Tuple consists of (`last_hidden_state`, *optional*: `hidden_states`, *optional*: `attentions`)
  `last_hidden_state` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) is a sequence of
  hidden-states at the output of the last layer of the encoder. Used in the cross-attention of the decoder.
- **past_key_values** (`~cache_utils.EncoderDecoderCache`, *optional*) --
  Pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention
  blocks) that can be used to speed up sequential decoding. This typically consists in the `past_key_values`
  returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.

  Only [Cache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).
  If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.

  The model will output the same cache format that is fed as input.

  If `past_key_values` are used, the user is expected to input only unprocessed `input_ids` (those that don't
  have their past key value states given to this model) of shape `(batch_size, unprocessed_length)` instead of all `input_ids`
  of shape `(batch_size, sequence_length)`.
- **decoder_inputs_embeds** (`tuple[torch.FloatTensor]` of shape `(batch_size, target_sequence_length, hidden_size)`, *optional*) --
  Optionally, instead of passing `decoder_input_ids` you can choose to directly pass an embedded
  representation. If `past_key_values` is used, optionally only the last `decoder_inputs_embeds` have to be
  input (see `past_key_values`). This is useful if you want more control over how to convert
  `decoder_input_ids` indices into associated vectors than the model's internal embedding lookup matrix.

  If `decoder_input_ids` and `decoder_inputs_embeds` are both unset, `decoder_inputs_embeds` takes the value
  of `inputs_embeds`.
- **decoder_position_ids** (`torch.LongTensor` of shape `(batch_size, target_sequence_length)`) --
  Indices of positions of each input sequence tokens in the position embeddings.
  Used to calculate the position embeddings up to `config.decoder_config.max_position_embeddings`
- **use_cache** (`bool`, *optional*) --
  If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
  `past_key_values`).
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.
- **labels** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Labels for computing the masked language modeling loss. Indices should either be in `[0, ...,
  config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored
  (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.0[Seq2SeqLMOutput](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.Seq2SeqLMOutput) or `tuple(torch.FloatTensor)`A [Seq2SeqLMOutput](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.Seq2SeqLMOutput) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([MoonshineStreamingConfig](/docs/transformers/v5.3.0/en/model_doc/moonshine_streaming#transformers.MoonshineStreamingConfig)) and inputs.
The [MoonshineStreamingForConditionalGeneration](/docs/transformers/v5.3.0/en/model_doc/moonshine_streaming#transformers.MoonshineStreamingForConditionalGeneration) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss.
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **past_key_values** (`EncoderDecoderCache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [EncoderDecoderCache](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.EncoderDecoderCache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention
  blocks) that can be used (see `past_key_values` input) to speed up sequential decoding.
- **decoder_hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the decoder at the output of each layer plus the initial embedding outputs.
- **decoder_attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights of the decoder, after the attention softmax, used to compute the weighted average in the
  self-attention heads.
- **cross_attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights of the decoder's cross-attention layer, after the attention softmax, used to compute the
  weighted average in the cross-attention heads.
- **encoder_last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) -- Sequence of hidden-states at the output of the last layer of the encoder of the model.
- **encoder_hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the encoder at the output of each layer plus the initial embedding outputs.
- **encoder_attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights of the encoder, after the attention softmax, used to compute the weighted average in the
  self-attention heads.

Example:

```python
>>> import torch
>>> from transformers import AutoProcessor, MoonshineStreamingForConditionalGeneration
>>> from datasets import load_dataset

>>> processor = AutoProcessor.from_pretrained("UsefulSensors/moonshine_streaming-tiny")
>>> model = MoonshineStreamingForConditionalGeneration.from_pretrained("UsefulSensors/moonshine_streaming-tiny")

>>> ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")

>>> inputs = processor(ds[0]["audio"]["array"], return_tensors="pt")
>>> input_values = inputs.input_values

>>> generated_ids = model.generate(input_values, max_new_tokens=100)

>>> transcription = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
>>> transcription
'Mr. Quilter is the apostle of the middle classes, and we are glad to welcome his gospel.'
```

**Parameters:**

config ([MoonshineStreamingConfig](/docs/transformers/v5.3.0/en/model_doc/moonshine_streaming#transformers.MoonshineStreamingConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.3.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

`[Seq2SeqLMOutput](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.Seq2SeqLMOutput) or `tuple(torch.FloatTensor)``

A [Seq2SeqLMOutput](/docs/transformers/v5.3.0/en/main_classes/output#transformers.modeling_outputs.Seq2SeqLMOutput) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([MoonshineStreamingConfig](/docs/transformers/v5.3.0/en/model_doc/moonshine_streaming#transformers.MoonshineStreamingConfig)) and inputs.
#### generate[[transformers.MoonshineStreamingForConditionalGeneration.generate]]

[Source](https://github.com/huggingface/transformers/blob/v5.3.0/src/transformers/generation/utils.py#L2122)

Generates sequences of token ids for models with a language modeling head.

Most generation-controlling parameters are set in `generation_config` which, if not passed, will be set to the
model's default generation configuration. You can override any `generation_config` by passing the corresponding
parameters to generate(), e.g. `.generate(inputs, num_beams=4, do_sample=True)`.

For an overview of generation strategies and code examples, check out the [following
guide](../generation_strategies).

**Parameters:**

inputs (`torch.Tensor` of varying shape depending on the modality, *optional*) : The sequence used as a prompt for the generation or as model inputs to the encoder. If `None` the method initializes it with `bos_token_id` and a batch size of 1. For decoder-only models `inputs` should be in the format of `input_ids`. For encoder-decoder models *inputs* can represent any of `input_ids`, `input_values`, `input_features`, or `pixel_values`.

generation_config ([GenerationConfig](/docs/transformers/v5.3.0/en/main_classes/text_generation#transformers.GenerationConfig), *optional*) : The generation configuration to be used as base parametrization for the generation call. `**kwargs` passed to generate matching the attributes of `generation_config` will override them. If `generation_config` is not provided, the default will be used, which has the following loading priority: 1) from the `generation_config.json` model file, if it exists; 2) from the model configuration. Please note that unspecified parameters will inherit [GenerationConfig](/docs/transformers/v5.3.0/en/main_classes/text_generation#transformers.GenerationConfig)'s default values, whose documentation should be checked to parameterize generation.

logits_processor (`LogitsProcessorList`, *optional*) : Custom logits processors that complement the default logits processors built from arguments and generation config. If a logit processor is passed that is already created with the arguments or a generation config an error is thrown. This feature is intended for advanced users.

stopping_criteria (`StoppingCriteriaList`, *optional*) : Custom stopping criteria that complements the default stopping criteria built from arguments and a generation config. If a stopping criteria is passed that is already created with the arguments or a generation config an error is thrown. If your stopping criteria depends on the `scores` input, make sure you pass `return_dict_in_generate=True, output_scores=True` to `generate`. This feature is intended for advanced users.

prefix_allowed_tokens_fn (`Callable[[int, torch.Tensor], list[int]]`, *optional*) : If provided, this function constraints the beam search to allowed tokens only at each step. If not provided no constraint is applied. This function takes 2 arguments: the batch ID `batch_id` and `input_ids`. It has to return a list with the allowed tokens for the next generation step conditioned on the batch ID `batch_id` and the previously generated tokens `inputs_ids`. This argument is useful for constrained generation conditioned on the prefix, as described in [Autoregressive Entity Retrieval](https://huggingface.co/papers/2010.00904).

synced_gpus (`bool`, *optional*) : Whether to continue running the while loop until max_length. Unless overridden, this flag will be set to `True` if using `FullyShardedDataParallel` or DeepSpeed ZeRO Stage 3 with multiple GPUs to avoid deadlocking if one GPU finishes generating before other GPUs. Otherwise, defaults to `False`.

assistant_model (`PreTrainedModel`, *optional*) : An assistant model that can be used to accelerate generation. The assistant model must have the exact same tokenizer. The acceleration is achieved when forecasting candidate tokens with the assistant model is much faster than running generation with the model you're calling generate from. As such, the assistant model should be much smaller.

streamer (`BaseStreamer`, *optional*) : Streamer object that will be used to stream the generated sequences. Generated tokens are passed through `streamer.put(token_ids)` and the streamer is responsible for any further processing.

negative_prompt_ids (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) : The negative prompt needed for some processors such as CFG. The batch size must match the input batch size. This is an experimental feature, subject to breaking API changes in future versions.

negative_prompt_attention_mask (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) : Attention_mask for `negative_prompt_ids`.

custom_generate (`str` or `Callable`, *optional*) : One of the following: - `str` (Hugging Face Hub repository name): runs the custom `generate` function defined at `custom_generate/generate.py` in that repository instead of the standard `generate` method. The repository fully replaces the generation logic, and the return type may differ. - `str` (local repository path): same as above but from a local path, `trust_remote_code` not required. - `Callable`: `generate` will perform the usual input preparation steps, then call the provided callable to run the decoding loop. For more information, see [the docs](../../generation_strategies#custom-generation-methods).

kwargs (`dict[str, Any]`, *optional*) : Ad hoc parametrization of `generation_config` and/or additional model-specific kwargs that will be forwarded to the `forward` function of the model. If the model is an encoder-decoder model, encoder specific kwargs should not be prefixed and decoder specific kwargs should be prefixed with *decoder_*.

**Returns:**

`[ModelOutput](/docs/transformers/v5.3.0/en/main_classes/output#transformers.utils.ModelOutput) or `torch.LongTensor``

A [ModelOutput](/docs/transformers/v5.3.0/en/main_classes/output#transformers.utils.ModelOutput) (if `return_dict_in_generate=True`
or when `config.return_dict_in_generate=True`) or a `torch.LongTensor`.

If the model is *not* an encoder-decoder model (`model.config.is_encoder_decoder=False`), the possible
[ModelOutput](/docs/transformers/v5.3.0/en/main_classes/output#transformers.utils.ModelOutput) types are:

- [GenerateDecoderOnlyOutput](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.generation.GenerateDecoderOnlyOutput),
- [GenerateBeamDecoderOnlyOutput](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.generation.GenerateBeamDecoderOnlyOutput)

If the model is an encoder-decoder model (`model.config.is_encoder_decoder=True`), the possible
[ModelOutput](/docs/transformers/v5.3.0/en/main_classes/output#transformers.utils.ModelOutput) types are:

- [GenerateEncoderDecoderOutput](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.generation.GenerateEncoderDecoderOutput),
- [GenerateBeamEncoderDecoderOutput](/docs/transformers/v5.3.0/en/internal/generation_utils#transformers.generation.GenerateBeamEncoderDecoderOutput)

