# Source: https://huggingface.co/docs/transformers/v5.0.0/model_doc/glmasr.md

# GlmAsr

## Overview

**GLM-ASR-Nano-2512** is a robust, open-source speech recognition model with **1.5B parameters**. Designed for
real-world complexity, it outperforms OpenAI Whisper V3 on multiple benchmarks while maintaining a compact size.

Key capabilities include:

* **Exceptional Dialect Support**
  Beyond standard Mandarin and English, the model is highly optimized for **Cantonese (粤语)** and other dialects,
  effectively bridging the gap in dialectal speech recognition.

* **Low-Volume Speech Robustness**
  Specifically trained for **"Whisper/Quiet Speech"** scenarios. It captures and accurately transcribes extremely
  low-volume audio that traditional models often miss.

* **SOTA Performance**
  Achieves the **lowest average error rate (4.10)** among comparable open-source models, showing significant advantages
  in Chinese benchmarks (Wenet Meeting, Aishell-1, etc..).

This model was contributed by [Eustache Le Bihan](https://huggingface.co/eustlb) and [Yuxuan Zhang](https://huggingface.co/ZHANGYUXUAN-zR).
you can check the [model card](https://huggingface.co/zai-org/GLM-ASR-Nano-2512) for more details and our 
[github repo](https://github.com/zai-org/GLM-ASR).

## Usage

### Basic usage

```py
from transformers import AutoModelForSeq2SeqLM, AutoProcessor

processor = AutoProcessor.from_pretrained("zai-org/GLM-ASR-Nano-2512")
model = AutoModelForSeq2SeqLM.from_pretrained("zai-org/GLM-ASR-Nano-2512", dtype="auto", device_map="auto")

inputs = processor.apply_transcription_request("https://huggingface.co/datasets/hf-internal-testing/dummy-audio-samples/resolve/main/bcn_weather.mp3")

inputs = inputs.to(model.device, dtype=model.dtype)
outputs = model.generate(**inputs, do_sample=False, max_new_tokens=500)

decoded_outputs = processor.batch_decode(outputs[:, inputs.input_ids.shape[1] :], skip_special_tokens=True)
print(decoded_outputs)
```

### Advanced usage

The processor's `apply_transcription_request` is equivalent to using the chat template in the following manner:

```py
from transformers import GlmAsrForConditionalGeneration, AutoProcessor

processor = GlmAsrForConditionalGeneration.from_pretrained("zai-org/GLM-ASR-Nano-2512")

inputs = processor.apply_transcription_request("https://huggingface.co/datasets/hf-internal-testing/dummy-audio-samples/resolve/main/bcn_weather.mp3")

# which is equivalent to
conversation = [
    {
        "role": "user",
        "content": [
            {
                "type": "audio",
                "url": "https://huggingface.co/datasets/hf-internal-testing/dummy-audio-samples/resolve/main/bcn_weather.mp3",
            },
            {"type": "text", "text": "Please transcribe this audio into text"},
        ],
    },
]

inputs = processor.apply_chat_template(
    conversation,
    tokenize=True,
    add_generation_prompt=True,
    return_dict=True,
)
```

One can also use audio arrays directly:

```py
from transformers import GlmAsrForConditionalGeneration, AutoProcessor
from datasets import load_dataset

processor = AutoProcessor.from_pretrained("zai-org/GLM-ASR-Nano-2512")
model = GlmAsrForConditionalGeneration.from_pretrained("zai-org/GLM-ASR-Nano-2512", dtype="auto", device_map="auto")

# loading audio directly from dataset
ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
ds = ds.cast_column("audio", Audio(sampling_rate=processor.feature_extractor.sampling_rate))
audio_array = ds[0]["audio"]["array"]

inputs = processor.apply_transcription_request(audio_array)

inputs = inputs.to(model.device, dtype=model.dtype)
outputs = model.generate(**inputs, do_sample=False, max_new_tokens=500)

decoded_outputs = processor.batch_decode(outputs[:, inputs.input_ids.shape[1] :], skip_special_tokens=True)
print(decoded_outputs)
```

### Batched inference

You can process multiple audio files at once:

```py
from transformers import GlmAsrForConditionalGeneration, AutoProcessor

processor = AutoProcessor.from_pretrained("zai-org/GLM-ASR-Nano-2512")
model = GlmAsrForConditionalGeneration.from_pretrained("zai-org/GLM-ASR-Nano-2512", dtype="auto", device_map="auto")

inputs = processor.apply_transcription_request([
    "https://huggingface.co/datasets/hf-internal-testing/dummy-audio-samples/resolve/main/bcn_weather.mp3",
    "https://huggingface.co/datasets/hf-internal-testing/dummy-audio-samples/resolve/main/obama.mp3",
])

inputs = inputs.to(model.device, dtype=model.dtype)
outputs = model.generate(**inputs, do_sample=False, max_new_tokens=500)

decoded_outputs = processor.batch_decode(outputs[:, inputs.input_ids.shape[1] :], skip_special_tokens=True)
print(decoded_outputs)
```

## GlmAsrEncoderConfig[[transformers.GlmAsrEncoderConfig]]

#### transformers.GlmAsrEncoderConfig[[transformers.GlmAsrEncoderConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/glmasr/configuration_glmasr.py#L19)

This is the configuration class to store the configuration of a [GlmAsrEncoder](/docs/transformers/v5.0.0/en/model_doc/glmasr#transformers.GlmAsrEncoder). It is used to instantiate a
glmasr audio encoder according to the specified arguments, defining the model architecture. Instantiating a
configuration with the defaults will yield a similar configuration to that of the audio encoder of the glmasr
architecture.

e.g. [zai-org/GLM-ASR-Nano-2512](https://huggingface.co/zai-org/GLM-ASR-Nano-2512)

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

```python
>>> from transformers import GlmAsrEncoderConfig, GlmAsrEncoder

>>> # Initializing a GlmAsrEncoderConfig
>>> configuration = GlmAsrEncoderConfig()

>>> # Initializing a GlmAsrEncoder (with random weights)
>>> model = GlmAsrEncoder(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

hidden_size (`int`, *optional*, defaults to 1280) : Dimensionality of the hidden representations.

intermediate_size (`int`, *optional*, defaults to 5120) : Dimension of the MLP representations.

num_hidden_layers (`int`, *optional*, defaults to 32) : Number of hidden layers in the Transformer encoder.

num_attention_heads (`int`, *optional*, defaults to 20) : Number of attention heads for each attention layer in the Transformer encoder.

num_key_value_heads (`int`, *optional*) : This is the number of key_value heads that should be used to implement Grouped Query Attention. If `num_key_value_heads=num_attention_heads`, the model will use Multi Head Attention (MHA), if `num_key_value_heads=1` the model will use Multi Query Attention (MQA) otherwise GQA is used. When converting a multi-head checkpoint to a GQA checkpoint, each group key and value head should be constructed by meanpooling all the original heads within that group. For more details, check out [this paper](https://huggingface.co/papers/2305.13245). If it is not specified, will default to `num_attention_heads`.

hidden_act (`str` or `function`, *optional*, defaults to `"gelu"`) : The non-linear activation function (function or string) in the encoder and pooler.

max_position_embeddings (`int`, *optional*, defaults to 1500) : The maximum sequence length that this model might ever be used with.

initializer_range (`float`, *optional*, defaults to 0.02) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

rope_parameters (`RopeParameters`, *optional*) : Dictionary containing the configuration parameters for the RoPE embeddings. The dictionary should contain a value for `rope_theta` and optionally parameters used for scaling in case you want to use RoPE with longer `max_position_embeddings`.

attention_dropout (`float`, *optional*, defaults to 0.0) : The dropout ratio for the attention probabilities.

num_mel_bins (`int`, *optional*, defaults to 128) : Number of mel features used per input features. Should correspond to the value used in the `GlmAsrProcessor` class.

## GlmAsrConfig[[transformers.GlmAsrConfig]]

#### transformers.GlmAsrConfig[[transformers.GlmAsrConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/glmasr/configuration_glmasr.py#L113)

This is the configuration class to store the configuration of a [GlmAsrForConditionalGeneration](/docs/transformers/v5.0.0/en/model_doc/glmasr#transformers.GlmAsrForConditionalGeneration). It is used to instantiate an
glmasr model according to the specified arguments, defining the model architecture. Instantiating a configuration
with the defaults will yield a similar configuration to that of the glmasr-Mini-3B.

e.g. [zai-org/GLM-ASR-Nano-2512](https://huggingface.co/zai-org/GLM-ASR-Nano-2512)

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

```python
>>> from transformers import GlmAsrForConditionalGeneration, GlmAsrConfig

>>> # Initializing a glmasr configuration
>>> configuration = GlmAsrConfig()

>>> # Initializing a GLM-ASR-Nano-2512 model with random weights
>>> model = GlmAsrForConditionalGeneration(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

audio_config (`Union[AutoConfig, dict]`, *optional*) : The config object or dictionary of the audio encoder.

text_config (`Union[AutoConfig, dict]`, *optional*) : The config object or dictionary of the text model.

audio_token_id (`int`, *optional*, defaults to 59260) : The audio token index to encode the audio prompt.

projector_hidden_act (`str`, *optional*, defaults to `"gelu"`) : The activation function (function or string) in the multi-modal projector.

## GlmAsrPreTrainedModel[[transformers.GlmAsrPreTrainedModel]]

#### transformers.GlmAsrPreTrainedModel[[transformers.GlmAsrPreTrainedModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/glmasr/modeling_glmasr.py#L278)

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

_forward_unimplementedtransformers.GlmAsrPreTrainedModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/torch/nn/modules/module.py#L391[{"name": "*input", "val": ": typing.Any"}]
Define the computation performed at every call.

Should be overridden by all subclasses.

Although the recipe for forward pass needs to be defined within
this function, one should call the `Module` instance afterwards
instead of this since the former takes care of running the
registered hooks while the latter silently ignores them.

**Parameters:**

config ([PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

## GlmAsrProcessor[[transformers.GlmAsrProcessor]]

#### transformers.GlmAsrProcessor[[transformers.GlmAsrProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/glmasr/processing_glmasr.py#L58)

Constructs an GlmAsr processor which wraps an GlmAsr feature extractor and an GlmAsr
tokenizer into a single processor.

[GlmAsrProcessor](/docs/transformers/v5.0.0/en/model_doc/glmasr#transformers.GlmAsrProcessor) offers all the functionalities of [WhisperFeatureExtractor](/docs/transformers/v5.0.0/en/model_doc/whisper#transformers.WhisperFeatureExtractor) and
[Qwen2TokenizerFast](/docs/transformers/v5.0.0/en/model_doc/qwen2#transformers.Qwen2Tokenizer). See the [__call__()](/docs/transformers/v5.0.0/en/model_doc/glmasr#transformers.GlmAsrProcessor.__call__) for more information.

__call__transformers.GlmAsrProcessor.__call__https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/glmasr/processing_glmasr.py#L106[{"name": "text", "val": ": str | list[str]"}, {"name": "audio", "val": ": typing.Union[numpy.ndarray, ForwardRef('torch.Tensor'), collections.abc.Sequence[numpy.ndarray], collections.abc.Sequence['torch.Tensor'], NoneType] = None"}, {"name": "output_labels", "val": ": bool | None = False"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.models.glmasr.processing_glmasr.GlmAsrProcessorKwargs]"}]- **text** (`str` or `list[str]`) --
  Input sequence or batch of sequences.
- **audio** (`np.ndarray` or `list[np.ndarray]`) --
  Input audio or batch of audios as NumPy arrays. If provided, there must be as many `text` inputs as
  `audio` inputs.
- **output_labels** (bool, *optional*, default=False) --
  Whether to return labels for training.0[BatchFeature](/docs/transformers/v5.0.0/en/main_classes/image_processor#transformers.BatchFeature)A dictionary with tokenized text (`input_ids`, `attention_mask`) and
audio features (`input_features`, `input_features_mask`).

Main method to prepare one or several text sequence(s) and audio waveform(s) for the model. This
method expands `` placeholders in the text based on the post-pool frame counts of the
audio windows, then tokenizes the provided strings as-is, and extracts log-mel features
with [WhisperFeatureExtractor](/docs/transformers/v5.0.0/en/model_doc/whisper#transformers.WhisperFeatureExtractor). If `audio` is `None`, no audio processing is performed and
the text is tokenized as-is (LM-only behavior).

**Parameters:**

feature_extractor ([WhisperFeatureExtractor](/docs/transformers/v5.0.0/en/model_doc/whisper#transformers.WhisperFeatureExtractor)) : The feature extractor is a required input.

tokenizer ([Qwen2TokenizerFast](/docs/transformers/v5.0.0/en/model_doc/qwen2#transformers.Qwen2Tokenizer)) : The tokenizer is a required input.

chat_template (`Optional[str]`, *optional*) : The Jinja template to use for formatting the conversation. If not provided, the tokenizer's default chat template will be used.

audio_token (`Optional[str]`, *optional*, defaults to `"`") : Special token used to represent audio inputs in the chat template.

default_transcription_prompt (`str`, *optional*, defaults to `"Please transcribe this audio into text"`) : Default prompt to use for transcription tasks when applying transcription requests.

max_audio_len (`int`, *optional*, defaults to 655) : Maximum length of audio sequences in seconds. Audio longer than this will be truncated. 655 gives approximately 8192 tokens, corresponding to the maximum sequence length of the text model.

**Returns:**

`[BatchFeature](/docs/transformers/v5.0.0/en/main_classes/image_processor#transformers.BatchFeature)`

A dictionary with tokenized text (`input_ids`, `attention_mask`) and
audio features (`input_features`, `input_features_mask`).

## GlmAsrEncoder[[transformers.GlmAsrEncoder]]

#### transformers.GlmAsrEncoder[[transformers.GlmAsrEncoder]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/glmasr/modeling_glmasr.py#L290)

forwardtransformers.GlmAsrEncoder.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/glmasr/modeling_glmasr.py#L313[{"name": "input_features", "val": ""}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_features** (`` of shape `(batch_size, sequence_length, feature_dim)`) --
  The tensors corresponding to the input audio features. Audio features can be obtained using
  [WhisperFeatureExtractor](/docs/transformers/v5.0.0/en/model_doc/whisper#transformers.WhisperFeatureExtractor). See [WhisperFeatureExtractor.__call__()](/docs/transformers/v5.0.0/en/model_doc/whisper#transformers.WhisperFeatureExtractor.__call__) for details ([GlmAsrProcessor](/docs/transformers/v5.0.0/en/model_doc/glmasr#transformers.GlmAsrProcessor) uses
  [WhisperFeatureExtractor](/docs/transformers/v5.0.0/en/model_doc/whisper#transformers.WhisperFeatureExtractor) for processing audios).0
The [GlmAsrEncoder](/docs/transformers/v5.0.0/en/model_doc/glmasr#transformers.GlmAsrEncoder) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

**Parameters:**

input_features (`` of shape `(batch_size, sequence_length, feature_dim)`) : The tensors corresponding to the input audio features. Audio features can be obtained using [WhisperFeatureExtractor](/docs/transformers/v5.0.0/en/model_doc/whisper#transformers.WhisperFeatureExtractor). See [WhisperFeatureExtractor.__call__()](/docs/transformers/v5.0.0/en/model_doc/whisper#transformers.WhisperFeatureExtractor.__call__) for details ([GlmAsrProcessor](/docs/transformers/v5.0.0/en/model_doc/glmasr#transformers.GlmAsrProcessor) uses [WhisperFeatureExtractor](/docs/transformers/v5.0.0/en/model_doc/whisper#transformers.WhisperFeatureExtractor) for processing audios).

## GlmAsrForConditionalGeneration[[transformers.GlmAsrForConditionalGeneration]]

#### transformers.GlmAsrForConditionalGeneration[[transformers.GlmAsrForConditionalGeneration]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/glmasr/modeling_glmasr.py#L356)

The GlmAsr model which consists of a fine-tuned Whisper encoder, a multi-modal projector and a Llama language model.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.GlmAsrForConditionalGeneration.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/glmasr/modeling_glmasr.py#L427[{"name": "input_ids", "val": ": torch.LongTensor | None = None"}, {"name": "input_features", "val": ": torch.FloatTensor | None = None"}, {"name": "input_features_mask", "val": ": torch.Tensor | None = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.LongTensor | None = None"}, {"name": "past_key_values", "val": ": transformers.cache_utils.Cache | None = None"}, {"name": "inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "labels", "val": ": torch.LongTensor | None = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "cache_position", "val": ": torch.LongTensor | None = None"}, {"name": "logits_to_keep", "val": ": int | torch.Tensor = 0"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **input_features** (`torch.FloatTensor` of shape `(batch_size, sequence_length, feature_dim)`, *optional*) --
  The tensors corresponding to the input audio features. Audio features can be obtained using
  [WhisperFeatureExtractor](/docs/transformers/v5.0.0/en/model_doc/whisper#transformers.WhisperFeatureExtractor). See [WhisperFeatureExtractor.__call__()](/docs/transformers/v5.0.0/en/model_doc/whisper#transformers.WhisperFeatureExtractor.__call__) for details ([GlmAsrProcessor](/docs/transformers/v5.0.0/en/model_doc/glmasr#transformers.GlmAsrProcessor) uses
  [WhisperFeatureExtractor](/docs/transformers/v5.0.0/en/model_doc/whisper#transformers.WhisperFeatureExtractor) for processing audios).
- **input_features_mask** (`torch.Tensor` of shape `(batch_size, feature_sequence_length)`) --
  Mask to avoid performing attention on padding feature indices. Mask values selected in `[0, 1]`:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.
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

  Only [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).
  If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.

  The model will output the same cache format that is fed as input.

  If `past_key_values` are used, the user is expected to input only unprocessed `input_ids` (those that don't
  have their past key value states given to this model) of shape `(batch_size, unprocessed_length)` instead of all `input_ids`
  of shape `(batch_size, sequence_length)`.
- **inputs_embeds** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) --
  Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation. This
  is useful if you want more control over how to convert `input_ids` indices into associated vectors than the
  model's internal embedding lookup matrix.
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
  This is useful when using packed tensor format (single dimension for batch and sequence length).0[transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or `tuple(torch.FloatTensor)`A [transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([GlmAsrConfig](/docs/transformers/v5.0.0/en/model_doc/glmasr#transformers.GlmAsrConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
  `past_key_values` input) to speed up sequential decoding.
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
The [GlmAsrForConditionalGeneration](/docs/transformers/v5.0.0/en/model_doc/glmasr#transformers.GlmAsrForConditionalGeneration) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Example:

```python
>>> from transformers import GlmAsrForConditionalGeneration, AutoProcessor

>>> model_id = "zai-org/GLM-ASR-Nano-2512"
>>> processor = AutoProcessor.from_pretrained(model_id)
>>> model = GlmAsrForConditionalGeneration.from_pretrained(model_id, dtype="auto", device_map="auto")
>>> inputs = processor.apply_transcription_request("https://huggingface.co/datasets/hf-internal-testing/dummy-audio-samples/resolve/main/bcn_weather.mp3")

>>> inputs = inputs.to(model.device, dtype=model.dtype)

>>> outputs = model.generate(**inputs, do_sample=False, max_new_tokens=500)

>>> decoded_outputs = processor.batch_decode(outputs[:, inputs.input_ids.shape[1] :], skip_special_tokens=True)
>>> print(decoded_outputs)
```

**Parameters:**

config ([GlmAsrForConditionalGeneration](/docs/transformers/v5.0.0/en/model_doc/glmasr#transformers.GlmAsrForConditionalGeneration)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

`[transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([GlmAsrConfig](/docs/transformers/v5.0.0/en/model_doc/glmasr#transformers.GlmAsrConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
  `past_key_values` input) to speed up sequential decoding.
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.

