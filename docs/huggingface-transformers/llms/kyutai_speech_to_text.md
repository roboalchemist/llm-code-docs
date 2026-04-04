# Source: https://huggingface.co/docs/transformers/v5.0.0/model_doc/kyutai_speech_to_text.md

# Kyutai Speech-To-Text

## Overview

[Kyutai STT](https://kyutai.org/next/stt) is a speech-to-text model architecture based on the [Mimi codec](https://huggingface.co/docs/transformers/en/model_doc/mimi), which encodes audio into discrete tokens in a streaming fashion, and a [Moshi-like](https://huggingface.co/docs/transformers/en/model_doc/moshi) autoregressive decoder. Kyutai's lab has released two model checkpoints:

- [kyutai/stt-1b-en_fr](https://huggingface.co/kyutai/stt-1b-en_fr): a 1B-parameter model capable of transcribing both English and French
- [kyutai/stt-2.6b-en](https://huggingface.co/kyutai/stt-2.6b-en): a 2.6B-parameter model focused solely on English, optimized for maximum transcription accuracy

    

## Usage Tips

### Inference

```python
import torch
from datasets import load_dataset, Audio
from transformers import KyutaiSpeechToTextProcessor, KyutaiSpeechToTextForConditionalGeneration
from accelerate import Accelerator

# 1. load the model and the processor
torch_device = Accelerator().device
model_id = "kyutai/stt-2.6b-en-trfs"

processor = KyutaiSpeechToTextProcessor.from_pretrained(model_id)
model = KyutaiSpeechToTextForConditionalGeneration.from_pretrained(model_id, device_map=torch_device, dtype="auto")

# 2. load audio samples
ds = load_dataset(
    "hf-internal-testing/librispeech_asr_dummy", "clean", split="validation"
)
ds = ds.cast_column("audio", Audio(sampling_rate=24000))

# 3. prepare the model inputs
inputs = processor(
    ds[0]["audio"]["array"],
)
inputs.to(model.device)

# 4. infer the model
output_tokens = model.generate(**inputs)

# 5. decode the generated tokens
print(processor.batch_decode(output_tokens, skip_special_tokens=True))
```

### Batched Inference

```python
import torch
from datasets import load_dataset, Audio
from transformers import KyutaiSpeechToTextProcessor, KyutaiSpeechToTextForConditionalGeneration
from accelerate import Accelerator

# 1. load the model and the processor
torch_device = Accelerator().device
model_id = "kyutai/stt-2.6b-en-trfs"

processor = KyutaiSpeechToTextProcessor.from_pretrained(model_id)
model = KyutaiSpeechToTextForConditionalGeneration.from_pretrained(model_id, device_map=torch_device, dtype="auto")

# 2. load audio samples
ds = load_dataset(
    "hf-internal-testing/librispeech_asr_dummy", "clean", split="validation"
)
ds = ds.cast_column("audio", Audio(sampling_rate=24000))

# 3. prepare the model inputs
audio_arrays = [ds[i]["audio"]["array"] for i in range(4)]
inputs = processor(audio_arrays, return_tensors="pt", padding=True)
inputs = inputs.to(model.device)

# 4. infer the model
output_tokens = model.generate(**inputs)

# 5. decode the generated tokens
decoded_outputs = processor.batch_decode(output_tokens, skip_special_tokens=True)
for output in decoded_outputs:
    print(output)
```

This model was contributed by [Eustache Le Bihan](https://huggingface.co/eustlb).
The original code can be found [here](https://github.com/kyutai-labs/moshi).

## KyutaiSpeechToTextConfig[[transformers.KyutaiSpeechToTextConfig]]

#### transformers.KyutaiSpeechToTextConfig[[transformers.KyutaiSpeechToTextConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/kyutai_speech_to_text/configuration_kyutai_speech_to_text.py#L25)

This is the configuration class to store the configuration of a [KyutaiSpeechToTextForConditionalGeneration](/docs/transformers/v5.0.0/en/model_doc/kyutai_speech_to_text#transformers.KyutaiSpeechToTextForConditionalGeneration).
It is used to instantiate a Kyutai Speech-to-Text model according to the specified arguments, defining the model
architecture. Instantiating a configuration with the defaults will yield a similar configuration to that of the
2.6b-en model.

e.g. [kyutai/stt-2.6b-en-trfs](https://huggingface.co/kyutai/stt-2.6b-en-trfs)

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:
```python
>>> from transformers import KyutaiSpeechToTextConfig, KyutaiSpeechToTextForConditionalGeneration

>>> # Initializing a KyutaiSpeechToTextConfig
>>> configuration = KyutaiSpeechToTextConfig()

>>> # Initializing a model
>>> model = KyutaiSpeechToTextForConditionalGeneration(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

codebook_vocab_size (`int`, *optional*, defaults to 2049) : Vocabulary size of the codebook. Defines the number of different audio tokens that can be represented by each codebook.

vocab_size (`int`, *optional*, defaults to 4001) : Vocabulary size of the model. Defines the number of different tokens that can be represented by the `input_ids` passed when calling the model.

hidden_size (`int`, *optional*, defaults to 2048) : Dimensionality of the layers and the pooler layer of the main decoder.

num_hidden_layers (`int`, *optional*, defaults to 48) : Number of decoder layers.

num_attention_heads (`int`, *optional*, defaults to 32) : Number of attention heads for each attention layer in the main decoder block.

num_key_value_heads (`int`, *optional*) : This is the number of key_value heads that should be used to implement Grouped Query Attention. If `num_key_value_heads=num_attention_heads`, the model will use Multi Head Attention (MHA), if `num_key_value_heads=1` the model will use Multi Query Attention (MQA) otherwise GQA is used. When converting a multi-head checkpoint to a GQA checkpoint, each group key and value head should be constructed by meanpooling all the original heads within that group. For more details checkout [this paper](https://huggingface.co/papers/2305.13245). If it is not specified, will default to `num_attention_heads`.

max_position_embeddings (`int`, *optional*, defaults to 750) : The maximum sequence length that this model might ever be used with. Typically, set this to something large just in case (e.g., 512 or 1024 or 2048).

rope_parameters (`RopeParameters`, *optional*) : Dictionary containing the configuration parameters for the RoPE embeddings. The dictionary should contain a value for `rope_theta` and optionally parameters used for scaling in case you want to use RoPE with longer `max_position_embeddings`.

hidden_act (`str` or `function`, *optional*, defaults to `"silu"`) : The non-linear activation function (function or string) in the decoder.

head_dim (`int`, *optional*, defaults to `hidden_size // num_attention_heads`) : The attention head dimension.

initializer_range (`float`, *optional*, defaults to 0.02) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

use_cache (`bool`, *optional*, defaults to `True`) : Whether or not the model should return the last key/values attentions (not used by all models). Only relevant if `config.is_decoder=True`.

sliding_window (`int`, *optional*, defaults to 375) : Sliding window attention window size. If not specified, will default to `3000`.

attention_dropout (`float`, *optional*, defaults to 0.0) : The dropout ratio for the attention probabilities.

ffn_dim (`int`, *optional*, defaults to 11264) : Dimensionality of the "intermediate" (often named feed-forward) layer in the main decoder block. Must be even.

rms_norm_eps (`float`, *optional*, defaults to 1e-08) : The epsilon used by the rms normalization layers.

num_codebooks (`int`, *optional*, defaults to 32) : The number of audio codebooks for each audio channels.

audio_bos_token_id (`int`, *optional*, defaults to 2048) : Beginning of stream token id for codebook tokens.

audio_pad_token_id (`int`, *optional*, defaults to 69569) : Padding token id for codebook tokens.

tie_word_embeddings (`bool`, *optional*, defaults to `False`) : Whether to tie weight embeddings.

pad_token_id (`int`, *optional*, defaults to 3) : Padding token id.

bos_token_id (`int`, *optional*, defaults to 48000) : Beginning of stream token id for text tokens.

eos_token_id (`int`, *optional*) : End of stream token id.

codec_config (`PreTrainedConfig`, *optional*) : Configuration for the codec.

kwargs (*optional*) : Dictionary of keyword arguments. Notably:

audio_encoder_config ([PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig), *optional*) : An instance of a configuration object that defines the audio encoder config.

depth__config ([PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig), *optional*) : An instance of a configuration object that defines the depth decoder config.

## KyutaiSpeechToTextProcessor[[transformers.KyutaiSpeechToTextProcessor]]

#### transformers.KyutaiSpeechToTextProcessor[[transformers.KyutaiSpeechToTextProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/kyutai_speech_to_text/processing_kyutai_speech_to_text.py#L30)

Constructs a KyutaiSpeechToTextProcessor which wraps a feature extractor and a tokenizer into a single processor.

[KyutaiSpeechToTextProcessor](/docs/transformers/v5.0.0/en/model_doc/kyutai_speech_to_text#transformers.KyutaiSpeechToTextProcessor) offers all the functionalities of [KyutaiSpeechToTextFeatureExtractor](/docs/transformers/v5.0.0/en/model_doc/kyutai_speech_to_text#transformers.KyutaiSpeechToTextFeatureExtractor) and `tokenizer_class`. See the
[~KyutaiSpeechToTextFeatureExtractor](/docs/transformers/v5.0.0/en/model_doc/kyutai_speech_to_text#transformers.KyutaiSpeechToTextFeatureExtractor) and `~tokenizer_class` for more information.

__call__transformers.KyutaiSpeechToTextProcessor.__call__https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/processing_utils.py#L617[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor'], NoneType] = None"}, {"name": "text", "val": ": str | list[str] | list[list[str]] | None = None"}, {"name": "videos", "val": ": typing.Union[list['PIL.Image.Image'], numpy.ndarray, ForwardRef('torch.Tensor'), list[numpy.ndarray], list['torch.Tensor'], list[list['PIL.Image.Image']], list[list[numpy.ndarray]], list[list['torch.Tensor']], transformers.video_utils.URL, list[transformers.video_utils.URL], list[list[transformers.video_utils.URL]], transformers.video_utils.Path, list[transformers.video_utils.Path], list[list[transformers.video_utils.Path]], NoneType] = None"}, {"name": "audio", "val": ": typing.Union[numpy.ndarray, ForwardRef('torch.Tensor'), collections.abc.Sequence[numpy.ndarray], collections.abc.Sequence['torch.Tensor'], NoneType] = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.processing_utils.ProcessingKwargs]"}]- **images** (`PIL.Image.Image`, `np.ndarray`, `torch.Tensor`, `list[PIL.Image.Image]`, `list[np.ndarray]`, `list[torch.Tensor]`) --
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

feature_extractor (`KyutaiSpeechToTextFeatureExtractor`) : The feature extractor is a required input.

tokenizer (`tokenizer_class`) : The tokenizer is a required input.

**Returns:**

`[BatchFeature](/docs/transformers/v5.0.0/en/main_classes/image_processor#transformers.BatchFeature)`

A [BatchFeature](/docs/transformers/v5.0.0/en/main_classes/image_processor#transformers.BatchFeature) object with processed inputs in a dict format.

## KyutaiSpeechToTextFeatureExtractor[[transformers.KyutaiSpeechToTextFeatureExtractor]]

#### transformers.KyutaiSpeechToTextFeatureExtractor[[transformers.KyutaiSpeechToTextFeatureExtractor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/kyutai_speech_to_text/feature_extraction_kyutai_speech_to_text.py#L32)

Constructs an KyutaiSpeechToText feature extractor.

This feature extractor inherits from [SequenceFeatureExtractor](/docs/transformers/v5.0.0/en/main_classes/feature_extractor#transformers.SequenceFeatureExtractor) which contains
most of the main methods. Users should refer to this superclass for more information regarding those methods.

**Parameters:**

feature_size (`int`, *optional*, defaults to 1) : The feature dimension of the extracted features. Use 1 for mono, 2 for stereo.

sampling_rate (`int`, *optional*, defaults to 24000) : The sampling rate at which the audio waveform should be digitalized expressed in hertz (Hz).

padding_value (`float`, *optional*, defaults to 0.0) : The value that is used to fill the padding values.

chunk_length_s (`float`, *optional*) : If defined the audio is pre-processed into chunks of lengths `chunk_length_s` and then encoded.

overlap (`float`, *optional*) : Defines the overlap between each chunk. It is used to compute the `chunk_stride` using the following formulae : `int((1.0 - self.overlap) * self.chunk_length)`.

audio_delay_seconds (`float`, *optional*, defaults to 0.0) : The delay in seconds to add after the audio (right padding).

audio_silence_prefix_seconds (`float`, *optional*, defaults to 0.0) : The silence prefix in seconds to add before the audio (left padding).

## KyutaiSpeechToTextForConditionalGeneration[[transformers.KyutaiSpeechToTextForConditionalGeneration]]

#### transformers.KyutaiSpeechToTextForConditionalGeneration[[transformers.KyutaiSpeechToTextForConditionalGeneration]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/kyutai_speech_to_text/modeling_kyutai_speech_to_text.py#L1081)

The Kyutai Speech To Text Model for token generation conditioned on other modalities (e.g. image-text-to-text generation).

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.KyutaiSpeechToTextForConditionalGeneration.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/kyutai_speech_to_text/modeling_kyutai_speech_to_text.py#L1103[{"name": "input_ids", "val": ": torch.LongTensor | None = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.LongTensor | None = None"}, {"name": "past_key_values", "val": ": transformers.cache_utils.Cache | None = None"}, {"name": "inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "labels", "val": ": torch.LongTensor | None = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "cache_position", "val": ": torch.LongTensor | None = None"}, {"name": "logits_to_keep", "val": ": int | torch.Tensor = 0"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
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
elements depending on the configuration ([KyutaiSpeechToTextConfig](/docs/transformers/v5.0.0/en/model_doc/kyutai_speech_to_text#transformers.KyutaiSpeechToTextConfig)) and inputs.

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
The [KyutaiSpeechToTextForConditionalGeneration](/docs/transformers/v5.0.0/en/model_doc/kyutai_speech_to_text#transformers.KyutaiSpeechToTextForConditionalGeneration) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Example:

```python
>>> import torch
>>> from datasets import load_dataset, Audio
>>> from transformers import KyutaiSpeechToTextProcessor, KyutaiSpeechToTextForConditionalGeneration

>>> torch_device = "cuda" if torch.cuda.is_available() else "cpu"
>>> model_id = "kyutai/stt-2.6b-en-trfs"

>>> processor = KyutaiSpeechToTextProcessor.from_pretrained(model_id)
>>> model = KyutaiSpeechToTextForConditionalGeneration.from_pretrained(model_id, device_map=torch_device)

>>> ds = load_dataset(
...     "hf-internal-testing/librispeech_asr_dummy", "clean", split="validation"
... )

>>> ds = ds.cast_column("audio", Audio(sampling_rate=24000))
>>> inputs = processor(
...     ds[0]["audio"]["array"],
... )
>>> inputs.to(torch_device)

>>> output_tokens = model.generate(**inputs)
>>> print(processor.batch_decode(output_tokens, skip_special_tokens=True))
```

**Parameters:**

config ([KyutaiSpeechToTextForConditionalGeneration](/docs/transformers/v5.0.0/en/model_doc/kyutai_speech_to_text#transformers.KyutaiSpeechToTextForConditionalGeneration)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

`[transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([KyutaiSpeechToTextConfig](/docs/transformers/v5.0.0/en/model_doc/kyutai_speech_to_text#transformers.KyutaiSpeechToTextConfig)) and inputs.

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
#### generate[[transformers.KyutaiSpeechToTextForConditionalGeneration.generate]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/kyutai_speech_to_text/modeling_kyutai_speech_to_text.py#L1358)

This method forwards all its arguments to GenerationMixin's [generate()](/docs/transformers/v5.0.0/en/main_classes/text_generation#transformers.GenerationMixin.generate). Please refer to the docstring of this method for more information.

## KyutaiSpeechToTextModel[[transformers.KyutaiSpeechToTextModel]]

#### transformers.KyutaiSpeechToTextModel[[transformers.KyutaiSpeechToTextModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/kyutai_speech_to_text/modeling_kyutai_speech_to_text.py#L818)

The bare Kyutai Speech To Text Text Model outputting raw hidden-states without any specific head on to.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.KyutaiSpeechToTextModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/kyutai_speech_to_text/modeling_kyutai_speech_to_text.py#L836[{"name": "input_ids", "val": ": torch.LongTensor | None = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.LongTensor | None = None"}, {"name": "past_key_values", "val": ": transformers.cache_utils.Cache | None = None"}, {"name": "inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "output_attentions", "val": ": bool | None = None"}, {"name": "output_hidden_states", "val": ": bool | None = None"}, {"name": "return_dict", "val": ": bool | None = None"}, {"name": "cache_position", "val": ": torch.LongTensor | None = None"}, {"name": "**kwargs", "val": ""}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
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
- **use_cache** (`bool`, *optional*) --
  If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
  `past_key_values`).
- **output_attentions** (`bool`, *optional*) --
  Whether or not to return the attentions tensors of all attention layers. See `attentions` under returned
  tensors for more detail.
- **output_hidden_states** (`bool`, *optional*) --
  Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
  more detail.
- **return_dict** (`bool`, *optional*) --
  Whether or not to return a [ModelOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.utils.ModelOutput) instead of a plain tuple.
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.0[transformers.modeling_outputs.BaseModelOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or `tuple(torch.FloatTensor)`A [transformers.modeling_outputs.BaseModelOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([KyutaiSpeechToTextConfig](/docs/transformers/v5.0.0/en/model_doc/kyutai_speech_to_text#transformers.KyutaiSpeechToTextConfig)) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.

  If `past_key_values` is used only the last hidden-state of the sequences of shape `(batch_size, 1,
  hidden_size)` is output.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks and optionally if
  `config.is_encoder_decoder=True` in the cross-attention blocks) that can be used (see `past_key_values`
  input) to speed up sequential decoding.
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
The [KyutaiSpeechToTextModel](/docs/transformers/v5.0.0/en/model_doc/kyutai_speech_to_text#transformers.KyutaiSpeechToTextModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

**Parameters:**

config ([KyutaiSpeechToTextModel](/docs/transformers/v5.0.0/en/model_doc/kyutai_speech_to_text#transformers.KyutaiSpeechToTextModel)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

`[transformers.modeling_outputs.BaseModelOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([KyutaiSpeechToTextConfig](/docs/transformers/v5.0.0/en/model_doc/kyutai_speech_to_text#transformers.KyutaiSpeechToTextConfig)) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.

  If `past_key_values` is used only the last hidden-state of the sequences of shape `(batch_size, 1,
  hidden_size)` is output.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks and optionally if
  `config.is_encoder_decoder=True` in the cross-attention blocks) that can be used (see `past_key_values`
  input) to speed up sequential decoding.
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.

