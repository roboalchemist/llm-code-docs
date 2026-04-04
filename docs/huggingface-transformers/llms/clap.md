# Source: https://huggingface.co/docs/transformers/v5.0.0/model_doc/clap.md

# CLAP

[CLAP (Contrastive Language-Audio Pretraining)](https://huggingface.co/papers/2211.06687) is a multimodal model that combines audio data with natural language descriptions through contrastive learning.

It incorporates feature fusion and keyword-to-caption augmentation to process variable-length audio inputs and to improve performance. CLAP doesn't require task-specific training data and can learn meaningful audio representations through natural language.

You can find all the original CLAP checkpoints under the [CLAP](https://huggingface.co/collections/laion/clap-contrastive-language-audio-pretraining-65415c0b18373b607262a490) collection.

> [!TIP]
> This model was contributed by [ybelkada](https://huggingface.co/ybelkada) and [ArthurZ](https://huggingface.co/ArthurZ).
>
> Click on the CLAP models in the right sidebar for more examples of how to apply CLAP to different audio retrieval and classification tasks.

The example below demonstrates how to extract text embeddings with the [AutoModel](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoModel) class.

```python
import torch
from transformers import AutoTokenizer, AutoModel

model = AutoModel.from_pretrained("laion/clap-htsat-unfused", dtype=torch.float16, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("laion/clap-htsat-unfused")

texts = ["the sound of a cat", "the sound of a dog", "music playing"]

inputs = tokenizer(texts, padding=True, return_tensors="pt").to(model.device)

with torch.no_grad():
    text_features = model.get_text_features(**inputs)

print(f"Text embeddings shape: {text_features.shape}")
print(f"Text embeddings: {text_features}")
```

## ClapConfig[[transformers.ClapConfig]]

#### transformers.ClapConfig[[transformers.ClapConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/clap/configuration_clap.py#L279)

[ClapConfig](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapConfig) is the configuration class to store the configuration of a [ClapModel](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapModel). It is used to instantiate
a CLAP model according to the specified arguments, defining the text model and audio model configs. Instantiating a
configuration with the defaults will yield a similar configuration to that of the CLAP
[laion/clap-htsat-fused](https://huggingface.co/laion/clap-htsat-fused) architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:

```python
>>> from transformers import ClapConfig, ClapModel

>>> # Initializing a ClapConfig with laion-ai/base style configuration
>>> configuration = ClapConfig()

>>> # Initializing a ClapModel (with random weights) from the laion-ai/base style configuration
>>> model = ClapModel(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config

>>> # We can also initialize a ClapConfig from a ClapTextConfig and a ClapAudioConfig
>>> from transformers import ClapTextConfig, ClapAudioConfig

>>> # Initializing a ClapText and ClapAudioConfig configuration
>>> config_text = ClapTextConfig()
>>> config_audio = ClapAudioConfig()

>>> config = ClapConfig(text_config=config_text, audio_config=config_audio)
```

**Parameters:**

text_config (`dict`, *optional*) : Dictionary of configuration options used to initialize [ClapTextConfig](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapTextConfig).

audio_config (`dict`, *optional*) : Dictionary of configuration options used to initialize [ClapAudioConfig](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapAudioConfig).

logit_scale_init_value (`float`, *optional*, defaults to 14.29) : The initial value of the *logit_scale* parameter. Default is used as per the original CLAP implementation.

projection_dim (`int`, *optional*, defaults to 512) : Dimensionality of text and audio projection layers.

projection_hidden_act (`str`, *optional*, defaults to `"relu"`) : Activation function for the projection layers.

initializer_factor (`float`, *optional*, defaults to 1.0) : Factor to scale the initialization of the model weights.

kwargs (*optional*) : Dictionary of keyword arguments.

## ClapTextConfig[[transformers.ClapTextConfig]]

#### transformers.ClapTextConfig[[transformers.ClapTextConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/clap/configuration_clap.py#L23)

This is the configuration class to store the configuration of a [ClapTextModel](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapTextModel). It is used to instantiate a CLAP
model according to the specified arguments, defining the model architecture. Instantiating a configuration with the
defaults will yield a similar configuration to that of the CLAP
[calp-hsat-fused](https://huggingface.co/laion/clap-hsat-fused) architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Examples:

```python
>>> from transformers import ClapTextConfig, ClapTextModel

>>> # Initializing a CLAP text configuration
>>> configuration = ClapTextConfig()

>>> # Initializing a model (with random weights) from the configuration
>>> model = ClapTextModel(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

vocab_size (`int`, *optional*, defaults to 30522) : Vocabulary size of the CLAP model. Defines the number of different tokens that can be represented by the `inputs_ids` passed when calling [ClapTextModel](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapTextModel).

hidden_size (`int`, *optional*, defaults to 768) : Dimensionality of the encoder layers and the pooler layer.

num_hidden_layers (`int`, *optional*, defaults to 12) : Number of hidden layers in the Transformer encoder.

num_attention_heads (`int`, *optional*, defaults to 12) : Number of attention heads for each attention layer in the Transformer encoder.

intermediate_size (`int`, *optional*, defaults to 3072) : Dimensionality of the "intermediate" (often named feed-forward) layer in the Transformer encoder.

hidden_act (`str` or `Callable`, *optional*, defaults to `"relu"`) : The non-linear activation function (function or string) in the encoder and pooler. If string, `"relu"`, `"relu"`, `"silu"` and `"relu_new"` are supported.

hidden_dropout_prob (`float`, *optional*, defaults to 0.1) : The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.

attention_probs_dropout_prob (`float`, *optional*, defaults to 0.1) : The dropout ratio for the attention probabilities.

max_position_embeddings (`int`, *optional*, defaults to 512) : The maximum sequence length that this model might ever be used with. Typically set this to something large just in case (e.g., 512 or 1024 or 2048).

type_vocab_size (`int`, *optional*, defaults to 2) : The vocabulary size of the `token_type_ids` passed when calling [ClapTextModel](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapTextModel).

layer_norm_eps (`float`, *optional*, defaults to 1e-12) : The epsilon used by the layer normalization layers.

projection_hidden_act (`str`, *optional*, defaults to `"relu"`) : The non-linear activation function (function or string) in the projection layer. If string, `"gelu"`, `"relu"`, `"silu"` and `"gelu_new"` are supported.

projection_dim (`int`, *optional*, defaults to 512) : Dimension of the projection head of the `ClapTextModelWithProjection`.

## ClapAudioConfig[[transformers.ClapAudioConfig]]

#### transformers.ClapAudioConfig[[transformers.ClapAudioConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/clap/configuration_clap.py#L126)

This is the configuration class to store the configuration of a [ClapAudioModel](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapAudioModel). It is used to instantiate a
CLAP audio encoder according to the specified arguments, defining the model architecture. Instantiating a
configuration with the defaults will yield a similar configuration to that of the audio encoder of the CLAP
[laion/clap-htsat-fused](https://huggingface.co/laion/clap-htsat-fused) architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:

```python
>>> from transformers import ClapAudioConfig, ClapAudioModel

>>> # Initializing a ClapAudioConfig with laion/clap-htsat-fused style configuration
>>> configuration = ClapAudioConfig()

>>> # Initializing a ClapAudioModel (with random weights) from the laion/clap-htsat-fused style configuration
>>> model = ClapAudioModel(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

window_size (`int`, *optional*, defaults to 8) : Image size of the spectrogram

num_mel_bins (`int`, *optional*, defaults to 64) : Number of mel features used per frames. Should correspond to the value used in the `ClapProcessor` class.

spec_size (`int`, *optional*, defaults to 256) : Desired input size of the spectrogram that the model supports. It can be different from the output of the `ClapFeatureExtractor`, in which case the input features will be resized. Corresponds to the `image_size` of the audio models.

hidden_act (`str`, *optional*, defaults to `"gelu"`) : The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`, `"relu"`, `"silu"` and `"gelu_new"` are supported.

patch_size (`int`, *optional*, defaults to 4) : Patch size for the audio spectrogram

patch_stride (`list`, *optional*, defaults to `[4, 4]`) : Patch stride for the audio spectrogram

num_classes (`int`, *optional*, defaults to 527) : Number of classes used for the head training

hidden_size (`int`, *optional*, defaults to 768) : Hidden size of the output of the audio encoder. Correspond to the dimension of the penultimate layer's output,which is sent to the projection MLP layer.

projection_dim (`int`, *optional*, defaults to 512) : Hidden size of the projection layer.

depths (`list`, *optional*, defaults to `[2, 2, 6, 2]`) : Depths used for the Swin Layers of the audio model

num_attention_heads (`list`, *optional*, defaults to `[4, 8, 16, 32]`) : Number of attention heads used for the Swin Layers of the audio model

enable_fusion (`bool`, *optional*, defaults to `False`) : Whether or not to enable patch fusion. This is the main contribution of the authors, and should give the best results.

hidden_dropout_prob (`float`, *optional*, defaults to 0.1) : The dropout probability for all fully connected layers in the encoder.

fusion_type (`[type]`, *optional*) : Fusion type used for the patch fusion.

patch_embed_input_channels (`int`, *optional*, defaults to 1) : Number of channels used for the input spectrogram

flatten_patch_embeds (`bool`, *optional*, defaults to `True`) : Whether or not to flatten the patch embeddings

patch_embeds_hidden_size (`int`, *optional*, defaults to 96) : Hidden size of the patch embeddings. It is used as the number of output channels.

enable_patch_layer_norm (`bool`, *optional*, defaults to `True`) : Whether or not to enable layer normalization for the patch embeddings

drop_path_rate (`float`, *optional*, defaults to 0.0) : Drop path rate for the patch fusion

attention_probs_dropout_prob (`float`, *optional*, defaults to 0.0) : The dropout ratio for the attention probabilities.

qkv_bias (`bool`, *optional*, defaults to `True`) : Whether or not to add a bias to the query, key, value projections.

mlp_ratio (`float`, *optional*, defaults to 4.0) : Ratio of the mlp hidden dim to embedding dim.

aff_block_r (`int`, *optional*, defaults to 4) : downsize_ratio used in the AudioFF block

num_hidden_layers (`int`, *optional*, defaults to 4) : Number of hidden layers in the Transformer encoder.

projection_hidden_act (`str`, *optional*, defaults to `"relu"`) : The non-linear activation function (function or string) in the projection layer. If string, `"gelu"`, `"relu"`, `"silu"` and `"gelu_new"` are supported.

layer_norm_eps (`[type]`, *optional*, defaults to 1e-05) : The epsilon used by the layer normalization layers.

initializer_factor (`float`, *optional*, defaults to 1.0) : A factor for initializing all weight matrices (should be kept to 1, used internally for initialization testing).

## ClapFeatureExtractor[[transformers.ClapFeatureExtractor]]

#### transformers.ClapFeatureExtractor[[transformers.ClapFeatureExtractor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/clap/feature_extraction_clap.py#L33)

Constructs a CLAP feature extractor.

This feature extractor inherits from [SequenceFeatureExtractor](/docs/transformers/v5.0.0/en/main_classes/feature_extractor#transformers.SequenceFeatureExtractor) which contains
most of the main methods. Users should refer to this superclass for more information regarding those methods.

This class extracts mel-filter bank features from raw speech using a custom numpy implementation of the *Short Time
Fourier Transform* (STFT) which should match pytorch's `torch.stft` equivalent.

to_dicttransformers.ClapFeatureExtractor.to_dicthttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/clap/feature_extraction_clap.py#L138[]`dict[str, Any]`Dictionary of all the attributes that make up this configuration instance, except for the
mel filter banks, which do not need to be saved or printed as they are too long.

Serializes this instance to a Python dictionary.

**Parameters:**

feature_size (`int`, *optional*, defaults to 64) : The feature dimension of the extracted Mel spectrograms. This corresponds to the number of mel filters (`n_mels`).

sampling_rate (`int`, *optional*, defaults to 48000) : The sampling rate at which the audio files should be digitalized expressed in hertz (Hz). This only serves to warn users if the audio fed to the feature extractor does not have the same sampling rate.

hop_length (`int`,*optional*, defaults to 480) : Length of the overlapping windows for the STFT used to obtain the Mel Spectrogram. The audio will be split in smaller `frames` with a step of `hop_length` between each frame.

max_length_s (`int`, *optional*, defaults to 10) : The maximum input length of the model in seconds. This is used to pad the audio.

fft_window_size (`int`, *optional*, defaults to 1024) : Size of the window (in samples) on which the Fourier transform is applied. This controls the frequency resolution of the spectrogram. 400 means that the fourier transform is computed on windows of 400 samples.

padding_value (`float`, *optional*, defaults to 0.0) : Padding value used to pad the audio. Should correspond to silences.

return_attention_mask (`bool`, *optional*, defaults to `False`) : Whether or not the model should return the attention masks corresponding to the input.

frequency_min (`float`, *optional*, defaults to 0) : The lowest frequency of interest. The STFT will not be computed for values below this.

frequency_max (`float`, *optional*, defaults to 14000) : The highest frequency of interest. The STFT will not be computed for values above this.

top_db (`float`, *optional*) : The highest decibel value used to convert the mel spectrogram to the log scale. For more details see the `audio_utils.power_to_db` function

truncation (`str`, *optional*, defaults to `"fusion"`) : Truncation pattern for long audio inputs. Two patterns are available: - `fusion` will use `_random_mel_fusion`, which stacks 3 random crops from the mel spectrogram and a downsampled version of the entire mel spectrogram. If `config.fusion` is set to True, shorter audios also need to return 4 mels, which will just be a copy of the original mel obtained from the padded audio. - `rand_trunc` will select a random crop of the mel spectrogram.

padding (`str`, *optional*, defaults to `"repeatpad"`) : Padding pattern for shorter audio inputs. Three patterns were originally implemented: - `repeatpad`: the audio is repeated, and then padded to fit the `max_length`. - `repeat`: the audio is repeated and then cut to fit the `max_length` - `pad`: the audio is padded.

**Returns:**

``dict[str, Any]``

Dictionary of all the attributes that make up this configuration instance, except for the
mel filter banks, which do not need to be saved or printed as they are too long.

## ClapProcessor[[transformers.ClapProcessor]]

#### transformers.ClapProcessor[[transformers.ClapProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/clap/processing_clap.py#L26)

Constructs a ClapProcessor which wraps a feature extractor and a tokenizer into a single processor.

[ClapProcessor](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapProcessor) offers all the functionalities of [ClapFeatureExtractor](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapFeatureExtractor) and [RobertaTokenizer](/docs/transformers/v5.0.0/en/model_doc/mvp#transformers.RobertaTokenizer). See the
[~ClapFeatureExtractor](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapFeatureExtractor) and [~RobertaTokenizer](/docs/transformers/v5.0.0/en/model_doc/mvp#transformers.RobertaTokenizer) for more information.

__call__transformers.ClapProcessor.__call__https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/processing_utils.py#L617[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor'], NoneType] = None"}, {"name": "text", "val": ": str | list[str] | list[list[str]] | None = None"}, {"name": "videos", "val": ": typing.Union[list['PIL.Image.Image'], numpy.ndarray, ForwardRef('torch.Tensor'), list[numpy.ndarray], list['torch.Tensor'], list[list['PIL.Image.Image']], list[list[numpy.ndarray]], list[list['torch.Tensor']], transformers.video_utils.URL, list[transformers.video_utils.URL], list[list[transformers.video_utils.URL]], transformers.video_utils.Path, list[transformers.video_utils.Path], list[list[transformers.video_utils.Path]], NoneType] = None"}, {"name": "audio", "val": ": typing.Union[numpy.ndarray, ForwardRef('torch.Tensor'), collections.abc.Sequence[numpy.ndarray], collections.abc.Sequence['torch.Tensor'], NoneType] = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.processing_utils.ProcessingKwargs]"}]- **images** (`PIL.Image.Image`, `np.ndarray`, `torch.Tensor`, `list[PIL.Image.Image]`, `list[np.ndarray]`, `list[torch.Tensor]`) --
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

feature_extractor (`ClapFeatureExtractor`) : The feature extractor is a required input.

tokenizer (`RobertaTokenizer`) : The tokenizer is a required input.

**Returns:**

`[BatchFeature](/docs/transformers/v5.0.0/en/main_classes/image_processor#transformers.BatchFeature)`

A [BatchFeature](/docs/transformers/v5.0.0/en/main_classes/image_processor#transformers.BatchFeature) object with processed inputs in a dict format.

## ClapModel[[transformers.ClapModel]]

#### transformers.ClapModel[[transformers.ClapModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/clap/modeling_clap.py#L1521)

The bare Clap Model outputting raw hidden-states without any specific head on top.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.ClapModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/clap/modeling_clap.py#L1627[{"name": "input_ids", "val": ": torch.LongTensor | None = None"}, {"name": "input_features", "val": ": torch.FloatTensor | None = None"}, {"name": "is_longer", "val": ": torch.BoolTensor | None = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.LongTensor | None = None"}, {"name": "return_loss", "val": ": bool | None = None"}, {"name": "output_attentions", "val": ": bool | None = None"}, {"name": "output_hidden_states", "val": ": bool | None = None"}, {"name": "return_dict", "val": ": bool | None = None"}, {"name": "**kwargs", "val": ""}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **input_features** (`torch.FloatTensor` of shape `(batch_size, sequence_length, feature_dim)`, *optional*) --
  The tensors corresponding to the input audio features. Audio features can be obtained using
  [ClapFeatureExtractor](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapFeatureExtractor). See `ClapFeatureExtractor.__call__()` for details ([ClapProcessor](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapProcessor) uses
  [ClapFeatureExtractor](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapFeatureExtractor) for processing audios).
- **is_longer** (`torch.FloatTensor`, of shape `(batch_size, 1)`, *optional*) --
  Whether the audio clip is longer than `max_length`. If `True`, a feature fusion will be enabled to enhance
  the features.
- **attention_mask** (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.

  [What are attention masks?](../glossary#attention-mask)
- **position_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of positions of each input sequence tokens in the position embeddings. Selected in the range `[0, config.n_positions - 1]`.

  [What are position IDs?](../glossary#position-ids)
- **return_loss** (`bool`, *optional*) --
  Whether or not to return the contrastive loss.
- **output_attentions** (`bool`, *optional*) --
  Whether or not to return the attentions tensors of all attention layers. See `attentions` under returned
  tensors for more detail.
- **output_hidden_states** (`bool`, *optional*) --
  Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
  more detail.
- **return_dict** (`bool`, *optional*) --
  Whether or not to return a [ModelOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.utils.ModelOutput) instead of a plain tuple.0`transformers.models.clap.modeling_clap.ClapOutput` or `tuple(torch.FloatTensor)`A `transformers.models.clap.modeling_clap.ClapOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([ClapConfig](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `return_loss` is `True`) -- Contrastive loss for audio-text similarity.
- **logits_per_audio** (`torch.FloatTensor` of shape `(audio_batch_size, text_batch_size)`) -- The scaled dot product scores between `audio_embeds` and `text_embeds`. This represents the audio-text
  similarity scores.
- **logits_per_text** (`torch.FloatTensor` of shape `(text_batch_size, audio_batch_size)`) -- The scaled dot product scores between `text_embeds` and `audio_embeds`. This represents the text-audio
  similarity scores.
- **text_embeds** (`torch.FloatTensor` of shape `(batch_size, output_dim`) -- The text embeddings obtained by applying the projection layer to the pooled output of [ClapTextModel](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapTextModel).
- **audio_embeds** (`torch.FloatTensor` of shape `(batch_size, output_dim`) -- The audio embeddings obtained by applying the projection layer to the pooled output of [ClapAudioModel](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapAudioModel).
- **text_model_output** (`.text_model_output`, defaults to `None`) -- The output of the [ClapTextModel](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapTextModel).
- **audio_model_output** (`.audio_model_output`, defaults to `None`) -- The output of the [ClapAudioModel](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapAudioModel).
The [ClapModel](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Examples:

```python
>>> from datasets import load_dataset
>>> from transformers import AutoProcessor, ClapModel

>>> dataset = load_dataset("hf-internal-testing/ashraq-esc50-1-dog-example")
>>> audio_sample = dataset["train"]["audio"][0]["array"]

>>> model = ClapModel.from_pretrained("laion/clap-htsat-unfused")
>>> processor = AutoProcessor.from_pretrained("laion/clap-htsat-unfused")

>>> input_text = ["Sound of a dog", "Sound of vacuum cleaner"]

>>> inputs = processor(text=input_text, audio=audio_sample, return_tensors="pt", padding=True)

>>> outputs = model(**inputs)
>>> logits_per_audio = outputs.logits_per_audio  # this is the audio-text similarity score
>>> probs = logits_per_audio.softmax(dim=-1)  # we can take the softmax to get the label probabilities
```

**Parameters:**

config ([ClapConfig](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``transformers.models.clap.modeling_clap.ClapOutput` or `tuple(torch.FloatTensor)``

A `transformers.models.clap.modeling_clap.ClapOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([ClapConfig](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `return_loss` is `True`) -- Contrastive loss for audio-text similarity.
- **logits_per_audio** (`torch.FloatTensor` of shape `(audio_batch_size, text_batch_size)`) -- The scaled dot product scores between `audio_embeds` and `text_embeds`. This represents the audio-text
  similarity scores.
- **logits_per_text** (`torch.FloatTensor` of shape `(text_batch_size, audio_batch_size)`) -- The scaled dot product scores between `text_embeds` and `audio_embeds`. This represents the text-audio
  similarity scores.
- **text_embeds** (`torch.FloatTensor` of shape `(batch_size, output_dim`) -- The text embeddings obtained by applying the projection layer to the pooled output of [ClapTextModel](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapTextModel).
- **audio_embeds** (`torch.FloatTensor` of shape `(batch_size, output_dim`) -- The audio embeddings obtained by applying the projection layer to the pooled output of [ClapAudioModel](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapAudioModel).
- **text_model_output** (`.text_model_output`, defaults to `None`) -- The output of the [ClapTextModel](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapTextModel).
- **audio_model_output** (`.audio_model_output`, defaults to `None`) -- The output of the [ClapAudioModel](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapAudioModel).
#### get_text_features[[transformers.ClapModel.get_text_features]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/clap/modeling_clap.py#L1556)

Examples:

```python
>>> import torch
>>> from transformers import AutoTokenizer, ClapModel

>>> model = ClapModel.from_pretrained("laion/clap-htsat-unfused")
>>> tokenizer = AutoTokenizer.from_pretrained("laion/clap-htsat-unfused")

>>> inputs = tokenizer(["the sound of a cat", "the sound of a dog"], padding=True, return_tensors="pt")
>>> with torch.inference_mode():
...     text_features = model.get_text_features(**inputs)
```

**Parameters:**

input_ids (`torch.Tensor` of shape `(batch_size, sequence_length)`) : Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.  [What are input IDs?](../glossary#input-ids)

attention_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) : Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:  - 1 for tokens that are **not masked**, - 0 for tokens that are **masked**.  [What are attention masks?](../glossary#attention-mask)

position_ids (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) : Indices of positions of each input sequence tokens in the position embeddings. Selected in the range `[0, config.n_positions - 1]`.  [What are position IDs?](../glossary#position-ids)

**Returns:**

`[transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([ClapConfig](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapConfig)) and inputs.

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
#### get_audio_features[[transformers.ClapModel.get_audio_features]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/clap/modeling_clap.py#L1591)

Examples:

```python
>>> import torch
>>> from transformers import AutoFeatureExtractor, ClapModel

>>> model = ClapModel.from_pretrained("laion/clap-htsat-unfused")
>>> feature_extractor = AutoFeatureExtractor.from_pretrained("laion/clap-htsat-unfused")
>>> random_audio = torch.rand((16_000))

>>> inputs = feature_extractor(random_audio, return_tensors="pt")
>>> with torch.inference_mode():
...     audio_features = model.get_audio_features(**inputs)
```

**Parameters:**

input_features (`torch.Tensor` of shape `(batch_size, sequence_length, feature_dim)`) : The tensors corresponding to the input audio features. Audio features can be obtained using [ClapFeatureExtractor](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapFeatureExtractor). See `ClapFeatureExtractor.__call__()` for details ([ClapProcessor](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapProcessor) uses [ClapFeatureExtractor](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapFeatureExtractor) for processing audios).

is_longer (`torch.FloatTensor`, of shape `(batch_size, 1)`, *optional*) : Whether the audio clip is longer than `max_length`. If `True`, a feature fusion will be enabled to enhance the features.

attention_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) : Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:  - 1 for tokens that are **not masked**, - 0 for tokens that are **masked**.  [What are attention masks?](../glossary#attention-mask)

**Returns:**

`[transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([ClapConfig](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapConfig)) and inputs.

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

## ClapTextModel[[transformers.ClapTextModel]]

#### transformers.ClapTextModel[[transformers.ClapTextModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/clap/modeling_clap.py#L1422)

The model can behave as an encoder (with only self-attention) as well as a decoder, in which case a layer of
cross-attention is added between the self-attention layers, following the architecture described in *Attention is
all you need*_ by Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz
Kaiser and Illia Polosukhin.

To behave as an decoder the model needs to be initialized with the `is_decoder` argument of the configuration set
to `True`. To be used in a Seq2Seq model, the model needs to initialized with both `is_decoder` argument and
`add_cross_attention` set to `True`; an `encoder_hidden_states` is then expected as an input to the forward pass.

.. _*Attention is all you need*: https://huggingface.co/papers/1706.03762

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.ClapTextModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/clap/modeling_clap.py#L1448[{"name": "input_ids", "val": ": torch.Tensor | None = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "token_type_ids", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.Tensor | None = None"}, {"name": "inputs_embeds", "val": ": torch.Tensor | None = None"}, {"name": "output_attentions", "val": ": bool | None = None"}, {"name": "output_hidden_states", "val": ": bool | None = None"}, {"name": "return_dict", "val": ": bool | None = None"}, {"name": "**kwargs", "val": ""}]- **input_ids** (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **attention_mask** (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.

  [What are attention masks?](../glossary#attention-mask)
- **token_type_ids** (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Segment token indices to indicate first and second portions of the inputs. Indices are selected in `[0, 1]`:

  - 0 corresponds to a *sentence A* token,
  - 1 corresponds to a *sentence B* token.

  [What are token type IDs?](../glossary#token-type-ids)
- **position_ids** (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of positions of each input sequence tokens in the position embeddings. Selected in the range `[0, config.n_positions - 1]`.

  [What are position IDs?](../glossary#position-ids)
- **inputs_embeds** (`torch.Tensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) --
  Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation. This
  is useful if you want more control over how to convert `input_ids` indices into associated vectors than the
  model's internal embedding lookup matrix.
- **output_attentions** (`bool`, *optional*) --
  Whether or not to return the attentions tensors of all attention layers. See `attentions` under returned
  tensors for more detail.
- **output_hidden_states** (`bool`, *optional*) --
  Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
  more detail.
- **return_dict** (`bool`, *optional*) --
  Whether or not to return a [ModelOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.utils.ModelOutput) instead of a plain tuple.0[transformers.modeling_outputs.BaseModelOutputWithPoolingAndCrossAttentions](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPoolingAndCrossAttentions) or `tuple(torch.FloatTensor)`A [transformers.modeling_outputs.BaseModelOutputWithPoolingAndCrossAttentions](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPoolingAndCrossAttentions) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([ClapConfig](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapConfig)) and inputs.

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
- **cross_attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` and `config.add_cross_attention=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights of the decoder's cross-attention layer, after the attention softmax, used to compute the
  weighted average in the cross-attention heads.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks and optionally if
  `config.is_encoder_decoder=True` in the cross-attention blocks) that can be used (see `past_key_values`
  input) to speed up sequential decoding.
The [ClapTextModel](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapTextModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

**Parameters:**

config ([ClapTextModel](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapTextModel)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

add_pooling_layer (`bool`, *optional*, defaults to `True`) : Whether to add a pooling layer

**Returns:**

`[transformers.modeling_outputs.BaseModelOutputWithPoolingAndCrossAttentions](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPoolingAndCrossAttentions) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutputWithPoolingAndCrossAttentions](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPoolingAndCrossAttentions) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([ClapConfig](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapConfig)) and inputs.

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
- **cross_attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` and `config.add_cross_attention=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights of the decoder's cross-attention layer, after the attention softmax, used to compute the
  weighted average in the cross-attention heads.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks and optionally if
  `config.is_encoder_decoder=True` in the cross-attention blocks) that can be used (see `past_key_values`
  input) to speed up sequential decoding.

## ClapTextModelWithProjection[[transformers.ClapTextModelWithProjection]]

#### transformers.ClapTextModelWithProjection[[transformers.ClapTextModelWithProjection]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/clap/modeling_clap.py#L1727)

The Clap Model with a projection layer on top (a linear layer on top of the pooled output).

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.ClapTextModelWithProjection.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/clap/modeling_clap.py#L1744[{"name": "input_ids", "val": ": torch.Tensor | None = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.Tensor | None = None"}, {"name": "output_attentions", "val": ": bool | None = None"}, {"name": "output_hidden_states", "val": ": bool | None = None"}, {"name": "return_dict", "val": ": bool | None = None"}, {"name": "**kwargs", "val": ""}]- **input_ids** (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **attention_mask** (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.

  [What are attention masks?](../glossary#attention-mask)
- **position_ids** (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of positions of each input sequence tokens in the position embeddings. Selected in the range `[0, config.n_positions - 1]`.

  [What are position IDs?](../glossary#position-ids)
- **output_attentions** (`bool`, *optional*) --
  Whether or not to return the attentions tensors of all attention layers. See `attentions` under returned
  tensors for more detail.
- **output_hidden_states** (`bool`, *optional*) --
  Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
  more detail.
- **return_dict** (`bool`, *optional*) --
  Whether or not to return a [ModelOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.utils.ModelOutput) instead of a plain tuple.0`transformers.models.clap.modeling_clap.ClapTextModelOutput` or `tuple(torch.FloatTensor)`A `transformers.models.clap.modeling_clap.ClapTextModelOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([ClapConfig](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapConfig)) and inputs.

- **text_embeds** (`torch.FloatTensor` of shape `(batch_size, output_dim)` *optional* returned when model is initialized with `with_projection=True`) -- The text embeddings obtained by applying the projection layer to the pooler_output.
- **last_hidden_state** (`torch.FloatTensor | None.last_hidden_state` of shape `(batch_size, sequence_length, hidden_size)`, defaults to `None`) -- Sequence of hidden-states at the output of the last layer of the model.
- **hidden_states** (`tuple[torch.FloatTensor, ...] | None.hidden_states`, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple[torch.FloatTensor, ...] | None.attentions`, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
The [ClapTextModelWithProjection](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapTextModelWithProjection) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Examples:

```python
>>> from transformers import AutoTokenizer, ClapTextModelWithProjection

>>> model = ClapTextModelWithProjection.from_pretrained("laion/clap-htsat-unfused")
>>> tokenizer = AutoTokenizer.from_pretrained("laion/clap-htsat-unfused")

>>> inputs = tokenizer(["a sound of a cat", "a sound of a dog"], padding=True, return_tensors="pt")

>>> outputs = model(**inputs)
>>> text_embeds = outputs.text_embeds
```

**Parameters:**

config ([ClapTextConfig](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapTextConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``transformers.models.clap.modeling_clap.ClapTextModelOutput` or `tuple(torch.FloatTensor)``

A `transformers.models.clap.modeling_clap.ClapTextModelOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([ClapConfig](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapConfig)) and inputs.

- **text_embeds** (`torch.FloatTensor` of shape `(batch_size, output_dim)` *optional* returned when model is initialized with `with_projection=True`) -- The text embeddings obtained by applying the projection layer to the pooler_output.
- **last_hidden_state** (`torch.FloatTensor | None.last_hidden_state` of shape `(batch_size, sequence_length, hidden_size)`, defaults to `None`) -- Sequence of hidden-states at the output of the last layer of the model.
- **hidden_states** (`tuple[torch.FloatTensor, ...] | None.hidden_states`, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple[torch.FloatTensor, ...] | None.attentions`, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.

## ClapAudioModel[[transformers.ClapAudioModel]]

#### transformers.ClapAudioModel[[transformers.ClapAudioModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/clap/modeling_clap.py#L1347)

forwardtransformers.ClapAudioModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/clap/modeling_clap.py#L1361[{"name": "input_features", "val": ": torch.FloatTensor | None = None"}, {"name": "is_longer", "val": ": torch.BoolTensor | None = None"}, {"name": "output_attentions", "val": ": bool | None = None"}, {"name": "output_hidden_states", "val": ": bool | None = None"}, {"name": "return_dict", "val": ": bool | None = None"}, {"name": "**kwargs", "val": ""}]- **input_features** (`torch.FloatTensor` of shape `(batch_size, sequence_length, feature_dim)`, *optional*) --
  The tensors corresponding to the input audio features. Audio features can be obtained using
  [ClapFeatureExtractor](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapFeatureExtractor). See `ClapFeatureExtractor.__call__()` for details ([ClapProcessor](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapProcessor) uses
  [ClapFeatureExtractor](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapFeatureExtractor) for processing audios).
- **is_longer** (`torch.FloatTensor`, of shape `(batch_size, 1)`, *optional*) --
  Whether the audio clip is longer than `max_length`. If `True`, a feature fusion will be enabled to enhance
  the features.
- **output_attentions** (`bool`, *optional*) --
  Whether or not to return the attentions tensors of all attention layers. See `attentions` under returned
  tensors for more detail.
- **output_hidden_states** (`bool`, *optional*) --
  Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
  more detail.
- **return_dict** (`bool`, *optional*) --
  Whether or not to return a [ModelOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.utils.ModelOutput) instead of a plain tuple.0[transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)`A [transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([ClapConfig](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapConfig)) and inputs.

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
The [ClapAudioModel](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapAudioModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Examples:

```python
>>> from datasets import load_dataset
>>> from transformers import AutoProcessor, ClapAudioModel

>>> dataset = load_dataset("hf-internal-testing/ashraq-esc50-1-dog-example")
>>> audio_sample = dataset["train"]["audio"][0]["array"]

>>> model = ClapAudioModel.from_pretrained("laion/clap-htsat-fused")
>>> processor = AutoProcessor.from_pretrained("laion/clap-htsat-fused")

>>> inputs = processor(audio=audio_sample, return_tensors="pt")

>>> outputs = model(**inputs)
>>> last_hidden_state = outputs.last_hidden_state
```

**Parameters:**

input_features (`torch.FloatTensor` of shape `(batch_size, sequence_length, feature_dim)`, *optional*) : The tensors corresponding to the input audio features. Audio features can be obtained using [ClapFeatureExtractor](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapFeatureExtractor). See `ClapFeatureExtractor.__call__()` for details ([ClapProcessor](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapProcessor) uses [ClapFeatureExtractor](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapFeatureExtractor) for processing audios).

is_longer (`torch.FloatTensor`, of shape `(batch_size, 1)`, *optional*) : Whether the audio clip is longer than `max_length`. If `True`, a feature fusion will be enabled to enhance the features.

output_attentions (`bool`, *optional*) : Whether or not to return the attentions tensors of all attention layers. See `attentions` under returned tensors for more detail.

output_hidden_states (`bool`, *optional*) : Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for more detail.

return_dict (`bool`, *optional*) : Whether or not to return a [ModelOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.utils.ModelOutput) instead of a plain tuple.

**Returns:**

`[transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([ClapConfig](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapConfig)) and inputs.

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

## ClapAudioModelWithProjection[[transformers.ClapAudioModelWithProjection]]

#### transformers.ClapAudioModelWithProjection[[transformers.ClapAudioModelWithProjection]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/clap/modeling_clap.py#L1794)

The Clap Model with a projection layer on top (a linear layer on top of the pooled output).

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.ClapAudioModelWithProjection.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/clap/modeling_clap.py#L1809[{"name": "input_features", "val": ": torch.FloatTensor | None = None"}, {"name": "is_longer", "val": ": torch.BoolTensor | None = None"}, {"name": "output_attentions", "val": ": bool | None = None"}, {"name": "output_hidden_states", "val": ": bool | None = None"}, {"name": "return_dict", "val": ": bool | None = None"}, {"name": "**kwargs", "val": ""}]- **input_features** (`torch.FloatTensor` of shape `(batch_size, sequence_length, feature_dim)`, *optional*) --
  The tensors corresponding to the input audio features. Audio features can be obtained using
  [ClapFeatureExtractor](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapFeatureExtractor). See `ClapFeatureExtractor.__call__()` for details ([ClapProcessor](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapProcessor) uses
  [ClapFeatureExtractor](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapFeatureExtractor) for processing audios).
- **is_longer** (`torch.FloatTensor`, of shape `(batch_size, 1)`, *optional*) --
  Whether the audio clip is longer than `max_length`. If `True`, a feature fusion will be enabled to enhance
  the features.
- **output_attentions** (`bool`, *optional*) --
  Whether or not to return the attentions tensors of all attention layers. See `attentions` under returned
  tensors for more detail.
- **output_hidden_states** (`bool`, *optional*) --
  Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
  more detail.
- **return_dict** (`bool`, *optional*) --
  Whether or not to return a [ModelOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.utils.ModelOutput) instead of a plain tuple.0`transformers.models.clap.modeling_clap.ClapAudioModelOutput` or `tuple(torch.FloatTensor)`A `transformers.models.clap.modeling_clap.ClapAudioModelOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([ClapConfig](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapConfig)) and inputs.

- **audio_embeds** (`torch.FloatTensor` of shape `(batch_size, hidden_size)`) -- The Audio embeddings obtained by applying the projection layer to the pooler_output.
- **last_hidden_state** (`torch.FloatTensor | None.last_hidden_state` of shape `(batch_size, sequence_length, hidden_size)`, defaults to `None`) -- Sequence of hidden-states at the output of the last layer of the model.
- **hidden_states** (`tuple[torch.FloatTensor, ...] | None.hidden_states`, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple[torch.FloatTensor, ...] | None.attentions`, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
The [ClapAudioModelWithProjection](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapAudioModelWithProjection) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Examples:

```python
>>> from datasets import load_dataset
>>> from transformers import ClapAudioModelWithProjection, ClapProcessor

>>> model = ClapAudioModelWithProjection.from_pretrained("laion/clap-htsat-fused")
>>> processor = ClapProcessor.from_pretrained("laion/clap-htsat-fused")

>>> dataset = load_dataset("hf-internal-testing/ashraq-esc50-1-dog-example")
>>> audio_sample = dataset["train"]["audio"][0]["array"]

>>> inputs = processor(audio=audio_sample, return_tensors="pt")
>>> outputs = model(**inputs)
>>> audio_embeds = outputs.audio_embeds
```

**Parameters:**

config ([ClapAudioConfig](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapAudioConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``transformers.models.clap.modeling_clap.ClapAudioModelOutput` or `tuple(torch.FloatTensor)``

A `transformers.models.clap.modeling_clap.ClapAudioModelOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([ClapConfig](/docs/transformers/v5.0.0/en/model_doc/clap#transformers.ClapConfig)) and inputs.

- **audio_embeds** (`torch.FloatTensor` of shape `(batch_size, hidden_size)`) -- The Audio embeddings obtained by applying the projection layer to the pooler_output.
- **last_hidden_state** (`torch.FloatTensor | None.last_hidden_state` of shape `(batch_size, sequence_length, hidden_size)`, defaults to `None`) -- Sequence of hidden-states at the output of the last layer of the model.
- **hidden_states** (`tuple[torch.FloatTensor, ...] | None.hidden_states`, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple[torch.FloatTensor, ...] | None.attentions`, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.

