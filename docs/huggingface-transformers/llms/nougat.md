# Source: https://huggingface.co/docs/transformers/v5.0.0/model_doc/nougat.md

# Nougat

## Overview

The Nougat model was proposed in [Nougat: Neural Optical Understanding for Academic Documents](https://huggingface.co/papers/2308.13418) by
Lukas Blecher, Guillem Cucurull, Thomas Scialom, Robert Stojnic. Nougat uses the same architecture as [Donut](donut), meaning an image Transformer
encoder and an autoregressive text Transformer decoder to translate scientific PDFs to markdown, enabling easier access to them.

The abstract from the paper is the following:

*Scientific knowledge is predominantly stored in books and scientific journals, often in the form of PDFs. However, the PDF format leads to a loss of semantic information, particularly for mathematical expressions. We propose Nougat (Neural Optical Understanding for Academic Documents), a Visual Transformer model that performs an Optical Character Recognition (OCR) task for processing scientific documents into a markup language, and demonstrate the effectiveness of our model on a new dataset of scientific documents. The proposed approach offers a promising solution to enhance the accessibility of scientific knowledge in the digital age, by bridging the gap between human-readable documents and machine-readable text. We release the models and code to accelerate future work on scientific text recognition.*

 Nougat high-level overview. Taken from the original paper. 

This model was contributed by [nielsr](https://huggingface.co/nielsr). The original code can be found
[here](https://github.com/facebookresearch/nougat).

## Usage tips

- The quickest way to get started with Nougat is by checking the [tutorial
  notebooks](https://github.com/NielsRogge/Transformers-Tutorials/tree/master/Nougat), which show how to use the model
  at inference time as well as fine-tuning on custom data.
- Nougat is always used within the [VisionEncoderDecoder](vision-encoder-decoder) framework. The model is identical to [Donut](donut) in terms of architecture.

## Inference

Nougat's `VisionEncoderDecoder` model accepts images as input and makes use of
[generate()](/docs/transformers/v5.0.0/en/main_classes/text_generation#transformers.GenerationMixin.generate) to autoregressively generate text given the input image.

The [NougatImageProcessor](/docs/transformers/v5.0.0/en/model_doc/nougat#transformers.NougatImageProcessor) class is responsible for preprocessing the input image and
[NougatTokenizerFast](/docs/transformers/v5.0.0/en/model_doc/nougat#transformers.NougatTokenizer) decodes the generated target tokens to the target string. The
[NougatProcessor](/docs/transformers/v5.0.0/en/model_doc/nougat#transformers.NougatProcessor) wraps [NougatImageProcessor](/docs/transformers/v5.0.0/en/model_doc/nougat#transformers.NougatImageProcessor) and [NougatTokenizerFast](/docs/transformers/v5.0.0/en/model_doc/nougat#transformers.NougatTokenizer) classes
into a single instance to both extract the input features and decode the predicted token ids.

- Step-by-step PDF transcription

```py
>>> from huggingface_hub import hf_hub_download
>>> import re
>>> from PIL import Image

>>> from transformers import NougatProcessor, VisionEncoderDecoderModel
from accelerate import Accelerator
>>> from datasets import load_dataset
>>> import torch

>>> processor = NougatProcessor.from_pretrained("facebook/nougat-base")
>>> model = VisionEncoderDecoderModel.from_pretrained("facebook/nougat-base")

>>> device = Accelerator().device
>>> model.to(device)
>>> # prepare PDF image for the model
>>> filepath = hf_hub_download(repo_id="hf-internal-testing/fixtures_docvqa", filename="nougat_paper.png", repo_type="dataset")
>>> image = Image.open(filepath)
>>> pixel_values = processor(image, return_tensors="pt").pixel_values

>>> # generate transcription (here we only generate 30 tokens)
>>> outputs = model.generate(
...     pixel_values.to(device),
...     min_length=1,
...     max_new_tokens=30,
...     bad_words_ids=[[processor.tokenizer.unk_token_id]],
... )

>>> sequence = processor.batch_decode(outputs, skip_special_tokens=True)[0]
>>> sequence = processor.post_process_generation(sequence, fix_markdown=False)
>>> # note: we're using repr here such for the sake of printing the \n characters, feel free to just print the sequence
>>> print(repr(sequence))
'\n\n# Nougat: Neural Optical Understanding for Academic Documents\n\n Lukas Blecher\n\nCorrespondence to: lblecher@'
```

See the [model hub](https://huggingface.co/models?filter=nougat) to look for Nougat checkpoints.

The model is identical to [Donut](donut) in terms of architecture.

## NougatImageProcessor[[transformers.NougatImageProcessor]]

#### transformers.NougatImageProcessor[[transformers.NougatImageProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/nougat/image_processing_nougat.py#L67)

Constructs a Nougat image processor.

preprocesstransformers.NougatImageProcessor.preprocesshttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/nougat/image_processing_nougat.py#L381[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor']]"}, {"name": "do_crop_margin", "val": ": bool | None = None"}, {"name": "do_resize", "val": ": bool | None = None"}, {"name": "size", "val": ": dict[str, int] | None = None"}, {"name": "resample", "val": ": PIL.Image.Resampling | None = None"}, {"name": "do_thumbnail", "val": ": bool | None = None"}, {"name": "do_align_long_axis", "val": ": bool | None = None"}, {"name": "do_pad", "val": ": bool | None = None"}, {"name": "do_rescale", "val": ": bool | None = None"}, {"name": "rescale_factor", "val": ": int | float | None = None"}, {"name": "do_normalize", "val": ": bool | None = None"}, {"name": "image_mean", "val": ": float | list[float] | None = None"}, {"name": "image_std", "val": ": float | list[float] | None = None"}, {"name": "return_tensors", "val": ": str | transformers.utils.generic.TensorType | None = None"}, {"name": "data_format", "val": ": transformers.image_utils.ChannelDimension | None = "}, {"name": "input_data_format", "val": ": str | transformers.image_utils.ChannelDimension | None = None"}]- **images** (`ImageInput`) --
  Image to preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255.
- **do_crop_margin** (`bool`, *optional*, defaults to `self.do_crop_margin`) --
  Whether to crop the image margins.
- **do_resize** (`bool`, *optional*, defaults to `self.do_resize`) --
  Whether to resize the image.
- **size** (`dict[str, int]`, *optional*, defaults to `self.size`) --
  Size of the image after resizing. Shortest edge of the image is resized to min(size["height"],
  size["width"]) with the longest edge resized to keep the input aspect ratio.
- **resample** (`int`, *optional*, defaults to `self.resample`) --
  Resampling filter to use if resizing the image. This can be one of the enum `PILImageResampling`. Only
  has an effect if `do_resize` is set to `True`.
- **do_thumbnail** (`bool`, *optional*, defaults to `self.do_thumbnail`) --
  Whether to resize the image using thumbnail method.
- **do_align_long_axis** (`bool`, *optional*, defaults to `self.do_align_long_axis`) --
  Whether to align the long axis of the image with the long axis of `size` by rotating by 90 degrees.
- **do_pad** (`bool`, *optional*, defaults to `self.do_pad`) --
  Whether to pad the images to the largest image size in the batch.
- **do_rescale** (`bool`, *optional*, defaults to `self.do_rescale`) --
  Whether to rescale the image by the specified scale `rescale_factor`.
- **rescale_factor** (`int` or `float`, *optional*, defaults to `self.rescale_factor`) --
  Scale factor to use if rescaling the image.
- **do_normalize** (`bool`, *optional*, defaults to `self.do_normalize`) --
  Whether to normalize the image.
- **image_mean** (`float` or `list[float]`, *optional*, defaults to `self.image_mean`) --
  Image mean to use for normalization.
- **image_std** (`float` or `list[float]`, *optional*, defaults to `self.image_std`) --
  Image standard deviation to use for normalization.
- **return_tensors** (`str` or `TensorType`, *optional*) --
  The type of tensors to return. Can be one of:
  - Unset: Return a list of `np.ndarray`.
  - `TensorType.PYTORCH` or `'pt'`: Return a batch of type `torch.Tensor`.
  - `TensorType.NUMPY` or `'np'`: Return a batch of type `np.ndarray`.
- **data_format** (`ChannelDimension` or `str`, *optional*, defaults to `ChannelDimension.FIRST`) --
  The channel dimension format for the output image. Can be one of:
  - `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
  - `ChannelDimension.LAST`: image in (height, width, num_channels) format.
  - Unset: defaults to the channel dimension format of the input image.
- **input_data_format** (`ChannelDimension` or `str`, *optional*) --
  The channel dimension format for the input image. If unset, the channel dimension format is inferred
  from the input image. Can be one of:
  - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
  - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.
  - `"none"` or `ChannelDimension.NONE`: image in (height, width) format.0

Preprocess an image or batch of images.

**Parameters:**

do_crop_margin (`bool`, *optional*, defaults to `True`) : Whether to crop the image margins.

do_resize (`bool`, *optional*, defaults to `True`) : Whether to resize the image's (height, width) dimensions to the specified `size`. Can be overridden by `do_resize` in the `preprocess` method.

size (`dict[str, int]` *optional*, defaults to `{"height" : 896, "width": 672}`): Size of the image after resizing. Can be overridden by `size` in the `preprocess` method.

resample (`PILImageResampling`, *optional*, defaults to `Resampling.BILINEAR`) : Resampling filter to use if resizing the image. Can be overridden by `resample` in the `preprocess` method.

do_thumbnail (`bool`, *optional*, defaults to `True`) : Whether to resize the image using thumbnail method.

do_align_long_axis (`bool`, *optional*, defaults to `False`) : Whether to align the long axis of the image with the long axis of `size` by rotating by 90 degrees.

do_pad (`bool`, *optional*, defaults to `True`) : Whether to pad the images to the largest image size in the batch.

do_rescale (`bool`, *optional*, defaults to `True`) : Whether to rescale the image by the specified scale `rescale_factor`. Can be overridden by the `do_rescale` parameter in the `preprocess` method.

rescale_factor (`int` or `float`, *optional*, defaults to `1/255`) : Scale factor to use if rescaling the image. Can be overridden by the `rescale_factor` parameter in the `preprocess` method.

do_normalize (`bool`, *optional*, defaults to `True`) : Whether to normalize the image. Can be overridden by `do_normalize` in the `preprocess` method.

image_mean (`float` or `list[float]`, *optional*, defaults to `IMAGENET_DEFAULT_MEAN`) : Mean to use if normalizing the image. This is a float or list of floats the length of the number of channels in the image. Can be overridden by the `image_mean` parameter in the `preprocess` method.

image_std (`float` or `list[float]`, *optional*, defaults to `IMAGENET_DEFAULT_STD`) : Image standard deviation.

## NougatImageProcessorFast[[transformers.NougatImageProcessorFast]]

#### transformers.NougatImageProcessorFast[[transformers.NougatImageProcessorFast]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/nougat/image_processing_nougat_fast.py#L47)

Constructs a fast Nougat image processor.

preprocesstransformers.NougatImageProcessorFast.preprocesshttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/nougat/image_processing_nougat_fast.py#L64[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor']]"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.models.nougat.image_processing_nougat.NougatImageProcessorKwargs]"}]- **images** (`Union[PIL.Image.Image, numpy.ndarray, torch.Tensor, list, list, list]`) --
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
- **do_crop_margin** (`bool`, *optional*, defaults to `True`) --
  Whether to crop the image margins.
- **do_thumbnail** (`bool`, *optional*, defaults to `True`) --
  Whether to resize the image using thumbnail method.
- **do_align_long_axis** (`bool`, *optional*, defaults to `False`) --
  Whether to align the long axis of the image with the long axis of `size` by rotating by 90 degrees.0``- **data** (`dict`) -- Dictionary of lists/arrays/tensors returned by the __call__ method ('pixel_values', etc.).
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

do_crop_margin (`bool`, *optional*, defaults to `True`) : Whether to crop the image margins.

do_thumbnail (`bool`, *optional*, defaults to `True`) : Whether to resize the image using thumbnail method.

do_align_long_axis (`bool`, *optional*, defaults to `False`) : Whether to align the long axis of the image with the long axis of `size` by rotating by 90 degrees.

**Returns:**

````

- **data** (`dict`) -- Dictionary of lists/arrays/tensors returned by the __call__ method ('pixel_values', etc.).
- **tensor_type** (`Union[None, str, TensorType]`, *optional*) -- You can give a tensor_type here to convert the lists of integers in PyTorch/Numpy Tensors at
  initialization.

## NougatTokenizer[[transformers.NougatTokenizer]]

#### transformers.NougatTokenizer[[transformers.NougatTokenizer]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/nougat/tokenization_nougat.py#L347)

Tokenizer for Nougat (backed by HuggingFace tokenizers library).

This tokenizer inherits from [TokenizersBackend](/docs/transformers/v5.0.0/en/main_classes/tokenizer#transformers.TokenizersBackend) which contains most of the main methods. Users should
refer to this superclass for more information regarding those methods. This class mainly adds Nougat-specific
methods for postprocessing the generated text.

correct_tablestransformers.NougatTokenizer.correct_tableshttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/nougat/tokenization_nougat.py#L493[{"name": "generation", "val": ": str"}]- **generation** (str) -- The generated text to be postprocessed.0strThe postprocessed text.

Takes a generated string and fixes tables/tabulars to make them match the markdown format needed.

Example:

```python
correct_tables("\begin{table} \begin{tabular}{l l} & \ \end{tabular} \end{table}")
"\begin{table}
abular}{l l} & \ \end{tabular}
le}"
```

**Parameters:**

vocab_file (`str`, *optional*) : Path to the vocabulary file.

merges_file (`str`, *optional*) : Path to the merges file.

tokenizer_file (`str`, *optional*) : [tokenizers](https://github.com/huggingface/tokenizers) file (generally has a .json extension) that contains everything needed to load the tokenizer. 

clean_up_tokenization_spaces (`str`, *optional*, defaults to `False`) : Whether to cleanup spaces after decoding, cleanup consists in removing potential artifacts like extra spaces. 

unk_token (`str`, *optional*, defaults to `""`) : The unknown token. A token that is not in the vocabulary cannot be converted to an ID and is set to be this token instead. 

bos_token (`str`, *optional*, defaults to `""`) : The beginning of sequence token that was used during pretraining. Can be used a sequence classifier token. 

eos_token (`str`, *optional*, defaults to `""`) : The end of sequence token. 

pad_token (`str`, *optional*, defaults to `""`) : The token used for padding, for example when batching sequences of different lengths. 

vocab (`str`, `dict` or `list`, *optional*) : Custom vocabulary dictionary. If not provided, vocabulary is loaded from vocab_file. 

merges (`str` or `list`, *optional*) : Custom merges list. If not provided, merges are loaded from merges_file.

**Returns:**

`str`

The postprocessed text.
#### post_process_generation[[transformers.NougatTokenizer.post_process_generation]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/nougat/tokenization_nougat.py#L623)

Postprocess a generated text or a list of generated texts.

This function can be used to perform postprocessing on generated text, such as fixing Markdown formatting.

Postprocessing is quite slow so it is recommended to use multiprocessing to speed up the process.

**Parameters:**

generation (Union[str, list[str]]) : The generated text or a list of generated texts.

fix_markdown (`bool`, *optional*, defaults to `True`) : Whether to perform Markdown formatting fixes.

num_workers (`int`, *optional*) : Optional number of workers to pass to leverage multiprocessing (postprocessing several texts in parallel).

**Returns:**

`Union[str, list[str]]`

The postprocessed text or list of postprocessed texts.
#### post_process_single[[transformers.NougatTokenizer.post_process_single]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/nougat/tokenization_nougat.py#L528)

Postprocess a single generated text. Regular expressions used here are taken directly from the Nougat article
authors. These expressions are commented for clarity and tested end-to-end in most cases.

**Parameters:**

generation (str) : The generated text to be postprocessed.

fix_markdown (bool, optional) : Whether to perform Markdown formatting fixes. Default is True.

**Returns:**

`str`

The postprocessed text.
#### remove_hallucinated_references[[transformers.NougatTokenizer.remove_hallucinated_references]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/nougat/tokenization_nougat.py#L463)

Remove hallucinated or missing references from the text.

This function identifies and removes references that are marked as missing or hallucinated from the input text.

**Parameters:**

text (`str`) : The input text containing references.

**Returns:**

``str``

The text with hallucinated references removed.

## NougatTokenizerFast[[transformers.NougatTokenizer]]

#### transformers.NougatTokenizer[[transformers.NougatTokenizer]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/nougat/tokenization_nougat.py#L347)

Tokenizer for Nougat (backed by HuggingFace tokenizers library).

This tokenizer inherits from [TokenizersBackend](/docs/transformers/v5.0.0/en/main_classes/tokenizer#transformers.TokenizersBackend) which contains most of the main methods. Users should
refer to this superclass for more information regarding those methods. This class mainly adds Nougat-specific
methods for postprocessing the generated text.

correct_tablestransformers.NougatTokenizer.correct_tableshttps://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/nougat/tokenization_nougat.py#L493[{"name": "generation", "val": ": str"}]- **generation** (str) -- The generated text to be postprocessed.0strThe postprocessed text.

Takes a generated string and fixes tables/tabulars to make them match the markdown format needed.

Example:

```python
correct_tables("\begin{table} \begin{tabular}{l l} & \ \end{tabular} \end{table}")
"\begin{table}
abular}{l l} & \ \end{tabular}
le}"
```

**Parameters:**

vocab_file (`str`, *optional*) : Path to the vocabulary file.

merges_file (`str`, *optional*) : Path to the merges file.

tokenizer_file (`str`, *optional*) : [tokenizers](https://github.com/huggingface/tokenizers) file (generally has a .json extension) that contains everything needed to load the tokenizer. 

clean_up_tokenization_spaces (`str`, *optional*, defaults to `False`) : Whether to cleanup spaces after decoding, cleanup consists in removing potential artifacts like extra spaces. 

unk_token (`str`, *optional*, defaults to `""`) : The unknown token. A token that is not in the vocabulary cannot be converted to an ID and is set to be this token instead. 

bos_token (`str`, *optional*, defaults to `""`) : The beginning of sequence token that was used during pretraining. Can be used a sequence classifier token. 

eos_token (`str`, *optional*, defaults to `""`) : The end of sequence token. 

pad_token (`str`, *optional*, defaults to `""`) : The token used for padding, for example when batching sequences of different lengths. 

vocab (`str`, `dict` or `list`, *optional*) : Custom vocabulary dictionary. If not provided, vocabulary is loaded from vocab_file. 

merges (`str` or `list`, *optional*) : Custom merges list. If not provided, merges are loaded from merges_file.

**Returns:**

`str`

The postprocessed text.
#### post_process_generation[[transformers.NougatTokenizer.post_process_generation]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/nougat/tokenization_nougat.py#L623)

Postprocess a generated text or a list of generated texts.

This function can be used to perform postprocessing on generated text, such as fixing Markdown formatting.

Postprocessing is quite slow so it is recommended to use multiprocessing to speed up the process.

**Parameters:**

generation (Union[str, list[str]]) : The generated text or a list of generated texts.

fix_markdown (`bool`, *optional*, defaults to `True`) : Whether to perform Markdown formatting fixes.

num_workers (`int`, *optional*) : Optional number of workers to pass to leverage multiprocessing (postprocessing several texts in parallel).

**Returns:**

`Union[str, list[str]]`

The postprocessed text or list of postprocessed texts.
#### post_process_single[[transformers.NougatTokenizer.post_process_single]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/nougat/tokenization_nougat.py#L528)

Postprocess a single generated text. Regular expressions used here are taken directly from the Nougat article
authors. These expressions are commented for clarity and tested end-to-end in most cases.

**Parameters:**

generation (str) : The generated text to be postprocessed.

fix_markdown (bool, optional) : Whether to perform Markdown formatting fixes. Default is True.

**Returns:**

`str`

The postprocessed text.
#### remove_hallucinated_references[[transformers.NougatTokenizer.remove_hallucinated_references]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/nougat/tokenization_nougat.py#L463)

Remove hallucinated or missing references from the text.

This function identifies and removes references that are marked as missing or hallucinated from the input text.

**Parameters:**

text (`str`) : The input text containing references.

**Returns:**

``str``

The text with hallucinated references removed.

## NougatProcessor[[transformers.NougatProcessor]]

#### transformers.NougatProcessor[[transformers.NougatProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/nougat/processing_nougat.py#L27)

Constructs a NougatProcessor which wraps a image processor and a tokenizer into a single processor.

[NougatProcessor](/docs/transformers/v5.0.0/en/model_doc/nougat#transformers.NougatProcessor) offers all the functionalities of [NougatImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/nougat#transformers.NougatImageProcessorFast) and [NougatTokenizer](/docs/transformers/v5.0.0/en/model_doc/nougat#transformers.NougatTokenizer). See the
[~NougatImageProcessorFast](/docs/transformers/v5.0.0/en/model_doc/nougat#transformers.NougatImageProcessorFast) and [~NougatTokenizer](/docs/transformers/v5.0.0/en/model_doc/nougat#transformers.NougatTokenizer) for more information.

__call__transformers.NougatProcessor.__call__https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/nougat/processing_nougat.py#L31[{"name": "images", "val": " = None"}, {"name": "text", "val": " = None"}, {"name": "do_crop_margin", "val": ": bool | None = None"}, {"name": "do_resize", "val": ": bool | None = None"}, {"name": "size", "val": ": dict[str, int] | None = None"}, {"name": "resample", "val": ": PILImageResampling = None"}, {"name": "do_thumbnail", "val": ": bool | None = None"}, {"name": "do_align_long_axis", "val": ": bool | None = None"}, {"name": "do_pad", "val": ": bool | None = None"}, {"name": "do_rescale", "val": ": bool | None = None"}, {"name": "rescale_factor", "val": ": int | float | None = None"}, {"name": "do_normalize", "val": ": bool | None = None"}, {"name": "image_mean", "val": ": float | list[float] | None = None"}, {"name": "image_std", "val": ": float | list[float] | None = None"}, {"name": "data_format", "val": ": typing.Optional[ForwardRef('ChannelDimension')] = 'channels_first'"}, {"name": "input_data_format", "val": ": typing.Union[str, ForwardRef('ChannelDimension'), NoneType] = None"}, {"name": "text_pair", "val": ": str | list[str] | list[list[str]] | None = None"}, {"name": "text_target", "val": ": str | list[str] | list[list[str]] | None = None"}, {"name": "text_pair_target", "val": ": str | list[str] | list[list[str]] | None = None"}, {"name": "add_special_tokens", "val": ": bool = True"}, {"name": "padding", "val": ": bool | str | transformers.utils.generic.PaddingStrategy = False"}, {"name": "truncation", "val": ": bool | str | transformers.tokenization_utils_base.TruncationStrategy | None = None"}, {"name": "max_length", "val": ": int | None = None"}, {"name": "stride", "val": ": int = 0"}, {"name": "is_split_into_words", "val": ": bool = False"}, {"name": "pad_to_multiple_of", "val": ": int | None = None"}, {"name": "return_tensors", "val": ": str | transformers.utils.generic.TensorType | None = None"}, {"name": "return_token_type_ids", "val": ": bool | None = None"}, {"name": "return_attention_mask", "val": ": bool | None = None"}, {"name": "return_overflowing_tokens", "val": ": bool = False"}, {"name": "return_special_tokens_mask", "val": ": bool = False"}, {"name": "return_offsets_mapping", "val": ": bool = False"}, {"name": "return_length", "val": ": bool = False"}, {"name": "verbose", "val": ": bool = True"}]- **images** (``) --
  Image to preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If
  passing in images with pixel values between 0 and 1, set `do_rescale=False`.
- **text** (``) --
  The sequence or batch of sequences to be encoded. Each sequence can be a string or a list of strings
  (pretokenized string). If you pass a pretokenized input, set `is_split_into_words=True` to avoid ambiguity with batched inputs.
- **do_crop_margin** (`bool`, *optional*) --
  Whether to automatically crop white margins from document images. When enabled, the processor detects
  and removes white space around the edges of document pages, which is useful for processing scanned
  documents or PDFs with large margins.
- **do_resize** (`bool`, *optional*) --
  Whether to resize the image.
- **size** (`dict`, *optional*) --
  Describes the maximum input dimensions to the model.
- **resample** (`PILImageResampling`, *optional*) --
  Resampling filter to use if resizing the image. This can be one of the enum `PILImageResampling`. Only
  has an effect if `do_resize` is set to `True`.
- **do_thumbnail** (`bool`, *optional*) --
  Whether to create a thumbnail version of the image. When enabled, a smaller version of the image is
  generated alongside the main processed image, which can be useful for preview or faster processing.
- **do_align_long_axis** (`bool`, *optional*) --
  Whether to automatically align images so that the longer axis is horizontal. When enabled, portrait
  images are rotated to landscape orientation, which is typically better for document processing tasks.
- **do_pad** (`bool`, *optional*) --
  Whether to pad the image. Padding is done either to the largest size in the batch
  or to a fixed square size per image. The exact padding strategy depends on the model.
- **do_rescale** (`bool`, *optional*) --
  Whether to rescale the image.
- **rescale_factor** (`Union[int, float]`, *optional*) --
  Rescale factor to rescale the image by if `do_rescale` is set to `True`.
- **do_normalize** (`bool`, *optional*) --
  Whether to normalize the image.
- **image_mean** (`Union[float, list]`, *optional*) --
  Image mean to use for normalization. Only has an effect if `do_normalize` is set to `True`.
- **image_std** (`Union[float, list]`, *optional*) --
  Image standard deviation to use for normalization. Only has an effect if `do_normalize` is set to
  `True`.
- **data_format** (`ChannelDimension`, *optional*, defaults to `channels_first`) --
  Only `ChannelDimension.FIRST` is supported. Added for compatibility with slow processors.
- **input_data_format** (`Union[str, ChannelDimension]`, *optional*) --
  The channel dimension format for the input image. If unset, the channel dimension format is inferred
  from the input image. Can be one of:
  - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
  - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.
  - `"none"` or `ChannelDimension.NONE`: image in (height, width) format.
- **text_pair** (`str, list[str] or list[int]`, *optional*) --
  Optional second sequence to be encoded. This can be a string, a list of strings (tokenized string using
  the `tokenize` method) or a list of integers (tokenized string ids using the `convert_tokens_to_ids`
  method).
- **text_target** (`str, list[str] or list[list[str]]`, *optional*) --
  The sequence or batch of sequences to be encoded as target texts. Each sequence can be a string or a
  list of strings (pretokenized string). If you pass pretokenized input, set `is_split_into_words=True`
  to avoid ambiguity with batched inputs.
- **text_pair_target** (`str, list[str] or list[list[str]]`, *optional*) --
  The sequence or batch of sequences to be encoded as target texts. Each sequence can be a string or a
  list of strings (pretokenized string). If you pass pretokenized input, set `is_split_into_words=True`
  to avoid ambiguity with batched inputs.
- **add_special_tokens** (`bool`, *optional*, defaults to `True`) --
  Whether or not to add special tokens when encoding the sequences. This will use the underlying
  `PretrainedTokenizerBase.build_inputs_with_special_tokens` function, which defines which tokens are
  automatically added to the input ids. This is useful if you want to add `bos` or `eos` tokens
  automatically.
- **padding** (bool, str or [PaddingStrategy](/docs/transformers/v5.0.0/en/internal/file_utils#transformers.utils.PaddingStrategy), *optional*, defaults to `False`) --
  Activates and controls padding. Accepts the following values:

  - `True` or `'longest'`: Pad to the longest sequence in the batch (or no padding if only a single
    sequence is provided).
  - `'max_length'`: Pad to a maximum length specified with the argument `max_length` or to the maximum
    acceptable input length for the model if that argument is not provided.
  - `False` or `'do_not_pad'` (default): No padding (i.e., can output a batch with sequences of different
    lengths).
- **truncation** (bool, str or [TruncationStrategy](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.tokenization_utils_base.TruncationStrategy), *optional*) --
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
- **stride** (`int`, *optional*, defaults to `0`) --
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
  This is especially useful to enable using Tensor Cores on NVIDIA hardware with compute capability
  `>= 7.5` (Volta).
- **return_tensors** (`Union[str, ~utils.generic.TensorType]`, *optional*) --
  If set, will return tensors of a particular framework. Acceptable values are:

  - `'pt'`: Return PyTorch `torch.Tensor` objects.
  - `'np'`: Return NumPy `np.ndarray` objects.
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

  This is only available on fast tokenizers inheriting from [PreTrainedTokenizerFast](/docs/transformers/v5.0.0/en/main_classes/tokenizer#transformers.TokenizersBackend), if using
  Python's tokenizer, this method will raise `NotImplementedError`.
- **return_length** (`bool`, *optional*, defaults to `False`) --
  Whether or not to return the lengths of the encoded inputs.
- **verbose** (`bool`, *optional*, defaults to `True`) --
  Whether or not to print more information and warnings.0

**Parameters:**

image_processor (`NougatImageProcessorFast`) : The image processor is a required input.

tokenizer (`NougatTokenizer`) : The tokenizer is a required input.
#### from_pretrained[[transformers.NougatProcessor.from_pretrained]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/processing_utils.py#L1364)

Instantiate a processor associated with a pretrained model.

This class method is simply calling the feature extractor
[from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/feature_extractor#transformers.FeatureExtractionMixin.from_pretrained), image processor
[ImageProcessingMixin](/docs/transformers/v5.0.0/en/internal/image_processing_utils#transformers.ImageProcessingMixin) and the tokenizer
`~tokenization_utils_base.PreTrainedTokenizer.from_pretrained` methods. Please refer to the docstrings of the
methods above for more information.

**Parameters:**

pretrained_model_name_or_path (`str` or `os.PathLike`) : This can be either:  - a string, the *model id* of a pretrained feature_extractor hosted inside a model repo on huggingface.co. - a path to a *directory* containing a feature extractor file saved using the [save_pretrained()](/docs/transformers/v5.0.0/en/main_classes/feature_extractor#transformers.FeatureExtractionMixin.save_pretrained) method, e.g., `./my_model_directory/`. - a path or url to a saved feature extractor JSON *file*, e.g., `./my_model_directory/preprocessor_config.json`.

- ****kwargs** : Additional keyword arguments passed along to both [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/feature_extractor#transformers.FeatureExtractionMixin.from_pretrained) and `~tokenization_utils_base.PreTrainedTokenizer.from_pretrained`.
#### save_pretrained[[transformers.NougatProcessor.save_pretrained]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/processing_utils.py#L792)

Saves the attributes of this processor (feature extractor, tokenizer...) in the specified directory so that it
can be reloaded using the [from_pretrained()](/docs/transformers/v5.0.0/en/main_classes/processors#transformers.ProcessorMixin.from_pretrained) method.

This class method is simply calling [save_pretrained()](/docs/transformers/v5.0.0/en/main_classes/feature_extractor#transformers.FeatureExtractionMixin.save_pretrained) and
[save_pretrained()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.save_pretrained). Please refer to the docstrings of the
methods above for more information.

**Parameters:**

save_directory (`str` or `os.PathLike`) : Directory where the feature extractor JSON file and the tokenizer files will be saved (directory will be created if it does not exist).

push_to_hub (`bool`, *optional*, defaults to `False`) : Whether or not to push your model to the Hugging Face model hub after saving it. You can specify the repository you want to push to with `repo_id` (will default to the name of `save_directory` in your namespace).

kwargs (`dict[str, Any]`, *optional*) : Additional key word arguments passed along to the [push_to_hub()](/docs/transformers/v5.0.0/en/main_classes/model#transformers.utils.PushToHubMixin.push_to_hub) method.
#### batch_decode[[transformers.NougatProcessor.batch_decode]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/processing_utils.py#L1593)

This method forwards all its arguments to PreTrainedTokenizer's [batch_decode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.batch_decode). Please
refer to the docstring of this method for more information.
#### decode[[transformers.NougatProcessor.decode]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/processing_utils.py#L1602)

This method forwards all its arguments to PreTrainedTokenizer's [decode()](/docs/transformers/v5.0.0/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.decode). Please refer to
the docstring of this method for more information.
#### post_process_generation[[transformers.NougatProcessor.post_process_generation]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/nougat/processing_nougat.py#L134)

This method forwards all its arguments to NougatTokenizer's `~PreTrainedTokenizer.post_process_generation`.
Please refer to the docstring of this method for more information.

