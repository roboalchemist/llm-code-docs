# Source: https://huggingface.co/docs/transformers/v5.0.0rc1/model_doc/kosmos2_5.md

# KOSMOS-2.5

The Kosmos-2.5 model was proposed in [KOSMOS-2.5: A Multimodal Literate Model](https://huggingface.co/papers/2309.11419/) by Microsoft.

The abstract from the paper is the following:

*We present Kosmos-2.5, a multimodal literate model for machine reading of text-intensive images. Pre-trained on large-scale text-intensive images, Kosmos-2.5 excels in two distinct yet cooperative transcription tasks: (1) generating spatially-aware text blocks, where each block of text is assigned its spatial coordinates within the image, and (2) producing structured text output that captures styles and structures into the markdown format. This unified multimodal literate capability is achieved through a shared Transformer architecture, task-specific prompts, and flexible text representations. We evaluate Kosmos-2.5 on end-to-end document-level text recognition and image-to-markdown text generation. Furthermore, the model can be readily adapted for any text-intensive image understanding task with different prompts through supervised fine-tuning, making it a general-purpose tool for real-world applications involving text-rich images. This work also paves the way for the future scaling of multimodal large language models.*

 Overview of tasks that KOSMOS-2.5 can handle. Taken from the original paper. 

The examples below demonstrates how to generate with [AutoModel](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoModel), for both Markdown and OCR tasks.

```py
import re
import torch
import requests
from PIL import Image, ImageDraw
from transformers import AutoProcessor, Kosmos2_5ForConditionalGeneration
from accelerate import Accelerator

repo = "microsoft/kosmos-2.5"
device = "cuda:0"
dtype = torch.bfloat16
model = Kosmos2_5ForConditionalGeneration.from_pretrained(repo, device_map=device, dtype=dtype)
processor = AutoProcessor.from_pretrained(repo)

# sample image
url = "https://huggingface.co/microsoft/kosmos-2.5/resolve/main/receipt_00008.png"
image = Image.open(requests.get(url, stream=True).raw)

prompt = ""
inputs = processor(text=prompt, images=image, return_tensors="pt")

height, width = inputs.pop("height"), inputs.pop("width")
raw_width, raw_height = image.size
scale_height = raw_height / height
scale_width = raw_width / width

inputs = {k: v.to(device) if v is not None else None for k, v in inputs.items()}
inputs["flattened_patches"] = inputs["flattened_patches"].to(dtype)
generated_ids = model.generate(
    **inputs,
    max_new_tokens=1024,
)

generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)
print(generated_text[0])
```

```py
import re
import torch
import requests
from PIL import Image, ImageDraw
from transformers import AutoProcessor, Kosmos2_5ForConditionalGeneration
from accelerate import Accelerator

repo = "microsoft/kosmos-2.5"
device = "cuda:0"
dtype = torch.bfloat16
model = Kosmos2_5ForConditionalGeneration.from_pretrained(repo, device_map=device, dtype=dtype)
processor = AutoProcessor.from_pretrained(repo)

# sample image
url = "https://huggingface.co/microsoft/kosmos-2.5/resolve/main/receipt_00008.png"
image = Image.open(requests.get(url, stream=True).raw)

# bs = 1
prompt = ""
inputs = processor(text=prompt, images=image, return_tensors="pt")
height, width = inputs.pop("height"), inputs.pop("width")
raw_width, raw_height = image.size
scale_height = raw_height / height
scale_width = raw_width / width

# bs > 1, batch generation
# inputs = processor(text=[prompt, prompt], images=[image,image], return_tensors="pt")
# height, width = inputs.pop("height"), inputs.pop("width")
# raw_width, raw_height = image.size
# scale_height = raw_height / height[0]
# scale_width = raw_width / width[0]

inputs = {k: v.to(device) if v is not None else None for k, v in inputs.items()}
inputs["flattened_patches"] = inputs["flattened_patches"].to(dtype)
generated_ids = model.generate(
    **inputs,
    max_new_tokens=1024,
)

generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)
def post_process(y, scale_height, scale_width):
    y = y.replace(prompt, "")
    if "" in prompt:
        return y
    pattern = r""
    bboxs_raw = re.findall(pattern, y)
    lines = re.split(pattern, y)[1:]
    bboxs = [re.findall(r"\d+", i) for i in bboxs_raw]
    bboxs = [[int(j) for j in i] for i in bboxs]
    info = ""
    for i in range(len(lines)):
        box = bboxs[i]
        x0, y0, x1, y1 = box
        if not (x0 >= x1 or y0 >= y1):
            x0 = int(x0 * scale_width)
            y0 = int(y0 * scale_height)
            x1 = int(x1 * scale_width)
            y1 = int(y1 * scale_height)
            info += f"{x0},{y0},{x1},{y0},{x1},{y1},{x0},{y1},{lines[i]}"
    return info

output_text = post_process(generated_text[0], scale_height, scale_width)
print(output_text)

draw = ImageDraw.Draw(image)
lines = output_text.split("\n")
for line in lines:
    # draw the bounding box
    line = list(line.split(","))
    if len(line) A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions. USER: {} ASSISTANT:"
prompt = template.format(question)
inputs = processor(text=prompt, images=image, return_tensors="pt")

height, width = inputs.pop("height"), inputs.pop("width")
raw_width, raw_height = image.size
scale_height = raw_height / height
scale_width = raw_width / width

inputs = {k: v.to(device) if v is not None else None for k, v in inputs.items()}
inputs["flattened_patches"] = inputs["flattened_patches"].to(dtype)
generated_ids = model.generate(
    **inputs,
    max_new_tokens=1024,
)

generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)
print(generated_text[0])
```

## Kosmos2_5Config[[transformers.Kosmos2_5Config]]

#### transformers.Kosmos2_5Config[[transformers.Kosmos2_5Config]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/kosmos2_5/configuration_kosmos2_5.py#L212)

This is the configuration class to store the configuration of a [Kosmos2_5Model](/docs/transformers/v5.0.0rc1/en/model_doc/kosmos2_5#transformers.Kosmos2_5Model). It is used to instantiate a
KOSMOS-2.5 model according to the specified arguments, defining the model architecture. Instantiating a configuration
with the defaults will yield a similar configuration to that of the KOSMOS-2.5
[microsoft/kosmos-2.5](https://huggingface.co/microsoft/kosmos-2.5) architecture.

**Parameters:**

text_config (`dict`, *optional*) : Dictionary of configuration options used to initialize `Kosmos2_5TextConfig`.

vision_config (`dict`, *optional*) : Dictionary of configuration options used to initialize `Kosmos2_5VisionConfig`.

latent_query_num (`int`, *optional*, defaults to 2048) : The number of latent query tokens that represent the image features used in the text decoder component.

kwargs (*optional*) : Dictionary of keyword arguments.

## Kosmos2_5ImageProcessor[[transformers.Kosmos2_5ImageProcessor]]

#### transformers.Kosmos2_5ImageProcessor[[transformers.Kosmos2_5ImageProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/kosmos2_5/image_processing_kosmos2_5.py#L90)

Constructs a Kosmos2_5 image processor.

preprocesstransformers.Kosmos2_5ImageProcessor.preprocesshttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/kosmos2_5/image_processing_kosmos2_5.py#L253[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor']]"}, {"name": "do_convert_rgb", "val": ": typing.Optional[bool] = None"}, {"name": "do_normalize", "val": ": typing.Optional[bool] = None"}, {"name": "max_patches", "val": ": typing.Optional[int] = None"}, {"name": "patch_size", "val": ": typing.Optional[dict[str, int]] = None"}, {"name": "return_tensors", "val": ": typing.Union[str, transformers.utils.generic.TensorType, NoneType] = None"}, {"name": "data_format", "val": ": ChannelDimension = "}, {"name": "input_data_format", "val": ": typing.Union[str, transformers.image_utils.ChannelDimension, NoneType] = None"}, {"name": "**kwargs", "val": ""}]- **images** (`ImageInput`) --
  Image to preprocess. Expects a single or batch of images.
- **do_convert_rgb** (`bool`, *optional*, defaults to `self.do_convert_rgb`) --
  Whether to convert the image to RGB.
- **do_normalize** (`bool`, *optional*, defaults to `self.do_normalize`) --
  Whether to normalize the image.
- **max_patches** (`int`, *optional*, defaults to `self.max_patches`) --
  Maximum number of patches to extract.
- **patch_size** (`dict`, *optional*, defaults to `self.patch_size`) --
  Dictionary containing the patch height and width.
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

Preprocess an image or batch of images. The processor first computes the maximum possible number of
aspect-ratio preserving patches of size `patch_size` that can be extracted from the image. It then pads the
image with zeros to make the image respect the constraint of `max_patches`.

**Parameters:**

do_convert_rgb (`bool`, *optional*, defaults to `True`) : Whether to convert the image to RGB.

do_normalize (`bool`, *optional*, defaults to `True`) : Whether to normalize the image. Can be overridden by the `do_normalize` parameter in the `preprocess` method. According to Kosmos2_5 paper and code, the image is normalized with its own mean and standard deviation.

patch_size (`Dict[str, int]`, *optional*, defaults to `{"height" : 16, "width": 16}`): The patch size to use for the image. According to Kosmos2_5 paper and code, the patch size is 16x16.

max_patches (`int`, *optional*, defaults to 4096) : The maximum number of patches to extract from the image as per the [KOSMOS 2.5 paper](https://huggingface.co/papers/2309.11419).

## Kosmos2_5ImageProcessorFast[[transformers.Kosmos2_5ImageProcessorFast]]

#### transformers.Kosmos2_5ImageProcessorFast[[transformers.Kosmos2_5ImageProcessorFast]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/kosmos2_5/image_processing_kosmos2_5_fast.py#L60)

Constructs a fast Kosmos2 5 image processor.

preprocesstransformers.Kosmos2_5ImageProcessorFast.preprocesshttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/kosmos2_5/image_processing_kosmos2_5_fast.py#L73[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor']]"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.models.kosmos2_5.image_processing_kosmos2_5.Kosmos2_5ImageProcessorKwargs]"}]- **images** (`Union[PIL.Image.Image, numpy.ndarray, torch.Tensor, list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor']]`) --
  Image to preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If
  passing in images with pixel values between 0 and 1, set `do_rescale=False`.
- **do_convert_rgb** (`bool`, *optional*) --
  Whether to convert the image to RGB.
- **do_resize** (`bool`, *optional*) --
  Whether to resize the image.
- **size** (`Annotated[Union[int, list[int], tuple[int, ...], dict[str, int], NoneType], None]`) --
  Describes the maximum input dimensions to the model.
- **crop_size** (`Annotated[Union[int, list[int], tuple[int, ...], dict[str, int], NoneType], None]`) --
  Size of the output image after applying `center_crop`.
- **resample** (`Annotated[Union[PILImageResampling, int, NoneType], None]`) --
  Resampling filter to use if resizing the image. This can be one of the enum `PILImageResampling`. Only
  has an effect if `do_resize` is set to `True`.
- **do_rescale** (`bool`, *optional*) --
  Whether to rescale the image.
- **rescale_factor** (`float`, *optional*) --
  Rescale factor to rescale the image by if `do_rescale` is set to `True`.
- **do_normalize** (`bool`, *optional*) --
  Whether to normalize the image.
- **image_mean** (`Union[float, list[float], tuple[float, ...], NoneType]`) --
  Image mean to use for normalization. Only has an effect if `do_normalize` is set to `True`.
- **image_std** (`Union[float, list[float], tuple[float, ...], NoneType]`) --
  Image standard deviation to use for normalization. Only has an effect if `do_normalize` is set to
  `True`.
- **do_pad** (`bool`, *optional*) --
  Whether to pad the image. Padding is done either to the largest size in the batch
  or to a fixed square size per image. The exact padding strategy depends on the model.
- **pad_size** (`Annotated[Union[int, list[int], tuple[int, ...], dict[str, int], NoneType], None]`) --
  The size in `{"height": int, "width" int}` to pad the images to. Must be larger than any image size
  provided for preprocessing. If `pad_size` is not provided, images will be padded to the largest
  height and width in the batch. Applied only when `do_pad=True.`
- **do_center_crop** (`bool`, *optional*) --
  Whether to center crop the image.
- **data_format** (`Union[~image_utils.ChannelDimension, str, NoneType]`) --
  Only `ChannelDimension.FIRST` is supported. Added for compatibility with slow processors.
- **input_data_format** (`Union[~image_utils.ChannelDimension, str, NoneType]`) --
  The channel dimension format for the input image. If unset, the channel dimension format is inferred
  from the input image. Can be one of:
  - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
  - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.
  - `"none"` or `ChannelDimension.NONE`: image in (height, width) format.
- **device** (`Annotated[Union[str, torch.device, NoneType], None]`) --
  The device to process the images on. If unset, the device is inferred from the input images.
- **return_tensors** (`Annotated[Union[str, ~utils.generic.TensorType, NoneType], None]`) --
  Returns stacked tensors if set to `pt, otherwise returns a list of tensors.
- **disable_grouping** (`bool`, *optional*) --
  Whether to disable grouping of images by size to process them individually and not in batches.
  If None, will be set to True if the images are on CPU, and False otherwise. This choice is based on
  empirical observations, as detailed here: https://github.com/huggingface/transformers/pull/38157
- **image_seq_length** (`int`, *optional*) --
  The number of image tokens to be used for each image in the input.
  Added for backward compatibility but this should be set as a processor attribute in future models.
- **patch_size** (`Dict[str, int]`, *optional*, defaults to `{"height" -- 16, "width": 16}`):
  The patch size to use for the image. According to Kosmos2_5 paper and code, the patch size is 16x16.
- **max_patches** (`int`, *optional*, defaults to 4096) --
  The maximum number of patches to extract from the image as per the
  [KOSMOS 2.5 paper](https://huggingface.co/papers/2309.11419).0``- **data** (`dict`) -- Dictionary of lists/arrays/tensors returned by the __call__ method ('pixel_values', etc.).
- **tensor_type** (`Union[None, str, TensorType]`, *optional*) -- You can give a tensor_type here to convert the lists of integers in PyTorch/Numpy Tensors at
  initialization.

**Parameters:**

images (`Union[PIL.Image.Image, numpy.ndarray, torch.Tensor, list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor']]`) : Image to preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If passing in images with pixel values between 0 and 1, set `do_rescale=False`.

do_convert_rgb (`bool`, *optional*) : Whether to convert the image to RGB.

do_resize (`bool`, *optional*) : Whether to resize the image.

size (`Annotated[Union[int, list[int], tuple[int, ...], dict[str, int], NoneType], None]`) : Describes the maximum input dimensions to the model.

crop_size (`Annotated[Union[int, list[int], tuple[int, ...], dict[str, int], NoneType], None]`) : Size of the output image after applying `center_crop`.

resample (`Annotated[Union[PILImageResampling, int, NoneType], None]`) : Resampling filter to use if resizing the image. This can be one of the enum `PILImageResampling`. Only has an effect if `do_resize` is set to `True`.

do_rescale (`bool`, *optional*) : Whether to rescale the image.

rescale_factor (`float`, *optional*) : Rescale factor to rescale the image by if `do_rescale` is set to `True`.

do_normalize (`bool`, *optional*) : Whether to normalize the image.

image_mean (`Union[float, list[float], tuple[float, ...], NoneType]`) : Image mean to use for normalization. Only has an effect if `do_normalize` is set to `True`.

image_std (`Union[float, list[float], tuple[float, ...], NoneType]`) : Image standard deviation to use for normalization. Only has an effect if `do_normalize` is set to `True`.

do_pad (`bool`, *optional*) : Whether to pad the image. Padding is done either to the largest size in the batch or to a fixed square size per image. The exact padding strategy depends on the model.

pad_size (`Annotated[Union[int, list[int], tuple[int, ...], dict[str, int], NoneType], None]`) : The size in `{"height": int, "width" int}` to pad the images to. Must be larger than any image size provided for preprocessing. If `pad_size` is not provided, images will be padded to the largest height and width in the batch. Applied only when `do_pad=True.`

do_center_crop (`bool`, *optional*) : Whether to center crop the image.

data_format (`Union[~image_utils.ChannelDimension, str, NoneType]`) : Only `ChannelDimension.FIRST` is supported. Added for compatibility with slow processors.

input_data_format (`Union[~image_utils.ChannelDimension, str, NoneType]`) : The channel dimension format for the input image. If unset, the channel dimension format is inferred from the input image. Can be one of: - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format. - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format. - `"none"` or `ChannelDimension.NONE`: image in (height, width) format.

device (`Annotated[Union[str, torch.device, NoneType], None]`) : The device to process the images on. If unset, the device is inferred from the input images.

return_tensors (`Annotated[Union[str, ~utils.generic.TensorType, NoneType], None]`) : Returns stacked tensors if set to `pt, otherwise returns a list of tensors.

disable_grouping (`bool`, *optional*) : Whether to disable grouping of images by size to process them individually and not in batches. If None, will be set to True if the images are on CPU, and False otherwise. This choice is based on empirical observations, as detailed here: https://github.com/huggingface/transformers/pull/38157

image_seq_length (`int`, *optional*) : The number of image tokens to be used for each image in the input. Added for backward compatibility but this should be set as a processor attribute in future models.

patch_size (`Dict[str, int]`, *optional*, defaults to `{"height" : 16, "width": 16}`): The patch size to use for the image. According to Kosmos2_5 paper and code, the patch size is 16x16.

max_patches (`int`, *optional*, defaults to 4096) : The maximum number of patches to extract from the image as per the [KOSMOS 2.5 paper](https://huggingface.co/papers/2309.11419).

**Returns:**

````

- **data** (`dict`) -- Dictionary of lists/arrays/tensors returned by the __call__ method ('pixel_values', etc.).
- **tensor_type** (`Union[None, str, TensorType]`, *optional*) -- You can give a tensor_type here to convert the lists of integers in PyTorch/Numpy Tensors at
  initialization.

## Kosmos2_5Processor[[transformers.Kosmos2_5Processor]]

#### transformers.Kosmos2_5Processor[[transformers.Kosmos2_5Processor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/kosmos2_5/processing_kosmos2_5.py#L47)

Constructs a Kosmos2_5 processor which wraps a PreTrainedTokenizerFast and Kosmos2_5 image processor into a single
processor.

[Kosmos2_5Processor](/docs/transformers/v5.0.0rc1/en/model_doc/kosmos2_5#transformers.Kosmos2_5Processor) offers all the functionalities of [Kosmos2_5ImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/kosmos2_5#transformers.Kosmos2_5ImageProcessor) and [PreTrainedTokenizerFast](/docs/transformers/v5.0.0rc1/en/main_classes/tokenizer#transformers.TokenizersBackend). See
the docstring of `__call__()` and [decode()](/docs/transformers/v5.0.0rc1/en/model_doc/kosmos2_5#transformers.Kosmos2_5Processor.decode) for more information.

batch_decodetransformers.Kosmos2_5Processor.batch_decodehttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/kosmos2_5/processing_kosmos2_5.py#L130[{"name": "*args", "val": ""}, {"name": "**kwargs", "val": ""}]

This method forwards all its arguments to Kosmos2_5TokenizerFast's [batch_decode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.batch_decode).
Please refer to the docstring of this method for more information.

**Parameters:**

image_processor (`Kosmos2_5ImageProcessor`) : An instance of [Kosmos2_5ImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/kosmos2_5#transformers.Kosmos2_5ImageProcessor). The image processor is a required input.

tokenizer (`T5Tokenizer`) : An instance of ['T5Tokenizer`]. The tokenizer is a required input.

num_image_tokens (`int`, *optional*, defaults to 2048) : Number of image tokens used as a placeholder.
#### decode[[transformers.Kosmos2_5Processor.decode]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/kosmos2_5/processing_kosmos2_5.py#L137)

This method forwards all its arguments to Kosmos2_5TokenizerFast's [decode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.decode). Please
refer to the docstring of this method for more information.

## Kosmos2_5Model[[transformers.Kosmos2_5Model]]

#### transformers.Kosmos2_5Model[[transformers.Kosmos2_5Model]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/kosmos2_5/modeling_kosmos2_5.py#L1379)

KOSMOS-2.5 Model for generating text and image features. The model consists of a vision encoder and a language model.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.Kosmos2_5Model.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/kosmos2_5/modeling_kosmos2_5.py#L1398[{"name": "input_ids", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "flattened_patches", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "width", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "height", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "image_embeds_position_mask", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "attention_mask", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "past_key_values", "val": ": typing.Optional[transformers.cache_utils.Cache] = None"}, {"name": "image_embeds", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "inputs_embeds", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "position_ids", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "use_cache", "val": ": typing.Optional[bool] = None"}, {"name": "output_attentions", "val": ": typing.Optional[bool] = None"}, {"name": "output_hidden_states", "val": ": typing.Optional[bool] = None"}, {"name": "cache_position", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default should you provide
  it.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **flattened_patches** (`torch.FloatTensor` of shape `(batch_size, max_patches, 2 + patch_height * patch_width * image_channels)`) --
  Flattened patches of the images. `flattened_patches` can be obtained using [AutoImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoImageProcessor). See
  [Kosmos2_5ImageProcessor.__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details.
- **width** (`torch.FloatTensor` of shape `(batch_size,)`) --
  The original width (before resizing) of each image in the batch. This can be obtained using
  [AutoImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoImageProcessor). See [Kosmos2_5ImageProcessor.__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details.
- **height** (`torch.FloatTensor` of shape `(batch_size,)`) --
  The original height (before resizing) of each image in the batch. This can be obtained using
  [AutoImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoImageProcessor). See [Kosmos2_5ImageProcessor.__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details.
- **image_embeds_position_mask** (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Mask to indicate the location in a sequence to insert the image features . Mask values selected in `[0,
  1]`:

  - 1 for places where to put the image features,
  - 0 for places that are not for image features (i.e. for text tokens).

- **attention_mask** (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.

  [What are attention masks?](../glossary#attention-mask)

- **past_key_values** (`Cache` of length `config.n_layers` with each tuple having 4 tensors of shape `(batch_size, num_heads, sequence_length - 1, embed_size_per_head)`) --
  Contains precomputed key and value hidden states of the attention blocks. Can be used to speed up decoding.

  If `past_key_values` are used, the user can optionally input only the last `decoder_input_ids` (those that
  don't have their past key value states given to this model) of shape `(batch_size, 1)` instead of all
  `decoder_input_ids` of shape `(batch_size, sequence_length)`.
- **image_embeds** -- (`torch.FloatTensor` of shape `(batch_size, latent_query_num, hidden_size)`, *optional*):
  Sequence of hidden-states at the output of `Kosmos2ImageToTextProjection`.
- **inputs_embeds** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) --
  Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation. This
  is useful if you want more control over how to convert `input_ids` indices into associated vectors than the
  model's internal embedding lookup matrix.
- **position_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of positions of each input sequence tokens in the position embeddings. Selected in the range `[0,
  config.max_position_embeddings - 1]`.

  [What are position IDs?](../glossary#position-ids)
- **use_cache** (`bool`, *optional*) --
  If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
  `past_key_values`).
- **output_attentions** (`bool`, *optional*) --
  Whether or not to return the attentions tensors of all attention layers. See `attentions` under returned
  tensors for more detail.
- **output_hidden_states** (`bool`, *optional*) --
  Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
  more detail.0`transformers.models.kosmos2_5.modeling_kosmos2_5.Kosmos2_5ModelOutput` or `tuple(torch.FloatTensor)`A `transformers.models.kosmos2_5.modeling_kosmos2_5.Kosmos2_5ModelOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration (``) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
- **width** (`torch.FloatTensor` of shape `(batch_size,)`) -- The original width (before resizing) of each image in the batch.
- **height** (`torch.FloatTensor` of shape `(batch_size,)`) -- The original height (before resizing) of each image in the batch.
- **image_embeds** (`torch.FloatTensor` of shape `(batch_size, latent_query_num, hidden_size)`, *optional*) -- Sequence of hidden-states at the output of `Kosmos2ImageToTextProjection`.
- **projection_attentions** (`tuple(torch.FloatTensor)`, *optional*) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights given by `Kosmos2ImageToTextProjection`, after the attention softmax, used to compute
  the weighted average in the self-attention heads.
- **vision_model_output(`BaseModelOutputWithPooling`,** *optional*) -- The output of the `Kosmos2VisionModel`.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks and optionally if
  `config.is_encoder_decoder=True` in the cross-attention blocks) that can be used (see `past_key_values`
  input) to speed up sequential decoding.
The [Kosmos2_5Model](/docs/transformers/v5.0.0rc1/en/model_doc/kosmos2_5#transformers.Kosmos2_5Model) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Examples:

```python
>>> from PIL import Image
>>> import requests
>>> from transformers import AutoProcessor, Kosmos2_5Model

>>> model = Kosmos2_5Model.from_pretrained("microsoft/kosmos2.5")
>>> processor = AutoProcessor.from_pretrained("microsoft/kosmos2.5")

>>> url = "https://huggingface.co/microsoft/kosmos2.5/resolve/main/snowman.jpg"
>>> image = Image.open(requests.get(url, stream=True).raw)

>>> text = (
...     " An image of a snowman"
...     " warming himself by a fire"
...     ""
... )

>>> inputs = processor(text=text, images=image, return_tensors="pt", add_eos_token=True)

>>> last_hidden_state = model(
...     pixel_values=inputs["pixel_values"],
...     input_ids=inputs["input_ids"],
...     attention_mask=inputs["attention_mask"],
...     image_embeds_position_mask=inputs["image_embeds_position_mask"],
... ).last_hidden_state
>>> list(last_hidden_state.shape)
[1, 91, 2048]
```

**Parameters:**

config ([Kosmos2_5Config](/docs/transformers/v5.0.0rc1/en/model_doc/kosmos2_5#transformers.Kosmos2_5Config)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``transformers.models.kosmos2_5.modeling_kosmos2_5.Kosmos2_5ModelOutput` or `tuple(torch.FloatTensor)``

A `transformers.models.kosmos2_5.modeling_kosmos2_5.Kosmos2_5ModelOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration (``) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
- **width** (`torch.FloatTensor` of shape `(batch_size,)`) -- The original width (before resizing) of each image in the batch.
- **height** (`torch.FloatTensor` of shape `(batch_size,)`) -- The original height (before resizing) of each image in the batch.
- **image_embeds** (`torch.FloatTensor` of shape `(batch_size, latent_query_num, hidden_size)`, *optional*) -- Sequence of hidden-states at the output of `Kosmos2ImageToTextProjection`.
- **projection_attentions** (`tuple(torch.FloatTensor)`, *optional*) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights given by `Kosmos2ImageToTextProjection`, after the attention softmax, used to compute
  the weighted average in the self-attention heads.
- **vision_model_output(`BaseModelOutputWithPooling`,** *optional*) -- The output of the `Kosmos2VisionModel`.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks and optionally if
  `config.is_encoder_decoder=True` in the cross-attention blocks) that can be used (see `past_key_values`
  input) to speed up sequential decoding.

## Kosmos2_5ForConditionalGeneration[[transformers.Kosmos2_5ForConditionalGeneration]]

#### transformers.Kosmos2_5ForConditionalGeneration[[transformers.Kosmos2_5ForConditionalGeneration]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/kosmos2_5/modeling_kosmos2_5.py#L1664)

KOSMOS-2.5 Model for generating text and bounding boxes given an image. The model consists of a vision encoder and a
language model.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.Kosmos2_5ForConditionalGeneration.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/kosmos2_5/modeling_kosmos2_5.py#L1687[{"name": "input_ids", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "flattened_patches", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "width", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "height", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "image_embeds_position_mask", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "attention_mask", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "past_key_values", "val": ": typing.Optional[transformers.cache_utils.Cache] = None"}, {"name": "image_embeds", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "inputs_embeds", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "position_ids", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "labels", "val": ": typing.Optional[torch.LongTensor] = None"}, {"name": "use_cache", "val": ": typing.Optional[bool] = None"}, {"name": "output_attentions", "val": ": typing.Optional[bool] = None"}, {"name": "output_hidden_states", "val": ": typing.Optional[bool] = None"}, {"name": "logits_to_keep", "val": ": typing.Union[int, torch.Tensor] = 0"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.utils.generic.TransformersKwargs]"}]- **input_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`) --
  Indices of input sequence tokens in the vocabulary. Padding will be ignored by default should you provide
  it.

  Indices can be obtained using [AutoTokenizer](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoTokenizer). See [PreTrainedTokenizer.encode()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.encode) and
  [PreTrainedTokenizer.__call__()](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.__call__) for details.

  [What are input IDs?](../glossary#input-ids)
- **flattened_patches** (`torch.FloatTensor` of shape `(batch_size, max_patches, 2 + patch_height * patch_width * image_channels)`) --
  Flattened patches of the images. `flattened_patches` can be obtained using [AutoImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoImageProcessor). See
  [Kosmos2_5ImageProcessor.__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details.
- **width** (`torch.FloatTensor` of shape `(batch_size,)`) --
  The original width (before resizing) of each image in the batch. This can be obtained using
  [AutoImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoImageProcessor). See [Kosmos2_5ImageProcessor.__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details.
- **height** (`torch.FloatTensor` of shape `(batch_size,)`) --
  The original height (before resizing) of each image in the batch. This can be obtained using
  [AutoImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/auto#transformers.AutoImageProcessor). See [Kosmos2_5ImageProcessor.__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details.
- **image_embeds_position_mask** (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Mask to indicate the location in a sequence to insert the image features . Mask values selected in `[0,
  1]`:

  - 1 for places where to put the image features,
  - 0 for places that are not for image features (i.e. for text tokens).

- **attention_mask** (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

  - 1 for tokens that are **not masked**,
  - 0 for tokens that are **masked**.

  [What are attention masks?](../glossary#attention-mask)

- **past_key_values** (`Cache` of length `config.n_layers` with each tuple having 4 tensors of shape `(batch_size, num_heads, sequence_length - 1, embed_size_per_head)`) --
  Contains precomputed key and value hidden states of the attention blocks. Can be used to speed up decoding.

  If `past_key_values` are used, the user can optionally input only the last `decoder_input_ids` (those that
  don't have their past key value states given to this model) of shape `(batch_size, 1)` instead of all
  `decoder_input_ids` of shape `(batch_size, sequence_length)`.
- **image_embeds** -- (`torch.FloatTensor` of shape `(batch_size, latent_query_num, hidden_size)`, *optional*):
  Sequence of hidden-states at the output of `Kosmos2ImageToTextProjection`.
- **inputs_embeds** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*) --
  Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation. This
  is useful if you want more control over how to convert `input_ids` indices into associated vectors than the
  model's internal embedding lookup matrix.
- **position_ids** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Indices of positions of each input sequence tokens in the position embeddings. Selected in the range `[0,
  config.max_position_embeddings - 1]`.

  [What are position IDs?](../glossary#position-ids)
- **use_cache** (`bool`, *optional*) --
  If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
  `past_key_values`).
- **output_attentions** (`bool`, *optional*) --
  Whether or not to return the attentions tensors of all attention layers. See `attentions` under returned
  tensors for more detail.
- **output_hidden_states** (`bool`, *optional*) --
  Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
  more detail.

- **labels** (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*) --
  Labels for computing the left-to-right language modeling loss (next word prediction). Indices should be in
  `[-100, 0, ..., config.vocab_size]` (see `input_ids` docstring) Tokens with indices set to `-100` are
  ignored (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`0`transformers.models.kosmos2_5.modeling_kosmos2_5.Kosmos2_5ForConditionalGenerationModelOutput` or `tuple(torch.FloatTensor)`A `transformers.models.kosmos2_5.modeling_kosmos2_5.Kosmos2_5ForConditionalGenerationModelOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration (``) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
- **width** (`torch.FloatTensor` of shape `(batch_size,)`) -- The original width (before resizing) of each image in the batch.
- **height** (`torch.FloatTensor` of shape `(batch_size,)`) -- The original height (before resizing) of each image in the batch.
- **image_embeds** (`torch.FloatTensor` of shape `(batch_size, latent_query_num, hidden_size)`, *optional*) -- Sequence of hidden-states at the output of `Kosmos2ImageToTextProjection`.
- **projection_attentions** (`tuple(torch.FloatTensor)`, *optional*) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights given by `Kosmos2ImageToTextProjection`, after the attention softmax, used to compute
  the weighted average in the self-attention heads.
- **vision_model_output(`BaseModelOutputWithPooling`,** *optional*) -- The output of the `Kosmos2VisionModel`.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks and optionally if
  `config.is_encoder_decoder=True` in the cross-attention blocks) that can be used (see `past_key_values`
  input) to speed up sequential decoding.
The [Kosmos2_5ForConditionalGeneration](/docs/transformers/v5.0.0rc1/en/model_doc/kosmos2_5#transformers.Kosmos2_5ForConditionalGeneration) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

Examples:

```python
>>> from PIL import Image
>>> import requests
>>> import torch
>>> from transformers import AutoProcessor, Kosmos2_5ForConditionalGeneration

>>> repo = "microsoft/kosmos-2.5"
>>> device = "cuda:0"
>>> dtype = torch.bfloat16 # torch.float16
>>> model = Kosmos2_5ForConditionalGeneration.from_pretrained(repo, device_map=device, dtype=dtype)
>>> processor = AutoProcessor.from_pretrained(repo)

>>> url = "https://huggingface.co/microsoft/kosmos-2.5/resolve/main/receipt_00008.png"

>>> image = Image.open(requests.get(url, stream=True).raw)

>>> prompt = "" # 

>>> inputs = processor(text=prompt, images=image, return_tensors="pt")
>>> height, width = inputs.pop("height"), inputs.pop("width")
>>> inputs = {k: v.to(device) if v is not None else None for k, v in inputs.items()}
>>> inputs["flattened_patches"] = inputs["flattened_patches"].to(dtype)

>>> generated_ids = model.generate(**inputs,max_new_tokens=1024)
>>> generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
>>> generated_text
'1\n[REG] BLACK SAKURA\n45,455\n1\nCOOKIE DOH SAUCES\n0\n1\nNATA DE COCO\n0\nSub Total 45,455\nPB1 (10%) 4,545\nRounding 0\nTotal 50,000\nCard Payment 50,000\n'
```

**Parameters:**

config ([Kosmos2_5Config](/docs/transformers/v5.0.0rc1/en/model_doc/kosmos2_5#transformers.Kosmos2_5Config)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

``transformers.models.kosmos2_5.modeling_kosmos2_5.Kosmos2_5ForConditionalGenerationModelOutput` or `tuple(torch.FloatTensor)``

A `transformers.models.kosmos2_5.modeling_kosmos2_5.Kosmos2_5ForConditionalGenerationModelOutput` or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration (``) and inputs.

- **loss** (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) -- Language modeling loss (for next-token prediction).
- **logits** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) -- Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
- **width** (`torch.FloatTensor` of shape `(batch_size,)`) -- The original width (before resizing) of each image in the batch.
- **height** (`torch.FloatTensor` of shape `(batch_size,)`) -- The original height (before resizing) of each image in the batch.
- **image_embeds** (`torch.FloatTensor` of shape `(batch_size, latent_query_num, hidden_size)`, *optional*) -- Sequence of hidden-states at the output of `Kosmos2ImageToTextProjection`.
- **projection_attentions** (`tuple(torch.FloatTensor)`, *optional*) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights given by `Kosmos2ImageToTextProjection`, after the attention softmax, used to compute
  the weighted average in the self-attention heads.
- **vision_model_output(`BaseModelOutputWithPooling`,** *optional*) -- The output of the `Kosmos2VisionModel`.
- **past_key_values** (`Cache`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`) -- It is a [Cache](/docs/transformers/v5.0.0rc1/en/internal/generation_utils#transformers.Cache) instance. For more details, see our [kv cache guide](https://huggingface.co/docs/transformers/en/kv_cache).

  Contains pre-computed hidden-states (key and values in the self-attention blocks and optionally if
  `config.is_encoder_decoder=True` in the cross-attention blocks) that can be used (see `past_key_values`
  input) to speed up sequential decoding.

