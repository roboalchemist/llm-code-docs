# Source: https://huggingface.co/docs/transformers/v5.0.0rc1/model_doc/pixtral.md

# Pixtral

[Pixtral](https://huggingface.co/papers/2410.07073) is a multimodal model trained to understand natural images and documents. It accepts images in their natural resolution and aspect ratio without resizing or padding due to it's 2D RoPE embeddings. In addition, Pixtral has a long 128K token context window for processing a large number of images. Pixtral couples a 400M vision encoder with a 12B Mistral Nemo decoder.

 Pixtral architecture. Taken from the blog post. 

You can find all the original Pixtral checkpoints under the [Mistral AI](https://huggingface.co/mistralai/models?search=pixtral) organization.

> [!TIP]
> This model was contributed by [amyeroberts](https://huggingface.co/amyeroberts) and [ArthurZ](https://huggingface.co/ArthurZ).
> Click on the Pixtral models in the right sidebar for more examples of how to apply Pixtral to different vision and language tasks.

```python
import torch
from transformers import AutoProcessor, LlavaForConditionalGeneration

model_id = "mistral-community/pixtral-12b"
model = LlavaForConditionalGeneration.from_pretrained(model_id, dtype="auto", device_map="auto")
processor = AutoProcessor.from_pretrained(model_id)

url_dog = "https://picsum.photos/id/237/200/300"
url_mountain = "https://picsum.photos/seed/picsum/200/300"

chat = [
    {
      "role": "user", "content": [
        {"type": "text", "content": "Can this animal"}, 
        {"type": "image", "url": url_dog}, 
        {"type": "text", "content": "live here?"}, 
        {"type": "image", "url" : url_mountain}
      ]
    }
]

inputs = processor.apply_chat_template(chat, add_generation_prompt=True, tokenize=True, return_dict=True, return_tensors"pt").to(model.device)
generate_ids = model.generate(**inputs, max_new_tokens=500)
output = processor.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
```

Quantization reduces the memory burden of large models by representing the weights in a lower precision. Refer to the [Quantization](../quantization/overview) overview for more available quantization backends.

The example below uses [bitsandbytes](../quantization/bitsandbytes) to quantize the model to 4-bits.

```python
import torch
import requests
from PIL import Image
from transformers import AutoProcessor, LlavaForConditionalGeneration, BitsAndBytesConfig

model_id = "mistral-community/pixtral-12b"

quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)

model = LlavaForConditionalGeneration.from_pretrained(
    model_id,
    quantization_config=quantization_config,
    device_map="auto"
)
processor = AutoProcessor.from_pretrained(model_id)

dog_url = "https://picsum.photos/id/237/200/300"
mountain_url = "https://picsum.photos/seed/picsum/200/300"
dog_image = Image.open(requests.get(dog_url, stream=True).raw)
mountain_image = Image.open(requests.get(mountain_url, stream=True).raw)

chat = [
    {
      "role": "user", "content": [
        {"type": "text", "text": "Can this animal"},
        {"type": "image"},
        {"type": "text", "text": "live here?"},
        {"type": "image"}
      ]
    }
]

prompt = processor.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)
inputs = processor(text=prompt, images=[dog_image, mountain_image], return_tensors="pt")

inputs["pixel_values"] = inputs["pixel_values"].to(model.dtype)
inputs = {k: v.to(model.device) for k, v in inputs.items()}

generate_ids = model.generate(**inputs, max_new_tokens=100)
output = processor.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)
print(output)
```

## Notes

- Pixtral uses [PixtralVisionModel](/docs/transformers/v5.0.0rc1/en/model_doc/pixtral#transformers.PixtralVisionModel) as the vision encoder and [MistralForCausalLM](/docs/transformers/v5.0.0rc1/en/model_doc/mistral#transformers.MistralForCausalLM)  for its language decoder.
- The model internally replaces `[IMG]` token placeholders with image embeddings.

    ```py
    "[INST][IMG]\nWhat are the things I should be cautious about when I visit this place?[/INST]"
    ```

    The `[IMG]` tokens are replaced with a number of `[IMG]` tokens that depend on the height and width of each image. Each row of the image is separated by a `[IMG_BREAK]` token and each image is separated by a `[IMG_END]` token. Use the `~Processor.apply_chat_template` method to handle these tokens for you.

## PixtralVisionConfig[[transformers.PixtralVisionConfig]]

#### transformers.PixtralVisionConfig[[transformers.PixtralVisionConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/pixtral/configuration_pixtral.py#L26)

This is the configuration class to store the configuration of a [PixtralVisionModel](/docs/transformers/v5.0.0rc1/en/model_doc/pixtral#transformers.PixtralVisionModel). It is used to instantiate an
Pixtral vision encoder according to the specified arguments, defining the model architecture. Instantiating a configuration
with the defaults will yield a similar configuration to the vision encoder used by Pixtral-12B.

e.g. [pixtral-hf/pixtral-9b](https://huggingface.co/pixtral-hf/pixtral-9b)

Configuration objects inherit from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) and can be used to control the model outputs. Read the
documentation from [PreTrainedConfig](/docs/transformers/v5.0.0rc1/en/main_classes/configuration#transformers.PreTrainedConfig) for more information.

Example:

```python
>>> from transformers import PixtralVisionModel, PixtralVisionConfig

>>> # Initializing a Pixtral-12B style configuration
>>> config = PixtralVisionConfig()

>>> # Initializing a model (with randomly initialized weights) from the configuration
>>> model = PixtralVisionModel(configuration)

>>> # Accessing the model configuration
>>> configuration = model.config
```

**Parameters:**

hidden_size (`int`, *optional*, defaults to 1024) : Dimension of the hidden representations.

intermediate_size (`int`, *optional*, defaults to 4096) : Dimension of the MLP representations.

num_hidden_layers (`int`, *optional*, defaults to 24) : Number of hidden layers in the Transformer encoder.

num_attention_heads (`int`, *optional*, defaults to 16) : Number of attention heads in the Transformer encoder.

num_channels (`int`, *optional*, defaults to 3) : Number of input channels in the input images.

image_size (`int`, *optional*, defaults to 1024) : Max dimension of the input images.

patch_size (`int`, *optional*, defaults to 16) : Size of the image patches.

hidden_act (`str`, *optional*, defaults to `"gelu"`) : Activation function used in the hidden layers.

attention_dropout (`float`, *optional*, defaults to 0.0) : Dropout probability for the attention layers.

rope_parameters (`RopeParameters`, *optional*) : The RopeParameters

initializer_range (`float`, *optional*, defaults to 0.02) : The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

## MistralCommonBackend[[transformers.MistralCommonBackend]]

#### transformers.MistralCommonBackend[[transformers.MistralCommonBackend]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/tokenization_mistral_common.py#L153)

Class to wrap `mistral-common` tokenizers.

`mistral-common` is the official tokenizer library for Mistral AI models. To use it, you need to install it with:

```bash
pip install transformers[mistral-common]
```

Otherwise the tokenizer falls back to the Transformers implementation of the tokenizer.

For more info on `mistral-common`, see [mistral-common](https://github.com/mistralai/mistral-common).

This class is a wrapper around a `mistral_common.tokens.tokenizers.mistral.MistralTokenizer`.
It provides a Hugging Face compatible interface to tokenize using the official mistral-common tokenizer.

Supports the following methods from the `PreTrainedTokenizerBase` class:

- [get_vocab()](/docs/transformers/v5.0.0rc1/en/model_doc/mistral3#transformers.MistralCommonBackend.get_vocab): Returns the vocabulary as a dictionary of token to index.
  This is a lossy conversion for Tekkenizer as some decoding errors are collapsed into the same token.
- [encode()](/docs/transformers/v5.0.0rc1/en/model_doc/mistral3#transformers.MistralCommonBackend.encode): Encode a string to a list of integers.
- [decode()](/docs/transformers/v5.0.0rc1/en/model_doc/mistral3#transformers.MistralCommonBackend.decode): Decode a list of integers to a string.
- [batch_decode()](/docs/transformers/v5.0.0rc1/en/model_doc/mistral3#transformers.MistralCommonBackend.batch_decode): Decode a batch of list of integers to a list of strings.
- [convert_tokens_to_ids()](/docs/transformers/v5.0.0rc1/en/model_doc/mistral3#transformers.MistralCommonBackend.convert_tokens_to_ids): Convert a list of tokens to a list of integers.
- [convert_ids_to_tokens()](/docs/transformers/v5.0.0rc1/en/model_doc/mistral3#transformers.MistralCommonBackend.convert_ids_to_tokens): Convert a list of integers to a list of tokens.
- [tokenize()](/docs/transformers/v5.0.0rc1/en/model_doc/mistral3#transformers.MistralCommonBackend.tokenize): Tokenize a string.
- [get_special_tokens_mask()](/docs/transformers/v5.0.0rc1/en/model_doc/mistral3#transformers.MistralCommonBackend.get_special_tokens_mask): Get the special tokens mask for a list of tokens.
- [prepare_for_model()](/docs/transformers/v5.0.0rc1/en/model_doc/mistral3#transformers.MistralCommonBackend.prepare_for_model): Prepare a list of inputs for the model.
- [pad()](/docs/transformers/v5.0.0rc1/en/model_doc/mistral3#transformers.MistralCommonBackend.pad): Pad a list of inputs to the same length.
- [truncate_sequences()](/docs/transformers/v5.0.0rc1/en/model_doc/mistral3#transformers.MistralCommonBackend.truncate_sequences): Truncate a list of sequences to the same length.
- [apply_chat_template()](/docs/transformers/v5.0.0rc1/en/model_doc/mistral3#transformers.MistralCommonBackend.apply_chat_template): Apply a chat template to a list of messages.
- `__call__()`: Tokenize a string or a list of strings.
- [from_pretrained()](/docs/transformers/v5.0.0rc1/en/model_doc/mistral3#transformers.MistralCommonBackend.from_pretrained): Download and cache a pretrained tokenizer from the Hugging Face model hub or local directory.
- [save_pretrained()](/docs/transformers/v5.0.0rc1/en/model_doc/mistral3#transformers.MistralCommonBackend.save_pretrained): Save a tokenizer to a directory, so it can be reloaded using the `from_pretrained` class method.
- [push_to_hub()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.utils.PushToHubMixin.push_to_hub): Upload tokenizer to the Hugging Face model hub.

Here are the key differences with the `PreTrainedTokenizerBase` class:

- Pair of sequences are not supported. The signature have been kept for compatibility but all arguments related to pair of sequences are ignored. The return values of pairs are returned as `None`.
- The `is_split_into_words` argument is not supported.
- The `return_token_type_ids` argument is not supported.
- It is not possible to add new tokens to the tokenizer. Also the special tokens are handled differently from Transformers. In `mistral-common`, special tokens are never encoded directly. This means that: `tokenizer.encode("")` will not return the ID of the `` token. Instead, it will return a list of IDs corresponding to the tokenization of the string `""`. For more information, see the [mistral-common documentation](https://mistralai.github.io/mistral-common/usage/tokenizers/#special-tokens).

If you have suggestions to improve this class, please open an issue on the [mistral-common GitHub repository](https://github.com/mistralai/mistral-common/issues) if it is related to the tokenizer or on the [Transformers GitHub repository](https://github.com/huggingface/transformers/issues) if it is related to the Hugging Face interface.

apply_chat_templatetransformers.MistralCommonBackend.apply_chat_templatehttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/tokenization_mistral_common.py#L1450[{"name": "conversation", "val": ": list[dict[str, str]] | list[list[dict[str, str]]]"}, {"name": "tools", "val": ": list[dict | collections.abc.Callable] | None = None"}, {"name": "add_generation_prompt", "val": ": bool = False"}, {"name": "continue_final_message", "val": ": bool = False"}, {"name": "tokenize", "val": ": bool = True"}, {"name": "padding", "val": ": bool | str | transformers.utils.generic.PaddingStrategy = False"}, {"name": "truncation", "val": ": bool = False"}, {"name": "max_length", "val": ": int | None = None"}, {"name": "return_tensors", "val": ": str | transformers.utils.generic.TensorType | None = None"}, {"name": "return_dict", "val": ": bool = True"}, {"name": "**kwargs", "val": ""}]- **conversation** (Union[List[Dict[str, str]], List[List[Dict[str, str]]]]) -- A list of dicts
  with "role" and "content" keys, representing the chat history so far.
- **tools** (`List[Union[Dict, Callable]]`, *optional*) --
  A list of tools (callable functions) that will be accessible to the model. If the template does not
  support function calling, this argument will have no effect. Each tool should be passed as a JSON Schema,
  giving the name, description and argument types for the tool. See our
  [chat templating guide](https://huggingface.co/docs/transformers/main/en/chat_templating#automated-function-conversion-for-tool-use)
  for more information.
- **add_generation_prompt** (`bool`, *optional*) --
  This argument is a no-op for `MistralCommonBackend`. However it cannot be used at the same time as `continue_final_message` to keep the API consistent and
  if any conversation ends with an assistant message, it will raise an error. In such case, use `continue_final_message` instead.
- **continue_final_message** (bool, *optional*) --
  If this is set, the chat will be formatted so that the final
  message in the chat is open-ended, without any EOS tokens. The model will continue this message
  rather than starting a new one. This allows you to "prefill" part of
  the model's response for it. Cannot be used at the same time as `add_generation_prompt`.
- **tokenize** (`bool`, defaults to `True`) --
  Whether to tokenize the output. If `False`, the output will be a string.
- **padding** (`bool`, `str` or [PaddingStrategy](/docs/transformers/v5.0.0rc1/en/internal/file_utils#transformers.utils.PaddingStrategy), *optional*, defaults to `False`) --
  Select a strategy to pad the returned sequences (according to the model's padding side and padding
  index) among:

  - `True` or `'longest'`: Pad to the longest sequence in the batch (or no padding if only a single
    sequence if provided).
  - `'max_length'`: Pad to a maximum length specified with the argument `max_length` or to the maximum
    acceptable input length for the model if that argument is not provided.
  - `False` or `'do_not_pad'` (default): No padding (i.e., can output a batch with sequences of different
    lengths).
- **truncation** (`bool`, defaults to `False`) --
  Whether to truncate sequences at the maximum length. Has no effect if tokenize is `False`.
- **max_length** (`int`, *optional*) --
  Maximum length (in tokens) to use for padding or truncation. Has no effect if tokenize is `False`. If
  not specified, the tokenizer's `max_length` attribute will be used as a default.
- **return_tensors** (`str` or [TensorType](/docs/transformers/v5.0.0rc1/en/internal/file_utils#transformers.TensorType), *optional*) --
  If set, will return tensors of a particular framework. Has no effect if tokenize is `False`. Acceptable
  values are:
  - `'pt'`: Return PyTorch `torch.Tensor` objects.
- **return_dict** (`bool`, defaults to `False`) --
  Whether to return a dictionary with named outputs. Has no effect if tokenize is `False`.
  If at least one conversation contains an image, its pixel values will be returned in the `pixel_values` key.
- **kwargs** (additional keyword arguments, *optional*) --
  Not supported by `MistralCommonBackend.apply_chat_template`.
  Will raise an error if used.0`Union[str, list[int], list[str], list[list[int]], BatchEncoding]`A list of token ids representing the tokenized chat so far, including control
tokens. This output is ready to pass to the model, either directly or via methods like `generate()`.

Converts a list of dictionaries with `"role"` and `"content"` keys to a list of token
ids.

**Parameters:**

conversation (Union[List[Dict[str, str]], List[List[Dict[str, str]]]]) : A list of dicts with "role" and "content" keys, representing the chat history so far.

tools (`List[Union[Dict, Callable]]`, *optional*) : A list of tools (callable functions) that will be accessible to the model. If the template does not support function calling, this argument will have no effect. Each tool should be passed as a JSON Schema, giving the name, description and argument types for the tool. See our [chat templating guide](https://huggingface.co/docs/transformers/main/en/chat_templating#automated-function-conversion-for-tool-use) for more information.

add_generation_prompt (`bool`, *optional*) : This argument is a no-op for `MistralCommonBackend`. However it cannot be used at the same time as `continue_final_message` to keep the API consistent and if any conversation ends with an assistant message, it will raise an error. In such case, use `continue_final_message` instead.

continue_final_message (bool, *optional*) : If this is set, the chat will be formatted so that the final message in the chat is open-ended, without any EOS tokens. The model will continue this message rather than starting a new one. This allows you to "prefill" part of the model's response for it. Cannot be used at the same time as `add_generation_prompt`.

tokenize (`bool`, defaults to `True`) : Whether to tokenize the output. If `False`, the output will be a string.

padding (`bool`, `str` or [PaddingStrategy](/docs/transformers/v5.0.0rc1/en/internal/file_utils#transformers.utils.PaddingStrategy), *optional*, defaults to `False`) : Select a strategy to pad the returned sequences (according to the model's padding side and padding index) among:  - `True` or `'longest'`: Pad to the longest sequence in the batch (or no padding if only a single sequence if provided). - `'max_length'`: Pad to a maximum length specified with the argument `max_length` or to the maximum acceptable input length for the model if that argument is not provided. - `False` or `'do_not_pad'` (default): No padding (i.e., can output a batch with sequences of different lengths).

truncation (`bool`, defaults to `False`) : Whether to truncate sequences at the maximum length. Has no effect if tokenize is `False`.

max_length (`int`, *optional*) : Maximum length (in tokens) to use for padding or truncation. Has no effect if tokenize is `False`. If not specified, the tokenizer's `max_length` attribute will be used as a default.

return_tensors (`str` or [TensorType](/docs/transformers/v5.0.0rc1/en/internal/file_utils#transformers.TensorType), *optional*) : If set, will return tensors of a particular framework. Has no effect if tokenize is `False`. Acceptable values are: - `'pt'`: Return PyTorch `torch.Tensor` objects.

return_dict (`bool`, defaults to `False`) : Whether to return a dictionary with named outputs. Has no effect if tokenize is `False`. If at least one conversation contains an image, its pixel values will be returned in the `pixel_values` key.

kwargs (additional keyword arguments, *optional*) : Not supported by `MistralCommonBackend.apply_chat_template`. Will raise an error if used.

**Returns:**

``Union[str, list[int], list[str], list[list[int]], BatchEncoding]``

A list of token ids representing the tokenized chat so far, including control
tokens. This output is ready to pass to the model, either directly or via methods like `generate()`.
#### batch_decode[[transformers.MistralCommonBackend.batch_decode]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/tokenization_mistral_common.py#L527)

Convert a list of lists of token ids into a list of strings by calling decode.

This method is provided for backwards compatibility. The `decode` method now handles batched input natively,
so you can use `decode` directly instead of `batch_decode`.

**Parameters:**

sequences (`Union[list[int], list[list[int]], np.ndarray, torch.Tensor]`) : List of tokenized input ids. Can be obtained using the `__call__` method.

skip_special_tokens (`bool`, *optional*, defaults to `False`) : Whether or not to remove special tokens in the decoding.

clean_up_tokenization_spaces (`bool`, *optional*) : Whether or not to clean up the tokenization spaces. If `None`, will default to `self.clean_up_tokenization_spaces`.

kwargs (additional keyword arguments, *optional*) : Not supported by `MistralCommonBackend.batch_decode`. Will raise an error if used.

**Returns:**

``list[str]``

The list of decoded sentences.
#### clean_up_tokenization[[transformers.MistralCommonBackend.clean_up_tokenization]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/tokenization_mistral_common.py#L281)

Clean up a list of simple English tokenization artifacts like spaces before punctuation.
#### convert_ids_to_tokens[[transformers.MistralCommonBackend.convert_ids_to_tokens]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/tokenization_mistral_common.py#L619)

Converts a single index or a sequence of indices in a token or a sequence of tokens, using the vocabulary and
added tokens.

**Parameters:**

ids (`int` or `list[int]`) : The token id (or token ids) to convert to tokens.

skip_special_tokens (`bool`, *optional*, defaults to `False`) : Whether or not to remove special tokens in the decoding.

**Returns:**

``str` or `list[str]``

The decoded token(s).
#### convert_tokens_to_ids[[transformers.MistralCommonBackend.convert_tokens_to_ids]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/tokenization_mistral_common.py#L677)

Converts a token string (or a sequence of tokens) in a single integer id (or a sequence of ids), using the
vocabulary.

**Parameters:**

tokens (`str` or `list[str]`) : One or several token(s) to convert to token id(s).

**Returns:**

``int` or `list[int]``

The token id or list of token ids.
#### decode[[transformers.MistralCommonBackend.decode]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/tokenization_mistral_common.py#L481)

Converts a sequence of ids in a string, using the tokenizer and vocabulary with options to remove special
tokens and clean up tokenization spaces.

**Parameters:**

token_ids (`Union[int, list[int], list[list[int]], np.ndarray, torch.Tensor]`) : A single sequence or a batch (list of sequences) of tokenized input ids. Can be obtained using the `__call__` method.

skip_special_tokens (`bool`, *optional*, defaults to `False`) : Whether or not to remove special tokens in the decoding.

clean_up_tokenization_spaces (`bool`, *optional*) : Whether or not to clean up the tokenization spaces. If `None`, will default to `self.clean_up_tokenization_spaces`.

kwargs (additional keyword arguments, *optional*) : Not supported by `MistralCommonBackend.decode`. Will raise an error if used.

**Returns:**

``Union[str, list[str]]``

The decoded string for a single sequence, or a list of decoded strings for a
batch of sequences.
#### encode[[transformers.MistralCommonBackend.encode]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/tokenization_mistral_common.py#L414)

Converts a string to a sequence of ids (integer), using the tokenizer and vocabulary.

**Parameters:**

text (`str` or `list[int]`) : The first sequence to be encoded. This can be a string or a list of integers (tokenized string ids).

text_pair (`None`, *optional*) : Not supported by `MistralCommonBackend.encode`. Kept to match `PreTrainedTokenizerBase.encode` signature. 

add_special_tokens (`bool`, *optional*, defaults to `True`) : Whether or not to add special tokens when encoding the sequences. This will use the underlying `PretrainedTokenizerBase.build_inputs_with_special_tokens` function, which defines which tokens are automatically added to the input ids. This is useful if you want to add `bos` or `eos` tokens automatically. When Tokenizer is loading with `finetuning` mode it adds both `bos` and `eos`. Else, for "test" mode it only adds `bos`.

padding (`bool`, `str` or [PaddingStrategy](/docs/transformers/v5.0.0rc1/en/internal/file_utils#transformers.utils.PaddingStrategy), *optional*, defaults to `False`) : Activates and controls padding. Accepts the following values:  - `True` or `'longest'`: Pad to the longest sequence in the batch (or no padding if only a single sequence is provided). - `'max_length'`: Pad to a maximum length specified with the argument `max_length` or to the maximum acceptable input length for the model if that argument is not provided. - `False` or `'do_not_pad'` (default): No padding (i.e., can output a batch with sequences of different lengths).

truncation (`bool`, `str` or [TruncationStrategy](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.tokenization_utils_base.TruncationStrategy), *optional*, defaults to `False`) : Activates and controls truncation. Accepts the following values:  - `True` or `'longest_first'`: Truncate to a maximum length specified with the argument `max_length` or to the maximum acceptable input length for the model if that argument is not provided. - `False` or `'do_not_truncate'` (default): No truncation (i.e., can output batch with sequence lengths greater than the model maximum admissible input size).

max_length (`int`, *optional*) : Controls the maximum length to use by one of the truncation/padding parameters.  If left unset or set to `None`, this will use the predefined model maximum length if a maximum length is required by one of the truncation/padding parameters. If the model has no specific maximum input length (like XLNet) truncation/padding to a maximum length will be deactivated.

stride (`int`, *optional*, defaults to 0) : If set to a number along with `max_length`, the overflowing tokens returned when `return_overflowing_tokens=True` will contain some tokens from the end of the truncated sequence returned to provide some overlap between truncated and overflowing sequences. The value of this argument defines the number of overlapping tokens.

pad_to_multiple_of (`int`, *optional*) : If set will pad the sequence to a multiple of the provided value. Requires `padding` to be activated. This is especially useful to enable the use of Tensor Cores on NVIDIA hardware with compute capability `>= 7.5` (Volta).

padding_side (`str`, *optional*) : The side on which the model should have padding applied. Should be selected between ['right', 'left']. Default value is picked from the class attribute of the same name.

return_tensors (`str` or [TensorType](/docs/transformers/v5.0.0rc1/en/internal/file_utils#transformers.TensorType), *optional*) : If set, will return tensors instead of list of python integers. Acceptable values are:  - `'pt'`: Return PyTorch `torch.Tensor` objects. 

- ****kwargs** : Not supported by `MistralCommonBackend.encode`. Will raise an error if used.

**Returns:**

``list[int]`, `torch.Tensor``

The tokenized ids of the text.
#### from_pretrained[[transformers.MistralCommonBackend.from_pretrained]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/tokenization_mistral_common.py#L1779)

Instantiate a `MistralCommonBackend` from a predefined
tokenizer.

**Parameters:**

pretrained_model_name_or_path (`str` or `os.PathLike`) : Can be either:  - A string, the *model id* of a predefined tokenizer hosted inside a model repo on huggingface.co. - A path to a *directory* containing the tokenizer config, for instance saved using the `MistralCommonBackend.tokenization_mistral_common.save_pretrained` method, e.g., `./my_model_directory/`.

mode (`Union[str, ValidationMode]`, *optional*, defaults to `ValidationMode.test`) : Validation mode for the `MistralTokenizer` tokenizer. Possible values are: - `"finetuning"` or `ValidationMode.finetuning`: The finetuning mode. - `"test"` or `ValidationMode.test`: The test mode. It changes how the tokenizer validates the input and prepare the request to the model.

cache_dir (`str` or `os.PathLike`, *optional*) : Path to a directory in which a downloaded predefined tokenizer vocabulary files should be cached if the standard cache should not be used.

force_download (`bool`, *optional*, defaults to `False`) : Whether or not to force the (re-)download the vocabulary files and override the cached versions if they exist.

token (`str` or *bool*, *optional*) : The token to use as HTTP bearer authorization for remote files. If `True`, will use the token generated when running `hf auth login` (stored in `~/.huggingface`).

local_files_only (`bool`, *optional*, defaults to `False`) : Whether or not to only rely on local files and not to attempt to download any files.

revision (`str`, *optional*, defaults to `"main"`) : The specific model version to use. It can be a branch name, a tag name, or a commit id, since we use a git-based system for storing models and other artifacts on huggingface.co, so `revision` can be any identifier allowed by git.

max_length (`int`, *optional*) : Controls the maximum length to use by one of the truncation/padding parameters.  If left unset or set to `None`, this will use the predefined model maximum length if a maximum length is required by one of the truncation/padding parameters. If the model has no specific maximum input length (like XLNet) truncation/padding to a maximum length will be deactivated.

padding_side (`str`, *optional*, defaults to `"left"`) : The side on which the model should have padding applied. Should be selected between ['right', 'left']. Default value is picked from the class attribute of the same name.

truncation_side (`str`, *optional*, defaults to `"right"`) : The side on which the model should have truncation applied. Should be selected between ['right', 'left'].

model_input_names (`List[string]`, *optional*) : The list of inputs accepted by the forward pass of the model (like `"token_type_ids"` or `"attention_mask"`). Default value is picked from the class attribute of the same name.

clean_up_tokenization_spaces (`bool`, *optional*, defaults to `False`) : Whether or not the model should cleanup the spaces that were added when splitting the input text during the tokenization process.

kwargs (additional keyword arguments, *optional*) : Not supported by `MistralCommonBackend.from_pretrained`. Will raise an error if used.
#### get_special_tokens_mask[[transformers.MistralCommonBackend.get_special_tokens_mask]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/tokenization_mistral_common.py#L833)

Retrieves sequence ids from a token list that has no special tokens added. This method is called when adding
special tokens using the tokenizer `prepare_for_model` or `encode_plus` methods.

**Parameters:**

token_ids_0 (`list[int]`) : List of ids of the sequence.

token_ids_1 (`list[int]`, *optional*) : Not supported by `MistralCommonBackend`. Kept to match the interface of `PreTrainedTokenizerBase`.

already_has_special_tokens (`bool`, *optional*, defaults to `False`) : Whether or not the token list is already formatted with special tokens for the model.

**Returns:**

`A list of integers in the range [0, 1]`

1 for a special token, 0 for a sequence token.
#### get_vocab[[transformers.MistralCommonBackend.get_vocab]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/tokenization_mistral_common.py#L388)

Returns the vocabulary as a dictionary of token to index.

This is a lossy conversion. There may be multiple token ids that decode to the same
string due to partial UTF-8 byte sequences being converted to �.

**Returns:**

``Dict[str, int]``

The vocabulary.
#### pad[[transformers.MistralCommonBackend.pad]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/tokenization_mistral_common.py#L1213)

Pad a single encoded input or a batch of encoded inputs up to predefined length or to the max sequence length
in the batch.

Padding side (left/right) padding token ids are defined at the tokenizer level (with `self.padding_side`,
`self.pad_token_id`).

If the `encoded_inputs` passed are dictionary of numpy arrays, PyTorch tensors, the
result will use the same type unless you provide a different tensor type with `return_tensors`. In the case of
PyTorch tensors, you will lose the specific device of your tensors however.

**Parameters:**

encoded_inputs ([BatchEncoding](/docs/transformers/v5.0.0rc1/en/main_classes/tokenizer#transformers.BatchEncoding), list of [BatchEncoding](/docs/transformers/v5.0.0rc1/en/main_classes/tokenizer#transformers.BatchEncoding), `Dict[str, list[int]]`, `Dict[str, list[list[int]]` or `List[Dict[str, list[int]]]`) : Tokenized inputs. Can represent one input ([BatchEncoding](/docs/transformers/v5.0.0rc1/en/main_classes/tokenizer#transformers.BatchEncoding) or `Dict[str, list[int]]`) or a batch of tokenized inputs (list of [BatchEncoding](/docs/transformers/v5.0.0rc1/en/main_classes/tokenizer#transformers.BatchEncoding), *Dict[str, list[list[int]]]* or *List[Dict[str, list[int]]]*) so you can use this method during preprocessing as well as in a PyTorch Dataloader collate function.  Instead of `list[int]` you can have tensors (numpy arrays, PyTorch tensors), see the note above for the return type.

padding (`bool`, `str` or [PaddingStrategy](/docs/transformers/v5.0.0rc1/en/internal/file_utils#transformers.utils.PaddingStrategy), *optional*, defaults to `True`) : Select a strategy to pad the returned sequences (according to the model's padding side and padding index) among:  - `True` or `'longest'` (default): Pad to the longest sequence in the batch (or no padding if only a single sequence if provided). - `'max_length'`: Pad to a maximum length specified with the argument `max_length` or to the maximum acceptable input length for the model if that argument is not provided. - `False` or `'do_not_pad'`: No padding (i.e., can output a batch with sequences of different lengths).

max_length (`int`, *optional*) : Maximum length of the returned list and optionally padding length (see above).

pad_to_multiple_of (`int`, *optional*) : If set will pad the sequence to a multiple of the provided value.  This is especially useful to enable the use of Tensor Cores on NVIDIA hardware with compute capability `>= 7.5` (Volta).

padding_side (`str`, *optional*) : The side on which the model should have padding applied. Should be selected between ['right', 'left']. Default value is picked from the class attribute of the same name.

return_attention_mask (`bool`, *optional*) : Whether to return the attention mask. If left to the default, will return the attention mask according to the specific tokenizer's default, defined by the `return_outputs` attribute.  [What are attention masks?](../glossary#attention-mask)

return_tensors (`str` or [TensorType](/docs/transformers/v5.0.0rc1/en/internal/file_utils#transformers.TensorType), *optional*) : If set, will return tensors instead of list of python integers. Acceptable values are:  - `'pt'`: Return PyTorch `torch.Tensor` objects. - `'np'`: Return Numpy `np.ndarray` objects.

verbose (`bool`, *optional*, defaults to `True`) : Whether or not to print more information and warnings.
#### prepare_for_model[[transformers.MistralCommonBackend.prepare_for_model]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/tokenization_mistral_common.py#L927)

Prepares a sequence of input id so that it can be used by the model. It
adds special tokens, truncates sequences if overflowing while taking into account the special tokens and
manages a moving window (with user defined stride) for overflowing tokens.

**Parameters:**

ids (`list[int]`) : Tokenized input ids of the first sequence.

pair_ids (`None`, *optional*) : Not supported by `MistralCommonBackend`. Kept to match the interface of `PreTrainedTokenizerBase`. 

add_special_tokens (`bool`, *optional*, defaults to `True`) : Whether or not to add special tokens when encoding the sequences. This will use the underlying `PretrainedTokenizerBase.build_inputs_with_special_tokens` function, which defines which tokens are automatically added to the input ids. This is useful if you want to add `bos` or `eos` tokens automatically. When Tokenizer is loading with `finetuning` mode it adds both `bos` and `eos`. Else, for "test" mode it only adds `bos`.

padding (`bool`, `str` or [PaddingStrategy](/docs/transformers/v5.0.0rc1/en/internal/file_utils#transformers.utils.PaddingStrategy), *optional*, defaults to `False`) : Activates and controls padding. Accepts the following values:  - `True` or `'longest'`: Pad to the longest sequence in the batch (or no padding if only a single sequence is provided). - `'max_length'`: Pad to a maximum length specified with the argument `max_length` or to the maximum acceptable input length for the model if that argument is not provided. - `False` or `'do_not_pad'` (default): No padding (i.e., can output a batch with sequences of different lengths).

truncation (`bool`, `str` or [TruncationStrategy](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.tokenization_utils_base.TruncationStrategy), *optional*, defaults to `False`) : Activates and controls truncation. Accepts the following values:  - `True` or `'longest_first'`: Truncate to a maximum length specified with the argument `max_length` or to the maximum acceptable input length for the model if that argument is not provided. - `False` or `'do_not_truncate'` (default): No truncation (i.e., can output batch with sequence lengths greater than the model maximum admissible input size).

max_length (`int`, *optional*) : Controls the maximum length to use by one of the truncation/padding parameters.  If left unset or set to `None`, this will use the predefined model maximum length if a maximum length is required by one of the truncation/padding parameters. If the model has no specific maximum input length (like XLNet) truncation/padding to a maximum length will be deactivated.

stride (`int`, *optional*, defaults to 0) : If set to a number along with `max_length`, the overflowing tokens returned when `return_overflowing_tokens=True` will contain some tokens from the end of the truncated sequence returned to provide some overlap between truncated and overflowing sequences. The value of this argument defines the number of overlapping tokens.

pad_to_multiple_of (`int`, *optional*) : If set will pad the sequence to a multiple of the provided value. Requires `padding` to be activated. This is especially useful to enable the use of Tensor Cores on NVIDIA hardware with compute capability `>= 7.5` (Volta).

padding_side (`str`, *optional*) : The side on which the model should have padding applied. Should be selected between ['right', 'left']. Default value is picked from the class attribute of the same name.

return_tensors (`str` or [TensorType](/docs/transformers/v5.0.0rc1/en/internal/file_utils#transformers.TensorType), *optional*) : If set, will return tensors instead of list of python integers. Acceptable values are:  - `'pt'`: Return PyTorch `torch.Tensor` objects. 

return_attention_mask (`bool`, *optional*) : Whether to return the attention mask. If left to the default, will return the attention mask according to the specific tokenizer's default, defined by the `return_outputs` attribute.  [What are attention masks?](../glossary#attention-mask)

return_overflowing_tokens (`bool`, *optional*, defaults to `False`) : Whether or not to return overflowing token sequences. If a pair of sequences of input ids (or a batch of pairs) is provided with `truncation_strategy = longest_first` or `True`, an error is raised instead of returning overflowing tokens.

return_special_tokens_mask (`bool`, *optional*, defaults to `False`) : Whether or not to return special tokens mask information.

return_length  (`bool`, *optional*, defaults to `False`) : Whether or not to return the lengths of the encoded inputs.

verbose (`bool`, *optional*, defaults to `True`) : Whether or not to print more information and warnings.

- ****kwargs** : passed to the `self.tokenize()` method

**Returns:**

`[BatchEncoding](/docs/transformers/v5.0.0rc1/en/main_classes/tokenizer#transformers.BatchEncoding)`

A [BatchEncoding](/docs/transformers/v5.0.0rc1/en/main_classes/tokenizer#transformers.BatchEncoding) with the following fields:

- **input_ids** -- List of token ids to be fed to a model.

  [What are input IDs?](../glossary#input-ids)

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
#### save_pretrained[[transformers.MistralCommonBackend.save_pretrained]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/tokenization_mistral_common.py#L1911)

Save the full tokenizer state.

This method make sure the full tokenizer can then be re-loaded using the
`~MistralCommonBackend.tokenization_mistral_common.from_pretrained` class method.

**Parameters:**

save_directory (`str` or `os.PathLike`) : The path to a directory where the tokenizer will be saved.

push_to_hub (`bool`, *optional*, defaults to `False`) : Whether or not to push your model to the Hugging Face model hub after saving it. You can specify the repository you want to push to with `repo_id` (will default to the name of `save_directory` in your namespace).

token (`str` or *bool*, *optional*, defaults to `None`) : The token to use to push to the model hub. If `True`, will use the token in the `HF_TOKEN` environment variable.

commit_message (`str`, *optional*) : The commit message to use when pushing to the hub.

repo_id (`str`, *optional*) : The name of the repository to which push to the Hub.

private (`bool`, *optional*) : Whether the model repository is private or not.

kwargs (`Dict[str, Any]`, *optional*) : Not supported by `MistralCommonBackend.save_pretrained`. Will raise an error if used.

**Returns:**

`A tuple of `str``

The files saved.
#### tokenize[[transformers.MistralCommonBackend.tokenize]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/tokenization_mistral_common.py#L711)

Converts a string into a sequence of tokens, using the tokenizer.

Split in words for word-based vocabulary or sub-words for sub-word-based vocabularies.

**Parameters:**

text (`str`) : The sequence to be encoded.

- ****kwargs** (additional keyword arguments) : Not supported by `MistralCommonBackend.tokenize`. Will raise an error if used.

**Returns:**

``list[str]``

The list of tokens.
#### truncate_sequences[[transformers.MistralCommonBackend.truncate_sequences]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/tokenization_mistral_common.py#L1375)

Truncates a sequence pair in-place following the strategy.

**Parameters:**

ids (`list[int]`) : Tokenized input ids. Can be obtained from a string by chaining the `tokenize` and `convert_tokens_to_ids` methods.

pair_ids (`None`, *optional*) : Not supported by `MistralCommonBackend`. Kept to match the signature of `PreTrainedTokenizerBase.truncate_sequences`.

num_tokens_to_remove (`int`, *optional*, defaults to 0) : Number of tokens to remove using the truncation strategy.

truncation_strategy (`str` or [TruncationStrategy](/docs/transformers/v5.0.0rc1/en/internal/tokenization_utils#transformers.tokenization_utils_base.TruncationStrategy), *optional*, defaults to `'longest_first'`) : The strategy to follow for truncation. Can be:  - `'longest_first'`: Truncate to a maximum length specified with the argument `max_length` or to the maximum acceptable input length for the model if that argument is not provided. - `'do_not_truncate'` (default): No truncation (i.e., can output batch with sequence lengths greater than the model maximum admissible input size).

stride (`int`, *optional*, defaults to 0) : If set to a positive number, the overflowing tokens returned will contain some tokens from the main sequence returned. The value of this argument defines the number of additional tokens.

**Returns:**

``Tuple[list[int], None, list[int]]``

The truncated `ids` and the list of
overflowing tokens. `None` is returned to match Transformers signature.

## PixtralVisionModel[[transformers.PixtralVisionModel]]

#### transformers.PixtralVisionModel[[transformers.PixtralVisionModel]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/pixtral/modeling_pixtral.py#L463)

The bare Pixtral Model outputting raw hidden-states without any specific head on top.

This model inherits from [PreTrainedModel](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel). Check the superclass documentation for the generic methods the
library implements for all its model (such as downloading or saving, resizing the input embeddings, pruning heads
etc.)

This model is also a PyTorch [torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) subclass.
Use it as a regular PyTorch Module and refer to the PyTorch documentation for all matter related to general usage
and behavior.

forwardtransformers.PixtralVisionModel.forwardhttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/pixtral/modeling_pixtral.py#L486[{"name": "pixel_values", "val": ": Tensor"}, {"name": "image_sizes", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "output_hidden_states", "val": ": typing.Optional[bool] = None"}, {"name": "output_attentions", "val": ": typing.Optional[bool] = None"}, {"name": "return_dict", "val": ": typing.Optional[bool] = None"}, {"name": "*args", "val": ""}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.modeling_flash_attention_utils.FlashAttentionKwargs]"}]- **pixel_values** (`torch.Tensor` of shape `(batch_size, num_channels, image_size, image_size)`) --
  The tensors corresponding to the input images. Pixel values can be obtained using
  [PixtralImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/pixtral#transformers.PixtralImageProcessor). See [PixtralImageProcessor.__call__()](/docs/transformers/v5.0.0rc1/en/model_doc/fuyu#transformers.FuyuImageProcessor.__call__) for details ([PixtralProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/pixtral#transformers.PixtralProcessor) uses
  [PixtralImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/pixtral#transformers.PixtralImageProcessor) for processing images).
- **image_sizes** (`torch.Tensor` of shape `(batch_size, 2)`, *optional*) --
  The sizes of the images in the batch, being (height, width) for each image.
- **output_hidden_states** (`bool`, *optional*) --
  Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
  more detail.
- **output_attentions** (`bool`, *optional*) --
  Whether or not to return the attentions tensors of all attention layers. See `attentions` under returned
  tensors for more detail.
- **return_dict** (`bool`, *optional*) --
  Whether or not to return a [ModelOutput](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.utils.ModelOutput) instead of a plain tuple.0[transformers.modeling_outputs.BaseModelOutput](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutput) or `tuple(torch.FloatTensor)`A [transformers.modeling_outputs.BaseModelOutput](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutput) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([PixtralVisionConfig](/docs/transformers/v5.0.0rc1/en/model_doc/pixtral#transformers.PixtralVisionConfig)) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.
The [PixtralVisionModel](/docs/transformers/v5.0.0rc1/en/model_doc/pixtral#transformers.PixtralVisionModel) forward method, overrides the `__call__` special method.

Although the recipe for forward pass needs to be defined within this function, one should call the `Module`
instance afterwards instead of this since the former takes care of running the pre and post processing steps while
the latter silently ignores them.

**Parameters:**

config ([PixtralVisionModel](/docs/transformers/v5.0.0rc1/en/model_doc/pixtral#transformers.PixtralVisionModel)) : Model configuration class with all the parameters of the model. Initializing with a config file does not load the weights associated with the model, only the configuration. Check out the [from_pretrained()](/docs/transformers/v5.0.0rc1/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) method to load the model weights.

**Returns:**

`[transformers.modeling_outputs.BaseModelOutput](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutput) or `tuple(torch.FloatTensor)``

A [transformers.modeling_outputs.BaseModelOutput](/docs/transformers/v5.0.0rc1/en/main_classes/output#transformers.modeling_outputs.BaseModelOutput) or a tuple of
`torch.FloatTensor` (if `return_dict=False` is passed or when `config.return_dict=False`) comprising various
elements depending on the configuration ([PixtralVisionConfig](/docs/transformers/v5.0.0rc1/en/model_doc/pixtral#transformers.PixtralVisionConfig)) and inputs.

- **last_hidden_state** (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`) -- Sequence of hidden-states at the output of the last layer of the model.
- **hidden_states** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`) -- Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
  one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

  Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
- **attentions** (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`) -- Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
  sequence_length)`.

  Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
  heads.

## PixtralImageProcessor[[transformers.PixtralImageProcessor]]

#### transformers.PixtralImageProcessor[[transformers.PixtralImageProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/pixtral/image_processing_pixtral.py#L149)

Constructs a Pixtral image processor.

preprocesstransformers.PixtralImageProcessor.preprocesshttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/pixtral/image_processing_pixtral.py#L330[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor']]"}, {"name": "do_resize", "val": ": typing.Optional[bool] = None"}, {"name": "size", "val": ": typing.Optional[dict[str, int]] = None"}, {"name": "patch_size", "val": ": typing.Optional[dict[str, int]] = None"}, {"name": "resample", "val": ": typing.Optional[PIL.Image.Resampling] = None"}, {"name": "do_rescale", "val": ": typing.Optional[bool] = None"}, {"name": "rescale_factor", "val": ": typing.Optional[float] = None"}, {"name": "do_normalize", "val": ": typing.Optional[bool] = None"}, {"name": "image_mean", "val": ": typing.Union[float, list[float], NoneType] = None"}, {"name": "image_std", "val": ": typing.Union[float, list[float], NoneType] = None"}, {"name": "do_convert_rgb", "val": ": typing.Optional[bool] = None"}, {"name": "return_tensors", "val": ": typing.Union[str, transformers.utils.generic.TensorType, NoneType] = None"}, {"name": "data_format", "val": ": typing.Optional[transformers.image_utils.ChannelDimension] = "}, {"name": "input_data_format", "val": ": typing.Union[str, transformers.image_utils.ChannelDimension, NoneType] = None"}, {"name": "**kwargs", "val": ""}]- **images** (`ImageInput`) --
  Image to preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If
  passing in images with pixel values between 0 and 1, set `do_rescale=False`.
- **do_resize** (`bool`, *optional*, defaults to `self.do_resize`) --
  Whether to resize the image.
- **size** (`dict[str, int]`, *optional*, defaults to `self.size`) --
  Describes the maximum input dimensions to the model.
- **patch_size** (`dict[str, int]`, *optional*, defaults to `self.patch_size`) --
  Patch size in the model. Used to calculate the image after resizing.
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

Preprocess an image or batch of images.

**Parameters:**

do_resize (`bool`, *optional*, defaults to `True`) : Whether to resize the image's (height, width) dimensions to the specified `size`. Can be overridden by `do_resize` in the `preprocess` method.

size (`dict[str, int]` *optional*, defaults to `{"longest_edge" : 1024}`): Size of the maximum dimension of either the height or width dimension of the image. Used to control how images are resized. If either the height or width are greater than `size["longest_edge"]` then both the height and width are rescaled by `height / ratio`, `width /ratio` where `ratio = max(height / longest_edge, width / longest_edge)`

patch_size (`dict[str, int]` *optional*, defaults to `{"height" : 16, "width": 16}`): Size of the patches in the model, used to calculate the output image size. Can be overridden by `patch_size` in the `preprocess` method.

resample (`PILImageResampling`, *optional*, defaults to `Resampling.BICUBIC`) : Resampling filter to use if resizing the image. Can be overridden by `resample` in the `preprocess` method.

do_rescale (`bool`, *optional*, defaults to `True`) : Whether to rescale the image by the specified scale `rescale_factor`. Can be overridden by `do_rescale` in the `preprocess` method.

rescale_factor (`int` or `float`, *optional*, defaults to `1/255`) : Scale factor to use if rescaling the image. Can be overridden by `rescale_factor` in the `preprocess` method.

do_normalize (`bool`, *optional*, defaults to `True`) : Whether to normalize the image. Can be overridden by `do_normalize` in the `preprocess` method.

image_mean (`float` or `list[float]`, *optional*, defaults to `[0.48145466, 0.4578275, 0.40821073]`) : Mean to use if normalizing the image. This is a float or list of floats the length of the number of channels in the image. Can be overridden by the `image_mean` parameter in the `preprocess` method.

image_std (`float` or `list[float]`, *optional*, defaults to `[0.26862954, 0.26130258, 0.27577711]`) : Standard deviation to use if normalizing the image. This is a float or list of floats the length of the number of channels in the image. Can be overridden by the `image_std` parameter in the `preprocess` method. Can be overridden by the `image_std` parameter in the `preprocess` method.

do_convert_rgb (`bool`, *optional*, defaults to `True`) : Whether to convert the image to RGB.

## PixtralImageProcessorFast[[transformers.PixtralImageProcessorFast]]

#### transformers.PixtralImageProcessorFast[[transformers.PixtralImageProcessorFast]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/pixtral/image_processing_pixtral_fast.py#L42)

Constructs a fast Pixtral image processor.

preprocesstransformers.PixtralImageProcessorFast.preprocesshttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/pixtral/image_processing_pixtral_fast.py#L60[{"name": "images", "val": ": typing.Union[ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor']]"}, {"name": "**kwargs", "val": ": typing_extensions.Unpack[transformers.models.pixtral.image_processing_pixtral.PixtralImageProcessorKwargs]"}]- **images** (`Union[PIL.Image.Image, numpy.ndarray, torch.Tensor, list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor']]`) --
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
- **patch_size** (`Union[dict[str, int], int]` *optional*, defaults to `{"height" -- 16, "width": 16}`):
  Size of the patches in the model, used to calculate the output image size. Can be overridden by `patch_size` in the `preprocess` method.0``- **data** (`dict`) -- Dictionary of lists/arrays/tensors returned by the __call__ method ('pixel_values', etc.).
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

patch_size (`Union[dict[str, int], int]` *optional*, defaults to `{"height" : 16, "width": 16}`): Size of the patches in the model, used to calculate the output image size. Can be overridden by `patch_size` in the `preprocess` method.

**Returns:**

````

- **data** (`dict`) -- Dictionary of lists/arrays/tensors returned by the __call__ method ('pixel_values', etc.).
- **tensor_type** (`Union[None, str, TensorType]`, *optional*) -- You can give a tensor_type here to convert the lists of integers in PyTorch/Numpy Tensors at
  initialization.

## PixtralProcessor[[transformers.PixtralProcessor]]

#### transformers.PixtralProcessor[[transformers.PixtralProcessor]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/models/pixtral/processing_pixtral.py#L64)

Constructs a Pixtral processor which wraps a Pixtral image processor and a Pixtral tokenizer into a single processor.

[PixtralProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/pixtral#transformers.PixtralProcessor) offers all the functionalities of [CLIPImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/clip#transformers.CLIPImageProcessor) and [LlamaTokenizerFast](/docs/transformers/v5.0.0rc1/en/model_doc/llama2#transformers.LlamaTokenizer). See the
`__call__()` and [decode()](/docs/transformers/v5.0.0rc1/en/main_classes/processors#transformers.ProcessorMixin.decode) for more information.

**Parameters:**

image_processor ([PixtralImageProcessor](/docs/transformers/v5.0.0rc1/en/model_doc/pixtral#transformers.PixtralImageProcessor), *optional*) : The image processor is a required input.

tokenizer ([LlamaTokenizerFast](/docs/transformers/v5.0.0rc1/en/model_doc/llama2#transformers.LlamaTokenizer), *optional*) : The tokenizer is a required input.

patch_size (`int`, *optional*, defaults to 16) : Patch size from the vision tower.

spatial_merge_size (`int`, *optional*, defaults to 1) : The downsampling factor for the spatial merge operation.

chat_template (`str`, *optional*) : A Jinja template which will be used to convert lists of messages in a chat into a tokenizable string.

image_token (`str`, *optional*, defaults to `"[IMG]"`) : Special token used to denote image location.

image_break_token (`str`, *optional*, defaults to `"[IMG_BREAK]"`) : Special token used to denote the end of a line of pixels in an image.

image_end_token (`str`, *optional*, defaults to `"[IMG_END]"`) : Special token used to denote the end of an image input.

