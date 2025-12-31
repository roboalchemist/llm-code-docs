# Source: https://huggingface.co/docs/transformers/v5.0.0rc1/model_doc/mimi.md

# Mimi

[Mimi](huggingface.co/papers/2410.00037) is a neural audio codec model with pretrained and quantized variants, designed for efficient speech representation and compression. The model operates at 1.1 kbps with a 12 Hz frame rate and uses a convolutional encoder-decoder architecture combined with a residual vector quantizer of 16 codebooks. Mimi outputs dual token streams i.e. semantic and acoustic to balance linguistic richness with high fidelity reconstruction. Key features include a causal streaming encoder for low-latency use, dual-path tokenization for flexible downstream generation, and integration readiness with large speech models like Moshi.

You can find the original Mimi checkpoints under the [Kyutai](https://huggingface.co/kyutai/models?search=mimi) organization.

>[!TIP]
> This model was contributed by [ylacombe](https://huggingface.co/ylacombe).
>
> Click on the Mimi models in the right sidebar for more examples of how to apply Mimi.

The example below demonstrates how to encode and decode audio with the [AutoModel](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoModel) class.

```python
>>> from datasets import load_dataset, Audio
>>> from transformers import MimiModel, AutoFeatureExtractor
>>> librispeech_dummy = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")

>>> # load model and feature extractor
>>> model = MimiModel.from_pretrained("kyutai/mimi")
>>> feature_extractor = AutoFeatureExtractor.from_pretrained("kyutai/mimi")

>>> # load audio sample
>>> librispeech_dummy = librispeech_dummy.cast_column("audio", Audio(sampling_rate=feature_extractor.sampling_rate))
>>> audio_sample = librispeech_dummy[-1]["audio"]["array"]
>>> inputs = feature_extractor(raw_audio=audio_sample, sampling_rate=feature_extractor.sampling_rate, return_tensors="pt")

>>> encoder_outputs = model.encode(inputs["input_values"], inputs["padding_mask"])
>>> audio_values = model.decode(encoder_outputs.audio_codes, inputs["padding_mask"])[0]
>>> # or the equivalent with a forward pass
>>> audio_values = model(inputs["input_values"], inputs["padding_mask"]).audio_values
```

## MimiConfig[[transformers.MimiConfig]]

#### transformers.MimiConfig[[transformers.MimiConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/mimi/configuration_mimi.py#L30)

This is the configuration class to store the configuration of an [MimiModel](/docs/transformers/v5.0.0rc1/en/model_doc/mimi#transformers.MimiModel). It is used to instantiate a
Mimi model according to the specified arguments, defining the model architecture. Instantiating a configuration
with the defaults will yield a similar configuration to that of the
[kyutai/mimi](https://huggingface.co/kyutai/mimi) architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:

```python
>>> from transformers import MimiModel, MimiConfig

>>> # Initializing a "kyutai/mimi" style configuration
>>> configuration = MimiConfig()

>>> # Initializing a model (with random weights) from the "kyutai/mimi" style configuration
>>> model = MimiModel(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

sampling_rate (`int`, *optional*, defaults to 24000) : The sampling rate at which the audio waveform should be digitalized expressed in hertz (Hz).

frame_rate (`float`, *optional*) : Should be computed from the other parameters, yet kept for backward compatibility.

audio_channels (`int`, *optional*, defaults to 1) : Number of channels in the audio data. Either 1 for mono or 2 for stereo.

hidden_size (`int`, *optional*, defaults to 512) : Intermediate representation dimension.

num_filters (`int`, *optional*, defaults to 64) : Number of convolution kernels of first `MimiConv1d` down sampling layer.

num_residual_layers (`int`,  *optional*, defaults to 1) : Number of residual layers.

upsampling_ratios (`Sequence[int]`, *optional*) : Kernel size and stride ratios. The encoder uses downsampling ratios instead of upsampling ratios, hence it will use the ratios in the reverse order to the ones specified here that must match the decoder order. If not specified, will defaults to `[8, 6, 5, 4]`

kernel_size (`int`, *optional*, defaults to 7) : Kernel size for the initial convolution.

last_kernel_size (`int`, *optional*, defaults to 3) : Kernel size for the last convolution layer.

residual_kernel_size (`int`, *optional*, defaults to 3) : Kernel size for the residual layers.

dilation_growth_rate (`int`, *optional*, defaults to 2) : How much to increase the dilation with each layer.

use_causal_conv (`bool`, *optional*, defaults to `True`) : Whether to use fully causal convolution.

pad_mode (`str`, *optional*, defaults to `"constant"`) : Padding mode for the convolutions.

compress (`int`, *optional*, defaults to 2) : Reduced dimensionality in residual branches.

trim_right_ratio (`float`, *optional*, defaults to 1.0) : Ratio for trimming at the right of the transposed convolution under the `use_causal_conv = True` setup. If equal to 1.0, it means that all the trimming is done at the right.

codebook_size (`int`, *optional*, defaults to 2048) : Number of discret codes in each codebooks.

codebook_dim (`int`, *optional*, defaults to 256) : Dimension of the unquantized codebook vectors. If not defined, uses `hidden_size`.

num_quantizers (`int`, *optional*, defaults to 32) : Number of quantizer channels, or codebooks, in the quantizer.

use_conv_shortcut (`bool`, *optional*, defaults to `False`) : Whether to use a convolutional layer as the 'skip' connection in the `MimiResnetBlock` block. If False, an identity function will be used, giving a generic residual connection.

vector_quantization_hidden_dimension (`int`, *optional*, defaults to 256) : Intermediate representation dimension in the residual vector quantization space.

num_semantic_quantizers (`int`, *optional*, defaults to 1) : Number of semantic quantizer channels, or codebooks, in the semantic quantizer. Must be lower than `num_quantizers`.

upsample_groups (`int`, *optional*, defaults to 512) : If `frame_rate!=encodec_frame_rate`, indicates the number of groups used in the upsampling operation to go from one rate to another.

num_hidden_layers (`int`, *optional*, defaults to 8) : Number of hidden layers in the Transformer models.

intermediate_size (`int`, *optional*, defaults to 2048) : Dimension of the MLP representations.

num_attention_heads (`int`, *optional*, defaults to 8) : Number of attention heads for each attention layer in the Transformer encoder.

num_key_value_heads (`int`, *optional*, defaults to 8) : This is the number of key_value heads that should be used to implement Grouped Query Attention. If `num_key_value_heads=num_attention_heads`, the model will use Multi Head Attention (MHA), if `num_key_value_heads=1` the model will use Multi Query Attention (MQA) otherwise GQA is used. When converting a multi-head checkpoint to a GQA checkpoint, each group key and value head should be constructed by meanpooling all the original heads within that group. For more details, check out [this paper](https://huggingface.co/papers/2305.13245). If it is not specified, will default to `8`.

head_dim (`int`, *optional*, defaults to `hidden_size // num_attention_heads`) : The attention head dimension.

hidden_act (`str` or `function`, *optional*, defaults to `"gelu"`) : The non-linear activation function (function or string) in the decoder.

max_position_embeddings (`int`, *optional*, defaults to 8000) : The maximum sequence length that this model might ever be used with. Mimi's sliding window attention allows sequence of up to 8000 tokens.

initializer_range (`float`, *optional*, defaults to 0.02) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

norm_eps (`float`, *optional*, defaults to 1e-05) : The epsilon used by the LayerNorm normalization layers.

use_cache (`bool`, *optional*, defaults to `False`) : Whether or not the model should return the last key/values attentions (not used by all models). Only relevant if `config.is_decoder=True`.

use_streaming (`bool`, *optional*, defaults to `False`) : Whether to use streaming mode. If `True`, the model encode method will return the padding cache that can be used in a subsequent call to the encode method.

rope_parameters (`RopeParameters`, *optional*) : Dictionary containing the configuration parameters for the RoPE embeddings. The dictionary should contain a value for `rope_theta` and optionally parameters used for scaling in case you want to use RoPE with longer `max_position_embeddings`.

sliding_window (`int`, *optional*, defaults to 250) : Sliding window attention window size. If not specified, will default to `250`.

attention_dropout (`float`, *optional*, defaults to 0.0) : The dropout ratio for the attention probabilities.

layer_scale_initial_scale (`float`, *optional*, defaults to 0.01) : Initial scale of the residual rescaling operation done in the Transformer models.

attention_bias (`bool`, defaults to `False`, *optional*, defaults to `False`) : Whether to use a bias in the query, key, value and output projection layers during self-attention.

## MimiModel[[transformers.MimiModel]]

#### transformers.MimiModel[[transformers.MimiModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/mimi/modeling_mimi.py#L1414)

The Mimi neural audio codec model.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

decodetransformers.MimiModel.decodehttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/mimi/modeling_mimi.py#L1631[{"name": "audio_codes", "val": ": Tensor"}, {"name": "padding_mask", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "decoder_past_key_values", "val": ": typing.Optional[transformers.cache_utils.Cache] = None"}, {"name": "return_dict", "val": ": typing.Optional[bool] = None"}]- **audio_codes** (`torch.LongTensor`  of shape `(batch_size, num_quantizers, codes_length)`, *optional*) --
  Discret code embeddings computed using `model.encode`.
- **padding_mask** (`torch.Tensor` of shape `(batch_size, channels, sequence_length)`) --
  Indicates which inputs are to be ignored due to padding, where elements are either 1 for *not masked* or 0
  for *masked*.
- **decoder_past_key_values** (`Cache`, *optional*) --
  Pre-computed hidden-states (key and values in the self-attention blocks) that can be used to speed up sequential decoding of the decoder transformer.
  This typically consists in the `past_key_values` returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.

  The model will output the same cache format that is fed as input.

  If `past_key_values` are used, the user can optionally input only the last `audio_values` or `audio_codes (those that don't
  have their past key value states given to this model).
- **return_dict** (`bool`, *optional*) --
  Whether or not to return a [ModelOutput](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.utils.ModelOutput) instead of a plain tuple.0

Decodes the given frames into an output audio waveform.

Note that the output might be a bit bigger than the input. In that case, any extra steps at the end can be
trimmed.

**Parameters:**

config ([MimiConfig](/docs/transformers/v5.0.0rc1/en/model_doc/mimi#transformers.MimiConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.
#### encode[[transformers.MimiModel.encode]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/mimi/modeling_mimi.py#L1521)

Encodes the input audio waveform into discrete codes.

**Parameters:**

input_values (`torch.Tensor` of shape `(batch_size, channels, sequence_length)`) : Float values of the input audio waveform.

padding_mask (`torch.Tensor` of shape `(batch_size, channels, sequence_length)`) : Indicates which inputs are to be ignored due to padding, where elements are either 1 for *not masked* or 0 for *masked*.

num_quantizers (`int`, *optional*) : Number of quantizers (i.e codebooks) to use. By default, all quantizers are used.

encoder_past_key_values (`Cache`, *optional*) : Pre-computed hidden-states (key and values in the self-attention blocks) that can be used to speed up sequential decoding of the encoder transformer. This typically consists in the `past_key_values` returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.  The model will output the same cache format that is fed as input.  If `past_key_values` are used, the user can optionally input only the last `audio_values` or `audio_codes (those that don't have their past key value states given to this model).

return_dict (`bool`, *optional*) : Whether or not to return a [ModelOutput](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.utils.ModelOutput) instead of a plain tuple.

**Returns:**

`codebook` of shape `[batch_size, num_codebooks, frames]`, the discrete encoded codes for the input audio waveform.
#### forward[[transformers.MimiModel.forward]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/mimi/modeling_mimi.py#L1679)

The [MimiModel](/docs/transformers/v5.0.0rc1/en/model_doc/mimi#transformers.MimiModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Examples:

```python
>>> from datasets import load_dataset
>>> from transformers import AutoFeatureExtractor, MimiModel

>>> dataset = load_dataset("hf-internal-testing/ashraq-esc50-1-dog-example")
>>> audio_sample = dataset["train"]["audio"][0]["array"]

>>> model_id = "kyutai/mimi"
>>> model = MimiModel.from_pretrained(model_id)
>>> feature_extractor = AutoFeatureExtractor.from_pretrained(model_id)

>>> inputs = feature_extractor(raw_audio=audio_sample, return_tensors="pt")

>>> outputs = model(**inputs)
>>> audio_codes = outputs.audio_codes
>>> audio_values = outputs.audio_values
```

**Parameters:**

input_values (`torch.FloatTensor` of shape `(batch_size, channels, sequence_length)`, *optional*) : Raw audio input converted to Float.

padding_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) : Indicates which inputs are to be ignored due to padding, where elements are either 1 for *not masked* or 0 for *masked*.

num_quantizers (`int`, *optional*) : Number of quantizers (i.e codebooks) to use. By default, all quantizers are used.

audio_codes (`torch.LongTensor`  of shape `(batch_size, num_quantizers, codes_length)`, *optional*) : Discret code embeddings computed using `model.encode`.

encoder_past_key_values (`Cache`, *optional*) : Pre-computed hidden-states (key and values in the self-attention blocks) that can be used to speed up sequential decoding of the encoder transformer. This typically consists in the `past_key_values` returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.  The model will output the same cache format that is fed as input.  If `past_key_values` are used, the user can optionally input only the last `audio_values` or `audio_codes (those that don't have their past key value states given to this model).

decoder_past_key_values (`Cache`, *optional*) : Pre-computed hidden-states (key and values in the self-attention blocks) that can be used to speed up sequential decoding of the decoder transformer. This typically consists in the `past_key_values` returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.  The model will output the same cache format that is fed as input.  If `past_key_values` are used, the user can optionally input only the last `audio_values` or `audio_codes (those that don't have their past key value states given to this model).

return_dict (`bool`, *optional*) : Whether or not to return a [ModelOutput](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.utils.ModelOutput) instead of a plain tuple.

**Returns:**

``transformers.models.mimi.modeling_mimi.MimiOutput` or `tuple(torch.FloatTensor)``

A `transformers.models.mimi.modeling_mimi.MimiOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([MimiConfig](/docs/transformers/v5.0.0rc1/en/model_doc/mimi#transformers.MimiConfig)) and inputs.

- **audio_codes** (`torch.LongTensor`  of shape `(batch_size, num_quantizers, codes_length)`, *optional*) -- Discret code embeddings computed using `model.encode`.
- **audio_values** (`torch.FloatTensor` of shape `(batch_size, sequence_length)`, *optional*) -- Decoded audio values, obtained using the decoder part of Mimi.
- **encoder_past_key_values** (`Cache`, *optional*) -- Pre-computed hidden-states (key and values in the self-attention blocks) that can be used to speed up sequential decoding of the encoder transformer.
  This typically consists in the `past_key_values` returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.

  The model will output the same cache format that is fed as input.

  If `past_key_values` are used, the user can optionally input only the last `audio_values` or `audio_codes (those that don't
  have their past key value states given to this model).
- **decoder_past_key_values** (`Cache`, *optional*) -- Pre-computed hidden-states (key and values in the self-attention blocks) that can be used to speed up sequential decoding of the decoder transformer.
  This typically consists in the `past_key_values` returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.

  The model will output the same cache format that is fed as input.

  If `past_key_values` are used, the user can optionally input only the last `audio_values` or `audio_codes (those that don't
  have their past key value states given to this model).

