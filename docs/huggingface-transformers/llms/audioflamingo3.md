# Source: https://huggingface.co/docs/transformers/v5.0.0/model_doc/audioflamingo3.md

# Audio Flamingo 3

## Overview

Audio Flamingo 3 (AF3) is a fully open large audio–language model designed for robust understanding and reasoning over speech, environmental sounds, and music. AF3 pairs a Whisper-style audio encoder with a causal language model and performs replace-in-place audio–text fusion: the processor aligns post-pool audio frames to a dedicated placeholder token and the model replaces those token slots with projected audio embeddings during the forward pass.

The model checkpoint is available at: [nvidia/audio-flamingo-3-hf](https://huggingface.co/nvidia/audio-flamingo-3-hf)

Highlights:

- Unified audio encoder across speech, sound, and music.
- **Long-audio support via windowing and post-pool alignment (up to 10 minutes maximum).** The model processes audio in 30-second windows with a hard limit of 20 windows (10 minutes total). Audio longer than 10 minutes will be truncated.
- Deterministic fusion that preserves sequence length by replacing audio placeholder tokens with audio embeddings.

This model was contributed by [Lasha Koroshinadze](https://huggingface.co/lashahub) and [Eric Bezzam](https://huggingface.co/bezzam).

### Paper

[Audio Flamingo 3](https://huggingface.co/papers/2507.08128): Advancing Audio Intelligence with Fully Open Large Audio Language Models  
A. Goel, S. Ghosh, J. Kim, S. Kumar, Z. Kong, S. Lee, C.-H. H. Yang, R. Duraiswami, D. Manocha, R. Valle, B. Catanzaro  
NVIDIA and University of Maryland  
Project: https://research.nvidia.com/labs/adlr/AF3/

## Usage

### Audio Instruct Mode

The model supports audio-text instructions, including multi-turn interactions, all processed in batches.

➡️ audio + text instruction

```python
from transformers import AudioFlamingo3ForConditionalGeneration, AutoProcessor

model_id = "nvidia/audio-flamingo-3-hf"
processor = AutoProcessor.from_pretrained(model_id)
model = AudioFlamingo3ForConditionalGeneration.from_pretrained(model_id, device_map="auto")

conversation = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "Transcribe the input speech."},
            {"type": "audio", "path": "https://huggingface.co/datasets/nvidia/AudioSkills/resolve/main/assets/WhDJDIviAOg_120_10.mp3"},
        ],
    }
]

inputs = processor.apply_chat_template(
    conversation,
    tokenize=True,
    add_generation_prompt=True,
    return_dict=True,
).to(model.device)

outputs = model.generate(**inputs, max_new_tokens=500)

decoded_outputs = processor.batch_decode(outputs[:, inputs.input_ids.shape[1]:], skip_special_tokens=True)
print(decoded_outputs)
```

➡️ multi-turn:

```python
from transformers import AudioFlamingo3ForConditionalGeneration, AutoProcessor

model_id = "nvidia/audio-flamingo-3-hf"
processor = AutoProcessor.from_pretrained(model_id)
model = AudioFlamingo3ForConditionalGeneration.from_pretrained(model_id, device_map="auto")

conversation = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Instruction: How does the tone of female speech change throughout the audio? Choose the correct option among the options below: (A) Sad to happy (B) Happy to sad (C) Neutral to happy (D) Happy to neutral.",
            },
            {"type": "audio", "path": "https://huggingface.co/datasets/nvidia/AudioSkills/resolve/main/assets/000000786159.31.wav"},
        ],
    },
    {
        "role": "assistant",
        "content": [{"type": "text", "text": "(A) Sad to happy"}],
    },
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "Why do you think so?"},
        ],
    },
]

inputs = processor.apply_chat_template(
    conversation,
    tokenize=True,
    add_generation_prompt=True,
    return_dict=True,
).to(model.device)

outputs = model.generate(**inputs, max_new_tokens=500)

decoded_outputs = processor.batch_decode(outputs[:, inputs.input_ids.shape[1]:], skip_special_tokens=True)
print(decoded_outputs)
```

➡️ text only:

```python
from transformers import AudioFlamingo3ForConditionalGeneration, AutoProcessor

model_id = "nvidia/audio-flamingo-3-hf"
processor = AutoProcessor.from_pretrained(model_id)
model = AudioFlamingo3ForConditionalGeneration.from_pretrained(model_id, device_map="auto")

conversation = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "What is the capital of France?"},
        ],
    }
]

inputs = processor.apply_chat_template(
    conversation,
    tokenize=True,
    add_generation_prompt=True,
    return_dict=True,
).to(model.device)

outputs = model.generate(**inputs, max_new_tokens=500)

decoded_outputs = processor.batch_decode(outputs[:, inputs.input_ids.shape[1]:], skip_special_tokens=True)
print(decoded_outputs)
```

➡️ audio only:

```python
from transformers import AudioFlamingo3ForConditionalGeneration, AutoProcessor

model_id = "nvidia/audio-flamingo-3-hf"
processor = AutoProcessor.from_pretrained(model_id)
model = AudioFlamingo3ForConditionalGeneration.from_pretrained(model_id, device_map="auto")

conversation = [
    {
        "role": "user",
        "content": [
            {"type": "audio", "path": "https://huggingface.co/datasets/nvidia/AudioSkills/resolve/main/assets/WhDJDIviAOg_120_10.mp3"},
        ],
    }
]

inputs = processor.apply_chat_template(
    conversation,
    tokenize=True,
    add_generation_prompt=True,
    return_dict=True,
).to(model.device)

outputs = model.generate(**inputs, max_new_tokens=500)

decoded_outputs = processor.batch_decode(outputs[:, inputs.input_ids.shape[1]:], skip_special_tokens=True)
print(decoded_outputs)
```

➡️ batched inference!

```python
from transformers import AudioFlamingo3ForConditionalGeneration, AutoProcessor

model_id = "nvidia/audio-flamingo-3-hf"
processor = AutoProcessor.from_pretrained(model_id)
model = AudioFlamingo3ForConditionalGeneration.from_pretrained(model_id, device_map="auto")

conversations = [
    [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Transcribe the input speech."},
                {
                    "type": "audio",
                    "path": "https://huggingface.co/datasets/nvidia/AudioSkills/resolve/main/assets/t_837b89f2-26aa-4ee2-bdf6-f73f0dd59b26.wav",
                },
            ],
        }
    ],
    [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "This track feels really peaceful and introspective. What elements make it feel so calming and meditative?",
                },
                {"type": "audio", "path": "https://huggingface.co/datasets/nvidia/AudioSkills/resolve/main/assets/FPSbCAANfbJLVSwD.mp3"},
            ],
        }
    ],
]

inputs = processor.apply_chat_template(
    conversations,
    tokenize=True,
    add_generation_prompt=True,
    return_dict=True,
).to(model.device)

outputs = model.generate(**inputs, max_new_tokens=500)

decoded_outputs = processor.batch_decode(outputs[:, inputs.input_ids.shape[1]:], skip_special_tokens=True)
print(decoded_outputs)
```

➡️ Training:

```python
from transformers import AudioFlamingo3ForConditionalGeneration, AutoProcessor

model_id = "nvidia/audio-flamingo-3-hf"
processor = AutoProcessor.from_pretrained(model_id)
model = AudioFlamingo3ForConditionalGeneration.from_pretrained(model_id, device_map="auto")
model.train()

conversation = [
    [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Transcribe the input speech."},
                {"type": "audio", "path": "https://huggingface.co/datasets/nvidia/AudioSkills/resolve/main/assets/WhDJDIviAOg_120_10.mp3"},
            ],
        },
        {
            "role": "assistant",
            "content": [{"type": "text", "text": "The transcription of the audio is 'summer follows spring the days grow longer and the nights are warm'."}],
        }
    ],
    [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "This track feels really peaceful and introspective. What elements make it feel so calming and meditative?",
                },
                {"type": "audio", "path": "https://huggingface.co/datasets/nvidia/AudioSkills/resolve/main/assets/FPSbCAANfbJLVSwD.mp3"},
            ],
        },
        {
            "role": "assistant",
            "content": [{"type": "text", "text": "The transcription of the audio is 'some transcription of the audio'."}],
        }

    ]
]

inputs = processor.apply_chat_template(
    conversation,
    tokenize=True,
    add_generation_prompt=True,
    return_dict=True,
    output_labels=True,
).to(model.device)

loss = model(**inputs).loss
loss.backward()
```

➡️ transcription shortcut

```python
from transformers import AudioFlamingo3ForConditionalGeneration, AutoProcessor

model_id = "nvidia/audio-flamingo-3-hf"
processor = AutoProcessor.from_pretrained(model_id)
model = AudioFlamingo3ForConditionalGeneration.from_pretrained(model_id, device_map="auto")

inputs = processor.apply_transcription_request(audio="https://huggingface.co/datasets/nvidia/AudioSkills/resolve/main/assets/t_837b89f2-26aa-4ee2-bdf6-f73f0dd59b26.wav").to(model.device)

outputs = model.generate(**inputs, max_new_tokens=500)
decoded_outputs = processor.batch_decode(outputs[:, inputs.input_ids.shape[1]:], skip_special_tokens=True, strip_prefix=True)

print(decoded_outputs)
```

The model is trained to emit transcriptions prefixed with assistant framing such as `The spoken content of the audio is "".`. Use `strip_prefix=True` (as shown above) to remove the fixed assistant sentence and surrounding quotes so that only the transcription remains.

## How the model works

### Architecture

* **AudioFlamingo3Encoder**
  Whisper-style feature extractor + encoder → average-pool over time (stride 2) → LayerNorm.
  Produces per-frame hidden states at the post-pool rate.

* **AudioFlamingo3MultiModalProjector**
  A small MLP that maps encoder features to the language model’s hidden size.

* **AudioFlamingo3ForConditionalGeneration**
  A causal language model that accepts text embeddings where each audio placeholder token slot is replaced, in place, by an audio frame embedding. No sequence-length change is introduced by fusion.

### Processor-level alignment

1. Each raw waveform is split into fixed-length windows based on the feature extractor’s `chunk_length` (seconds) and `sampling_rate` (Hz).
2. For each window, the processor computes the number of post-pool frames `post_pool_len` that the encoder will output (matching the conv/pool schedule).
3. The processor expands the audio placeholder token by the total number of post-pool frames across all windows.
4. The model later replaces those token positions with the corresponding projected audio embeddings.

## Usage patterns

### Transcription shortcut

For automatic speech recognition you can skip writing the default instruction each time and call
`apply_transcription_request()`:

```python
inputs = processor.apply_transcription_request(audio=audio_array)
```

Pass `prompt="Transcribe the input speech."` (or a list of prompts for batch audio) to customize the instruction while
keeping the audio placeholder handling.

`audio` accepts in-memory arrays, local file paths, or URLs. Any processor kwargs (`text_kwargs`, `audio_kwargs`, etc.)
are forwarded, so you can tweak padding or tensor formats just like when calling `processor(...)`.

## Long audio and windowing

**Important: Maximum audio length is 10 minutes.** Audio longer than this will be truncated.

* The default setup processes 30-second windows at 16 kHz mono.
* **The processor enforces a hard limit of 20 windows per sample, resulting in a maximum of 10 minutes of audio (20 windows × 30 seconds).**
* For each window:

  * `mel_len` is the padded mel length.
  * A conv stack reduces time as `conv_output_len = (mel_len - 1) // 2 + 1`.
  * Post-pool frames per window: `post_pool_len = (conv_output_len - 2) // 2 + 1`.
  * An audio placeholder token is expanded to the sum of `post_pool_len` across all windows.

## Padding, attention, and caching

* **Left padding vs right padding**
  For generation with mixed prompt lengths in a batch, left padding is usually preferable.
  For training, right padding is common; AF3’s fusion mechanism itself is padding-agnostic because it replaces in place.
* **Attention masks**
  The processor returns `attention_mask` (text) and `input_features_mask` (audio). The model builds an internal 4-D mask on the encoder’s pre-pool axis with negative infinity at pad positions.
* **Caching**
  During generation, `input_features` and `input_features_mask` are only passed on the first step. Subsequent steps use cached keys/values from the language model.

## Troubleshooting

* Empty or truncated outputs when batching
  Use left padding for batched generation and decode only the new tokens after the prompt length, as shown in the quickstart.

## AudioFlamingo3Config[[transformers.AudioFlamingo3Config]]

#### transformers.AudioFlamingo3Config[[transformers.AudioFlamingo3Config]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/audioflamingo3/configuration_audioflamingo3.py#L127)

This is the configuration class to store the configuration of an [AudioFlamingo3ForConditionalGeneration](/docs/transformers/v5.0.0/en/model_doc/audioflamingo3#transformers.AudioFlamingo3ForConditionalGeneration). It is used to instantiate an
AudioFlamingo3 model according to the specified arguments, defining the model architecture. Instantiating a configuration
with the defaults will yield a similar configuration to that of the AudioFlamingo3.

e.g. [nvidia/audio-flamingo-3-hf](https://huggingface.co/nvidia/audio-flamingo-3-hf)

Configuration objects inherit from [PretrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PretrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:

```python
>>> from transformers import AudioFlamingo3ForConditionalGeneration, AudioFlamingo3Config, AudioFlamingo3EncoderConfig, Qwen2Config

>>> # Initializing an AudioFlamingo3Encoder config
>>> audio_config = AudioFlamingo3EncoderConfig()

>>> # Initializing a Qwen2 config
>>> text_config = Qwen2Config()

>>> # Initializing an AudioFlamingo3 configuration
>>> configuration = AudioFlamingo3Config(audio_config, text_config)

>>> # Initializing a model from the audioflamingo3 style configuration
>>> model = AudioFlamingo3ForConditionalGeneration(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

audio_config (`Union[AudioFlamingo3EncoderConfig, dict]`, *optional*, defaults to `AudioFlamingo3EncoderConfig`) : The config object or dictionary of the audio backbone.

text_config (`Union[AutoConfig, dict]`, *optional*, defaults to `Qwen2Config`) : The config object or dictionary of the text backbone.

audio_token_id (`int`, *optional*, defaults to 151669) : The audio token index to encode the audio prompt.

projector_hidden_act (`str`, *optional*, defaults to `"gelu"`) : Activation function used in the projector.

projector_bias (`bool`, *optional*, defaults to `True`) : Whether to include bias terms in the projector.

## AudioFlamingo3EncoderConfig[[transformers.AudioFlamingo3EncoderConfig]]

#### transformers.AudioFlamingo3EncoderConfig[[transformers.AudioFlamingo3EncoderConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/audioflamingo3/configuration_audioflamingo3.py#L24)

This is the configuration class to store the configuration of an [AudioFlamingo3Encoder](/docs/transformers/v5.0.0/en/model_doc/audioflamingo3#transformers.AudioFlamingo3Encoder). It is used to instantiate an
AudioFlamingo3 audio encoder according to the specified arguments, defining the model architecture. Instantiating a
configuration with the defaults will yield a similar configuration to that of the audio encoder of the AudioFlamingo3
architecture.

e.g. [nvidia/audio-flamingo-3-hf](https://huggingface.co/nvidia/audio-flamingo-3-hf)

Configuration objects inherit from [PretrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PretrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:

```python
>>> from transformers import AudioFlamingo3EncoderConfig, AudioFlamingo3Encoder

>>> # Initializing an AudioFlamingo3EncoderConfig
>>> configuration = AudioFlamingo3EncoderConfig()

>>> # Initializing an AudioFlamingo3Encoder (with random weights)
>>> model = AudioFlamingo3Encoder(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

num_mel_bins (`int`, *optional*, defaults to 128) : Number of mel features used per input features. Should correspond to the value used in the `AudioFlamingo3Processor` class.

num_hidden_layers (`int`, *optional*, defaults to 32) : Number of encoder layers.

num_attention_heads (`int`, *optional*, defaults to 20) : Number of attention heads for each attention layer in the Transformer encoder.

intermediate_size (`int`, *optional*, defaults to 5120) : Dimensionality of the "intermediate" (often named feed-forward) layer in encoder.

layerdrop (`float`, *optional*, defaults to 0.0) : The LayerDrop probability for the encoder. See the [LayerDrop paper](https://huggingface.co/papers/1909.11556) for more details.

activation_function (`str`, *optional*, defaults to `"gelu"`) : The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`, `"relu"`, `"silu"` and `"gelu_new"` are supported.

hidden_size (`int`, *optional*, defaults to 1280) : Dimensionality of the layers.

dropout (`float`, *optional*, defaults to 0.0) : The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.

attention_dropout (`float`, *optional*, defaults to 0.0) : The dropout ratio for the attention probabilities.

activation_dropout (`float`, *optional*, defaults to 0.0) : The dropout ratio for activations inside the fully connected layer.

initializer_range (`float`, *optional*, defaults to 0.02) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

scale_embedding (`bool`, *optional*, defaults to `False`) : Scale embeddings by dividing by sqrt(hidden_size).

max_source_positions (`int`, *optional*, defaults to 1500) : The maximum sequence length of log-mel filter-bank features that this model might ever be used with.

## AudioFlamingo3Processor[[transformers.AudioFlamingo3Processor]]

#### transformers.AudioFlamingo3Processor[[transformers.AudioFlamingo3Processor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/audioflamingo3/processing_audioflamingo3.py#L52)

Constructs an AudioFlamingo3 processor which wraps an AudioFlamingo3 feature extractor and an AudioFlamingo3
tokenizer into a single processor.

[AudioFlamingo3Processor](/docs/transformers/v5.0.0/en/model_doc/audioflamingo3#transformers.AudioFlamingo3Processor) offers all the functionalities of [WhisperFeatureExtractor](/docs/transformers/v5.0.0/en/model_doc/whisper#transformers.WhisperFeatureExtractor) and
[Qwen2TokenizerFast](/docs/transformers/v5.0.0/en/model_doc/qwen2#transformers.Qwen2Tokenizer). See the [__call__()](/docs/transformers/v5.0.0/en/model_doc/audioflamingo3#transformers.AudioFlamingo3Processor.__call__) for more information.

__call__transformers.AudioFlamingo3Processor.__call__https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/audioflamingo3/processing_audioflamingo3.py#L96[{"name": "text", "val": ": str | list[str]"}, {"name": "audio", "val": ": typing.Union[numpy.ndarray, ForwardRef('torch.Tensor'), collections.abc.Sequence[numpy.ndarray], collections.abc.Sequence['torch.Tensor'], NoneType] = None"}, {"name": "output_labels", "val": ": bool | None = False"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.models.audioflamingo3.processing_audioflamingo3.AudioFlamingo3ProcessorKwargs]"}]- **text** (`str` or `list[str]`) --
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

audio_token (`Optional[str]`, *optional*, defaults to `""`) : Special token used to represent audio inputs in the chat template.

default_transcription_prompt (`str`, *optional*, defaults to `"Transcribe the input speech."`) : Default prompt to use for transcription tasks when applying transcription requests.

max_audio_len (`int`, *optional*, defaults to 600) : Maximum length of audio sequences in seconds. Audio longer than this will be truncated.

**Returns:**

`[BatchFeature](/docs/transformers/v5.0.0/en/main_classes/image_processor#transformers.BatchFeature)`

A dictionary with tokenized text (`input_ids`, `attention_mask`) and
audio features (`input_features`, `input_features_mask`).

## AudioFlamingo3Encoder[[transformers.AudioFlamingo3Encoder]]

#### transformers.AudioFlamingo3Encoder[[transformers.AudioFlamingo3Encoder]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/audioflamingo3/modeling_audioflamingo3.py#L272)

The audio model from AudioFlamingo3 without any head or projection on top.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.AudioFlamingo3Encoder.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/audioflamingo3/modeling_audioflamingo3.py#L324[{"name": "input_features", "val": ": Tensor"}, {"name": "input_features_mask", "val": ": torch.Tensor | None = None"}, {"name": "**kwargs", "val": ""}]- **input_features** (`torch.FloatTensor` of shape `(batch_size, feature_size, sequence_length)`) --
  Log-Mel features extracted from raw audio. Use the processor/feature extractor to compute and pad
  these features from waveform input.
- **input_features_mask** (`torch.FloatTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Mask to avoid performing attention on padding feature indices. Mask values selected in `[0, 1]`:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.0

**Parameters:**

config ([AudioFlamingo3EncoderConfig](/docs/transformers/v5.0.0/en/model_doc/audioflamingo3#transformers.AudioFlamingo3EncoderConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

## AudioFlamingo3ForConditionalGeneration[[transformers.AudioFlamingo3ForConditionalGeneration]]

#### transformers.AudioFlamingo3ForConditionalGeneration[[transformers.AudioFlamingo3ForConditionalGeneration]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/audioflamingo3/modeling_audioflamingo3.py#L416)

The AudioFlamingo3 model which consists of a fine-tuned Whisper encoder, a multi-modal projector and a Qwen2 language model.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.AudioFlamingo3ForConditionalGeneration.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/audioflamingo3/modeling_audioflamingo3.py#L484[{"name": "input_ids", "val": ": torch.LongTensor | None = None"}, {"name": "input_features", "val": ": torch.FloatTensor | None = None"}, {"name": "input_features_mask", "val": ": torch.Tensor | None = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.LongTensor | None = None"}, {"name": "past_key_values", "val": ": transformers.cache_utils.Cache | None = None"}, {"name": "inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "labels", "val": ": torch.LongTensor | None = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "cache_position", "val": ": torch.LongTensor | None = None"}, {"name": "logits_to_keep", "val": ": int | torch.Tensor = 0"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **input_features** (`torch.FloatTensor` of shape `(batch_size, sequence_length, feature_dim)`, *optional*) --
  The tensors corresponding to the input audio features. Audio features can be obtained using
  [WhisperFeatureExtractor](/docs/transformers/v5.0.0/en/model_doc/whisper#transformers.WhisperFeatureExtractor). See [WhisperFeatureExtractor.__call__()](/docs/transformers/v5.0.0/en/model_doc/whisper#transformers.WhisperFeatureExtractor.__call__) for details ([AudioFlamingo3Processor](/docs/transformers/v5.0.0/en/model_doc/audioflamingo3#transformers.AudioFlamingo3Processor) uses
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
elements depending on the configuration ([AudioFlamingo3Config](/docs/transformers/v5.0.0/en/model_doc/audioflamingo3#transformers.AudioFlamingo3Config)) and inputs.

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
The [AudioFlamingo3ForConditionalGeneration](/docs/transformers/v5.0.0/en/model_doc/audioflamingo3#transformers.AudioFlamingo3ForConditionalGeneration) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Example:

```python
>>> from transformers import AudioFlamingo3ForConditionalGeneration, AutoProcessor

>>> model_id = "nvidia/audio-flamingo-3-hf"
>>> processor = AutoProcessor.from_pretrained(model_id)
>>> model = AudioFlamingo3ForConditionalGeneration.from_pretrained(model_id, device_map="auto")

>>> conversations = [
>>>     [
>>>         {
>>>             "role": "user",
>>>             "content": [
>>>                 {"type": "text", "text": "Transcribe the input speech."},
>>>                 {
>>>                     "type": "audio",
>>>                     "path": "https://huggingface.co/datasets/nvidia/AudioSkills/resolve/main/assets/t_837b89f2-26aa-4ee2-bdf6-f73f0dd59b26.wav",
>>>                 },
>>>             ],
>>>         }
>>>     ],
>>>     [
>>>         {
>>>             "role": "user",
>>>             "content": [
>>>                 {
>>>                     "type": "text",
>>>                     "text": "This track feels really peaceful and introspective. What elements make it feel so calming and meditative?",
>>>                 },
>>>                 {"type": "audio", "path": "https://huggingface.co/datasets/nvidia/AudioSkills/resolve/main/assets/FPSbCAANfbJLVSwD.mp3"},
>>>             ],
>>>         }
>>>     ],
>>> ]

>>> inputs = processor.apply_chat_template(
>>>     conversations,
>>>     tokenize=True,
>>>     add_generation_prompt=True,
>>>     return_dict=True,
>>> ).to(model.device)

>>> outputs = model.generate(**inputs, max_new_tokens=500)

>>> decoded_outputs = processor.batch_decode(
>>>     outputs[:, inputs["input_ids"].shape[1]:], skip_special_tokens=True
>>> )
>>> print(decoded_outputs)
["The spoken content of the audio is...", "The track's calming and meditative feel can be attributed to..."]
```

**Parameters:**

config ([AudioFlamingo3ForConditionalGeneration](/docs/transformers/v5.0.0/en/model_doc/audioflamingo3#transformers.AudioFlamingo3ForConditionalGeneration)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

`[transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([AudioFlamingo3Config](/docs/transformers/v5.0.0/en/model_doc/audioflamingo3#transformers.AudioFlamingo3Config)) and inputs.

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
#### get_audio_features[[transformers.AudioFlamingo3ForConditionalGeneration.get_audio_features]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/audioflamingo3/modeling_audioflamingo3.py#L449)

This method is used to get the audio embeddings from input features (a log mel spectrogram), meaning inferring the audio encoder and the multi-modal projector.

Example:

```python
```

**Parameters:**

input_features (`torch.FloatTensor`) : Float values of mel features extracted from the raw speech waveform. Raw speech waveform can be obtained by loading a `.flac` or `.wav` audio file into an array of type `list[float]` or a `numpy.ndarray`, *e.g.* via the soundfile library (`pip install soundfile`). To prepare the array into `input_features`, the [AutoFeatureExtractor](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoFeatureExtractor) should be used for extracting the mel features, padding and conversion into a tensor of type `torch.FloatTensor`. See [__call__()](/docs/transformers/v5.0.0/en/model_doc/whisper#transformers.WhisperFeatureExtractor.__call__)

input_features_mask (`torch.Tensor` of shape `(batch_size, feature_sequence_length)`) : Mask to avoid performing attention on padded feature indices.

**Returns:**

`[transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([AudioFlamingo3Config](/docs/transformers/v5.0.0/en/model_doc/audioflamingo3#transformers.AudioFlamingo3Config)) and inputs.

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

