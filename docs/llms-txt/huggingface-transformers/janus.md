# Source: https://huggingface.co/docs/transformers/v5.0.0rc1/model_doc/janus.md

# Janus

## Overview

The Janus Model was originally proposed in [Janus: Decoupling Visual Encoding for Unified Multimodal Understanding and Generation](https://huggingface.co/papers/2410.13848) by DeepSeek AI team and later refined in [Janus-Pro: Unified Multimodal Understanding and Generation with Data and Model Scaling](https://huggingface.co/papers/2501.17811). Janus is a vision-language model that can generate both image and text output, it can also take both images and text as input.

> [!NOTE]
> The model doesn't generate both images and text in an interleaved format. The user has to pass a parameter indicating whether to generate text or image.

The abstract from the original paper is the following:

*In this paper, we introduce Janus, an autoregressive framework that unifies multimodal understanding and generation. Prior research often relies on a single visual encoder for both tasks, such as Chameleon. However, due to the differing levels of information granularity required by multimodal understanding and generation, this approach can lead to suboptimal performance, particularly in multimodal understanding. To address this issue, we decouple visual encoding into separate pathways, while still leveraging a single, unified transformer architecture for processing. The decoupling not only alleviates the conflict between the visual encoder's roles in understanding and generation, but also enhances the framework's flexibility. For instance, both the multimodal understanding and generation components can independently select their most suitable encoding methods. Experiments show that Janus surpasses previous unified model and matches or exceeds the performance of task-specific models. The simplicity, high flexibility, and effectiveness of Janus make it a strong candidate for next-generation unified multimodal models.*

The abstract from the aforementioned `Janus-Pro` paper, released afterwards, is the following:

*In this work, we introduce Janus-Pro, an advanced version of the previous work Janus. Specifically, Janus-Pro incorporates (1) an optimized training strate (2) expanded training data, and (3) scaling to larger model size. With these improvements, Janus-Pro achieves significant advancements in both multimodal understanding and text-to-image instruction-following capabilities, while also enhancing the stability of text-to-image generation. We hope this work will inspire further exploration in the field. Code and models are publicly available.*

This model was contributed by [Yaswanth Gali](https://huggingface.co/yaswanthgali) and [Hugo Silva](https://huggingface.co/hugosilva664).
The original code can be found [here](https://github.com/deepseek-ai/Janus).

## Usage Example

### Single image inference

Here is the example of visual understanding with a single image.

> [!NOTE]
> Note that the model has been trained with a specific prompt format for chatting. Use `processor.apply_chat_template(my_conversation_dict)` to correctly format your prompts.

```python
import torch
from PIL import Image
import requests

from transformers import JanusForConditionalGeneration, JanusProcessor

model_id = "deepseek-community/Janus-Pro-1B"
# Prepare Input for generation.
messages = [
    {
        "role": "user",
        "content": [
            {'type':'image', 'url': 'http://images.cocodataset.org/val2017/000000039769.jpg'},
            {'type':"text", "text":"What do you see in this image?."}
        ]
    },
]

# Set generation mode to `text` to perform text generation.
processor = JanusProcessor.from_pretrained(model_id)
model = JanusForConditionalGeneration.from_pretrained(model_id,     
        dtype=torch.bfloat16,
        device_map="auto")

inputs = processor.apply_chat_template(
    messages,
    add_generation_prompt=True,
    generation_mode="text",
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
).to(model.device, dtype=torch.bfloat16)

output = model.generate(**inputs, max_new_tokens=40,generation_mode='text',do_sample=True)
text = processor.decode(output[0], skip_special_tokens=True)
print(text)
```

### Multi image inference

Janus can perform inference with multiple images as input, where images can belong to the same prompt or different prompts in batched inference, where the model processes many conversations in parallel. Here is how you can do it:

```python
import torch
from PIL import Image
import requests

from transformers import JanusForConditionalGeneration, JanusProcessor

model_id = "deepseek-community/Janus-Pro-1B"

image_urls = [
    "http://images.cocodataset.org/val2017/000000039769.jpg",
    "https://www.ilankelman.org/stopsigns/australia.jpg",
    "https://huggingface.co/microsoft/kosmos-2-patch14-224/resolve/main/snowman.jpg"
]

messages = [
    [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What’s the difference between"},
                {"type": "image", "url": image_urls[0]},
                {"type": "text", "text": " and "},
                {"type": "image", "url": image_urls[1]}
            ]
        }
    ],
    [
        {
            "role": "user",
            "content": [
                {"type": "image", "url": image_urls[2]},
                {"type": "text", "text": "What do you see in this image?"}
            ]
        }
    ]
]

# Load model and processor
processor = JanusProcessor.from_pretrained(model_id)
model = JanusForConditionalGeneration.from_pretrained(
    model_id, dtype=torch.bfloat16, device_map="auto"
)

inputs = processor.apply_chat_template(
    messages,
    add_generation_prompt=True,
    generation_mode="text",
    tokenize=True,
    padding=True,
    return_dict=True,
    return_tensors="pt"
).to(model.device, dtype=torch.bfloat16)

# Generate response
output = model.generate(**inputs, max_new_tokens=40, generation_mode='text', do_sample=False)
text = processor.batch_decode(output, skip_special_tokens=True)
print(text)
```

## Text to Image generation

Janus can also generate images given a prompt.

```python
import torch
from transformers import JanusForConditionalGeneration, JanusProcessor

# Set generation mode to `image` to prepare inputs for image generation..

model_id = "deepseek-community/Janus-Pro-1B"
processor = JanusProcessor.from_pretrained(model_id)
model = JanusForConditionalGeneration.from_pretrained(model_id,
        dtype=torch.bfloat16,
        device_map="auto")

messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "A dog running under the rain."},
        ],
     }
]

prompt = processor.apply_chat_template(messages, add_generation_prompt=True)
inputs = processor(text=prompt,generation_mode="image",return_tensors="pt").to(model.device, dtype=torch.bfloat16)

# Set num_return_sequence parameter to generate multiple images per prompt.
model.generation_config.num_return_sequences = 2
outputs = model.generate(**inputs,
                         generation_mode="image",
                         do_sample=True,
                         use_cache=True,
                         )
# Perform post-processing on the generated token ids.
decoded_image = model.decode_image_tokens(outputs)
images = processor.postprocess(list(decoded_image.float()),return_tensors="PIL.Image.Image")
# Save the image
for i, image in enumerate(images['pixel_values']):
    image.save(f"result{i}.png")
```

## JanusConfig[[transformers.JanusConfig]]

#### transformers.JanusConfig[[transformers.JanusConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/janus/configuration_janus.py#L212)

This is the configuration class to store the configuration of a [JanusModel](/docs/transformers/v5.0.0rc1/en/model_doc/janus#transformers.JanusModel). It is used to instantiate an
Janus model according to the specified arguments, defining the model architecture. Instantiating a configuration
with the defaults will yield a similar configuration to that of the Janus-1B or Janus-7B models.

e.g. [deepseek-community/Janus-Pro-1B](https://huggingface.co/deepseek-community/Janus-Pro-1B) or
[deepseek-community/Janus-Pro-7B](https://huggingface.co/deepseek-community/Janus-Pro-7B)

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:

```python
>>> from transformers import JanusForConditionalGeneration, JanusConfig, JanusVisionConfig, JanusVQVAEConfig, LlamaConfig

>>> # Initializing a Janus vision config
>>> vision_config = JanusVisionConfig()

>>> # Initializing a Llama config
>>> text_config = LlamaConfig()

>>> # Initializing a VQ config
>>> vq_config = JanusVQVAEConfig()

>>> # Initializing a Janus Pro 1B style configuration
>>> configuration = JanusConfig(vision_config=vision_config, text_config=text_config, vq_config=vq_config)

>>> # Initializing a model from the Janus Pro 1B style configuration
>>> model = JanusForConditionalGeneration(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

text_config (`Union[AutoConfig, dict]`, *optional*, defaults to `LlamaConfig`) : The config object or dictionary of the text backbone.

vision_config (`Union[AutoConfig, dict]`,  *optional*, defaults to `JanusVisionConfig`) : The config object or dictionary of the vision backbone.

vq_config (`Union[AutoConfig, dict]`,  *optional*, defaults to `JanusVQVAEConfig`) : The config object or dictionary of the VQVAE backbone.

image_token_id (`int`, *optional*, defaults to 100581) : Token index of a placeholder image token.

## JanusVisionConfig[[transformers.JanusVisionConfig]]

#### transformers.JanusVisionConfig[[transformers.JanusVisionConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/janus/configuration_janus.py#L30)

This is the configuration class to store the configuration of a [JanusVisionModel](/docs/transformers/v5.0.0rc1/en/model_doc/janus#transformers.JanusVisionModel). It is used to instantiate a
`JanusVisionModel` according to the specified arguments, defining the model architecture.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

**Parameters:**

hidden_size (`int`, *optional*, defaults to 1024) : Dimensionality of the encoder layers and the pooler layer.

num_hidden_layers (`int`, *optional*, defaults to 24) : Number of hidden layers in the Transformer encoder.

num_attention_heads (`int`, *optional*, defaults to 16) : Number of attention heads for each attention layer in the Transformer encoder.

num_channels (`int`, *optional*, defaults to 3) : The number of input channels.

patch_size (`int`, *optional*, defaults to 16) : The size (resolution) of each patch.

image_size (`int`, *optional*, defaults to 384) : The size (resolution) of each image.

attention_dropout (`float`, *optional*, defaults to 0.0) : Dropout probability for attention weights.

layer_norm_eps (`float`, *optional*, defaults to 1e-06) : The epsilon used by the layer normalization layers.

hidden_act (`str` or `function`, *optional*, defaults to `"gelu"`) : The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`, `"relu"`, `"selu"`, and `"gelu_new"` are supported.

mlp_ratio (`float`, *optional*, defaults to 4.0) : Ratio of MLP hidden dimensionality to embedding dimensionality.

attention_bias (`bool`, *optional*, defaults to `True`) : Whether to add a bias to the queries, keys, and values in the attention layers.

hidden_dropout_rate (`float`, *optional*, defaults to 0.0) : The dropout probability for fully connected layers in the encoder.

projection_dim (`int`, *optional*, defaults to 2048) : Dimensionality of the MLP projection head.

projection_dropout (`float`, *optional*, defaults to 0.0) : Dropout probability for the projection layer.

use_qk_norm (`bool`, *optional*, defaults to `False`) : Whether to normalize the query and key matrices.

initializer_range (`float`, *optional*, defaults to 0.02) : The standard deviation of the truncated normal initializer for initializing all weight matrices.

depth (`int`, *optional*, defaults to 2) : Number of hidden layers in the aligner module.

num_image_tokens (`int`, *optional*, defaults to 576) : Number of image tokens.

## JanusVQVAEConfig[[transformers.JanusVQVAEConfig]]

#### transformers.JanusVQVAEConfig[[transformers.JanusVQVAEConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/janus/configuration_janus.py#L125)

This is the configuration class to store the configuration of a `JanusVQVAEModel`. It is used to instantiate a
`JanusVQVAEModel` according to the specified arguments, defining the model architecture.
Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) for more information. Instantiating a
configuration with the defaults will yield a similar configuration to the VQModel of the
[deepseek-community/Janus-Pro-1B](https://huggingface.co/deepseek-community/Janus-Pro-1B).

**Parameters:**

embed_dim (`int`, *optional*, defaults to 8) : Dimensionality of each embedding vector.

num_embeddings (`int`, *optional*, defaults to 16384) : Number of codebook embeddings.

double_latent (`bool`, *optional*, defaults to `False`) : Whether to use double z channels.

latent_channels (`int`, *optional*, defaults to 256) : Number of channels for the latent space.

num_patches (`int`, *optional*, defaults to 32) : Num of patches the input images can be divided into.

in_channels (`int`, *optional*, defaults to 3) : Number of input channels.

out_channels (`int`, *optional*, defaults to 3) : Number of out channels.

base_channels (`int`, *optional*, defaults to 128) : Base channel count.

channel_multiplier (`list[int]`, *optional*, defaults to `[1, 1, 2, 2, 4]`) : Channel multipliers for each resolution.

num_res_blocks (`int`, *optional*, defaults to 2) : Number of residual blocks.

dropout (`float`, *optional*, defaults to 0.0) : Dropout rate.

initializer_range (`float`, *optional*, defaults to 0.02) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

projection_dim (`int`, *optional*, defaults to 2048) : Dimensionality of the MLP projection head.

num_hidden_layers (`int`, *optional*, defaults to 2) : Number of hidden layers in VAVAE MLP Connecter module.

hidden_act (`str` or `Callable`, *optional*, defaults to `"gelu"`) : The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`, `"relu"`, `"silu"` and `"gelu_new"` are supported.

image_token_embed_dim (`int`, *optional*, defaults to 2048) : Dimension of image embeddings. It should be same as the dimensionality of text embeddings.

## JanusProcessor[[transformers.JanusProcessor]]

#### transformers.JanusProcessor[[transformers.JanusProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/janus/processing_janus.py#L49)

Constructs a Janus processor which wraps a Janus Image Processor and a Llama tokenizer into a single processor.

[JanusProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/janus#transformers.JanusProcessor) offers all the functionalities of [JanusImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/janus#transformers.JanusImageProcessor) and [LlamaTokenizerFast](/docs/transformers/v5.0.0rc1/en/model_doc/llama2#transformers.LlamaTokenizer). See the
`__call__()` and [decode()](/docs/transformers/v5.0.0rc1/en/main_classes/processors#transformers.ProcessorMixin.decode) for more information.

post_process_multimodal_outputtransformers.JanusProcessor.post_process_multimodal_outputhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/janus/processing_janus.py#L155[{"name": "generated_outputs", "val": ""}, {"name": "skip_special_tokens", "val": " = True"}, {"name": "generation_mode", "val": " = None"}, {"name": "**kwargs", "val": ""}]- **generated_outputs** (`torch.Tensor` or `np.ndarray`) --
  The output of the model `generate` function. The output is expected to be a tensor of shape `(batch_size, sequence_length)`
  or `(sequence_length,)`.
- **skip_special_tokens** (`bool`, *optional*, defaults to `True`) --
  Whether or not to remove special tokens in the output. Argument passed to the tokenizer's `batch_decode` method.
- **generation_mode** (`str`, *optional*) --
  Generation mode indicated which modality to output and can be one of `["text", "image", "audio"]`.
- ****kwargs** --
  Additional arguments to be passed to the tokenizer's `batch_decode method`.0`list[Union[str, PIL.Image.Image]]`The decoded text or generated image.

Post-process the output of a multimodal model to return the requested modality output.
If the model cannot generated the requested modality, an error will be raised.

**Parameters:**

image_processor ([JanusImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/janus#transformers.JanusImageProcessor)) : The image processor is a required input.

tokenizer ([LlamaTokenizerFast](/docs/transformers/v5.0.0rc1/en/model_doc/llama2#transformers.LlamaTokenizer)) : The tokenizer is a required input.

chat_template (`str`, *optional*) : A Jinja template which will be used to convert lists of messages in a chat into a tokenizable string.

use_default_system_prompt (`str`, *optional*, defaults to `False`) : Use default system prompt for Text Generation.

**Returns:**

``list[Union[str, PIL.Image.Image]]``

The decoded text or generated image.
#### postprocess[[transformers.JanusProcessor.postprocess]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/janus/processing_janus.py#L148)

Forwards all arguments to the image processor's `postprocess` method.
Refer to the original method's docstring for more details.

## JanusImageProcessor[[transformers.JanusImageProcessor]]

#### transformers.JanusImageProcessor[[transformers.JanusImageProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/janus/image_processing_janus.py#L64)

Constructs a JANUS image processor.

pad_to_squaretransformers.JanusImageProcessor.pad_to_squarehttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/janus/image_processing_janus.py#L360[{"name": "image", "val": ": ndarray"}, {"name": "background_color", "val": ": typing.Union[int, tuple[int, int, int]] = 0"}, {"name": "data_format", "val": ": typing.Union[str, transformers.image_utils.ChannelDimension, NoneType] = None"}, {"name": "input_data_format", "val": ": typing.Union[str, transformers.image_utils.ChannelDimension, NoneType] = None"}]- **image** (`np.ndarray`) --
  The image to pad.
- **background_color** (`int` or `tuple[int, int, int]`, *optional*, defaults to 0) --
  The color to use for the padding. Can be an integer for single channel or a
  tuple of integers representing for multi-channel images. If passed as integer
  in multi-channel mode, it will default to `0` in subsequent channels.
- **data_format** (`str` or `ChannelDimension`, *optional*) --
  The channel dimension format for the output image. Can be one of:
  - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
  - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.
  If unset, will use same as the input image.
- **input_data_format** (`str` or `ChannelDimension`, *optional*) --
  The channel dimension format for the input image. Can be one of:
  - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
  - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.0`np.ndarray`The padded image.

Pads an image to a square based on the longest edge.

**Parameters:**

do_resize (`bool`, *optional*, defaults to `True`) : Whether to resize the image's (height, width) dimensions to the specified `size`. Can be overridden by the `do_resize` parameter in the `preprocess` method.

size (`dict`, *optional*, defaults to `{"height" : 384, "width": 384}`): Size of the output image after resizing. Can be overridden by the `size` parameter in the `preprocess` method.

min_size (`int`, *optional*, defaults to 14) : The minimum allowed size for the resized image. Ensures that neither the height nor width falls below this value after resizing.

resample (`PILImageResampling`, *optional*, defaults to `Resampling.BICUBIC`) : Resampling filter to use if resizing the image. Only has an effect if `do_resize` is set to `True`. Can be overridden by the `resample` parameter in the `preprocess` method.

do_rescale (`bool`, *optional*, defaults to `True`) : Whether to rescale the image by the specified scale `rescale_factor`. Can be overridden by the `do_rescale` parameter in the `preprocess` method.

rescale_factor (`int` or `float`, *optional*, defaults to `1/255`) : Scale factor to use if rescaling the image. Only has an effect if `do_rescale` is set to `True`. Can be overridden by the `rescale_factor` parameter in the `preprocess` method.

do_normalize (`bool`, *optional*, defaults to `True`) : Whether to normalize the image. Can be overridden by the `do_normalize` parameter in the `preprocess` method. Can be overridden by the `do_normalize` parameter in the `preprocess` method.

image_mean (`float` or `list[float]`, *optional*, defaults to `IMAGENET_STANDARD_MEAN`) : Mean to use if normalizing the image. This is a float or list of floats the length of the number of channels in the image. Can be overridden by the `image_mean` parameter in the `preprocess` method. Can be overridden by the `image_mean` parameter in the `preprocess` method.

image_std (`float` or `list[float]`, *optional*, defaults to `IMAGENET_STANDARD_STD`) : Standard deviation to use if normalizing the image. This is a float or list of floats the length of the number of channels in the image. Can be overridden by the `image_std` parameter in the `preprocess` method. Can be overridden by the `image_std` parameter in the `preprocess` method.

do_convert_rgb (`bool`, *optional*, defaults to `True`) : Whether to convert the image to RGB.

do_pad (`bool`, *optional*, defaults to `True`) : Whether to pad the image to square or not.

**Returns:**

``np.ndarray``

The padded image.
#### postprocess[[transformers.JanusImageProcessor.postprocess]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/janus/image_processing_janus.py#L434)

Applies post-processing to the decoded image tokens by reversing transformations applied during preprocessing.
#### preprocess[[transformers.JanusImageProcessor.preprocess]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/janus/image_processing_janus.py#L209)

Preprocess an image or batch of images.

**Parameters:**

images (`ImageInput`) : Image to preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If passing in images with pixel values between 0 and 1, set `do_rescale=False`.

do_resize (`bool`, *optional*, defaults to `self.do_resize`) : Whether to resize the image.

size (`dict[str, int]`, *optional*, defaults to `self.size`) : Controls the size of the image after `resize`. The shortest edge of the image is resized to `size["shortest_edge"]` whilst preserving the aspect ratio. If the longest edge of this resized image is > `int(size["shortest_edge"] * (1333 / 800))`, then the image is resized again to make the longest edge equal to `int(size["shortest_edge"] * (1333 / 800))`.

resample (`PILImageResampling`, *optional*, defaults to `self.resample`) : Resampling filter to use if resizing the image. Only has an effect if `do_resize` is set to `True`.

do_rescale (`bool`, *optional*, defaults to `self.do_rescale`) : Whether to rescale the image values between [0 - 1].

rescale_factor (`float`, *optional*, defaults to `self.rescale_factor`) : Rescale factor to rescale the image by if `do_rescale` is set to `True`.

do_normalize (`bool`, *optional*, defaults to `self.do_normalize`) : Whether to normalize the image.

image_mean (`float` or `list[float]`, *optional*, defaults to `self.image_mean`) : Image mean to normalize the image by if `do_normalize` is set to `True`.

image_std (`float` or `list[float]`, *optional*, defaults to `self.image_std`) : Image standard deviation to normalize the image by if `do_normalize` is set to `True`.

do_convert_rgb (`bool`, *optional*, defaults to `self.do_convert_rgb`) : Whether to convert the image to RGB.

background_color (`tuple[int, int, int]`) : The background color to use for the padding.

do_pad (`bool`, *optional*, defaults to `self.do_pad`) : Whether to pad the image to square or not.

return_tensors (`str` or `TensorType`, *optional*) : The type of tensors to return. Can be one of: - Unset: Return a list of `np.ndarray`. - `TensorType.PYTORCH` or `'pt'`: Return a batch of type `torch.Tensor`. - `TensorType.NUMPY` or `'np'`: Return a batch of type `np.ndarray`.

data_format (`ChannelDimension` or `str`, *optional*, defaults to `ChannelDimension.FIRST`) : The channel dimension format for the output image. Can be one of: - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format. - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format. - Unset: Use the channel dimension format of the input image.

input_data_format (`ChannelDimension` or `str`, *optional*) : The channel dimension format for the input image. If unset, the channel dimension format is inferred from the input image. Can be one of: - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format. - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format. - `"none"` or `ChannelDimension.NONE`: image in (height, width) format.
#### resize[[transformers.JanusImageProcessor.resize]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/janus/image_processing_janus.py#L144)

Resize an image to dynamically calculated size.

**Parameters:**

image (`np.ndarray`) : Image to resize.

size (`dict[str, int]` or `int`) : The size to resize the image to. If a dictionary, it should have the keys `"height"` and `"width"`.

resample (`PILImageResampling`, *optional*, defaults to `PILImageResampling.BICUBIC`) : `PILImageResampling` filter to use when resizing the image e.g. `PILImageResampling.BICUBIC`.

data_format (`ChannelDimension` or `str`, *optional*) : The channel dimension format for the output image. If unset, the channel dimension format of the input image is used. Can be one of: - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format. - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format. - `None`: will be inferred from input

input_data_format (`ChannelDimension` or `str`, *optional*) : The channel dimension format for the input image. If unset, the channel dimension format is inferred from the input image. Can be one of: - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format. - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format. - `"none"` or `ChannelDimension.NONE`: image in (height, width) format.

**Returns:**

``np.ndarray``

The resized image.
#### unnormalize[[transformers.JanusImageProcessor.unnormalize]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/janus/image_processing_janus.py#L485)

Unnormalizes `image` using the mean and standard deviation specified by `mean` and `std`.
image = (image * image_std) + image_mean

**Parameters:**

image (`torch.Tensor` of shape `(batch_size, num_channels, image_size, image_size)` or `(num_channels, image_size, image_size)`) : Batch of pixel values to postprocess.

image_mean (`float` or `Iterable[float]`) : The mean to use for unnormalization.

image_std (`float` or `Iterable[float]`) : The standard deviation to use for unnormalization.

input_data_format (`ChannelDimension` or `str`, *optional*) : The channel dimension format for the input image. If unset, the channel dimension format is inferred from the input image. Can be one of: - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format. - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format. - `"none"` or `ChannelDimension.NONE`: image in (height, width) format.

## JanusImageProcessorFast[[transformers.JanusImageProcessorFast]]

#### transformers.JanusImageProcessorFast[[transformers.JanusImageProcessorFast]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/janus/image_processing_janus_fast.py#L44)

Constructs a fast Janus image processor.

pad_to_squaretransformers.JanusImageProcessorFast.pad_to_squarehttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/janus/image_processing_janus_fast.py#L91[{"name": "images", "val": ": torch.Tensor"}, {"name": "background_color", "val": ": typing.Union[int, tuple[int, int, int]] = 0"}]- **images** (`torch.Tensor`) --
  The images to pad.
- **background_color** (`int` or `tuple[int, int, int]`, *optional*, defaults to 0) --
  The color to use for the padding. Can be an integer for single channel or a
  tuple of integers representing for multi-channel images. If passed as integer
  in multi-channel mode, it will default to `0` in subsequent channels.0`torch.Tensor`The padded images.

Pads an image to a square based on the longest edge.

**Parameters:**

images (`torch.Tensor`) : The images to pad.

background_color (`int` or `tuple[int, int, int]`, *optional*, defaults to 0) : The color to use for the padding. Can be an integer for single channel or a tuple of integers representing for multi-channel images. If passed as integer in multi-channel mode, it will default to `0` in subsequent channels.

**Returns:**

``torch.Tensor``

The padded images.

## JanusVisionModel[[transformers.JanusVisionModel]]

#### transformers.JanusVisionModel[[transformers.JanusVisionModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/janus/modeling_janus.py#L546)

The bare Janus Model outputting raw hidden-states without any specific head on top.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.JanusVisionModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/janus/modeling_janus.py#L566[{"name": "pixel_values", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "interpolate_pos_encoding", "val": ": bool = False"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **pixel_values** (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`, *optional*) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [JanusImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/janus#transformers.JanusImageProcessor). See [JanusImageProcessor.__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details ([JanusProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/janus#transformers.JanusProcessor) uses
  [JanusImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/janus#transformers.JanusImageProcessor) for processing images).
- **interpolate_pos_encoding** (`bool`, defaults to `False`) --
  Whether to interpolate the pre-trained position encodings.0[transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)`A [transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([JanusConfig](/docs/transformers/v5.0.0rc1/en/model_doc/janus#transformers.JanusConfig)) and inputs.

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
The [JanusVisionModel](/docs/transformers/v5.0.0rc1/en/model_doc/janus#transformers.JanusVisionModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

**Parameters:**

config ([JanusVisionConfig](/docs/transformers/v5.0.0rc1/en/model_doc/janus#transformers.JanusVisionConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

`[transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([JanusConfig](/docs/transformers/v5.0.0rc1/en/model_doc/janus#transformers.JanusConfig)) and inputs.

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

## JanusVQVAE[[transformers.JanusVQVAE]]

#### transformers.JanusVQVAE[[transformers.JanusVQVAE]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/janus/modeling_janus.py#L957)

The VQ-VAE model used in Janus for encoding/decoding images into discrete tokens.
This model follows the "Make-a-scene: Scene-based text-to-image generation with human priors" paper from
[ Oran Gafni, Adam Polyak, Oron Ashual, Shelly Sheynin, Devi Parikh, and Yaniv
Taigman](https://huggingface.co/papers/2203.13131).

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.JanusVQVAE.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/janus/modeling_janus.py#L1005[{"name": "pixel_values", "val": ": FloatTensor"}, {"name": "**kwargs", "val": ""}]- **pixel_values** (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [JanusImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/janus#transformers.JanusImageProcessor). See [JanusImageProcessor.__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details ([JanusProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/janus#transformers.JanusProcessor) uses
  [JanusImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/janus#transformers.JanusImageProcessor) for processing images).0`tuple[torch.FloatTensor, torch.FloatTensor]`
The [JanusVQVAE](/docs/transformers/v5.0.0rc1/en/model_doc/janus#transformers.JanusVQVAE) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

**Parameters:**

config ([JanusVQVAEConfig](/docs/transformers/v5.0.0rc1/en/model_doc/janus#transformers.JanusVQVAEConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

`tuple[torch.FloatTensor, torch.FloatTensor]`

## JanusModel[[transformers.JanusModel]]

#### transformers.JanusModel[[transformers.JanusModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/janus/modeling_janus.py#L1058)

The Janus model which consists of a siglip vision backbone, a Llama language model and a VQ model.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.JanusModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/janus/modeling_janus.py#L1115[{"name": "input_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "pixel_values", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "attention_mask", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "position_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "past_key_values", "val": ": typing.Optional[transformers.cache_utils.Cache] = None"}, {"name": "cache_position", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "inputs_embeds", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "use_cache", "val": ": typing.Optional[bool] = None"}, {"name": "logits_to_keep", "val": ": typing.Union[int, torch.Tensor] = 0"}, {"name": "**kwargs", "val": ""}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **pixel_values** (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`, *optional*) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [JanusImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/janus#transformers.JanusImageProcessor). See [JanusImageProcessor.__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details ([JanusProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/janus#transformers.JanusProcessor) uses
  [JanusImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/janus#transformers.JanusImageProcessor) for processing images).
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
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.
- **inputs_embeds** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) --
  Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation. This
  is useful if you want more control over how to convert `input_ids` indices into associated vectors than the
  model's internal embedding lookup matrix.
- **use_cache** (`bool`, *optional*) --
  If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
  `past_key_values`).
- **logits_to_keep** (`Union[int, torch.Tensor]`, defaults to `0`) --
  If an `int`, compute logits for the last `logits_to_keep` tokens. If `0`, calculate logits for all
  `input_ids` (special case). Only last token logits are needed for generation, and calculating them only for that
  token can save memory, which becomes pretty significant for long sequences or large vocabulary size.
  If a `torch.Tensor`, must be 1D corresponding to the indices to keep in the sequence length dimension.
  This is useful when using packed tensor format (single dimension for batch and sequence length).0
The [JanusModel](/docs/transformers/v5.0.0rc1/en/model_doc/janus#transformers.JanusModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

**Parameters:**

config ([JanusConfig](/docs/transformers/v5.0.0rc1/en/model_doc/janus#transformers.JanusConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

## JanusForConditionalGeneration[[transformers.JanusForConditionalGeneration]]

#### transformers.JanusForConditionalGeneration[[transformers.JanusForConditionalGeneration]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/janus/modeling_janus.py#L1166)

forwardtransformers.JanusForConditionalGeneration.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/janus/modeling_janus.py#L1191[{"name": "input_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "pixel_values", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "attention_mask", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "position_ids", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "past_key_values", "val": ": typing.Optional[transformers.cache_utils.Cache] = None"}, {"name": "cache_position", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "inputs_embeds", "val": ": typing.Optional[torch.FloatTensor] = None"}, {"name": "labels", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "use_cache", "val": ": typing.Optional[bool] = None"}, {"name": "logits_to_keep", "val": ": typing.Union[int, torch.Tensor] = 0"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **pixel_values** (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`, *optional*) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [JanusImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/janus#transformers.JanusImageProcessor). See [JanusImageProcessor.__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details ([JanusProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/janus#transformers.JanusProcessor) uses
  [JanusImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/janus#transformers.JanusImageProcessor) for processing images).
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
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.
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
- **logits_to_keep** (`Union[int, torch.Tensor]`, defaults to `0`) --
  If an `int`, compute logits for the last `logits_to_keep` tokens. If `0`, calculate logits for all
  `input_ids` (special case). Only last token logits are needed for generation, and calculating them only for that
  token can save memory, which becomes pretty significant for long sequences or large vocabulary size.
  If a `torch.Tensor`, must be 1D corresponding to the indices to keep in the sequence length dimension.
  This is useful when using packed tensor format (single dimension for batch and sequence length).0
The [JanusForConditionalGeneration](/docs/transformers/v5.0.0rc1/en/model_doc/janus#transformers.JanusForConditionalGeneration) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Example:

```python
>>> from PIL import Image
>>> import requests
>>> from transformers import AutoProcessor, JanusForConditionalGeneration

>>> model = JanusForConditionalGeneration.from_pretrained("deepseek-community/Janus-Pro-1B")
>>> processor = AutoProcessor.from_pretrained("deepseek-community/Janus-Pro-1B")

>>> messages = [
...     {
...         "role": "user", "content": [
...             {"type": "image", "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/pipeline-cat-chonk.jpeg"},
...             {"type": "text", "text": "Where is the cat standing?"},
...         ]
...     },
... ]

>>> inputs = processor.apply_chat_template(
...     messages,
...     tokenize=True,
...     return_dict=True,
...     return_tensors="pt",
...     add_generation_prompt=True
... )
>>> # Generate
>>> generate_ids = model.generate(**inputs)
>>> processor.batch_decode(generate_ids, skip_special_tokens=True)[0]
```

**Parameters:**

input_ids (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) : Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.  [What are input IDs?](../glossary#input-ids)

pixel_values (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`, *optional*) : The tensors corresponding to the input images. Pixel values can be obtained using [JanusImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/janus#transformers.JanusImageProcessor). See [JanusImageProcessor.__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details ([JanusProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/janus#transformers.JanusProcessor) uses [JanusImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/janus#transformers.JanusImageProcessor) for processing images).

attention_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) : Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:  - 1 for tokens that are **not masked**, - 0 for tokens that are **masked**.  [What are attention masks?](../glossary#attention-mask)

position_ids (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) : Indices of positions of each input sequence tokens in the position embeddings. Selected in the range `[0, config.n_positions - 1]`.  [What are position IDs?](../glossary#position-ids)

past_key_values (`~cache_utils.Cache`, *optional*) : Pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention blocks) that can be used to speed up sequential decoding. This typically consists in the `past_key_values` returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.  Only [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance is allowed as input, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache). If no `past_key_values` are passed, [DynamicCache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.DynamicCache) will be initialized by default.  The model will output the same cache format that is fed as input.  If `past_key_values` are used, the user is expected to input only unprocessed `input_ids` (those that don't have their past key value states given to this model) of shape `(batch_size, unprocessed_length)` instead of all `input_ids` of shape `(batch_size, sequence_length)`.

cache_position (`torch.LongTensor` of shape `(sequence_length)`, *optional*) : Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`, this tensor is not affected by padding. It is used to update the cache in the correct position and to infer the complete sequence length.

inputs_embeds (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) : Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation. This is useful if you want more control over how to convert `input_ids` indices into associated vectors than the model's internal embedding lookup matrix.

labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) : Labels for computing the masked language modeling loss. Indices should either be in `[0, ..., config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.

use_cache (`bool`, *optional*) : If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see `past_key_values`).

logits_to_keep (`Union[int, torch.Tensor]`, defaults to `0`) : If an `int`, compute logits for the last `logits_to_keep` tokens. If `0`, calculate logits for all `input_ids` (special case). Only last token logits are needed for generation, and calculating them only for that token can save memory, which becomes pretty significant for long sequences or large vocabulary size. If a `torch.Tensor`, must be 1D corresponding to the indices to keep in the sequence length dimension. This is useful when using packed tensor format (single dimension for batch and sequence length).

