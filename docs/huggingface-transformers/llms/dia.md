# Source: https://huggingface.co/docs/transformers/v5.0.0rc1/model_doc/dia.md

# Dia

    
        
        
        
    

## Overview

[Dia](https://github.com/nari-labs/dia) is an open-source text-to-speech (TTS) model (1.6B parameters) developed by [Nari Labs](https://huggingface.co/nari-labs).
It can generate highly realistic dialogue from transcript including non-verbal communications such as laughter and coughing.
Furthermore, emotion and tone control is also possible via audio conditioning (voice cloning).

**Model Architecture:**
Dia is an encoder-decoder transformer based on the original transformer architecture. However, some more modern features such as
rotational positional embeddings (RoPE) are also included. For its text portion (encoder), a byte tokenizer is utilized while
for the audio portion (decoder), a pretrained codec model [DAC](./dac) is used - DAC encodes speech into discrete codebook
tokens and decodes them back into audio.

## Usage Tips

### Generation with Text

```python
from transformers import AutoProcessor, DiaForConditionalGeneration
from accelerate import Accelerator

torch_device = Accelerator().device
model_checkpoint = "nari-labs/Dia-1.6B-0626"

text = ["[S1] Dia is an open weights text to dialogue model."]
processor = AutoProcessor.from_pretrained(model_checkpoint)
inputs = processor(text=text, padding=True, return_tensors="pt").to(torch_device)

model = DiaForConditionalGeneration.from_pretrained(model_checkpoint).to(torch_device)
outputs = model.generate(**inputs, max_new_tokens=256)  # corresponds to around ~2s

# save audio to a file
outputs = processor.batch_decode(outputs)
processor.save_audio(outputs, "example.wav")

```

### Generation with Text and Audio (Voice Cloning)

```python
from datasets import load_dataset, Audio
from transformers import AutoProcessor, DiaForConditionalGeneration
from accelerate import Accelerator

torch_device = Accelerator().device
model_checkpoint = "nari-labs/Dia-1.6B-0626"

ds = load_dataset("hf-internal-testing/dailytalk-dummy", split="train")
ds = ds.cast_column("audio", Audio(sampling_rate=44100))
audio = ds[-1]["audio"]["array"]
# text is a transcript of the audio + additional text you want as new audio
text = ["[S1] I know. It's going to save me a lot of money, I hope. [S2] I sure hope so for you."]

processor = AutoProcessor.from_pretrained(model_checkpoint)
inputs = processor(text=text, audio=audio, padding=True, return_tensors="pt").to(torch_device)
prompt_len = processor.get_audio_prompt_len(inputs["decoder_attention_mask"])

model = DiaForConditionalGeneration.from_pretrained(model_checkpoint).to(torch_device)
outputs = model.generate(**inputs, max_new_tokens=256)  # corresponds to around ~2s

# retrieve actually generated audio and save to a file
outputs = processor.batch_decode(outputs, audio_prompt_len=prompt_len)
processor.save_audio(outputs, "example_with_audio.wav")
```

### Training

```python
from datasets import load_dataset, Audio
from transformers import AutoProcessor, DiaForConditionalGeneration
from accelerate import Accelerator

torch_device = Accelerator().device
model_checkpoint = "nari-labs/Dia-1.6B-0626"

ds = load_dataset("hf-internal-testing/dailytalk-dummy", split="train")
ds = ds.cast_column("audio", Audio(sampling_rate=44100))
audio = ds[-1]["audio"]["array"]
# text is a transcript of the audio
text = ["[S1] I know. It's going to save me a lot of money, I hope."]

processor = AutoProcessor.from_pretrained(model_checkpoint)
inputs = processor(
    text=text,
    audio=audio,
    generation=False,
    output_labels=True,
    padding=True,
    return_tensors="pt"
).to(torch_device)

model = DiaForConditionalGeneration.from_pretrained(model_checkpoint).to(torch_device)
out = model(**inputs)
out.loss.backward()
```

This model was contributed by [Jaeyong Sung](https://huggingface.co/buttercrab), [Arthur Zucker](https://huggingface.co/ArthurZ),
and [Anton Vlasjuk](https://huggingface.co/AntonV). The original code can be found [here](https://github.com/nari-labs/dia/).

## DiaConfig[[transformers.DiaConfig]]

#### transformers.DiaConfig[[transformers.DiaConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/dia/configuration_dia.py#L200)

This is the configuration class to store the configuration of a [DiaModel](/docs/transformers/v5.0.0rc1/en/model_doc/dia#transformers.DiaModel). It is used to instantiate a
Dia model according to the specified arguments, defining the model architecture. Instantiating a configuration
with the defaults will yield a similar configuration to that of the
[nari-labs/Dia-1.6B](https://huggingface.co/nari-labs/Dia-1.6B) architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:

```python
>>> from transformers import DiaConfig, DiaModel

>>> # Initializing a DiaConfig with default values
>>> configuration = DiaConfig()

>>> # Initializing a DiaModel (with random weights) from the configuration
>>> model = DiaModel(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

get_text_configtransformers.DiaConfig.get_text_confighttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/dia/configuration_dia.py#L289[{"name": "*args", "val": ""}, {"name": "**kwargs", "val": ""}]
Defaulting to audio config as it's the decoder in this case which is usually the text backbone

**Parameters:**

encoder_config (`DiaEncoderConfig`, *optional*) : Configuration for the encoder part of the model. If not provided, a default `DiaEncoderConfig` will be used.

decoder_config (`DiaDecoderConfig`, *optional*) : Configuration for the decoder part of the model. If not provided, a default `DiaDecoderConfig` will be used.

norm_eps (`float`, *optional*, defaults to 1e-05) : The epsilon used by the normalization layers.

is_encoder_decoder (`bool`, *optional*, defaults to `True`) : Indicating that this model uses an encoder-decoder architecture.

pad_token_id (`int`, *optional*, defaults to 1025) : Padding token id.

eos_token_id (`int`, *optional*, defaults to 1024) : End of stream token id.

bos_token_id (`int`, *optional*, defaults to 1026) : Beginning of stream token id.

delay_pattern (`list[int]`, *optional*, defaults to `[0, 8, 9, 10, 11, 12, 13, 14, 15]`) : The delay pattern for the decoder. The length of this list must match `decoder_config.num_channels`.

initializer_range (`float`, *optional*, defaults to 0.02) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

use_cache (`bool`, *optional*, defaults to `True`) : Whether or not the model should return the last key/values attentions (not used by all models).

## DiaDecoderConfig[[transformers.DiaDecoderConfig]]

#### transformers.DiaDecoderConfig[[transformers.DiaDecoderConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/dia/configuration_dia.py#L100)

This is the configuration class to store the configuration of a `DiaDecoder`. It is used to instantiate a Dia
decoder according to the specified arguments, defining the decoder architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

**Parameters:**

max_position_embeddings (`int`, *optional*, defaults to 3072) : The maximum sequence length that this model might ever be used with.

num_hidden_layers (`int`, *optional*, defaults to 18) : Number of hidden layers in the Transformer decoder.

hidden_size (`int`, *optional*, defaults to 2048) : Dimensionality of the decoder layers and the pooler layer.

intermediate_size (`int`, *optional*, defaults to 8192) : Dimensionality of the "intermediate" (often named feed-forward) layer in the Transformer decoder.

num_attention_heads (`int`, *optional*, defaults to 16) : Number of attention heads for each attention layer in the Transformer decoder.

num_key_value_heads (`int`, *optional*, defaults to 4) : Number of key and value heads for each attention layer in the Transformer decoder.

head_dim (`int`, *optional*, defaults to 128) : Dimensionality of the attention head.

cross_num_attention_heads (`int`, *optional*, defaults to 16) : Number of attention heads for each cross-attention layer in the Transformer decoder.

cross_head_dim (`int`, *optional*, defaults to 128) : Dimensionality of the cross-attention head.

cross_num_key_value_heads (`int`, *optional*, defaults to 16) : Number of key and value heads for each cross-attention layer in the Transformer decoder.

cross_hidden_size (`int`, *optional*, defaults to 1024) : Dimensionality of the cross-attention layers.

norm_eps (`float`, *optional*, defaults to 1e-05) : The epsilon used by the normalization layers.

vocab_size (`int`, *optional*, defaults to 1028) : Vocabulary size of the Dia model. Defines the number of different tokens that can be represented by the `inputs_ids` passed when calling [DiaModel](/docs/transformers/v5.0.0rc1/en/model_doc/dia#transformers.DiaModel).

hidden_act (`str` or `function`, *optional*, defaults to `"silu"`) : The non-linear activation function (function or string) in the decoder. If string, `"gelu"`, `"relu"`, `"swish"` and `"gelu_new"` are supported.

num_channels (`int`, *optional*, defaults to 9) : Number of channels for the Dia decoder.

rope_parameters (`RopeParameters`, *optional*) : Dictionary containing the configuration parameters for the RoPE embeddings. The dictionary should contain a value for `rope_theta` and optionally parameters used for scaling in case you want to use RoPE with longer `max_position_embeddings`.

initializer_range (`float`, *optional*, defaults to 0.02) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

use_cache (`bool`, *optional*, defaults to `True`) : Whether or not the model should return the last key/values attentions (not used by all models).

is_encoder_decoder (`bool`, *optional*, defaults to `True`) : Indicating that this model is part of an encoder-decoder architecture.

## DiaEncoderConfig[[transformers.DiaEncoderConfig]]

#### transformers.DiaEncoderConfig[[transformers.DiaEncoderConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/dia/configuration_dia.py#L27)

This is the configuration class to store the configuration of a `DiaEncoder`. It is used to instantiate a Dia
encoder according to the specified arguments, defining the encoder architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

**Parameters:**

max_position_embeddings (`int`, *optional*, defaults to 1024) : The maximum sequence length that this model might ever be used with.

num_hidden_layers (`int`, *optional*, defaults to 12) : Number of hidden layers in the Transformer encoder.

hidden_size (`int`, *optional*, defaults to 1024) : Dimensionality of the encoder layers and the pooler layer.

num_attention_heads (`int`, *optional*, defaults to 16) : Number of attention heads for each attention layer in the Transformer encoder.

num_key_value_heads (`int`, *optional*, defaults to 16) : Number of key and value heads for each attention layer in the Transformer encoder.

head_dim (`int`, *optional*, defaults to 128) : Dimensionality of the attention head.

intermediate_size (`int`, *optional*, defaults to 4096) : Dimensionality of the "intermediate" (often named feed-forward) layer in the Transformer encoder.

norm_eps (`float`, *optional*, defaults to 1e-05) : The epsilon used by the normalization layers.

vocab_size (`int`, *optional*, defaults to 256) : Vocabulary size of the Dia model. Defines the number of different tokens that can be represented by the `inputs_ids` passed when calling [DiaModel](/docs/transformers/v5.0.0rc1/en/model_doc/dia#transformers.DiaModel).

hidden_act (`str` or `function`, *optional*, defaults to `"silu"`) : The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`, `"relu"`, `"swish"` and `"gelu_new"` are supported.

rope_parameters (`RopeParameters`, *optional*) : Dictionary containing the configuration parameters for the RoPE embeddings. The dictionary should contain a value for `rope_theta` and optionally parameters used for scaling in case you want to use RoPE with longer `max_position_embeddings`.

initializer_range (`float`, *optional*, defaults to 0.02) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

## DiaTokenizer[[transformers.DiaTokenizer]]

#### transformers.DiaTokenizer[[transformers.DiaTokenizer]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/dia/tokenization_dia.py#L26)

Construct a Dia tokenizer. Dia simply uses raw bytes utf-8 encoding except for special tokens `[S1]` and `[S2]`.

This tokenizer inherits from [PreTrainedTokenizerFast](/docs/transformers/v5.0.0rc1/en/main_classes/tokenizer#transformers.TokenizersBackend) which contains most of the main methods. Users should
refer to this superclass for more information regarding those methods.

__call__transformers.DiaTokenizer.__call__https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/tokenization_utils_base.py#L2469[{"name": "text", "val": ": Union[TextInput, PreTokenizedInput, list[TextInput], list[PreTokenizedInput], None] = None"}, {"name": "text_pair", "val": ": Optional[Union[TextInput, PreTokenizedInput, list[TextInput], list[PreTokenizedInput]]] = None"}, {"name": "text_target", "val": ": Union[TextInput, PreTokenizedInput, list[TextInput], list[PreTokenizedInput], None] = None"}, {"name": "text_pair_target", "val": ": Optional[Union[TextInput, PreTokenizedInput, list[TextInput], list[PreTokenizedInput]]] = None"}, {"name": "add_special_tokens", "val": ": bool = True"}, {"name": "padding", "val": ": Union[bool, str, PaddingStrategy] = False"}, {"name": "truncation", "val": ": Union[bool, str, TruncationStrategy, None] = None"}, {"name": "max_length", "val": ": Optional[int] = None"}, {"name": "stride", "val": ": int = 0"}, {"name": "is_split_into_words", "val": ": bool = False"}, {"name": "pad_to_multiple_of", "val": ": Optional[int] = None"}, {"name": "padding_side", "val": ": Optional[str] = None"}, {"name": "return_tensors", "val": ": Optional[Union[str, TensorType]] = None"}, {"name": "return_token_type_ids", "val": ": Optional[bool] = None"}, {"name": "return_attention_mask", "val": ": Optional[bool] = None"}, {"name": "return_overflowing_tokens", "val": ": bool = False"}, {"name": "return_special_tokens_mask", "val": ": bool = False"}, {"name": "return_offsets_mapping", "val": ": bool = False"}, {"name": "return_length", "val": ": bool = False"}, {"name": "verbose", "val": ": bool = True"}, {"name": "tokenizer_kwargs", "val": ": Optional[dict[str, Any]] = None"}, {"name": "**kwargs", "val": ""}]- **text** (`str`, `list[str]`, `list[list[str]]`, *optional*) --
  The sequence or batch of sequences to be encoded. Each sequence can be a string or a list of strings
  (pretokenized string). If the sequences are provided as list of strings (pretokenized), you must set
  `is_split_into_words=True` (to lift the ambiguity with a batch of sequences).
- **text_pair** (`str`, `list[str]`, `list[list[str]]`, *optional*) --
  The sequence or batch of sequences to be encoded. Each sequence can be a string or a list of strings
  (pretokenized string). If the sequences are provided as list of strings (pretokenized), you must set
  `is_split_into_words=True` (to lift the ambiguity with a batch of sequences).
- **text_target** (`str`, `list[str]`, `list[list[str]]`, *optional*) --
  The sequence or batch of sequences to be encoded as target texts. Each sequence can be a string or a
  list of strings (pretokenized string). If the sequences are provided as list of strings (pretokenized),
  you must set `is_split_into_words=True` (to lift the ambiguity with a batch of sequences).
- **text_pair_target** (`str`, `list[str]`, `list[list[str]]`, *optional*) --
  The sequence or batch of sequences to be encoded as target texts. Each sequence can be a string or a
  list of strings (pretokenized string). If the sequences are provided as list of strings (pretokenized),
  you must set `is_split_into_words=True` (to lift the ambiguity with a batch of sequences).
- **tokenizer_kwargs** (`dict[str, Any]`, *optional*) --
  Additional kwargs to pass to the tokenizer. These will be merged with the explicit parameters and
  other kwargs, with explicit parameters taking precedence.

- **add_special_tokens** (`bool`, *optional*, defaults to `True`) --
  Whether or not to add special tokens when encoding the sequences. This will use the underlying
  `PretrainedTokenizerBase.build_inputs_with_special_tokens` function, which defines which tokens are
  automatically added to the input ids. This is useful if you want to add `bos` or `eos` tokens
  automatically.
- **padding** (`bool`, `str` or [PaddingStrategy](/docs/transformers/v5.0.0rc1/en/internal/file_utils#transformers.utils.PaddingStrategy), *optional*, defaults to `False`) --
  Activates and controls padding. Accepts the following values:

  - `True` or `'longest'`: Pad to the longest sequence in the batch (or no padding if only a single
    sequence is provided).
  - `'max_length'`: Pad to a maximum length specified with the argument `max_length` or to the maximum
    acceptable input length for the model if that argument is not provided.
  - `False` or `'do_not_pad'` (default): No padding (i.e., can output a batch with sequences of different
    lengths).
- **truncation** (`bool`, `str` or [TruncationStrategy](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.tokenization_utils_base.TruncationStrategy), *optional*, defaults to `False`) --
  Activates and controls truncation. Accepts the following values:

  - `True` or `'longest_first'`: Truncate to a maximum length specified with the argument `max_length` or
    to the maximum acceptable input length for the model if that argument is not provided. This will
    truncate token by token, removing a token from the longest sequence in the pair if a pair of
    sequences (or a batch of pairs) is provided.
  - `'only_first'`: Truncate to a maximum length specified with the argument `max_length` or to the
    maximum acceptable input length for the model if that argument is not provided. This will only
    truncate the first sequence of a pair if a pair of sequences (or a batch of pairs) is provided.
  - `'only_second'`: Truncate to a maximum length specified with the argument `max_length` or to the
    maximum acceptable input length for the model if that argument is not provided. This will only
    truncate the second sequence of a pair if a pair of sequences (or a batch of pairs) is provided.
  - `False` or `'do_not_truncate'` (default): No truncation (i.e., can output batch with sequence lengths
    greater than the model maximum admissible input size).
- **max_length** (`int`, *optional*) --
  Controls the maximum length to use by one of the truncation/padding parameters.

  If left unset or set to `None`, this will use the predefined model maximum length if a maximum length
  is required by one of the truncation/padding parameters. If the model has no specific maximum input
  length (like XLNet) truncation/padding to a maximum length will be deactivated.
- **stride** (`int`, *optional*, defaults to 0) --
  If set to a number along with `max_length`, the overflowing tokens returned when
  `return_overflowing_tokens=True` will contain some tokens from the end of the truncated sequence
  returned to provide some overlap between truncated and overflowing sequences. The value of this
  argument defines the number of overlapping tokens.
- **is_split_into_words** (`bool`, *optional*, defaults to `False`) --
  Whether or not the input is already pre-tokenized (e.g., split into words). If set to `True`, the
  tokenizer assumes the input is already split into words (for instance, by splitting it on whitespace)
  which it will tokenize. This is useful for NER or token classification.
- **pad_to_multiple_of** (`int`, *optional*) --
  If set will pad the sequence to a multiple of the provided value. Requires `padding` to be activated.
  This is especially useful to enable the use of Tensor Cores on NVIDIA hardware with compute capability
  `>= 7.5` (Volta).
- **padding_side** (`str`, *optional*) --
  The side on which the model should have padding applied. Should be selected between ['right', 'left'].
  Default value is picked from the class attribute of the same name.
- **return_tensors** (`str` or [TensorType](/docs/transformers/v5.0.0rc1/en/internal/file_utils#transformers.TensorType), *optional*) --
  If set, will return tensors instead of list of python integers. Acceptable values are:

  - `'pt'`: Return PyTorch `torch.Tensor` objects.
  - `'np'`: Return Numpy `np.ndarray` objects.

- **return_token_type_ids** (`bool`, *optional*) --
  Whether to return token type IDs. If left to the default, will return the token type IDs according to
  the specific tokenizer's default, defined by the `return_outputs` attribute.

  [What are token type IDs?](../glossary#token-type-ids)
- **return_attention_mask** (`bool`, *optional*) --
  Whether to return the attention mask. If left to the default, will return the attention mask according
  to the specific tokenizer's default, defined by the `return_outputs` attribute.

  [What are attention masks?](../glossary#attention-mask)
- **return_overflowing_tokens** (`bool`, *optional*, defaults to `False`) --
  Whether or not to return overflowing token sequences. If a pair of sequences of input ids (or a batch
  of pairs) is provided with `truncation_strategy = longest_first` or `True`, an error is raised instead
  of returning overflowing tokens.
- **return_special_tokens_mask** (`bool`, *optional*, defaults to `False`) --
  Whether or not to return special tokens mask information.
- **return_offsets_mapping** (`bool`, *optional*, defaults to `False`) --
  Whether or not to return `(char_start, char_end)` for each token.

  This is only available on fast tokenizers inheriting from [PreTrainedTokenizerFast](/docs/transformers/v5.0.0rc1/en/main_classes/tokenizer#transformers.TokenizersBackend), if using
  Python's tokenizer, this method will raise `NotImplementedError`.
- **return_length**  (`bool`, *optional*, defaults to `False`) --
  Whether or not to return the lengths of the encoded inputs.
- **verbose** (`bool`, *optional*, defaults to `True`) --
  Whether or not to print more information and warnings.
- ****kwargs** -- passed to the `self.tokenize()` method0[BatchEncoding](/docs/transformers/v5.0.0rc1/en/main_classes/tokenizer#transformers.BatchEncoding)A [BatchEncoding](/docs/transformers/v5.0.0rc1/en/main_classes/tokenizer#transformers.BatchEncoding) with the following fields:

- **input_ids** -- List of token ids to be fed to a model.

  [What are input IDs?](../glossary#input-ids)

- **token_type_ids** -- List of token type ids to be fed to a model (when `return_token_type_ids=True` or
  if *"token_type_ids"* is in `self.model_input_names`).

  [What are token type IDs?](../glossary#token-type-ids)

- **attention_mask** -- List of indices specifying which tokens should be attended to by the model (when
  `return_attention_mask=True` or if *"attention_mask"* is in `self.model_input_names`).

  [What are attention masks?](../glossary#attention-mask)

- **overflowing_tokens** -- List of overflowing tokens sequences (when a `max_length` is specified and
  `return_overflowing_tokens=True`).
- **num_truncated_tokens** -- Number of tokens truncated (when a `max_length` is specified and
  `return_overflowing_tokens=True`).
- **special_tokens_mask** -- List of 0s and 1s, with 1 specifying added special tokens and 0 specifying
  regular sequence tokens (when `add_special_tokens=True` and `return_special_tokens_mask=True`).
- **length** -- The length of the inputs (when `return_length=True`)

Main method to tokenize and prepare for the model one or several sequence(s) or one or several pair(s) of
sequences.

**Parameters:**

pad_token (`str`, *optional*, defaults to `""`) : The token used for padding, for example when batching sequences of different lengths.

unk_token (`str`, *optional*, defaults to `""`) : The unknown token. A token that is not in the vocabulary cannot be converted to an ID and is set to be this token instead.

max_length (`int`, *optional*, defaults to 1024) : The maximum length of the sequences when encoding. Sequences longer than this will be truncated.

offset (`int`, *optional*, defaults to 0) : The offset of the tokenizer.

**Returns:**

`[BatchEncoding](/docs/transformers/v5.0.0rc1/en/main_classes/tokenizer#transformers.BatchEncoding)`

A [BatchEncoding](/docs/transformers/v5.0.0rc1/en/main_classes/tokenizer#transformers.BatchEncoding) with the following fields:

- **input_ids** -- List of token ids to be fed to a model.

  [What are input IDs?](../glossary#input-ids)

- **token_type_ids** -- List of token type ids to be fed to a model (when `return_token_type_ids=True` or
  if *"token_type_ids"* is in `self.model_input_names`).

  [What are token type IDs?](../glossary#token-type-ids)

- **attention_mask** -- List of indices specifying which tokens should be attended to by the model (when
  `return_attention_mask=True` or if *"attention_mask"* is in `self.model_input_names`).

  [What are attention masks?](../glossary#attention-mask)

- **overflowing_tokens** -- List of overflowing tokens sequences (when a `max_length` is specified and
  `return_overflowing_tokens=True`).
- **num_truncated_tokens** -- Number of tokens truncated (when a `max_length` is specified and
  `return_overflowing_tokens=True`).
- **special_tokens_mask** -- List of 0s and 1s, with 1 specifying added special tokens and 0 specifying
  regular sequence tokens (when `add_special_tokens=True` and `return_special_tokens_mask=True`).
- **length** -- The length of the inputs (when `return_length=True`)

## DiaFeatureExtractor[[transformers.DiaFeatureExtractor]]

#### transformers.DiaFeatureExtractor[[transformers.DiaFeatureExtractor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/dia/feature_extraction_dia.py#L29)

Constructs an Dia feature extractor.

This feature extractor inherits from [SequenceFeatureExtractor](/docs/transformers/v5.0.0rc1/en/main_classes/feature_extractor#transformers.SequenceFeatureExtractor) which contains
most of the main methods. Users should refer to this superclass for more information regarding those methods.

__call__transformers.DiaFeatureExtractor.__call__https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/dia/feature_extraction_dia.py#L60[{"name": "raw_audio", "val": ": typing.Union[numpy.ndarray, list[float], list[numpy.ndarray], list[list[float]]]"}, {"name": "padding", "val": ": typing.Union[bool, str, transformers.utils.generic.PaddingStrategy, NoneType] = None"}, {"name": "truncation", "val": ": typing.Optional[bool] = False"}, {"name": "max_length", "val": ": typing.Optional[int] = None"}, {"name": "return_tensors", "val": ": typing.Union[str, transformers.utils.generic.TensorType, NoneType] = None"}, {"name": "sampling_rate", "val": ": typing.Optional[int] = None"}]- **raw_audio** (`np.ndarray`, `list[float]`, `list[np.ndarray]`, `list[list[float]]`) --
  The sequence or batch of sequences to be processed. Each sequence can be a numpy array, a list of float
  values, a list of numpy arrays or a list of list of float values. The numpy array must be of shape
  `(num_samples,)` for mono audio (`feature_size = 1`), or `(2, num_samples)` for stereo audio
  (`feature_size = 2`).
- **padding** (`bool`, `str` or [PaddingStrategy](/docs/transformers/v5.0.0rc1/en/internal/file_utils#transformers.utils.PaddingStrategy), *optional*, defaults to `True`) --
  Select a strategy to pad the returned sequences (according to the model's padding side and padding
  index) among:

  - `True` or `'longest'`: Pad to the longest sequence in the batch (or no padding if only a single
    sequence if provided).
  - `'max_length'`: Pad to a maximum length specified with the argument `max_length` or to the maximum
    acceptable input length for the model if that argument is not provided.
  - `False` or `'do_not_pad'` (default): No padding (i.e., can output a batch with sequences of different
    lengths).
- **truncation** (`bool`, *optional*, defaults to `False`) --
  Activates truncation to cut input sequences longer than `max_length` to `max_length`.
- **max_length** (`int`, *optional*) --
  Maximum length of the returned list and optionally padding length (see above).
- **return_tensors** (`str` or [TensorType](/docs/transformers/v5.0.0rc1/en/internal/file_utils#transformers.TensorType), *optional*, default to 'pt') --
  If set, will return tensors instead of list of python integers. Acceptable values are:

  - `'pt'`: Return PyTorch `torch.Tensor` objects.
  - `'np'`: Return Numpy `np.ndarray` objects.
- **sampling_rate** (`int`, *optional*) --
  The sampling rate at which the `audio` input was sampled. It is strongly recommended to pass
  `sampling_rate` at the forward call to prevent silent errors.0

Main method to featurize and prepare for the model one or several sequence(s).

**Parameters:**

feature_size (`int`, *optional*, defaults to 1) : The feature dimension of the extracted features. Use 1 for mono, 2 for stereo.

sampling_rate (`int`, *optional*, defaults to 16000) : The sampling rate at which the audio waveform should be digitalized, expressed in hertz (Hz).

padding_value (`float`, *optional*, defaults to 0.0) : The value that is used for padding.

hop_length (`int`, *optional*, defaults to 512) : Overlap length between successive windows.

## DiaProcessor[[transformers.DiaProcessor]]

#### transformers.DiaProcessor[[transformers.DiaProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/dia/processing_dia.py#L64)

Constructs a Dia processor which wraps a [DiaFeatureExtractor](/docs/transformers/v5.0.0rc1/en/model_doc/dia#transformers.DiaFeatureExtractor), [DiaTokenizer](/docs/transformers/v5.0.0rc1/en/model_doc/dia#transformers.DiaTokenizer), and a [DacModel](/docs/transformers/v5.0.0rc1/en/model_doc/dac#transformers.DacModel) into
a single processor. It inherits, the audio feature extraction, tokenizer, and audio encode/decode functio-
nalities. See [__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/dia#transformers.DiaProcessor.__call__), `~DiaProcessor.encode`, and [decode()](/docs/transformers/v5.0.0rc1/en/model_doc/dia#transformers.DiaProcessor.decode) for more
information.

__call__transformers.DiaProcessor.__call__https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/dia/processing_dia.py#L85[{"name": "text", "val": ": typing.Union[str, list[str]]"}, {"name": "audio", "val": ": typing.Union[numpy.ndarray, ForwardRef('torch.Tensor'), collections.abc.Sequence[numpy.ndarray], collections.abc.Sequence['torch.Tensor'], NoneType] = None"}, {"name": "output_labels", "val": ": typing.Optional[bool] = False"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.models.dia.processing_dia.DiaProcessorKwargs]"}]

Main method to prepare text(s) and audio to be fed as input to the model. The `audio` argument is
forwarded to the DiaFeatureExtractor's [__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/dia#transformers.DiaFeatureExtractor.__call__) and subsequently to the
DacModel's [encode()](/docs/transformers/v5.0.0rc1/en/model_doc/dac#transformers.DacModel.encode). The `text` argument to [__call__()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__). Please refer
to the docstring of the above methods for more information.

**Parameters:**

feature_extractor (`DiaFeatureExtractor`) : An instance of [DiaFeatureExtractor](/docs/transformers/v5.0.0rc1/en/model_doc/dia#transformers.DiaFeatureExtractor). The feature extractor is a required input.

tokenizer (`DiaTokenizer`) : An instance of [DiaTokenizer](/docs/transformers/v5.0.0rc1/en/model_doc/dia#transformers.DiaTokenizer). The tokenizer is a required input.

audio_tokenizer (`DacModel`) : An instance of [DacModel](/docs/transformers/v5.0.0rc1/en/model_doc/dac#transformers.DacModel) used to encode/decode audio into/from codebooks. It is is a required input.
#### batch_decode[[transformers.DiaProcessor.batch_decode]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/dia/processing_dia.py#L256)

Decodes a batch of audio codebook sequences into their respective audio waveforms via the
`audio_tokenizer`. See [decode()](/docs/transformers/v5.0.0rc1/en/model_doc/dac#transformers.DacModel.decode) for more information.

**Parameters:**

decoder_input_ids (`torch.Tensor`) : The complete output sequence of the decoder.

audio_prompt_len (`int`) : The audio prefix length (e.g. when using voice cloning).
#### decode[[transformers.DiaProcessor.decode]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/dia/processing_dia.py#L327)

Decodes a single sequence of audio codebooks into the respective audio waveform via the
`audio_tokenizer`. See [decode()](/docs/transformers/v5.0.0rc1/en/model_doc/dac#transformers.DacModel.decode) and [batch_decode()](/docs/transformers/v5.0.0rc1/en/model_doc/dia#transformers.DiaProcessor.batch_decode) for more information.

## DiaModel[[transformers.DiaModel]]

#### transformers.DiaModel[[transformers.DiaModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/dia/modeling_dia.py#L683)

The bare Dia model outputting raw hidden-states without any specific head on top.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.DiaModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/dia/modeling_dia.py#L691[{"name": "input_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "attention_mask", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "decoder_input_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "decoder_position_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "decoder_attention_mask", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "encoder_outputs", "val": ": typing.Union[transformers.modeling_outputs.BaseModelOutput, tuple, NoneType] = None"}, {"name": "past_key_values", "val": ": typing.Optional[transformers.cache_utils.EncoderDecoderCache] = None"}, {"name": "use_cache", "val": ": typing.Optional[bool] = None"}, {"name": "output_attentions", "val": ": typing.Optional[bool] = None"}, {"name": "output_hidden_states", "val": ": typing.Optional[bool] = None"}, {"name": "cache_position", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "**kwargs", "val": ""}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **attention_mask** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.

  [What are attention masks?](../glossary#attention-mask)
- **decoder_input_ids** (`torch.LongTensor` of shape `(batch_size * num_codebooks, target_sequence_length) --
- **or** (batch_size, target_sequence_length, num_codebooks)`, *optional*) --
  1. (batch_size * num_codebooks, target_sequence_length): corresponds to the general use case where
  the audio input codebooks are flattened into the batch dimension. This also aligns with the flat-
  tened audio logits which are used to calculate the loss.

  2. (batch_size, sequence_length, num_codebooks): corresponds to the internally used shape of
  Dia to calculate embeddings and subsequent steps more efficiently.

  If no `decoder_input_ids` are provided, it will create a tensor of `bos_token_id` with shape
  `(batch_size, 1, num_codebooks)`. Indices can be obtained using the [DiaProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/dia#transformers.DiaProcessor). See
  [DiaProcessor.__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/dia#transformers.DiaProcessor.__call__) for more details.

  [What are decoder input IDs?](../glossary#decoder-input-ids)
- **decoder_position_ids** (`torch.LongTensor` of shape `(batch_size, target_sequence_length)`) --
  Indices of positions of each input sequence tokens in the position embeddings.
  Used to calculate the position embeddings up to `config.decoder_config.max_position_embeddings`.

  [What are position IDs?](../glossary#position-ids)
- **decoder_attention_mask** (`torch.LongTensor` of shape `(batch_size, target_sequence_length)`, *optional*) --
  Mask to avoid performing attention on certain token indices. By default, a causal mask will be used, to
  make sure the model can only look at previous inputs in order to predict the future.
- **encoder_outputs** (`Union[~modeling_outputs.BaseModelOutput, tuple, NoneType]`) --
  Tuple consists of (`last_hidden_state`, *optional*: `hidden_states`, *optional*: `attentions`)
  `last_hidden_state` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) is a sequence of
  hidden-states at the output of the last layer of the encoder. Used in the cross-attention of the decoder.
- **past_key_values** (`~cache_utils.EncoderDecoderCache`, *optional*) --
  Pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention
  blocks) that can be used to speed up sequential decoding. This typically consists in the `past_key_values`
  returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.

  Only [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).
  If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.

  The model will output the same cache format that is fed as input.

  If `past_key_values` are used, the user is expected to input only unprocessed `input_ids` (those that don't
  have their past key value states given to this model) of shape `(batch_size, unprocessed_length)` instead of all `input_ids`
  of shape `(batch_size, sequence_length)`.
- **use_cache** (`bool`, *optional*) --
  If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
  `past_key_values`).
- **output_attentions** (`bool`, *optional*) --
  Whether or not to return the attentions tensors of all attention layers. See `attentions` under returned
  tensors for more detail.
- **output_hidden_states** (`bool`, *optional*) --
  Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
  more detail.
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.0[transformers.modeling_outputs.Seq2SeqModelOutput](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.Seq2SeqModelOutput) or `tuple(torch.FloatTensor)`A [transformers.modeling_outputs.Seq2SeqModelOutput](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.Seq2SeqModelOutput) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration (`None`) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the decoder of the model.

  If `past_key_values` is used only the last hidden-state of the sequences of shape `(batch_size, 1,
  hidden_size)` is output.
- **past_key_values** (`EncoderDecoderCache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [EncoderDecoderCache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.EncoderDecoderCache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

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
The [DiaModel](/docs/transformers/v5.0.0rc1/en/model_doc/dia#transformers.DiaModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

**Parameters:**

config ([DiaConfig](/docs/transformers/v5.0.0rc1/en/model_doc/dia#transformers.DiaConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

`[transformers.modeling_outputs.Seq2SeqModelOutput](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.Seq2SeqModelOutput) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.Seq2SeqModelOutput](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.Seq2SeqModelOutput) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration (`None`) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the decoder of the model.

  If `past_key_values` is used only the last hidden-state of the sequences of shape `(batch_size, 1,
  hidden_size)` is output.
- **past_key_values** (`EncoderDecoderCache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [EncoderDecoderCache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.EncoderDecoderCache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

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

## DiaForConditionalGeneration[[transformers.DiaForConditionalGeneration]]

#### transformers.DiaForConditionalGeneration[[transformers.DiaForConditionalGeneration]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/dia/modeling_dia.py#L808)

The Dia model consisting of a (byte) text encoder and audio decoder with a prediction head on top.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.DiaForConditionalGeneration.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/dia/modeling_dia.py#L827[{"name": "input_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "attention_mask", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "decoder_input_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "decoder_position_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "decoder_attention_mask", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "encoder_outputs", "val": ": typing.Union[transformers.modeling_outputs.BaseModelOutput, tuple, NoneType] = None"}, {"name": "past_key_values", "val": ": typing.Optional[transformers.cache_utils.EncoderDecoderCache] = None"}, {"name": "use_cache", "val": ": typing.Optional[bool] = None"}, {"name": "output_attentions", "val": ": typing.Optional[bool] = None"}, {"name": "output_hidden_states", "val": ": typing.Optional[bool] = None"}, {"name": "labels", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "cache_position", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "**kwargs", "val": ""}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **attention_mask** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.

  [What are attention masks?](../glossary#attention-mask)
- **decoder_input_ids** (`torch.LongTensor` of shape `(batch_size * num_codebooks, target_sequence_length) --
- **or** (batch_size, target_sequence_length, num_codebooks)`, *optional*) --
  1. (batch_size * num_codebooks, target_sequence_length): corresponds to the general use case where
  the audio input codebooks are flattened into the batch dimension. This also aligns with the flat-
  tened audio logits which are used to calculate the loss.

  2. (batch_size, sequence_length, num_codebooks): corresponds to the internally used shape of
  Dia to calculate embeddings and subsequent steps more efficiently.

  If no `decoder_input_ids` are provided, it will create a tensor of `bos_token_id` with shape
  `(batch_size, 1, num_codebooks)`. Indices can be obtained using the [DiaProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/dia#transformers.DiaProcessor). See
  [DiaProcessor.__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/dia#transformers.DiaProcessor.__call__) for more details.

  [What are decoder input IDs?](../glossary#decoder-input-ids)
- **decoder_position_ids** (`torch.LongTensor` of shape `(batch_size, target_sequence_length)`) --
  Indices of positions of each input sequence tokens in the position embeddings.
  Used to calculate the position embeddings up to `config.decoder_config.max_position_embeddings`.

  [What are position IDs?](../glossary#position-ids)
- **decoder_attention_mask** (`torch.LongTensor` of shape `(batch_size, target_sequence_length)`, *optional*) --
  Mask to avoid performing attention on certain token indices. By default, a causal mask will be used, to
  make sure the model can only look at previous inputs in order to predict the future.
- **encoder_outputs** (`Union[~modeling_outputs.BaseModelOutput, tuple, NoneType]`) --
  Tuple consists of (`last_hidden_state`, *optional*: `hidden_states`, *optional*: `attentions`)
  `last_hidden_state` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) is a sequence of
  hidden-states at the output of the last layer of the encoder. Used in the cross-attention of the decoder.
- **past_key_values** (`~cache_utils.EncoderDecoderCache`, *optional*) --
  Pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention
  blocks) that can be used to speed up sequential decoding. This typically consists in the `past_key_values`
  returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.

  Only [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).
  If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.

  The model will output the same cache format that is fed as input.

  If `past_key_values` are used, the user is expected to input only unprocessed `input_ids` (those that don't
  have their past key value states given to this model) of shape `(batch_size, unprocessed_length)` instead of all `input_ids`
  of shape `(batch_size, sequence_length)`.
- **use_cache** (`bool`, *optional*) --
  If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
  `past_key_values`).
- **output_attentions** (`bool`, *optional*) --
  Whether or not to return the attentions tensors of all attention layers. See `attentions` under returned
  tensors for more detail.
- **output_hidden_states** (`bool`, *optional*) --
  Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
  more detail.
- **labels** (`torch.LongTensor` of shape `(batch_size * num_codebooks,)`, *optional*) --
  Labels for computing the masked language modeling loss. Indices should either be in
  `[0, ..., config.decoder_config.vocab_size - 1]` or -100. Tokens with indices set to `-100`
  are ignored (masked).
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.0[transformers.modeling_outputs.Seq2SeqLMOutput](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.Seq2SeqLMOutput) or `tuple(torch.FloatTensor)`A [transformers.modeling_outputs.Seq2SeqLMOutput](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.Seq2SeqLMOutput) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration (`None`) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss.
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **past_key_values** (`EncoderDecoderCache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [EncoderDecoderCache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.EncoderDecoderCache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

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
The [DiaForConditionalGeneration](/docs/transformers/v5.0.0rc1/en/model_doc/dia#transformers.DiaForConditionalGeneration) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

**Parameters:**

config ([DiaConfig](/docs/transformers/v5.0.0rc1/en/model_doc/dia#transformers.DiaConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

`[transformers.modeling_outputs.Seq2SeqLMOutput](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.Seq2SeqLMOutput) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.Seq2SeqLMOutput](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.Seq2SeqLMOutput) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration (`None`) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss.
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **past_key_values** (`EncoderDecoderCache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [EncoderDecoderCache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.EncoderDecoderCache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

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
#### generate[[transformers.DiaForConditionalGeneration.generate]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/dia/generation_dia.py#L415)

