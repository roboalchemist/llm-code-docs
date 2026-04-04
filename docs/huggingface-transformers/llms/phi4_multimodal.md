# Source: https://huggingface.co/docs/transformers/v5.0.0/model_doc/phi4_multimodal.md

## Phi4 Multimodal

[Phi4 Multimodal](https://huggingface.co/papers/2503.01743) is a multimodal model capable of text, image, and speech and audio inputs or any combination of these. It features a mixture of LoRA adapters for handling different inputs, and each input is routed to the appropriate encoder.

You can find all the original Phi4 Multimodal checkpoints under the [Phi4](https://huggingface.co/collections/microsoft/phi-4-677e9380e514feb5577a40e4) collection.

> [!TIP]
> This model was contributed by [cyrilvallez](https://huggingface.co/cyrilvallez).
>
> Click on the Phi-4 Multimodal in the right sidebar for more examples of how to apply Phi-4 Multimodal to different tasks.

The example below demonstrates how to generate text based on an image with [Pipeline](/docs/transformers/v5.0.0/en/main_classes/pipelines#transformers.Pipeline) or the [AutoModel](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoModel) class.

```python
from transformers import pipeline
generator = pipeline("text-generation", model="microsoft/Phi-4-multimodal-instruct", dtype="auto", device=0)

prompt = "Explain the concept of multimodal AI in simple terms."

result = generator(prompt, max_length=50)
print(result[0]['generated_text'])
```

```python
import torch
from transformers import AutoModelForCausalLM, AutoProcessor, GenerationConfig
from accelerate import Accelerator

model_path = "microsoft/Phi-4-multimodal-instruct"
device = Accelerator().device

processor = AutoProcessor.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path, device_map=device, dtype=torch.float16)

model.load_adapter(model_path, adapter_name="vision", device_map=device, adapter_kwargs={"subfolder": 'vision-lora'})

messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "url": "https://www.ilankelman.org/stopsigns/australia.jpg"},
            {"type": "text", "text": "What is shown in this image?"},
        ],
    },
]

model.set_adapter("vision")
inputs = processor.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
).to(model.device)

generate_ids = model.generate(
    **inputs,
    max_new_tokens=1000,
    do_sample=False,
)
generate_ids = generate_ids[:, inputs['input_ids'].shape[1]:]
response = processor.batch_decode(
    generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False
)[0]
print(f'>>> Response\n{response}')
```

## Notes

The example below demonstrates inference with an audio and text input.

```py
import torch
from transformers import AutoModelForCausalLM, AutoProcessor, GenerationConfig
from accelerate import Accelerator

model_path = "microsoft/Phi-4-multimodal-instruct"
device = Accelerator().device

processor = AutoProcessor.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path, device_map=device,  dtype=torch.float16)

model.load_adapter(model_path, adapter_name="speech", device_map=device, adapter_kwargs={"subfolder": 'speech-lora'})
model.set_adapter("speech")
audio_url = "https://upload.wikimedia.org/wikipedia/commons/b/b0/Barbara_Sahakian_BBC_Radio4_The_Life_Scientific_29_May_2012_b01j5j24.flac"
messages = [
    {
        "role": "user",
        "content": [
            {"type": "audio", "url": audio_url},
            {"type": "text", "text": "Transcribe the audio to text, and then translate the audio to French. Use  as a separator between the origina transcript and the translation."},
        ],
    },
]

inputs = processor.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
).to(model.device)

generate_ids = model.generate(
    **inputs,
    max_new_tokens=1000,
    do_sample=False,
)
generate_ids = generate_ids[:, inputs['input_ids'].shape[1]:]
response = processor.batch_decode(
    generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False
)[0]
print(f'>>> Response\n{response}')

```

## Phi4MultimodalFeatureExtractor[[transformers.Phi4MultimodalFeatureExtractor]]

#### transformers.Phi4MultimodalFeatureExtractor[[transformers.Phi4MultimodalFeatureExtractor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/phi4_multimodal/feature_extraction_phi4_multimodal.py#L34)

## Phi4MultimodalImageProcessorFast[[transformers.Phi4MultimodalImageProcessorFast]]

#### transformers.Phi4MultimodalImageProcessorFast[[transformers.Phi4MultimodalImageProcessorFast]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/phi4_multimodal/image_processing_phi4_multimodal_fast.py#L51)

Constructs a fast Phi4 Multimodal image processor.

pad_to_max_num_cropstransformers.Phi4MultimodalImageProcessorFast.pad_to_max_num_cropshttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/phi4_multimodal/image_processing_phi4_multimodal_fast.py#L140[{"name": "images", "val": ""}, {"name": "max_crops", "val": " = 5"}]

images: B x 3 x H x W, B>> from transformers import Phi4MultimodalAudioConfig

>>> # Initializing a Phi4MultimodalAudioConfig with microsoft/Phi-4-multimodal-instruct style configuration
>>> configuration = Phi4MultimodalAudioConfig()
```

**Parameters:**

hidden_size (`int`, *optional*, defaults to 1024) : Dimensionality of the encoder layers.

intermediate_size (`int`, *optional*, defaults to 1536) : Dimensionality of the "intermediate" (i.e., feed-forward) layer in the Transformer encoder.

num_blocks (`int`, *optional*, defaults to 24) : Number of hidden layers in the Transformer encoder.

num_attention_heads (`int`, *optional*, defaults to 16) : Number of attention heads for each attention layer in the Transformer encoder.

activation (`str`, *optional*, defaults to `"swish"`) : The non-linear activation function in the MLPs.

chunk_size (`int`, *optional*, defaults to -1) : The chunk size to create the masks.

left_chunk (`int`, *optional*, defaults to 18) : The left chunk to create the masks.

dropout_rate (`float`, *optional*, defaults to 0.0) : The dropout ratio.

ext_pw_out_channel (`int`, *optional*, defaults to 1024) : Number of out channels in the point-wise conv modules.

depthwise_separable_out_channel (`int`, *optional*, defaults to 1024) : Number of out channels in the depth-wise separable conv modules.

depthwise_multiplier (`int`, *optional*, defaults to 1) : Input size multiplier for the depth-wise separable conv modules.

kernel_size (`int`, *optional*, defaults to 3) : Kernel size for the depth-wise separable conv modules.

conv_activation (`str`, *optional*, defaults to `"swish"`) : The non-linear activation function in the conv modules.

input_size (`int`, *optional*, defaults to 80) : Input size for the audio model.

conv_glu_type (`str`, *optional*, defaults to `"swish"`) : The non-linear activation function in the point-wise conv modules.

time_reduction (`int`, *optional*, defaults to 8) : Time reduction (subsampling factor).

bias_max_distance (`int`, *optional*, defaults to 1000) : Max distance for the relative attention bias module.

bias_symmetric (`bool`, *optional*, defaults to `False`) : Whether the relative attention bias should be symmetric or not.

nemo_activation (`str`, *optional*, defaults to `"relu"`) : The non-linear activation function in the nemo conv modules.

nemo_conv_channels (`int`, *optional*, defaults to 1024) : Number of channels in the nemo conv modules.

downsample_rate (`int`, *optional*, defaults to 1) : Downsample rate for the audio feature extractor.

initializer_range (`float`, *optional*, defaults to 0.02) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

audio_token_id (`int`, *optional*, defaults to 200011) : The audio token id.

feature_layer (`int`, *optional*, defaults to -2) : The index of the layer of the encoder from which to extract audio features.

## Phi4MultimodalVisionConfig[[transformers.Phi4MultimodalVisionConfig]]

#### transformers.Phi4MultimodalVisionConfig[[transformers.Phi4MultimodalVisionConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/phi4_multimodal/configuration_phi4_multimodal.py#L27)

This is the configuration class to store the configuration of a [Phi4MultimodalVisionModel](/docs/transformers/v5.0.0/en/model_doc/phi4_multimodal#transformers.Phi4MultimodalVisionModel). It is used to instantiate a
Phi4Multimodal vision encoder according to the specified arguments, defining the model architecture. Instantiating a
configuration with the defaults will yield a similar configuration to that of the vision encoder of
[microsoft/Phi-4-multimodal-instruct](https://huggingface.co/microsoft/Phi-4-multimodal-instruct) architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:

```python
>>> from transformers import Phi4MultimodalVisionConfig

>>> # Initializing a Phi4MultimodalVisionConfig with microsoft/Phi-4-multimodal-instruct style configuration
>>> configuration = Phi4MultimodalVisionConfig()
```

**Parameters:**

hidden_size (`int`, *optional*, defaults to 1152) : Dimensionality of the encoder layers and the pooler layer.

intermediate_size (`int`, *optional*, defaults to 4304) : Dimensionality of the "intermediate" (i.e., feed-forward) layer in the Transformer encoder.

num_hidden_layers (`int`, *optional*, defaults to 27) : Number of hidden layers in the Transformer encoder.

num_attention_heads (`int`, *optional*, defaults to 16) : Number of attention heads for each attention layer in the Transformer encoder.

num_channels (`int`, *optional*, defaults to 3) : Number of channels in the input images.

image_size (`int`, *optional*, defaults to 448) : The size (resolution) of each image.

patch_size (`int`, *optional*, defaults to 14) : The size (resolution) of each patch.

hidden_act (`str` or `function`, *optional*, defaults to `"gelu_pytorch_tanh"`) : The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`, `"relu"`, `"selu"` and `"gelu_new"` `"quick_gelu"` are supported.

layer_norm_eps (`float`, *optional*, defaults to 1e-06) : The epsilon used by the layer normalization layers.

attention_dropout (`float`, *optional*, defaults to 0.0) : The dropout ratio for the attention probabilities.

crop_size (`int`, *optional*, defaults to 448) : Crop size for the input images.

image_token_id (`int`, *optional*, defaults to 200010) : The image token id.

feature_layer (`int`, *optional*, defaults to -2) : The index of the layer of the encoder from which to extract image features.

## Phi4MultimodalConfig[[transformers.Phi4MultimodalConfig]]

#### transformers.Phi4MultimodalConfig[[transformers.Phi4MultimodalConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/phi4_multimodal/configuration_phi4_multimodal.py#L245)

This is the configuration class to store the configuration of a [Phi4MultimodalModel](/docs/transformers/v5.0.0/en/model_doc/phi4_multimodal#transformers.Phi4MultimodalModel). It is used to instantiate a
Phi4Multimodal model according to the specified arguments, defining the model architecture. Instantiating a configuration
with the defaults will yield a similar configuration to that of the
[microsoft/Phi-4-multimodal-instruct](https://huggingface.co/microsoft/Phi-4-multimodal-instruct) architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:

```python
>>> from transformers import Phi4MultimodalModel, Phi4MultimodalConfig

>>> # Initializing a Phi4Multimodal style configuration
>>> configuration = Phi4MultimodalConfig.from_pretrained("microsoft/Phi-4-multimodal-instruct")

>>> # Initializing a model from the configuration
>>> model = Phi4MultimodalModel(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

validate_ropetransformers.Phi4MultimodalConfig.validate_ropehttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/phi4_multimodal/configuration_phi4_multimodal.py#L435[{"name": "ignore_keys", "val": ": set | None = None"}]

Validate the `rope_parameters` configuration.

**Parameters:**

vocab_size (`int`, *optional*, defaults to 200064) : Vocabulary size of the Phi-3 model. Defines the number of different tokens that can be represented by the `inputs_ids` passed when calling [Phi3Model](/docs/transformers/v5.0.0/en/model_doc/phi3#transformers.Phi3Model).

hidden_size (`int`, *optional*, defaults to 3072) : Dimension of the hidden representations.

intermediate_size (`int`, *optional*, defaults to 8192) : Dimension of the MLP representations.

num_hidden_layers (`int`, *optional*, defaults to 32) : Number of hidden layers in the Transformer decoder.

num_attention_heads (`int`, *optional*, defaults to 32) : Number of attention heads for each attention layer in the Transformer decoder.

num_key_value_heads (`int`, *optional*, defaults to 8) : This is the number of key_value heads that should be used to implement Grouped Query Attention. If `num_key_value_heads=num_attention_heads`, the model will use Multi Head Attention (MHA), if `num_key_value_heads=1` the model will use Multi Query Attention (MQA) otherwise GQA is used. When converting a multi-head checkpoint to a GQA checkpoint, each group key and value head should be constructed by meanpooling all the original heads within that group. For more details, check out [this paper](https://huggingface.co/papers/2305.13245). If it is not specified, will default to `num_attention_heads`.

resid_pdrop (`float`, *optional*, defaults to 0.0) : Dropout probability for mlp outputs.

embd_pdrop (`int`, *optional*, defaults to 0.0) : The dropout ratio for the embeddings.

attention_dropout (`float`, *optional*, defaults to 0.0) : The dropout ratio after computing the attention scores.

hidden_act (`str` or `function`, *optional*, defaults to `"silu"`) : The non-linear activation function (function or string) in the decoder.

max_position_embeddings (`int`, *optional*, defaults to 131072) : The maximum sequence length that this model might ever be used with.

initializer_range (`float`, *optional*, defaults to 0.02) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

rms_norm_eps (`float`, *optional*, defaults to 1e-05) : The epsilon value used for the RMSNorm.

use_cache (`bool`, *optional*, defaults to `True`) : Whether or not the model should return the last key/values attentions (not used by all models). Only relevant if `config.is_decoder=True`. Whether to tie weight embeddings or not.

tie_word_embeddings (`bool`, *optional*, defaults to `False`) : Whether to tie weight embeddings

rope_parameters (`RopeParameters`, *optional*) : Dictionary containing the configuration parameters for the RoPE embeddings. The dictionary should contain a value for `rope_theta` and optionally parameters used for scaling in case you want to use RoPE with longer `max_position_embeddings`.

bos_token_id (`int`, *optional*, defaults to 199999) : The id of the "beginning-of-sequence" token.

eos_token_id (`int` or `list[int]`, *optional*, defaults to `[199999, 200020]`) : The id of the "end-of-sequence" token.

pad_token_id (`int`, *optional*, defaults to 199999) : The id of the padding token.

original_max_position_embeddings (`int`, *optional*, defaults to 4096) : The maximum sequence length that this model was trained with. This is used to determine the size of the original RoPE embeddings when using long scaling.

sliding_window (`int`, *optional*) : Sliding window attention window size. If `None`, no sliding window is applied.

vision_config (`Phi4MultimodalVisionConfig` or `dict`, *optional*) : The vision config for the underlying image embedding model. If not provided, will default to the configuration used to instantiate a model similar in architecture as [microsoft/Phi-4-multimodal-instruct](https://huggingface.co/microsoft/Phi-4-multimodal-instruct).

audio_config (`Phi4MultimodalAudioConfig` or `dict`, *optional*) : The audio config for the underlying audio embedding model. If not provided, will default to the configuration used to instantiate a model similar in architecture as [microsoft/Phi-4-multimodal-instruct](https://huggingface.co/microsoft/Phi-4-multimodal-instruct).

## Phi4MultimodalAudioModel[[transformers.Phi4MultimodalAudioModel]]

#### transformers.Phi4MultimodalAudioModel[[transformers.Phi4MultimodalAudioModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/phi4_multimodal/modeling_phi4_multimodal.py#L956)

forward_embeddingstransformers.Phi4MultimodalAudioModel.forward_embeddingshttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/phi4_multimodal/modeling_phi4_multimodal.py#L992[{"name": "hidden_states", "val": ""}, {"name": "masks", "val": ""}]
Forwarding the inputs through the top embedding layers

## Phi4MultimodalVisionModel[[transformers.Phi4MultimodalVisionModel]]

#### transformers.Phi4MultimodalVisionModel[[transformers.Phi4MultimodalVisionModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/phi4_multimodal/modeling_phi4_multimodal.py#L425)

## Phi4MultimodalModel[[transformers.Phi4MultimodalModel]]

#### transformers.Phi4MultimodalModel[[transformers.Phi4MultimodalModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/phi4_multimodal/modeling_phi4_multimodal.py#L1530)

The bare Phi4 Multimodal Model outputting raw hidden-states without any specific head on top.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.Phi4MultimodalModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/phi4_multimodal/modeling_phi4_multimodal.py#L1552[{"name": "input_ids", "val": ": torch.LongTensor | None = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.LongTensor | None = None"}, {"name": "past_key_values", "val": ": transformers.cache_utils.Cache | None = None"}, {"name": "inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "image_pixel_values", "val": ": torch.FloatTensor | None = None"}, {"name": "image_sizes", "val": ": torch.LongTensor | None = None"}, {"name": "image_attention_mask", "val": " = None"}, {"name": "audio_input_features", "val": ": torch.FloatTensor | None = None"}, {"name": "audio_embed_sizes", "val": " = None"}, {"name": "audio_attention_mask", "val": " = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "output_attentions", "val": ": bool | None = None"}, {"name": "output_hidden_states", "val": ": bool | None = None"}, {"name": "cache_position", "val": ": torch.LongTensor | None = None"}, {"name": "**kwargs", "val": ""}]

image_pixel_values (`torch.FloatTensor`, *optional*):
If the input contains images, these correspond to the pixel values after transformations (as returned by
the Processor)
image_sizes (`torch.LongTensor`, *optional*):
If the input contains images, these correspond to size of each image.
image_attention_mask (`torch.LongTensor`, *optional*):
Attention mask for the images.
audio_input_features (`torch.FloatTensor`, *optional*):
If the input contains audio samples, these correspond to the values after transformation (as returned by
the Processor).
audio_embed_sizes (`torch.Tensor`, *optional*):
Size of the audio inputs.
audio_attention_mask (`torch.Tensor, *optional*):
Attention mask for the audio inputs.

**Parameters:**

config ([Phi4MultimodalConfig](/docs/transformers/v5.0.0/en/model_doc/phi4_multimodal#transformers.Phi4MultimodalConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

## Phi4MultimodalForCausalLM[[transformers.Phi4MultimodalForCausalLM]]

#### transformers.Phi4MultimodalForCausalLM[[transformers.Phi4MultimodalForCausalLM]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/phi4_multimodal/modeling_phi4_multimodal.py#L1647)

The Phi4 Multimodal Model for causal language modeling.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.Phi4MultimodalForCausalLM.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/phi4_multimodal/modeling_phi4_multimodal.py#L1661[{"name": "input_ids", "val": ": torch.LongTensor | None = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.LongTensor | None = None"}, {"name": "past_key_values", "val": ": transformers.cache_utils.Cache | None = None"}, {"name": "inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "image_pixel_values", "val": ": torch.FloatTensor | None = None"}, {"name": "image_sizes", "val": ": torch.LongTensor | None = None"}, {"name": "image_attention_mask", "val": " = None"}, {"name": "audio_input_features", "val": ": torch.FloatTensor | None = None"}, {"name": "audio_embed_sizes", "val": " = None"}, {"name": "audio_attention_mask", "val": " = None"}, {"name": "labels", "val": ": torch.LongTensor | None = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "output_attentions", "val": ": bool | None = None"}, {"name": "output_hidden_states", "val": ": bool | None = None"}, {"name": "cache_position", "val": ": torch.LongTensor | None = None"}, {"name": "logits_to_keep", "val": ": int | torch.Tensor = 0"}, {"name": "**kwargs", "val": ""}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
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
- **image_pixel_values** (`torch.FloatTensor`, *optional*) --
  If the input contains images, these correspond to the pixel values after transformations (as returned by
  the Processor)
- **image_sizes** (`torch.LongTensor`, *optional*) --
  If the input contains images, these correspond to size of each image.
- **image_attention_mask** (`torch.LongTensor`, *optional*) --
  Attention mask for the images.
- **audio_input_features** (`torch.FloatTensor`, *optional*) --
  If the input contains audio samples, these correspond to the values after transformation (as returned by
  the Processor).
- **audio_embed_sizes** (`torch.Tensor`, *optional*) --
  Size of the audio inputs.
- **audio_attention_mask** (`torch.Tensor, *optional*) --
  Attention mask for the audio inputs.
- **labels** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Labels for computing the masked language modeling loss. Indices should either be in `[0, ...,
  config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored
  (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.
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
  the complete sequence length.
- **logits_to_keep** (`Union[int, torch.Tensor]`, *optional*, defaults to `0`) --
  If an `int`, compute logits for the last `logits_to_keep` tokens. If `0`, calculate logits for all
  `input_ids` (special case). Only last token logits are needed for generation, and calculating them only for that
  token can save memory, which becomes pretty significant for long sequences or large vocabulary size.
  If a `torch.Tensor`, must be 1D corresponding to the indices to keep in the sequence length dimension.
  This is useful when using packed tensor format (single dimension for batch and sequence length).0[transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or `tuple(torch.FloatTensor)`A [transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Phi4MultimodalConfig](/docs/transformers/v5.0.0/en/model_doc/phi4_multimodal#transformers.Phi4MultimodalConfig)) and inputs.

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
The [Phi4MultimodalForCausalLM](/docs/transformers/v5.0.0/en/model_doc/phi4_multimodal#transformers.Phi4MultimodalForCausalLM) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Example:
```python
>>> from transformers import AutoTokenizer, Phi4MultimodalForCausalLM
>>> model = Phi4MultimodalForCausalLM.from_pretrained("TBA")
>>> tokenizer = AutoTokenizer.from_pretrained("TBA")
>>> prompt = "This is an example script ."
>>> inputs = tokenizer(prompt, return_tensors="pt")
>>> # Generate
>>> generate_ids = model.generate(inputs.input_ids, max_length=30)
>>> tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
'This is an example script .\n Certainly! Below is a sample script that demonstrates a simple task, such as calculating the sum'
```

**Parameters:**

config ([Phi4MultimodalForCausalLM](/docs/transformers/v5.0.0/en/model_doc/phi4_multimodal#transformers.Phi4MultimodalForCausalLM)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

`[transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.CausalLMOutputWithPast](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.CausalLMOutputWithPast) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([Phi4MultimodalConfig](/docs/transformers/v5.0.0/en/model_doc/phi4_multimodal#transformers.Phi4MultimodalConfig)) and inputs.

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

