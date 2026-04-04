# Source: https://huggingface.co/docs/transformers/v5.0.0rc1/model_doc/qwen3_omni_moe.md

# Qwen3-Omni-MOE

## Overview

The Qwen3-Omni-MOE model is a unified multiple modalities model proposed in [Qwen3-Omni Technical Report](https://huggingface.co/papers/2509.17765) from Qwen team, Alibaba Group.

The abstract from the technical report is the following:

*We present Qwen3-Omni, a single multimodal model that, for the first time, maintains state-of-the-art performance across text, image, audio, and video without any degradation relative to single-modal counterparts. Qwen3-Omni matches the performance of same-sized single-modal models within the Qwen series and excels particularly on audio tasks. Across 36 audio and audio-visual benchmarks, Qwen3-Omni achieves open-source SOTA on 32 benchmarks and overall SOTA on 22, outperforming strong closed-source models such as Gemini-2.5-Pro, Seed-ASR, and GPT-4o-Transcribe. Qwen3-Omni adopts a Thinker-Talker MoE architecture that unifies perception and generation across text, images, audio, and video, yielding fluent text and natural real-time speech. It supports text interaction in 119 languages, speech understanding in 19 languages, and speech generation in 10 languages. To reduce first-packet latency in streaming synthesis, Talker autoregressively predicts discrete speech codecs using a multi-codebook scheme. Leveraging the representational capacity of these codebooks, we replace computationally intensive block-wise diffusion with a lightweight causal ConvNet, enabling streaming from the first codec frame. In cold-start settings, Qwen3-Omni achieves a theoretical end-to-end first-packet latency of 234 ms. To further strengthen multimodal reasoning, we introduce a Thinking model that explicitly reasons over inputs from any modality. Since the research community currently lacks a general-purpose audio captioning model, we fine-tuned Qwen3-Omni-30B-A3B to obtain Qwen3-Omni-30B-A3B-Captioner, which produces detailed, low-hallucination captions for arbitrary audio inputs. Qwen3-Omni-30B-A3B, Qwen3-Omni-30B-A3B-Thinking, and Qwen3-Omni-30B-A3B-Captioner are publicly released under the Apache 2.0 license.

## Notes

- Use [Qwen3OmniMoeForConditionalGeneration](/docs/transformers/v5.0.0rc1/en/model_doc/qwen3_omni_moe#transformers.Qwen3OmniMoeForConditionalGeneration) to generate audio and text output. To generate only one output type, use [Qwen3OmniMoeThinkerForConditionalGeneration](/docs/transformers/v5.0.0rc1/en/model_doc/qwen3_omni_moe#transformers.Qwen3OmniMoeThinkerForConditionalGeneration) for text-only and [Qwen3OmniMoeTalkerForConditionalGeneration](/docs/transformers/v5.0.0rc1/en/model_doc/qwen3_omni_moe#transformers.Qwen3OmniMoeTalkerForConditionalGeneration) for audio-only outputs.
- Audio generation with [Qwen3OmniMoeForConditionalGeneration](/docs/transformers/v5.0.0rc1/en/model_doc/qwen3_omni_moe#transformers.Qwen3OmniMoeForConditionalGeneration) supports only single batch size at the moment.
- In case out out-of-memory errors hwen working with video input, decrease `processor.max_pixels`. By default the maximum is set to a very arge value and high resolution visuals will not be resized, unless resolution exceeds `processor.max_pixels`.
- The processor has its own [apply_chat_template()](/docs/transformers/v5.0.0rc1/en/main_classes/processors#transformers.ProcessorMixin.apply_chat_template) method to convert chat messages to model inputs.

## Usage example

`Qwen3-Omni` can be found on the [Huggingface Hub](https://huggingface.co/Qwen).

### Single Media inference

The model can accept text, images, audio and videos as input. Here's an example code for inference.

```python
import soundfile as sf
from transformers import Qwen3OmniMoeForConditionalGeneration, Qwen3OmniMoeProcessor

model = Qwen3OmniMoeForConditionalGeneration.from_pretrained(
    "Qwen/Qwen3-Omni-30B-A3B-Instruct",
    dtype="auto",
    device_map="auto"
)
processor = Qwen3OmniMoeProcessor.from_pretrained("Qwen/Qwen3-Omni-30B-A3B-Instruct")

conversations = [
    {
        "role": "system",
        "content": [
            {"type": "text", "text": "You are Qwen, a virtual human developed by the Qwen Team, Alibaba Group, capable of perceiving auditory and visual inputs, as well as generating text and speech."}
        ],
    },
    {
        "role": "user",
        "content": [
            {"type": "video", "video": "/path/to/video.mp4"},
            {"type": "text", "text": "What cant you hear and see in this video?"},
        ],
    },
]

inputs = processor.apply_chat_template(
    conversations,
    load_audio_from_video=True,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
    fps=1,

    # kwargs to be passed to `Qwen3OmniMoeProcessor`
    padding=True,
    use_audio_in_video=True,
).to(model.device)

# Generation params for audio or text can be different and have to be prefixed with `thinker_` or `talker_`
text_ids, audio = model.generate(**inputs, use_audio_in_video=True, thinker_do_sample=False, talker_do_sample=True)
text = processor.batch_decode(text_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)

sf.write(
    "output.wav",
    audio.reshape(-1).detach().cpu().numpy(),
    samplerate=24000,
)
print(text)
```

### Text-only generation

To generate only text output and save compute by not loading the audio generation model, we can use `Qwen3OmniMoeThinkerForConditionalGeneration` model.

```python
from transformers import Qwen3OmniMoeThinkerForConditionalGeneration, Qwen3OmniMoeProcessor

model = Qwen3OmniMoeThinkerForConditionalGeneration.from_pretrained(
    "Qwen/Qwen3-Omni-30B-A3B-Instruct",
    dtype="auto",
    device_map="auto",
)
processor = Qwen3OmniMoeProcessor.from_pretrained("Qwen/Qwen3-Omni-30B-A3B-Instruct")

conversations = [
    {
        "role": "system",
        "content": [
            {"type": "text", "text": "You are Qwen, a virtual human developed by the Qwen Team, Alibaba Group, capable of perceiving auditory and visual inputs, as well as generating text and speech."}
        ],
    },
    {
        "role": "user",
        "content": [
            {"type": "video", "video": "/path/to/video.mp4"},
            {"type": "text", "text": "What cant you hear and see in this video?"},
        ],
    },
]

inputs = processor.apply_chat_template(
    conversations,
    load_audio_from_video=True,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
    fps=1,

    # kwargs to be passed to `Qwen3OmniMoeProcessor`
    padding=True,
    use_audio_in_video=True,
).to(model.device)

text_ids = model.generate(**inputs, use_audio_in_video=True)
text = processor.batch_decode(text_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)

sf.write(
    "output.wav",
    audio.reshape(-1).detach().cpu().numpy(),
    samplerate=24000,
)
print(text)
```

### Batch Mixed Media Inference

The model can batch inputs composed of mixed samples of various types such as text, images, audio and videos as input when using `Qwen3OmniMoeThinkerForConditionalGeneration` model. Here is an example.

```python
import soundfile as sf
from transformers import Qwen3OmniMoeForConditionalGeneration, Qwen3OmniMoeProcessor

model = Qwen3OmniMoeForConditionalGeneration.from_pretrained(
    "Qwen/Qwen3-Omni-30B-A3B-Instruct",
    dtype="auto",
    device_map="auto"
)
processor = Qwen3OmniMoeProcessor.from_pretrained("Qwen/Qwen3-Omni-30B-A3B-Instruct")

# Conversation with video only
conversation1 = [
    {
        "role": "system",
        "content": [
            {"type": "text", "text": "You are Qwen, a virtual human developed by the Qwen Team, Alibaba Group, capable of perceiving auditory and visual inputs, as well as generating text and speech."}
        ],
    },
    {
        "role": "user",
        "content": [
            {"type": "video", "path": "/path/to/video.mp4"},
        ]
    }
]

# Conversation with audio only
conversation2 = [
    {
        "role": "system",
        "content": [
            {"type": "text", "text": "You are Qwen, a virtual human developed by the Qwen Team, Alibaba Group, capable of perceiving auditory and visual inputs, as well as generating text and speech."}
        ],
    },
    {
        "role": "user",
        "content": [
            {"type": "audio", "path": "/path/to/audio.wav"},
        ]
    }
]

# Conversation with pure text
conversation3 = [
    {
        "role": "system",
        "content": [
            {"type": "text", "text": "You are Qwen, a virtual human developed by the Qwen Team, Alibaba Group, capable of perceiving auditory and visual inputs, as well as generating text and speech."}
        ],
    },
    {
        "role": "user",
        "content": [{"type": "text", "text": "who are you?"}],
    }
]

# Conversation with mixed media
conversation4 = [
    {
        "role": "system",
        "content": [
            {"type": "text", "text": "You are Qwen, a virtual human developed by the Qwen Team, Alibaba Group, capable of perceiving auditory and visual inputs, as well as generating text and speech."}
        ],
    },
    {
        "role": "user",
        "content": [
            {"type": "image", "path": "/path/to/image.jpg"},
            {"type": "video", "path": "/path/to/video.mp4"},
            {"type": "audio", "path": "/path/to/audio.wav"},
            {"type": "text", "text": "What are the elements can you see and hear in these medias?"},
        ],
    }
]

conversations = [conversation1, conversation2, conversation3, conversation4]

inputs = processor.apply_chat_template(
    conversations,
    load_audio_from_video=True,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
    fps=1,

    # kwargs to be passed to `Qwen3OmniMoeProcessor`
    padding=True,
    use_audio_in_video=True,
).to(model.thinker.device)

text_ids = model.generate(**inputs, use_audio_in_video=True)
text = processor.batch_decode(text_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)

print(text)
```

### Usage Tips

#### Image Resolution trade-off

The model supports a wide range of resolution inputs. By default, it uses the native resolution for input, but higher resolutions can enhance performance at the cost of more computation. Users can set the minimum and maximum number of pixels to achieve an optimal configuration for their needs.

```python
min_pixels = 128*28*28
max_pixels = 768*28*28
processor = AutoProcessor.from_pretrained("Qwen/Qwen3-Omni-30B-A3B-Instruct", min_pixels=min_pixels, max_pixels=max_pixels)
```

#### Prompt for audio output

If users need audio output, the system prompt must be set as "You are Qwen, a virtual human developed by the Qwen Team, Alibaba Group, capable of perceiving auditory and visual inputs, as well as generating text and speech.", otherwise the audio output may not work as expected.

```json
{
    "role": "system",
    "content": "You are Qwen, a virtual human developed by the Qwen Team, Alibaba Group, capable of perceiving auditory and visual inputs, as well as generating text and speech.",
}
```

#### Use audio output or not

The model supports both text and audio outputs, if users do not need audio outputs, they can set `enable_audio_output` in the `from_pretrained` function. This option will save about `~2GB` of GPU memory but the `return_audio` option for `generate` function will only allow to be set at `False`.

```python
model = Qwen3OmniMoeForConditionalGeneration.from_pretrained(
    "Qwen/Qwen3-Omni-30B-A3B-Instruct",
    dtype="auto",
    device_map="auto",
    enable_audio_output=False,
)
```

In order to obtain a flexible experience, we recommend that users set `enable_audio_output` at `True` when initializing the model through `from_pretrained` function, and then decide whether to return audio when `generate` function is called. When `return_audio` is set to `False`, the model will only return text outputs to get text responses faster.

```python
model = Qwen3OmniMoeForConditionalGeneration.from_pretrained(
    "Qwen/Qwen3-Omni-30B-A3B-Instruct",
    dtype="auto",
    device_map="auto",
    enable_audio_output=True,
)
...
text_ids = model.generate(**inputs, return_audio=False)
```

#### Change voice type of output audio

Qwen3-Omni-MOE supports the ability to change the voice of the output audio. Users can use the `spk` parameter of `generate` function to specify the voice type. The `"Qwen/Qwen3-Omni-30B-A3B-Instruct"` checkpoint support two voice types: `Chelsie` and `Ethan`, while `Chelsie` is a female voice and `Ethan` is a male voice. By default, if `spk` is not specified, the default voice type is `Chelsie`.

```python
text_ids, audio = model.generate(**inputs, spk="Chelsie")
```

```python
text_ids, audio = model.generate(**inputs, spk="Ethan")
```

#### Flash-Attention 2 to speed up generation

First, make sure to install the latest version of Flash Attention 2:

```bash
pip install -U flash-attn --no-build-isolation
```

Also, you should have hardware that is compatible with FlashAttention 2. Read more about it in the official documentation of the [flash attention repository](https://github.com/Dao-AILab/flash-attention). FlashAttention-2 can only be used when a model is loaded in `torch.float16` or `torch.bfloat16`.

To load and run a model using FlashAttention-2, add `attn_implementation="flash_attention_2"` when loading the model:

```python
from transformers import Qwen3OmniMoeForConditionalGeneration

model = Qwen3OmniMoeForConditionalGeneration.from_pretrained(
    "Qwen/Qwen3-Omni-30B-A3B-Instruct",
    device_map="auto",
    dtype=torch.bfloat16,
    attn_implementation="flash_attention_2",
)
```

## Qwen3OmniMoeConfig[[transformers.Qwen3OmniMoeConfig]]

#### transformers.Qwen3OmniMoeConfig[[transformers.Qwen3OmniMoeConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/configuration_qwen3_omni_moe.py#L1031)

This is the configuration class to store the configuration of a [Qwen3OmniMoeForConditionalGeneration](/docs/transformers/v5.0.0rc1/en/model_doc/qwen3_omni_moe#transformers.Qwen3OmniMoeForConditionalGeneration). It is used to instantiate a Qwen3Omni
model according to the specified sub-models configurations, defining the model architecture.

Instantiating a configuration with the defaults will yield a similar configuration to that of the
[Qwen/Qwen2.5-Omni-7B](https://huggingface.co/Qwen/Qwen2.5-Omni-7B) architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:

```python
>>> from transformers import (
...     Qwen3OmniMoeThinkerConfig,
...     Qwen3OmniMoeTalkerConfig,
...     Qwen3OmniMoeCode2WavConfig,
...     Qwen3OmniMoeForConditionalGeneration,
...     Qwen3OmniMoeConfig,
... )

>>> # Initializing a Qwen3OmniMoe style configuration
>>> configuration = Qwen3OmniMoeConfig()

>>> # Initializing a model from the configuration
>>> model = Qwen3OmniMoeForConditionalGeneration(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

get_text_configtransformers.Qwen3OmniMoeConfig.get_text_confighttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/configuration_qwen3_omni_moe.py#L1118[{"name": "decoder", "val": " = False"}]- **decoder** (`Optional[bool]`, *optional*, defaults to `False`) --
  If set to `True`, then only search for decoder config names.0

Returns the config that is meant to be used with text IO. On most models, it is the original config instance
itself. On specific composite models, it is under a set of valid names.

**Parameters:**

thinker_config (`dict`, *optional*) : Configuration of the underlying thinker sub-model.

talker_config (`dict`, *optional*) : Configuration of the underlying talker sub-model.

code2wav_config (`dict`, *optional*) : Configuration of the underlying code2wav sub-model.

enable_audio_output (`bool`, *optional*, defaults to `True`) : Whether enable audio output and load talker and code2wav module.

## Qwen3OmniMoeThinkerConfig[[transformers.Qwen3OmniMoeThinkerConfig]]

#### transformers.Qwen3OmniMoeThinkerConfig[[transformers.Qwen3OmniMoeThinkerConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/configuration_qwen3_omni_moe.py#L347)

This is the configuration class to store the configuration of a `Qwen3OmniMoeThinker`. It is used to instantiate a
Qwen3-Omni-Thinker model according to the specified arguments, defining the model architecture. Instantiating a
configuration with the defaults will yield a similar configuration to that of the thinker component of the Qwen3-Omni
architecture.

e.g. [Qwen/Qwen3-Omni-7B](https://huggingface.co/Qwen/Qwen3-Omni-7B)

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:

```python
>>> from transformers import Qwen3OmniMoeThinkerModel, Qwen3OmniMoeThinkerConfig

>>> # Initializing a default Qwen3OmniMoeThinkerConfig
>>> configuration = Qwen3OmniMoeThinkerConfig()

>>> # Initializing a model (with random weights) from the default configuration
>>> model = Qwen3OmniMoeThinkerModel(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

audio_config (`dict`, *optional*) : The config dictionary of the audio backbone.

vision_config (`dict`, *optional*) : The config dictionary of the vision backbone.

text_config (`dict`, *optional*) : The config dictionary of the text backbone.

audio_token_id (`int`, *optional*, defaults to 151646) : The audio token id to encode the audio prompt.

image_token_id (`int`, *optional*, defaults to 151655) : The image token id to encode the image prompt.

video_token_id (`int`, *optional*, defaults to 151656) : The video token id to encode the video prompt.

position_id_per_seconds (`int`, *optional*, defaults to 25) : The increment of position id per second.

audio_start_token_id (`int`, *optional*, defaults to 151647) : The audio start token id to encode the audio prompt.

user_token_id (`int`, *optional*, defaults to 872) : The user token id to encode the user token.

initializer_range (`float`, *optional*, defaults to 0.02) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

## Qwen3OmniMoeTalkerConfig[[transformers.Qwen3OmniMoeTalkerConfig]]

#### transformers.Qwen3OmniMoeTalkerConfig[[transformers.Qwen3OmniMoeTalkerConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/configuration_qwen3_omni_moe.py#L777)

This is the configuration class to store the configuration of a `Qwen3OmniMoeTalker`. It is used to instantiate a
Qwen3-Omni multi-modal talker model capable of handling text, audio, and vision modalities in a unified architecture.
The model integrates a text decoder with a code predictor for autoregressive generation of both semantic and acoustic
tokens, enabling speech and multimodal content generation. This configuration wraps sub-configurations for the text and
code predictor components, allowing modular setup and initialization.

e.g. [Qwen/Qwen3-Omni-7B](https://huggingface.co/Qwen/Qwen3-Omni-7B)

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:

```python
>>> from transformers import Qwen3OmniMoeTalkerConfig, Qwen3OmniMoeTalker

>>> # Initialize a Qwen3OmniMoeTalkerConfig with default sub-configurations
>>> config = Qwen3OmniMoeTalkerConfig(
...     num_code_groups=32,
...     thinker_hidden_size=2048,
... )

>>> # Initialize the full Qwen3-Omni Talker model
>>> model = Qwen3OmniMoeTalker(config)

>>> # Access the model configuration
>>> config = model.config
>>> print(config.text_config)  # Access text decoder configuration
>>> print(config.code_predictor_config)  # Access code predictor configuration
```

**Parameters:**

code_predictor_config (`dict`, *optional*) : A dictionary of configuration parameters used to initialize a `Qwen3OmniMoeTalkerCodePredictorConfig`. If not provided, defaults will be used.

text_config (`dict`, *optional*) : A dictionary of configuration parameters used to initialize a `Qwen3OmniMoeTalkerTextConfig`. If not provided, defaults will be used.

num_code_groups (`int`, *optional*, defaults to 32) : Number of codebook groups used in the predicted acoustic token sequence, corresponding to multi-codebook VQ representation.

thinker_hidden_size (`int`, *optional*, defaults to 2048) : Hidden dimension size of the thinker module used for intermediate reasoning or latent planning before audio generation.

codec_eos_token_id (`int`, *optional*, defaults to 4198) : Token ID representing the end-of-speech token in the codec-generated sequence.

accept_hidden_layer (`int`, *optional*, defaults to 18) : Index of the hidden layer whose output is used for accepting or refining generated tokens during think-and-speak process.

codec_nothink_id (`int`, *optional*, defaults to 4203) : Token ID indicating no thinking step is required during generation.

codec_think_bos_id (`int`, *optional*, defaults to 4204) : Token ID marking the beginning of a thinking sequence.

codec_think_eos_id (`int`, *optional*, defaults to 4205) : Token ID marking the end of a thinking sequence.

codec_pad_id (`int`, *optional*, defaults to 4196) : Padding token ID used in codec input sequences.

codec_bos_id (`int`, *optional*, defaults to 4197) : Beginning-of-speech token ID in codec sequences.

audio_token_id (`int`, *optional*, defaults to 151646) : Special token ID used to indicate the position of audio tokens in the input sequence.

image_token_id (`int`, *optional*, defaults to 151655) : Special token ID used to represent image inputs in the multimodal context.

video_token_id (`int`, *optional*, defaults to 151656) : Special token ID used to represent video inputs.

vision_start_token_id (`int`, *optional*, defaults to 151652) : Token ID indicating the start of a visual input sequence (e.g., image or video embeddings).

position_id_per_seconds (`int`, *optional*, defaults to 25) : Number of position IDs allocated per second of audio content, used for temporal alignment in generation.

audio_start_token_id (`int`, *optional*, defaults to 151669) : Token ID that indicates the start of an audio generation segment in the output.

speaker_id (`dict`, *optional*) : Speaker name to speaker id dict.

## Qwen3OmniMoeForConditionalGeneration[[transformers.Qwen3OmniMoeForConditionalGeneration]]

#### transformers.Qwen3OmniMoeForConditionalGeneration[[transformers.Qwen3OmniMoeForConditionalGeneration]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/modeling_qwen3_omni_moe.py#L3788)

## Qwen3OmniMoeThinkerTextModel[[transformers.Qwen3OmniMoeThinkerTextModel]]

#### transformers.Qwen3OmniMoeThinkerTextModel[[transformers.Qwen3OmniMoeThinkerTextModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/modeling_qwen3_omni_moe.py#L1646)

Text part of Qwen3OmniMoeThinker, not a pure text-only model, as DeepStack integrates visual features into the early hidden states.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.Qwen3OmniMoeThinkerTextModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/modeling_qwen3_omni_moe.py#L1672[{"name": "input_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "attention_mask", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "position_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "past_key_values", "val": ": typing.Optional[transformers.cache_utils.Cache] = None"}, {"name": "inputs_embeds", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "use_cache", "val": ": typing.Optional[bool] = None"}, {"name": "cache_position", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "visual_pos_masks", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "deepstack_visual_embeds", "val": ": typing.Optional[list[torch.Tensor]] = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.modeling_flash_attention_utils.FlashAttentionKwargs]"}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

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

  Only [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).
  If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.

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
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.
- **visual_pos_masks** (`torch.Tensor` of shape `(batch_size, seqlen)`, *optional*) --
  The mask of the visual positions.
- **deepstack_visual_embeds** (`list[torch.Tensor]`, *optional*) --
  The deepstack visual embeddings. The shape is (num_layers, visual_seqlen, embed_dim).
  The feature is extracted from the different visual encoder layers, and fed to the decoder
  hidden states. It's from the paper DeepStack(https://arxiv.org/abs/2406.04334).0[transformers.modeling_outputs.BaseModelOutputWithPast](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or `tuple(torch.FloatTensor)`A [transformers.modeling_outputs.BaseModelOutputWithPast](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Qwen3OmniMoeConfig](/docs/transformers/v5.0.0rc1/en/model_doc/qwen3_omni_moe#transformers.Qwen3OmniMoeConfig)) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.

  If `past_key_values` is used only the last hidden-state of the sequences of shape `(batch_size, 1,
  hidden_size)` is output.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

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
The [Qwen3OmniMoeThinkerTextModel](/docs/transformers/v5.0.0rc1/en/model_doc/qwen3_omni_moe#transformers.Qwen3OmniMoeThinkerTextModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

**Parameters:**

config (`Qwen3OmniMoeTextConfig`) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

`[transformers.modeling_outputs.BaseModelOutputWithPast](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutputWithPast](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Qwen3OmniMoeConfig](/docs/transformers/v5.0.0rc1/en/model_doc/qwen3_omni_moe#transformers.Qwen3OmniMoeConfig)) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.

  If `past_key_values` is used only the last hidden-state of the sequences of shape `(batch_size, 1,
  hidden_size)` is output.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

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

## Qwen3OmniMoeThinkerForConditionalGeneration[[transformers.Qwen3OmniMoeThinkerForConditionalGeneration]]

#### transformers.Qwen3OmniMoeThinkerForConditionalGeneration[[transformers.Qwen3OmniMoeThinkerForConditionalGeneration]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/modeling_qwen3_omni_moe.py#L1875)

The Qwen2.5OmniThinker model which consists of a audio backbone and a language model.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.Qwen3OmniMoeThinkerForConditionalGeneration.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/modeling_qwen3_omni_moe.py#L2022[{"name": "input_ids", "val": " = None"}, {"name": "input_features", "val": " = None"}, {"name": "pixel_values", "val": " = None"}, {"name": "pixel_values_videos", "val": " = None"}, {"name": "image_grid_thw", "val": " = None"}, {"name": "video_grid_thw", "val": " = None"}, {"name": "attention_mask", "val": " = None"}, {"name": "feature_attention_mask", "val": " = None"}, {"name": "audio_feature_lengths", "val": " = None"}, {"name": "position_ids", "val": " = None"}, {"name": "past_key_values", "val": " = None"}, {"name": "inputs_embeds", "val": " = None"}, {"name": "rope_deltas", "val": " = None"}, {"name": "labels", "val": " = None"}, {"name": "use_cache", "val": " = None"}, {"name": "output_router_logits", "val": ": typing.Optional[bool] = None"}, {"name": "use_audio_in_video", "val": " = None"}, {"name": "cache_position", "val": " = None"}, {"name": "video_second_per_grid", "val": " = None"}, {"name": "**kwargs", "val": ""}]- **input_ids** (`` of shape `(batch_size, sequence_length)`) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **input_features** (`` of shape `(batch_size, sequence_length, feature_dim)`) --
  The tensors corresponding to the input audio features. Audio features can be obtained using
  [WhisperFeatureExtractor](/docs/transformers/v5.0.0rc1/en/model_doc/whisper#transformers.WhisperFeatureExtractor). See [WhisperFeatureExtractor.__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/whisper#transformers.WhisperFeatureExtractor.__call__) for details ([Qwen3OmniMoeProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/qwen3_omni_moe#transformers.Qwen3OmniMoeProcessor) uses
  [WhisperFeatureExtractor](/docs/transformers/v5.0.0rc1/en/model_doc/whisper#transformers.WhisperFeatureExtractor) for processing audios).
- **pixel_values** (`` of shape `(batch_size, num_channels, image_size, image_size)`) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [Qwen2VLImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/qwen2_vl#transformers.Qwen2VLImageProcessor). See [Qwen2VLImageProcessor.__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details ([Qwen3OmniMoeProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/qwen3_omni_moe#transformers.Qwen3OmniMoeProcessor) uses
  [Qwen2VLImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/qwen2_vl#transformers.Qwen2VLImageProcessor) for processing images).
- **pixel_values_videos** (`` of shape `(batch_size, num_frames, num_channels, frame_size, frame_size)`) --
  The tensors corresponding to the input video. Pixel values for videos can be obtained using
  [Qwen2VLVideoProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/qwen2_vl#transformers.Qwen2VLVideoProcessor). See `Qwen2VLVideoProcessor.__call__()` for details ([Qwen3OmniMoeProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/qwen3_omni_moe#transformers.Qwen3OmniMoeProcessor) uses
  [Qwen2VLVideoProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/qwen2_vl#transformers.Qwen2VLVideoProcessor) for processing videos).
- **image_grid_thw** (`torch.LongTensor` of shape `(num_images, 3)`, *optional*) --
  The temporal, height and width of feature shape of each image in LLM.
- **video_grid_thw** (`torch.LongTensor` of shape `(num_videos, 3)`, *optional*) --
  The temporal, height and width of feature shape of each video in LLM.
- **attention_mask** (`` of shape `(batch_size, sequence_length)`) --
  Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.

  [What are attention masks?](../glossary#attention-mask)
- **feature_attention_mask** (`torch.Tensor` of shape `(batch_size, feature_sequence_length)`, *optional*) --
  Mask to avoid performing attention on padding feature indices. Mask values selected in `[0, 1]`:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.
- **audio_feature_lengths** (`torch.LongTensor` of shape `(num_audios)`, *optional*) --
  The length of feature shape of each audio in LLM.
- **position_ids** (`` of shape `(batch_size, sequence_length)`) --
  Indices of positions of each input sequence tokens in the position embeddings. Selected in the range `[0, config.n_positions - 1]`.

  [What are position IDs?](../glossary#position-ids)
- **past_key_values** (``) --
  Pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention
  blocks) that can be used to speed up sequential decoding. This typically consists in the `past_key_values`
  returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.

  Only [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).
  If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.

  The model will output the same cache format that is fed as input.

  If `past_key_values` are used, the user is expected to input only unprocessed `input_ids` (those that don't
  have their past key value states given to this model) of shape `(batch_size, unprocessed_length)` instead of all `input_ids`
  of shape `(batch_size, sequence_length)`.
- **inputs_embeds** (`` of shape `(batch_size, sequence_length, hidden_size)`) --
  Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation. This
  is useful if you want more control over how to convert `input_ids` indices into associated vectors than the
  model's internal embedding lookup matrix.
- **rope_deltas** (`torch.LongTensor` of shape `(batch_size, )`, *optional*) --
  The rope index difference between sequence length and multimodal rope.
- **labels** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Labels for computing the masked language modeling loss. Indices should either be in `[0, ...,
  config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored
  (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.
- **use_cache** (``) --
  If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
  `past_key_values`).
- **output_router_logits** (`bool`, *optional*) --
  Whether or not to return the logits of all the routers. They are useful for computing the router loss, and
  should not be returned during inference.
- **use_audio_in_video** (`bool`, *optional*) --
  Whether or not use audio track in video, should same as the parameter in `process_audio_info`.
- **cache_position** (`` of shape `(sequence_length)`) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.
- **video_second_per_grid** (`torch.LongTensor` of shape `(num_videos)`, *optional*) --
  Number of seconds per grid for each video, used for temporal feature mapping.0`transformers.models.qwen3_omni_moe.modeling_qwen3_omni_moe.Qwen3OmniMoeThinkerCausalLMOutputWithPast` or `tuple(torch.FloatTensor)`A `transformers.models.qwen3_omni_moe.modeling_qwen3_omni_moe.Qwen3OmniMoeThinkerCausalLMOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Qwen3OmniMoeConfig](/docs/transformers/v5.0.0rc1/en/model_doc/qwen3_omni_moe#transformers.Qwen3OmniMoeConfig)) and inputs.

- **rope_deltas** (`torch.LongTensor` of shape `(batch_size, )`, *optional*) -- The rope index difference between sequence length and multimodal rope.
The [Qwen3OmniMoeThinkerForConditionalGeneration](/docs/transformers/v5.0.0rc1/en/model_doc/qwen3_omni_moe#transformers.Qwen3OmniMoeThinkerForConditionalGeneration) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Example:

```python
>>> from io import BytesIO
>>> from urllib.request import urlopen
>>> import librosa
>>> from qwen_vl_utils import process_vision_info
>>> from transformers import Qwen3OmniMoeProcessor, Qwen3OmniMoeThinkerForConditionalGeneration

>>> thinker = Qwen3OmniMoeThinkerForConditionalGeneration.from_pretrained("Qwen/Qwen2.5-Omni-7B")
>>> processor = Qwen3OmniMoeProcessor.from_pretrained("Qwen/Qwen2.5-Omni-7B")

>>> conversations = [
>>>         {'role': 'system', 'content': 'You are a helpful voice chat bot, and please respond to me in a casual conversation manner using random voice.'},
>>>         {"role": "user", "content": [
>>>             {"type": "image", "image_url": "https://www.ilankelman.org/stopsigns/australia.jpg"},
>>>             {"type": "audio", "audio_url": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen2-Audio/audio/glass-breaking-151256.mp3"},
>>>         ]},
>>> ]

>>> text = processor.apply_chat_template(conversation, add_generation_prompt=True, tokenize=False)
>>> audios = [ librosa.load(BytesIO(urlopen( conversations[1]['content'][1]['audio_url'] ).read()), sr=self.processor.feature_extractor.sampling_rate) ]
>>> images, videos = process_vision_info(conversations)
>>> inputs = processor(text=text, audio=audios, images=images, videos=videos, return_tensors="pt", padding=True)

>>> # Generate
>>> inputs['use_audio_in_video'] = `True` or `False`
>>> generation = thinker.generate(**inputs, max_new_tokens=2048)
>>> generate_ids = generation[:, inputs.input_ids.size(1):]

>>> response = processor.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
```

**Parameters:**

config ([Qwen3OmniMoeThinkerForConditionalGeneration](/docs/transformers/v5.0.0rc1/en/model_doc/qwen3_omni_moe#transformers.Qwen3OmniMoeThinkerForConditionalGeneration)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``transformers.models.qwen3_omni_moe.modeling_qwen3_omni_moe.Qwen3OmniMoeThinkerCausalLMOutputWithPast` or `tuple(torch.FloatTensor)``

A `transformers.models.qwen3_omni_moe.modeling_qwen3_omni_moe.Qwen3OmniMoeThinkerCausalLMOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Qwen3OmniMoeConfig](/docs/transformers/v5.0.0rc1/en/model_doc/qwen3_omni_moe#transformers.Qwen3OmniMoeConfig)) and inputs.

- **rope_deltas** (`torch.LongTensor` of shape `(batch_size, )`, *optional*) -- The rope index difference between sequence length and multimodal rope.
#### get_audio_features[[transformers.Qwen3OmniMoeThinkerForConditionalGeneration.get_audio_features]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/modeling_qwen3_omni_moe.py#L1942)

Encodes audios into continuous embeddings that can be forwarded to the language model.

**Parameters:**

input_features (`torch.FloatTensor`) : The tensors corresponding to the input audios.

feature_attention_mask (`torch.LongTensor`, *optional*) : Mask to avoid performing attention on padding feature indices. Mask values selected in `[0, 1]`:

audio_feature_lengths (`torch.LongTensor` of shape `(num_audios)`, *optional*) : The length of feature shape of each audio in LLM.
#### get_image_features[[transformers.Qwen3OmniMoeThinkerForConditionalGeneration.get_image_features]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/modeling_qwen3_omni_moe.py#L1928)

Encodes images into continuous embeddings that can be forwarded to the language model.

**Parameters:**

pixel_values (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`) : The tensors corresponding to the input images.

image_grid_thw (`torch.LongTensor` of shape `(num_images, 3)`, *optional*) : The temporal, height and width of feature shape of each image in LLM.
#### get_placeholder_mask[[transformers.Qwen3OmniMoeThinkerForConditionalGeneration.get_placeholder_mask]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/modeling_qwen3_omni_moe.py#L1974)

Obtains multimodal placeholder mask from `input_ids` or `inputs_embeds`, and checks that the placeholder token count is
equal to the length of multimodal features. If the lengths are different, an error is raised.
#### get_video_features[[transformers.Qwen3OmniMoeThinkerForConditionalGeneration.get_video_features]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/modeling_qwen3_omni_moe.py#L1912)

Encodes videos into continuous embeddings that can be forwarded to the language model.

**Parameters:**

pixel_values_videos (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`) : The tensors corresponding to the input videos.

video_grid_thw (`torch.LongTensor` of shape `(num_videos, 3)`, *optional*) : The temporal, height and width of feature shape of each video in LLM.

## Qwen3OmniMoeTalkerForConditionalGeneration[[transformers.Qwen3OmniMoeTalkerForConditionalGeneration]]

#### transformers.Qwen3OmniMoeTalkerForConditionalGeneration[[transformers.Qwen3OmniMoeTalkerForConditionalGeneration]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/modeling_qwen3_omni_moe.py#L3022)

The Qwen3 Omni Moe Model for token generation conditioned on other modalities (e.g. image-text-to-text generation).

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.Qwen3OmniMoeTalkerForConditionalGeneration.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/modeling_qwen3_omni_moe.py#L3053[{"name": "input_ids", "val": " = None"}, {"name": "attention_mask", "val": " = None"}, {"name": "use_audio_in_video", "val": " = None"}, {"name": "audio_feature_lengths", "val": " = None"}, {"name": "video_second_per_grid", "val": " = None"}, {"name": "image_grid_thw", "val": " = None"}, {"name": "video_grid_thw", "val": " = None"}, {"name": "position_ids", "val": " = None"}, {"name": "past_key_values", "val": " = None"}, {"name": "inputs_embeds", "val": " = None"}, {"name": "labels", "val": " = None"}, {"name": "use_cache", "val": " = None"}, {"name": "output_router_logits", "val": " = None"}, {"name": "cache_position", "val": " = None"}, {"name": "residual_codes", "val": " = None"}, {"name": "trailing_text_hidden", "val": " = None"}, {"name": "tts_pad_embed", "val": " = None"}, {"name": "generation_step", "val": " = None"}, {"name": "talker_input_ids", "val": " = None"}, {"name": "**kwargs", "val": ""}]- **input_ids** (` of shape *(batch_size, sequence_length)*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [*AutoTokenizer*]. See [*PreTrainedTokenizer.encode*] and
  [*PreTrainedTokenizer.__call__*] for details.

  [What are input IDs?](../glossary#input-ids)
- **attention_mask** (` of shape *(batch_size, sequence_length)*) --
  Mask to avoid performing attention on padding token indices. Mask values selected in *[0, 1]*:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.

  [What are attention masks?](../glossary#attention-mask)
- **use_audio_in_video** (*bool*, *optional*) --
  If set to *True*, use the audio in video.
- **audio_feature_lengths** (*torch.LongTensor* of shape *(num_audios)*, *optional*) --
  The length of feature shape of each audio in LLM.
- **video_second_per_grid** (*torch.LongTensor* of shape *(num_videos)*, *optional*) --
  Number of seconds per grid for each video, used for temporal feature mapping.
- **image_grid_thw** (*torch.LongTensor* of shape *(num_images, 3)*, *optional*) --
  The temporal, height and width of feature shape of each image in LLM.
- **video_grid_thw** (*torch.LongTensor* of shape *(num_videos, 3)*, *optional*) --
  The temporal, height and width of feature shape of each video in LLM.
- **position_ids** (` of shape *(batch_size, sequence_length)*) --
  Indices of positions of each input sequence tokens in the position embeddings. Selected in the range *[0, config.n_positions - 1]*.

  [What are position IDs?](../glossary#position-ids)
- **past_key_values** (`) --
  Pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention
  blocks) that can be used to speed up sequential decoding. This typically consists in the *past_key_values*
  returned by the model at a previous stage of decoding, when *use_cache=True* or *config.use_cache=True*.

  Only [*~cache_utils.Cache*] instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).
  If no *past_key_values* are passed, [*~cache_utils.DynamicCache*] will be initialized by default.

  The model will output the same cache format that is fed as input.

  If *past_key_values* are used, the user is expected to input only unprocessed *input_ids* (those that don't
  have their past key value states given to this model) of shape *(batch_size, unprocessed_length)* instead of all *input_ids*
  of shape *(batch_size, sequence_length)*.
- **inputs_embeds** (` of shape *(batch_size, sequence_length, hidden_size)*) --
  Optionally, instead of passing *input_ids* you can choose to directly pass an embedded representation. This
  is useful if you want more control over how to convert *input_ids* indices into associated vectors than the
  model's internal embedding lookup matrix.
- **labels** (` of shape *(batch_size, sequence_length)*) --
  Labels for computing the masked language modeling loss. Indices should either be in *[0, ...,
  config.vocab_size]* or -100 (see *input_ids* docstring). Tokens with indices set to *-100* are ignored
  (masked), the loss is only computed for the tokens with labels in *[0, ..., config.vocab_size]*.
- **use_cache** (`) --
  If set to *True*, *past_key_values* key value states are returned and can be used to speed up decoding (see
  *past_key_values*).
- **output_router_logits** (`) --
  Whether or not to return the logits of all the routers. They are useful for computing the router loss, and
  should not be returned during inference.
- **cache_position** (`` of shape *(sequence_length)*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to *position_ids*,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.
- **residual_codes** (*torch.Tensor*) --
  The predicted residual codes of previous step.
- **trailing_text_hidden** (*torch.Tensor*) --
  Text hidden states from thinker after the first token.
- **tts_pad_embed** (*torch.Tensor*) --
  Embedding tensor of *tts_pad_token_id*.
- **generation_step** (*int*) --
  Generation step since prefill, used to sync with *trailing_text_hidden*.
- **talker_input_ids** (*torch.Tensor*) --
  Input ids from thinker, used to compute 3d RoPE.0[*transformers.modeling_outputs.MoeCausalLMOutputWithPast*] or *tuple(torch.FloatTensor)*A [*transformers.modeling_outputs.MoeCausalLMOutputWithPast*] or a tuple of
*torch.FloatTensor* (if *return_dict=False* is passed or when *config.return_dict=False*) comprising various
elements depending on the configuration ([*Qwen3OmniMoeConfig*]) and inputs.

- **loss** (*torch.FloatTensor* of shape *(1,)*, *optional*, returned when *labels* is provided) -- Language modeling loss (for next-token prediction).

- **logits** (*torch.FloatTensor* of shape *(batch_size, sequence_length, config.vocab_size)*) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).

- **aux_loss** (*torch.FloatTensor*, *optional*, returned when *labels* is provided) -- aux_loss for the sparse modules.

- **router_logits** (*tuple(torch.FloatTensor)*, *optional*, returned when *output_router_probs=True* and *config.add_router_probs=True* is passed or when *config.output_router_probs=True*) -- Tuple of *torch.FloatTensor* (one for each layer) of shape *(batch_size, sequence_length, num_experts)*.

  Raw router logtis (post-softmax) that are computed by MoE routers, these terms are used to compute the auxiliary
  loss for Mixture of Experts models.

- **past_key_values** (*Cache*, *optional*, returned when *use_cache=True* is passed or when *config.use_cache=True*) -- It is a [*~cache_utils.Cache*] instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
  *past_key_values* input) to speed up sequential decoding.
- **hidden_states** (*tuple(torch.FloatTensor)*, *optional*, returned when *output_hidden_states=True* is passed or when *config.output_hidden_states=True*) -- Tuple of *torch.FloatTensor* (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape *(batch_size, sequence_length, hidden_size)*.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (*tuple(torch.FloatTensor)*, *optional*, returned when *output_attentions=True* is passed or when *config.output_attentions=True*) -- Tuple of *torch.FloatTensor* (one for each layer) of shape *(batch_size, num_heads, sequence_length,
  sequence_length)*.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
The [*Qwen3OmniMoeTalkerForConditionalGeneration*] forward method, overrides the *__call__* special method.

Although the recipe for forward pass needs to be defined within this function, one should call the [*Module*]
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

**Parameters:**

config ([Qwen3OmniMoeTalkerConfig](/docs/transformers/v5.0.0rc1/en/model_doc/qwen3_omni_moe#transformers.Qwen3OmniMoeTalkerConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

`[*transformers.modeling_outputs.MoeCausalLMOutputWithPast*] or *tuple(torch.FloatTensor)*`

A [*transformers.modeling_outputs.MoeCausalLMOutputWithPast*] or a tuple of
*torch.FloatTensor* (if *return_dict=False* is passed or when *config.return_dict=False*) comprising various
elements depending on the configuration ([*Qwen3OmniMoeConfig*]) and inputs.

- **loss** (*torch.FloatTensor* of shape *(1,)*, *optional*, returned when *labels* is provided) -- Language modeling loss (for next-token prediction).

- **logits** (*torch.FloatTensor* of shape *(batch_size, sequence_length, config.vocab_size)*) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).

- **aux_loss** (*torch.FloatTensor*, *optional*, returned when *labels* is provided) -- aux_loss for the sparse modules.

- **router_logits** (*tuple(torch.FloatTensor)*, *optional*, returned when *output_router_probs=True* and *config.add_router_probs=True* is passed or when *config.output_router_probs=True*) -- Tuple of *torch.FloatTensor* (one for each layer) of shape *(batch_size, sequence_length, num_experts)*.

  Raw router logtis (post-softmax) that are computed by MoE routers, these terms are used to compute the auxiliary
  loss for Mixture of Experts models.

- **past_key_values** (*Cache*, *optional*, returned when *use_cache=True* is passed or when *config.use_cache=True*) -- It is a [*~cache_utils.Cache*] instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
  *past_key_values* input) to speed up sequential decoding.
- **hidden_states** (*tuple(torch.FloatTensor)*, *optional*, returned when *output_hidden_states=True* is passed or when *config.output_hidden_states=True*) -- Tuple of *torch.FloatTensor* (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape *(batch_size, sequence_length, hidden_size)*.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (*tuple(torch.FloatTensor)*, *optional*, returned when *output_attentions=True* is passed or when *config.output_attentions=True*) -- Tuple of *torch.FloatTensor* (one for each layer) of shape *(batch_size, num_heads, sequence_length,
  sequence_length)*.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.

## Qwen3OmniMoePreTrainedModel[[transformers.Qwen3OmniMoePreTrainedModel]]

#### transformers.Qwen3OmniMoePreTrainedModel[[transformers.Qwen3OmniMoePreTrainedModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/modeling_qwen3_omni_moe.py#L68)

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

**Parameters:**

config ([PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

## Qwen3OmniMoePreTrainedModelForConditionalGeneration[[transformers.Qwen3OmniMoePreTrainedModelForConditionalGeneration]]

#### transformers.Qwen3OmniMoePreTrainedModelForConditionalGeneration[[transformers.Qwen3OmniMoePreTrainedModelForConditionalGeneration]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/modeling_qwen3_omni_moe.py#L101)

get_chunked_indextransformers.Qwen3OmniMoePreTrainedModelForConditionalGeneration.get_chunked_indexhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/modeling_qwen3_omni_moe.py#L179[{"name": "token_indices", "val": ": Tensor"}, {"name": "tokens_per_chunk", "val": ": int"}, {"name": "remove_index", "val": ": int"}]- **token_indices** (`torch.Tensor` of shape `(seq_len, )`) -- A monotonically increasing list of
  token index values.
- **t_ntoken_per_chunk** (`int`) -- Number of tokens per chunk (used as the chunk size threshold).
- **remove_index** (`int`) An index id to subtract from `token_indices` before chunking --0`list[tuple[int, int]]`A list of tuples, each representing the start (inclusive)
and end (exclusive) indices of a chunk in `token_indices`.

Splits token index list into chunks based on token value ranges.

Given a list of token indices, returns a list of (start, end) index tuples representing
slices of the list where the token values fall within successive ranges of `t_ntoken_per_chunk`.

For example, if `t_ntoken_per_chunk` is 1000, the function will create chunks such that:
- the first chunk contains token values = 1000 and < 2000, and so on.

**Parameters:**

token_indices (`torch.Tensor` of shape `(seq_len, )`) : A monotonically increasing list of token index values.

t_ntoken_per_chunk (`int`) : Number of tokens per chunk (used as the chunk size threshold).

remove_index (`int`) An index id to subtract from `token_indices` before chunking --

**Returns:**

``list[tuple[int, int]]``

A list of tuples, each representing the start (inclusive)
and end (exclusive) indices of a chunk in `token_indices`.
#### get_rope_index[[transformers.Qwen3OmniMoePreTrainedModelForConditionalGeneration.get_rope_index]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/modeling_qwen3_omni_moe.py#L216)

Calculate the 3D rope index based on image and video's temporal, height and width in LLM.

Explanation:
Each embedding sequence contains vision embedding and text embedding or just contains text embedding.

For pure text embedding sequence, the rotary position embedding has no difference with modern LLMs.
Examples:
input_ids: [T T T T T], here T is for text.
temporal position_ids: [0, 1, 2, 3, 4]
height position_ids: [0, 1, 2, 3, 4]
width position_ids: [0, 1, 2, 3, 4]

For vision and text embedding sequence, we calculate 3D rotary position embedding for vision part
and 1D rotary position embedding for text part.
Examples:
Temporal (Time): 3 patches, representing different segments of the video in time.
Height: 2 patches, dividing each frame vertically.
Width: 2 patches, dividing each frame horizontally.
We also have some important parameters:
fps (Frames Per Second): The video's frame rate, set to 1. This means one frame is processed each second.
tokens_per_second: This is a crucial parameter. It dictates how many "time-steps" or "temporal tokens" are conceptually packed into a one-second interval of the video. In this case, we have 25 tokens per second. So each second of the video will be represented with 25 separate time points. It essentially defines the temporal granularity.
temporal_patch_size: The number of frames that compose one temporal patch. Here, it's 2 frames.
interval: The step size for the temporal position IDs, calculated as tokens_per_second * temporal_patch_size / fps. In this case, 25 * 2 / 1 = 50. This means that each temporal patch will be have a difference of 50 in the temporal position IDs.
input_ids: [V V V V V V V V V V V V T T T T T], here V is for vision.
vision temporal position_ids: [0, 0, 0, 0, 50, 50, 50, 50, 100, 100, 100, 100]
vision height position_ids: [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
vision width position_ids: [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
text temporal position_ids: [101, 102, 103, 104, 105]
text height position_ids: [101, 102, 103, 104, 105]
text width position_ids: [101, 102, 103, 104, 105]
Here we calculate the text start position_ids as the max vision position_ids plus 1.

**Parameters:**

input_ids (`torch.LongTensor` of shape `(batch_size, sequence_length)`) : Indices of input sequence tokens in the vocabulary. Padding will be ignored by default should you provide it.

image_grid_thw (`torch.LongTensor` of shape `(num_images, 3)`, *optional*) : The temporal, height and width of feature shape of each image in LLM.

video_grid_thw (`torch.LongTensor` of shape `(num_videos, 3)`, *optional*) : The temporal, height and width of feature shape of each video in LLM.

attention_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) : Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:  - 1 for tokens that are **not masked**, - 0 for tokens that are **masked**.

use_audio_in_video (`bool`, *optional*) : If set to `True`, use the audio in video.

audio_seqlens (`torch.LongTensor` of shape `(num_audios)`, *optional*) : The length of feature shape of each audio in LLM.

second_per_grids (`torch.LongTensor` of shape `(num_videos)`, *optional*) : The time interval (in seconds) for each grid along the temporal dimension in the 3D position IDs.

**Returns:**

position_ids (`torch.LongTensor` of shape `(3, batch_size, sequence_length)`)
mrope_position_deltas (`torch.Tensor` of shape `(batch_size)`)

## Qwen3OmniMoeTalkerModel[[transformers.Qwen3OmniMoeTalkerModel]]

#### transformers.Qwen3OmniMoeTalkerModel[[transformers.Qwen3OmniMoeTalkerModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/modeling_qwen3_omni_moe.py#L2887)

Text part of Qwen3OmniMoe, not a pure text-only model, as DeepStack integrates visual features into the early hidden states.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.Qwen3OmniMoeTalkerModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/modeling_qwen3_omni_moe.py#L2913[{"name": "input_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "attention_mask", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "position_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "past_key_values", "val": ": typing.Optional[transformers.cache_utils.Cache] = None"}, {"name": "inputs_embeds", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "use_cache", "val": ": typing.Optional[bool] = None"}, {"name": "cache_position", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "visual_pos_masks", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "deepstack_visual_embeds", "val": ": typing.Optional[list[torch.Tensor]] = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.modeling_flash_attention_utils.FlashAttentionKwargs]"}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

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

  Only [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).
  If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.

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
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.
- **visual_pos_masks** (`torch.Tensor` of shape `(batch_size, seqlen)`, *optional*) --
  The mask of the visual positions.
- **deepstack_visual_embeds** (`list[torch.Tensor]`, *optional*) --
  The deepstack visual embeddings. The shape is (num_layers, visual_seqlen, embed_dim).
  The feature is extracted from the different visual encoder layers, and fed to the decoder
  hidden states. It's from the paper DeepStack(https://arxiv.org/abs/2406.04334).0[transformers.modeling_outputs.BaseModelOutputWithPast](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or `tuple(torch.FloatTensor)`A [transformers.modeling_outputs.BaseModelOutputWithPast](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Qwen3OmniMoeConfig](/docs/transformers/v5.0.0rc1/en/model_doc/qwen3_omni_moe#transformers.Qwen3OmniMoeConfig)) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.

  If `past_key_values` is used only the last hidden-state of the sequences of shape `(batch_size, 1,
  hidden_size)` is output.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

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
The [Qwen3OmniMoeTalkerModel](/docs/transformers/v5.0.0rc1/en/model_doc/qwen3_omni_moe#transformers.Qwen3OmniMoeTalkerModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

**Parameters:**

config (`Qwen3OmniMoeTalkerTextConfig`) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

`[transformers.modeling_outputs.BaseModelOutputWithPast](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutputWithPast](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Qwen3OmniMoeConfig](/docs/transformers/v5.0.0rc1/en/model_doc/qwen3_omni_moe#transformers.Qwen3OmniMoeConfig)) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.

  If `past_key_values` is used only the last hidden-state of the sequences of shape `(batch_size, 1,
  hidden_size)` is output.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

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

## Qwen3OmniMoeThinkerTextPreTrainedModel[[transformers.Qwen3OmniMoeThinkerTextPreTrainedModel]]

#### transformers.Qwen3OmniMoeThinkerTextPreTrainedModel[[transformers.Qwen3OmniMoeThinkerTextPreTrainedModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/modeling_qwen3_omni_moe.py#L1590)

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

**Parameters:**

config ([PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

## Qwen3OmniMoeProcessor[[transformers.Qwen3OmniMoeProcessor]]

#### transformers.Qwen3OmniMoeProcessor[[transformers.Qwen3OmniMoeProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/processing_qwen3_omni_moe.py#L86)

Constructs a Qwen2.5Omni processor.
[Qwen3OmniMoeProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/qwen3_omni_moe#transformers.Qwen3OmniMoeProcessor) offers all the functionalities of [Qwen2VLImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/qwen2_vl#transformers.Qwen2VLImageProcessor), [WhisperFeatureExtractor](/docs/transformers/v5.0.0rc1/en/model_doc/whisper#transformers.WhisperFeatureExtractor), and [Qwen2TokenizerFast](/docs/transformers/v5.0.0rc1/en/model_doc/qwen2#transformers.Qwen2Tokenizer). See the
`__call__()` and [decode()](/docs/transformers/v5.0.0rc1/en/main_classes/processors#transformers.ProcessorMixin.decode) for more information.

get_chunked_indextransformers.Qwen3OmniMoeProcessor.get_chunked_indexhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/processing_qwen3_omni_moe.py#L296[{"name": "token_indices", "val": ": ndarray"}, {"name": "tokens_per_chunk", "val": ": int"}]- **token_indices** (`np.ndarray`) -- A monotonically increasing list of token index values.
- **t_ntoken_per_chunk** (`int`) -- Number of tokens per chunk (used as the chunk size threshold).0`list[tuple[int, int]]`A list of tuples, each representing the start (inclusive)
and end (exclusive) indices of a chunk in `token_indices`.

Splits token index list into chunks based on token value ranges.

Given a list of token indices, returns a list of (start, end) index tuples representing
slices of the list where the token values fall within successive ranges of `t_ntoken_per_chunk`.

For example, if `t_ntoken_per_chunk` is 1000, the function will create chunks such that:
- the first chunk contains token values = 1000 and < 2000, and so on.

**Parameters:**

image_processor ([Qwen2VLImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/qwen2_vl#transformers.Qwen2VLImageProcessor), *optional*) : The image processor.

video_processor ([Qwen2VLVideoProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/qwen2_vl#transformers.Qwen2VLVideoProcessor), *optional*) : The video processor.

feature_extractor ([WhisperFeatureExtractor](/docs/transformers/v5.0.0rc1/en/model_doc/whisper#transformers.WhisperFeatureExtractor), *optional*) : The audio feature extractor.

tokenizer ([Qwen2TokenizerFast](/docs/transformers/v5.0.0rc1/en/model_doc/qwen2#transformers.Qwen2Tokenizer), *optional*) : The text tokenizer.

chat_template (`Optional[str]`, *optional*) : The Jinja template to use for formatting the conversation. If not provided, the default chat template is used.

**Returns:**

``list[tuple[int, int]]``

A list of tuples, each representing the start (inclusive)
and end (exclusive) indices of a chunk in `token_indices`.
#### post_process_image_text_to_text[[transformers.Qwen3OmniMoeProcessor.post_process_image_text_to_text]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/processing_qwen3_omni_moe.py#L332)

Post-process the output of a vlm to decode the text.

**Parameters:**

generated_outputs (`torch.Tensor` or `np.ndarray`) : The output of the model `generate` function. The output is expected to be a tensor of shape `(batch_size, sequence_length)` or `(sequence_length,)`.

skip_special_tokens (`bool`, *optional*, defaults to `True`) : Whether or not to remove special tokens in the output. Argument passed to the tokenizer's `batch_decode` method.

- ****kwargs** : Additional arguments to be passed to the tokenizer's `batch_decode method`.

**Returns:**

``list[str]``

The decoded text.
#### post_process_multimodal_output[[transformers.Qwen3OmniMoeProcessor.post_process_multimodal_output]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/processing_qwen3_omni_moe.py#L350)

Post-process the output of a multimodal model to return the requested modality output.
If the model cannot generated the requested modality, an error will be raised.

**Parameters:**

generated_outputs (`torch.Tensor` or `np.ndarray`) : The output of the model `generate` function. The output is expected to be a tensor of shape `(batch_size, sequence_length)` or `(sequence_length,)`.

skip_special_tokens (`bool`, *optional*, defaults to `True`) : Whether or not to remove special tokens in the output. Argument passed to the tokenizer's `batch_decode` method.

generation_mode (`str`, *optional*) : Generation mode indicated which modality to output and can be one of `["text", "image", "audio"]`.

- ****kwargs** : Additional arguments to be passed to the tokenizer's `batch_decode method`.

**Returns:**

``list[Inion[str, np.ndarray]]``

The decoded text or generated audio.

## Qwen3OmniMoeCode2Wav[[transformers.Qwen3OmniMoeCode2Wav]]

#### transformers.Qwen3OmniMoeCode2Wav[[transformers.Qwen3OmniMoeCode2Wav]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/modeling_qwen3_omni_moe.py#L3725)

## Qwen3OmniMoeCode2WavDecoderBlock[[transformers.Qwen3OmniMoeCode2WavDecoderBlock]]

#### transformers.Qwen3OmniMoeCode2WavDecoderBlock[[transformers.Qwen3OmniMoeCode2WavDecoderBlock]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/modeling_qwen3_omni_moe.py#L3702)

## Qwen3OmniMoeCode2WavTransformerModel[[transformers.Qwen3OmniMoeCode2WavTransformerModel]]

#### transformers.Qwen3OmniMoeCode2WavTransformerModel[[transformers.Qwen3OmniMoeCode2WavTransformerModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/modeling_qwen3_omni_moe.py#L3548)

The bare Qwen3 Omni Moe Model outputting raw hidden-states without any specific head on top.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.Qwen3OmniMoeCode2WavTransformerModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/modeling_qwen3_omni_moe.py#L3568[{"name": "input_ids", "val": " = None"}, {"name": "attention_mask", "val": " = None"}, {"name": "position_ids", "val": " = None"}, {"name": "past_key_values", "val": " = None"}, {"name": "inputs_embeds", "val": " = None"}, {"name": "use_cache", "val": " = None"}, {"name": "cache_position", "val": " = None"}, {"name": "**kwargs", "val": ""}]- **input_ids** (`` of shape `(batch_size, sequence_length)`) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **attention_mask** (`` of shape `(batch_size, sequence_length)`) --
  Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.

  [What are attention masks?](../glossary#attention-mask)
- **position_ids** (`` of shape `(batch_size, sequence_length)`) --
  Indices of positions of each input sequence tokens in the position embeddings. Selected in the range `[0, config.n_positions - 1]`.

  [What are position IDs?](../glossary#position-ids)
- **past_key_values** (``) --
  Pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention
  blocks) that can be used to speed up sequential decoding. This typically consists in the `past_key_values`
  returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.

  Only [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).
  If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.

  The model will output the same cache format that is fed as input.

  If `past_key_values` are used, the user is expected to input only unprocessed `input_ids` (those that don't
  have their past key value states given to this model) of shape `(batch_size, unprocessed_length)` instead of all `input_ids`
  of shape `(batch_size, sequence_length)`.
- **inputs_embeds** (`` of shape `(batch_size, sequence_length, hidden_size)`) --
  Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation. This
  is useful if you want more control over how to convert `input_ids` indices into associated vectors than the
  model's internal embedding lookup matrix.
- **use_cache** (``) --
  If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
  `past_key_values`).
- **cache_position** (`` of shape `(sequence_length)`) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.0[transformers.modeling_outputs.BaseModelOutputWithPast](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or `tuple(torch.FloatTensor)`A [transformers.modeling_outputs.BaseModelOutputWithPast](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Qwen3OmniMoeConfig](/docs/transformers/v5.0.0rc1/en/model_doc/qwen3_omni_moe#transformers.Qwen3OmniMoeConfig)) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.

  If `past_key_values` is used only the last hidden-state of the sequences of shape `(batch_size, 1,
  hidden_size)` is output.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

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
The [Qwen3OmniMoeCode2WavTransformerModel](/docs/transformers/v5.0.0rc1/en/model_doc/qwen3_omni_moe#transformers.Qwen3OmniMoeCode2WavTransformerModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

**Parameters:**

config (`Qwen3OmniMoeCode2WavConfig`) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

`[transformers.modeling_outputs.BaseModelOutputWithPast](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutputWithPast](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Qwen3OmniMoeConfig](/docs/transformers/v5.0.0rc1/en/model_doc/qwen3_omni_moe#transformers.Qwen3OmniMoeConfig)) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.

  If `past_key_values` is used only the last hidden-state of the sequences of shape `(batch_size, 1,
  hidden_size)` is output.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

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

## Qwen3OmniMoeTalkerCodePredictorModel[[transformers.Qwen3OmniMoeTalkerCodePredictorModel]]

#### transformers.Qwen3OmniMoeTalkerCodePredictorModel[[transformers.Qwen3OmniMoeTalkerCodePredictorModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/modeling_qwen3_omni_moe.py#L2529)

The bare Qwen3 Omni Moe Model outputting raw hidden-states without any specific head on top.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.Qwen3OmniMoeTalkerCodePredictorModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/modeling_qwen3_omni_moe.py#L2558[{"name": "input_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "attention_mask", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "position_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "past_key_values", "val": ": typing.Optional[transformers.cache_utils.Cache] = None"}, {"name": "inputs_embeds", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "use_cache", "val": ": typing.Optional[bool] = None"}, {"name": "cache_position", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

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

  Only [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).
  If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.

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
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.0[transformers.modeling_outputs.BaseModelOutputWithPast](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or `tuple(torch.FloatTensor)`A [transformers.modeling_outputs.BaseModelOutputWithPast](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Qwen3OmniMoeConfig](/docs/transformers/v5.0.0rc1/en/model_doc/qwen3_omni_moe#transformers.Qwen3OmniMoeConfig)) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.

  If `past_key_values` is used only the last hidden-state of the sequences of shape `(batch_size, 1,
  hidden_size)` is output.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

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
The [Qwen3OmniMoeTalkerCodePredictorModel](/docs/transformers/v5.0.0rc1/en/model_doc/qwen3_omni_moe#transformers.Qwen3OmniMoeTalkerCodePredictorModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

**Parameters:**

config (`Qwen3OmniMoeTalkerCodePredictorConfig`) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

`[transformers.modeling_outputs.BaseModelOutputWithPast](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutputWithPast](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Qwen3OmniMoeConfig](/docs/transformers/v5.0.0rc1/en/model_doc/qwen3_omni_moe#transformers.Qwen3OmniMoeConfig)) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.

  If `past_key_values` is used only the last hidden-state of the sequences of shape `(batch_size, 1,
  hidden_size)` is output.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

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

## Qwen3OmniMoeTalkerCodePredictorModelForConditionalGeneration[[transformers.Qwen3OmniMoeTalkerCodePredictorModelForConditionalGeneration]]

#### transformers.Qwen3OmniMoeTalkerCodePredictorModelForConditionalGeneration[[transformers.Qwen3OmniMoeTalkerCodePredictorModelForConditionalGeneration]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/modeling_qwen3_omni_moe.py#L2630)

The Qwen3 Omni Moe Model for token generation conditioned on other modalities (e.g. image-text-to-text generation).

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.Qwen3OmniMoeTalkerCodePredictorModelForConditionalGeneration.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/qwen3_omni_moe/modeling_qwen3_omni_moe.py#L2652[{"name": "input_ids", "val": " = None"}, {"name": "attention_mask", "val": " = None"}, {"name": "position_ids", "val": " = None"}, {"name": "past_key_values", "val": " = None"}, {"name": "inputs_embeds", "val": " = None"}, {"name": "labels", "val": " = None"}, {"name": "use_cache", "val": " = None"}, {"name": "cache_position", "val": " = None"}, {"name": "generation_steps", "val": " = None"}, {"name": "**kwargs", "val": ""}]- **input_ids** (`` of shape `(batch_size, sequence_length)`) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **attention_mask** (`` of shape `(batch_size, sequence_length)`) --
  Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.

  [What are attention masks?](../glossary#attention-mask)
- **position_ids** (`` of shape `(batch_size, sequence_length)`) --
  Indices of positions of each input sequence tokens in the position embeddings. Selected in the range `[0, config.n_positions - 1]`.

  [What are position IDs?](../glossary#position-ids)
- **past_key_values** (``) --
  Pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention
  blocks) that can be used to speed up sequential decoding. This typically consists in the `past_key_values`
  returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.

  Only [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).
  If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.

  The model will output the same cache format that is fed as input.

  If `past_key_values` are used, the user is expected to input only unprocessed `input_ids` (those that don't
  have their past key value states given to this model) of shape `(batch_size, unprocessed_length)` instead of all `input_ids`
  of shape `(batch_size, sequence_length)`.
- **inputs_embeds** (`` of shape `(batch_size, sequence_length, hidden_size)`) --
  Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation. This
  is useful if you want more control over how to convert `input_ids` indices into associated vectors than the
  model's internal embedding lookup matrix.
- **labels** (`` of shape `(batch_size, sequence_length)`) --
  Labels for computing the masked language modeling loss. Indices should either be in `[0, ...,
  config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored
  (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.
- **use_cache** (``) --
  If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
  `past_key_values`).
- **cache_position** (`` of shape `(sequence_length)`) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.
- **generation_steps** (`int`) --
  generation step of code predictor, 0..num_code_groups-10[transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or `tuple(torch.FloatTensor)`A [transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Qwen3OmniMoeConfig](/docs/transformers/v5.0.0rc1/en/model_doc/qwen3_omni_moe#transformers.Qwen3OmniMoeConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
  `past_key_values` input) to speed up sequential decoding.
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
The [Qwen3OmniMoeTalkerCodePredictorModelForConditionalGeneration](/docs/transformers/v5.0.0rc1/en/model_doc/qwen3_omni_moe#transformers.Qwen3OmniMoeTalkerCodePredictorModelForConditionalGeneration) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

**Parameters:**

config (`Qwen3OmniMoeTalkerCodePredictorConfig`) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

`[transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Qwen3OmniMoeConfig](/docs/transformers/v5.0.0rc1/en/model_doc/qwen3_omni_moe#transformers.Qwen3OmniMoeConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
  `past_key_values` input) to speed up sequential decoding.
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.

