# Source: https://huggingface.co/docs/transformers/v5.0.0/model_doc/llava_onevision.md

# LLaVA-OneVision

## Overview

The LLaVA-OneVision model was proposed in [LLaVA-OneVision: Easy Visual Task Transfer](https://huggingface.co/papers/2408.03326) by 

 LLaVA-OneVision architecture. Taken from the original paper. 

Tips:

- We advise users to use `padding_side="left"` when computing batched generation as it leads to more accurate results. Simply make sure to call `processor.tokenizer.padding_side = "left"` before generating.

- Llava-OneVision uses different number of patches for images and thus has to pad the inputs inside modeling code, aside from the padding done when processing the inputs. The default setting is "left-padding" if model is in `eval()` mode, otherwise "right-padding".

### Formatting Prompts with Chat Templates  

Each **checkpoint** is trained with a specific prompt format, depending on the underlying large language model backbone. To ensure correct formatting, use the processor’s `apply_chat_template` method.  

**Important:**  

- You must construct a conversation history — passing a plain string won't work.  
- Each message should be a dictionary with `"role"` and `"content"` keys.  
- The `"content"` should be a list of dictionaries for different modalities like `"text"` and `"image"`.  

Here’s an example of how to structure your input.
We will use [llava-onevision-qwen2-7b-si-hf](https://huggingface.co/llava-hf/llava-onevision-qwen2-7b-si-hf) and a conversation history of text and image. Each content field has to be a list of dicts, as follows:

```python
from transformers import AutoProcessor

processor = AutoProcessor.from_pretrained("llava-hf/llava-onevision-qwen2-7b-si-hf")

conversation = [
    {
        "role": "user",
        "content": [
            {"type": "image"},
            {"type": "text", "text": "What’s shown in this image?"},
        ],
    },
    {
        "role": "assistant",
        "content": [{"type": "text", "text": "This image shows a red stop sign."},]
    },
    {

        "role": "user",
        "content": [
            {"type": "text", "text": "Describe the image in more details."},
        ],
    },
]

text_prompt = processor.apply_chat_template(conversation, add_generation_prompt=True)

# Note that the template simply formats your prompt, you still have to tokenize it and obtain pixel values for your images
print(text_prompt)
'user\nWhat is shown in this image?\nassistant\nPage showing the list of options.'
```

🚀 **Bonus:** If you're using `transformers>=4.49.0`, you can also get a vectorized output from `apply_chat_template`. See the **Usage Examples** below for more details on how to use it.

This model was contributed by [RaushanTurganbay](https://huggingface.co/RaushanTurganbay).
The original code can be found [here](https://github.com/LLaVA-VL/LLaVA-NeXT/tree/main).

## Usage example

### Single image inference

Here's how to load the model and perform inference in half-precision (`torch.float16`):

```python
from transformers import AutoProcessor, LlavaOnevisionForConditionalGeneration
from accelerate import Accelerator
import torch

device = Accelerator().device

processor = AutoProcessor.from_pretrained("llava-hf/llava-onevision-qwen2-7b-ov-hf") 
model = LlavaOnevisionForConditionalGeneration.from_pretrained(
    "llava-hf/llava-onevision-qwen2-7b-ov-hf",
    dtype=torch.float16,
    device_map=device
)

# prepare image and text prompt, using the appropriate prompt template
url = "https://github.com/haotian-liu/LLaVA/blob/1a91fc274d7c35a9b50b3cb29c4247ae5837ce39/images/llava_v1_5_radar.jpg?raw=true"
conversation = [
    {
        "role": "user",
        "content": [
            {"type": "image", "url": url},
            {"type": "text", "text": "What is shown in this image?"},
        ],
    },
]
inputs = processor.apply_chat_template(conversation, add_generation_prompt=True, tokenize=True, return_dict=True, return_tensors="pt")
inputs = inputs.to(model.device, torch.float16)

# autoregressively complete prompt
output = model.generate(**inputs, max_new_tokens=100)
print(processor.decode(output[0], skip_special_tokens=True))
'user\n\nWhat is shown in this image?\nassistant\nThe image shows a radar chart, also known as a spider chart or a star chart, which is used to compare multiple quantitative variables. Each axis represents a different variable, and the chart is filled with'
```

### Multi image inference

LLaVa-OneVision can perform inference with multiple images as input, where images either belong to the same prompt or different prompts (in batched inference). For that you have to use checkpoints with an "ov" suffix. For multi-image cases, we recommend using a **nested list of images** as input. Otherwise, every image will be patchified and consume a lot of memory. Here is how you can do it:

```python
import requests
from PIL import Image
import torch
from transformers import AutoProcessor, LlavaOnevisionForConditionalGeneration

# Load the model in half-precision
model = LlavaOnevisionForConditionalGeneration.from_pretrained("llava-hf/llava-onevision-qwen2-7b-ov-hf", dtype=torch.float16, device_map="auto")
processor = AutoProcessor.from_pretrained("llava-hf/llava-onevision-qwen2-7b-ov-hf")

# Prepare a batch of two prompts, where the first one is a multi-turn conversation and the second is not
conversation_1 = [
    {
        "role": "user",
        "content": [
            {"type": "image", "url": "https://www.ilankelman.org/stopsigns/australia.jpg"},
            {"type": "text", "text": "What is shown in this image?"},
        ],
    },
    {
        "role": "assistant",
        "content": [
            {"type": "text", "text": "There is a red stop sign in the image."},
        ],
    },
    {
        "role": "user",
        "content": [
            {"type": "image", "url": "http://images.cocodataset.org/val2017/000000039769.jpg"},
            {"type": "text", "text": "What about this image? How many cats do you see?"},
        ],
    },
]

conversation_2 = [
    {
        "role": "user",
        "content": [
            {"type": "image", "url": "https://huggingface.co/microsoft/kosmos-2-patch14-224/resolve/main/snowman.jpg"},
            {"type": "text", "text": "What is shown in this image?"},
        ],
    },
]

inputs = processor.apply_chat_template(
    [conversation_1, conversation_2],
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    padding=True,
    padding_side="left",
    return_tensors="pt",
).to(model.device, torch.float16)

# Generate
generate_ids = model.generate(**inputs, max_new_tokens=30)
processor.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)
['user\n\nWhat is shown in this image?\nassistant\nThere is a red stop sign in the image.\nuser\n\nWhat about this image? How many cats do you see?\nassistant\ntwo', 'user\n\nWhat is shown in this image?\nassistant\nThe image shows a whimsical scene of a snowman sitting by a campfire. The snowman is anthropomorphized, wearing a hat and']
```

### Video inference

LLaVa-OneVision also can perform inference with videos as input, where video frames are treated as multiple images. Here is how you can do it:

```python
from huggingface_hub import hf_hub_download
import torch
from transformers import AutoProcessor, LlavaOnevisionForConditionalGeneration

# Load the model in half-precision
model = LlavaOnevisionForConditionalGeneration.from_pretrained("llava-hf/llava-onevision-qwen2-7b-ov-hf", dtype=torch.float16, device_map="auto")
processor = AutoProcessor.from_pretrained("llava-hf/llava-onevision-qwen2-7b-ov-hf")

video_path = hf_hub_download(repo_id="raushan-testing-hf/videos-test", filename="sample_demo_1.mp4", repo_type="dataset")
conversation = [
    {

        "role": "user",
        "content": [
            {"type": "video", "path": video_path},
            {"type": "text", "text": "Why is this video funny?"},
            ],
    },
]

inputs = processor.apply_chat_template(
    conversation,
    num_frames=8
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt"
).to(model.device, torch.float16)

out = model.generate(**inputs, max_new_tokens=60)
processor.batch_decode(out, skip_special_tokens=True, clean_up_tokenization_spaces=True)
["user\n\nWhy is this video funny?\nassistant\nThe video appears to be humorous because it shows a young child, who is wearing glasses and holding a book, seemingly reading with a serious and focused expression. The child's glasses are a bit oversized for their face, which adds a comical touch, as it's a common trope to see children wearing"]
```

## Model optimization

### Quantization using bitsandbytes

The model can be loaded in 8 or 4 bits, greatly reducing the memory requirements while maintaining the performance of the original model. First make sure to install bitsandbytes, `pip install bitsandbytes` and make sure to have access to a GPU/accelerator that is supported by the library.

bitsandbytes is being refactored to support multiple backends beyond CUDA. Currently, ROCm (AMD GPU) and Intel CPU implementations are mature, with Intel XPU in progress and Apple Silicon support expected by Q4/Q1. For installation instructions and the latest backend updates, visit [this link](https://huggingface.co/docs/bitsandbytes/main/en/installation#multi-backend).

We value your feedback to help identify bugs before the full release! Check out [these docs](https://huggingface.co/docs/bitsandbytes/main/en/non_cuda_backends) for more details and feedback links.

Simply change the snippet above with:

```python
from transformers import LlavaOnevisionForConditionalGeneration, BitsAndBytesConfig

# specify how to quantize the model
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
)

model = LlavaOnevisionForConditionalGeneration.from_pretrained(model_id, quantization_config=quantization_config, device_map="auto")
```

### Use Flash-Attention 2 to further speed-up generation

First make sure to install flash-attn. Refer to the [original repository of Flash Attention](https://github.com/Dao-AILab/flash-attention) regarding that package installation. Simply change the snippet above with:

```python
from transformers import LlavaOnevisionForConditionalGeneration

model = LlavaOnevisionForConditionalGeneration.from_pretrained(
    model_id,
    dtype=torch.float16,
    use_flash_attention_2=True
).to(0)
```

## LlavaOnevisionConfig[[transformers.LlavaOnevisionConfig]]

#### transformers.LlavaOnevisionConfig[[transformers.LlavaOnevisionConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/llava_onevision/configuration_llava_onevision.py#L26)

This is the configuration class to store the configuration of a [LlavaOnevisionForConditionalGeneration](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionForConditionalGeneration). It is used to instantiate an
Llava-NeXT model according to the specified arguments, defining the model architecture. Instantiating a configuration
with the defaults will yield a similar configuration to that of the [llava-hf/llava-onevision-qwen2-7b-ov-hf](https://huggingface.co/llava-hf/llava-onevision-qwen2-7b-ov-hf)
model.

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:

```python
>>> from transformers import LlavaOnevisionForConditionalGeneration, LlavaOnevisionConfig, SiglipVisionConfig, Qwen2Config

>>> # Initializing a CLIP-vision config
>>> vision_config = SiglipVisionConfig()

>>> # Initializing a Llama config
>>> text_config = Qwen2Config()

>>> # Initializing a Llava-Next llava-hf/llava-onevision-qwen2-7b-ov-hf style configuration
>>> configuration = LlavaOnevisionConfig(vision_config, text_config)

>>> # Initializing a model from the llava-hf/llava-onevision-qwen2-7b-ov-hf style configuration
>>> model = LlavaOnevisionForConditionalGeneration(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

vision_config (`Union[AutoConfig, dict]`,  *optional*, defaults to `SiglipVisionConfig`) : The config object or dictionary of the vision backbone.

text_config (`Union[AutoConfig, dict]`, *optional*, defaults to `Qwen2Config`) : The config object or dictionary of the text backbone.

image_token_index (`int`, *optional*, defaults to 151646) : The image token index to encode the image prompt.

video_token_index (`int`, *optional*, defaults to 151647) : The video token index to encode the video prompt.

projector_hidden_act (`str`, *optional*, defaults to `"gelu"`) : The activation function used by the multimodal projector.

vision_feature_select_strategy (`str`, *optional*, defaults to `"full"`) : The feature selection strategy used to select the vision feature from the vision backbone. Can be one of `"default"` or `"full"`. If `"default"`, the CLS token is removed from the vision features. If `"full"`, the full vision features are used.

vision_feature_layer (`Union[int, list[int]]`, *optional*, defaults to -1) : The index of the layer to select the vision feature. If multiple indices are provided, the vision feature of the corresponding indices will be concatenated to form the vision features.

vision_aspect_ratio (`str`, *optional*, defaults to `"anyres_max_9"`) : Aspect ratio used when processong image features. The default value is "anyres_max_9".

image_grid_pinpoints (`List`, *optional*) : A list of possible resolutions to use for processing high resolution images. Each item in the list should be a tuple or list of the form `(height, width)`.

multimodal_projector_bias (`bool`, *optional*, defaults to `True`) : Whether to use bias in the multimodal projector.

tie_word_embeddings (`bool`, *optional*, defaults to `False`) : Whether to tie weight embeddings

## LlavaOnevisionProcessor[[transformers.LlavaOnevisionProcessor]]

#### transformers.LlavaOnevisionProcessor[[transformers.LlavaOnevisionProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/llava_onevision/processing_llava_onevision.py#L47)

Constructs a LlavaOnevisionProcessor which wraps a image processor, a tokenizer, and a video processor into a single processor.

[LlavaOnevisionProcessor](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionProcessor) offers all the functionalities of [LlavaOnevisionImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionImageProcessorFast), `tokenizer_class`, and [LlavaOnevisionVideoProcessor](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionVideoProcessor). See the
[~LlavaOnevisionImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionImageProcessorFast), `~tokenizer_class`, and [~LlavaOnevisionVideoProcessor](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionVideoProcessor) for more information.

__call__transformers.LlavaOnevisionProcessor.__call__https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/llava_onevision/processing_llava_onevision.py#L91[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor'], NoneType] = None"}, {"name": "text", "val": ": str | list[str] | list[list[str]] = None"}, {"name": "videos", "val": ": typing.Union[list['PIL.Image.Image'], numpy.ndarray, ForwardRef('torch.Tensor'), list[numpy.ndarray], list['torch.Tensor'], list[list['PIL.Image.Image']], list[list[numpy.ndarray]], list[list['torch.Tensor']], transformers.video_utils.URL, list[transformers.video_utils.URL], list[list[transformers.video_utils.URL]], transformers.video_utils.Path, list[transformers.video_utils.Path], list[list[transformers.video_utils.Path]], NoneType] = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.models.llava_onevision.processing_llava_onevision.LlavaOnevisionProcessorKwargs]"}]- **images** (`Union[PIL.Image.Image, numpy.ndarray, torch.Tensor, list, list, list]`, *optional*) --
  Image to preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If
  passing in images with pixel values between 0 and 1, set `do_rescale=False`.
- **text** (`Union[str, list, list]`, *optional*) --
  The sequence or batch of sequences to be encoded. Each sequence can be a string or a list of strings
  (pretokenized string). If you pass a pretokenized input, set `is_split_into_words=True` to avoid ambiguity with batched inputs.
- **videos** (`Union[list, numpy.ndarray, torch.Tensor, list, list, list, list, list, ~video_utils.URL, list, list, ~video_utils.Path, list, list]`, *optional*) --
  Video to preprocess. Expects a single or batch of videos with pixel values ranging from 0 to 255. If
  passing in videos with pixel values between 0 and 1, set `do_rescale=False`.
- **return_tensors** (`str` or [TensorType](/docs/transformers/v5.0.0/en/internal/file_utils#transformers.TensorType), *optional*) --
  If set, will return tensors of a particular framework. Acceptable values are:

  - `'pt'`: Return PyTorch `torch.Tensor` objects.
  - `'np'`: Return NumPy `np.ndarray` objects.0[BatchFeature](/docs/transformers/v5.0.0/en/main_classes/image_processor#transformers.BatchFeature)A [BatchFeature](/docs/transformers/v5.0.0/en/main_classes/image_processor#transformers.BatchFeature) with the following fields:

- **input_ids** -- List of token ids to be fed to a model. Returned when `text` is not `None`.
- **attention_mask** -- List of indices specifying which tokens should be attended to by the model (when
  `return_attention_mask=True` or if *"attention_mask"* is in `self.model_input_names` and if `text` is not
  `None`).
- **pixel_values** -- Pixel values to be fed to a model. Returned when `images` is not `None`.
- **pixel_values_videos** -- Pixel values of a video input to be fed to a model. Returned when `videos` is not `None`.
- **image_sizes** -- Size of each image that will be used to unpad an image. Returned when `images` is not `None`.

**Parameters:**

image_processor (`LlavaOnevisionImageProcessorFast`) : The image processor is a required input.

tokenizer (`tokenizer_class`) : The tokenizer is a required input.

video_processor (`LlavaOnevisionVideoProcessor`) : The video processor is a required input.

num_image_tokens (`int`, *optional*) : Number of image tokens for one imagethat will be returned by vision tower.

vision_feature_select_strategy (`str`, *optional*) : The feature selection strategy used to select the vision feature from the vision backbone. Should be same as in model's config

chat_template (`str`) : A Jinja template to convert lists of messages in a chat into a tokenizable string.

image_token (`str`, *optional*, defaults to `""`) : Special token used to denote image location.

video_token (`str`, *optional*, defaults to `""`) : Special token used to denote video location.

vision_aspect_ratio (`str`, *optional*, defaults to `"anyres_max_9"`) : Aspect ratio used when processong image features. The default value is "anyres_max_9".

**Returns:**

`[BatchFeature](/docs/transformers/v5.0.0/en/main_classes/image_processor#transformers.BatchFeature)`

A [BatchFeature](/docs/transformers/v5.0.0/en/main_classes/image_processor#transformers.BatchFeature) with the following fields:

- **input_ids** -- List of token ids to be fed to a model. Returned when `text` is not `None`.
- **attention_mask** -- List of indices specifying which tokens should be attended to by the model (when
  `return_attention_mask=True` or if *"attention_mask"* is in `self.model_input_names` and if `text` is not
  `None`).
- **pixel_values** -- Pixel values to be fed to a model. Returned when `images` is not `None`.
- **pixel_values_videos** -- Pixel values of a video input to be fed to a model. Returned when `videos` is not `None`.
- **image_sizes** -- Size of each image that will be used to unpad an image. Returned when `images` is not `None`.

## LlavaOnevisionImageProcessor[[transformers.LlavaOnevisionImageProcessor]]

#### transformers.LlavaOnevisionImageProcessor[[transformers.LlavaOnevisionImageProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/llava_onevision/image_processing_llava_onevision.py#L118)

Constructs a LLaVa-Onevision image processor. Based on [SiglipImageProcessor](/docs/transformers/v5.0.0/en/model_doc/siglip#transformers.SiglipImageProcessor) with incorporation of processing each video frame.

preprocesstransformers.LlavaOnevisionImageProcessor.preprocesshttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/llava_onevision/image_processing_llava_onevision.py#L611[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor']]"}, {"name": "do_resize", "val": ": bool | None = None"}, {"name": "size", "val": ": dict[str, int] | None = None"}, {"name": "image_grid_pinpoints", "val": ": list | None = None"}, {"name": "resample", "val": ": PIL.Image.Resampling | None = None"}, {"name": "do_rescale", "val": ": bool | None = None"}, {"name": "rescale_factor", "val": ": float | None = None"}, {"name": "do_normalize", "val": ": bool | None = None"}, {"name": "image_mean", "val": ": float | list[float] | None = None"}, {"name": "image_std", "val": ": float | list[float] | None = None"}, {"name": "do_pad", "val": ": bool | None = None"}, {"name": "do_convert_rgb", "val": ": bool | None = None"}, {"name": "return_tensors", "val": ": str | transformers.utils.generic.TensorType | None = None"}, {"name": "data_format", "val": ": transformers.image_utils.ChannelDimension | None = "}, {"name": "input_data_format", "val": ": str | transformers.image_utils.ChannelDimension | None = None"}]- **images** (`PIL.Image.Image`, `np.ndarray`, `torch.Tensor`, `list[PIL.Image.Image]`, `list[np.ndarray]`, `list[torch.Tensor]`) --
  The image or batch of images to be prepared. Each image can be a PIL image, NumPy array or PyTorch
  tensor. Both channels-first and channels-last formats are supported.
- **do_resize** (`bool`, *optional*, defaults to `self.do_resize`) --
  Whether to resize the image.
- **size** (`dict[str, int]`, *optional*, defaults to `self.size`) --
  Size of the image after resizing. Shortest edge of the image is resized to size["shortest_edge"], with
  the longest edge resized to keep the input aspect ratio.
- **image_grid_pinpoints** (`List` *optional*, defaults to `self.image_grid_pinpoints`) --
  A list of possible resolutions to use for processing high resolution images. The best resolution is
  selected based on the original size of the image.
- **resample** (`int`, *optional*, defaults to `self.resample`) --
  Resampling filter to use if resizing the image. This can be one of the enum `PILImageResampling`. Only
  has an effect if `do_resize` is set to `True`.
- **do_rescale** (`bool`, *optional*, defaults to `self.do_rescale`) --
  Whether to rescale the image.
- **rescale_factor** (`float`, *optional*, defaults to `self.rescale_factor`) --
  Rescale factor to rescale the image by if `do_rescale` is set to `True`.
- **do_normalize** (`bool`, *optional*, defaults to `self.do_normalize`) --
  Whether to normalize the image.
- **image_mean** (`float` or `list[float]`, *optional*, defaults to `self.image_mean`) --
  Image mean to use for normalization. Only has an effect if `do_normalize` is set to `True`.
- **image_std** (`float` or `list[float]`, *optional*, defaults to `self.image_std`) --
  Image standard deviation to use for normalization. Only has an effect if `do_normalize` is set to
  `True`.
- **do_pad** (`bool`, *optional*, defaults to `self.do_pad`) --
  Whether to pad the image. If `True`, will pad the patch dimension of the images in the batch to the largest
  number of patches in the batch. Padding will be applied to the bottom and right with zeros.
- **do_convert_rgb** (`bool`, *optional*, defaults to `self.do_convert_rgb`) --
  Whether to convert the image to RGB.
- **return_tensors** (`str` or `TensorType`, *optional*) --
  The type of tensors to return. Can be one of:
  - Unset: Return a list of `np.ndarray`.
  - `TensorType.PYTORCH` or `'pt'`: Return a batch of type `torch.Tensor`.
  - `TensorType.NUMPY` or `'np'`: Return a batch of type `np.ndarray`.
- **data_format** (`ChannelDimension` or `str`, *optional*, defaults to `ChannelDimension.FIRST`) --
  The channel dimension format for the output image. Can be one of:
  - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
  - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.
  - Unset: Use the channel dimension format of the input image.
- **input_data_format** (`ChannelDimension` or `str`, *optional*) --
  The channel dimension format for the input image. If unset, the channel dimension format is inferred
  from the input image. Can be one of:
  - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
  - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.
  - `"none"` or `ChannelDimension.NONE`: image in (height, width) format.0

**Parameters:**

do_resize (`bool`, *optional*, defaults to `True`) : Whether to resize the image's (height, width) dimensions to the specified `size`. Can be overridden by `do_resize` in the `preprocess` method.

size (`dict[str, int]` *optional*, defaults to `{"shortest_edge" : 224}`): Size of the image after resizing. The shortest edge of the image is resized to size["shortest_edge"], with the longest edge resized to keep the input aspect ratio. Can be overridden by `size` in the `preprocess` method.

image_grid_pinpoints (`List` *optional*, defaults to `[[672, 336], [336, 672], [672, 672], [336, 1008], [1008, 336]]`) : A list of possible resolutions to use for processing high resolution images. The best resolution is selected based on the original size of the image. Can be overridden by `image_grid_pinpoints` in the `preprocess` method. Not used for processing videos.

resample (`PILImageResampling`, *optional*, defaults to `Resampling.BICUBIC`) : Resampling filter to use if resizing the image. Can be overridden by `resample` in the `preprocess` method.

do_rescale (`bool`, *optional*, defaults to `True`) : Whether to rescale the image by the specified scale `rescale_factor`. Can be overridden by `do_rescale` in the `preprocess` method.

rescale_factor (`int` or `float`, *optional*, defaults to `1/255`) : Scale factor to use if rescaling the image. Can be overridden by `rescale_factor` in the `preprocess` method.

do_normalize (`bool`, *optional*, defaults to `True`) : Whether to normalize the image. Can be overridden by `do_normalize` in the `preprocess` method.

image_mean (`float` or `list[float]`, *optional*, defaults to `[0.48145466, 0.4578275, 0.40821073]`) : Mean to use if normalizing the image. This is a float or list of floats the length of the number of channels in the image. Can be overridden by the `image_mean` parameter in the `preprocess` method.

image_std (`float` or `list[float]`, *optional*, defaults to `[0.26862954, 0.26130258, 0.27577711]`) : Standard deviation to use if normalizing the image. This is a float or list of floats the length of the number of channels in the image. Can be overridden by the `image_std` parameter in the `preprocess` method. Can be overridden by the `image_std` parameter in the `preprocess` method.

do_pad (`bool`, *optional*, defaults to `True`) : Whether to pad the image. If `True`, will pad the patch dimension of the images in the batch to the largest number of patches in the batch. Padding will be applied to the bottom and right with zeros.

do_convert_rgb (`bool`, *optional*, defaults to `True`) : Whether to convert the image to RGB.

## LlavaOnevisionImageProcessorFast[[transformers.LlavaOnevisionImageProcessorFast]]

#### transformers.LlavaOnevisionImageProcessorFast[[transformers.LlavaOnevisionImageProcessorFast]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/llava_onevision/image_processing_llava_onevision_fast.py#L48)

Constructs a fast Llava Onevision image processor.

preprocesstransformers.LlavaOnevisionImageProcessorFast.preprocesshttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/llava_onevision/image_processing_llava_onevision_fast.py#L68[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor']]"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.models.llava_onevision.image_processing_llava_onevision.LlavaOnevisionImageProcessorKwargs]"}]- **images** (`Union[PIL.Image.Image, numpy.ndarray, torch.Tensor, list, list, list]`) --
  Image to preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If
  passing in images with pixel values between 0 and 1, set `do_rescale=False`.
- **do_convert_rgb** (`bool | None.do_convert_rgb`) --
  Whether to convert the image to RGB.
- **do_resize** (`bool | None.do_resize`) --
  Whether to resize the image.
- **size** (`Annotated[int | list[int] | tuple[int, ...] | dict[str, int] | None, None]`) --
  Describes the maximum input dimensions to the model.
- **crop_size** (`Annotated[int | list[int] | tuple[int, ...] | dict[str, int] | None, None]`) --
  Size of the output image after applying `center_crop`.
- **resample** (`Annotated[Union[PILImageResampling, int, NoneType], None]`) --
  Resampling filter to use if resizing the image. This can be one of the enum `PILImageResampling`. Only
  has an effect if `do_resize` is set to `True`.
- **do_rescale** (`bool | None.do_rescale`) --
  Whether to rescale the image.
- **rescale_factor** (`float | None.rescale_factor`) --
  Rescale factor to rescale the image by if `do_rescale` is set to `True`.
- **do_normalize** (`bool | None.do_normalize`) --
  Whether to normalize the image.
- **image_mean** (`float | list[float] | tuple[float, ...] | None.image_mean`) --
  Image mean to use for normalization. Only has an effect if `do_normalize` is set to `True`.
- **image_std** (`float | list[float] | tuple[float, ...] | None.image_std`) --
  Image standard deviation to use for normalization. Only has an effect if `do_normalize` is set to
  `True`.
- **do_pad** (`bool | None.do_pad`) --
  Whether to pad the image. Padding is done either to the largest size in the batch
  or to a fixed square size per image. The exact padding strategy depends on the model.
- **pad_size** (`Annotated[int | list[int] | tuple[int, ...] | dict[str, int] | None, None]`) --
  The size in `{"height": int, "width" int}` to pad the images to. Must be larger than any image size
  provided for preprocessing. If `pad_size` is not provided, images will be padded to the largest
  height and width in the batch. Applied only when `do_pad=True.`
- **do_center_crop** (`bool | None.do_center_crop`) --
  Whether to center crop the image.
- **data_format** (`str | ~image_utils.ChannelDimension | None.data_format`) --
  Only `ChannelDimension.FIRST` is supported. Added for compatibility with slow processors.
- **input_data_format** (`str | ~image_utils.ChannelDimension | None.input_data_format`) --
  The channel dimension format for the input image. If unset, the channel dimension format is inferred
  from the input image. Can be one of:
  - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
  - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.
  - `"none"` or `ChannelDimension.NONE`: image in (height, width) format.
- **device** (`Annotated[Union[str, torch.device, NoneType], None]`) --
  The device to process the images on. If unset, the device is inferred from the input images.
- **return_tensors** (`Annotated[str | ~utils.generic.TensorType | None, None]`) --
  Returns stacked tensors if set to `pt, otherwise returns a list of tensors.
- **disable_grouping** (`bool | None.disable_grouping`) --
  Whether to disable grouping of images by size to process them individually and not in batches.
  If None, will be set to True if the images are on CPU, and False otherwise. This choice is based on
  empirical observations, as detailed here: https://github.com/huggingface/transformers/pull/38157
- **image_seq_length** (`int | None.image_seq_length`) --
  The number of image tokens to be used for each image in the input.
  Added for backward compatibility but this should be set as a processor attribute in future models.
- **image_grid_pinpoints** (`list[list[int]]`, *optional*) --
  A list of possible resolutions to use for processing high resolution images. The best resolution is selected
  based on the original size of the image. Can be overridden by `image_grid_pinpoints` in the `preprocess`
  method.0``- **data** (`dict`) -- Dictionary of lists/arrays/tensors returned by the __call__ method ('pixel_values', etc.).
- **tensor_type** (`Union[None, str, TensorType]`, *optional*) -- You can give a tensor_type here to convert the lists of integers in PyTorch/Numpy Tensors at
  initialization.

**Parameters:**

images (`Union[PIL.Image.Image, numpy.ndarray, torch.Tensor, list, list, list]`) : Image to preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If passing in images with pixel values between 0 and 1, set `do_rescale=False`.

do_convert_rgb (`bool | None.do_convert_rgb`) : Whether to convert the image to RGB.

do_resize (`bool | None.do_resize`) : Whether to resize the image.

size (`Annotated[int | list[int] | tuple[int, ...] | dict[str, int] | None, None]`) : Describes the maximum input dimensions to the model.

crop_size (`Annotated[int | list[int] | tuple[int, ...] | dict[str, int] | None, None]`) : Size of the output image after applying `center_crop`.

resample (`Annotated[Union[PILImageResampling, int, NoneType], None]`) : Resampling filter to use if resizing the image. This can be one of the enum `PILImageResampling`. Only has an effect if `do_resize` is set to `True`.

do_rescale (`bool | None.do_rescale`) : Whether to rescale the image.

rescale_factor (`float | None.rescale_factor`) : Rescale factor to rescale the image by if `do_rescale` is set to `True`.

do_normalize (`bool | None.do_normalize`) : Whether to normalize the image.

image_mean (`float | list[float] | tuple[float, ...] | None.image_mean`) : Image mean to use for normalization. Only has an effect if `do_normalize` is set to `True`.

image_std (`float | list[float] | tuple[float, ...] | None.image_std`) : Image standard deviation to use for normalization. Only has an effect if `do_normalize` is set to `True`.

do_pad (`bool | None.do_pad`) : Whether to pad the image. Padding is done either to the largest size in the batch or to a fixed square size per image. The exact padding strategy depends on the model.

pad_size (`Annotated[int | list[int] | tuple[int, ...] | dict[str, int] | None, None]`) : The size in `{"height": int, "width" int}` to pad the images to. Must be larger than any image size provided for preprocessing. If `pad_size` is not provided, images will be padded to the largest height and width in the batch. Applied only when `do_pad=True.`

do_center_crop (`bool | None.do_center_crop`) : Whether to center crop the image.

data_format (`str | ~image_utils.ChannelDimension | None.data_format`) : Only `ChannelDimension.FIRST` is supported. Added for compatibility with slow processors.

input_data_format (`str | ~image_utils.ChannelDimension | None.input_data_format`) : The channel dimension format for the input image. If unset, the channel dimension format is inferred from the input image. Can be one of: - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format. - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format. - `"none"` or `ChannelDimension.NONE`: image in (height, width) format.

device (`Annotated[Union[str, torch.device, NoneType], None]`) : The device to process the images on. If unset, the device is inferred from the input images.

return_tensors (`Annotated[str | ~utils.generic.TensorType | None, None]`) : Returns stacked tensors if set to `pt, otherwise returns a list of tensors.

disable_grouping (`bool | None.disable_grouping`) : Whether to disable grouping of images by size to process them individually and not in batches. If None, will be set to True if the images are on CPU, and False otherwise. This choice is based on empirical observations, as detailed here: https://github.com/huggingface/transformers/pull/38157

image_seq_length (`int | None.image_seq_length`) : The number of image tokens to be used for each image in the input. Added for backward compatibility but this should be set as a processor attribute in future models.

image_grid_pinpoints (`list[list[int]]`, *optional*) : A list of possible resolutions to use for processing high resolution images. The best resolution is selected based on the original size of the image. Can be overridden by `image_grid_pinpoints` in the `preprocess` method.

**Returns:**

````

- **data** (`dict`) -- Dictionary of lists/arrays/tensors returned by the __call__ method ('pixel_values', etc.).
- **tensor_type** (`Union[None, str, TensorType]`, *optional*) -- You can give a tensor_type here to convert the lists of integers in PyTorch/Numpy Tensors at
  initialization.

## LlavaOnevisionVideoProcessor[[transformers.LlavaOnevisionVideoProcessor]]

#### transformers.LlavaOnevisionVideoProcessor[[transformers.LlavaOnevisionVideoProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/llava_onevision/video_processing_llava_onevision.py#L20)

## LlavaOnevisionModel[[transformers.LlavaOnevisionModel]]

#### transformers.LlavaOnevisionModel[[transformers.LlavaOnevisionModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/llava_onevision/modeling_llava_onevision.py#L267)

The Llava-Next model which consists of a vision backbone and a language model without language modeling head.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.LlavaOnevisionModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/llava_onevision/modeling_llava_onevision.py#L473[{"name": "input_ids", "val": ": torch.LongTensor | None = None"}, {"name": "pixel_values", "val": ": torch.FloatTensor | None = None"}, {"name": "image_sizes", "val": ": torch.LongTensor | None = None"}, {"name": "pixel_values_videos", "val": ": torch.FloatTensor | None = None"}, {"name": "image_sizes_videos", "val": ": torch.LongTensor | None = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.LongTensor | None = None"}, {"name": "past_key_values", "val": ": transformers.cache_utils.Cache | None = None"}, {"name": "inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "vision_feature_layer", "val": ": int | list[int] | None = None"}, {"name": "vision_feature_select_strategy", "val": ": str | None = None"}, {"name": "vision_aspect_ratio", "val": ": str | None = None"}, {"name": "batch_num_images", "val": ": torch.LongTensor | None = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "output_attentions", "val": ": bool | None = None"}, {"name": "output_hidden_states", "val": ": bool | None = None"}, {"name": "return_dict", "val": ": bool | None = None"}, {"name": "cache_position", "val": ": torch.LongTensor | None = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.modeling_flash_attention_utils.FlashAttentionKwargs]"}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **pixel_values** (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`, *optional*) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [LlavaOnevisionImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionImageProcessorFast). See [LlavaOnevisionImageProcessorFast.__call__()](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details ([LlavaOnevisionProcessor](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionProcessor) uses
  [LlavaOnevisionImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionImageProcessorFast) for processing images).
- **image_sizes** (`torch.LongTensor` of shape `(batch_size, 2)`, *optional*) --
  The sizes of the images in the batch, being (height, width) for each image.
- **pixel_values_videos** (`torch.FloatTensor` of shape `(batch_size, num_frames, num_channels, frame_size, frame_size)`, *optional*) --
  The tensors corresponding to the input video. Pixel values for videos can be obtained using
  [LlavaOnevisionVideoProcessor](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionVideoProcessor). See [LlavaOnevisionVideoProcessor.__call__()](/docs/transformers/v5.0.0/en/model_doc/pe_video#transformers.PeVideoVideoProcessor.__call__) for details ([LlavaOnevisionProcessor](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionProcessor) uses
  [LlavaOnevisionVideoProcessor](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionVideoProcessor) for processing videos).
- **image_sizes_videos** (`torch.LongTensor` of shape `(batch_size, frames, 2)`, *optional*) --
  The sizes of the videos in the batch, being (height, width) for each frame in the video.
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
- **vision_feature_layer** (`Union[int, list]`, *optional*) --
  The index of the layer to select the vision feature. If multiple indices are provided,
  the vision feature of the corresponding indices will be concatenated to form the
  vision features.
- **vision_feature_select_strategy** (`str`, *optional*) --
  The feature selection strategy used to select the vision feature from the vision backbone.
  Can be one of `"default"` or `"full"`.
- **vision_aspect_ratio** (`str`, *optional*, defaults to `"anyres_max_9"`) --
  Aspect ratio used when processing image features. The default value is "anyres_max_9".
- **batch_num_images** (`torch.LongTensor`, *optional*) --
  Number of images in each sample.
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
  the complete sequence length.0`transformers.models.llava_onevision.modeling_llava_onevision.LlavaOnevisionModelOutputWithPast` or `tuple(torch.FloatTensor)`A `transformers.models.llava_onevision.modeling_llava_onevision.LlavaOnevisionModelOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([LlavaOnevisionConfig](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionConfig)) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) -- Sequence of hidden-states at the output of the last layer of the model.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
  `past_key_values` input) to speed up sequential decoding.
- **hidden_states** (`tuple`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
- **image_hidden_states** (`torch.FloatTensor`, *optional*) -- A `torch.FloatTensor` of size `(batch_size, num_images, sequence_length, hidden_size)`.
  image_hidden_states of the model produced by the vision encoder and after projecting the last hidden state.
- **video_hidden_states** (`torch.FloatTensor`, *optional*) -- A `torch.FloatTensor`  of size `(batch_size * num_frames, num_videos, sequence_length, hidden_size)`.
  video_hidden_states of the model produced by the vision encoder and after projecting the last hidden state.
The [LlavaOnevisionModel](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

**Parameters:**

config ([LlavaOnevisionModel](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionModel)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``transformers.models.llava_onevision.modeling_llava_onevision.LlavaOnevisionModelOutputWithPast` or `tuple(torch.FloatTensor)``

A `transformers.models.llava_onevision.modeling_llava_onevision.LlavaOnevisionModelOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([LlavaOnevisionConfig](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionConfig)) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) -- Sequence of hidden-states at the output of the last layer of the model.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
  `past_key_values` input) to speed up sequential decoding.
- **hidden_states** (`tuple`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
- **image_hidden_states** (`torch.FloatTensor`, *optional*) -- A `torch.FloatTensor` of size `(batch_size, num_images, sequence_length, hidden_size)`.
  image_hidden_states of the model produced by the vision encoder and after projecting the last hidden state.
- **video_hidden_states** (`torch.FloatTensor`, *optional*) -- A `torch.FloatTensor`  of size `(batch_size * num_frames, num_videos, sequence_length, hidden_size)`.
  video_hidden_states of the model produced by the vision encoder and after projecting the last hidden state.
#### get_image_features[[transformers.LlavaOnevisionModel.get_image_features]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/llava_onevision/modeling_llava_onevision.py#L356)

Obtains image last hidden states from the vision tower and apply multimodal projection.

**Parameters:**

pixel_values (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`) : The tensors corresponding to the input images. Pixel values can be obtained using [LlavaOnevisionImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionImageProcessorFast). See [LlavaOnevisionImageProcessorFast.__call__()](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details ([LlavaOnevisionProcessor](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionProcessor) uses [LlavaOnevisionImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionImageProcessorFast) for processing images).

image_sizes (`torch.Tensor` of shape `(num_images, 2)`) : Actual image size of each images (H, W).

vision_feature_layer (`Union[int, list]`, *optional*) : The index of the layer to select the vision feature. If multiple indices are provided, the vision feature of the corresponding indices will be concatenated to form the vision features.

vision_feature_select_strategy (`str`, *optional*) : The feature selection strategy used to select the vision feature from the vision backbone. Can be one of `"default"` or `"full"`.

vision_aspect_ratio (`str`, *optional*, defaults to `"anyres_max_9"`) : Aspect ratio used when processing image features. The default value is "anyres_max_9".

batch_num_images (`torch.LongTensor`, *optional*) : Number of images in each sample.

output_hidden_states (`bool`, *optional*) : Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for more detail.

**Returns:**

`[transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([LlavaOnevisionConfig](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionConfig)) and inputs.

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
#### get_placeholder_mask[[transformers.LlavaOnevisionModel.get_placeholder_mask]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/llava_onevision/modeling_llava_onevision.py#L432)

Obtains multimodal placeholder mask from `input_ids` or `inputs_embeds`, and checks that the placeholder token count is
equal to the length of multimodal features. If the lengths are different, an error is raised.
#### get_video_features[[transformers.LlavaOnevisionModel.get_video_features]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/llava_onevision/modeling_llava_onevision.py#L575)

Obtains video last hidden states from the vision tower, apply multimodal projection and pooling.

**Parameters:**

pixel_values (`torch.FloatTensor]` of shape `(batch_size, num_frames, channels, height, width)`) : The tensors corresponding to the input video.

vision_feature_layer (`Union[int, list[int]], *optional*, defaults to -2`) : The index of the layer to select the vision feature. If multiple indices are provided, the vision feature of the corresponding indices will be concatenated to form the vision features.

vision_feature_layer (`Union[int, list]`, *optional*) : The index of the layer to select the vision feature. If multiple indices are provided, the vision feature of the corresponding indices will be concatenated to form the vision features.

vision_feature_select_strategy (`str`, *optional*) : The feature selection strategy used to select the vision feature from the vision backbone. Can be one of `"default"` or `"full"`

output_hidden_states (`bool`, *optional*) : Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for more detail.

**Returns:**

`[transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([LlavaOnevisionConfig](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionConfig)) and inputs.

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
#### pack_image_features[[transformers.LlavaOnevisionModel.pack_image_features]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/llava_onevision/modeling_llava_onevision.py#L291)

Reshape, unpad and then pack each image_feature into a single image_features tensor containing all visual vectors.

**Parameters:**

image_features (`list[torch.Tensor]` of length num_images, each of shape `(num_patches, image_length, embed_dim)`) : List of image feature tensor, each contains all the visual feature of all patches.

image_sizes (`torch.Tensor` of shape `(num_images, 2)`) : Actual image size of each images (H, W).

image_newline (`torch.Tensor` of shape `(embed_dim)`) : New line embedding vector.

vision_aspect_ratio (`str`, *optional*, "anyres_max_9") : Aspect ratio used when processing image features. The default value is "anyres_max_9".

**Returns:**

image_features (`torch.Tensor` of shape `(all_feat_len, embed_dim)`)
feature_lens (`list[int]`)
token length of each image in image_features

## LlavaOnevisionForConditionalGeneration[[transformers.LlavaOnevisionForConditionalGeneration]]

#### transformers.LlavaOnevisionForConditionalGeneration[[transformers.LlavaOnevisionForConditionalGeneration]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/llava_onevision/modeling_llava_onevision.py#L645)

The LLAVA-NeXT model which consists of a vision backbone and a language model.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.LlavaOnevisionForConditionalGeneration.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/llava_onevision/modeling_llava_onevision.py#L707[{"name": "input_ids", "val": ": torch.LongTensor | None = None"}, {"name": "pixel_values", "val": ": torch.FloatTensor | None = None"}, {"name": "image_sizes", "val": ": torch.LongTensor | None = None"}, {"name": "pixel_values_videos", "val": ": torch.FloatTensor | None = None"}, {"name": "image_sizes_videos", "val": ": torch.LongTensor | None = None"}, {"name": "attention_mask", "val": ": torch.Tensor | None = None"}, {"name": "position_ids", "val": ": torch.LongTensor | None = None"}, {"name": "past_key_values", "val": ": transformers.cache_utils.Cache | None = None"}, {"name": "inputs_embeds", "val": ": torch.FloatTensor | None = None"}, {"name": "vision_feature_layer", "val": ": int | list[int] | None = None"}, {"name": "vision_feature_select_strategy", "val": ": str | None = None"}, {"name": "vision_aspect_ratio", "val": ": str | None = None"}, {"name": "batch_num_images", "val": ": torch.LongTensor | None = None"}, {"name": "labels", "val": ": torch.LongTensor | None = None"}, {"name": "use_cache", "val": ": bool | None = None"}, {"name": "output_attentions", "val": ": bool | None = None"}, {"name": "output_hidden_states", "val": ": bool | None = None"}, {"name": "return_dict", "val": ": bool | None = None"}, {"name": "cache_position", "val": ": torch.LongTensor | None = None"}, {"name": "logits_to_keep", "val": ": int | torch.Tensor = 0"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **pixel_values** (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`, *optional*) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [LlavaOnevisionImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionImageProcessorFast). See [LlavaOnevisionImageProcessorFast.__call__()](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details ([LlavaOnevisionProcessor](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionProcessor) uses
  [LlavaOnevisionImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionImageProcessorFast) for processing images).
- **image_sizes** (`torch.LongTensor` of shape `(batch_size, 2)`, *optional*) --
  The sizes of the images in the batch, being (height, width) for each image.
- **pixel_values_videos** (`torch.FloatTensor` of shape `(batch_size, num_frames, num_channels, frame_size, frame_size)`, *optional*) --
  The tensors corresponding to the input video. Pixel values for videos can be obtained using
  [LlavaOnevisionVideoProcessor](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionVideoProcessor). See [LlavaOnevisionVideoProcessor.__call__()](/docs/transformers/v5.0.0/en/model_doc/pe_video#transformers.PeVideoVideoProcessor.__call__) for details ([LlavaOnevisionProcessor](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionProcessor) uses
  [LlavaOnevisionVideoProcessor](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionVideoProcessor) for processing videos).
- **image_sizes_videos** (`torch.LongTensor` of shape `(batch_size, frames, 2)`, *optional*) --
  The sizes of the videos in the batch, being (height, width) for each frame in the video.
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
- **vision_feature_layer** (`Union[int, list]`, *optional*) --
  The index of the layer to select the vision feature. If multiple indices are provided,
  the vision feature of the corresponding indices will be concatenated to form the
  vision features.
- **vision_feature_select_strategy** (`str`, *optional*) --
  The feature selection strategy used to select the vision feature from the vision backbone.
  Can be one of `"default"` or `"full"`.
- **vision_aspect_ratio** (`str`, *optional*, defaults to `"anyres_max_9"`) --
  Aspect ratio used when processing image features. The default value is "anyres_max_9".
- **batch_num_images** (`torch.LongTensor`, *optional*) --
  Number of images in each sample.
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
- **return_dict** (`bool`, *optional*) --
  Whether or not to return a [ModelOutput](/docs/transformers/v5.0.0/en/main_classes/output#transformers.utils.ModelOutput) instead of a plain tuple.
- **cache_position** (`torch.LongTensor` of shape `(sequence_length)`, *optional*) --
  Indices depicting the position of the input sequence tokens in the sequence. Contrarily to `position_ids`,
  this tensor is not affected by padding. It is used to update the cache in the correct position and to infer
  the complete sequence length.
- **logits_to_keep** (`Union[int, torch.Tensor]`, *optional*, defaults to `0`) --
  If an `int`, compute logits for the last `logits_to_keep` tokens. If `0`, calculate logits for all
  `input_ids` (special case). Only last token logits are needed for generation, and calculating them only for that
  token can save memory, which becomes pretty significant for long sequences or large vocabulary size.
  If a `torch.Tensor`, must be 1D corresponding to the indices to keep in the sequence length dimension.
  This is useful when using packed tensor format (single dimension for batch and sequence length).0`transformers.models.llava_onevision.modeling_llava_onevision.LlavaOnevisionCausalLMOutputWithPast` or `tuple(torch.FloatTensor)`A `transformers.models.llava_onevision.modeling_llava_onevision.LlavaOnevisionCausalLMOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([LlavaOnevisionConfig](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
  `past_key_values` input) to speed up sequential decoding.
- **hidden_states** (`tuple[torch.FloatTensor] | None.hidden_states`, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple[torch.FloatTensor] | None.attentions`, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
- **image_hidden_states** (`torch.FloatTensor`, *optional*) -- A `torch.FloatTensor` of size (batch_size * num_patches, num_images, sequence_length, hidden_size)`.
  image_hidden_states of the model produced by the vision encoder and after projecting the last hidden state.
- **video_hidden_states** (`torch.FloatTensor`, *optional*) -- A `torch.FloatTensor`  of size `(batch_size * num_frames, num_videos, sequence_length, hidden_size)`.
  video_hidden_states of the model produced by the vision encoder and after projecting the last hidden state.
The [LlavaOnevisionForConditionalGeneration](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionForConditionalGeneration) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Example:

```python
>>> from PIL import Image
>>> import httpx
>>> from io import BytesIO
>>> import torch
>>> from transformers import LlavaOnevisionProcessor, LlavaOnevisionForConditionalGeneration

>>> model = LlavaOnevisionForConditionalGeneration.from_pretrained("llava-hf/llava-onevision-qwen2-7b-ov-hf", dtype="float16", device_map="cuda:0")
>>> processor = LlavaOnevisionProcessor.from_pretrained("llava-hf/llava-onevision-qwen2-7b-ov-hf")

>>> conversation = [
...     {
...       "role": "user",
...       "content": [
...           {"type": "text", "text": "What is shown in this image?"},
...           {"type": "image"},
...         ],
...     },
... ]
>>> prompt = processor.apply_chat_template(conversation, add_generation_prompt=True)

>>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
>>> with httpx.stream("GET", url) as response:
...     image = Image.open(BytesIO(response.read()))
>>> inputs = processor(text=prompt, images=image, return_tensors='pt').to(0, torch.float16)

>>> output = model.generate(**inputs, max_new_tokens=20, do_sample=False)
>>> processor.batch_decode(output, skip_special_tokens=True)[0]
"user\n\nWhat is shown in this image?\nassistant\ncat"
```

**Parameters:**

config ([LlavaOnevisionConfig](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionConfig)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``transformers.models.llava_onevision.modeling_llava_onevision.LlavaOnevisionCausalLMOutputWithPast` or `tuple(torch.FloatTensor)``

A `transformers.models.llava_onevision.modeling_llava_onevision.LlavaOnevisionCausalLMOutputWithPast` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([LlavaOnevisionConfig](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionConfig)) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
  `past_key_values` input) to speed up sequential decoding.
- **hidden_states** (`tuple[torch.FloatTensor] | None.hidden_states`, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple[torch.FloatTensor] | None.attentions`, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
- **image_hidden_states** (`torch.FloatTensor`, *optional*) -- A `torch.FloatTensor` of size (batch_size * num_patches, num_images, sequence_length, hidden_size)`.
  image_hidden_states of the model produced by the vision encoder and after projecting the last hidden state.
- **video_hidden_states** (`torch.FloatTensor`, *optional*) -- A `torch.FloatTensor`  of size `(batch_size * num_frames, num_videos, sequence_length, hidden_size)`.
  video_hidden_states of the model produced by the vision encoder and after projecting the last hidden state.
#### get_image_features[[transformers.LlavaOnevisionForConditionalGeneration.get_image_features]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/llava_onevision/modeling_llava_onevision.py#L678)

Example:

```python
>>> from PIL import Image
>>> from transformers import AutoProcessor, LlavaOnevisionForConditionalGeneration

>>> model = LlavaOnevisionForConditionalGeneration.from_pretrained("llava-hf/llava-onevision-qwen2-7b-ov-hf")
>>> processor = AutoProcessor.from_pretrained("llava-hf/llava-onevision-qwen2-7b-ov-hf")

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

pixel_values (`torch.FloatTensor` of shape `(batch_size, num_channels, image_size, image_size)`) : The tensors corresponding to the input images. Pixel values can be obtained using [LlavaOnevisionImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionImageProcessorFast). See [LlavaOnevisionImageProcessorFast.__call__()](/docs/transformers/v5.0.0/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details ([LlavaOnevisionProcessor](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionProcessor) uses [LlavaOnevisionImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionImageProcessorFast) for processing images).

image_sizes (`torch.Tensor` of shape `(num_images, 2)`) : Actual image size of each images (H, W).

vision_feature_layer (`Union[int, list]`, *optional*) : The index of the layer to select the vision feature. If multiple indices are provided, the vision feature of the corresponding indices will be concatenated to form the vision features.

vision_feature_select_strategy (`str`, *optional*) : The feature selection strategy used to select the vision feature from the vision backbone. Can be one of `"default"` or `"full"`.

vision_aspect_ratio (`str`, *optional*, defaults to `"anyres_max_9"`) : Aspect ratio used when processing image features. The default value is "anyres_max_9".

batch_num_images (`torch.LongTensor`, *optional*) : Number of images in each sample.

**Returns:**

`[transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([LlavaOnevisionConfig](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionConfig)) and inputs.

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
#### get_video_features[[transformers.LlavaOnevisionForConditionalGeneration.get_video_features]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/llava_onevision/modeling_llava_onevision.py#L922)

Example:

```python
>>> from PIL import Image
>>> from transformers import AutoProcessor, LlavaOnevisionForConditionalGeneration

>>> model = LlavaOnevisionForConditionalGeneration.from_pretrained("llava-hf/llava-onevision-qwen2-7b-ov-hf")
>>> processor = AutoProcessor.from_pretrained("llava-hf/llava-onevision-qwen2-7b-ov-hf")

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

pixel_values (`torch.FloatTensor]` of shape `(batch_size, num_frames, channels, height, width)`) : The tensors corresponding to the input video.

vision_feature_layer (`Union[int, list[int]]`, *optional;*) : The index of the layer to select the vision feature. If multiple indices are provided, the vision feature of the corresponding indices will be concatenated to form the vision features.

vision_feature_layer (`Union[int, list]`, *optional*) : The index of the layer to select the vision feature. If multiple indices are provided, the vision feature of the corresponding indices will be concatenated to form the vision features.

vision_feature_select_strategy (`str`, *optional*) : The feature selection strategy used to select the vision feature from the vision backbone. Can be one of `"default"` or `"full"`

**Returns:**

`[transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutputWithPooling](/docs/transformers/v5.0.0/en/main_classes/output#transformers.modeling_outputs.BaseModelOutputWithPooling) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([LlavaOnevisionConfig](/docs/transformers/v5.0.0/en/model_doc/llava_onevision#transformers.LlavaOnevisionConfig)) and inputs.

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

